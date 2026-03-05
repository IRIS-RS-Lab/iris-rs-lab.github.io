#!/usr/bin/env python3
import re
import sys
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
    month = clean_bib_text(entry.get('month', '01'))
    # 简单处理月份映射 (Jan -> 01)
    month_map = {"jan":"01", "feb":"02", "mar":"03", "apr":"04", "may":"05", "jun":"06",
                 "jul":"07", "aug":"08", "sep":"09", "oct":"10", "nov":"11", "dec":"12"}
    month_num = month_map.get(month.lower()[:3], "01") if not month.isdigit() else month.zfill(2)
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
authors:[{authors_str}]
tags: [{tags_str}]
featured: false
# 🔴 如果你想为这篇论文添加详细页面，请删除下面这行 `external_link`
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
=== 论文详情页存根 ===
当前论文在列表中不可点击（无详情页）。
如果需要展示详细页面，请：
1. 删除上方的 `external_link: "#no-detail"`
2. 取消注释下方的正文内容并填写你的介绍
-->

<!--
## 摘要
{abstract}

## 方法与结果
(如果你有配图，将其命名为 featured.jpg 放在当前文件夹即可，引擎会自动抓取)

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
    if not BIB_FILE.exists():
        print(f"Warning: {BIB_FILE} not found. Skipping sync.")
        sys.exit(0)

    print(f"[*] Parsing {BIB_FILE} ...")
    with open(BIB_FILE, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    for entry in bib_database.entries:
        generate_hugo_bundle(entry, ZH_DIR, "zh")
        generate_hugo_bundle(entry, EN_DIR, "en")

    print("[*] Sync complete. Remember to commit the generated files.")

if __name__ == "__main__":
    main()
