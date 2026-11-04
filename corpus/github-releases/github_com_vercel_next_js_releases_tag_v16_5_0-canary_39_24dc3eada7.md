---
title: "vercel/next.js v16.5.0-canary.39 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.39"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-04T02:25:24Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.39"
---

# vercel/next.js v16.5.0-canary.39 released

> Source: github-releases | Category: changelog | 2026-11-04T02:25:24Z

## vercel/next.js — v16.5.0-canary.39

### Core Changes

- Strip internal middleware cookie headers from edge responses: #101109
- Fix stale compressed framing for forwarded fetch responses: #101108
- [use cache] Fix cache key when binary args are used: #101107
- Fix shared shell poisoning from request-supplied placeholder params: #101106
- [next/image] Fix false-positive AVIF/HEIC detection: #101105
- Fix `unstable_cache` leaking cold `'use cache'` fills across root params: #101104
- Fix outer 'use cache' entries reused across root param values: #101103

### Misc Changes

- Turbopack: keep CSS Modules when a loader rule's `as` adds an existing extension: #101065
- Add segment config parity regression tests: #100881
- Turbopack: cleanup ReferencedAssetIdent: #101095
- [test] Fix flaky resume data cache tests: #101088
- docs: fix import.meta.glob base docs: #101085
- create-next-app: remove unused webpack bundler option: #101081
- [experiment] [turbopack-cli] compile .go files: #99980

### Credits 

Huge thanks to @eps1lon, @lukesandberg, @mischnic, @unstubbable, @icyJoseph, and @timneutkens for helping!
