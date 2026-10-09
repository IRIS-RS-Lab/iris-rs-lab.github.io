# Contributing to IRIS Website

## Quick rules
- One content item = one folder (Page Bundle): `index.md` + images/PDFs in the same folder.
- Keep **large files** (datasets, >25MB PDFs, models) on Zenodo/GitHub Releases/OSS; this site stores only thumbnails and links.
- Every change goes through a PR if possible.

## Add a News post
Copy `TEMPLATES/post.zh.md` -> `content/zh/post/YYYY-MM-DD-your-slug/index.md`.
Generate its English counterpart with the sync described below.

## Add a Project
Copy `TEMPLATES/project.zh.md` to `content/zh/project/<slug>/index.md`.
Put `featured.jpg` next to it and generate its English counterpart with the sync below.

## Sync the English website
Chinese pages in `content/zh/`, the project list in `data/projects/zh.yaml`,
publication metadata in `data/publications/generated.json`, and navigation in
`config/_default/menus.zh.yaml` are the sources for generated English content.
Edit the Chinese source first. English-only pages without a Chinese counterpart are preserved.
Hugo shares resources between matching language bundles, so images do not need to be copied.
The sync points raw HTML image and download links to the shared Chinese bundle resources.

Install dependencies and regenerate English content locally:
```shell
python -m pip install -r requirements-dev.txt -r requirements-translation.txt
python scripts/sync_pubs.py --skip-bundles
python scripts/sync_en.py
python scripts/sync_en.py --check
```

Existing translations are stored in `data/translations/en.json`. They work without an API key.
To correct an English translation, edit its value in this cache and rerun the sync.
English pages with a matching Chinese source, `data/projects/en.yaml`,
`data/publications/en.json`, and `config/_default/menus.en.yaml` are generated outputs.
Do not edit these outputs directly. `data/translations/generated_en.json` tracks ownership,
so removing a Chinese page removes only its generated English counterpart.
Publication display text is translated; the original BibTeX and citation links are retained.

For new or changed Chinese text, set `OPENAI_API_KEY` in your local environment and run:
```shell
python scripts/sync_en.py --translate
```
The script uses OpenAI Responses with Structured Outputs, translates only uncached text,
and protects links, HTML tags, Hugo shortcodes, code, and formulas. Set
`OPENAI_TRANSLATION_MODEL` to choose a model; the default is `gpt-4.1-mini`.
Review newly generated translations before committing local changes.

For automatic deployment, configure the repository's Actions secret `OPENAI_API_KEY`.
The optional Actions variable `OPENAI_TRANSLATION_MODEL` selects the model.
GitHub Actions restores cached translations, generates English content before the Hugo build,
and saves the cache only after a successful sync. If the key is missing or translation fails,
the build uses the existing English files. Chinese updates can still be published.
Generated English files are included in the deployed site; the workflow does not commit them back to Git.
Pushing changes to `.github/workflows/hugo.yaml` requires a token with the `workflow` scope,
or equivalent permission to update Actions workflow files.

## Add a Publication detail page
Publication detail pages are **optional**.
- Default behavior: keep `external_link: "#no-detail"` so list titles are non-clickable.
- To enable a detail page for a selected paper: remove `external_link` from that paper's `index.md`, then add your full content/figures.
- Optional assets: `featured.jpg`, `cite.bib`, PDF links.

## Update publications list (Zotero)
Export BibTeX or BibLaTeX to `publications.bib` (repo root).
Run `pip install -r requirements-dev.txt`, then `python scripts/sync_pubs.py --skip-bundles`.
Commit both `publications.bib` and `data/publications/generated.json`.
GitHub Actions repeats the sync before building and deploying the site.
To create optional detail-page stubs without overwriting existing pages, omit `--skip-bundles`.
