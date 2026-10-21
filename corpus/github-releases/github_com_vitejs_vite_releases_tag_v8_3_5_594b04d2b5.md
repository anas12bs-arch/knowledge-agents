---
title: "vitejs/vite v8.3.5 released"
url: "https://github.com/vitejs/vite/releases/tag/v8.3.5"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "vite"]
date: "2026-10-21T11:43:47Z"
metadata:
  repo: "vitejs/vite"
  version: "v8.3.5"
---

# vitejs/vite v8.3.5 released

> Source: github-releases | Category: changelog | 2026-10-21T11:43:47Z

## vitejs/vite — v8.3.5

### Bug Fixes

* **build:** handle missing chunk import maps ([#23777](https://github.com/vitejs/vite/issues/23777)) ([8d7623d](https://github.com/vitejs/vite/commit/8d7623d9b5647714a5b20cbd787a5401ca846229))
* **build:** include preload dependencies to chunk import map hashing ([#23793](https://github.com/vitejs/vite/issues/23793)) ([4d16e7c](https://github.com/vitejs/vite/commit/4d16e7c14d5e1c361f148238b1e81131238ab8e9))
* **bundled-dev:** apply `server.origin` to asset URLs ([#23683](https://github.com/vitejs/vite/issues/23683)) ([52ba877](https://github.com/vitejs/vite/commit/52ba877693c8633458d163117504a8259beb3cf5))
* **bundled-dev:** declare utf-8 charset in fallback page ([#23846](https://github.com/vitejs/vite/issues/23846)) ([197daf6](https://github.com/vitejs/vite/commit/197daf6c4c7bfdaa005bebcc41dd2ff22fa3a5b6))
* **bundled-dev:** ignore build.chunkImportMap ([#23685](https://github.com/vitejs/vite/issues/23685)) ([cfe917d](https://github.com/vitejs/vite/commit/cfe917d67d279a13f20ae9449e3befa736b64b07))
* **bundled-dev:** include user `import.meta.env.*` defines in the `import.meta.env` object ([#23713](https://github.com/vitejs/vite/issues/23713)) ([6019aa7](https://github.com/vitejs/vite/commit/6019aa79975465516da7c6f532d568422b019a25))
* **bundled-dev:** map forwarded error stacks through the bundle source maps ([#23741](https://github.com/vitejs/vite/issues/23741)) ([11fe1e4](https://github.com/vitejs/vite/commit/11fe1e46ff0c136cb90fbe263ba03993bc94df18))
* **bundled-dev:** normalize served output files ([#23684](https://github.com/vitejs/vite/issues/23684)) ([df4e02c](https://github.com/vitejs/vite/commit/df4e02cc8317a62f21edefc79a9690571ffed1f3))
* **bundled-dev:** stop hmr propagation at modules that are no longer imported ([#23839](https://github.com/vitejs/vite/issues/23839)) ([7471e8c](https://github.com/vitejs/vite/commit/7471e8c3b32d3d55243590bb7713e602c9fb0212))
* **css:** don't fail on a literal `%` in `url()` ([#23676](https://github.com/vitejs/vite/issues/23676)) ([50b382d](https://github.com/vitejs/vite/commit/50b382d31835b8b4bc8b6964738ac03146e44261))
* **deps:** update all non-major dependencies ([#23731](https://github.com/vitejs/vite/issues/23731)) ([cf80aa5](https://github.com/vitejs/vite/commit/cf80aa552cac02eac0293330ccd5fde3c7ae8d29))
* **deps:** update all non-major dependencies ([#23826](https://github.com/vitejs/vite/issues/23826)) ([77d8373](https://github.com/vitejs/vite/commit/77d8373510da1b26ce057eb2248e570b7f63fde9))
* **deps:** update rolldown-related dependencies ([#23733](https://github.com/vitejs/vite/issues/23733)) ([43f0d05](https://github.com/vitejs/vite/commit/43f0d052e514c3ad2dea2f7dc44b0720e1f62f48))
* **deps:** update rolldown-related dependencies ([#23827](https://github.com/vitejs/vite/issues/23827)) ([c2e0418](https://github.com/vitejs/vite/commit/c2e04187e49aab7ab809989f0537b4906653acab))
* **optimizer:** fall back to yarn.lock for lockfile hash ([#23667](https://github.com/vitejs/vite/issues/23667)) ([f206096](https://github.com/vitejs/vite/commit/f20609630faa93026924275115d1426fdc08629e))
* **optimizer:** scan `oxc.jsxInject` imports ([#23758](https://github.com/vitejs/vite/issues/23758)) ([38f3cb4](https://github.com/vitejs/vite/commit/38f3cb45b1490ed24775547ceafa677b91a57714))
* **optimizer:** skip patches dir check for yarn.lock fallback ([#23725](https://github.com/vitejs/vite/issues/23725)) ([8e890e1](https://github.com/vitejs/vite/commit/8e890e1ce438bfbc07ea4931ce332e40589940fa))
* **optimizer:** skip patches dir hash for nub lockfile ([#23761](https://github.com/vitejs/vite/issues/23761)) ([a7d5696](https://github.com/vitejs/vite/commit/a7d56967ef0050a09c0507e63a18164bc7a0d486))
* **resolve:** support subpath imports with multiple `#` ([#23631](https://github.com/vitejs/vite/issues/23631)) ([0d86b34](https://github.com/vitejs/vite/commit/0d86b3485fbbd0fcb9a1f70a14adedfcb7a1fff1))
* **resolve:** update resolve.exports to 2.0.4 ([#23739](https://github.com/vite
