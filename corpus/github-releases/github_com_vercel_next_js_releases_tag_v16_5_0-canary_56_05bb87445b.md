---
title: "vercel/next.js v16.5.0-canary.56 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.56"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-19T20:55:40Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.56"
---

# vercel/next.js v16.5.0-canary.56 released

> Source: github-releases | Category: changelog | 2026-11-19T20:55:40Z

## vercel/next.js — v16.5.0-canary.56

### Core Changes

- Support bot and method-based prerender bypass capabilities: #101911
- Compute Turbopack route bundle stats in Rust: #101540
- Avoid full-segment writes without Cache Components: #101832
- Add an experimental Go front server for next start: #101695

### Misc Changes

- Wait for hydration in external-browser-runtime hydration tests: #102060
- test: skip instant-testing-api-exposure build-rejection test in deploy mode: #102056
- turbo-tasks-backend benches: skip keyed_deps setup for benchmarks excluded by the filter: #101933
- turbopack: replace EcmascriptInputTransforms::extend with new/concat turbo tasks: #102010
- turbopack-trace-server: support xz compressed trace files: #101956
- turbo-tasks-malloc: bump mimalloc to v3.7.0: #102029
- turbo-tasks-backend: deterministic re-execution oracle in recompute_dependency test: #102048
- test: print running test output when CI cancels run-tests: #101724

### Credits 

Huge thanks to @unstubbable, @sokra, @zhengdaodeguL, @jamiboym, @mischnic, and @lukesandberg for helping!
