---
title: "vitejs/vite v8.3.8 released"
url: "https://github.com/vitejs/vite/releases/tag/v8.3.8"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "vite"]
date: "2026-11-11T09:19:14Z"
metadata:
  repo: "vitejs/vite"
  version: "v8.3.8"
---

# vitejs/vite v8.3.8 released

> Source: github-releases | Category: changelog | 2026-11-11T09:19:14Z

## vitejs/vite — v8.3.8

### Bug Fixes

* **build:** keep `magicString` and `ast` in transform hook meta ([#24012](https://github.com/vitejs/vite/issues/24012)) ([a3b28e8](https://github.com/vitejs/vite/commit/a3b28e8744ffae9abd018696ad4fc01b27ac71ce))
* **bundled-dev:** emit assets referenced by inline workers during load ([#23103](https://github.com/vitejs/vite/issues/23103)) ([5e50bae](https://github.com/vitejs/vite/commit/5e50bae4bdfa123c25c4f5afcbb27efd96fcf681))
* **config:** skip native loader compat checks for type-only imports ([#24021](https://github.com/vitejs/vite/issues/24021)) ([e554294](https://github.com/vitejs/vite/commit/e5542942715b281ca5803554c43d48448d72d7f2))
* **css:** reject CSS entrypoints when `build.cssCodeSplit: false` ([#23112](https://github.com/vitejs/vite/issues/23112)) ([e4ad62b](https://github.com/vitejs/vite/commit/e4ad62ba6523e889f988b6e882d9d81be7f26711))
* **deps:** update all non-major dependencies ([#24027](https://github.com/vitejs/vite/issues/24027)) ([a13aa04](https://github.com/vitejs/vite/commit/a13aa045d1cf2a28e9a5dd2bcb008236f4eaf19a))
* hide console window when running `yarn config get` on Windows ([#24013](https://github.com/vitejs/vite/issues/24013)) ([3f6c4cd](https://github.com/vitejs/vite/commit/3f6c4cdae3b7984840cc32ff6752a45736025406))

### Performance Improvements

* **css:** import sass once instead of per file ([#24041](https://github.com/vitejs/vite/issues/24041)) ([db8b119](https://github.com/vitejs/vite/commit/db8b1190abbb7e30aad0055f97dde02d7ed504c7))
* defer `net use` until a UNC path is resolved on Windows ([#24014](https://github.com/vitejs/vite/issues/24014)) ([b643046](https://github.com/vitejs/vite/commit/b6430466c57f4783b707fd14a43c237082094081))

### Miscellaneous Chores

* **deps:** update dependency @types/node to v26 ([#24029](https://github.com/vitejs/vite/issues/24029)) ([dd780cd](https://github.com/vitejs/vite/commit/dd780cd761221a0c5fa4810335f0190ecb9c7294))
* enable vitest plugin in Oxlint ([#24052](https://github.com/vitejs/vite/issues/24052)) ([ce979e4](https://github.com/vitejs/vite/commit/ce979e4c4be5f48c5862445ef124d863853e39b1))
* enable vitest style rules in Oxlint ([#24053](https://github.com/vitejs/vite/issues/24053)) ([b8c8270](https://github.com/vitejs/vite/commit/b8c8270f3f01a9dbf02c336e7468bf6f1df0f5ad))
* revert "fix(build): keep `magicString` and `ast` in transform hook meta ([#24012](https://github.com/vitejs/vite/issues/24012))" ([#24065](https://github.com/vitejs/vite/issues/24065)) ([afc44f0](https://github.com/vitejs/vite/commit/afc44f0957f7ef52d27d5026200a289de374c215))

### Code Refactoring

* **optimizer:** use non-capturing group for external types regex ([#24048](https://github.com/vitejs/vite/issues/24048)) ([ef23433](https://github.com/vitejs/vite/commit/ef2343355b29a3f389e4af51147b767331bd7a5b))

### Tests

* avoid joining logs for assertion ([#24057](https://github.com/vitejs/vite/issues/24057)) ([fbb0a4e](https://github.com/vitejs/vite/commit/fbb0a4e719fda240459aa54f872a89dc52473fe2))

