import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import yaml

from scripts.sync_en import FRONT_MATTER, localize_links, protect, render_outputs, sync, translate_missing, validate_translation


class EnglishSyncTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.body = '\n{{< section_nav >}}\n\n研究介绍 [链接](/zh/project/demo/)\n\n```python\nprint("保留中文代码")\n```\n'
        self.translation = '\n{{< section_nav >}}\n\nResearch introduction [Link](/zh/project/demo/)\n\n```python\nprint("保留中文代码")\n```\n'
        self.cache = {
            '研究': 'Research', '实验项目': 'Demo Project', '负责人': 'Project Lead',
            '龙腾飞': 'Tengfei Long', '项目': 'Projects',
            '中文论文': 'A Chinese-language Paper', '遥感学报': 'Journal of Remote Sensing',
            self.body: self.translation,
        }
        self.write('content/zh/project/demo/index.md', '---\ntitle: 研究\ndate: 2026-10-09\nfeatured: true\n---\n' + self.body)
        self.write('data/projects/zh.yaml', 'entries:\n- title: 实验项目\n  start: "2026-01"\n  end: "2027-12"\n  funding: 123.45万元\n  members: [龙腾飞]\n  role: 负责人\n  page: /zh/project/demo/\n')
        self.write('config/_default/menus.zh.yaml', 'main:\n- name: 项目\n  url: /zh/project/demo/\n  weight: 40\n')
        self.write('data/publications/generated.json', json.dumps({'entries': [{
            'citekey': 'paper2026', 'title': '中文论文', 'authors': ['龙腾飞'],
            'authors_text': '龙腾飞', 'venue': '遥感学报', 'keywords': [], 'badges': [],
            'year': '2026', 'doi': '10.1000/example', 'url': 'https://example.com/paper',
        }]}, ensure_ascii=False))

    def write(self, filename, text):
        path = self.root / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')

    def test_offline_sync_preserves_metadata_code_and_updates_links(self):
        sync(self.root, self.cache)
        page = (self.root / 'content/en/project/demo/index.md').read_text(encoding='utf-8')
        match = FRONT_MATTER.fullmatch(page)
        metadata = yaml.safe_load(match[1])
        self.assertEqual(metadata['title'], 'Research')
        self.assertEqual(str(metadata['date']), '2026-10-09')
        self.assertTrue(metadata['featured'])
        self.assertIn('[Link](/en/project/demo/)', match[2])
        self.assertIn('print("保留中文代码")', match[2])
        project = yaml.safe_load((self.root / 'data/projects/en.yaml').read_text(encoding='utf-8'))['entries'][0]
        self.assertEqual(project['members'], ['Tengfei Long'])
        self.assertEqual(project['funding'], 'CNY 1,234,500')
        self.assertEqual(project['start'], '2026-01')
        self.assertEqual(project['page'], '/en/project/demo/')
        publication = json.loads((self.root / 'data/publications/en.json').read_text(encoding='utf-8'))['entries'][0]
        self.assertEqual(publication['title'], 'A Chinese-language Paper')
        self.assertEqual(publication['authors_text'], 'Tengfei Long')
        self.assertEqual(publication['doi'], '10.1000/example')
        self.assertEqual(publication['url'], 'https://example.com/paper')
        before = {p: p.stat().st_mtime_ns for p in (self.root / 'content/en').rglob('*.md')}
        sync(self.root, self.cache)
        self.assertEqual(before, {p: p.stat().st_mtime_ns for p in before})
        sync(self.root, self.cache, check=True)

    def test_missing_translation_leaves_existing_output_unchanged(self):
        sync(self.root, self.cache)
        page = self.root / 'content/en/project/demo/index.md'
        original = page.read_bytes()
        source = self.root / 'content/zh/project/demo/index.md'
        source.write_text(source.read_text(encoding='utf-8').replace('title: 研究', 'title: 新研究'), encoding='utf-8')
        _, missing = render_outputs(self.root, self.cache)
        self.assertEqual(missing, ['新研究'])
        with self.assertRaisesRegex(ValueError, 'Missing 1 translations'):
            sync(self.root, self.cache)
        self.assertEqual(page.read_bytes(), original)

    def test_html_images_and_downloads_use_shared_chinese_resources(self):
        self.write('content/zh/project/demo/image.jpg', 'image')
        self.write('content/zh/project/demo/report.pdf', 'document')
        source = self.root / 'content/zh/project/demo/index.md'
        source.write_text(source.read_text(encoding='utf-8') +
                          '\n<figure>\n  <a href="report.pdf">PDF</a>\n    <img src="image.jpg" alt="Demo">\n</figure>\n'
                          '\n```html\n<img src="image.jpg">\n```\n', encoding='utf-8')
        self.cache[FRONT_MATTER.fullmatch(source.read_text(encoding='utf-8'))[2]] = self.translation + \
            '\n<figure>\n  <a href="report.pdf">PDF</a>\n    <img src="image.jpg" alt="Demo">\n</figure>\n' \
            '\n```html\n<img src="image.jpg">\n```\n'
        sync(self.root, self.cache)
        page = (self.root / 'content/en/project/demo/index.md').read_text(encoding='utf-8')
        self.assertIn('src="/zh/project/demo/image.jpg"', page)
        self.assertIn('href="/zh/project/demo/report.pdf"', page)
        self.assertIn('```html\n<img src="image.jpg">\n```', page)
        self.assertEqual(localize_links('[Link](/zh/project/) https://example.com/zh/'),
                         '[Link](/en/project/) https://example.com/zh/')

    def test_source_removal_deletes_only_generated_pages(self):
        sync(self.root, self.cache)
        self.write('content/en/independent/index.md', 'An independent English page.')
        (self.root / 'content/zh/project/demo/index.md').unlink()
        sync(self.root, self.cache)
        self.assertFalse((self.root / 'content/en/project/demo/index.md').exists())
        self.assertTrue((self.root / 'content/en/independent/index.md').exists())

    def test_invalid_manifest_cannot_delete_other_files(self):
        self.write('data/translations/generated_en.json', json.dumps({'files': ['../outside.md']}))
        with self.assertRaisesRegex(ValueError, 'Invalid generated page path'):
            sync(self.root, self.cache)

    def test_translation_preserves_urls_shortcodes_code_and_math(self):
        for source, translation in (
            ('中文 [链接](https://example.com/a)', 'English [Link](https://wrong.example/a)'),
            ('中文 {{< section_nav >}}', 'English {{< wrong >}}'),
            ('中文 `x["中文"]`', 'English `x["English"]`'),
            ('中文\n\n    print("中文")\n', 'English\n\n    print("English")\n'),
            ('中文 $x^2$ &deg;', 'English $x^3$ &deg;'),
        ):
            with self.subTest(source=source), self.assertRaises(ValueError):
                validate_translation(source, translation)
        validate_translation('- 地址：`北京市海淀区`', '- Address: `Haidian District, Beijing`')

    def test_api_restores_placeholders_and_rejects_changed_tokens(self):
        source = '中文 [链接](https://example.com/a)'
        client = Mock()
        client.responses.create.return_value = SimpleNamespace(
            status='completed', output_text=json.dumps({'translations': ['English [Link](__IRIS_KEEP_0__)']})
        )
        cache = {}
        translate_missing([source], cache, client, 'test-model')
        self.assertEqual(cache[source], 'English [Link](https://example.com/a)')
        self.assertEqual(json.loads(client.responses.create.call_args.kwargs['input']), [protect(source)[0]])
        self.assertFalse(client.responses.create.call_args.kwargs['store'])
        client.responses.create.return_value.output_text = json.dumps({'translations': ['English [Link](__IRIS_KEEP_9__)']})
        with self.assertRaisesRegex(ValueError, 'protected placeholders'):
            translate_missing([source], {}, client, 'test-model')


if __name__ == '__main__':
    unittest.main()
