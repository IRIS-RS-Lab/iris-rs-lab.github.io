---
title: 论文
type: landing
sections:
  - block: markdown
    content:
      title: 论文与出版物
      text: |
        这里汇总 IRIS 的论文列表与详情页面。
        
        - 建议：用 Zotero 定期导出 `publications.bib`，再通过脚本自动生成/补全详情页（后续可加 Actions 自动化）。
  - block: collection
    id: all_pubs
    content:
      title: 全部论文
      subtitle: ''
      text: |
        按时间排序显示（可配合标签过滤）。
      count: 0
      filters:
        folders:
          - publication
        tag: ""
        category: ""
        featured_only: false
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      offset: 0
      sort_by: "Date"
      sort_ascending: false
    design:
      view: compact
---
