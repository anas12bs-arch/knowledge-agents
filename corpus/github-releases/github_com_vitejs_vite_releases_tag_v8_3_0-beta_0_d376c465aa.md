---
title: "vitejs/vite v8.3.0-beta.0 released"
url: "https://github.com/vitejs/vite/releases/tag/v8.3.0-beta.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "vite"]
date: "2026-09-02T09:58:23Z"
metadata:
  repo: "vitejs/vite"
  version: "v8.3.0-beta.0"
---

# vitejs/vite v8.3.0-beta.0 released

> Source: github-releases | Category: changelog | 2026-09-02T09:58:23Z

## vitejs/vite — v8.3.0-beta.0

### Features

* accept Rolldown watch options in `server.watch` ([#23133](https://github.com/vitejs/vite/issues/23133)) ([1b5cfe3](https://github.com/vitejs/vite/commit/1b5cfe3d3777d4ceb7f35fcee9d3c4279316a084))
* add closeServer and closePreviewServer hooks ([#23110](https://github.com/vitejs/vite/issues/23110)) ([e17d2d5](https://github.com/vitejs/vite/commit/e17d2d565b0288f169c7995adb2b192f917548e7))
* add top-level `tsconfig` option ([#23310](https://github.com/vitejs/vite/issues/23310)) ([93164c3](https://github.com/vitejs/vite/commit/93164c3530a7b4fc7bbedfb986d6afa9546cdef3))
* add warning for unsupported hooks in plugin returned from `applyToEnvironment` hook ([#23191](https://github.com/vitejs/vite/issues/23191)) ([fdef04f](https://github.com/vitejs/vite/commit/fdef04f112aadfea40ad3c448d96a49a04c168bd))
* **cli:** support naming the CPU profile via --profile [name] ([#23042](https://github.com/vitejs/vite/issues/23042)) ([a500dee](https://github.com/vitejs/vite/commit/a500deeb6f52d93ca501a0fc612a5392b939f2f5))
* **config:** warn on named imports from JSON modules ([#23378](https://github.com/vitejs/vite/issues/23378)) ([472385e](https://github.com/vitejs/vite/commit/472385e6ec4b21e3167c7abf9769883d1c9675f8))
* **css:** minify style tag ([#23183](https://github.com/vitejs/vite/issues/23183)) ([8156684](https://github.com/vitejs/vite/commit/8156684572bdcf73e9d8568ed67971f0467fab60))
* searched params attached to workers are now preserved ([#22280](https://github.com/vitejs/vite/issues/22280)) ([517b97f](https://github.com/vitejs/vite/commit/517b97f57ab9473e7417da856eb641d76870a56e))
* support subpath imports in dynamic import statements ([#23185](https://github.com/vitejs/vite/issues/23185)) ([b78e2f1](https://github.com/vitejs/vite/commit/b78e2f1bc1cba404c4bd9faf518d26ec85e89fc7))
* use `import.meta.ROLLDOWN_FILE_URL_*` for assets in JS ([#22888](https://github.com/vitejs/vite/issues/22888)) ([4366ac4](https://github.com/vitejs/vite/commit/4366ac468343252df6d5706361a6348afa66f9cc))
* use `import.meta.ROLLDOWN_FILE_URL_*` for other plugins ([#22894](https://github.com/vitejs/vite/issues/22894)) ([e38f29e](https://github.com/vitejs/vite/commit/e38f29ee48bea5ea3178faec5b78708e86f38afb))
* **worker:** remove worker chunk if it's detected that it's not referenced ([#22473](https://github.com/vitejs/vite/issues/22473)) ([924997a](https://github.com/vitejs/vite/commit/924997a4bdda9115faee9bdb622fcec4fc8357f0))

### Bug Fixes

* **config:** close bundles when generation fails ([#23256](https://github.com/vitejs/vite/issues/23256)) ([6bacc95](https://github.com/vitejs/vite/commit/6bacc956df5a76cc5653b9de4493453b953439fd))
* **css:** keep newline-separated srcset candidates intact ([#23265](https://github.com/vitejs/vite/issues/23265)) ([4f9d2f4](https://github.com/vitejs/vite/commit/4f9d2f4dadc83191200de7d2154c957a711e8c3d))
* **deps:** update all non-major dependencies ([#23337](https://github.com/vitejs/vite/issues/23337)) ([d550815](https://github.com/vitejs/vite/commit/d55081581ddd4d55667fef38e85d02ab7f879f15))
* **deps:** update all non-major dependencies ([#23404](https://github.com/vitejs/vite/issues/23404)) ([238ad81](https://github.com/vitejs/vite/commit/238ad811c7fb9e4730cbd317d0657867ed3447b3))
* **deps:** update rolldown-related dependencies ([#23338](https://github.com/vitejs/vite/issues/23338)) ([76e8082](https://github.com/vitejs/vite/commit/76e8082c56a2872dc8017c5672bc36cba8dcf75d))
* **deps:** update rolldown-related dependencies ([#23405](https://github.com/vitejs/vite/issues/23405)) ([b882566](https://github.com/vitejs/vite/commit/b88256607e3a051b7bcb0b338b3c4665926b55a8))
* **dev:** run closeBundle after buildEnd failure ([#23165](https://github.com/vitejs/vite/issues/23165)) ([8cb872e](https://github.com/vitejs/vite/commit/8cb872e7fb65b03f6068923c6aa7fcf3e71baf21))
* **hmr:** handle `import.meta.hot.invalidate` in virtual module ([#23171](https://github.com/vitejs/vite/issues/23171)) ([6162968](https://githu
