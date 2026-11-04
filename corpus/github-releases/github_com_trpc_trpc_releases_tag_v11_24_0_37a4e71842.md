---
title: "trpc/trpc v11.24.0 released"
url: "https://github.com/trpc/trpc/releases/tag/v11.24.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "trpc"]
date: "2026-11-04T02:25:34Z"
metadata:
  repo: "trpc/trpc"
  version: "v11.24.0"
---

# trpc/trpc v11.24.0 released

> Source: github-releases | Category: changelog | 2026-11-04T02:25:34Z

## trpc/trpc — v11.24.0

## What's Changed
* fix(tanstack-react-query): reset useSubscription to idle when the server stops by @okxint in https://github.com/trpc/trpc/pull/7620
* fix(client): transformer error typo, and check docs links in package sources by @KATT in https://github.com/trpc/trpc/pull/7809
* fix(react-query): pass the cursor to procedures in createServerSideHelpers infinite helpers by @NgoQuocViet2001 in https://github.com/trpc/trpc/pull/7721
* fix(monorepo): keep pnpm-lock.yaml out of release commits and typecheck before pushing by @KATT in https://github.com/trpc/trpc/pull/7834
* fix(react-query): allow useQueries callbacks that return a union of tuple lengths by @TheForgivenOne in https://github.com/trpc/trpc/pull/7616
* perf(server): try the sync parser first for zod-like schemas by @dlecan in https://github.com/trpc/trpc/pull/7627
* fix(client): back off when the server rejects a websocket connection by @aliamanatali in https://github.com/trpc/trpc/pull/7833
* feat(next): include hierarchical subpaths in App Router cache tags by @rajveer3x in https://github.com/trpc/trpc/pull/7746
* feat: opt-in `pathSeparator` for procedure paths in HTTP URLs by @KATT in https://github.com/trpc/trpc/pull/7845
* fix(tanstack-react-query): omit `input` from handles when it is undefined by @KATT in https://github.com/trpc/trpc/pull/7848
* fix(client): reject batch validation errors without stalling requests by @maximilliangrand in https://github.com/trpc/trpc/pull/7723
* fix(server): notify every behaviorSubject observer when one unsubscribes inside next by @MindOfqc in https://github.com/trpc/trpc/pull/7742
* fix(client): surface SSE decoding errors and close subscriptions by @maximilliangrand in https://github.com/trpc/trpc/pull/7724
* fix(server): reject line breaks and null characters in tracked() ids by @Nexory in https://github.com/trpc/trpc/pull/7732
* fix(server): map errors to their http status when the error data is not an object by @MindOfqc in https://github.com/trpc/trpc/pull/7740
* fix(client): release completed HTTP request abort listeners by @brennanbutler01 in https://github.com/trpc/trpc/pull/7606
* fix(client): preserve late JSONL reads and reject missing nested chunks by @maximilliangrand in https://github.com/trpc/trpc/pull/7728
* fix(server): don't leak unhandled rejections from unread jsonl promise chunks by @KATT in https://github.com/trpc/trpc/pull/7854
* fix(server): respect maxBodySize in the Fastify adapter by @KATT in https://github.com/trpc/trpc/pull/7856
* fix(server): enforce maxBatchSize for WebSocket batches by @KATT in https://github.com/trpc/trpc/pull/7858

## New Contributors
* @hasanmahira made their first contribution in https://github.com/trpc/trpc/pull/7619
* @NgoQuocViet2001 made their first contribution in https://github.com/trpc/trpc/pull/7721
* @TheForgivenOne made their first contribution in https://github.com/trpc/trpc/pull/7616
* @dlecan made their first contribution in https://github.com/trpc/trpc/pull/7627
* @aliamanatali made their first contribution in https://github.com/trpc/trpc/pull/7833
* @Gourav224 made their first contribution in https://github.com/trpc/trpc/pull/7719
* @rajveer3x made their first contribution in https://github.com/trpc/trpc/pull/7746
* @Nexory made their first contribution in https://github.com/trpc/trpc/pull/7732
* @brennanbutler01 made their first contribution in https://github.com/trpc/trpc/pull/7606

**Full Changelog**: https://github.com/trpc/trpc/compare/v11.23.0...v11.24.0
