---
title: "vercel/next.js v16.5.0-canary.12 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.12"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-15T05:11:53Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.12"
---

# vercel/next.js v16.5.0-canary.12 released

> Source: github-releases | Category: changelog | 2026-10-15T05:11:53Z

## vercel/next.js — v16.5.0-canary.12

### Core Changes

- Upgrade from pnpm v10 to v12: #99827

### Example Changes

- docs(examples): fix typo and update HTTP links to HTTPS in example READMEs: #99924

### Misc Changes

- Turbopack: Avoid `serde_json::RawValue` conversions in a few places: #97713
- docs: replace unbounded cacheHandler snippets and fix tag handling in examples: #100186
- Turbopack: don't treat events as relevant because their parent dir is in the watcher batch: #99782
- Fix CI for react 18.3: #100202
- docs: clarify ESLint 10 support: #100198
- ci: remove release eval dispatcher: #100200
- Copy pnpm store to tmpfs for test fixtures: #99960

### Credits 

Huge thanks to @bgw, @karan5028ji, @icyJoseph, @sokra, @lukesandberg, and @aurorascharff for helping!
