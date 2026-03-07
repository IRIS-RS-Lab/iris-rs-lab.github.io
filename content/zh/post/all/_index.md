---
title: 全部动态
weight: 10
type: landing
sections:
  - block: markdown
    content:
      title: ''
      text: |
        {{< section_nav >}}
  - block: collection
    id: posts_all
    content:
      # title: 动态列表
      title: ''
      subtitle: ''
      count: 0
      filters:
        folders:
          - post
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
      view: card
---
