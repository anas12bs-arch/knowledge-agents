---
title: "remix-run/remix ui@0.9.0 released"
url: "https://github.com/remix-run/remix/releases/tag/ui%400.9.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-09-09T00:28:03Z"
metadata:
  repo: "remix-run/remix"
  version: "ui@0.9.0"
---

# remix-run/remix ui@0.9.0 released

> Source: github-releases | Category: changelog | 2026-09-09T00:28:03Z

## remix-run/remix — ui@0.9.0

### Minor Changes

- Client entries can now provide import maps through `resolveClientEntry()`. The `<ImportMap>` component from `remix/ui/server` combines your mappings with those from blocking client entries so the initial document contains one complete import map. New mappings from later frame responses are installed before their client entries load. Plain `<script type="importmap">` elements remain supported when you do not need to combine mappings (see #11706).

  When a frame response changes an installed import mapping or integrity value, Remix loads a fresh document so navigation after a deployment cannot mix old and new modules.

- `run()` now accepts a `processClientEntryPreloads` callback to handle preloads for client entries discovered after the initial page load. Use it with `remix/multiple-import-maps-polyfill` to preload modules in browsers that need the polyfill, returning an empty array to skip native modulepreload links. See the [client entry setup example](https://github.com/remix-run/remix/tree/main/packages/multiple-import-maps-polyfill#usage) (see #11706).

### Patch Changes

- `handle.update()` now warns and skips the extra render when called during component setup. Calls during rendering, or before the initial commit from outside setup, report a clear component error. Move these updates into an event handler or a `handle.queueTask()` callback (see #11795).

- Fixed delayed scroll resets and history scroll restoration during frame navigation. Scroll now updates once the destination and its blocking frames first render, without waiting for the rest of the streamed content or client entry hydration. Also fixed scroll jumps in Chromium and stale or repeated scroll changes during redirects and overlapping reloads (see #11755).

  Failed `frame.reload()` calls no longer cause a second unhandled promise rejection when the caller already handles the error.

- Browsers without `NavigateEvent.sourceElement` support now use full document navigation, so links and forms keep working when frame navigation is unavailable (see #11820).

- Frames now render HTML responses with `3xx` and `4xx` status codes, so form validation messages and error pages appear in the frame when using the default resolver. HTML content types are now recognized regardless of case (see #11823).
