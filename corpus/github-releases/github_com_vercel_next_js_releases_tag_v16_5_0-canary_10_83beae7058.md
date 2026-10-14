---
title: "vercel/next.js v16.5.0-canary.10 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.10"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-14T00:53:01Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.10"
---

# vercel/next.js v16.5.0-canary.10 released

> Source: github-releases | Category: changelog | 2026-10-14T00:53:01Z

## vercel/next.js — v16.5.0-canary.10

### Core Changes

- docs: make agent feedback command work in npm workspaces: #100135
- test: install local Next.js sibling packages in CNA tests: #100062
- Don't blame the Pages Router for next/headers imported through a Client Component: #100087
- Resolve relative imports in `next.config.ts` from the config directory: #99743

### Misc Changes

- Update evals for stabilized navigation APIs: #100145
- Turbopack: improve segment config parsing: #98641
- docs(cache-handlers): explain updateTags durations, fix Redis EX for Infinity: #96517
- Turbopack: Use the imagesize crate to correctly size AVIF images (still no optimization or encoding): #99966
- Fix Turbopack lazy dynamic-import chunk-list collisions: #99940
- Turbopack: de-flake the active Tokio worker count test: #100120
- Turbopack: preload _app's next/dynamic chunks with _app's own availability: #100091
- test: deflake app-basepath external redirect test: #100096
- turbopack-ecmascript-runtime: simplify the shared HMR module instantiation: #99671
- chore: Make Rust warnings non-fatal unless on CI: #99939
- Fix rustdoc warnings: #100036
- Durable use cache: ignore binding usage when traversing: #100128
- chore: Fix agents instruction about rebuilding test changes: #100116
- chore: Prevent concurrent pack-for-isolated-tests: #100118
- Split filesystem-cache e2e test into multiple suites: #100111
- docs: update links to demos moved to the nextjs org: #100119
- test: allow custom webpack deployments to complete: #100054
- Turbopack: fix edge route handlers when cacheHandlers is configured: #100046
- fix(next-code-frame): snap visible window to char boundaries: #92646

### Credits 

Huge thanks to @aurorascharff, @mischnic, @leejpsd, @bgw, @jimmyhmiller, @devjiwonchoi, @sokra, @lukesandberg, @icyJoseph, @mugi-uno, and @dxdc for helping!
