---
title: "vercel/next.js v16.5.0-canary.41 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.41"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-05T02:51:16Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.41"
---

# vercel/next.js v16.5.0-canary.41 released

> Source: github-releases | Category: changelog | 2026-11-05T02:51:16Z

## vercel/next.js — v16.5.0-canary.41

### Core Changes

- feat(next/image): add internal image redirects (to match existing external image redirects): #98271
- Turbopack: show the source-mapped file in issue headers: #101161
- Add Request Insights filters and pause controls: #96924
- Avoid instrumenting Next.js telemetry requests: #97182
- Classify framework request activity: #96914
- Move optional lockfile parameters into options object: #101132
- Record Instant Insights validation worker spans: #98677
- Share local tracing across development runtimes: #98676
- [image-optimizer] Replace handleDevOutput with an 'optimized' flag in ImageOptimizerResult, make the caller responsible for blur svg placeholder generation: #101167
- [image-optimizer] Move previous cache entry reuse out of `next/image-optimizer-transform`: #101126
- Deeply freeze the loaded config in test mode: #99943
- fix: do not run onStage listeners for stages that were aborted: #95684
- Update font data: #101129
- Remove the experimental.lockDistDir opt-out option: #100747
- Keep loaded config from sharing objects with defaults and callers: #99942

### Misc Changes

- Fix effects applying when they didn't need to because expression was replaced: #101166
- fix: server actions entrypoint erroring build with `type: commonjs`: #101164
- skills: improve cache-aware navigation workflows: #101169
- docs: document experimental flags removed in Next.js 16: #101165
- docs: useServerInsertedHTML: #98671
- Turbopack: narrow async-module emptiness dependencies: #101154
- eval: measure Next Dev Loop on Pokédex: #100962
- Turbopack: internalize evaluation pool plumbing: #101143
- Turbopack: generate require.context as a synthetic module: #100526
- turbopack-node: linear IPC frame parsing with eager UTF-8 decoding: #99968
- turbo-tasks-backend: keep recorded GC roots until their TTL expires: #100279
- Turbopack: only read conditionally needed values where they are used: #101072

### Credits 

Huge thanks to @styfle, @lukesandberg, @DavidIlie, @bgw, @jimmyhmiller, @lubieowoce, @aurorascharff, @icyJoseph, @jamiboym, and @mischnic for helping!
