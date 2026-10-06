---
title: "vercel/next.js v16.4.0-canary.61 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.4.0-canary.61"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-06T01:34:28Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.4.0-canary.61"
---

# vercel/next.js v16.4.0-canary.61 released

> Source: github-releases | Category: changelog | 2026-10-06T01:34:28Z

## vercel/next.js — v16.4.0-canary.61

### Misc Changes

- Turbopack: Cache canonicalized paths without turbo-tasks, try to find the longest cached prefix first: #99270
- Record parameter matching usage in build metadata: #99594
- Bundle Analyzer Agent Skill: Stream versioned analyzer graph as JSON Lines: #99387
-  Revert "Optimize esm exports by shifting the protocol burden to getters (#98932)": #99704
- [PPF] Log Sync IO errors in runtime prerenders: #99688
- docs: clarify use client directive as a file level directive: #99703
- Stabilize `forbidden()` and `unauthorized()`: #99689
- turbopack-ecmascript-runtime: type-check every runtime file: #99670
- test: unflake use-cache-search-params: #99691
- Avoid mutating config for default export paths: #99496
- Keep compile-mode metadata outside configuration: #99491
- Keep dynamic asset prefixes outside configuration: #99490
- eslint-config-next: support ESLint 10: #99628
- Add Instant Insights for prefetch() and navigation(): #97801
- rename `RenderStage.Runtime` to `PrefetchRuntime`: #99679
- Collect root param dependencies for `'use cache'` at build time: #99274
- Add client fixes for fully static route errors: #99659
- docs: clarify hover prefetching with Partial Prefetching: #99665
- Durable use cache entries: sort env var list: #99657
- next-swc: rebuild native when embedded js/src files change: #99669

### Credits 

Huge thanks to @bgw, @gnoff, @wbinnssmith, @lubieowoce, @kassens, @acdlite, @lukesandberg, @jamiboym, @aurorascharff, @unstubbable, and @mischnic for helping!
