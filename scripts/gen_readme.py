import json
from collections import OrderedDict, defaultdict

# Load extracted tools
with open('/home/li/awesome-wechat-automation/data/tools.json', 'r', encoding='utf-8') as f:
    tools = json.load(f)

# Add missing category tools from research agent
missing = [
  {
    "name": "doocs/md",
    "url": "https://github.com/doocs/md",
    "stars": 12946,
    "language": "TypeScript",
    "license": "WTFPL",
    "description_en": "Concise WeChat Markdown editor with custom themes, content management, multi-image hosting, and AI assistance.",
    "category": "media"
  },
  {
    "name": "markdown-nice",
    "url": "https://github.com/mdnice/markdown-nice",
    "stars": 4647,
    "language": "JavaScript",
    "license": "GPL-3.0",
    "description_en": "Markdown editor with theme design for producing nicely formatted articles, commonly used for WeChat official accounts.",
    "category": "media"
  },
  {
    "name": "wechat-format",
    "url": "https://github.com/lyricat/wechat-format",
    "stars": 4535,
    "language": "JavaScript",
    "license": "",
    "description_en": "WeChat Official Account layout editor that converts Markdown to WeChat-specific HTML.",
    "category": "media"
  },
  {
    "name": "online-markdown",
    "url": "https://github.com/barretlee/online-markdown",
    "stars": 921,
    "language": "JavaScript",
    "license": "Other",
    "description_en": "Online markdown converter specially designed for WeChat public account formatting.",
    "category": "media"
  },
  {
    "name": "silk-v3-decoder",
    "url": "https://github.com/kn007/silk-v3-decoder",
    "stars": 3154,
    "language": "C",
    "license": "MIT",
    "description_en": "Decodes Silk v3 audio files from WeChat/QQ and converts them to formats such as MP3.",
    "category": "media"
  },
  {
    "name": "xiaohu-wechat-format",
    "url": "https://github.com/xiaohuailabs/xiaohu-wechat-format",
    "stars": 644,
    "language": "Python",
    "license": "",
    "description_en": "Claude Code skill for one-click WeChat official account formatting and publishing, converting Markdown to WeChat-compatible HTML drafts.",
    "category": "media"
  },
  {
    "name": "weui",
    "url": "https://github.com/Tencent/weui",
    "stars": 27387,
    "language": "HTML/CSS",
    "license": "Other",
    "description_en": "Official WeChat UI library by Tencent for mobile web applications.",
    "category": "sdk"
  },
  {
    "name": "EasyWeChat",
    "url": "https://github.com/w7corp/easywechat",
    "stars": 10373,
    "language": "PHP",
    "license": "MIT",
    "description_en": "PHP SDK for WeChat official account and mini program development.",
    "category": "sdk"
  },
  {
    "name": "wechatpy",
    "url": "https://github.com/wechatpy/wechatpy",
    "stars": 4291,
    "language": "Python",
    "license": "MIT",
    "description_en": "Python SDK for WeChat official account, mini program, and payment APIs.",
    "category": "sdk"
  },
  {
    "name": "wechat-python-sdk",
    "url": "https://github.com/doraemonext/wechat-python-sdk",
    "stars": 1348,
    "language": "Python",
    "license": "BSD-2-Clause",
    "description_en": "Python development kit for the WeChat public platform (deprecated).",
    "category": "sdk"
  },
  {
    "name": "vConsole",
    "url": "https://github.com/Tencent/vConsole",
    "stars": 17494,
    "language": "TypeScript",
    "license": "Other",
    "description_en": "Lightweight, extendable front-end developer tool for debugging mobile web pages inside WeChat webview.",
    "category": "cli"
  },
  {
    "name": "wechat-spider (bowenpay)",
    "url": "https://github.com/bowenpay/wechat-spider",
    "stars": 3354,
    "language": "Python",
    "license": "",
    "description_en": "WeChat official account spider for crawling public account articles and metadata.",
    "category": "cli"
  },
  {
    "name": "wechat-spider (striver-ing)",
    "url": "https://github.com/striver-ing/wechat-spider",
    "stars": 2872,
    "language": "Python",
    "license": "",
    "description_en": "Open-source WeChat spider that crawls articles, views, likes, and comments from official accounts.",
    "category": "cli"
  },
  {
    "name": "wechat_spider (lqqyt2423)",
    "url": "https://github.com/lqqyt2423/wechat_spider",
    "stars": 1538,
    "language": "JavaScript",
    "license": "MIT",
    "description_en": "WeChat spider that fetches article content, views, likes, comments, and historical article links.",
    "category": "cli"
  }
]

