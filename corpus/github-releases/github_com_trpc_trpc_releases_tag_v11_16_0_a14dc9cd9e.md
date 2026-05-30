---
title: "trpc/trpc v11.16.0 released"
url: "https://github.com/trpc/trpc/releases/tag/v11.16.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "trpc"]
date: "2026-05-30T14:31:23Z"
metadata:
  repo: "trpc/trpc"
  version: "v11.16.0"
---

# trpc/trpc v11.16.0 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:23Z

## trpc/trpc — v11.16.0

## What's Changed
* feat: OpenAPI Cyclic Types support by @Nick-Lucas in https://github.com/trpc/trpc/pull/7283
* chore: Review stale skills (manual) by @github-actions[bot] in https://github.com/trpc/trpc/pull/7294

### `@trpc/openapi` 11.16.0-alpha

* Drops the type depth limit of 20, and significantly hardens cyclic-type support for both inference and Zod
* Support zod.lazy via Standard Schema fallback
* Strip symbols from output (no more `__@asyncIterator@5456` symbols in output)
* Add more comprehensive types for the OpenAPI doc from the official package (now a dependency) and apply some patches to these types because they're slightly outdated
* Fixes several issues with gathering schema descriptions, such as consuming jsdoc comments from node_modules types

## New Contributors
* @github-actions[bot] made their first contribution in https://github.com/trpc/trpc/pull/7294

**Full Changelog**: https://github.com/trpc/trpc/compare/v11.15.1...v11.16.0
