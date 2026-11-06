---
title: "trpc/trpc v11.25.0 released"
url: "https://github.com/trpc/trpc/releases/tag/v11.25.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "trpc"]
date: "2026-11-06T22:04:55Z"
metadata:
  repo: "trpc/trpc"
  version: "v11.25.0"
---

# trpc/trpc v11.25.0 released

> Source: github-releases | Category: changelog | 2026-11-06T22:04:55Z

## trpc/trpc — v11.25.0

## @trpc/server

### Fixes

* fix(server): settle pending next() on abort and ignore teardown emissions in observableToAsyncIterable by @KATT in https://github.com/trpc/trpc/pull/7867
* fix(server): don't crash when a subscription's teardown throws on abort by @KATT in https://github.com/trpc/trpc/pull/7884
* fix(server): report a ws subscription's cleanup error after the client stops it by @KATT in https://github.com/trpc/trpc/pull/7888
* fix(server): keep websocket subscriptions owned through setup and cleanup by @KATT in https://github.com/trpc/trpc/pull/7704
* fix(server): deliver to every behaviorSubject subscriber when one throws by @KATT in https://github.com/trpc/trpc/pull/7900
* fix(server): ship the root LICENSE in the @trpc/server tarball again by @KATT in https://github.com/trpc/trpc/pull/7904
* fix(server): keep a throwing onError, errorFormatter or encoder from crashing the ws server by @KATT in https://github.com/trpc/trpc/pull/7915
* fix(server): keep the Node adapters running when a streamed body fails or errorFormatter throws by @KATT in https://github.com/trpc/trpc/pull/7931

## @trpc/client

### Features

* feat(client): make subscribe() without callbacks return an async iterable by @KATT in https://github.com/trpc/trpc/pull/7865

### Fixes

* fix(client): send a wsLink request that retryLink retries with the same id by @KATT in https://github.com/trpc/trpc/pull/7889
* fix(client): give each wsLink attempt its own wire id so a late stopped frame can't end the retry by @KATT in https://github.com/trpc/trpc/pull/7892
* fix(client): surface wsClient reconnect errors, and keep reconnecting when onClose or onError throws by @KATT in https://github.com/trpc/trpc/pull/7891
* fix(client): keep wsClient reconnecting when onConnectionStateChange throws by @KATT in https://github.com/trpc/trpc/pull/7896
* fix(client): start the wsLink subscription when onConnectionStateChange throws on the first state by @KATT in https://github.com/trpc/trpc/pull/7899
* fix(client): stop counting a rejection once the socket gets a result by @aliamanatali in https://github.com/trpc/trpc/pull/7860
* fix(client): reject WebSocket batches when sending fails by @maximilliangrand in https://github.com/trpc/trpc/pull/7725
* fix(client): don't flush a later WebSocket request onto a connecting socket by @KATT in https://github.com/trpc/trpc/pull/7911
* fix(client): keep a wsLink socket working when a handler throws by @KATT in https://github.com/trpc/trpc/pull/7926
* fix(client): isolate retired WebSocket close and error events by @maximilliangrand in https://github.com/trpc/trpc/pull/7727

### Refactors

* refactor(client): drop subscribe() runtime guards the types already rule out by @KATT in https://github.com/trpc/trpc/pull/7946

**Full Changelog**: https://github.com/trpc/trpc/compare/v11.24.0...v11.25.0

