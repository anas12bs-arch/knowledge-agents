---
title: "vercel/next.js v16.5.0-canary.37 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.37"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-03T02:05:44Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.37"
---

# vercel/next.js v16.5.0-canary.37 released

> Source: github-releases | Category: changelog | 2026-11-03T02:05:44Z

## vercel/next.js — v16.5.0-canary.37

### Core Changes

- Add router.experimental_prepare(): #101050
- Handle registries not serving JSON when checking the version: #95062
- Fix navigations rerendering fully static ISR pages in `next start`: #100854
- [refactor] Remove obsolete RDC and PPR feature guards: #100827
- [no-unsafe-inline] Carry the Flight payload as data instead of inline scripts: #97573
- [no-unsafe-inline] Add an experimental flag for React's external browser runtime: #97570
- Fix revalidation for caches with short stale times: #101037
- Consistently use headersToExcludeInCacheKey: #101035
- turbopack: experimental minify-before-chunking feature: #98760

### Misc Changes

- fix(turbopack): invalidate lazy compilation state across sessions: #98867
- docs: improve turbo_tasks consistency guidance for agents: #101055
- Revert 'Turbopack: ignore fully dynamic alternatives when tracing file paths (#100651)': #101053
- Don't count features behind a new experimental flag as public API: #101051
- docs: add turbo_tasks consistency guidance for agents: #100986
- docs: correct io() prefetch behavior vs connection(): #101031
- perf: use keyed invalidation for get_chunk_groups_for_module: #101034
- test: fail e2e tests on Rust panics: #100922
- turbo-tasks: add batched keyed reads via KeyedReadRef: #100884

### Credits 

Huge thanks to @fireairforce, @mischnic, @acdlite, @vctqs1, @unstubbable, @eps1lon, @icyJoseph, @sokra, and @andrewimm for helping!
