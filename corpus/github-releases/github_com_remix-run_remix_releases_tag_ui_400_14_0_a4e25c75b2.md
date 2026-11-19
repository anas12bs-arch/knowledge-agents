---
title: "remix-run/remix ui@0.14.0 released"
url: "https://github.com/remix-run/remix/releases/tag/ui%400.14.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-11-19T04:02:34Z"
metadata:
  repo: "remix-run/remix"
  version: "ui@0.14.0"
---

# remix-run/remix ui@0.14.0 released

> Source: github-releases | Category: changelog | 2026-11-19T04:02:34Z

## remix-run/remix — ui@0.14.0

### Minor Changes

- BREAKING CHANGE: The `animateExit()` mixin now starts animations synchronously in `beforeRemove` instead of deferring them to a microtask. This allows `animateLayout()` to measure the updated layout when exiting elements are taken out of normal flow. ([#12220](https://github.com/remix-run/remix/pull/12220))

  This is unlikely to be a breaking change for most consumers. Custom mixins used alongside `animateExit()` may be affected if they inspect computed styles or call `getAnimations()` in `beforeRemove` and rely on the exit animation starting later.

- `animateEntrance()` and `animateExit()` mixins now support per-property timing and compositing overrides via the `transition` option. ([#12220](https://github.com/remix-run/remix/pull/12220))

- Validate native controls with a shared form schema using `@remix-run/ui/form`. `form.Context` supplies field bindings, and `root`, `control`, `label`, and `error` mixins provide native constraints, validation feedback, and accessible associations. Failed submissions restore values and display errors. Applications own the markup, and forms work with or without JavaScript. These experimental APIs may change or be removed in patch releases. ([#11630](https://github.com/remix-run/remix/pull/11630))

- Added `@remix-run/ui/toast` for accessible toast notifications. A shared manager retains notifications in the browser, with providers and mixins connecting them to your own markup after mounting. ([#12084](https://github.com/remix-run/remix/pull/12084))

### Patch Changes

- Bumped `@remix-run/*` dependencies:
  - [`component@1.3.0`](https://github.com/remix-run/remix/releases/tag/component@1.3.0)
  - [`data-schema@1.0.1`](https://github.com/remix-run/remix/releases/tag/data-schema@1.0.1)
