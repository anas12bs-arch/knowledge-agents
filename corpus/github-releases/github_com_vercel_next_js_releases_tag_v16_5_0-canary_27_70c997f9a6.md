---
title: "vercel/next.js v16.5.0-canary.27 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.27"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-25T12:02:00Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.27"
---

# vercel/next.js v16.5.0-canary.27 released

> Source: github-releases | Category: changelog | 2026-10-25T12:02:00Z

## vercel/next.js — v16.5.0-canary.27

### Core Changes

- Build the inline Flight script from React's strings instead of re-encoding them: #100142
- Fix dist dir lockfile on filesystems with no or limited lockfile implementations (e.g. NFS): #100684

### Misc Changes

- perf(turbopack): look up chunk group indices through a keyed cell: #99050
- Turbopack: track availability by chunk group: #98685
- refactor(turbopack): chunk chunk groups by key: #99750
- Turbopack: consume graph-derived chunk groups: #98734
- turbo-tasks-backend: stripe SnapshotCoordinator's operation count and poll for the drain: #100280
- turbo-tasks-backend: parallelize decoding of large batch lookups: #100453
- turbo-persistence: don't shrink the shard count before the first bottom merge: #100424

### Credits 

Huge thanks to @sokra, @lukesandberg, @gaearon, and @bgw for helping!
