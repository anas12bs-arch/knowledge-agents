---
title: "remix-run/remix ui@0.8.0 released"
url: "https://github.com/remix-run/remix/releases/tag/ui%400.8.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-08-31T22:49:04Z"
metadata:
  repo: "remix-run/remix"
  version: "ui@0.8.0"
---

# remix-run/remix ui@0.8.0 released

> Source: github-releases | Category: changelog | 2026-08-31T22:49:04Z

## remix-run/remix — ui@0.8.0

### Minor Changes

- BREAKING CHANGE: Remix UI framework-owned DOM attributes now consistently use the `data-rmx-*` namespace. Rename `rmx-document`, `rmx-target`, `rmx-src`, `rmx-history`, `rmx-reset-scroll`, `rmx-preserve-dom`, and `data-key` to `data-rmx-document`, `data-rmx-target`, `data-rmx-src`, `data-rmx-history`, `data-rmx-reset-scroll`, `data-rmx-preserve-dom`, and `data-rmx-key`. Generated style and module preload markers now use `data-rmx-style` and `data-rmx-module-preload` instead of `data-rmx`.

- BREAKING CHANGE: During server rendering, script elements with non-string children previously serialized those children as escaped HTML text. They now render empty and report an error. Pass a single string child, such as `JSON.stringify(value)`, to embed script content without HTML entity escaping. Script-tag sequences that could terminate the element remain escaped.

- BREAKING CHANGE: Remove `addEventListeners()`. Use native `target.addEventListener(type, listener, { signal })` instead. If a listener used the helper's second callback argument, create an `AbortController` and abort it when the listener runs again or its lifetime signal aborts.

- Added a browser-only SPA response protocol to `remix/ui` for associating bodyless route responses with Remix UI nodes. Application code uses the higher-level `render()` and `run()` APIs from `remix/spa`.

### Patch Changes

- Prevent aborted `renderToStream` requests with multiple blocking `Frame`s from producing unhandled promise rejections that can crash Node servers.

- Changed the scheduler's cascading update guard to warn when many component updates happen in one event-loop turn and only throw the infinite-loop error when a single component instance repeatedly updates itself. This keeps large `clientEntry` hydration bursts interactive while still surfacing component names and counts for diagnosis.

- Fixed `mix` prop types to accept argument-bearing mixins authored for a base element type on compatible subtype elements.

- Gracefully degrade to document navigations for browsers that do not support the Navigation API (see #11665).

- Fix `data-rmx-reset-scroll="false"` and `navigate(..., { resetScroll: false })` to preserve the current scroll position. Default navigations now leave scroll resets and history restoration to the browser.

- Adjust CSS escaping to preserve CSS range media queries such as `@media (width < 900px)` in server-rendered `css()` output while continuing to neutralize literal closing `</style>` tags.

- Restore saved scroll positions for intercepted back and forward navigations when client entry reconciliation temporarily shrinks the document or triggers scroll anchoring, while continuing to wait for nested blocking frames before the Navigation API restores scrolling.

- Prevent Safari Navigation API scroll resets from desynchronizing page hit testing after intercepted push and replace navigations (see [WebKit bug 309542](https://bugs.webkit.org/show_bug.cgi?id=309542)).
