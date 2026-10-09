---
title: "pydantic/pydantic v2.14.0 released"
url: "https://github.com/pydantic/pydantic/releases/tag/v2.14.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "pydantic"]
date: "2026-10-09T00:19:21Z"
metadata:
  repo: "pydantic/pydantic"
  version: "v2.14.0"
---

# pydantic/pydantic v2.14.0 released

> Source: github-releases | Category: changelog | 2026-10-09T00:19:21Z

## pydantic/pydantic — v2.14.0

### What's Changed

The highlights of the v2.14 release are available in the [blog post](https://pydantic.dev/articles/pydantic-v2-14-release).
Several minor changes (considered non-breaking changes according to our [versioning policy](https://pydantic.dev/docs/validation/2.14/get-started/version-policy/#pydantic-v2)) are also included in this release. Make sure to look into them before upgrading.

This release drops support for Python 3.9 and adds support for Python 3.15.

#### New Features

* Add support for `multiple_of` constraint in `fraction` and `timedelta` core schemas by @Viicos in [#13873](https://github.com/pydantic/pydantic/pull/13873)
* Add `__namespace__` parameter to `create_model()` by @Viicos in [#13895](https://github.com/pydantic/pydantic/pull/13895)

#### Changes

* Add an `ordered-dict` core schema by @Viicos in [#13796](https://github.com/pydantic/pydantic/pull/13796)
* Add a `counter` core schema by @Viicos in [#13824](https://github.com/pydantic/pydantic/pull/13824)
* Do not mutate `model_config` attribute by @Viicos in [#13825](https://github.com/pydantic/pydantic/pull/13825)
* Reject newlines in `NameEmail` validation by @Viicos in [#13897](https://github.com/pydantic/pydantic/pull/13897)

#### Fixes

* Call enum constructors in both validation modes by @Viicos in [#13792](https://github.com/pydantic/pydantic/pull/13792)
* Fix documentation examples not raising and remove unused `string_sub_type` unused error code by @Viicos in [#13821](https://github.com/pydantic/pydantic/pull/13821)
* Catch `OverflowError` during `ByteSize` validation by @Viicos in [#13850](https://github.com/pydantic/pydantic/pull/13850)
* Require `multiple_of` constraints to be positive by @Viicos in [#13862](https://github.com/pydantic/pydantic/pull/13862)
* Always pop field name and model type stacks during schema generation by @saquibjawedbit in [#13859](https://github.com/pydantic/pydantic/pull/13859)
* Handle `TypeError` gracefully during docstring extraction by @Viicos in [#13874](https://github.com/pydantic/pydantic/pull/13874)
* Fix config propagation of stdlib dataclasses and `TypedDict`s in JSON Schema by @Viicos in [#13891](https://github.com/pydantic/pydantic/pull/13891)
* Don't apply `ser_json_timedelta` to all datetime types in serialization inference by @Viicos in [#13892](https://github.com/pydantic/pydantic/pull/13892)
* Encode JSON Schema defaults with a consistent configuration by @Viicos in [#13893](https://github.com/pydantic/pydantic/pull/13893)
* Propagate `init` and `kw_only=False` from `Field()` to stdlib dataclass fields by @Viicos in [#13898](https://github.com/pydantic/pydantic/pull/13898)
* Respect propagated extra config in the JSON Schema of stdlib dataclasses by @Viicos in [#13899](https://github.com/pydantic/pydantic/pull/13899)
* Handle OS errors during `ZoneInfo` validation by @Viicos in [#13912](https://github.com/pydantic/pydantic/pull/13912)
* Handle exceptions during `Decimal` validation by @Viicos in [#13940](https://github.com/pydantic/pydantic/pull/13940)
* Rebuild incomplete types during serialization inference by @Viicos in [#13922](https://github.com/pydantic/pydantic/pull/13922)
* Reject large exponents in `Fraction` validation by @Viicos in [#13944](https://github.com/pydantic/pydantic/pull/13944)
* Avoid validating URL prefix multiple times in multi host URLs by @Viicos in [#13945](https://github.com/pydantic/pydantic/pull/13945)

**Full Changelog**: https://github.com/pydantic/pydantic/compare/v2.13.0...v2.14.0
