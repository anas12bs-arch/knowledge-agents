---
title: "docker/compose v5.4.0 released"
url: "https://github.com/docker/compose/releases/tag/v5.4.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "compose"]
date: "2026-08-03T16:15:40Z"
metadata:
  repo: "docker/compose"
  version: "v5.4.0"
---

# docker/compose v5.4.0 released

> Source: github-releases | Category: changelog | 2026-08-03T16:15:40Z

## docker/compose — v5.4.0

## What's Changed

> ℹ️ This release introduces a new way to reconcile resources such as volumes and networks

### ✨ Improvements
* Feat(reconcile): model volume recreation in the plan by @ndeloof in https://github.com/docker/compose/pull/13962
* Feat(reconcile): model network lifecycle in the plan by @ndeloof in https://github.com/docker/compose/pull/13966

### 🐛 Fixes
* Fix(reconcile): preserve zero-replica services during hashing by @junhaoliao in https://github.com/docker/compose/pull/13931
* Fix(config): warn when service selection is silently ignored by @glours in https://github.com/docker/compose/pull/13950
* Fix(build): use platform image-manifest digest, not attested index by @glours in https://github.com/docker/compose/pull/13949
* Fix(oci): honor --insecure-registry when `up` re-loads the model by @ptrdom in https://github.com/docker/compose/pull/13894
* Fix(config): pin type:image volume sources and pre_start hook images by @glours in https://github.com/docker/compose/pull/13956
* Tolerate missing env file on more runtime commands by @maxproske in https://github.com/docker/compose/pull/13603
* Resolve `pre_start` hook images alongside service images by @ndeloof in https://github.com/docker/compose/pull/13937
* Fix(cp): return non-nil Content from dry-run CopyFromContainer by @glours in https://github.com/docker/compose/pull/13982
* Fix(config): apply config flags to `--services`/`--volumes`/`--networks`/`--models`/`--hash` by @glours in https://github.com/docker/compose/pull/13979
* Fix: tolerate missing env file on scale, watch and shell completion by @glours in https://github.com/docker/compose/pull/13973

### 🔧  Internal
* README: remove Go Report Card badge by @thaJeztah in https://github.com/docker/compose/pull/13926
* Docs: adopt `AGENTS.md` standard, symlink `CLAUDE.md` to it by @glours in https://github.com/docker/compose/pull/13871
* Dockerfile: update golang image to alpine `3.23` by @thaJeztah in https://github.com/docker/compose/pull/13921
* Docs: require dated `AI_AGENT_DISCLOSURE.md`, drop committed copy by @glours in https://github.com/docker/compose/pull/13976
* CI: publish images to Docker Hub using OIDC by @glours in https://github.com/docker/compose/pull/13994

### ⚙️ Dependencies
* Build(deps): bump github/codeql-action/upload-sarif from `4.36.2` to `4.37.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13942
* Build(deps): bump the docker-actions group across 1 directory with 4 updates by @dependabot[bot] in https://github.com/docker/compose/pull/13941
* Build(deps): bump actions/stale from `10.3.0` to `10.4.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13943
* Build(deps): bump github.com/mattn/go-shellwords from `1.0.13` to `1.0.14` by @dependabot[bot] in https://github.com/docker/compose/pull/13948
* Build(deps): bump golang.org/x/sync from `0.21.0` to `0.22.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13927
* Build(deps): bump golang.org/x/sys from `0.46.0` to `0.47.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13928
* Build(deps): bump docker/github-builder/.github/workflows/bake.yml from `1.13.0` to `1.14.0` in the docker-actions group by @dependabot[bot] in https://github.com/docker/compose/pull/13953
* Build(deps): bump google.golang.org/grpc from `1.81.1` to `1.82.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13922
* Build(deps): bump softprops/action-gh-release from `3.0.1` to `3.0.2` by @dependabot[bot] in https://github.com/docker/compose/pull/13955
* Build(deps): bump actions/setup-go from `6.5.0` to `7.0.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13960
* Build(deps): bump google.golang.org/grpc from `1.82.0` to `1.82.1` in the go_modules group across 1 directory by @dependabot[bot] in https://github.com/docker/compose/pull/13961
* Build(deps): bump github.com/docker/cli from `29.6.1+incompatible` to `29.6.2+incompatible` by @depe
