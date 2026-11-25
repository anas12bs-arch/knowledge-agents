---
title: "vitejs/vite v8.4.0-beta.2 released"
url: "https://github.com/vitejs/vite/releases/tag/v8.4.0-beta.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "vite"]
date: "2026-11-25T05:46:12Z"
metadata:
  repo: "vitejs/vite"
  version: "v8.4.0-beta.2"
---

# vitejs/vite v8.4.0-beta.2 released

> Source: github-releases | Category: changelog | 2026-11-25T05:46:12Z

## vitejs/vite — v8.4.0-beta.2

### Features

* add plugin name to hook errors ([#24107](https://github.com/vitejs/vite/issues/24107)) ([40475e5](https://github.com/vitejs/vite/commit/40475e51e785e470b09a67b23d66487649b32226))
* add plugin name to module hook errors ([#24151](https://github.com/vitejs/vite/issues/24151)) ([e1e1ac8](https://github.com/vitejs/vite/commit/e1e1ac831a5f8e5259287796858a854eb2326312))

### Bug Fixes

* close server on failed start (fix [#23965](https://github.com/vitejs/vite/issues/23965)) ([#24020](https://github.com/vitejs/vite/issues/24020)) ([c732677](https://github.com/vitejs/vite/commit/c7326770e1121733435e0527af972f387d64d344))
* **css:** dedupe CSS of inlined common chunks when `cssCodeSplit: false` ([#24168](https://github.com/vitejs/vite/issues/24168)) ([1b34d86](https://github.com/vitejs/vite/commit/1b34d86d957e80532cb7d43897a1692df2bfc42c))
* **deps:** update all non-major dependencies ([#24190](https://github.com/vitejs/vite/issues/24190)) ([87d8a5a](https://github.com/vitejs/vite/commit/87d8a5a96f048ae3bbcd2d19e0449d176e636107))
* **dev:** register references to safe modules only for `server.fs.strict: 'extended'` ([#24206](https://github.com/vitejs/vite/issues/24206)) ([a78fb8a](https://github.com/vitejs/vite/commit/a78fb8a28db01e83611120012bd5d1189bab68aa))
* **html:** keep entry script side effects when another importer loads it first ([#24135](https://github.com/vitejs/vite/issues/24135)) ([ef295d5](https://github.com/vitejs/vite/commit/ef295d54d56478437112acd7deeb9821d755b90f))
* keep plugin error messages as thrown ([#24148](https://github.com/vitejs/vite/issues/24148)) ([24eb35a](https://github.com/vitejs/vite/commit/24eb35ad15694f1145b405c20a36a265f37a34f7))
* **optimizer:** detect in-place patch file edits in lockfile hash ([#24126](https://github.com/vitejs/vite/issues/24126)) ([d7dfe9b](https://github.com/vitejs/vite/commit/d7dfe9b7beedb756f56e509ed425e18af2aa065c))
* **optimizer:** respect top-level tsconfig option when scanning and bundling deps ([#24119](https://github.com/vitejs/vite/issues/24119)) ([760a953](https://github.com/vitejs/vite/commit/760a953fd4b4d1dd58b2652d5962af50a7510d5c))
* preserve drive letter case in `safeRealpathSync` on Windows ([#24146](https://github.com/vitejs/vite/issues/24146)) ([3567471](https://github.com/vitejs/vite/commit/3567471998e3da315675086f44368e266c9c0e33))
* **server:** allow closing uninitialized `DevEnvironment` ([#24184](https://github.com/vitejs/vite/issues/24184)) ([826dcb8](https://github.com/vitejs/vite/commit/826dcb822394b7e8151f745e61f6748865f96c29))
* **server:** keep `this.addWatchFile` in `load` hook on a module's first request ([#23861](https://github.com/vitejs/vite/issues/23861)) ([b516bc2](https://github.com/vitejs/vite/commit/b516bc2f0a0b040a4c4a2fb636bf5bb61d9ad5a2))

### Performance Improvements

* **build:** shift source maps for preload rewrites instead of re-tracing them ([#24049](https://github.com/vitejs/vite/issues/24049)) ([dbce0c6](https://github.com/vitejs/vite/commit/dbce0c6715f26ae602ebf983f87f153a3a8a6e60))
* **build:** skip build import analysis hooks for unaffected chunks ([#24150](https://github.com/vitejs/vite/issues/24150)) ([1a06564](https://github.com/vitejs/vite/commit/1a065640083cafe5ae8b981b9bbfb4b0ddf93632))
* **build:** skip terser plugin when terser is not used ([#24149](https://github.com/vitejs/vite/issues/24149)) ([3bde8ed](https://github.com/vitejs/vite/commit/3bde8eda6d2d1b2c120a705d3d050b84de2c3e43))

### Documentation

* replace stale esbuild references in option JSDoc ([#24196](https://github.com/vitejs/vite/issues/24196)) ([0a19968](https://github.com/vitejs/vite/commit/0a1996890a4f84da995e3d37113a8df5c8e9900b))

### Miscellaneous Chores

* **css:** fix typo in `preliminaryNameToChunkMap` ([#24195](https://github.com/vitejs/vite/issues/24195)) ([3eabee5](https://github.com/vitejs/vite/commit/3eabee5c97e0ea802ebbaed71276d23f73e5b158))

### Code Refactoring

* **build:** skip license plugin via applyToEnvironment w
