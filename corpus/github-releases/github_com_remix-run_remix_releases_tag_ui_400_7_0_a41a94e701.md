---
title: "remix-run/remix ui@0.7.0 released"
url: "https://github.com/remix-run/remix/releases/tag/ui%400.7.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-08-17T22:25:15Z"
metadata:
  repo: "remix-run/remix"
  version: "ui@0.7.0"
---

# remix-run/remix ui@0.7.0 released

> Source: github-releases | Category: changelog | 2026-08-17T22:25:15Z

## remix-run/remix — ui@0.7.0

### Minor Changes

- `run()` now uses a default browser frame resolver when `resolveFrame` is omitted. Apps that supplied a resolver only to fetch frame HTML can remove it:

  ```diff
   let app = run({
     loadModule,
  -  resolveFrame(src, options) {
  -    return fetch(src, {
  -      headers: { Accept: 'text/html' },
  -      signal: options?.signal,
  -    })
  -  },
   })
  ```

  All `run()` calls now enable frame reloads and same-origin link and form navigation through the Navigation API. The default resolver submits the requested method, encoding, and form data, and rejects non-OK responses. Keep a custom `resolveFrame` when the app needs custom request headers, body encoding, response handling, or error UI. Add `rmx-document` to a link or form to leave that navigation to the browser (see #11693).
