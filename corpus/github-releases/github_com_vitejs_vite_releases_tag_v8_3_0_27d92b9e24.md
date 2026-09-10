---
title: "vitejs/vite v8.3.0 released"
url: "https://github.com/vitejs/vite/releases/tag/v8.3.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "vite"]
date: "2026-09-10T11:46:12Z"
metadata:
  repo: "vitejs/vite"
  version: "v8.3.0"
---

# vitejs/vite v8.3.0 released

> Source: github-releases | Category: changelog | 2026-09-10T11:46:12Z

## vitejs/vite — v8.3.0

### Features

* **build:** avoid settling seen preload dependencies for performance ([#23446](https://github.com/vitejs/vite/issues/23446)) ([e6f6b3e](https://github.com/vitejs/vite/commit/e6f6b3e3119256daa837b2dc399058c8aa45b470))

### Bug Fixes

* handle CRLF line endings in code frame positions ([#23219](https://github.com/vitejs/vite/issues/23219)) ([9913672](https://github.com/vitejs/vite/commit/9913672bee9c34a2df7fff4c2538783cd4f43b4e))
* only treat whole `node_modules` path segments as dependencies (fix [#17467](https://github.com/vitejs/vite/issues/17467)) ([#23437](https://github.com/vitejs/vite/issues/23437)) ([ef0dc17](https://github.com/vitejs/vite/commit/ef0dc17ada53d1169ae5a89cb8f6482831466755))

### Performance Improvements

* **proxy:** pre-compile context matchers at server creation ([#23263](https://github.com/vitejs/vite/issues/23263)) ([8abf700](https://github.com/vitejs/vite/commit/8abf700eeb2411d8402d08f8e2696effafdbe774))

