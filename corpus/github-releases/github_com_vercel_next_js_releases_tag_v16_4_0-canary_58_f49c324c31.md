---
title: "vercel/next.js v16.4.0-canary.58 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.4.0-canary.58"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-03T05:50:19Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.4.0-canary.58"
---

# vercel/next.js v16.4.0-canary.58 released

> Source: github-releases | Category: changelog | 2026-10-03T05:50:19Z

## vercel/next.js — v16.4.0-canary.58

### Misc Changes

- Optimize esm exports by shifting the protocol burden to getters: #98932
- fix: fix pnpm builds in Docker examples: #97352
- Assert transient task references are not serialized: #99300
- Reorganize bundle analyzer toolbar: #98920
- Show async module scope in bundle analyzer: #98918
- Show bundle changes in compare treemap: #98837
- improve disk read semantics around MustExist and AllowMissing: #99249
- Allow opt-in facade-backed export mangling: #99309
- Add bundle analyzer route summary: #98787
- [turbo-tasks-backend] Correctly maintain outdated_collectibles to prevent unnecessary stale executions: #99386
- Upgrade React from `8b0da1c6-20260922` to `278794d7-20261002`: #99600
- Warn when Partial Prefetching is not configured: #99452
- Store the Turbopack module cache in a Map: #98947
- Improve agent feedback reporting reliability: #99591
- Enable empty generateStaticParams deploy diagnostics: #99406
- test: enable Nx deployment coverage: #99407
- test: enable deployment coverage for monorepo fixtures: #99395
- test: capture deployment experimental flags in config: #99534
- test: extract a shared helper for deployment feature flags: #99533
- Move App Page header parsing to handler entrypoints: #99506
- docs: clarify ensureStatic levels from dogfooding: #99590
- Gate param-matching deploy tests on the adapter: #99582
- docs: update the MCP guide for next-devtools-mcp 0.4: #99583
- Document agent upgrades across Next.js: #99293
- [test] Fix the legacy image preload order assertion for React 18: #99572
- docs: Remove task decomposition and validation boilerplate from AGENTS.md: #99558
- Turbopack: Use a FrozenMap for DiskFileSystemMap: #99569
- [test] Expose first-run e2e test failures in CI: #99528
- Turbopack: `resolveFileUrl`/`placeholderFileUrl` is always called with a module path: #99560
- Turbopack: Remove implicit mismatched root fallthrough for AfterResolvePluginCondition, accept None as a root: #99556
- Turbopack: Allow ResolveMap entries to match against all possible roots: #99555
- Turbopack: Support import.meta.url in additional roots: #99511

### Credits 

Huge thanks to @lukesandberg, @6iu8a, @wbinnssmith, @sokra, @aurorascharff, @jamiboym, @gnoff, @devjiwonchoi, @unstubbable, and @bgw for helping!
