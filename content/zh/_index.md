---
title: 首页
type: landing
sections:
  - block: hero
    content:
      title: IRIS智能遥感信息工程与应用课题组
      text: |
        Intelligent Remote-sensing Information Systems & Applications (IRIS)
        
        面向计算机视觉与多源遥感，构建“感知—理解—应用”一体化的智能信息系统。
        从地球到眼球：以遥感的“慧眼”连接更广阔的跨学科愿景。
      primary_action:
        text: 查看论文
        url: /zh/publication/
        icon: hero/sparkles
      secondary_action:
        text: 资源共享
        url: /zh/resources/
      announcement:
        text: IRIS = Iris（虹膜）｜对地观测的慧眼 × 生命科学的温度
        link:
          text: 了解交叉研究
          url: /zh/research/cross/
  - block: markdown
    content:
      title: 我们做什么
      subtitle: Research Themes
      text: |
        - **遥感智能解译**：变化检测、目标/场景识别、语义分割、SAR/光学融合。
        - **计算机视觉**：表征学习、跨域泛化、多模态理解与可靠评估。
        - **系统与应用**：数据集/基准、开源工具链、行业落地与可解释性。
  - block: collection
    id: news
    content:
      title: 最新动态
      count: 5
      filters:
        folders:
          - post
      sort_by: "Date"
      sort_ascending: false
    design:
      view: compact
  - block: collection
    id: projects
    content:
      title: 精选项目
      count: 6
      filters:
        folders:
          - project
      sort_by: "Date"
      sort_ascending: false
    design:
      view: compact
  - block: collection
    id: pubs
    content:
      title: 最新论文
      count: 8
      filters:
        folders:
          - publication
      sort_by: "Date"
      sort_ascending: false
    design:
      view: compact
  - block: markdown
    content:
      title: 联系我们
      text: |
        - 邮箱：`contact@iris-lab.org`
        - 位置：`XXX University / XXX Lab`
---
