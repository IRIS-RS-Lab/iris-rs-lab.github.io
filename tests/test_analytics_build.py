"""Compile real analytics partials without requiring the external Hugo theme."""
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which('hugo'), 'Hugo is not installed')
class AnalyticsTemplateTests(unittest.TestCase):
    def render(self, measurement_id='', environment='production', service_id=''):
        with tempfile.TemporaryDirectory(prefix='iris-analytics-') as temp:
            root = Path(temp)
            shutil.copytree(ROOT / 'layouts/partials/analytics', root / 'layouts/partials/analytics')
            shutil.copytree(ROOT / 'assets/js', root / 'assets/js')
            (root / 'layouts/index.html').write_text(
                '<!doctype html><html><head>{{ partial "analytics/google_analytics" . }}'
                '</head><body>{{ partial "analytics/consent" . }}</body></html>', encoding='utf-8')
            config = {
                'baseURL': 'https://example.org/', 'defaultContentLanguage': 'zh',
                'languages': {'zh': {'weight': 1}, 'en': {'weight': 2}},
                'params': {'marketing': {'analytics': {'google_analytics': measurement_id}}},
                'services': {'googleAnalytics': {'ID': service_id}},
            }
            (root / 'hugo.json').write_text(json.dumps(config), encoding='utf-8')
            result = subprocess.run(['hugo', '--source', str(root), '--environment', environment],
                                    capture_output=True, text=True, encoding='utf-8', errors='replace')
            html = {}
            if result.returncode == 0:
                html = {lang: (root / 'public' / prefix / 'index.html').read_text(encoding='utf-8')
                        for lang, prefix in [('zh', ''), ('en', 'en')]}
            return result, html

    def test_empty_id_renders_no_analytics_or_consent(self):
        result, html = self.render()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn('iris-analytics', html['zh'])

    def test_production_renders_one_loader_and_localized_consent(self):
        result, html = self.render('G-TEST123')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for page in html.values():
            self.assertEqual(page.count('id="iris-analytics"'), 1)
            self.assertEqual(page.count('id="iris-analytics-consent"'), 1)
            self.assertIn('data-measurement-id="G-TEST123"', page)
            self.assertIn('integrity="sha256-', page)
            self.assertNotIn('src="https://www.googletagmanager.com', page)
        self.assertIn('同意访问统计', html['zh'])
        self.assertIn('Accept analytics', html['en'])

    def test_development_never_tracks(self):
        result, html = self.render('G-TEST123', 'development')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn('iris-analytics', html['zh'])

    def test_standard_hugo_service_setting_is_supported(self):
        result, html = self.render(service_id='G-SERVICE123')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('data-measurement-id="G-SERVICE123"', html['en'])

    def test_invalid_id_fails_production_build(self):
        result, _ = self.render('UA-123-1')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('requires a GA4 measurement ID', result.stdout + result.stderr)
