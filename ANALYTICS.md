# 网站访问统计与站长工具配置

## 1. Google Analytics 4：访问与传播效果

1. 打开 <https://analytics.google.com/>，用课题组管理的账号创建 GA4 媒体资源。
2. 创建 **Web 数据流**，网址填写 `https://iris-rs-lab.github.io`。
   中英文共用一个数据流，按页面路径 `/zh/`、`/en/` 分析，不重复创建媒体资源。
3. 复制 **衡量 ID**（`G-` 开头），填写 `config/_default/params.yaml`：

   ```yaml
   marketing:
     analytics:
       google_analytics: "G-你的实际ID"
     verification:
       google: ""
       bing: ""
       baidu: ""
   ```

   编辑已有的 `marketing` 节点，不要再新增同名节点，也不要放到 `hugoblox` 下。
   ID 是公开标识，不是 API 密钥；不要填账号密码、服务账号 JSON 或访问令牌。
   标准 Hugo `services.googleAnalytics.ID` 也受支持，以上配置优先。
4. Web 数据流中配置 **增强型衡量**。建议启用网页浏览、滚动、出站点击、文件下载；
   关闭站内搜索、表单互动和不使用的视频互动，避免收集输入内容。
   本站不是 SPA，网页浏览的高级设置中关闭“基于浏览器历史记录事件的网页更改”，
   防止额外自动页面事件绕过本站对 URL 查询串的清理。
   不要额外安装 GTM 或第二份 GA 代码，否则可能重复计数、绕过同意控制。
5. 不启用 Google Signals、广告个性化、用户提供的数据收集或 User-ID。
   事件数据保留期建议先选 2 个月；按实际需要调整，并限制管理后台成员权限。
6. 正常审核、提交并部署后，在网站页脚选择“同意访问统计”，检查 GA 的**实时报告**。
   常规报表通常需等待 24–48 小时。没有真实 ID 或未部署前不会产生统计。

### 推荐关注的报告

| 问题 | GA4 报告或指标 |
| --- | --- |
| 有多少人访问，是否增长？ | 活跃用户、会话、浏览量；按周/月比较 |
| 访客从哪里来？ | 流量获取：来源 / 媒介、默认渠道组 |
| 哪些内容最受关注？ | 网页和屏幕：按页面路径比较论文、项目、动态与资源 |
| 中英文网站使用情况？ | 用 `/zh/` 与 `/en/` 路径筛选；不要把浏览器语言当成页面语言 |
| 论文、代码和数据是否有人点击？ | 增强型衡量的 `click`、`file_download` 事件 |

增强型衡量在 Google 后台开启，不由仓库自动开启。
`file_download` 衡量链接点击，不证明文件实际下载完成；跨站 PDF 链接可能同时出现出站点击。
滚动事件也不等于完整阅读。确有业务意义时再将相应事件标记为“关键事件”。
不要在公开页面 URL、文件链接、页面标题或 UTM 标签中放邮箱、姓名、令牌等个人或敏感信息：
增强型衡量可能发送链接地址，页面路径和标题本身也会进入统计。

### 区分传播渠道

对外分享链接可使用公开、简短的英文/数字标签，例如：

```text
https://iris-rs-lab.github.io/zh/?utm_source=newsletter&utm_medium=email&utm_campaign=lab_2026
```

代码清理发送给 GA 的页面 URL 和来源 URL 的查询串与片段；
单独保留 `utm_source`、`utm_medium`、`utm_campaign`、`utm_id`、`utm_content` 的归因值，
只接受 1–100 位英文字母、数字及 `._~-`，不发送 `utm_term`。
直接进入带 UTM 的页面时若选择同意，归因生效；未同意时不会为了保留归因而额外跟踪跨页行为。

## 2. Google Search Console：搜索曝光与收录

1. 打开 <https://search.google.com/search-console/>。
2. 添加 **网址前缀** 资源 `https://iris-rs-lab.github.io/`。
   该地址属于 GitHub 托管域名，通常无法控制 `github.io` 的 DNS，故不要选需要 DNS 验证的域资源。
