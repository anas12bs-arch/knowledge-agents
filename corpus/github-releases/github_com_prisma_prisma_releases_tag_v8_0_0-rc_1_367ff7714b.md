---
title: "prisma/prisma v8.0.0-rc.1 released"
url: "https://github.com/prisma/prisma/releases/tag/v8.0.0-rc.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "prisma"]
date: "2026-08-07T11:23:46Z"
metadata:
  repo: "prisma/prisma"
  version: "v8.0.0-rc.1"
---

# prisma/prisma v8.0.0-rc.1 released

> Source: github-releases | Category: changelog | 2026-08-07T11:23:46Z

## prisma/prisma — v8.0.0-rc.1

# v8.0.0-rc.1

This is the first release on the v8 release-candidate line: releases are now versioned `8.0.0-rc.N` instead of `0.x` minors. It also makes every aggregate read back through the codec its target declares — `count()` returns a `bigint` — splits the SQL driver interface into a row-streaming call and a statistics call, and fixes four defects in query planning, emit, and driver error reporting.

## The v8 release-candidate line

Releases are now versioned `8.0.0-rc.1`, `8.0.0-rc.2`, and so on, with the counter advancing on every release. "The v8 RC" is the product name; the number underneath iterates freely, so there is no promise that the last RC before `8.0.0` final is numbered `rc.1`. There are no further `0.x` minors. The policy is written up in [`docs/oss/versioning.md`](https://github.com/prisma/prisma/blob/v8.0.0-rc.1/docs/oss/versioning.md). ([#29899](https://github.com/prisma/prisma/pull/29899))

For every package this repository publishes, `latest` keeps tracking the newest release, RC included. These package names have no pre-v8 stable audience to protect — a bare `npm install` of one of them was already an early-access install, and still is. The bare `prisma` package is not published from this repository; its v8 CLI shim lives in [prisma/prisma-cli](https://github.com/prisma/prisma-cli).

**Existing installs are not moved onto the RC line by `npm update`.** Lockfiles pin resolved versions, and a `^0.x` range can never match a `8.0.0-rc.N` pre-release, because pre-releases do not satisfy stable ranges. Only a fresh install, or an explicit version change on your side, lands on the RC.

Development builds move to the same line: every push to `main` that does not change the root version publishes `8.0.0-rc.X-dev.N` under the `dev` dist-tag.

**An RC respin may still contain breaking changes.** Until `8.0.0` final ships, the pre-1.0 latitude documented in [`docs/oss/versioning.md`](https://github.com/prisma/prisma/blob/v8.0.0-rc.1/docs/oss/versioning.md) carries over: a new `rc.N` may remove or rename APIs, change the semantics of existing ones, or change the contract format. Read the breaking-changes section of each release before you upgrade.

## Breaking changes

- **Aggregate results carry the codec their target declares** — an aggregate is now read back through the codec its target declares for that result rather than through whatever the driver handed over, so aggregate application types change. `count()` is a `bigint` on both PostgreSQL and SQLite, at the top level and inside an include, and an empty relation reads `0n`. On PostgreSQL, `sum` over `int2`/`int4` widens to a `bigint`, while `sum(int8)` and `avg` over any integer are `numeric` and read as exact decimal **strings**; `min`/`max` keep the column's own type, except over `varchar`, which returns `text`. On SQLite, `sum` over an integer column is a `bigint` and `avg` is always a `number`. Sweep your code for equality and arithmetic against an aggregate result (`count === 2` is false when `count` is `2n`) and for `JSON.stringify` over one (it throws on a bigint). `having(...)` operands are the exception and stay plain numbers — they are compared inside SQL and never cross a codec. Regenerate your contracts (`prisma-next contract emit`): `contract.d.ts` gains an `AggregateTypes` block that both the ORM and the SQL builder resolve result types from, and against an older contract an aggregate resolves to `never` in the ORM and `unknown` in the SQL builder. The type is not the only guard: an aggregate whose operation and input codec the composed target does not declare is rejected before the query runs, with the error code `ORM.AGGREGATE_UNSUPPORTED`. See the [upgrade recipe](https://github.com/prisma/prisma/blob/v8.0.0-rc.1/skills/prisma-next-upgrade/upgrades/0.17-to-8.0.0-rc.1/) and the [extension-author recipe](https://github.com/prisma/prisma/blob/v8.0.0-rc.1/skills/prisma-8-extension-upgrade/upgrades/0.17-to-8.0.0-rc.1/). ([#29867](https://github
