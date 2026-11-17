---
title: "docker/compose v5.7.2 released"
url: "https://github.com/docker/compose/releases/tag/v5.7.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "compose"]
date: "2026-11-17T17:58:11Z"
metadata:
  repo: "docker/compose"
  version: "v5.7.2"
---

# docker/compose v5.7.2 released

> Source: github-releases | Category: changelog | 2026-11-17T17:58:11Z

## docker/compose — v5.7.2

## What's Changed

### ✨ Improvements
* Feat(up): stream the logs while `--wait` waits for the services by @glours in https://github.com/docker/compose/pull/14454

### 🐛 Fixes
* Fix(oci): tell a null "manifests" from a list, and report a host failure as such by @ndeloof in https://github.com/docker/compose/pull/14491
* Fix(config): skip pure resource provider services in `config --images` by @TDnorthgarden in https://github.com/docker/compose/pull/14332
* Fix(down): keep volumes other services use on `down -v` with services by @htoyoda18 in https://github.com/docker/compose/pull/14449
* Fix(scale): reject empty service name in `--scale` flag by @arsalanyavari in https://github.com/docker/compose/pull/14481
* Fix: surface a provider-backed service's scale over its control channel by @ndeloof in https://github.com/docker/compose/pull/14298
* Fix(dry-run): skip lifecycle hooks instead of failing on exec attach by @glours in https://github.com/docker/compose/pull/14504
* Fix(progress): stop inverting success in `EventProcessor.Done` by @glours in https://github.com/docker/compose/pull/14503
* Fix: `COMPOSE_REMOVE_ORPHANS` resolves identically for every command carrying the flag by @ndeloof in https://github.com/docker/compose/pull/14139
* Fix(up): recreate a stopped container whose network was removed by @ndeloof in https://github.com/docker/compose/pull/14519
* Fix(pre_start): name the hook when its container cannot start by @ndeloof in https://github.com/docker/compose/pull/14520

### 🔧  Internal
* Chore: address the review notes left by @htoyoda18 in https://github.com/docker/compose/pull/14469
* Fix(relay): build the relay image like the compose binary by @ndeloof in https://github.com/docker/compose/pull/14497
* Refactor(compose): move publish and transform to `internal/publish` by @ndeloof in https://github.com/docker/compose/pull/14409
* Refactor(compose): move the plan types to `internal/planning` by @ndeloof in https://github.com/docker/compose/pull/14408
* Refactor(compose): move the image build to `internal/build` by @ndeloof in https://github.com/docker/compose/pull/14411
* Refactor(compose): move the `develop.watch` loop to `internal/devwatch` by @ndeloof in https://github.com/docker/compose/pull/14412
* Refactor(e2e): move the e2e framework and tests out of `pkg/` to `internal/e2e` by @ndeloof in https://github.com/docker/compose/pull/14404
* Docs(agents): add an architecture map of the non-guessable facts by @ndeloof in https://github.com/docker/compose/pull/14134
* Refactor(publish): pin the backend wiring, share the digest resolver by @glours in https://github.com/docker/compose/pull/14501
* Api: document the zero values, validate the `recreate` policy, type the not-running error by @ndeloof in https://github.com/docker/compose/pull/14417

### ⚙️ Dependencies
* Build(deps): bump github/codeql-action/upload-sarif from 4.39.1 to 4.39.3 by @dependabot[bot] in https://github.com/docker/compose/pull/14492
* Build(deps): bump github.com/spf13/pflag from 1.0.10 to 1.1.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14470
* Build(deps): bump softprops/action-gh-release from 3.0.3 to 3.0.4 by @dependabot[bot] in https://github.com/docker/compose/pull/14495
* Build(deps): bump the docker-actions group with 2 updates by @dependabot[bot] in https://github.com/docker/compose/pull/14494
* Build(deps): bump golang.org/x/sync from 0.24.0 to 0.25.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14484
* Revert "build(deps): bump github.com/spf13/pflag from 1.0.10 to 1.1.0" by @ndeloof in https://github.com/docker/compose/pull/14496
* Build(deps): bump peter-evans/create-pull-request from 8.1.1 to 8.1.2 by @dependabot[bot] in https://github.com/docker/compose/pull/14500
* Chore(deps): github.com/DefangLabs/secret-detector v1.1.0 by @thaJeztah in https://github.com/docker/compose/pull/14512
* Build(deps): bump github.com/moby/moby/client from 0.6.2 to 0.6.3 by @depe
