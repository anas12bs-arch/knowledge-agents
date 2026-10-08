---
title: "vitejs/vite v8.3.4 released"
url: "https://github.com/vitejs/vite/releases/tag/v8.3.4"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "vite"]
date: "2026-10-08T14:39:39Z"
metadata:
  repo: "vitejs/vite"
  version: "v8.3.4"
---

# vitejs/vite v8.3.4 released

> Source: github-releases | Category: changelog | 2026-10-08T14:39:39Z

## vitejs/vite — v8.3.4

### Features

* **bundled-dev:** support `import.meta.hot.acceptExports` ([#23463](https://github.com/vitejs/vite/issues/23463)) ([bc0f21c](https://github.com/vitejs/vite/commit/bc0f21c56a2e003a4d2dd23ccb9da3ec8c706c4e))

### Bug Fixes

* avoid mutating hmr defaults (fix [#23575](https://github.com/vitejs/vite/issues/23575)) ([#23576](https://github.com/vitejs/vite/issues/23576)) ([574d5e3](https://github.com/vitejs/vite/commit/574d5e351905fe99891364d03c2440531378f7fd))
* **build:** correct preloads when chunkImportMap is enabled with non-root base ([#23698](https://github.com/vitejs/vite/issues/23698)) ([2a8c0f0](https://github.com/vitejs/vite/commit/2a8c0f05c76e35c43ab3560984a5103c8db8dbcd))
* **build:** wait for in-flight stylesheets in preload helper (fix [#23652](https://github.com/vitejs/vite/issues/23652)) ([#23662](https://github.com/vitejs/vite/issues/23662)) ([036b745](https://github.com/vitejs/vite/commit/036b74599b2fe1d8c61475371b856ceb88d26963))
* **bundled-dev:** serve `/@vite/client` and stub `@vite/env` ([#23664](https://github.com/vitejs/vite/issues/23664)) ([5afc5a8](https://github.com/vitejs/vite/commit/5afc5a8876624888fc1e8f43fed1c85c4b0e830b))
* **client:** skip rewriting unchanged adopted styles ([#23697](https://github.com/vitejs/vite/issues/23697)) ([fa71469](https://github.com/vitejs/vite/commit/fa7146938b0ca703653c90c20907191a01c032ba))
* **css:** resolve imported preprocessors from their file path with lightningcss ([#23688](https://github.com/vitejs/vite/issues/23688)) ([cf52011](https://github.com/vitejs/vite/commit/cf52011c46409a4a45f3d74bba631b8f005c4bc9))
* **deps:** update all non-major dependencies ([#23648](https://github.com/vitejs/vite/issues/23648)) ([8a4c19c](https://github.com/vitejs/vite/commit/8a4c19cfc035f2dd203f2fa6d00ab9256a5e77c9))
* **deps:** update rolldown-related dependencies ([#23649](https://github.com/vitejs/vite/issues/23649)) ([794516d](https://github.com/vitejs/vite/commit/794516d50cff80e405bc9b3e5faac1c82987566c))
* **dev:** a restart requested during a restart used to be dropped (fix [#23392](https://github.com/vitejs/vite/issues/23392)) ([#23484](https://github.com/vitejs/vite/issues/23484)) ([70d56ea](https://github.com/vitejs/vite/commit/70d56ea1848909edab416934f3f68ce14343eb73))
* don't treat modules ending with js-like query as js ([#23687](https://github.com/vitejs/vite/issues/23687)) ([fcb6f12](https://github.com/vitejs/vite/commit/fcb6f1252a95857823d935f98554b938888d41a0))
* **html:** avoid adding filesystem root to watcher ([#23689](https://github.com/vitejs/vite/issues/23689)) ([3a7f2ae](https://github.com/vitejs/vite/commit/3a7f2aea757d59bae66ad6edf6b321d26a7e6778))
* **html:** skip caching CSS of chunks in a cycle (fix [#23628](https://github.com/vitejs/vite/issues/23628)) ([#23636](https://github.com/vitejs/vite/issues/23636)) ([15d82f7](https://github.com/vitejs/vite/commit/15d82f7dc679ab9c18d5ce2c3711157c2365ddd1))
* **optimizer:** scan deep imports with custom extensions ([#23678](https://github.com/vitejs/vite/issues/23678)) ([8579189](https://github.com/vitejs/vite/commit/8579189bae8626b6ddab55a09325e209d62e027e))
* remove input option unescaping for now ([#23694](https://github.com/vitejs/vite/issues/23694)) ([facc2fb](https://github.com/vitejs/vite/commit/facc2fb1fffce03d9e2dd7011d0bd0eeddc7d0f6))
* **server:** match static aliases on path boundaries ([#23643](https://github.com/vitejs/vite/issues/23643)) ([b28db28](https://github.com/vitejs/vite/commit/b28db28e9e62d9866a9a0f1b22e74589cc180577))
* **watcher:** normalize file before root check in `ensureWatchedFile` ([#23673](https://github.com/vitejs/vite/issues/23673)) ([12bb28c](https://github.com/vitejs/vite/commit/12bb28c22379c8d2fe90088fa0eefbfa2ab3fb80))

### Performance Improvements

* **module-runner:** skip cloning call sites that have no source map ([#23646](https://github.com/vitejs/vite/issues/23646)) ([3d67486](https://github.com/vitejs/vite/commit/3d674869a50a0bca84a8cc8dc55bd35d57100e3
