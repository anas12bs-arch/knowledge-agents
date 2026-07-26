---
title: "vercel/next.js v16.3.0-canary.97 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.0-canary.97"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-07-26T00:10:28Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.0-canary.97"
---

# vercel/next.js v16.3.0-canary.97 released

> Source: github-releases | Category: changelog | 2026-07-26T00:10:28Z

## vercel/next.js — v16.3.0-canary.97

### Misc Changes

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

### Credits 

Huge thanks to @petehunt, @gaearon, @unstubbable, and @marcoshernanz for helping!
