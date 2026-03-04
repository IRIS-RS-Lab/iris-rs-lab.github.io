---
title: People
type: landing
sections:
  - block: markdown
    content:
      title: People
      text: |
        This page aggregates team member profiles.
        
        > Maintenance: one profile per folder in `content/en/authors/<id>/_index.md` (Chinese in `content/zh/authors/`).
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
