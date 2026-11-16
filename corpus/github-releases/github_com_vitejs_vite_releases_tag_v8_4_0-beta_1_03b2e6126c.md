---
title: "vitejs/vite v8.4.0-beta.1 released"
url: "https://github.com/vitejs/vite/releases/tag/v8.4.0-beta.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "vite"]
date: "2026-11-16T07:53:04Z"
metadata:
  repo: "vitejs/vite"
  version: "v8.4.0-beta.1"
---

# vitejs/vite v8.4.0-beta.1 released

> Source: github-releases | Category: changelog | 2026-11-16T07:53:04Z

## vitejs/vite — v8.4.0-beta.1

### Features

* add `environment.addSafeModule` ([#23974](https://github.com/vitejs/vite/issues/23974)) ([e0fe98a](https://github.com/vitejs/vite/commit/e0fe98a050db0fcfa04c24a09b7d8f72dbbf68e1))
* add `server.fs.strict: 'extended'` ([#23972](https://github.com/vitejs/vite/issues/23972)) ([e4babd7](https://github.com/vitejs/vite/commit/e4babd7262256a3c5c383109eb7f7d489760faf5))
* **build:** include worker chunks in manifest ([#23699](https://github.com/vitejs/vite/issues/23699)) ([bc6e03c](https://github.com/vitejs/vite/commit/bc6e03c1d7eb5c2a7e202cd25d9ca1512cd06f6f))
* **build:** support retrying failed CSS preloads ([#23710](https://github.com/vitejs/vite/issues/23710)) ([2155e12](https://github.com/vitejs/vite/commit/2155e125cac5792785a485759ecc0e8af18f0438))
* **cli:** omit `-0` suffix from the first profile file name ([#23490](https://github.com/vitejs/vite/issues/23490)) ([c64ba40](https://github.com/vitejs/vite/commit/c64ba40bc5951eebc266aea4609277e566db3c3c))
* **css:** skip emitting empty CSS files ([#24059](https://github.com/vitejs/vite/issues/24059)) ([c5be55f](https://github.com/vitejs/vite/commit/c5be55f571e418992fd39f34267ec4929e79d014))
* **css:** support subpath imports in CSS `url()` ([#23869](https://github.com/vitejs/vite/issues/23869)) ([c110663](https://github.com/vitejs/vite/commit/c110663facf21a8cee199d1c668908e919d6218e))
* **environment:** expose build manifest on build environment ([#23292](https://github.com/vitejs/vite/issues/23292)) ([4db9844](https://github.com/vitejs/vite/commit/4db98449a802abd67a6975fb4fdf260fa8f82979))
* migrate to `dev.sourcemap.css` from `css.devSourcemap` ([#23765](https://github.com/vitejs/vite/issues/23765)) ([76cb51b](https://github.com/vitejs/vite/commit/76cb51bba1a8988b00a5becae5829c3e7a49d9ab))
* **module-runner:** align stacktrace with v8 ([#23690](https://github.com/vitejs/vite/issues/23690)) ([bd32fea](https://github.com/vitejs/vite/commit/bd32fea2cb171cf993c70b4dd12097d5166b3b28))
* **preview:** serve wasm compressed ([#24051](https://github.com/vitejs/vite/issues/24051)) ([39d63b8](https://github.com/vitejs/vite/commit/39d63b8479c6314caab9b78a05d3aaaf36a86b2c))
* register more references to safe modules ([#23168](https://github.com/vitejs/vite/issues/23168)) ([e258ce1](https://github.com/vitejs/vite/commit/e258ce140eef64cf89ff38c410125abd8726f274))
* register references in HTML to safe modules ([#23169](https://github.com/vitejs/vite/issues/23169)) ([ef30399](https://github.com/vitejs/vite/commit/ef30399e751740b8ad28f0a7523b3fb42c7cc539))
* separate `safeModulePaths` per environment ([#23973](https://github.com/vitejs/vite/issues/23973)) ([7480c54](https://github.com/vitejs/vite/commit/7480c547947d0b1dc519815d8f6f670964b15026))
* show running process for the same project ([#23624](https://github.com/vitejs/vite/issues/23624)) ([3e1a86e](https://github.com/vitejs/vite/commit/3e1a86e6c87a3c18356252c5d69bf9604cb85950))
* stabilize `--configLoader` and deprecate `--configLoader=runner` ([#23714](https://github.com/vitejs/vite/issues/23714)) ([e719122](https://github.com/vitejs/vite/commit/e719122cf6758086c1c228c14ad016358337cf09))
* support bundled dev mode in ssr ([#21626](https://github.com/vitejs/vite/issues/21626)) ([5ff255e](https://github.com/vitejs/vite/commit/5ff255e5b9f1460dd844ccf7a82d6f59f8899033))
* **wasm:** support source phase imports ([#22675](https://github.com/vitejs/vite/issues/22675)) ([97bb00f](https://github.com/vitejs/vite/commit/97bb00f8f55e18caa5621c1a23dd057f1ca836e8))

### Bug Fixes

* **build:** keep `magicString` and `ast` in transform hook meta ([#24067](https://github.com/vitejs/vite/issues/24067)) ([c0d590d](https://github.com/vitejs/vite/commit/c0d590d697bb21530f687ea094a36c943620232c))
* **bundled-dev:** load lazy chunks under `base` ([#23798](https://github.com/vitejs/vite/issues/23798)) ([d5c79c7](https://github.com/vitejs/vite/commit/d5c79c7a7c7a3794491f67fbb344d08d7ff814ab))
* **client:** fallback to waiting on main thread for s
