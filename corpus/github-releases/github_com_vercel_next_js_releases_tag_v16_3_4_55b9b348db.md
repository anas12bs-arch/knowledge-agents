---
title: "vercel/next.js v16.3.4 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.4"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-08-31T22:49:01Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.4"
---

# vercel/next.js v16.3.4 released

> Source: github-releases | Category: changelog | 2026-08-31T22:49:01Z

## vercel/next.js — v16.3.4

Follow-up release to [v16.3.3](https://github.com/vercel/next.js/releases/tag/v16.3.3) re-enabling AVIF Image Optimization ([#97949](https://github.com/vercel/next.js/pull/97949)).

The following bug fixes have been backported. It does **not** include all pending features/changes on canary.

- testmode: Fix infinite recursion in testmode passthrough fetch (#97691)
- Fix build error when aliasing typescript to @typescript/typescript6 (#97997)
- Fix unset crossOrigin in Turbopack manifests (#97930)

### Credits

Huge thanks to @eps1lon, @mischnic, and @timneutkens for helping!
