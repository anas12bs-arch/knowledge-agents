---
title: "docker/compose v5.7.0 released"
url: "https://github.com/docker/compose/releases/tag/v5.7.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "compose"]
date: "2026-11-02T20:03:46Z"
metadata:
  repo: "docker/compose"
  version: "v5.7.0"
---

# docker/compose v5.7.0 released

> Source: github-releases | Category: changelog | 2026-11-02T20:03:46Z

## docker/compose — v5.7.0

## What's Changed

> ℹ️ **Heads-up for users of Compose as a library:** `Up` now runs its Create and Start phases as **a single plan over a single daemon snapshot**, for `up -d` ([#14290](https://github.com/docker/compose/pull/14290)) and interactive `up` ([#14305](https://github.com/docker/compose/pull/14305)), as `scale`, watch rebuilds and `start` already do ([#14291](https://github.com/docker/compose/pull/14291), [#14296](https://github.com/docker/compose/pull/14296)). The CLI behaves as before. If you call `api.Compose.Up` from your own program:
>
> * `Up` now validates its options first, with the same rules as the CLI flags: `UpOptions.Validate()` returns an `*api.IncompatibleOptionsError` (`errors.Is(err, api.ErrIncompatibleOptions)`) for `Start.Wait` combined with `Start.Attach`, and for a detached `Up` (no `Start.Attach`) combined with `OnExit`, `ExitCodeFrom` or `Watch`. Those combinations used to be silently ignored ([#14306](https://github.com/docker/compose/pull/14306)).
> * `Up` works on the project it is given and ignores `StartOptions.Project`.
> * The daemon is not observed again between the two phases: a container that exits after the plan is built is not started again, and one removed in between makes its start fail instead of being skipped. A planning error of the Start phase now fails before any container is created.
> * A foreground `Up` now gives a `use_api_socket` service its `/run/secrets/docker/config.json`, as `up -d` does, and shows the output of `pre_start` hooks.
> * The keyboard menu of an interactive `up` is no longer built by the library: set `NavigationMenu: true` **and** pass an implementation with `compose.WithNavigationMenu(...)`, otherwise no menu is displayed and a warning says so ([#14324](https://github.com/docker/compose/pull/14324)).
>
> Other changes to the library surface in this release: `DownOptions.Images` is now an `api.ImagePruneMode` (untyped constants still compile, a `string` variable needs a conversion) and an invalid value is rejected before `Down` removes anything ([#14149](https://github.com/docker/compose/pull/14149)); `compose.ServiceHash`, `compose.NetworkHash` and `compose.VolumeHash` are no longer exported, the helpers having moved to an internal package ([#14405](https://github.com/docker/compose/pull/14405)); `api.Compose` is now assembled from six smaller interfaces, with the same method set ([#14322](https://github.com/docker/compose/pull/14322)); `PushOptions.IgnoreMissing` is added.

### ✨ Improvements

**Execution plan**
* Feat: detached up runs on a single plan by @ndeloof in https://github.com/docker/compose/pull/14290
* Feat(up): interactive up runs on a single plan by @ndeloof in https://github.com/docker/compose/pull/14305
* Feat: scale and watch rebuild use the unified plan by @ndeloof in https://github.com/docker/compose/pull/14291
* Feat: compose start builds a start-only plan by @ndeloof in https://github.com/docker/compose/pull/14296

**Commands**
* Feat(run): --no-recreate reuses existing dependencies as-is by @ndeloof in https://github.com/docker/compose/pull/14144
* Feat(push): add --ignore-missing to skip images not available locally by @glours in https://github.com/docker/compose/pull/14341
* Feat(push): deprecate --ignore-push-failures in favor of --ignore-missing by @glours in https://github.com/docker/compose/pull/14354
* Feat(stats): add --all-projects and --aggregate flags by @glours in https://github.com/docker/compose/pull/14337
* Feat(network): let a service opt out of its name as a network alias by @glours in https://github.com/docker/compose/pull/14342
* Pass --parallel limit to bake as --jobs by @maxproske in https://github.com/docker/compose/pull/14352

**Other**
* Feat: support the umask service attribute by @ndeloof in https://github.com/docker/compose/pull/14367
* Use the Docker Desktop Hub session for Docker Hub registry credentials by @Benehiko in https://github.com/docker/compose/pull/14295

###
