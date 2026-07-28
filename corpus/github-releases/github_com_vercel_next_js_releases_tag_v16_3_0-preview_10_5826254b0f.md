---
title: "vercel/next.js v16.3.0-preview.10 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.0-preview.10"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-07-28T17:02:42Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.0-preview.10"
---

# vercel/next.js v16.3.0-preview.10 released

> Source: github-releases | Category: changelog | 2026-07-28T17:02:42Z

## vercel/next.js — v16.3.0-preview.10

### Misc Changes

- Unify allow-runtime with Partial Prefetching: #96106
- Attempt static prefetch before resorting to runtime: #96095
- Block prefetch task until sufficient response is received: #96017
- Use a safe clock for Request Insights bookkeeping: #96274
- Count key length in remaining byte-budgeted LRUs: #96231
- Serve cached misses from the filesystem route cache: #96230
- Count URL key length in the filesystem route cache LRU: #96229
- Turbopack: Only extend the watcher's batch window for unfiltered events: #96186
- Turbopack: Store watcher batch state with bitflags instead of 4 different sets: #96114
- docs: document query-only href resolution and fix with-vercel-blob : #96280
- Micro-optimization for string format: #95774
- Upgrade React from `28cd4bb0-20260723` to `756fdd47-20260727`: #96270
- [test] Unflake more tests: #96081
- [test] Run the navigation e2e suite under cacheComponents: #95877
- [test] Run more test suites under cacheComponents flag, again: #96196
- [test] Unflake a prefetch-related race: #96222
- docs(ai-agents): restructure as steps and close 16.2/16.3 coverage gaps: #96247
- Replace vendored `http-proxy` with `httpxy`: #96060
- Update vendored `@mswjs/interceptors` to 0.41.9: #96059
- Track whether runtime data is accessed during prefetch: #95964
- Add Instant Insights request timing: #95958
- [turbopack] Tree-shake `module.exports = {...}` (CJS): #95996
- [turbopack] Fix de-opt in getChunkRelativeUrl(): #96183
- Add shell offset to static segment prefetches: #95963
- Turbopack: support import.meta.glob caseSensitive option: #96226
- fix(sandbox): release one-shot timeout ids after they run: #96161
- Fix dev overlay symbolication for project paths needing percent-encoding: #96221
- [internal] Add a skill for benching changes in a sandbox: #95943
- Run dev validation in process when using Webpack: #96219
- Read chunk source maps from disk in the dev validation worker: #96218
- Retry the source map lookup with a plain path: #96215
- Pass fallback params to the dev validation worker as maps: #96210
- [sourcemaps] Reuse source map payloads and consumers across stack frames: #96198
- fix: release compression stream when client disconnects mid-response: #96173
- Run Cache Components dev validation on a worker thread: #96153
- Add a benchmark for dev Cache Components validation on a worker thread: #96152
- [test] Unflake the `enabled-features-trace` test suite: #96175
- [refactor] Prepare dev validation for running on a worker thread: #96151
- Add the `experimental.devValidationWorker` config flag: #96150
- [refactor] Model dev validation render outputs as a discriminated union: #96149
- Forward dev invalid dynamic usage errors from the render, not validation: #96148
- Optimize implicit cache tag derivation: #96120
- Avoid quadratic HMR queue shifts: #96137
- [sourcemaps] Use file: sourcemaps for Turbopack to improve dev performance: #95946
- Give RouteCacheEntry a single hidden class across its lifecycle: #96164
- Keep optimistic-route param handling monomorphic: #96169
- Store RouteTree slots in a Map to keep slot access monomorphic: #96168
- Make reifyRouteTree object literals match the canonical RouteTree key order: #96162
- Keep VaryPath monomorphic by making isRootParam required: #96122
- docs: expand and modernize the Single-Page Applications guide: #95860
- docs: navigation interrupts after streaming has started (notFound, forbidden, unauthorized): #95851
- docs: reframe prefetching around automatic vs. controllable behavior: #95896
- docs(view-transitions): fix the skill install command: #96142
- Include additional prerender metadata about build-time routes: #96080
- Optimize app page entry analysis: #96058
- [ts-plugin] Preserve TypeScript quick info metadata: #95863
- [turbopack] Import Webpack's tests for tree-shaking: #95811
- [turbopack] Drop dead `require()` calls: #95718
- [turbopack] Track usage of modules imported with `require()`: #95717
- Return plain text 404 for non-document req
