---
title: "docker/compose v5.8.1 released"
url: "https://github.com/docker/compose/releases/tag/v5.8.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "compose"]
date: "2026-11-27T19:31:19Z"
metadata:
  repo: "docker/compose"
  version: "v5.8.1"
---

# docker/compose v5.8.1 released

> Source: github-releases | Category: changelog | 2026-11-27T19:31:19Z

## docker/compose — v5.8.1

## What's Changed

### ✨ Improvements
* Feat(oci): directly load from cache if possible by @gzm0 in https://github.com/docker/compose/pull/14466

### 🐛 Fixes
* Fix(up): wait for every replica in --wait and service_completed_successfully by @Zoomish in https://github.com/docker/compose/pull/14523
* Fix(watch): delete a large batch of synced paths in several execs by @htoyoda18 in https://github.com/docker/compose/pull/14528
* Fix(hooks): stop or restart a container whose pre_stop hook cannot run by @htoyoda18 in https://github.com/docker/compose/pull/14547
* Cli: one project-resolution story — single name precedence, no swallowed load error, strict service validation by @ndeloof in https://github.com/docker/compose/pull/14151
* Fix(executor): run pre_stop hooks before the plan stops a container by @htoyoda18 in https://github.com/docker/compose/pull/14477
* Fix(models): don't pull again a model written in short form by @ndeloof in https://github.com/docker/compose/pull/14532
* Fix(jobs): treat an engine endpoint without HTTP/2 as jobs unsupported by @glours in https://github.com/docker/compose/pull/14559
* Fix(plan): run the pre_stop hooks before every stop the plan makes by @ndeloof in https://github.com/docker/compose/pull/14555

### 🔧  Internal
* E2e: forward Docker TLS environment variables to the tests by @ricardobranco777 in https://github.com/docker/compose/pull/14524
* Ci: run the e2e suite nightly against the head of Moby and Buildx by @ndeloof in https://github.com/docker/compose/pull/14548
* Ci: use the official zizmor action by @thaJeztah in https://github.com/docker/compose/pull/14556
* Refactor: give each component only the engine families it uses by @ndeloof in https://github.com/docker/compose/pull/14534
* Feat(api): Validate for the options of Logs, Events, Publish and Down by @ndeloof in https://github.com/docker/compose/pull/14515

### ⚙️ Dependencies
* Build(deps): bump peter-evans/create-pull-request from 8.1.2 to 8.1.3 by @dependabot[bot] in https://github.com/docker/compose/pull/14530
* Chore(deps): bump secrets-engine/client to v1.0.0 and drop secrets-engine/x by @Benehiko in https://github.com/docker/compose/pull/14541
* Build(deps): bump actions/setup-go from 7.0.0 to 7.1.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14543
* Build(deps): bump tags.cncf.io/container-device-interface from 1.1.1 to 1.1.2 by @dependabot[bot] in https://github.com/docker/compose/pull/14537
* Build(deps): bump github.com/klauspost/compress from 1.20.0 to 1.20.5 by @glours in https://github.com/docker/compose/pull/14549
* Build(deps): bump actions/setup-go from 7.0.0 to 7.1.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14554
* Build(deps): bump github.com/docker/cli from 29.10.0+incompatible to 29.10.1+incompatible by @dependabot[bot] in https://github.com/docker/compose/pull/14553
* Build(deps): bump github.com/mattn/go-shellwords from 1.0.16 to 1.0.17 by @dependabot[bot] in https://github.com/docker/compose/pull/14552

## New Contributors
* @Zoomish made their first contribution in https://github.com/docker/compose/pull/14523
* @gzm0 made their first contribution in https://github.com/docker/compose/pull/14466

**Full Changelog**: https://github.com/docker/compose/compare/v5.8.0...v5.8.1

