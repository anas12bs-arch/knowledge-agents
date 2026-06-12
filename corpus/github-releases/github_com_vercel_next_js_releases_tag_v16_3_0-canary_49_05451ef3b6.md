---
title: "vercel/next.js v16.3.0-canary.49 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.0-canary.49"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-06-12T11:32:05Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.0-canary.49"
---

# vercel/next.js v16.3.0-canary.49 released

> Source: github-releases | Category: changelog | 2026-06-12T11:32:05Z

## vercel/next.js — v16.3.0-canary.49

### Misc Changes

- [turbopack] Rename variables in `path_join` and add tests: #94625
- Warn on prefetch={true} navigation without Partial Prefetching (dev): #94672
- Serve stale `'use cache'` entries in the dev server until they expire: #94662
- Re-fetch dynamic content on navigation with `partialPrefetching` enabled: #94655
- docs: expand the Cache Components migration guide: #94649
- Add Owner Stack to "`prefetch={true}` navigation without Partial Prefetching" warning: #94683
- [tubopack] migrate rcstr! to use scattered collect: #94498
- Strip internal dev request-id headers from userland `headers()`: #94703
- Persist `'use cache: private'` entries in dev: #94694
- [App Shells] refactor instant-validation to make adding new stages easier: #94711
- migrate turbo-tasks to scattered collect: #94503
- [CC] refactor staged rendering codepaths in params/searchParams: #94718
- [App Shells] Track whether shell prefetch used session data: #94484
- Treat empty resume bodies as dynamic render requests: #94729

### Credits 

Huge thanks to @sampoder, @acdlite, @unstubbable, @icyJoseph, @eps1lon, @lukesandberg, @lubieowoce, and @gnoff for helping!

