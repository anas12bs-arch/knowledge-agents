---
title: "vercel/next.js v16.3.0-preview.6 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.0-preview.6"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-07-13T20:23:01Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.0-preview.6"
---

# vercel/next.js v16.3.0-preview.6 released

> Source: github-releases | Category: changelog | 2026-07-13T20:23:01Z

## vercel/next.js — v16.3.0-preview.6

### Core Changes

- Enhance ESLint rule `no-location-assign-relative-destination`: #93057

### Misc Changes

- Turbopack: order CSS modules by chunk-group co-occurrence in linearize: #95579
- [test] Disable i18n-api-support deploy test for Turbopack with adapters: #95739
- Fork navigation-testing-lock module: #95611
- docs: runtime prefetching update: #95564
- request insights: add agent diagnosis access (4/5): #93977
- Fix Pages router 404 runtime rendering with Adapter: #95264
- Fix duplicate static files in adapter: #95681
- Update font data: #95725
- [test] Disable middleware-rewrites deploy test for Turbopack with adapters: #95680
- request insights: expose dev snapshots to tools and HMR (3/5): #93976
- request insights: derive request history and fetch data (2/5): #93975
- request insights: record local framework spans (1/5): #93974
- Turbopack tests: remove assertions that duplicate webpack results: #95688
- Fix support for `custom-media-queries` in LightningCSS: #95689
- Clarify AI-assisted contribution policy in PR template and AGENTS.md: #95629
- docs: add Building guide: #94999
- docs: add incremental adoption path to Cache Components migration guide: #95325
- [PPF] Sync IO is only allowed in the dynamic stage: #95384
- refactor: remove unnecessary switches from StagedRenderingController: #95383
- Keep the request body a plain Readable after middleware so Readable.toWeb() doesn't hang: #95607
- docs: note default error/not-found UI follows OS color scheme, not app theme: #95673
- test: skip redbox check in "static prefetch - missing suspense around search params": #95670
- test: allow-runtime breaks Link's Server component child detection: #95596
- docs: Immutable static assets: #95348
- [turbopack] Simplify service worker e2e tests: #95672
- [docs] Update "Handling a Custom `Service Worker`" in the CRA migration docs: #95434
- [docs] Update progressive web apps documentation for new service worker syntax: #95431
- (TypeScript 7 Support) Add experimental TypeScript CLI backend: #95639
- [turbopack] Compile service workers registered from pages router pages: #95583
- [turbopack] Output service workers to `/_next/static/`: #95554
- Reduce the size of OperationVc from 8 bytes to 4: #95614
- Upgrade React from `df4bd1b4-20260708` to `5123b063-20260708`: #95642
- Add attribute rendering benchmark: #95621
- docs(opengraph-image): load assets at module scope to keep route static under Cache Components: #95246
- Convert agent-041's blocking-data check to the agentic LLM judge: #95630
- Upgrade React from `12a4baec-20260707` to `df4bd1b4-20260708`: #95612
- Make the agent-rules block verifiable and self-upgrading: #95467
- Refresh outdated agent-rules blocks on next dev and codemod upgrade: #95470
- [ci] Split up large instant-validation tests: #95627
- [ci] Split up large rsc-build-errors development test: #95624
- [ci] split up large cache-components-errors tests: #95623
- docs: update MCP guides for the thin next-devtools-mcp: #94859
- Normalize and validate `expire` and `revalidate` values to handle Infinity and surface mistakes early: #95493
- [ci] Bump PR stats job timeout to 35 minutes: #95592
- [ci] Pin typescript version in tests: #95619
- fix(create-next-app): render filenames in Geist Mono so the preloaded font is used: #95471
- [turbopack] print Turbopack warnings after SSG: #95430
- fix(create-next-app): pin both axes on Tailwind template logos to silence aspect-ratio warning: #95609
- Turbopack: enable `import with {type: 'text'}` by default: #95606
- Consistently gate navigation-testing-lock API on flag: #95582
- test: Fix immutable static asset deployment tests for real: #95600
- Upgrade React from `23def8fd-20260706` to `12a4baec-20260707`: #95581
- Split remaining "client-node"-only modules into .browser variants: #95366
- [turbopack] Don't evict when there is little memory to save: #95213
- align dev and build output: #94916
- [turbopack] Don't persist if there is little work to do: #95137
- fix: log "Part
