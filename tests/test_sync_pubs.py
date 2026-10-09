import tempfile
import unittest
from pathlib import Path

import bibtexparser

from scripts.sync_pubs import build_publication_record, generate_hugo_bundle


class PublicationExportTests(unittest.TestCase):
    def test_bibtex_and_biblatex_article_metadata(self):
        exports = (
            'year = {2026}, month = oct, journal = {Scientific Data}',
            'date = {2026-10-05}, journaltitle = {Scientific Data}',
        )
        for fields in exports:
            with self.subTest(fields=fields):
                entry = bibtexparser.loads(
                    '@article{forest2026, title = {Forest cover}, '
                    'author = {Peng, Xue Li}, ' + fields + '}'
                ).entries[0]
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


if __name__ == '__main__':
    unittest.main()
