---
title: "prisma/prisma v8.0.0-rc.2 released"
url: "https://github.com/prisma/prisma/releases/tag/v8.0.0-rc.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "prisma"]
date: "2026-08-17T16:35:30Z"
metadata:
  repo: "prisma/prisma"
  version: "v8.0.0-rc.2"
---

# prisma/prisma v8.0.0-rc.2 released

> Source: github-releases | Category: changelog | 2026-08-17T16:35:30Z

## prisma/prisma — v8.0.0-rc.2

# v8.0.0-rc.2

This release retires the `prisma-next` binary in favour of the unified `prisma` CLI, returns the default aggregates to plain JavaScript numbers with lossless variants beside them, makes CHECK constraints a declared part of the contract, and splits runtime row queries from non-returning writes. Almost every application will need to re-emit its contract and rename its config file, so read the breaking changes before upgrading.

Two upgrade recipes carry the mechanical translations for this hop: the [user recipe](https://github.com/prisma/prisma/blob/v8.0.0-rc.2/skills/prisma-next-upgrade/upgrades/8.0.0-rc.1-to-8.0.0-rc.2/) and the [extension-author recipe](https://github.com/prisma/prisma/blob/v8.0.0-rc.2/skills/prisma-8-extension-upgrade/upgrades/8.0.0-rc.1-to-8.0.0-rc.2/).

## Breaking changes

- **This repository no longer publishes a CLI; the unified `prisma` CLI replaces it** — nothing published ships a `prisma-next` bin anymore. `@prisma/orm-toolchain` exposes the `orm` command family at `@prisma/orm-toolchain/cli` and no binary, and the database facades forward no launcher. Install `@prisma/cli` (the prisma-cli distribution, published under `next` for the v8 line) and replace `prisma-next <command>` in package scripts and CI with the unified CLI. The config file moves with it: `prisma-next.config.ts` is deprecated in favour of `prisma.config.ts`, and the config value is now engine-shaped, with your existing ORM config nested under an `orm` section. Both the old filename and the flat shape still load, each printing a deprecation warning on stderr, so the rename and the rewrap can land separately. See the [user recipe](https://github.com/prisma/prisma/blob/v8.0.0-rc.2/skills/prisma-next-upgrade/upgrades/8.0.0-rc.1-to-8.0.0-rc.2/). ([#30005](https://github.com/prisma/prisma/pull/30005))

  Before:

  ```ts
  // prisma-next.config.ts
  import { defineConfig } from '@prisma/orm-postgres/config';

  export default defineConfig({ contract: './contract.ts', output: './generated' });
  ```

  After:

  ```ts
  // prisma.config.ts
  import { defineConfig } from '@prisma/cli-engine';
  import { defineConfig as ormConfig } from '@prisma/orm-postgres/config';

  export default defineConfig({
    orm: ormConfig({ contract: './contract.ts', output: './generated' }),
  });
  ```

- **The default aggregates are JavaScript numbers again, with lossless variants beside them** — `count()`, `sum()` over an integer column, and `avg()` over an integer column all return `number`. In `8.0.0-rc.1` they returned a `bigint`, a `bigint` or decimal string depending on the column's width, and a decimal string respectively. The lossless results moved to three new operations: `countBigInt()` returns a `bigint`, `sumBigInt()` returns a `bigint`, and `avgDecimal()` returns an exact decimal string (PostgreSQL only — SQLite has no decimal type and contributes none). A `count()` or integer `sum()` whose value passes ±(2^53 − 1) now raises `RUNTIME.DECODE_FAILED` rather than returning a rounded number, so move those calls to the `BigInt` variants where the magnitude is real. Unchanged: `min`/`max`, `sum`/`avg` over a float column, `sum` over `Decimal`, `sum` over `UnboundedInt`, and the ORM's `having(...)` operands. The SQL builder's comparison operands do move, because `fns.gt(a, b)` types both sides from one codec. The same PR also makes the wide-integer codecs refuse the wrong JavaScript type: a `BigInt` or `UnboundedInt` column rejects a `number` and a `BigIntNumber` column rejects a `bigint`, with `RUNTIME.ENCODE_FAILED` naming the type that arrived, where previously a number was accepted and stringified — which let a fractional value reach an integer column unremarked. See the [user recipe](https://github.com/prisma/prisma/blob/v8.0.0-rc.2/skills/prisma-next-upgrade/upgrades/8.0.0-rc.1-to-8.0.0-rc.2/). ([#29930](https://github.com/prisma/prisma/pull/29930))

  Before:

  ```ts
  const { total } = await db.User.aggregate((a) => ({ total: a.c
