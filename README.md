# 🚀 Awesome WeChat Automation

> A curated list of WeChat Official Account (微信公众号) auto-publishing and operation automation tools, plus related WeChat ecosystem automation.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg) ![Last Commit](https://img.shields.io/github/last-commit/Lxcardoza993/awesome-wechat-automation) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

**Languages**: [English](README.md) · [简体中文](README.zh-CN.md)

*If this list is useful, please ⭐ the repo — it helps others find it.*

## Contents

- [📝 Official Account Auto-Publishing](#📝-official-account-auto-publishing)
- [✍️ Article Drafting & AI Writing](#✍-article-drafting--ai-writing)
- [🖼️ Media & Asset Management](#🖼-media--asset-management)
- [📊 Analytics & Monitoring](#📊-analytics--monitoring)
- [🔄 Multi-Platform Publishing to WeChat](#🔄-multi-platform-publishing-to-wechat)
- [🔌 Official Account SDKs & API Wrappers](#🔌-official-account-sdks--api-wrappers)
- [🌐 Browser Automation / RPA for WeChat](#🌐-browser-automation--rpa-for-wechat)
- [🧩 Related: Mini Program Automation](#🧩-related-mini-program-automation)
- [🏢 Related: Enterprise WeChat Automation](#🏢-related-enterprise-wechat-automation)
- [🤖 Related: WeChat Bots & Customer Service](#🤖-related-wechat-bots--customer-service)
- [🛠️ CLI / Developer Utilities](#🛠-cli--developer-utilities)
- [Quick Selection Guide](#quick-selection-guide)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [Star History](#star-history)
- [License](#license)

## Why this list

WeChat Official Account automation spans publishing, content formatting, media management, analytics, SDKs, and related WeChat/Mini Program/Enterprise WeChat tooling. This list collects open-source projects that make it easier to automate and extend WeChat workflows.

## 📝 Official Account Auto-Publishing

| Tool | ⭐ | Language | Description | License |
| --- | --- | --- | --- | --- |
| [wechat-publisher](https://github.com/sakuraoxo-clio/wechat-publisher) | 77 | TypeScript | Claude/Coex skill that converts articles into WeChat-compliant HTML, uploads images, optionally generates AI covers, and pushes one-click drafts to the WeChat Official Account draft box. | MIT |
| [wechat-publisher-mcp](https://github.com/BobGod/wechat-publisher-mcp) | 49 | JavaScript | MCP server dedicated to WeChat Official Account article publishing, exposing Markdown-to-WeChat-HTML conversion, cover handling, preview/formal publishing, and status queries to MCP-compatible AI tools. | MIT |
| [wechat-publisher](https://github.com/0731coderlee-sudo/wechat-publisher) | 41 | Shell | OpenClaw/CLI skill that converts Markdown into styled WeChat HTML and publishes it to the WeChat Official Account draft box with automatic image hosting and multiple code-highlight themes. | MIT |
| [wechat-publisher](https://github.com/xiaonan0527/wechat-publisher) | 13 | JavaScript | Standalone OpenClaw skill that converts Markdown to WeChat-compatible inline-style HTML and pushes drafts via the WeChat Official Account API with automatic image upload and optional cover generation. | — |
| [wechat-publisher](https://github.com/penxxy/wechat-publisher) | 9 | Python | Python SDK for WeChat Official Account development that supports article publishing, image upload, batch publishing, and access-token caching. | MIT |
| [ai-news-wechat-publisher](https://github.com/xiaomi158/ai-news-wechat-publisher) | 6 | HTML | Automated AI-news publishing pipeline that scrapes RSS feeds, summarizes and categorizes stories with DeepSeek, and posts formatted articles to a WeChat Official Account on a schedule. | — |
| [wx-manage](https://github.com/niefy/wx-manage) | — | Java | WeChat Official Account management backend based on Spring Boot and Vue. | — |
| [wechat-article-publisher-skill](https://skillsmp.com/creators/iamzifei/wechat-article-publisher-skill/skills-wechat-article-publisher) | — | — | Claude/Codex skill for publishing WeChat articles via skillsmp.com. | — |

## ✍️ Article Drafting & AI Writing

| Tool | ⭐ | Language | Description | License |
| --- | --- | --- | --- | --- |
| [wechat-publisher](https://github.com/jiji262/wechat-publisher) | 132 | HTML | A Claude Code/Codex/Cursor skill and CLI that researches topics, writes 3000-5000 word WeChat articles, generates images, and publishes drafts to WeChat Official Accounts. | — |
| [ai-wechat](https://github.com/YuppyChen/ai-wechat) | 60 | TypeScript | A Claude Code-based workflow for creating and publishing WeChat Official Account articles from ideas through Markdown drafting, formatting, and HTML publishing. | — |
| [wechat-ai-publisher](https://github.com/bbwdadfg/wechat-ai-publisher) | 37 | Shell | An agent skill that collects AI trends, writes WeChat Official Account articles, generates images, and publishes drafts to WeChat. | MIT |
| [fengyun-publish](https://github.com/duliangkuan/fengyun-publish) | 20 | Python | A 19-step end-to-end AI pipeline for WeChat Official Accounts that picks topics, researches, writes, reviews, lays out, and pushes drafts. | MIT |
| [wechat-article-agent](https://github.com/ymstar/wechat-article-agent) | 7 | Python | A LangChain/LangGraph agent that researches a topic, writes an article, creates a cover image, audits content, and publishes to a WeChat Official Account draft box. | Apache-2.0 |
| [wechat-article-generator](https://github.com/icebear0828/wechat-article-generator) | 7 | Python | An end-to-end WeChat Official Account article pipeline that uses AI to write, generate images, censor sensitive words, render WeChat-compatible HTML, and copy it for posting. | — |
| [wechat-article-writing-skill](https://github.com/AlexLaoBai/wechat-article-writing-skill) | 4 | Python | A WeChat Official Account automated writing and publishing skill with auto and guided modes, multiple themes, and one-click draft push. | MIT |
| [weblog-skills](https://github.com/szsip239/weblog-skills) | 4 | JavaScript | A Markdown-to-WeChat publishing skill with AI style writing, doocs/md HTML rendering, AI humanization, and one-click draft push. | — |

## 🖼️ Media & Asset Management

| Tool | ⭐ | Language | Description | License |
| --- | --- | --- | --- | --- |
| [doocs/md](https://github.com/doocs/md) | 12946 | TypeScript | Concise WeChat Markdown editor with custom themes, content management, multi-image hosting, and AI assistance. | WTFPL |
| [markdown-nice](https://github.com/mdnice/markdown-nice) | 4647 | JavaScript | Markdown editor with theme design for producing nicely formatted articles, commonly used for WeChat official accounts. | GPL-3.0 |
| [wechat-format](https://github.com/lyricat/wechat-format) | 4535 | JavaScript | WeChat Official Account layout editor that converts Markdown to WeChat-specific HTML. | — |
| [silk-v3-decoder](https://github.com/kn007/silk-v3-decoder) | 3154 | C | Decodes Silk v3 audio files from WeChat/QQ and converts them to formats such as MP3. | MIT |
| [online-markdown](https://github.com/barretlee/online-markdown) | 921 | JavaScript | Online markdown converter specially designed for WeChat public account formatting. | Other |
| [xiaohu-wechat-format](https://github.com/xiaohuailabs/xiaohu-wechat-format) | 644 | Python | Claude Code skill for one-click WeChat official account formatting and publishing, converting Markdown to WeChat-compatible HTML drafts. | — |

## 📊 Analytics & Monitoring

| Tool | ⭐ | Language | Description | License |
| --- | --- | --- | --- | --- |
| [WeChatDataAnalysis](https://github.com/LifeArchiveProject/WeChatDataAnalysis) | 1516 | Python | Decrypts WeChat 4.x data and generates annual summaries, chat records, and Moments exports for analysis. | — |
| [sentry-miniapp](https://github.com/lizhiyao/sentry-miniapp) | 667 | TypeScript | SDK for error and performance monitoring of WeChat Mini Programs and other mini-app platforms. | MIT |
| [WeChat-Data-Analysis](https://github.com/allen1881996/WeChat-Data-Analysis) | 463 | Python | Extracts and analyzes iPhone and MacBook WeChat chat history from local databases. | MIT |
| [wechat_articles_spider](https://github.com/ghh1251/wechat_articles_spider) | 341 | Python | Crawls WeChat Official Account public articles for collection and analysis without packet capture. | MIT |
| [wechat-data-tools](https://github.com/Agentchengfeng/wechat-data-tools) | 80 | Python | Monitors WeChat Official Account articles, fetches engagement data, and generates visual reports. | — |
| [mini-program-monitor](https://github.com/SkyAPM/mini-program-monitor) | 8 | TypeScript | Apache SkyWalking monitoring client for WeChat and Alipay Mini Programs. | Apache-2.0 |
| [clickstream-wechat](https://github.com/awslabs/clickstream-wechat) | 5 | TypeScript | AWS Clickstream analytics SDK for WeChat Mini Programs. | Apache-2.0 |
| [wechat-data-analysis](https://github.com/yanzhenjia/wechat-data-analysis) | 1 | Python | Local analytics tool for WeChat Official Account articles. | MIT |

## 🔄 Multi-Platform Publishing to WeChat

| Tool | ⭐ | Language | Description | License |
| --- | --- | --- | --- | --- |
| [mdeditor](https://github.com/xiaobox/mdeditor) | 668 | JavaScript | A Markdown editor and social-platform publisher that converts Markdown into WeChat-optimized rich text for one-click publishing to WeChat Official Accounts and other social platforms. | MIT |
| [SyncCaster](https://github.com/RyanYipeng/SyncCaster) | 431 | TypeScript | A Chrome extension that converts self-written or captured web articles to Markdown and uses DOM automation to publish them to WeChat Official Accounts, Juejin, CSDN, Zhihu, and other platforms. | MIT |
| [lovpen-obsidian](https://github.com/MarkShawn2020/lovpen-obsidian) | 11 | TypeScript | An Obsidian plugin that formats notes once and distributes them to WeChat, Zhihu, XiaoHongShu, and Twitter. | MIT |
| [mulit-article-publisher](https://github.com/meijintao233/mulit-article-publisher) | 8 | JavaScript | A multi-platform article publisher that posts articles to Juejin, WeChat, Toutiao, Zhihu, and tech blogs. | MIT |
| [multi-platform-publisher](https://github.com/mguozhen/multi-platform-publisher) | 6 | Python | A command-line tool that publishes content to X/Twitter, LinkedIn, WeChat Official Accounts, and Xiaohongshu. | MIT |
| [obsidian-md-publisher](https://github.com/volcanicll/obsidian-md-publisher) | 2 | TypeScript | An Obsidian plugin that one-clicks to publish Markdown notes to WeChat Official Accounts, Zhihu, Toutiao, and Xiaohongshu. | MIT |
| [wechat-publisher](https://github.com/RanceLee233/wechat-publisher) | 2 | JavaScript | An Obsidian plugin that publishes Markdown notes directly as drafts to WeChat Official Accounts. | MIT |
| [Notion2wechatMP](https://github.com/royrenwb/Notion2wechatMP) | 1 | JavaScript | A tool that finds articles in Notion and automatically sends them to WeChat Official Account drafts. | — |

## 🔌 Official Account SDKs & API Wrappers

| Tool | ⭐ | Language | Description | License |
| --- | --- | --- | --- | --- |
| [weui](https://github.com/Tencent/weui) | 27387 | HTML/CSS | Official WeChat UI library by Tencent for mobile web applications. | Other |
| [EasyWeChat](https://github.com/w7corp/easywechat) | 10373 | PHP | PHP SDK for WeChat official account and mini program development. | MIT |
| [wechatpy](https://github.com/wechatpy/wechatpy) | 4291 | Python | Python SDK for WeChat official account, mini program, and payment APIs. | MIT |
| [wechat-python-sdk](https://github.com/doraemonext/wechat-python-sdk) | 1348 | Python | Python development kit for the WeChat public platform (deprecated). | BSD-2-Clause |

## 🌐 Browser Automation / RPA for WeChat

| Tool | ⭐ | Language | Description | License |
| --- | --- | --- | --- | --- |
| [wxauto](https://github.com/cluic/wxauto) | 7151 | Python | Automates the Windows WeChat desktop client for sending and receiving messages and building simple WeChat bots. | Apache-2.0 |
| [pywechat](https://github.com/Hello-Mr-Crab/pywechat) | 1658 | Python | Automates the Windows WeChat desktop client via pywinauto to perform most PC WeChat operations. | — |
| [robotic-process-automation](https://github.com/yihleego/robotic-process-automation) | 308 | Java | Java RPA framework for automating WeChat and WeCom desktop clients. | MIT |
| [WeChatMediaPlatformAutomation](https://github.com/LinusLing/WeChatMediaPlatformAutomation) | 214 | JavaScript | Publishes or previews articles on the WeChat Official Account web platform (mp.weixin.qq.com) using Puppeteer. | MIT |
| [WeChatAuto.SDK](https://github.com/scottfly189/WeChatAuto.SDK) | 188 | C# | .NET UI-automation SDK for WeChat RPA, supporting messaging, group/friend management, and Moments operations. | MIT |
| [agent-wechat](https://github.com/thisnick/agent-wechat) | 110 | Rust | RPA-based WeChat automation tool written in Rust. | — |
| [wechat-rpa-bot-skill](https://github.com/LeoMusk/wechat-rpa-bot-skill) | 65 | Python | WeChat RPA skill for AI agents, supporting headless operation and REST API control. | — |
| [wechat-daily-report-bot](https://github.com/perrycan/wechat-daily-report-bot) | 34 | Python | Automates daily work-report roll-call in WeChat groups using wxauto and FastAPI. | MIT |

## 🧩 Related: Mini Program Automation

| Tool | ⭐ | Language | Description | License |
| --- | --- | --- | --- | --- |
| [mini-ci](https://github.com/ruochuan12/mini-ci) | 220 | TypeScript | Enhanced CLI wrapper around the official miniprogram-ci supporting batch and multi-project WeChat Mini Program upload, preview, and configuration-driven CI workflows. | MIT |
| [miniprogram-deploy](https://github.com/sunxiuguo/miniprogram-deploy) | 26 | TypeScript | Automation tool that wraps miniprogram-ci to upload and preview WeChat Mini Programs. | — |
| [wx-ci](https://github.com/jaluik/wx-ci) | 18 | TypeScript | One-click command-line script for packaging, uploading, and previewing WeChat Mini Programs without opening WeChat DevTools. | MIT |
| [actions.mini-program](https://github.com/echoings/actions.mini-program) | 14 | TypeScript | GitHub Action that wraps miniprogram-ci for automated WeChat Mini Program preview and upload in CI/CD pipelines. | MIT |
| [miniprogram-automator-extension](https://github.com/nchejara/miniprogram-automator-extension) | 13 | JavaScript | Functional extension library that simplifies end-to-end testing of WeChat Mini Programs with the official miniprogram-automator. | — |
| [miniprogram-remote-control](https://github.com/LSTM-Kirigaya/miniprogram-remote-control) | 3 | JavaScript | CLI remote-control wrapper around miniprogram-automator to automate clicks, text input, screenshots, tab switching, and relaunching of WeChat Mini Programs. | — |
| [miniprogram-ci](https://www.npmjs.com/package/miniprogram-ci) | — | JavaScript | Official Tencent package for building, uploading, previewing, and publishing WeChat Mini Programs from the command line without the WeChat DevTools GUI. | — |
| [miniprogram-automator](https://www.npmjs.com/package/miniprogram-automator) | — | JavaScript | Official Tencent SDK that automates the WeChat DevTools to launch WeChat Mini Programs and simulate user actions for testing. | — |

## 🏢 Related: Enterprise WeChat Automation

| Tool | ⭐ | Language | Description | License |
| --- | --- | --- | --- | --- |
| [LangBot](https://github.com/langbot-app/LangBot) | 16600 | Python | A production-grade multi-platform chatbot framework that supports Enterprise WeChat/WeCom, enabling AI agent customer service and workflow integrations with n8n/Dify. | Apache-2.0 |
| [wecom-cli](https://github.com/WecomTeam/wecom-cli) | 2400 | Rust | An official-style command-line interface for Enterprise WeChat that lets humans and AI agents operate WeCom from the terminal, including messaging, contacts, tasks, and meetings. | MIT |
| [go-wecom](https://github.com/wenerme/go-wecom) | 98 | Go | A Go SDK for WeChat Work that wraps over 500 generated API endpoints across 37 functional categories to build Enterprise WeChat automations. | Apache-2.0 |
| [wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server) | 96 | Python | An MCP server that exposes tools for AI assistants to send messages, files, images, and template-card notifications to WeCom/Enterprise WeChat group chats via the official bot webhook API. | MIT |
| [wecombot](https://github.com/voidint/wecombot) | 9 | Go | A lightweight Go SDK for WeCom group chat robots that sends text, Markdown, images, files, voice, news, and template-card messages with zero third-party dependencies. | MIT |
| [wechat_work_webhook_rb](https://github.com/mqzhang/wechat_work_webhook_rb) | 4 | Ruby | A Ruby client for Enterprise WeChat group chat bot webhooks supporting text, Markdown, image, news article, and file message types. | MIT |

## 🤖 Related: WeChat Bots & Customer Service

| Tool | ⭐ | Language | Description | License |
| --- | --- | --- | --- | --- |
| [CowAgent](https://github.com/zhayujie/CowAgent) | 45760 | Python | Open-source AI assistant and agent harness (formerly chatgpt-on-wechat) that supports multi-channel deployment including WeChat. | MIT |
| [ItChat](https://github.com/littlecodersh/ItChat) | 26472 | Python | Complete and graceful API for WeChat personal accounts that enables building a personal WeChat bot in a few dozen lines of code. | MIT |
| [wechaty](https://github.com/wechaty/wechaty) | 22889 | TypeScript | Conversational RPA SDK that lets developers build chatbots for WeChat and other messaging platforms. | Apache-2.0 |
| [wechat-bot](https://github.com/wangrongding/wechat-bot) | 11130 | JavaScript | WeChat bot built on WeChaty that connects ChatGPT, Claude, Kimi, DeepSeek and Ollama to auto-reply messages and manage groups/friends. | MIT |
| [WeChatFerry](https://github.com/lich0821/WeChatFerry) | 6748 | C++ | WeChat hook-based robot framework that can integrate DeepSeek, Gemini, ChatGPT, ChatGLM and other large models. | MIT |
| [ChatGPT-wechat-bot](https://github.com/AutumnWhj/ChatGPT-wechat-bot) | 4720 | TypeScript | ChatGPT bot for WeChat that deploys OpenAI conversations through the Wechaty framework. | MIT |
| [wechat-gptbot](https://github.com/iuiaoin/wechat-gptbot) | 609 | Python | Stable WeChat robot based on ChatGPT designed for low-risk personal-account automation. | MIT |
| [BotFramework-WeChat](https://github.com/microsoft/BotFramework-WeChat) | 69 | C# | Adapter that enables Microsoft BotFramework bots to send and receive messages on WeChat. | MIT |

## 🛠️ CLI / Developer Utilities

| Tool | ⭐ | Language | Description | License |
| --- | --- | --- | --- | --- |
| [vConsole](https://github.com/Tencent/vConsole) | 17494 | TypeScript | Lightweight, extendable front-end developer tool for debugging mobile web pages inside WeChat webview. | Other |
| [wechat-spider (bowenpay)](https://github.com/bowenpay/wechat-spider) | 3354 | Python | WeChat official account spider for crawling public account articles and metadata. | — |
| [wechat-spider (striver-ing)](https://github.com/striver-ing/wechat-spider) | 2872 | Python | Open-source WeChat spider that crawls articles, views, likes, and comments from official accounts. | — |
| [wechat_spider (lqqyt2423)](https://github.com/lqqyt2423/wechat_spider) | 1538 | JavaScript | WeChat spider that fetches article content, views, likes, comments, and historical article links. | MIT |
| [wechat-cli](https://github.com/huohuoer/wechat-cli) | 1499 | Python | A command-line tool that queries local WeChat data—chat history, contacts, sessions, and favorites—for LLM integration and analysis. | Apache-2.0 |
| [Mojo-Weixin](https://github.com/hexsum/Mojo-Weixin) | 1251 | Perl | A non-GUI personal WeChat client framework with an plugin-based HTTP API for automation and chatbot development. | MIT |
| [wx-cli](https://github.com/pandorafuture/wx-cli) | 103 | Rust | A command-line tool to decrypt and query WeChat macOS local databases for contacts, messages, and sessions. | MIT |
| [Wechat-Claude-bot](https://github.com/mrliuzhiyu/Wechat-Claude-bot) | 33 | Python | A WeChat bot that lets you remotely control the Claude Code CLI to execute commands and manage projects from your phone. | GPL-3.0 |
| [clawbot](https://github.com/adysec/clawbot) | 30 | Rust | An iLink bot management tool providing a command-line interface and web dashboard for WeChat automation. | — |
| [wechat-cli](https://github.com/systemxlabs/wechat-cli) | 22 | Rust | A CLI for interacting with a WeChat iLink bot to send, receive, and manage WeChat messages from the terminal. | MIT |
| [wechat-devtool](https://github.com/NewFuture/wechat-devtool) | 6 | TypeScript | A cross-platform command-line wrapper for invoking the WeChat MiniProgram developer tools in Node.js and npm projects. | MIT |

## Quick Selection Guide

- **End-to-end WeChat article publishing** → [wechat-publisher](https://github.com/jiji262/wechat-publisher) — Claude/Codex skill and CLI that researches, writes, and publishes drafts.
- **Format Markdown for WeChat** → [doocs/md](https://github.com/doocs/md) — popular Markdown editor with WeChat theme and image hosting.
- **Build WeChat chatbots** → [wechaty](https://github.com/wechaty/wechaty) — conversational RPA SDK for WeChat bots.
- **WeChat Official Account SDK (Python)** → [wechatpy](https://github.com/wechatpy/wechatpy) — Python SDK for official account and mini program APIs.
- **Automate Windows WeChat desktop** → [wxauto](https://github.com/cluic/wxauto) — UI automation for Windows WeChat.
- **Enterprise WeChat webhooks** → [wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server) — MCP server for WeCom group bot notifications.
- **Mini Program CI/CD** → [miniprogram-ci](https://www.npmjs.com/package/miniprogram-ci) — official Tencent CLI for building and uploading mini programs.
- **WeChat data analytics** → [wechat_articles_spider](https://github.com/ghh1251/wechat_articles_spider) — crawl public WeChat articles for analysis.

## Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Please provide tool name, link, star count, primary language, one-sentence description, license, and category.

## Acknowledgments

Thanks to all the open-source WeChat automation projects and their maintainers.

## Star History

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Lxcardoza993/awesome-wechat-automation&type=Date&theme=dark">
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Lxcardoza993/awesome-wechat-automation&type=Date">
  <img alt="Star History" src="https://api.star-history.com/svg?repos=Lxcardoza993/awesome-wechat-automation&type=Date">
</picture>

## License

List content is dedicated to the public domain under [CC0-1.0](LICENSE). Each tool retains its own license.
