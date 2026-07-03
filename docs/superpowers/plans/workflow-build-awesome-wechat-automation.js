export const meta = {
  name: "build-awesome-wechat-automation",
  description: "Research, compile, and publish the awesome-wechat-automation list with subagent-driven execution.",
  phases: [
    { title: "Research", detail: "Parallel category research for WeChat automation tools" },
    { title: "Synthesize", detail: "Generate and write English and Chinese READMEs" },
    { title: "Publish", detail: "Add license/contributing, initialize repo, create GitHub repo, push" }
  ]
};

const CATEGORIES = [
  { key: "auto-publishing", name: "Official Account Auto-Publishing", queries: ["wechat official account auto publish github", "wechat mp publisher automation github", "wechat article publisher automation github"] },
  { key: "ai-writing", name: "Article Drafting & AI Writing", queries: ["wechat article ai writing github", "wechat official account ai writer github"] },
  { key: "media", name: "Media & Asset Management", queries: ["wechat media asset management github", "wechat official account image material github"] },
  { key: "analytics", name: "Analytics & Monitoring", queries: ["wechat official account analytics github", "wechat mp data monitor github"] },
  { key: "multi-platform", name: "Multi-Platform Publishing to WeChat", queries: ["notion to wechat publisher github", "markdown to wechat official account github"] },
  { key: "sdk", name: "Official Account SDKs & API Wrappers", queries: ["wechat official account sdk github", "wechat mp api wrapper github"] },
  { key: "browser-rpa", name: "Browser Automation / RPA for WeChat", queries: ["wechat web automation playwright github", "wechat official account rpa github"] },
  { key: "miniprogram", name: "Mini Program Automation", queries: ["wechat mini program automation github", "wechat miniprogram ci github"] },
  { key: "wecom", name: "Enterprise WeChat Automation", queries: ["wecom automation github", "enterprise wechat automation github"] },
  { key: "bots", name: "WeChat Bots & Customer Service", queries: ["wechat bot automation github", "wechat personal account bot github"] },
  { key: "cli", name: "CLI / Developer Utilities", queries: ["wechat cli tool github", "wechat developer utility github"] }
];

const SEED_TOOLS = [
  { name: "wx-manage", url: "https://github.com/niefy/wx-manage", category: "auto-publishing", stars: 0, language: "Java", license: "", description_en: "WeChat Official Account management backend (Vue + Spring Boot)." },
  { name: "wechat-publisher", url: "https://github.com/jiji262/wechat-publisher", category: "auto-publishing", stars: 0, language: "Python", license: "", description_en: "Automated publishing tool for WeChat Official Accounts." },
  { name: "wechat-publisher", url: "https://github.com/xiaonan0527/wechat-publisher", category: "auto-publishing", stars: 0, language: "Python", license: "", description_en: "Another automated WeChat Official Account publisher." },
  { name: "wechat-article-publisher-skill", url: "https://skillsmp.com/creators/iamzifei/wechat-article-publisher-skill/skills-wechat-article-publisher", category: "auto-publishing", stars: 0, language: "—", license: "", description_en: "Claude/Codex skill for publishing WeChat articles." }
];

phase("Research");

const researchResults = await parallel(
  CATEGORIES.map(cat => () => agent(
    `Research WeChat automation tools for category: "${cat.name}" (key: ${cat.key}).
Use web search and GitHub search with these queries: ${cat.queries.join("; ")}.
Return up to 8 relevant open-source tools. For each tool include:
- name: repository name
- url: GitHub or primary source URL
- stars: approximate star count (integer, 0 if unknown)
- language: primary programming language (empty if unknown)
- license: license if known, else empty string
- description_en: one factual sentence describing what it does for WeChat automation
- category: "${cat.key}"
Avoid generic tools without WeChat-specific support. Prioritize actively maintained repos with clear WeChat features.`,
    { label: `research:${cat.key}`, phase: "Research", schema: {
      type: "object",
      properties: { tools: { type: "array", items: { type: "object", properties: {
        name: { type: "string" },
        url: { type: "string" },
        stars: { type: "integer" },
        language: { type: "string" },
        license: { type: "string" },
        description_en: { type: "string" },
        category: { type: "string" }
      }, required: ["name", "url", "stars", "language", "description_en", "category"] } } },
      required: ["tools"]
    } }
  ))
);

const allTools = new Map();
SEED_TOOLS.forEach(t => allTools.set(t.url, t));
researchResults.filter(Boolean).forEach(r => r.tools.forEach(t => {
  if (!allTools.has(t.url)) allTools.set(t.url, t);
}));
const tools = Array.from(allTools.values());
log(`Collected ${tools.length} unique tools.`);

phase("Synthesize");

const toolsJson = JSON.stringify(tools);
const categoriesJson = JSON.stringify(CATEGORIES.map(c => ({ key: c.key, name: c.name })));

