---
title: "vercel/next.js v16.5.0-canary.11 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.11"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-15T05:11:53Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.11"
---

# vercel/next.js v16.5.0-canary.11 released

> Source: github-releases | Category: changelog | 2026-10-15T05:11:53Z

## vercel/next.js — v16.5.0-canary.11

### Core Changes

- Upgrade React from `b618bbb4-20261007` to `07dde64d-20261013`: #100194
- Remove staticInfo.rsc: #100172
- fix(analyze): use route summaries as the analyzer route index: #100081
- Reload on missed Turbopack startup CSS updates: #99963
- Remove unused getParams matcher cache: #100078
- fix: mark HTTP fetch failures as span errors: #99877
- docs: explain router.prefetch stages: #99786

### Misc Changes

- docs: fix "a HTTP"/"a SSR" grammar and Node.js casing: #99542
- docs: narrow catchError ErrorInfo.error, typed as unknown: #100196
- docs: update links for newly transferred demos: #100197
- ci: update release eval workflow pin: #100189
- ci: run evals for releases and canaries: #100126
- test: speed up use-cache-cross-deployment even more: #100181
- Turbopack: only search <head> for existing chunk tags: #100175
- docs: clarify Server Action dispatch across Mutating Data and the guide: #100144
- test: speed up use-cache-cross-deployment: #100138
- Turbopack: avoid document-wide selector scans when probing for chunk tags: #100047
- Don't optimize the aggregation graph during `connect_child`: #100147
- Simplify aggregation update queue control flow: #100146
- [ci] Fix Rspack test manifest update workflow: #100052
- docs: fix example path regexr: #100084

### Credits 

Huge thanks to @deveshasawa28, @icyJoseph, @aurorascharff, @mischnic, @wbinnssmith, @sokra, @kakadiadarpan, @lukesandberg, and @sabrinaluo for helping!
