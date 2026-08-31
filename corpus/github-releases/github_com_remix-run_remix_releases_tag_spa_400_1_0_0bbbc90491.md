---
title: "remix-run/remix spa@0.1.0 released"
url: "https://github.com/remix-run/remix/releases/tag/spa%400.1.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-08-31T22:49:04Z"
metadata:
  repo: "remix-run/remix"
  version: "spa@0.1.0"
---

# remix-run/remix spa@0.1.0 released

> Source: github-releases | Category: changelog | 2026-08-31T22:49:04Z

## remix-run/remix — spa@0.1.0

### Minor Changes

- Added the initial `@remix-run/spa` package with `render()` middleware and a `run(router, { fallback? })` browser runtime for client-rendered Remix applications. Route handlers use `context.render()` while the package preserves the router's `Request` to `Response` contract and hides the SPA response carrier.

### Patch Changes

- Bumped `@remix-run/*` dependencies:
  - [`render-middleware@0.2.0`](https://github.com/remix-run/remix/releases/tag/render-middleware@0.2.0)
  - [`ui@0.8.0`](https://github.com/remix-run/remix/releases/tag/ui@0.8.0)
