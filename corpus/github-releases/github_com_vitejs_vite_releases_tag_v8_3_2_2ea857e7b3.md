---
title: "vitejs/vite v8.3.2 released"
url: "https://github.com/vitejs/vite/releases/tag/v8.3.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "vite"]
date: "2026-10-01T16:26:48Z"
metadata:
  repo: "vitejs/vite"
  version: "v8.3.2"
---

# vitejs/vite v8.3.2 released

> Source: github-releases | Category: changelog | 2026-10-01T16:26:48Z

## vitejs/vite — v8.3.2

### Bug Fixes

* **build:** preload CSS correctly when `renderBuiltUrl` returns URLs with queries ([#23611](https://github.com/vitejs/vite/issues/23611)) ([64e0a21](https://github.com/vitejs/vite/commit/64e0a215c24f0522b27b91f93cfd93e317b94481))
* **bundled-dev:** serve lazy chunk sourcemaps ([#23026](https://github.com/vitejs/vite/issues/23026)) ([eb7aa9a](https://github.com/vitejs/vite/commit/eb7aa9a8816a1e926d5d9b4cbe7e796b61314ce2))
* **bundled-dev:** serve the rolldown runtime from the installed rolldown ([#23568](https://github.com/vitejs/vite/issues/23568)) ([bc598a6](https://github.com/vitejs/vite/commit/bc598a6a8a6b7d6e157e9f19c16911cff8d2360c))
* **deps:** update all non-major dependencies ([#23601](https://github.com/vitejs/vite/issues/23601)) ([9944fa6](https://github.com/vitejs/vite/commit/9944fa6033873f13ae88f59e023ab642c50fee2b))
* **deps:** update rolldown-related dependencies ([#23602](https://github.com/vitejs/vite/issues/23602)) ([88c1741](https://github.com/vitejs/vite/commit/88c17415af221b3a13e778f4f2c0e907c8287baf))
* **html:** resolve percent-encoded srcset urls ([#23609](https://github.com/vitejs/vite/issues/23609)) ([53f1ce7](https://github.com/vitejs/vite/commit/53f1ce7bfe38426861f6da572ef0e3359f6a80cd))
* limit size of object and array printing via `forwardConsole` ([#23565](https://github.com/vitejs/vite/issues/23565)) ([e64a587](https://github.com/vitejs/vite/commit/e64a5877dd3e552843a545749ccc257568917d28))
* merge `build.rolldownOptions.output.minify` correctly ([#23536](https://github.com/vitejs/vite/issues/23536)) ([bba3bb8](https://github.com/vitejs/vite/commit/bba3bb8beedd185948956e02667d450672632d79))
* **optimize-deps:** avoid "unsupported" warnings for browser:false mappings ([#23590](https://github.com/vitejs/vite/issues/23590)) ([5e4b9ca](https://github.com/vitejs/vite/commit/5e4b9ca3dcb24b51f58a765fd2d852614bbf3574))
* **optimizer:** preserve excluded optional peer require fallbacks ([#23600](https://github.com/vitejs/vite/issues/23600)) ([a2bd6fa](https://github.com/vitejs/vite/commit/a2bd6fa897c35c8a691671a7d70061c1cdd5c688))
* pass queries to `renderBuiltUrl` ([#23586](https://github.com/vitejs/vite/issues/23586)) ([744269e](https://github.com/vitejs/vite/commit/744269e5b2a155074910ddd275aecf2b83938496))
* **server:** handle file watcher errors without crashing ([#23503](https://github.com/vitejs/vite/issues/23503)) ([6894f5c](https://github.com/vitejs/vite/commit/6894f5cbceac589536a0efb476d881a47f5ab1c5))
* **server:** release previous environments after initialization ([#23499](https://github.com/vitejs/vite/issues/23499)) ([5a3a010](https://github.com/vitejs/vite/commit/5a3a010eea4c9ebbdcc080819f93068d4e035bd4))
* **ssr:** encode whitespace in module runner sourceURL ([#23513](https://github.com/vitejs/vite/issues/23513)) ([bbc8812](https://github.com/vitejs/vite/commit/bbc88129c967a8b8eedebd93acc82bee63b86b2a))
* **worker:** align worker urls in client and server when using terser ([#23614](https://github.com/vitejs/vite/issues/23614)) ([24bd331](https://github.com/vitejs/vite/commit/24bd3316f3b2503d04a49361e365532bdb335e19))

### Performance Improvements

* avoid encoding intermediate source maps ([#23461](https://github.com/vitejs/vite/issues/23461)) ([89574f6](https://github.com/vitejs/vite/commit/89574f6d940a7273a53c5122a4477285801a696a))
* **build:** avoid quadratic link scan in the preload helper ([#23510](https://github.com/vitejs/vite/issues/23510)) ([cf5c028](https://github.com/vitejs/vite/commit/cf5c0288d526824aead1b24e977400f13c527927))
* only register time middleware when debug logging is enabled ([#23621](https://github.com/vitejs/vite/issues/23621)) ([94d0080](https://github.com/vitejs/vite/commit/94d0080345e23d63d4cd02df2f7fa2afae775c26))

### Documentation

* fix dead og-image PNG links in vite6/vite7 changelog entries ([#23594](https://github.com/vitejs/vite/issues/23594)) ([1929b4c](https://github.com/vitejs/vite/commit/1929b4cc5f38ad53781e3b07b8bdaa32cf18da07))
