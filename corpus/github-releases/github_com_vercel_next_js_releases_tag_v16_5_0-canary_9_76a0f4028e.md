---
title: "vercel/next.js v16.5.0-canary.9 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.9"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-13T03:14:06Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.9"
---

# vercel/next.js v16.5.0-canary.9 released

> Source: github-releases | Category: changelog | 2026-10-13T03:14:06Z

## vercel/next.js — v16.5.0-canary.9

### Core Changes

- Gate upgrade reminder rules with agentUpgrade: #99990
- Enable network access for Codex upgrades: #100074
- Make it possible to disable `turbopackGc`: #100067
- fix: use EntryKeySide in EntryKey side field: #100053
- fix: use removePathPrefix instead of regex: #100063
- Fix root params detection on Windows: #100065
- Durable use cache: exclude context for path and code hashes: #99898
- Ensure `workStore.page` is unnormalized for generateStaticParams: #99881
- fix(codemod): find bundled docs via workspace packages in agents-md: #100017
- fix(codemod): make agents-md docs root relative to the output file: #100016
- docs: link ensureStatic TypeScript hints to its API reference: #100033
- fix: scope managed agent-feedback wording so it limits feedback, not verification: #100020
- Keep dev code frames sized to the terminal after a resize: #99916

### Example Changes

- Add cache-handler-redis-turbo example (Next.js 16 Cache Components + Redis): #96622

### Misc Changes

- Narrow upgrade eval triggers: #100075
- docs: update links for transferred demo repositories: #100041
- Expand durable use cache cross-deployment test coverage: #99900
- [cd] Support non-LTS releases: #99948
- docs: clarify Cache Components runtime config: #99820
- fix(next/image): annotate Image export so deprecated props show as deprecated: #98597
- turbo-tasks: lock-free priority queue for lowest-priority tasks, skip heap lock when empty: #99773

### Credits 

Huge thanks to @devjiwonchoi, @aurorascharff, @lukesandberg, @mischnic, @sokra, @eps1lon, @JannikZed, @awss1i, and @franpeza for helping!
