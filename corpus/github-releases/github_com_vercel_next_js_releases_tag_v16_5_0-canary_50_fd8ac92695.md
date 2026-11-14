---
title: "vercel/next.js v16.5.0-canary.50 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.50"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-14T14:46:39Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.50"
---

# vercel/next.js v16.5.0-canary.50 released

> Source: github-releases | Category: changelog | 2026-11-14T14:46:39Z

## vercel/next.js — v16.5.0-canary.50

### Core Changes

- Enable turbopackMinifyBeforeChunking by default on canary releases: #101113
- Turbopack: write smaller/faster client reference manifests: #101312
- Generate managed agent instructions on next dev and respect opt-outs: #101746
- fix(next/image): check the LCP element loading state: #101737
- Run render error reporting outside the work-unit scope: #101597
- Fix RSC navigation and runtime prefetches in `next start`: #101357
- Expose full-route RSC prerender classification to adapters: #101309
- Distinguish dynamic rendering from required prerendering: #101511
- turbopack: size chunk items by their minified code when minifying before chunking: #101010
- Prevent repeated prerenders during fallback shell revalidation: #101756
- Enable Turbopack GC by default: #101591
- Exit next dev when the server process is killed by a signal: #101752
- Store "use cache" durability once per entry in server reference manifest: #101674
- Remove `durability` property from `createServerModuleMap` results: #101730
- Resolve webpack dev HMR test callback when a build has nothing to apply: #101682
- turbo-tasks: capture effects on multiple workers: #101514
- Turbopack: report routes nested inside catch-all segments instead of panicking in dev: #101697

### Example Changes

- docs: standalone env file precedence and with-docker-multi-env secrets: #101728
- examples: bump Alpine Docker base images to Node 24: #101215

### Misc Changes

- docs: place shell param-order rule with build-time shells: #101680
- turbo-persistence: don't modify the directory on read-only open: #101779
- Optimize inline_atom: #101778
- docs: clarify standalone .env copying and the next-server tracing exclude key: #101699
- docs: Add more clarification about SVG security policies: #101311
- Add a 48-hour Cargo dependency cooldown: #101765
- Update Rust nightly to 2026-11-13: #101764
- Upgrade React from `df6aa4ec-20261112` to `df6aa4ec-20261112`: #101760
- turbo-tasks-backend: store task edges in flat EdgeSets: #101489
- turbo-tasks-backend: add a profile driver to the keyed dependencies benchmark: #101731
- docs: correct deploymentId environment variable precedence: #101740
- Turbopack: list compact re-export namespace keys in code unit order: #101494
- turbo-tasks-backend: fix transient root test race: #101700
- Scaffold separate entrypoint for Turbopack NFT functionality: #94356
- Turbopack: read UnusedReferences by key in ESM export code generation: #101626
- Require real deployment coverage for application behavior: #101510
- Turbopack: read UnusedReferences by key in pattern mapping: #101725
- test: replace files atomically in patchFile: #101683
- turbo-persistence: faster key block sorting: #100335
- turbopack: return small free ranges to the OS after project shutdown: #101623
- Turbopack: return freed memory eagerly while shutting down the project: #101589
- turbo-persistence: validate sst_inspect block reads with BlockOffsets: #100313

### Credits 

Huge thanks to @lukesandberg, @icyJoseph, @aurorascharff, @bgw, @wbinnssmith, @unstubbable, @sokra, and @mischnic for helping!
