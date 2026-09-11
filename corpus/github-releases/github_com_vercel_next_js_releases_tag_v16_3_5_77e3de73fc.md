---
title: "vercel/next.js v16.3.5 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.5"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-09-11T19:52:35Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.5"
---

# vercel/next.js v16.3.5 released

> Source: github-releases | Category: changelog | 2026-09-11T19:52:35Z

## vercel/next.js — v16.3.5

The following bug fixes have been backported. It does not include all pending features/changes on canary.

- next/image: Skip 0-byte entries when initializing disk LRU cache (#98185)
- next/image: Reject empty images when reading/writing to the disk cache (#98186)
- Emit whole-app server NFTs when `output: 'standalone'` is used with an adapter (#98167)
- Add CSP nonce to script tags of loading and template files (#98403)
- Fix `use cache` prerender signal retention (#98448)
