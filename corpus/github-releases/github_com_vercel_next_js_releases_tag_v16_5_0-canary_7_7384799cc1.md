---
title: "vercel/next.js v16.5.0-canary.7 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.7"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-10T14:28:51Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.7"
---

# vercel/next.js v16.5.0-canary.7 released

> Source: github-releases | Category: changelog | 2026-10-10T14:28:51Z

## vercel/next.js — v16.5.0-canary.7

### Core Changes

- Reland experimental custom webpack support: #99234

### Misc Changes

- Add CI for upgrade evals with shared preparation: #99908
- Rebuild upgrade evals around delivered apps: #99880
- Upgrade Corepack to 0.34.7: #99959
- Upgrade Turborepo to 2.11.7: #99958
- Normalize pnpm store cache keys: #99957
- test: cover Pages Router _app availability in Turbopack dev (#99789): #99910
- Turbopack: chain the Pages Router development client module graph: #98823
- turbopack: report an actionable error when Node.js child processes cannot connect: #99887
- Turbopack: Ignore realpath errors during module resolution, matching node's behavior: #99951
- test: add a `vercel` gate condition for Vercel-specific deploy tests: #99837
- test: remove per-test Corepack overrides now that deploy mode enables it: #99945

### Credits 

Huge thanks to @devjiwonchoi, @bgw, @sokra, @lukesandberg, and @jamiboym for helping!
