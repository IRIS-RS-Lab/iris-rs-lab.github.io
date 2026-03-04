---
title: 成员
type: landing
sections:
  - block: markdown
    content:
      title: 团队成员
      text: |
        这里展示 IRIS 的老师、学生与合作者。
        
        > 维护方式：每位成员一个 `content/zh/authors/<id>/_index.md`（英文在 `content/en/authors/`），然后此页自动聚合展示。
  - block: collection
    id: team
    content:
      title: Team
      subtitle: ''
      text: |
      count: 0
      filters:
        folders:
          - authors
        tag: ""
        category: ""
        featured_only: false
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      offset: 0
      sort_by: "Title"
      sort_ascending: true
    design:
      view: card
---
