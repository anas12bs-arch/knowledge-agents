---
title: "prisma/prisma v0.17.0 released"
url: "https://github.com/prisma/prisma/releases/tag/v0.17.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "prisma"]
date: "2026-08-04T15:45:13Z"
metadata:
  repo: "prisma/prisma"
  version: "v0.17.0"
---

# prisma/prisma v0.17.0 released

> Source: github-releases | Category: changelog | 2026-08-04T15:45:13Z

## prisma/prisma — v0.17.0

# v0.17.0

This is the namespace release: Prisma Next now publishes as 17 packages under the `@prisma` scope, and an application depends on exactly one database facade. It also completes the structured error-code scheme across every plane, makes relation-loading lossless for big numbers and temporal values, and gives every SQL index and RLS policy an exact, migratable name.

## Breaking changes

- **One `@prisma` package per application** — the `@prisma-next/*` scope is retired; nothing publishes under it again. An application depends on exactly one database facade — `@prisma/orm-postgres`, `@prisma/orm-sqlite`, or `@prisma/orm-mongo` — plus any extension packs it uses (now named `@prisma/orm-extension-*`); everything else arrives as the facade's exact-pinned dependencies. Regenerating your contract rewrites generated imports to facade entrypoints with no `contractHash` change. See the [0.16-to-0.17 upgrade recipe](https://github.com/prisma/prisma/blob/v0.17.0/skills/upgrade/prisma-next-upgrade/upgrades/0.16-to-0.17/) and the [extension-author recipe](https://github.com/prisma/prisma/blob/v0.17.0/skills/extension-author/prisma-8-extension-upgrade/upgrades/0.16-to-0.17/). ([#29864](https://github.com/prisma/prisma/pull/29864), [#29880](https://github.com/prisma/prisma/pull/29880), [#29883](https://github.com/prisma/prisma/pull/29883), [#29884](https://github.com/prisma/prisma/pull/29884))

  Before:

  ```jsonc
  "dependencies": {
    "@prisma-next/postgres": "0.16.0",
    "@prisma-next/framework-components": "0.16.0",
    "@prisma-next/sql-runtime": "0.16.0"
  }
  ```

  After:

  ```jsonc
  "dependencies": {
    "@prisma/orm-postgres": "0.17.0"
  }
  ```

- **Every published error is a structured envelope with a dotted code** — the four legacy error systems (`PN-CLI-4001`-style codes, `RUNTIME.DECODE_FAILED`-style codes, and codeless error classes) consolidate into one scheme: a structural envelope carrying a `NAMESPACE.SUBCODE` code, recognized by the `isStructuredError` type predicate instead of `instanceof`. The ORM, contract-authoring, adapter/target, extension, and framework planes are all swept; legacy error classes (`PslFormatError`, the Supabase and SQL-escape classes, framework classes) are deleted. Prisma 7's `P1001`-style codes are not carried over. ([#1016](https://github.com/prisma/prisma-next/pull/1016), [#1021](https://github.com/prisma/prisma-next/pull/1021), [#1025](https://github.com/prisma/prisma-next/pull/1025), [#1049](https://github.com/prisma/prisma-next/pull/1049), [#1053](https://github.com/prisma/prisma-next/pull/1053), [#1063](https://github.com/prisma/prisma-next/pull/1063))

  Before:

  ```ts
  if (error instanceof PslFormatError) {
    report(error.diagnostics);
  }
  ```

  After:

  ```ts
  if (isStructuredError(error) && error.code === 'PSL.PARSE_FAILED') {
    report(error.meta.diagnostics);
  }
  ```

- **Content hashes are bare hex** — the `sha256:` prefix is gone from every surface (emitted contracts, migration manifests, refs, CLI output, and the database marker), and loaders reject the prefixed form. Contract hash values are unchanged; `migrationHash` values change. A codemod in the [0.16-to-0.17 recipe](https://github.com/prisma/prisma/blob/v0.17.0/skills/upgrade/prisma-next-upgrade/upgrades/0.16-to-0.17/) converts checked-in migration trees. ([#1033](https://github.com/prisma/prisma-next/pull/1033))

- **Migration contract snapshots move into a content-addressed store** — per-migration sibling snapshot files and ref-paired copies are replaced by a single `migrations/snapshots/<hex>/` store per migrations root; every distinct contract is stored once, and `migration.ts` imports its bookend contracts from the store. This is a clean break with no fallback reader; a one-shot migrator (`scripts/migrate-migrations-layout.mjs`) converts existing trees and re-verifies every `migrationHash` unchanged. ([#1018](https://github.com/prisma/prisma-next/pull/1018), [#1024](https://github.com/prisma/p
