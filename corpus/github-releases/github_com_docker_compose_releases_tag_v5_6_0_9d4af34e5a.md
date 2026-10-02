---
title: "docker/compose v5.6.0 released"
url: "https://github.com/docker/compose/releases/tag/v5.6.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "compose"]
date: "2026-10-02T21:53:13Z"
metadata:
  repo: "docker/compose"
  version: "v5.6.0"
---

# docker/compose v5.6.0 released

> Source: github-releases | Category: changelog | 2026-10-02T21:53:13Z

## docker/compose — v5.6.0

## What's Changed

> ℹ️ This release adds **partial support for jobs**: only manually-triggered jobs are supported for now, scheduled jobs are not yet available. Full job support will land once the corresponding Docker Engine support is merged.

### ✨ Improvements

**Jobs**
* Adopt compose-go jobs and container-spec layering by @ndeloof in https://github.com/docker/compose/pull/14093

**Provider services**
* Feat(provider): get-service-config provider request by @ndeloof in https://github.com/docker/compose/pull/14175
* Feat(provider): publish-endpoint deploys a network relay for provider services by @ndeloof in https://github.com/docker/compose/pull/14193
* Get-relay-info tells providers where to bind for the relay by @ndeloof in https://github.com/docker/compose/pull/14258
* Feat(compose): dedicated network for the provider relay link by @ndeloof in https://github.com/docker/compose/pull/14275
* Provider services take part in the image phase, with image distribution on demand by @ndeloof in https://github.com/docker/compose/pull/14252

**Other**
* Feat(compose): warn on unsupported compose-file attributes by @glours in https://github.com/docker/compose/pull/14196
* PRIVATE_PORT optional for `docker compose port` by @maxproske in https://github.com/docker/compose/pull/13577

### 🐛 Fixes
* Fix(build): hand unresolved 'auto' progress mode to bake by @ndeloof in https://github.com/docker/compose/pull/14194
* Fix(watch): coalesce rebuilds triggered during a burst of file changes by @glours in https://github.com/docker/compose/pull/14202
* Fix(port): preserve tie order for dual-stack port publishers by @glours in https://github.com/docker/compose/pull/14213
* Fix(publish): warn when push falls back from OCI 1.1 to OCI 1.0 by @htoyoda18 in https://github.com/docker/compose/pull/14146
* Fix: detect externally stopped and removed containers in up monitor by @glours in https://github.com/docker/compose/pull/13990
* Fix(dry-run): commit no longer creates a real image; the interception set becomes declarative by @ndeloof in https://github.com/docker/compose/pull/14150
* Fix(up): drop benign context.Canceled noise from the final report by @ndeloof in https://github.com/docker/compose/pull/14227
* Fix(relay): reconnect to new networks when routes are unchanged by @ndeloof in https://github.com/docker/compose/pull/14236
* Fix(provider): clean up stale relay and guard start/restart against it by @ndeloof in https://github.com/docker/compose/pull/14238
* Fix(hash): pin the service config-hash byte layout, decoupled from compose-go struct refactorings by @ndeloof in https://github.com/docker/compose/pull/14215
* Fix(hash): repair main after #14093/#14215 merged in reverse order by @ndeloof in https://github.com/docker/compose/pull/14253
* Fix(logs): restart re-attach loses a fast run's output — found by deflaking e2e by @ndeloof in https://github.com/docker/compose/pull/14140
* Fix: provider migration condemns the service's stale replicas by @ndeloof in https://github.com/docker/compose/pull/14264
* Fix/down rmi dangling images by @glours in https://github.com/docker/compose/pull/14266
* Fix/dry run service completed successfully 14269 by @glours in https://github.com/docker/compose/pull/14270
* Fix: honor --parallel across all bulk engine-call fan-outs by @glours in https://github.com/docker/compose/pull/14177
* Fix: adapt to compose-go v2.16.1 promoting x-initialSync silently by @glours in https://github.com/docker/compose/pull/14281

### 🔧  Internal
* Remove jonboulle/clockwork for testing/synctest by @thaJeztah in https://github.com/docker/compose/pull/14185
* Rebuild the TTY progress renderer on a model/layout/screen split by @ndeloof in https://github.com/docker/compose/pull/14051
* Golangci-lint: enable perfsprint linter by @thaJeztah in https://github.com/docker/compose/pull/14207
* Cmd/prompt: remove uses of github.com/AlecAivazis/survey/v2 by @thaJeztah in https://github.com/docker/compose/
