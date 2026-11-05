---
title: "vitejs/vite v8.3.6 released"
url: "https://github.com/vitejs/vite/releases/tag/v8.3.6"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "vite"]
date: "2026-11-05T09:56:35Z"
metadata:
  repo: "vitejs/vite"
  version: "v8.3.6"
---

# vitejs/vite v8.3.6 released

> Source: github-releases | Category: changelog | 2026-11-05T09:56:35Z

## vitejs/vite — v8.3.6

### Bug Fixes

* await overlapping plugin container close calls ([#23935](https://github.com/vitejs/vite/issues/23935)) ([175bbeb](https://github.com/vitejs/vite/commit/175bbeb231fe8bbf260b0b3866b30080690c4f5e))
* **build:** resolve dynamic imports with queries appended when collecting CSS dependencies ([#23909](https://github.com/vitejs/vite/issues/23909)) ([df36558](https://github.com/vitejs/vite/commit/df365589738866363fff7335ed58948a5c440580))
* **build:** use stable module ids in chunk import map hash signatures (fix [#23975](https://github.com/vitejs/vite/issues/23975)) ([#23976](https://github.com/vitejs/vite/issues/23976)) ([8069835](https://github.com/vitejs/vite/commit/8069835ac32ae7682b34de55fdba6c5d2484bae0))
* **bundled-dev:** allow named imports from Node built-ins ([#23858](https://github.com/vitejs/vite/issues/23858)) ([4260c75](https://github.com/vitejs/vite/commit/4260c756944a430e897f689efcfa4f8648953488))
* **bundled-dev:** reload when hmr cannot run an entry again ([#23849](https://github.com/vitejs/vite/issues/23849)) ([a236886](https://github.com/vitejs/vite/commit/a236886026c3a5de0680ea616de7de830d7a90e7))
* **deps:** update `@rollup/plugin-alias` to v6.0.1 ([#23862](https://github.com/vitejs/vite/issues/23862)) ([67c965b](https://github.com/vitejs/vite/commit/67c965b1df64249bceb747037e87d22f75b3e471))
* **deps:** update all non-major dependencies ([#23896](https://github.com/vitejs/vite/issues/23896)) ([46b91c5](https://github.com/vitejs/vite/commit/46b91c5bf9c2901b8511c893bc3fc38b8bba6e4f))
* **deps:** update all non-major dependencies ([#23966](https://github.com/vitejs/vite/issues/23966)) ([b3cb057](https://github.com/vitejs/vite/commit/b3cb0575aff63004a71301a1ec798aeea2aa05d7))
* **deps:** update rolldown-related dependencies ([#23868](https://github.com/vitejs/vite/issues/23868)) ([a63eb87](https://github.com/vitejs/vite/commit/a63eb8722e7d47d1efb710b6410c8d5e5a04a18f))
* **deps:** update rolldown-related dependencies ([#23967](https://github.com/vitejs/vite/issues/23967)) ([0105733](https://github.com/vitejs/vite/commit/0105733e610dd5b770bb5397e8d9fbc54a9f6312))
* **dev:** escape ANSI escape sequence for `server.forwardConsole` ([#23933](https://github.com/vitejs/vite/issues/23933)) ([4f340fd](https://github.com/vitejs/vite/commit/4f340fdb1b619089bbf8ae5dc56c2c0866224306))
* **html:** remove adjacent module tags on the first line ([#23823](https://github.com/vitejs/vite/issues/23823)) ([eab1dc2](https://github.com/vitejs/vite/commit/eab1dc2752fcccf7f06427afc9915794e256e3bc))
* ignore pnpm's .modules.yaml as a Vite Task input ([#23634](https://github.com/vitejs/vite/issues/23634)) ([95c2daf](https://github.com/vitejs/vite/commit/95c2daf1352b3509ec93e6e08a0eaabe23a61b28))
* **optimizer:** detect cache dir precisely ([#23912](https://github.com/vitejs/vite/issues/23912)) ([cc9bc21](https://github.com/vitejs/vite/commit/cc9bc2131d471bb4d60364614b326ada3ca7d10d))
* **optimizer:** resolve subpath imports (#) with Vite's resolver ([#23959](https://github.com/vitejs/vite/issues/23959)) ([0fdd81e](https://github.com/vitejs/vite/commit/0fdd81e9460dd44806b2b6290603ee2c8366a54e))
* respect `build.sourcemap` from environment ([#23879](https://github.com/vitejs/vite/issues/23879)) ([82e7aa0](https://github.com/vitejs/vite/commit/82e7aa0374a15e1c67594557ab5893c91578f897))
* **server:** escape HTML attributes ([#23995](https://github.com/vitejs/vite/issues/23995)) ([a270391](https://github.com/vitejs/vite/commit/a27039101e3726498063c9662da9c0c097016bd1))
* **server:** preserve `$` patterns in static alias replacements ([#23703](https://github.com/vitejs/vite/issues/23703)) ([1b6ed05](https://github.com/vitejs/vite/commit/1b6ed05397c0670e6114e3e1380188f0313ae590))
* **ssr:** convert external require against built-in modules to import for `ssr.target=webworker` ([#23759](https://github.com/vitejs/vite/issues/23759)) ([a711f1c](https://github.com/vitejs/vite/commit/a711f1c6328ca7f59857ed99e32853c
