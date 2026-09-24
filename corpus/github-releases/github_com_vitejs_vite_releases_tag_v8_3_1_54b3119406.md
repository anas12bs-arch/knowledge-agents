---
title: "vitejs/vite v8.3.1 released"
url: "https://github.com/vitejs/vite/releases/tag/v8.3.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "vite"]
date: "2026-09-24T15:17:40Z"
metadata:
  repo: "vitejs/vite"
  version: "v8.3.1"
---

# vitejs/vite v8.3.1 released

> Source: github-releases | Category: changelog | 2026-09-24T15:17:40Z

## vitejs/vite — v8.3.1

### Bug Fixes

* **deps:** update all non-major dependencies ([#23482](https://github.com/vitejs/vite/issues/23482)) ([3c752c8](https://github.com/vitejs/vite/commit/3c752c8932bc0599465ba4a6d8f44aaf1e934c3d))
* **deps:** update all non-major dependencies ([#23537](https://github.com/vitejs/vite/issues/23537)) ([e8990c4](https://github.com/vitejs/vite/commit/e8990c4d6101dfaca2654ed8ab4d0574ee920248))
* **deps:** update rolldown-related dependencies ([#23483](https://github.com/vitejs/vite/issues/23483)) ([9aecbbf](https://github.com/vitejs/vite/commit/9aecbbfa5fb5da4b9981c099cb9746a9fd210806))
* handle `server.ws: false` in mergeConfig ([#23511](https://github.com/vitejs/vite/issues/23511)) ([f68c0d5](https://github.com/vitejs/vite/commit/f68c0d5a28c96555431413e3e2cbe644337b087f))
* merge `build.rolldownOptions.output.comments` correctly ([#23514](https://github.com/vitejs/vite/issues/23514)) ([4aba8d8](https://github.com/vitejs/vite/commit/4aba8d8720e82e4c5b694a4b7877755a3f84fc57))
* **optimizer:** don't skip imports whose binding starts with type ([#23540](https://github.com/vitejs/vite/issues/23540)) ([39330f4](https://github.com/vitejs/vite/commit/39330f489a0ae08923557f0ce10a307d6662a3f5))
* **optimizer:** resolve pending discovered dep processing on close before init ([#23567](https://github.com/vitejs/vite/issues/23567)) ([5f89433](https://github.com/vitejs/vite/commit/5f894339d27882fedc86bf6b1076fa6d92e404f3))
* **server:** avoid reinitializing watcher when adding file after server close ([#23572](https://github.com/vitejs/vite/issues/23572)) ([6f831f9](https://github.com/vitejs/vite/commit/6f831f9b58ebda77638b514042ad8d160edfb928))
* **sourcemap:** skip URL source roots when injecting sources content ([#23519](https://github.com/vitejs/vite/issues/23519)) ([04fc30a](https://github.com/vitejs/vite/commit/04fc30a4b91870e65a436b3420620a2e02a94a41))

### Miscellaneous Chores

* merge prereleases in changelog ([#23466](https://github.com/vitejs/vite/issues/23466)) ([99bd9d1](https://github.com/vitejs/vite/commit/99bd9d1d46153fa939f4a304cc0177db42e28776))
* **optimizer:** add debug log when waiting for dep before init ([#23566](https://github.com/vitejs/vite/issues/23566)) ([63567c7](https://github.com/vitejs/vite/commit/63567c73ac132e6384fef384e6b9f7e8d5a37fff))
* update `optimizeDeps.include` comment ([#23489](https://github.com/vitejs/vite/issues/23489)) ([6a84c72](https://github.com/vitejs/vite/commit/6a84c72100da4e4be4badb2d9a0026279b4df136))

### Code Refactoring

* assets regexp use non-capture ([#23491](https://github.com/vitejs/vite/issues/23491)) ([f4b4431](https://github.com/vitejs/vite/commit/f4b4431a2f9097fd9bbb7aaebbf1b63c4b54dea1))
* remove duplicate configurations ([#23532](https://github.com/vitejs/vite/issues/23532)) ([9abd99b](https://github.com/vitejs/vite/commit/9abd99bfdd3117149d6faf87fc37bc9899b1c998))
* replace `find` with `some` ([#23554](https://github.com/vitejs/vite/issues/23554)) ([af7cdf6](https://github.com/vitejs/vite/commit/af7cdf6964f124f58d66037e808fe687654948e2))

