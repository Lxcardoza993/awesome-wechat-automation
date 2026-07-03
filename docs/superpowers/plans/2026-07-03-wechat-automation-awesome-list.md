# Awesome WeChat Automation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create and publish `Lxcardoza993/awesome-wechat-automation`, a bilingual high-star-style awesome list focused on WeChat Official Account auto-publishing/operations automation, plus related WeChat ecosystem tools.

**Architecture:** A static GitHub repository containing English and Chinese READMEs, a CC0-1.0 license, and a contributing guide. Content is curated via parallel research subagents that gather tool metadata; a final synthesis agent assembles the READMEs.

**Tech Stack:** Markdown, Git, GitHub CLI (`gh`), shields.io, star-history.com.

## Global Constraints

- Repository visibility: **public** (user explicitly requested public).
- License: **CC0-1.0** for list content; each listed tool keeps its own license.
- README style must match `awesome-api-key-leak-detection` and `awesome-voice2text`: badges, language switcher, categorized tables, star history chart.
- Minimum deliverable: ≥8 categories, ≥30 tools, English + Chinese READMEs.
- Descriptions must be factual, one-sentence, no marketing fluff.
- All external tool metadata must be verified against live GitHub/GitLab pages where possible.

---

### Task 1: Research & gather candidate tools

**Files:**
- Create: `data/raw-tools-{en,zh}.jsonl` (temporary working files)
- Output: `data/tools.csv`

**Interfaces:**
- Consumes: design spec, seed URLs from user.
- Produces: a CSV/JSON list of candidate tools with fields: `name, url, category, stars, language, license, description_en, description_zh, notes`.

- [ ] **Step 1: Seed list compilation**
  ```bash
  mkdir -p /home/li/awesome-wechat-automation/data
  ```
  Write seed entries for the four user-provided links into `data/seed-tools.csv`.

- [ ] **Step 2: Parallel web research via subagents**
  Dispatch multiple subagents (one per category) to search GitHub for WeChat automation tools. Search queries:
  - `wechat official account publish automation github`
  - `wechat mp publisher automation github`
  - `wechat article auto publish github`
  - `wechat bot automation github`
  - `wechat work automation github`
  - `wechat mini program automation github`
  Each subagent returns a JSON list of up to 10 tools with name, URL, stars, language, license, description.

- [ ] **Step 3: Deduplicate and verify**
  Merge subagent outputs, remove duplicates (by repo URL), verify star counts and primary languages via `gh api repos/{owner}/{repo}` or web fetch. Write final `data/tools.csv`.

- [ ] **Step 4: Commit**
  ```bash
  git init
  git add data/tools.csv data/seed-tools.csv
  git commit -m "chore: initial tool research dataset"
  ```

---

### Task 2: Draft English README

**Files:**
- Create: `README.md`
- Reference: `awesome-api-key-leak-detection/README.md`, `awesome-voice2text/README.md`

**Interfaces:**
- Consumes: `data/tools.csv`
- Produces: `README.md`

- [ ] **Step 1: Write header & badges**
  Include:
  - Title: `# 🚀 Awesome WeChat Automation`
  - Badges: Awesome, License, Last Commit, PRs Welcome, Tools count
  - Language switcher: English · 简体中文

- [ ] **Step 2: Write categories as tables**
  Use category headers with emojis. Table columns: `Tool | ⭐ | Language | Description | License`.
  Categories:
  - 📝 Official Account Auto-Publishing
  - ✍️ Article Drafting & AI Writing
  - 🖼️ Media & Asset Management
  - 📊 Analytics & Monitoring
  - 🔄 Multi-Platform Publishing to WeChat
  - 🔌 Official Account SDKs & API Wrappers
  - 🌐 Browser Automation / RPA for WeChat
  - 🧩 Related: Mini Program Automation
  - 🏢 Related: Enterprise WeChat Automation
  - 🤖 Related: WeChat Bots & Customer Service
  - 🛠️ CLI / Developer Utilities

- [ ] **Step 3: Add quick selection guide, contributing, acknowledgments, star history, license**

- [ ] **Step 4: Commit**
  ```bash
  git add README.md
  git commit -m "docs: add English README"
  ```

---

### Task 3: Draft Chinese README

**Files:**
- Create: `README.zh-CN.md`

**Interfaces:**
- Consumes: `README.md`
- Produces: `README.zh-CN.md`

- [ ] **Step 1: Translate/adapt README.md to Chinese**
  Preserve all links and table structure. Translate descriptions to natural Chinese.

- [ ] **Step 2: Update language switcher**
  Ensure switcher points correctly to `README.md` and `README.zh-CN.md`.

- [ ] **Step 3: Commit**
  ```bash
  git add README.zh-CN.md
  git commit -m "docs: add Chinese README"
  ```

---

### Task 4: Add LICENSE and CONTRIBUTING.md

**Files:**
- Create: `LICENSE`
- Create: `CONTRIBUTING.md`

**Interfaces:**
- Consumes: design spec
- Produces: `LICENSE`, `CONTRIBUTING.md`

- [ ] **Step 1: Write CC0-1.0 LICENSE**
  Use the standard CC0 legal text.

- [ ] **Step 2: Write CONTRIBUTING.md (bilingual)**
  Include: how to propose a tool, required fields, description style, no marketing fluff.

- [ ] **Step 3: Commit**
  ```bash
  git add LICENSE CONTRIBUTING.md
  git commit -m "chore: add CC0 license and contributing guide"
  ```

---

### Task 5: Create GitHub repo and push

**Files:**
- Modify: `.git/config` (via `git remote add`)

**Interfaces:**
- Consumes: local repository
- Produces: remote GitHub repository

- [ ] **Step 1: Create public GitHub repository**
  ```bash
  gh repo create Lxcardoza993/awesome-wechat-automation --public --description "A curated list of WeChat Official Account automation and related WeChat ecosystem tools." --source=. --push
  ```

- [ ] **Step 2: Verify remote and push**
  ```bash
  git remote -v
  git push -u origin main
  ```

---

### Task 6: Verify publication

**Files:** None (read-only checks)

- [ ] **Step 1: Confirm public visibility**
  ```bash
  gh api repos/Lxcardoza993/awesome-wechat-automation --jq '.visibility'
  ```
  Expected output: `PUBLIC`

- [ ] **Step 2: Confirm README renders**
  ```bash
  gh api repos/Lxcardoza993/awesome-wechat-automation/readme --jq '.name'
  ```
  Expected output: `README.md`

---

## Self-Review Checklist

- [x] Spec coverage: all design sections map to a task.
- [x] No placeholders: each step has exact commands or content.
- [x] Type consistency: CSV fields used consistently across tasks.
- [x] Public visibility explicitly enforced via `--public` flag.
