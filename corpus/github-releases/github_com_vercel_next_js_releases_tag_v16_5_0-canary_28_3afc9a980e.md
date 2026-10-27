---
title: "vercel/next.js v16.5.0-canary.28 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.28"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-27T01:41:32Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.28"
---

# vercel/next.js v16.5.0-canary.28 released

> Source: github-releases | Category: changelog | 2026-10-27T01:41:32Z

## vercel/next.js — v16.5.0-canary.28

### Core Changes

- Fix draft mode rendering with Cache Components: #100728
- Render complete HTML documents after MPA Server Actions: #100740
- Turbopack: add minServerChunkSize and maxMergeServerChunkSize options: #100712
- test: read isNextDev/isNextDeploy/isNextStart from e2e-utils: #100419
- perf(build): avoid O(pages²) original app path scan in static check: #100615
- [PPF] Fix hanging HTML response after a `'use cache'` error: #100673
- export: only send each static generation batch its own resume data cache seeds: #100048

### Misc Changes

- docs: note that non-function exports of a use cache file are not available to Client Components: #100594
- Mark docs diagrams skill as internal: #100743
- [test] Isolate deploy e2e revalidation scope per suite: #100718
- test: migrate more conditions to gates: #100422
- Support fs.stat in Turbopack webpack loaders: #100272
- test: document deploy exclusions for suites that need a local server: #100483
- Turbopack: ensure tests are dropping turbo tasks correctly: #99601
- turbopack: skip redundant work in merged modules reconciliation: #100238
- turbopack: merge chunk group lists in parallel in compute_merged_modules: #100237
- bench: add warm cached build benchmark to nested-deps-app-router-many-pages: #100570
- turbo-tasks: update reader leaf distance inline when adding output dependency: #99764

### Credits 

Huge thanks to @icyJoseph, @unstubbable, @aurorascharff, @eps1lon, @mischnic, @jimmyhmiller, @sokra, @jamiboym, @arnaud-coral, and @lukesandberg for helping!
