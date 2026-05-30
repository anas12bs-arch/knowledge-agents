---
title: "pydantic/pydantic v2.14.0a1 released"
url: "https://github.com/pydantic/pydantic/releases/tag/v2.14.0a1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "pydantic"]
date: "2026-05-30T14:31:29Z"
metadata:
  repo: "pydantic/pydantic"
  version: "v2.14.0a1"
---

# pydantic/pydantic v2.14.0a1 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:29Z

## pydantic/pydantic — v2.14.0a1

## v2.14.0a1 (2026-05-22)

### What's Changed

#### Packaging

* Add PyEmscripten platform tag support by @Viicos, @greateggsgreg and @sinaatalay in [#13199](https://github.com/pydantic/pydantic/pull/13199):
  `pydantic-core` now has a 3.14 wheel published with the [`pyemscripten_2026_0` platform tag](https://pyodide.org/en/latest/development/abi/314.html).
  Note that this wheel can only be used with [Pyodide 314.0](https://github.com/pyodide/pyodide/issues/6233) and greater, still in development.
  It is recommended to wait for the final 314.0 release (and for Pydantic to publish a new wheel in a future 2.14 release).

#### Changes

* Accept `None` in `MultiHostUrl.build()`'s `hosts` parameter by @Viicos in [#13068](https://github.com/pydantic/pydantic/pull/13068)
* Drop support for Python 3.9 by @Viicos in [#13070](https://github.com/pydantic/pydantic/pull/13070)
* Remove support for `eval_type_backport()` by @Viicos in [#13133](https://github.com/pydantic/pydantic/pull/13133)
* Only deepcopy non-updated fields in `model_copy()` by @connorcarpenter15 in [#13087](https://github.com/pydantic/pydantic/pull/13087)

#### Fixes

* Add Mypy plugin workaround for dynamic models defined in functions by @ilevkivskyi in [#13177](https://github.com/pydantic/pydantic/pull/13177)
* Fallback to `create_model()` overload definition when `__base__` is set to a type variable in the Mypy plugin by @cyphercodes in [#13146](https://github.com/pydantic/pydantic/pull/13146)

### New Contributors

* @ilevkivskyi made their first contribution in [#13177](https://github.com/pydantic/pydantic/pull/13177)
* @cyphercodes made their first contribution in [#13146](https://github.com/pydantic/pydantic/pull/13146)
* @connorcarpenter15 made their first contribution in [#13087](https://github.com/pydantic/pydantic/pull/13087)

**Full Changelog**: https://github.com/pydantic/pydantic/compare/v2.13.4...v2.14.0a1
