---
title: "vercel/next.js v16.5.0-canary.59 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.59"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-21T04:08:51Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.59"
---

# vercel/next.js v16.5.0-canary.59 released

> Source: github-releases | Category: changelog | 2026-11-21T04:08:51Z

## vercel/next.js — v16.5.0-canary.59

### Core Changes

- switchyard: restore 'in front of' in three test comments: #102082
- Write Turbopack dist dir metadata from Rust: #101638

### Example Changes

- examples: remove examples built on abandoned libraries: #102092
- examples: Update storage integrations and remove Grafbase and Xata examples: #100454

### Misc Changes

- Turbopack: take next/dynamic loader availability from chunking for the loadable manifest: #101172
- Turbopack: keep ?server-data on Pages data endpoint _app/_document modules: #102099
- Turbopack: report unreadable filesystem cache files clearly: #101980
- docs: remove generic agent workflow guidance: #102071
- test: wait for destination render in dynamic-param casing navigation test: #102145
- turbo-tasks: re-check job counters while stopping: #102142
- Turbopack: shrink slow tests under Miri: #102135
- Fix NODE_ENV evaluation through default process imports: #102130

### Credits 

Huge thanks to @jamiboym, @lukesandberg, @kassens, @sokra, @icyJoseph, and @mischnic for helping!
