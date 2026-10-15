---
title: "vercel/next.js v16.5.0-canary.13 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.13"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-15T21:37:47Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.13"
---

# vercel/next.js v16.5.0-canary.13 released

> Source: github-releases | Category: changelog | 2026-10-15T21:37:47Z

## vercel/next.js — v16.5.0-canary.13

### Core Changes

- Fix extensionless Google font URLs in both bundlers: #100158
- Emit the Turbopack shared-runtime bootstrap in the PPR resume so it gets the CSP nonce: #100102
- Keep requests through middleware in a single OpenTelemetry trace: #100136
- Write webpack dev manifests atomically: #100112

### Misc Changes

- next-api: isolate dropped entrypoint collectibles in an inner operation: #100187
- turbo-tasks-backend: optimize aggregated updates outside of the lock: #100165
- docs: Add turborepo agents rules: #100214

### Credits 

Huge thanks to @sokra, @andrewimm, and @bgw for helping!
