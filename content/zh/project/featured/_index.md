---
title: 重点项目
weight: 20
type: landing
sections:
  - block: markdown
    content:
      title: ''
      text: |
        {{< section_nav >}}
  - block: collection
    id: projects_featured
    content:
      title: 重点项目列表
      subtitle: ''
      text: |
        可作为首页精选项目的来源。
      count: 0
      filters:
        folders:
          - project
        tag: ""
        category: ""
        featured_only: true
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      offset: 0
      sort_by: "Date"
      sort_ascending: false
    design:
      view: card
---
