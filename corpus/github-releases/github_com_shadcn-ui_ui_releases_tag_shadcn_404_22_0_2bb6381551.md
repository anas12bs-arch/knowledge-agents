---
title: "shadcn-ui/ui shadcn@4.22.0 released"
url: "https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.22.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ui"]
date: "2026-10-16T21:52:03Z"
metadata:
  repo: "shadcn-ui/ui"
  version: "shadcn@4.22.0"
---

# shadcn-ui/ui shadcn@4.22.0 released

> Source: github-releases | Category: changelog | 2026-10-16T21:52:03Z

## shadcn-ui/ui — shadcn@4.22.0

### Minor Changes

- [#12298](https://github.com/shadcn-ui/ui/pull/12298) [`954ce95`](https://github.com/shadcn-ui/ui/commit/954ce953412867a57b7e067c076fa7fd395ea115) Thanks [@shadcn](https://github.com/shadcn)! - Upgrade to Zod 4. `shadcn/schema` and `@shadcn/registry/schema` now export Zod 4 schemas, so passing them to Zod 3's `z` no longer typechecks. On Zod 3, use the exported types (`RegistryItem`, `RegistryItemFile`, `Config`) and the schema's own methods (`registryItemSchema.array()`) instead of `z.infer` and `z.array`. Zod errors expose `issues`, not `errors`. Validation messages now use Zod 4's wording.

### Patch Changes

- Updated dependencies [[`954ce95`](https://github.com/shadcn-ui/ui/commit/954ce953412867a57b7e067c076fa7fd395ea115)]:
  - @shadcn/registry@0.2.0