# Merge
existing_urls = {t['url'] for t in tools}
for t in missing:
    if t['url'] not in existing_urls:
        tools.append(t)
        existing_urls.add(t['url'])

# Add user seed tools that weren't discovered
seed_tools = [
  {
    "name": "wx-manage",
    "url": "https://github.com/niefy/wx-manage",
    "stars": 0,
    "language": "Java",
    "license": "",
    "description_en": "WeChat Official Account management backend based on Spring Boot and Vue.",
    "category": "auto-publishing"
  },
  {
    "name": "wechat-article-publisher-skill",
    "url": "https://skillsmp.com/creators/iamzifei/wechat-article-publisher-skill/skills-wechat-article-publisher",
    "stars": 0,
    "language": "—",
    "license": "",
    "description_en": "Claude/Codex skill for publishing WeChat articles via skillsmp.com.",
    "category": "auto-publishing"
  }
]
for t in seed_tools:
    if t['url'] not in existing_urls:
        tools.append(t)
        existing_urls.add(t['url'])

# Save
with open('/home/li/awesome-wechat-automation/data/tools.json', 'w', encoding='utf-8') as f:
    json.dump(tools, f, indent=2, ensure_ascii=False)

print(f"Total tools: {len(tools)}")

# Group by category order
CATEGORIES = [
    "auto-publishing",
    "ai-writing",
    "media",
    "analytics",
    "multi-platform",
    "sdk",
    "browser-rpa",
    "miniprogram",
    "wecom",
    "bots",
    "cli"
]

category_titles = {
    "auto-publishing": "📝 Official Account Auto-Publishing",
    "ai-writing": "✍️ Article Drafting & AI Writing",
    "media": "🖼️ Media & Asset Management",
    "analytics": "📊 Analytics & Monitoring",
    "multi-platform": "🔄 Multi-Platform Publishing to WeChat",
    "sdk": "🔌 Official Account SDKs & API Wrappers",
    "browser-rpa": "🌐 Browser Automation / RPA for WeChat",
    "miniprogram": "🧩 Related: Mini Program Automation",
    "wecom": "🏢 Related: Enterprise WeChat Automation",
    "bots": "🤖 Related: WeChat Bots & Customer Service",
    "cli": "🛠️ CLI / Developer Utilities",
}

groups = defaultdict(list)
for t in tools:
    groups[t['category']].append(t)

