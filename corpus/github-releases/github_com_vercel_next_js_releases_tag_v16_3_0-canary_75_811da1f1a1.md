---
title: "vercel/next.js v16.3.0-canary.75 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.0-canary.75"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-07-02T11:12:47Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.0-canary.75"
---

# vercel/next.js v16.3.0-canary.75 released

> Source: github-releases | Category: changelog | 2026-07-02T11:12:47Z

## vercel/next.js — v16.3.0-canary.75

### Misc Changes

- [cd] Replace the release package with our own GitHub release creation: #95352
- [test] Enable deploy tests for the Instant Navigation Testing API suite: #95236
- Await reused in-flight prefetch entries under Instant Navigation lock: #95301
- [test] Park the blocking-fallback segment on a withheld param: #95300
- Make `instant()` resilient to a leaked navigation-testing cookie: #95375
- [ci] Avoid running full CI mid-stack for GH-native stacks, same as we do for Graphite: #95218
- Remove 'silence this warning' from instant validation fix output: #95187
- fix(turbopack): allow `#/` prefixed subpath import specifiers: #94461

### Credits 

Huge thanks to @eps1lon, @unstubbable, @bgw, @aurorascharff, and @sleitor for helping!
