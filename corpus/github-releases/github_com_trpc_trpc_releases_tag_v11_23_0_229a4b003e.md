---
title: "trpc/trpc v11.23.0 released"
url: "https://github.com/trpc/trpc/releases/tag/v11.23.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "trpc"]
date: "2026-11-02T20:03:44Z"
metadata:
  repo: "trpc/trpc"
  version: "v11.23.0"
---

# trpc/trpc v11.23.0 released

> Source: github-releases | Category: changelog | 2026-11-02T20:03:44Z

## trpc/trpc — v11.23.0

## What's Changed
* fix(react-query): always inject cursor field in infinite queries by @Zelys-DFKH in https://github.com/trpc/trpc/pull/7361
* fix(react-query): usable proxy type for createTRPCReact<AnyTRPCRouter> by @momomuchu in https://github.com/trpc/trpc/pull/7428
* feat(react-query,tanstack-react-query): support @tanstack/react-query 5.105 types by @KATT in https://github.com/trpc/trpc/pull/7760
* fix(server): set the allow header on 405 responses by @10kartik in https://github.com/trpc/trpc/pull/7769
* fix(client): let a caller's Content-Type header replace the default by @10kartik in https://github.com/trpc/trpc/pull/7780
* fix(server): accept a standalone basePath without a trailing slash by @10kartik in https://github.com/trpc/trpc/pull/7781
* feat(client): rename `unstable_localLink` to `localLink` by @KATT in https://github.com/trpc/trpc/pull/7777
* feat(tanstack-react-query): query handles with `$` helpers (`unstable_$prefetch`, `unstable_$ensure`, `unstable_$fetch`, `unstable_$fromHandle`) by @KATT in https://github.com/trpc/trpc/pull/7759
* fix(client): keep the connection state idle after wsClient.close() by @MindOfqc in https://github.com/trpc/trpc/pull/7733
* fix(tanstack-react-query): query handles carry no data by @KATT in https://github.com/trpc/trpc/pull/7822

## New Contributors
* @Zelys-DFKH made their first contribution in https://github.com/trpc/trpc/pull/7361
* @momomuchu made their first contribution in https://github.com/trpc/trpc/pull/7428
* @Emmanuelzyronis made their first contribution in https://github.com/trpc/trpc/pull/7609
* @10kartik made their first contribution in https://github.com/trpc/trpc/pull/7769

**Full Changelog**: https://github.com/trpc/trpc/compare/v11.22.1...v11.23.0
