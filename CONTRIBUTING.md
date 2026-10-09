# Contributing to IRIS Website

## Quick rules
- One content item = one folder (Page Bundle): `index.md` + images/PDFs in the same folder.
- Keep **large files** (datasets, >25MB PDFs, models) on Zenodo/GitHub Releases/OSS; this site stores only thumbnails and links.
- Every change goes through a PR if possible.

## Add a News post
Copy `TEMPLATES/post.zh.md` -> `content/zh/post/YYYY-MM-DD-your-slug/index.md`
and `TEMPLATES/post.en.md` -> `content/en/post/YYYY-MM-DD-your-slug/index.md`

## Add a Project
Copy templates to `content/*/project/<slug>/index.md`. Put `featured.jpg` next to it.

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
