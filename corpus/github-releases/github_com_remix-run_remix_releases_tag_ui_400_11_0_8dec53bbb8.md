---
title: "remix-run/remix ui@0.11.0 released"
url: "https://github.com/remix-run/remix/releases/tag/ui%400.11.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-09-28T23:55:19Z"
metadata:
  repo: "remix-run/remix"
  version: "ui@0.11.0"
---

# remix-run/remix ui@0.11.0 released

> Source: github-releases | Category: changelog | 2026-09-28T23:55:19Z

## remix-run/remix — ui@0.11.0

### Minor Changes

- Preserve client-owned attributes during frame reloads with `data-rmx-preserve-attrs="class data-theme"` on any matched element, including `<html>` and `<body>` (see #11809). The named attributes keep their live values or absence while other attributes and children reconcile normally. The incoming HTML controls the list; clearing it or removing a name returns those attributes to normal reconciliation.

### Patch Changes

- Send `X-Remix-Frame: true` from the default browser resolver for all frame loads, including top-frame navigation and reloads. Named frames also send `X-Remix-Target`, allowing handlers to identify and target frame requests consistently across browser and server rendering (see #11941).

- Treat marker-less HTML that starts with a doctype or `<html>` as a document reload, so pages rendered with `renderToString` can be navigated by the client runtime (see #11808).

- Keep hash-only navigations within a fully loaded page and download requests under browser control without reloading a frame. If a hash navigation interrupts a pending frame load, reload the destination so the previous page is not left visible. Preserve downloads even when another navigation listener changes the source link's `download` attribute.

- Preserve parent component context for client entries rendered inside a `<Frame>`, including setup-time context reads when the provider module loads later and after frame reloads. Keep nested frame content interactive when its owning client entry module is already cached (see #11894).

- Preserve server-rendered textarea values when a hydrated client entry first updates, without overwriting uncontrolled user edits.

- Allow client entry props to use ordinary interfaces, including nested objects whose properties are all optional (see #11918).

- Document custom mixin setup, lifecycle events, and deferred host removal with `event.persistNode()`, including cancellation and keyed-node reclamation. Expand public API documentation for root, frame, context, anchoring, CSS mixin, and server-rendering helpers, and correct the popover, context, and anchoring examples.
