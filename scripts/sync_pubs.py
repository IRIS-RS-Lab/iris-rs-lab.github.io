#!/usr/bin/env python3
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import bibtexparser
except ImportError:
    sys.exit("Critical: Missing bibtexparser. Run `pip install bibtexparser`")

# 目录配置 (Fail Fast 检查)
ROOT_DIR = Path(__file__).resolve().parent.parent
BIB_FILE = ROOT_DIR / "publications.bib"
ZH_DIR = ROOT_DIR / "content/zh/publication"
EN_DIR = ROOT_DIR / "content/en/publication"
DATA_DIR = ROOT_DIR / "data/publications"
DATA_FILE = DATA_DIR / "generated.json"

def clean_bib_text(text: str) -> str:
    """清理 BibTeX 特殊字符和换行"""
    if not text:
        return ""
    text = re.sub(r'[{}]', '', text)
    text = re.sub(r'\\&', '&', text)
    text = re.sub(r'\\%', '%', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip().replace('"', '\\"')

def parse_authors(author_field: str) -> str:
    """转换 'Last, First and Last, First' 为 Hugo 数组格式"""
    if not author_field:
        return ""
    authors = [a.strip() for a in author_field.split(' and ')]
    return ", ".join([f'"{clean_bib_text(a)}"' for a in authors])

def parse_tags(keywords_field: str) -> str:
    if not keywords_field:
        return ""
    tags = [t.strip() for t in keywords_field.split(',')]
    return ", ".join([f'"{clean_bib_text(t)}"' for t in tags])

def normalize_month(month: str) -> str:
    month = clean_bib_text(month or "")
    month_map = {
        "jan": "01", "feb": "02", "mar": "03", "apr": "04",
        "may": "05", "jun": "06", "jul": "07", "aug": "08",
        "sep": "09", "oct": "10", "nov": "11", "dec": "12",
    }
    if not month:
        return "01"
    if month.isdigit():
        return month.zfill(2)
    return month_map.get(month.lower()[:3], "01")

def normalize_badges(entry: dict) -> list[str]:
    badges: list[str] = []

    for field in ("badges", "badge", "award", "awards", "special", "highlight"):
        raw = clean_bib_text(entry.get(field, ""))
        if not raw:
            continue
        parts = [p.strip() for p in re.split(r"[;,|/]", raw) if p.strip()]
        badges.extend(parts)

    truthy = {"true", "yes", "1"}
    if clean_bib_text(entry.get("cover", "")).lower() in truthy:
        badges.append("Cover Paper")
    if clean_bib_text(entry.get("bestpaper", "")).lower() in truthy:
        badges.append("Best Paper")

    deduped = []
    seen = set()
    for badge in badges:
        key = badge.lower()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(badge)
    return deduped

def build_publication_record(entry: dict) -> dict | None:
    citekey = clean_bib_text(entry.get("ID", ""))
    if not citekey:
        return None

    title = clean_bib_text(entry.get("title", "Untitled"))
    authors = [clean_bib_text(a) for a in entry.get("author", "").split(" and ") if a.strip()]
    year = clean_bib_text(entry.get("year", "2000"))
    month_num = normalize_month(entry.get("month", "01"))
    date_str = f"{year}-{month_num}-01"
    venue = clean_bib_text(entry.get("journal", entry.get("booktitle", "")))
    keywords = [clean_bib_text(t) for t in entry.get("keywords", "").split(",") if t.strip()]

    return {
        "citekey": citekey,
        "entry_type": clean_bib_text(entry.get("ENTRYTYPE", "")),
        "title": title,
        "authors": authors,
        "authors_text": ", ".join(authors),
        "venue": venue,
        "date": date_str,
        "year": year,
        "month": month_num,
        "abstract": clean_bib_text(entry.get("abstract", "")),
        "doi": clean_bib_text(entry.get("doi", "")),
        "url": clean_bib_text(entry.get("url", "")),
        "keywords": keywords,
        "badges": normalize_badges(entry),
    }

def write_publication_data(entries: list[dict]):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": str(BIB_FILE.relative_to(ROOT_DIR)).replace("\\", "/"),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "entries": sorted(entries, key=lambda item: item["date"], reverse=True),
    }
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"[*] Wrote data: {DATA_FILE}")

def generate_hugo_bundle(entry: dict, target_dir: Path, lang: str):
    citekey = entry.get('ID')
    if not citekey:
        return

    bundle_dir = target_dir / citekey
    index_file = bundle_dir / "index.md"

    # 防御性逻辑：如果文件已存在，直接跳过（保护人工修改的资产）
    if index_file.exists():
        return

    # 提取并清洗数据
    title = clean_bib_text(entry.get('title', 'Untitled'))
    year = clean_bib_text(entry.get('year', '2000'))
    month_num = normalize_month(entry.get('month', '01'))
    date_str = f"{year}-{month_num}-01"

    abstract = clean_bib_text(entry.get('abstract', ''))
    authors_str = parse_authors(entry.get('author', ''))
    tags_str = parse_tags(entry.get('keywords', ''))
    venue = clean_bib_text(entry.get('journal', entry.get('booktitle', '')))

    summary = f"Published in {venue}." if venue else ""

    # 构造 Markdown
    content = f"""---
title: "{title}"
date: {date_str}
summary: "{summary}"
authors: [{authors_str}]
tags:[{tags_str}]
featured: false
# 🔴 核心机制：此行代码会让这篇论文在列表中不可点击。若要为其添加详细页面，请删除这行代码！
external_link: "#no-detail"
links:
  - name: PDF
    url: "{entry.get('url', '')}"
    icon: hero/document
  - name: Code
    url: ""
    icon: brands/github
---

<!--
================ 详情页隐藏区 ================
如果你删除了上方的 external_link 激活了详情页，
可以取消下方内容的注释，放入你的成果展示。
(若有配图，直接将图片命名为 featured.jpg 放在本文件夹)
==============================================
-->

<!--
## 摘要
{abstract}

## 引用格式
```bibtex
@article{{{citekey},
  title={{{title}}},
  author={{{entry.get('author', '')}}},
  journal={{{venue}}},
  year={{{year}}}
}}
```
-->
"""
    # 写入文件
    bundle_dir.mkdir(parents=True, exist_ok=True)
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[+] Created ({lang}): {citekey}")

def main():
    parser = argparse.ArgumentParser(description="Sync publication metadata from publications.bib.")
    parser.add_argument("--skip-bundles", action="store_true", help="Only generate structured publication data.")
    args = parser.parse_args()

    if not BIB_FILE.exists():
        print(f"Warning: {BIB_FILE} not found. Skipping sync.")
        sys.exit(0)

    print(f"[*] Parsing {BIB_FILE} ...")
    with open(BIB_FILE, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    data_entries = []
    for entry in bib_database.entries:
        record = build_publication_record(entry)
        if record:
            data_entries.append(record)
        if not args.skip_bundles:
            generate_hugo_bundle(entry, ZH_DIR, "zh")
            generate_hugo_bundle(entry, EN_DIR, "en")

    write_publication_data(data_entries)
    print("[*] Sync complete. Remember to commit the generated files.")

if __name__ == "__main__":
    main()
