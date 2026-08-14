---
title: "remix-run/remix ui@0.5.0 released"
url: "https://github.com/remix-run/remix/releases/tag/ui%400.5.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-08-14T03:14:41Z"
metadata:
  repo: "remix-run/remix"
  version: "ui@0.5.0"
---

# remix-run/remix ui@0.5.0 released

> Source: github-releases | Category: changelog | 2026-08-14T03:14:41Z

## remix-run/remix — ui@0.5.0

### Minor Changes

- BREAKING CHANGE: Browser `resolveFrame` callbacks now receive a single options object instead of positional signal and target arguments. Update `resolveFrame(src, signal, target)` implementations to use `resolveFrame(src, options)` and read `options?.signal` and `options?.target`.

- Added `frames` to the `app` object returned from `run()`, mirroring the existing `handle.frames` API

- Added `@remix-run/ui/dev/refresh` for development tooling that needs to reconcile mounted roots after component modules update.

- Same-origin forms now progressively enhance into frame navigations when `run({ resolveFrame })` is configured. Native constraint validation runs before interception, submissions target the top frame by default, `rmx-target` selects a named frame, and `rmx-document` opts back into document navigation. For non-GET submissions, resolvers receive the browser's native `FormData` plus the selected method and encoding, and remain responsible for request encoding and `_method` conventions. Non-GET submissions to the current URL replace its history entry without retaining their `FormData`; submissions to a different URL and GET submissions push a new entry.

- Browser frame resolvers may now return a `Response`. Its body is streamed into the frame, and when a top-frame navigation follows a redirect, the final response URL replaces the current navigation entry and becomes the frame's canonical `src` without loading the frame a second time. Direct reloads and named-frame navigations render the redirected response without replacing their canonical `src` with the final response URL.

- Add an `rmx-history="push|replace"` attribute for anchors and forms that overrides the history behavior of enhanced frame navigations. Native anchors using `link(href, { history })` emit the corresponding attribute value automatically.

- Add an `rmx-preserve-dom` attribute that tells the DOM reconciler to preserve a matching element's current attributes and children during reloads, allowing client-owned subtrees such as custom elements to manage their own DOM.

### Patch Changes

- Allow element-wide mixins such as `css()` to be used on subtype hosts like `<select>` without TypeScript assignability errors.

- Built-in styled components now use adaptive `light-dark(...)` colors for their internal surfaces, text, borders, focus rings, and control states so they render correctly in dark color schemes.

- Escape less-than characters in server-rendered `css()` output so style values cannot terminate the generated `<style>` element.

- Fix hydrated component updates that could lose content when adding elements before existing content in a fragment

- Prevent navigation and reloads from hanging when a nested `Frame` marker moves outside a frame region while the DOM is being updated.

- Preserve client entry and frame state only for live boundaries with matching semantic identities, while replacing pending client entry SSR during reloads and releasing temporary response metadata after hydration or cancellation.

- Prevent client-side document navigation and `Frame` updates from stalling after navigating between pages with different `Frame` layouts. A frame's end marker could be reused as the start marker of an incoming frame, which left the frame's region bounds and instance pointing at the wrong nodes.

- Preserve resolved client-created frame content when its parent rerenders while the frame is still pending (see #11659).

- Prevent document and frame reloads from dropping newly rendered sibling elements when client entries from the previous content are disposed.

- Reload frames rendered within preserved client entries during ancestor frame reloads

- Show complete destination server-rendered client entry content during document and frame reloads while replacement modules load, instead of retaining only positionally matched source content.

- Fix top frame reloads using the previous URL after navigation targets a named frame.