# Generate English README
lines = []
lines.append("# 🚀 Awesome WeChat Automation")
lines.append("")
lines.append("> A curated list of WeChat Official Account (微信公众号) auto-publishing and operation automation tools, plus related WeChat ecosystem automation.")
lines.append("")
lines.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg) ![Last Commit](https://img.shields.io/github/last-commit/Lxcardoza993/awesome-wechat-automation) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)")
lines.append("")
lines.append("**Languages**: [English](README.md) · [简体中文](README.zh-CN.md)")
lines.append("")
lines.append("*If this list is useful, please ⭐ the repo — it helps others find it.*")
lines.append("")
lines.append("## Contents")
lines.append("")
for cat in CATEGORIES:
    anchor = category_titles[cat].lower().replace(' ', '-').replace(':', '').replace('️', '').replace('/', '').replace('&', '')
    lines.append(f"- [{category_titles[cat]}](#{anchor})")
lines.append("- [Quick Selection Guide](#quick-selection-guide)")
lines.append("- [Contributing](#contributing)")
lines.append("- [Acknowledgments](#acknowledgments)")
lines.append("- [Star History](#star-history)")
lines.append("- [License](#license)")
lines.append("")
lines.append("## Why this list")
lines.append("")
lines.append("WeChat Official Account automation spans publishing, content formatting, media management, analytics, SDKs, and related WeChat/Mini Program/Enterprise WeChat tooling. This list collects open-source projects that make it easier to automate and extend WeChat workflows.")
lines.append("")

for cat in CATEGORIES:
    title = category_titles[cat]
    lines.append(f"## {title}")
    lines.append("")
    cat_tools = sorted(groups.get(cat, []), key=lambda x: -x['stars'])
    if not cat_tools:
        lines.append("*No tools found yet.*")
        lines.append("")
        continue
    lines.append("| Tool | ⭐ | Language | Description | License |")
    lines.append("| --- | --- | --- | --- | --- |")
    for t in cat_tools:
        name = f"[{t['name']}]({t['url']})"
        stars = t['stars'] if t['stars'] > 0 else '—'
        lang = t['language'] or '—'
        desc = t['description_en']
        lic = t['license'] or '—'
        lines.append(f"| {name} | {stars} | {lang} | {desc} | {lic} |")
    lines.append("")

lines.append("## Quick Selection Guide")
lines.append("")
lines.append("- **End-to-end WeChat article publishing** → [wechat-publisher](https://github.com/jiji262/wechat-publisher) — Claude/Codex skill and CLI that researches, writes, and publishes drafts.")
lines.append("- **Format Markdown for WeChat** → [doocs/md](https://github.com/doocs/md) — popular Markdown editor with WeChat theme and image hosting.")
lines.append("- **Build WeChat chatbots** → [wechaty](https://github.com/wechaty/wechaty) — conversational RPA SDK for WeChat bots.")
lines.append("- **WeChat Official Account SDK (Python)** → [wechatpy](https://github.com/wechatpy/wechatpy) — Python SDK for official account and mini program APIs.")
lines.append("- **Automate Windows WeChat desktop** → [wxauto](https://github.com/cluic/wxauto) — UI automation for Windows WeChat.")
lines.append("- **Enterprise WeChat webhooks** → [wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server) — MCP server for WeCom group bot notifications.")
lines.append("- **Mini Program CI/CD** → [miniprogram-ci](https://www.npmjs.com/package/miniprogram-ci) — official Tencent CLI for building and uploading mini programs.")
lines.append("- **WeChat data analytics** → [wechat_articles_spider](https://github.com/ghh1251/wechat_articles_spider) — crawl public WeChat articles for analysis.")
lines.append("")
lines.append("## Contributing")
lines.append("")
lines.append("Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Please provide tool name, link, star count, primary language, one-sentence description, license, and category.")
lines.append("")
lines.append("## Acknowledgments")
lines.append("")
lines.append("Thanks to all the open-source WeChat automation projects and their maintainers.")
lines.append("")
lines.append("## Star History")
lines.append("")
lines.append("<picture>")
lines.append('  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Lxcardoza993/awesome-wechat-automation&type=Date&theme=dark">')
lines.append('  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Lxcardoza993/awesome-wechat-automation&type=Date">')
lines.append('  <img alt="Star History" src="https://api.star-history.com/svg?repos=Lxcardoza993/awesome-wechat-automation&type=Date">')
lines.append("</picture>")
lines.append("")
lines.append("## License")
lines.append("")
lines.append("List content is dedicated to the public domain under [CC0-1.0](LICENSE). Each tool retains its own license.")
lines.append("")

readme_en = "\n".join(lines)
with open('/home/li/awesome-wechat-automation/README.md', 'w', encoding='utf-8') as f:
    f.write(readme_en)

print("README.md generated")
print(f"README length: {len(readme_en)} chars")
