---
title: "pydantic/pydantic v2.14.1 released"
url: "https://github.com/pydantic/pydantic/releases/tag/v2.14.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "pydantic"]
date: "2026-10-12T00:47:55Z"
metadata:
  repo: "pydantic/pydantic"
  version: "v2.14.1"
---

# pydantic/pydantic v2.14.1 released

> Source: github-releases | Category: changelog | 2026-10-12T00:47:55Z

## pydantic/pydantic — v2.14.1

### What's Changed

#### Performance

* Avoid Python tuple allocation during model fields validation by @Viicos in [#13955](https://github.com/pydantic/pydantic/pull/13955)
* Avoid unnecessary extra dict allocation in model validation by @Viicos in [#13956](https://github.com/pydantic/pydantic/pull/13956)

#### Fixes

* Fix `arguments-v3` schema with variadic keywords by @Viicos in [#13954](https://github.com/pydantic/pydantic/pull/13954)
* Fix `TypeError` on `ForwardRef` on Python 3.10.0 by @Viicos in [#13964](https://github.com/pydantic/pydantic/pull/13964)
* Support `closed` and `extra_items` via inheritance in `TypedDict` by @Viicos in [#13967](https://github.com/pydantic/pydantic/pull/13967)
* Enforce the `max_digits` whole-digits limit in the Python `Decimal` validator by @Viicos in [#13972](https://github.com/pydantic/pydantic/pull/13972)
* Reject out-of-range int inputs for `timedelta` by @Viicos in [#13973](https://github.com/pydantic/pydantic/pull/13973)
* Support named tuples in `Sequence` validation by @Viicos in [#13978](https://github.com/pydantic/pydantic/pull/13978)

**Full Changelog**: https://github.com/pydantic/pydantic/compare/v2.14.0...v2.14.1
