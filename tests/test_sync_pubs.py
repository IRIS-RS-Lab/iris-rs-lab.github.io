import tempfile
import unittest
from pathlib import Path

from scripts.sync_pubs import build_publication_record, generate_hugo_bundle, parse_bib_entries


class PublicationExportTests(unittest.TestCase):
    def test_bibtex_and_biblatex_article_metadata(self):
        exports = (
            'year = {2026}, month = oct, journal = {Scientific Data}',
            'date = {2026-10-05}, journaltitle = {Scientific Data}',
        )
        for fields in exports:
            with self.subTest(fields=fields):
                entry = parse_bib_entries(
                    '@article{forest2026, title = {Forest cover}, '
                    'author = {Peng, Xue Li}, ' + fields + '}'
                )[0]
                record = build_publication_record(entry)
                self.assertEqual(record['venue'], 'Scientific Data')
                self.assertEqual(record['year'], '2026')
                self.assertEqual(record['month'], '10')
                self.assertEqual(record['sort_date'], '2026-10-01')

                with tempfile.TemporaryDirectory() as directory:
                    target = Path(directory)
                    generate_hugo_bundle(entry, target, 'en')
                    content = (target / 'forest2026' / 'index.md').read_text(
                        encoding='utf-8'
                    )
                    self.assertIn('date: 2026-10-01', content)
                    self.assertIn('Published in Scientific Data.', content)

    def test_nonstandard_web_snapshot_is_skipped(self):
        entries = parse_bib_entries(
            '@online{snapshot, title = {Forest cover}, '
            'url = {https://example.com/forest}}\n'
            '@article{forest2026, title = {Forest cover}, '
            'date = {2026}, author = {Peng, Xue Li}, '
            'journaltitle = {Scientific Data}}'
        )
        self.assertEqual([entry['ID'] for entry in entries], ['forest2026'])


if __name__ == '__main__':
    unittest.main()
