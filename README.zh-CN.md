# 🚀 Awesome WeChat Automation

> 精选的微信公众号自动发布与运营自动化工具清单，以及微信生态相关自动化资源。

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg) ![Last Commit](https://img.shields.io/github/last-commit/Lxcardoza993/awesome-wechat-automation) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

**Languages**: [English](README.md) · [简体中文](README.zh-CN.md)

*如果这份清单对你有帮助，请给仓库点个 ⭐，帮助更多人发现它。*

## 目录

- [📝 官方账号自动发布](#📝-官方账号自动发布)
- [✍️ 文章起草与 AI 写作](#✍-文章起草与-ai-写作)
- [🖼️ 媒体与素材管理](#🖼-媒体与素材管理)
- [📊 数据分析与监控](#📊-数据分析与监控)
- [🔄 多平台发布到微信](#🔄-多平台发布到微信)
- [🔌 官方账号 SDK 与 API 封装](#🔌-官方账号-sdk-与-api-封装)
- [🌐 微信浏览器自动化 / RPA](#🌐-微信浏览器自动化--rpa)
- [🧩 相关：小程序自动化](#🧩-相关小程序自动化)
- [🏢 相关：企业微信自动化](#🏢-相关企业微信自动化)
- [🤖 相关：微信机器人与客服](#🤖-相关微信机器人与客服)
- [🛠️ CLI / 开发者工具](#🛠-cli--开发者工具)
- [快速选型指南](#快速选型指南)
- [贡献](#贡献)
- [致谢](#致谢)
- [Star 历史](#star-历史)
- [许可证](#许可证)

## 为什么有这份清单

微信公众号自动化涵盖发布、内容排版、媒体管理、数据分析、SDK 以及微信小程序/企业微信等相关工具。这份清单收集了能够帮助自动化和扩展微信工作流的开源项目。

## 📝 官方账号自动发布

| 工具 | ⭐ | 语言 | 描述 | 许可证 |
| --- | --- | --- | --- | --- |
| [wechat-publisher](https://github.com/sakuraoxo-clio/wechat-publisher) | 77 | TypeScript | Claude/Coex skill，将文章转换为符合微信规范的 HTML，上传图片，可选生成 AI 封面，并一键推送草稿到微信公众号草稿箱。 | MIT |
| [wechat-publisher-mcp](https://github.com/BobGod/wechat-publisher-mcp) | 49 | JavaScript | 专为微信公众号文章发布打造的 MCP server，向兼容 MCP 的 AI 工具提供 Markdown 转微信 HTML、封面处理、预览/正式发布和状态查询能力。 | MIT |
| [wechat-publisher](https://github.com/0731coderlee-sudo/wechat-publisher) | 41 | Shell | OpenClaw/CLI skill，将 Markdown 转换为样式化微信 HTML 并发布到微信公众号草稿箱，支持自动图床托管和多种代码高亮主题。 | MIT |
| [wx-manage](https://github.com/niefy/wx-manage) | — | Java | 基于 Spring Boot 和 Vue 的微信公众号管理后台。 | — |
| [wechat-publisher](https://github.com/xiaonan0527/wechat-publisher) | 13 | JavaScript | 独立的 OpenClaw skill，将 Markdown 转为微信兼容的内联样式 HTML，并通过微信公众号 API 推送草稿，支持自动上传图片和可选封面生成。 | — |
| [wechat-article-publisher-skill](https://skillsmp.com/creators/iamzifei/wechat-article-publisher-skill/skills-wechat-article-publisher) | — | — | 通过 skillsmp.com 发布微信文章的 Claude/Codex skill。 | — |
| [wechat-publisher](https://github.com/penxxy/wechat-publisher) | 9 | Python | 微信公众号开发 Python SDK，支持文章发布、图片上传、批量发布和 access-token 缓存。 | MIT |
| [ai-news-wechat-publisher](https://github.com/xiaomi158/ai-news-wechat-publisher) | 6 | HTML | 自动化 AI 新闻发布流水线，抓取 RSS 源后使用 DeepSeek 总结和分类，并按计划将排版好的文章发布到微信公众号。 | — |

## ✍️ 文章起草与 AI 写作

| 工具 | ⭐ | 语言 | 描述 | 许可证 |
| --- | --- | --- | --- | --- |
| [wechat-publisher](https://github.com/jiji262/wechat-publisher) | 132 | HTML | Claude Code/Codex/Cursor skill 与 CLI，可调研主题、撰写 3000-5000 字的微信文章、生成图片并发布草稿到微信公众号。 | — |
| [ai-wechat](https://github.com/YuppyChen/ai-wechat) | 60 | TypeScript | 基于 Claude Code 的工作流，从创意到 Markdown 起草、排版和 HTML 发布，创建并发布微信公众号文章。 | — |
| [wechat-ai-publisher](https://github.com/bbwdadfg/wechat-ai-publisher) | 37 | Shell | Agent skill，收集 AI 趋势、撰写微信公众号文章、生成图片并发布草稿到微信。 | MIT |
| [fengyun-publish](https://github.com/duliangkuan/fengyun-publish) | 20 | Python | 19 步端到端微信公众号 AI 流水线，涵盖选题、调研、写作、审校、排版和推送草稿。 | MIT |
| [wechat-article-agent](https://github.com/ymstar/wechat-article-agent) | 7 | Python | LangChain/LangGraph agent，可调研主题、撰写文章、创建封面图、审核内容并发布到微信公众号草稿箱。 | Apache-2.0 |
| [wechat-article-generator](https://github.com/icebear0828/wechat-article-generator) | 7 | Python | 端到端微信公众号文章流水线，使用 AI 写作、生成图片、过滤敏感词、渲染微信兼容 HTML 并复制用于发布。 | — |
| [wechat-article-writing-skill](https://github.com/AlexLaoBai/wechat-article-writing-skill) | 4 | Python | 微信公众号自动写作和发布 skill，支持自动/引导模式、多种主题和一键推送草稿。 | MIT |
| [weblog-skills](https://github.com/szsip239/weblog-skills) | 4 | JavaScript | Markdown 转微信发布 skill，支持 AI 风格写作、doocs/md HTML 渲染、AI 人性化和一键推送草稿。 | — |

## 🖼️ 媒体与素材管理

| 工具 | ⭐ | 语言 | 描述 | 许可证 |
| --- | --- | --- | --- | --- |
| [doocs/md](https://github.com/doocs/md) | 12946 | TypeScript | 简洁的微信 Markdown 编辑器，支持自定义主题、内容管理、多图床和 AI 辅助。 | WTFPL |
| [markdown-nice](https://github.com/mdnice/markdown-nice) | 4647 | JavaScript | 支持主题设计的 Markdown 编辑器，常用于生成格式精美的微信公众号文章。 | GPL-3.0 |
| [wechat-format](https://github.com/lyricat/wechat-format) | 4535 | JavaScript | 微信公众号排版编辑器，将 Markdown 转换为微信专用 HTML。 | — |
| [silk-v3-decoder](https://github.com/kn007/silk-v3-decoder) | 3154 | C | 解码微信/QQ 的 Silk v3 音频文件并转换为 MP3 等格式。 | MIT |
| [online-markdown](https://github.com/barretlee/online-markdown) | 921 | JavaScript | 专为微信公众号排版设计的在线 Markdown 转换器。 | Other |
| [xiaohu-wechat-format](https://github.com/xiaohuailabs/xiaohu-wechat-format) | 644 | Python | Claude Code skill，一键完成微信公众号排版和发布，将 Markdown 转为微信兼容的 HTML 草稿。 | — |

## 📊 数据分析与监控

| 工具 | ⭐ | 语言 | 描述 | 许可证 |
| --- | --- | --- | --- | --- |
| [WeChatDataAnalysis](https://github.com/LifeArchiveProject/WeChatDataAnalysis) | 1516 | Python | 解密微信 4.x 数据，生成年度总结、聊天记录和朋友圈导出供分析。 | — |
| [sentry-miniapp](https://github.com/lizhiyao/sentry-miniapp) | 667 | TypeScript | 用于微信小程序及其他小程序平台错误与性能监控的 SDK。 | MIT |
| [WeChat-Data-Analysis](https://github.com/allen1881996/WeChat-Data-Analysis) | 463 | Python | 从 iPhone 和 MacBook 本地数据库中提取并分析微信聊天记录。 | MIT |
| [wechat_articles_spider](https://github.com/ghh1251/wechat_articles_spider) | 341 | Python | 爬取微信公众号公开文章用于收集和分析，无需抓包。 | MIT |
| [wechat-data-tools](https://github.com/Agentchengfeng/wechat-data-tools) | 80 | Python | 监控微信公众号文章、获取互动数据并生成可视化报告。 | — |
| [mini-program-monitor](https://github.com/SkyAPM/mini-program-monitor) | 8 | TypeScript | 面向微信和支付宝小程序的 Apache SkyWalking 监控客户端。 | Apache-2.0 |
| [clickstream-wechat](https://github.com/awslabs/clickstream-wechat) | 5 | TypeScript | 适用于微信小程序的 AWS Clickstream 分析 SDK。 | Apache-2.0 |
| [wechat-data-analysis](https://github.com/yanzhenjia/wechat-data-analysis) | 1 | Python | 微信公众号文章本地分析工具。 | MIT |

## 🔄 多平台发布到微信

| 工具 | ⭐ | 语言 | 描述 | 许可证 |
| --- | --- | --- | --- | --- |
| [mdeditor](https://github.com/xiaobox/mdeditor) | 668 | JavaScript | Markdown 编辑器和社交平台发布工具，将 Markdown 转为微信优化富文本，一键发布到微信公众号等社交平台。 | MIT |
| [SyncCaster](https://github.com/RyanYipeng/SyncCaster) | 431 | TypeScript | Chrome 扩展，将自写或捕获的网页文章转为 Markdown，并通过 DOM 自动化发布到微信公众号、掘金、CSDN、知乎等平台。 | MIT |
| [lovpen-obsidian](https://github.com/MarkShawn2020/lovpen-obsidian) | 11 | TypeScript | Obsidian 插件，一次格式化笔记后分发到微信、知乎、小红书和 Twitter。 | MIT |
| [mulit-article-publisher](https://github.com/meijintao233/mulit-article-publisher) | 8 | JavaScript | 多平台文章发布工具，可将文章发布到掘金、微信、今日头条、知乎和技术博客。 | MIT |
| [multi-platform-publisher](https://github.com/mguozhen/multi-platform-publisher) | 6 | Python | 命令行工具，将内容发布到 X/Twitter、LinkedIn、微信公众号和小红书。 | MIT |
| [obsidian-md-publisher](https://github.com/volcanicll/obsidian-md-publisher) | 2 | TypeScript | Obsidian 插件，一键将 Markdown 笔记发布到微信公众号、知乎、今日头条和小红书。 | MIT |
| [wechat-publisher](https://github.com/RanceLee233/wechat-publisher) | 2 | JavaScript | Obsidian 插件，将 Markdown 笔记直接作为草稿发布到微信公众号。 | MIT |
| [Notion2wechatMP](https://github.com/royrenwb/Notion2wechatMP) | 1 | JavaScript | 在 Notion 中查找文章并自动发送到微信公众号草稿箱的工具。 | — |

## 🔌 官方账号 SDK 与 API 封装

| 工具 | ⭐ | 语言 | 描述 | 许可证 |
| --- | --- | --- | --- | --- |
| [weui](https://github.com/Tencent/weui) | 27387 | HTML/CSS | 腾讯官方出品的移动 Web 应用 UI 库。 | Other |
| [EasyWeChat](https://github.com/w7corp/easywechat) | 10373 | PHP | 用于微信公众号和小程序开发的 PHP SDK。 | MIT |
| [wechatpy](https://github.com/wechatpy/wechatpy) | 4291 | Python | 用于微信公众号、小程序和支付 API 的 Python SDK。 | MIT |
| [wechat-python-sdk](https://github.com/doraemonext/wechat-python-sdk) | 1348 | Python | 微信公众平台 Python 开发工具包（已弃用）。 | BSD-2-Clause |

## 🌐 微信浏览器自动化 / RPA

| 工具 | ⭐ | 语言 | 描述 | 许可证 |
| --- | --- | --- | --- | --- |
| [wxauto](https://github.com/cluic/wxauto) | 7151 | Python | 自动化 Windows 微信桌面客户端，实现收发消息和构建简单微信机器人。 | Apache-2.0 |
| [pywechat](https://github.com/Hello-Mr-Crab/pywechat) | 1658 | Python | 通过 pywinauto 自动化 Windows 微信桌面客户端，执行大部分 PC 微信操作。 | — |
| [robotic-process-automation](https://github.com/yihleego/robotic-process-automation) | 308 | Java | 用于自动化微信和企业微信桌面客户端的 Java RPA 框架。 | MIT |
| [WeChatMediaPlatformAutomation](https://github.com/LinusLing/WeChatMediaPlatformAutomation) | 214 | JavaScript | 使用 Puppeteer 在微信公众平台网页（mp.weixin.qq.com）发布或预览文章。 | MIT |
| [WeChatAuto.SDK](https://github.com/scottfly189/WeChatAuto.SDK) | 188 | C# | .NET UI 自动化 SDK，用于微信 RPA，支持消息收发、群/好友管理和朋友圈操作。 | MIT |
| [agent-wechat](https://github.com/thisnick/agent-wechat) | 110 | Rust | 基于 Rust 的 RPA 微信自动化工具。 | — |
| [wechat-rpa-bot-skill](https://github.com/LeoMusk/wechat-rpa-bot-skill) | 65 | Python | 面向 AI agent 的微信 RPA skill，支持无头运行和 REST API 控制。 | — |
| [wechat-daily-report-bot](https://github.com/perrycan/wechat-daily-report-bot) | 34 | Python | 使用 wxauto 和 FastAPI 在微信群中自动进行每日工作汇报点名。 | MIT |

## 🧩 相关：小程序自动化

| 工具 | ⭐ | 语言 | 描述 | 许可证 |
| --- | --- | --- | --- | --- |
| [mini-ci](https://github.com/ruochuan12/mini-ci) | 220 | TypeScript | 对官方 miniprogram-ci 的增强型 CLI 封装，支持批量、多项目的微信小程序上传、预览和配置驱动 CI 工作流。 | MIT |
| [miniprogram-deploy](https://github.com/sunxiuguo/miniprogram-deploy) | 26 | TypeScript | 封装 miniprogram-ci 的自动化工具，用于微信小程序的上传和预览。 | — |
| [wx-ci](https://github.com/jaluik/wx-ci) | 18 | TypeScript | 一键命令行脚本，用于微信小程序的打包、上传和预览，无需打开微信开发者工具。 | MIT |
| [actions.mini-program](https://github.com/echoings/actions.mini-program) | 14 | TypeScript | 封装 miniprogram-ci 的 GitHub Action，用于 CI/CD 流水线中自动预览和上传微信小程序。 | MIT |
| [miniprogram-automator-extension](https://github.com/nchejara/miniprogram-automator-extension) | 13 | JavaScript | 扩展函数库，简化使用官方 miniprogram-automator 对微信小程序进行端到端测试。 | — |
| [miniprogram-remote-control](https://github.com/LSTM-Kirigaya/miniprogram-remote-control) | 3 | JavaScript | 围绕 miniprogram-automator 的 CLI 远程控制封装，自动化微信小程序的点击、输入、截图、切换标签和重新启动。 | — |
| [miniprogram-ci](https://www.npmjs.com/package/miniprogram-ci) | — | JavaScript | 腾讯官方命令行工具包，无需微信开发者工具 GUI 即可构建、上传、预览和发布微信小程序。 | — |
| [miniprogram-automator](https://www.npmjs.com/package/miniprogram-automator) | — | JavaScript | 腾讯官方 SDK，自动化微信开发者工具以启动微信小程序并模拟用户操作进行测试。 | — |

## 🏢 相关：企业微信自动化

| 工具 | ⭐ | 语言 | 描述 | 许可证 |
| --- | --- | --- | --- | --- |
| [LangBot](https://github.com/langbot-app/LangBot) | 16600 | Python | 生产级多平台聊天机器人框架，支持企业微信/WeCom，实现 AI agent 客服和 n8n/Dify 工作流集成。 | Apache-2.0 |
| [wecom-cli](https://github.com/WecomTeam/wecom-cli) | 2400 | Rust | 官方风格的企业微信命令行界面，让人类和 AI agent 从终端操作企业微信，包括消息、通讯录、任务和会议。 | MIT |
| [go-wecom](https://github.com/wenerme/go-wecom) | 98 | Go | 面向微信工作的 Go SDK，封装 37 个功能分类下超过 500 个生成 API 端点，用于构建企业微信自动化。 | Apache-2.0 |
| [wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server) | 96 | Python | MCP server，向 AI 助手暴露工具，通过官方机器人 webhook API 向企业微信群聊发送消息、文件、图片和模板卡片通知。 | MIT |
| [wecombot](https://github.com/voidint/wecombot) | 9 | Go | 轻量级 Go SDK，用于企业微信群聊机器人，支持发送文本、Markdown、图片、文件、语音、新闻和模板卡片消息，零第三方依赖。 | MIT |
| [wechat_work_webhook_rb](https://github.com/mqzhang/wechat_work_webhook_rb) | 4 | Ruby | 企业微信群聊机器人 webhook Ruby 客户端，支持文本、Markdown、图片、新闻文章和文件消息类型。 | MIT |

## 🤖 相关：微信机器人与客服

| 工具 | ⭐ | 语言 | 描述 | 许可证 |
| --- | --- | --- | --- | --- |
| [CowAgent](https://github.com/zhayujie/CowAgent) | 45760 | Python | 开源 AI 助手和 agent 框架（原 chatgpt-on-wechat），支持包括微信在内的多渠道部署。 | MIT |
| [ItChat](https://github.com/littlecodersh/ItChat) | 26472 | Python | 完整而优雅的微信个人号 API，只需几十行代码即可构建个人微信机器人。 | MIT |
| [wechaty](https://github.com/wechaty/wechaty) | 22889 | TypeScript | 对话式 RPA SDK，帮助开发者为微信及其他消息平台构建聊天机器人。 | Apache-2.0 |
| [wechat-bot](https://github.com/wangrongding/wechat-bot) | 11130 | JavaScript | 基于 WeChaty 的微信机器人，接入 ChatGPT、Claude、Kimi、DeepSeek 和 Ollama 自动回复消息并管理群/好友。 | MIT |
| [WeChatFerry](https://github.com/lich0821/WeChatFerry) | 6748 | C++ | 基于 Hook 的微信机器人框架，可接入 DeepSeek、Gemini、ChatGPT、ChatGLM 等大模型。 | MIT |
| [ChatGPT-wechat-bot](https://github.com/AutumnWhj/ChatGPT-wechat-bot) | 4720 | TypeScript | 基于 Wechaty 框架部署 OpenAI 对话的 ChatGPT 微信机器人。 | MIT |
| [wechat-gptbot](https://github.com/iuiaoin/wechat-gptbot) | 609 | Python | 基于 ChatGPT 的稳定微信机器人，适用于低风险的私人账号自动化。 | MIT |
| [BotFramework-WeChat](https://github.com/microsoft/BotFramework-WeChat) | 69 | C# | 适配器，让 Microsoft BotFramework 机器人能够在微信上收发消息。 | MIT |

## 🛠️ CLI / 开发者工具

| 工具 | ⭐ | 语言 | 描述 | 许可证 |
| --- | --- | --- | --- | --- |
| [vConsole](https://github.com/Tencent/vConsole) | 17494 | TypeScript | 轻量、可扩展的前端开发者工具，用于在微信 webview 中调试移动网页。 | Other |
| [wechat-spider (bowenpay)](https://github.com/bowenpay/wechat-spider) | 3354 | Python | 爬取微信公众号文章和元数据的爬虫。 | — |
| [wechat-spider (striver-ing)](https://github.com/striver-ing/wechat-spider) | 2872 | Python | 开源微信爬虫，爬取公众号文章、阅读量、点赞和评论。 | — |
| [wechat_spider (lqqyt2423)](https://github.com/lqqyt2423/wechat_spider) | 1538 | JavaScript | 爬取微信文章内容、阅读量、点赞、评论和历史文章链接的爬虫。 | MIT |
| [wechat-cli](https://github.com/huohuoer/wechat-cli) | 1499 | Python | 命令行工具，查询本地微信数据（聊天记录、联系人、会话和收藏）用于大模型集成和分析。 | Apache-2.0 |
| [Mojo-Weixin](https://github.com/hexsum/Mojo-Weixin) | 1251 | Perl | 非 GUI 个人微信客户端框架，提供基于插件的 HTTP API 用于自动化和聊天机器人开发。 | MIT |
| [wx-cli](https://github.com/pandorafuture/wx-cli) | 103 | Rust | 命令行工具，解密并查询微信 macOS 本地数据库中的联系人、消息和 LICENSE。 | MIT |
| [Wechat-Claude-bot](https://github.com/mrliuzhiyu/Wechat-Claude-bot) | 33 | Python | 微信机器人，可远程控制 Claude Code CLI，通过手机执行命令和管理项目。 | GPL-3.0 |
| [clawbot](https://github.com/adysec/clawbot) | 30 | Rust | iLink 机器人管理工具，提供命令行界面和 Web 仪表盘用于微信自动化。 | — |
| [wechat-cli](https://github.com/systemxlabs/wechat-cli) | 22 | Rust | 与微信 iLink 机器人交互的 CLI，用于在终端中收发和管理微信消息。 | MIT |
| [wechat-devtool](https://github.com/NewFuture/wechat-devtool) | 6 | TypeScript | 跨平台命令行封装，用于在 Node.js 和 npm 项目中调用微信小程序开发者工具。 | MIT |

## 快速选型指南

- **端到端微信文章发布** → [wechat-publisher](https://github.com/jiji262/wechat-publisher) — Claude/Codex skill 和 CLI，支持调研、写作和发布草稿。
- **为微信排版 Markdown** → [doocs/md](https://github.com/doocs/md) — 流行的微信主题 Markdown 编辑器和图床工具。
- **构建微信聊天机器人** → [wechaty](https://github.com/wechaty/wechaty) — 对话式 RPA SDK，用于微信机器人。
- **微信公众号 SDK（Python）** → [wechatpy](https://github.com/wechatpy/wechatpy) — 面向公众号和小程序 API 的 Python SDK。
- **自动化 Windows 微信桌面端** → [wxauto](https://github.com/cluic/wxauto) — Windows 微信 UI 自动化。
- **企业微信 webhook** → [wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server) — 用于企业微信群机器人通知的 MCP server。
- **小程序 CI/CD** → [miniprogram-ci](https://www.npmjs.com/package/miniprogram-ci) — 腾讯官方 CLI，用于构建和上传小程序。
- **微信数据分析** → [wechat_articles_spider](https://github.com/ghh1251/wechat_articles_spider) — 爬取公开微信文章用于分析。

## 贡献

欢迎贡献 — 详见 [CONTRIBUTING.md](CONTRIBUTING.md)。请提供工具名称、链接、star 数、主要语言、一句话描述、许可证和分类。

## 致谢

感谢所有开源微信自动化项目及其维护者。

## Star 历史

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Lxcardoza993/awesome-wechat-automation&type=Date&theme=dark">
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Lxcardoza993/awesome-wechat-automation&type=Date">
  <img alt="Star History" src="https://api.star-history.com/svg?repos=Lxcardoza993/awesome-wechat-automation&type=Date">
</picture>

## 许可证

清单内容以 [CC0-1.0](LICENSE)  dedicate 至公共领域。各工具保留其自身许可证。
