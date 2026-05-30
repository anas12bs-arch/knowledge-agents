---
title: "remix-run/remix ui@0.3.0 released"
url: "https://github.com/remix-run/remix/releases/tag/ui%400.3.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-05-30T14:31:17Z"
metadata:
  repo: "remix-run/remix"
  version: "ui@0.3.0"
---

# remix-run/remix ui@0.3.0 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:17Z

## remix-run/remix — ui@0.3.0

### Minor Changes

- BREAKING CHANGE: Remix UI component render functions no longer receive props as an argument. Type component props on `Handle<Props>` and read current values from `handle.props` in both setup and render code.

- Updated `anchor(floating, anchorTarget, options)` to accept either an `HTMLElement` or coordinate target via the new `AnchorPoint`/`AnchorTarget` types.

- Added `menu.contextTrigger()` so menus can open from right-click pointer locations while keeping existing keyboard navigation, submenus, and selection behavior.

### Patch Changes

- Fixed `css(...)` so nested selector objects render recursively instead of serializing deeper nested rules as `[object Object]` (see #11459).

- Dispatch reload events for nested frames when an ancestor frame reloads

- Prevent non-blocking frames from displaying their fallback when an ancestor frame is reloaded
