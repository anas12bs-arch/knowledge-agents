---
title: "vercel/next.js v16.5.0-canary.16 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.16"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-17T00:00:16Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.16"
---

# vercel/next.js v16.5.0-canary.16 released

> Source: github-releases | Category: changelog | 2026-10-17T00:00:16Z

## vercel/next.js — v16.5.0-canary.16

### Core Changes

- Refactor fetchStrategy -> stage and completeness: #99706
- Remove dead NextNodeServer.renderHTML: #100284
- Pass Server Action request metadata into App rendering: #100274
- Revert "Keep requests through middleware in a single OpenTelemetry trace": #100302
- Respect release age when pinning the upgrade CLI: #100256

### Misc Changes

- test: remove stale deploy gate on cold RSC navigation param caching test: #100285
- Fix upgrade eval worktree dependency links: #100257

### Credits 

Huge thanks to @lukesandberg, @acdlite, @kassens, @devjiwonchoi, and @sokra for helping!
