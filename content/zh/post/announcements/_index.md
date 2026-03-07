---
title: 通知公告
weight: 20
type: landing
sections:
  - block: markdown
    content:
      title: ''
      text: |
        {{< section_nav >}}
  - block: collection
    id: posts_announcements
    content:
      title: 公告列表
      subtitle: ''
      count: 0
      filters:
        folders:
          - post
        tag: "Announcement"
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
