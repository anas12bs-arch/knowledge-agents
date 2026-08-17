---
title: "remix-run/remix static-middleware@0.4.14 released"
url: "https://github.com/remix-run/remix/releases/tag/static-middleware%400.4.14"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-08-17T22:48:12Z"
metadata:
  repo: "remix-run/remix"
  version: "static-middleware@0.4.14"
---

# remix-run/remix static-middleware@0.4.14 released

> Source: github-releases | Category: changelog | 2026-08-17T22:48:12Z

## remix-run/remix — static-middleware@0.4.14

### Patch Changes

- Fixed `staticFiles()` middleware types being incompatible with other router middleware by updating `@remix-run/fetch-router` to `^0.21.0`. This keeps the established `@remix-run/static-middleware` package compatible with Remix 3 projects without package-manager overrides.