const writeTasks = await parallel([
  () => agent(
    `Write the English README.md for /home/li/awesome-wechat-automation/README.md.
Repository: Lxcardoza993/awesome-wechat-automation
Tool data: ${toolsJson}
Categories: ${categoriesJson}

Requirements:
- Title with emoji and these badges: Awesome, License: CC0-1.0, Last Commit, PRs Welcome, Tools count
- Language switcher: [English](README.md) · [简体中文](README.zh-CN.md)
- "Why this list" / description paragraph
- Table of Contents with anchor links to each category
- For each category, a markdown table with columns: Tool, ⭐, Language, Description, License
- A "Quick Selection Guide" section
- A "Contributing" section with link to CONTRIBUTING.md
- An "Acknowledgments" section
- A "Star History" section using picture/source for dark/light mode with URL: https://api.star-history.com/svg?repos=Lxcardoza993/awesome-wechat-automation&type=Date
- A "License" section stating CC0-1.0 and linking to LICENSE
- Descriptions must be factual, one sentence, no marketing fluff.

Use the Write tool to create /home/li/awesome-wechat-automation/README.md with the full content. Then return { "files": ["README.md"] }.`,
    { label: "write:README.md", phase: "Synthesize", schema: { type: "object", properties: { files: { type: "array", items: { type: "string" } } }, required: ["files"] } }
  ),
  () => agent(
    `Write the Chinese README.zh-CN.md for /home/li/awesome-wechat-automation/README.zh-CN.md.
Repository: Lxcardoza993/awesome-wechat-automation
Tool data: ${toolsJson}
Categories: ${categoriesJson}

Requirements:
- Title with emoji and badges
- Language switcher: [English](README.md) · [简体中文](README.zh-CN.md)
- "为什么有这份清单" description in Chinese
- 目录 with anchor links
- For each category, a markdown table with columns: 工具, ⭐, 语言, 描述, 许可证
- "快速选型指南" section
- "贡献" section linking to CONTRIBUTING.md
- "致谢" section
- "Star History" section with dark/light picture/sources using URL: https://api.star-history.com/svg?repos=Lxcardoza993/awesome-wechat-automation&type=Date
- "许可证" section stating CC0-1.0 and linking to LICENSE
- Descriptions in natural, concise Chinese. Factual, no marketing fluff.

Use the Write tool to create /home/li/awesome-wechat-automation/README.zh-CN.md with the full content. Then return { "files": ["README.zh-CN.md"] }.`,
    { label: "write:README.zh-CN.md", phase: "Synthesize", schema: { type: "object", properties: { files: { type: "array", items: { type: "string" } } }, required: ["files"] } }
  )
]);

log(`Synthesized files: ${writeTasks.filter(Boolean).flatMap(t => t.files).join(", ")}`);

phase("Publish");

const publishResult = await agent(
  `Complete publication of the awesome-wechat-automation repository.

Tool data to save as /home/li/awesome-wechat-automation/data/tools.json (pretty printed):
${toolsJson}

Tasks:
1. Create /home/li/awesome-wechat-automation/LICENSE with standard CC0-1.0 legal text.
2. Create /home/li/awesome-wechat-automation/CONTRIBUTING.md with a bilingual (English/Chinese) guide. Include: how to propose a tool, required fields (name, link, stars, language, one-sentence description, license, category), and style rules (factual, no marketing).
3. Create /home/li/awesome-wechat-automation/data/tools.json with the JSON above.
4. Initialize git in /home/li/awesome-wechat-automation if not already done.
5. Stage all files and commit with message: "docs: initial awesome-wechat-automation list"
6. Create public GitHub repo and push:
   gh repo create Lxcardoza993/awesome-wechat-automation --public --description "A curated list of WeChat Official Account automation and related WeChat ecosystem tools." --source=. --push
   If it fails because repo exists, run: git remote add origin https://github.com/Lxcardoza993/awesome-wechat-automation.git && git push -u origin main --force
7. Verify with: gh api repos/Lxcardoza993/awesome-wechat-automation --jq '.visibility'
8. Verify README with: gh api repos/Lxcardoza993/awesome-wechat-automation/readme --jq '.name'

Return a JSON object: { success: boolean, visibility: string, readme_name: string, files_created: string[], errors: string }`,
  { label: "publish:repo", phase: "Publish", schema: { type: "object", properties: {
    success: { type: "boolean" },
    visibility: { type: "string" },
    readme_name: { type: "string" },
    files_created: { type: "array", items: { type: "string" } },
    errors: { type: "string" }
  }, required: ["success"] } }
);

log(`Published: success=${publishResult.success}, visibility=${publishResult.visibility}, readme=${publishResult.readme_name}`);

const result = {
  tools_count: tools.length,
  files: writeTasks.filter(Boolean).flatMap(t => t.files),
  publish: publishResult
};

log(`Result: ${JSON.stringify(result)}`);
