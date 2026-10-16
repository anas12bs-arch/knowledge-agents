---
title: "vercel/next.js v16.5.0-canary.15 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.15"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-16T01:46:07Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.15"
---

# vercel/next.js v16.5.0-canary.15 released

> Source: github-releases | Category: changelog | 2026-10-16T01:46:07Z

## vercel/next.js — v16.5.0-canary.15

### Core Changes

- Hoist app page request URL into render context: #99269
- Hide overlay editor button labels on smaller screens: #100266
- Prefer non-partial entries regardless of FetchStrategy: #99705
- [Partial Prefetching] Don't report vary params in responses that include dynamic data: #99700
- [Partial Prefetching] Small optimizations and fixes: #99695
- [Cached Navs] Extract the shell from a fully cached response: #99619
- Refactor the navigation fetch and decode layering: #99618
- [Cached Navs] Don't extract static stage: #99617
- Make error overlay editor actions easier to discover: #100206

### Misc Changes

- Turbopack: don't inherit API route config from parent layouts: #100243
- test: Add more segment config tests: #100242
- Add more test coverage for non-Partial Prefetching behavior: #100133
- chore: Remove package.json#workspaces: #100234
- docs: Add Pages Router upgrade guides for versions 15 and 16: #100247
- docs: note that 'use cache: private' results persist across requests in dev: #100252
- test: unskip tests for Turbopack: #100185

### Credits 

Huge thanks to @gnoff, @samselikoff, @mischnic, @acdlite, and @icyJoseph for helping!
