---
title: "vercel/next.js v16.5.0-canary.20 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.20"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-21T11:43:44Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.20"
---

# vercel/next.js v16.5.0-canary.20 released

> Source: github-releases | Category: changelog | 2026-10-21T11:43:44Z

## vercel/next.js — v16.5.0-canary.20

### Core Changes

- Upgrade React from `ba39b32a-20261019` to `a6792708-20261019`: #100459
- Pass request headers explicitly into App request stores: #100333
- Remove request from App page prerender entry point: #100331
- Use render lifecycle callback for fetch metrics cleanup: #100323
- Upgrade React from `99c106c4-20261014` to `ba39b32a-20261019`: #100403
- Pass interception capability into App rendering: #100409

### Misc Changes

- [cd] Gate release bot credentials behind GitHub environments: #100121
- test: retry vercel deploy on transient pre-deployment network errors: #100070
- turbo-tasks: batch schedule invalidated tasks and cell dependents: #100446
- turbopack: use reverse postorder priority in compute_merged_modules: #100430
- turbopack: use reverse postorder priority in collect_graph: #100429
- turbopack: use reverse postorder priority in compute_chunk_group_info: #100428
- Turbopack: propagate late partial namespace provenance to passthrough targets: #100444
- turbopack: store unused reference edges in a keyed Vc: #100441
- AGENTS.md: prefer e2e/execution tests over implementation-mapped unit tests: #100451
- docs: document useRouter push/replace void return and useTransition migration: #100420
- docs: type proxy examples with NextRequest and fix cookie check: #100417
- Turbopack: keep env and preview props invalidations key-granular on warm start: #100425
- test: unflake prefetch-fallback-static in deploy: #99366
- Fix Activity testing guide claim about label and placeholder locators: #100445
- [ci] Upload adapter test results via GitHub Actions OIDC: #100400
- turbo-persistence: read compaction inputs with pread instead of mmap: #100336
- test: explain why deploy build-log markers are missing: #100069
- test: bound deploy build-log polling with backoff and per-call timeouts: #100068
- turbo-tasks-backend: remove racy ungated collectibles_outdated_dependency test: #100377

### Credits 

Huge thanks to @eps1lon, @sokra, @Aryan9891, @deveshasawa28, @lukesandberg, @lubieowoce, @icyJoseph, and @kassens for helping!
