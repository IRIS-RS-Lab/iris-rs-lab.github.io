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
Export BibTeX to `publications.bib` (repo root) and commit it.
(Optional) we can add an importer workflow later to auto-generate stubs.
