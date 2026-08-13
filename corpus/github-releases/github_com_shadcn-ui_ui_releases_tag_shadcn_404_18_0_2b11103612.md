---
title: "shadcn-ui/ui shadcn@4.18.0 released"
url: "https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.18.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ui"]
date: "2026-08-13T19:34:08Z"
metadata:
  repo: "shadcn-ui/ui"
  version: "shadcn@4.18.0"
---

# shadcn-ui/ui shadcn@4.18.0 released

> Source: github-releases | Category: changelog | 2026-08-13T19:34:08Z

## shadcn-ui/ui — shadcn@4.18.0

### Minor Changes

- [#11501](https://github.com/shadcn-ui/ui/pull/11501) [`aef1cdca54e8da689351cdddf959342909e45e76`](https://github.com/shadcn-ui/ui/commit/aef1cdca54e8da689351cdddf959342909e45e76) Thanks [@shadcn](https://github.com/shadcn)! - merge registries from package.json and components.json, and support adding registries to package.json when components.json is not present

### Patch Changes

- [#11500](https://github.com/shadcn-ui/ui/pull/11500) [`e66b99b14dd9c54afc434dbf5a702f170b1153b0`](https://github.com/shadcn-ui/ui/commit/e66b99b14dd9c54afc434dbf5a702f170b1153b0) Thanks [@shadcn](https://github.com/shadcn)! - Skip unreadable directories during file scans instead of failing with `EACCES`.

- [#11504](https://github.com/shadcn-ui/ui/pull/11504) [`9f4e3ff26025d16a243ea03cc891c734c4cf0b59`](https://github.com/shadcn-ui/ui/commit/9f4e3ff26025d16a243ea03cc891c734c4cf0b59) Thanks [@shadcn](https://github.com/shadcn)! - Skip unreadable directories when resolving monorepo targets.

- [#11502](https://github.com/shadcn-ui/ui/pull/11502) [`87d71b3629c34f3c38a353a211ec8591c1ff1721`](https://github.com/shadcn-ui/ui/commit/87d71b3629c34f3c38a353a211ec8591c1ff1721) Thanks [@shadcn](https://github.com/shadcn)! - resolve registries declared in package.json when adding components. `shadcn add`, `search`, `view` and `init` now resolve registries from package.json in memory without persisting them to components.json

- [#9248](https://github.com/shadcn-ui/ui/pull/9248) [`03c45b822e60195796dfd3d2fcf7c223ff4ece86`](https://github.com/shadcn-ui/ui/commit/03c45b822e60195796dfd3d2fcf7c223ff4ece86) Thanks [@Grafikart](https://github.com/Grafikart)! - Fix shadcn for projects with unreadable permission files
