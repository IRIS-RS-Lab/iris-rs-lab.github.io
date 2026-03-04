---
title: 首页
type: landing
sections:
  - block: hero
    content:
      title: IRIS（艾瑞斯）智能遥感信息工程与应用课题组
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
        
        > 想快速开始维护内容？直接参考仓库里的 `TEMPLATES/` 模板（论文/项目/动态）。
  - block: collection
    id: projects
    content:
      title: 精选项目
      subtitle: ''
      text: |
        展示课题组的代表性项目、系统与数据集。
      count: 6
      filters:
        folders:
          - project
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
  - block: collection
    id: pubs
    content:
      title: 最新论文
      subtitle: ''
      text: |
        持续更新的论文列表与详情页面。
      count: 8
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
  - block: collection
    id: news
    content:
      title: 最新动态
      subtitle: ''
      text: |
        组会、学术交流、竞赛与重要里程碑。
      count: 6
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
      view: compact
  - block: markdown
    content:
      title: 联系我们
      text: |
        - 邮箱：`contact@iris-lab.org`（建议后续替换为你们实际邮箱）
        - 位置：`XXX University / XXX Lab`
        
        > 合作与招生：请见 **加入我们** 页面。
---