3. 选择 HTML 标记验证，仅复制 `content="..."` 中的验证码，填入
   `marketing.verification.google`。主题已实现 meta 标签，无需再手工加模板。
4. 部署后确认页面源码有 `google-site-verification`，回平台点击验证。
5. 提交 `https://iris-rs-lab.github.io/sitemap.xml`；这是多语言站点地图索引，
   会指向中英文子站点地图。使用网址检查查看首页及重点论文/项目页的可索引状态。
6. 在 GA4 管理界面将 Search Console 与对应 Web 数据流关联（需要相应权限），
   联合分析搜索曝光、点击、CTR、平均排名与落地页访问。

Search Console 衡量 Google 搜索表现，不等于全站访问量，也不要求访客同意加载 GA。
提交站点地图并不保证收录或排名。验证通过后保留验证码，以供后续复核。

## 3. Bing 与百度站长工具

- **Bing Webmaster Tools**：<https://www.bing.com/webmasters/>
  可以尝试从 Search Console 导入资源，或把 HTML meta 验证码填到
  `marketing.verification.bing`。提交同一站点地图，查看抓取、索引及 SEO 诊断。
- **百度搜索资源平台**：<https://ziyuan.baidu.com/>
  若账号及站点符合平台当前准入要求，把 HTML meta 验证码填到
  `marketing.verification.baidu`，再按平台实际提供的方式提交链接。
  GitHub Pages 的大陆访问可达性会影响抓取，不能靠验证标签解决。
- **PageSpeed Insights**：<https://pagespeed.web.dev/>
  输入中英文首页及重点页面地址，关注 LCP、INP、CLS 和图片体积。
  流量小时可能没有真实用户的 Core Web Vitals 数据；实验室评分与真实用户指标并不相同。

不需要为使用上述工具额外嵌入广告、热图或会话录制脚本。
若以后增加 Microsoft Clarity、百度统计或 GTM，需要单独接入相同的同意机制；
本次同意控制只覆盖本站的 GA4 加载器，不应直接启用主题的其他分析脚本。

## 4. 隐私、覆盖率与验证

- 空 ID 完全关闭 GA 和同意界面；只有 production 构建且 ID 有效才输出加载器。
  普通 `hugo server` 预览不采集；不要用 production 模式开展日常本地预览。
- 默认不向 Google Analytics 发请求，明确同意后才异步加载 Google 脚本。
  这不代表整个主题没有其他第三方资源（例如字体）。
- 同意/拒绝在当前浏览器保存 180 天，中英文共享。页脚可重新选择并撤回；
  撤回会禁用后续 GA 采集、更新同意状态，并尽力清理本站可访问的 `_ga` Cookie。
  不能撤销已发出的请求或删除 Google 已接收的数据；删除历史数据需在 GA 后台处理。
- 尊重浏览器 DNT / Global Privacy Control，即使此前同意也不加载统计。
  浏览器禁用存储时仍可浏览和选择，但选择可能无法跨页保留。
- 同意制、广告拦截器和网络可达性会使 GA 低估访问量，国内访问可能无法上报。
  GA 无法回溯安装前的访问，也不应被当作审计级的精确人数。
- 本次未嵌入公开的 PV/UV 计数器。GA 报告需要登录，切勿把管理凭证放进前端代码。
  如以后需要公开数字，宜通过服务端定期发布不含访客信息的聚合数据。
- 这是一套技术上的最小化措施，不代表自动满足所有适用地区的隐私义务；
  启用前由网站负责人确认隐私说明和数据处理安排。

本地自动测试（Node 22+、Hugo，及项目 Python 依赖）：

```shell
node --test tests/test_analytics.cjs
python -m unittest discover -s tests -v
```

自动测试不访问 Google，也不使用真实统计 ID。模板测试使用独立小型 Hugo 站点，
不依赖外部主题；不能代替完整网站构建。CI 在固定 Hugo 0.128.2 下运行测试后构建全站。
上线验收应分别打开中英文页，在浏览器 Network 筛选 `googletagmanager` / `google-analytics`：
未同意、拒绝时不应发出 GA 请求；同意后才应加载脚本并上报；
随后检查实时报告、撤回操作和下一次页面加载行为。
