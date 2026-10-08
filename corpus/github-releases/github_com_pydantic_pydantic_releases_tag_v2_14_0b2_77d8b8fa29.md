---
title: "pydantic/pydantic v2.14.0b2 released"
url: "https://github.com/pydantic/pydantic/releases/tag/v2.14.0b2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "pydantic"]
date: "2026-10-08T14:39:52Z"
metadata:
  repo: "pydantic/pydantic"
  version: "v2.14.0b2"
---

# pydantic/pydantic v2.14.0b2 released

> Source: github-releases | Category: changelog | 2026-10-08T14:39:52Z

## pydantic/pydantic — v2.14.0b2

### What's Changed

This pre-release adds full support for Python 3.15 specific features, such as support for [`frozendict`](https://docs.python.org/3.15/library/stdtypes.html#frozendict), making use of [`TypeForm`](https://docs.python.org/3.15/library/typing.html#typing.TypeForm) and stabilizing the [`MISSING` sentinel](https://pydantic.dev/docs/validation/latest/concepts/types/#missing-sentinel) type.

#### New Features

* Allow any `CoreSchema` to be used as serialization by @Viicos in [#13680](https://github.com/pydantic/pydantic/pull/13680)
* Add support for [`frozendict`](https://docs.python.org/3.15/library/stdtypes.html#frozendict) type by @Viicos in [#13634](https://github.com/pydantic/pydantic/pull/13634)
* Allow `dict`, `frozendict` and `frozenset` as `defaultdict` default factories by @Viicos in [#13623](https://github.com/pydantic/pydantic/pull/13623)
* Add support for [`TypeForm`](https://docs.python.org/3.15/library/typing.html#typing.TypeForm) by @Viicos in [#13459](https://github.com/pydantic/pydantic/pull/13459).

  This adds support for static type checking where a type form is expected. For instance, type adapters:

    ```python
    from pydantic import TypeAdapter

    ta = TypeAdapter(int | str)
    assert_type(ta.validate_python(1), int | str)
    ```

* Add support for lazy imports by @Viicos in [#13776](https://github.com/pydantic/pydantic/pull/13776)
* Stabilize `MISSING` sentinel by @Viicos in [#13782](https://github.com/pydantic/pydantic/pull/13782).

  The [`MISSING` sentinel](https://pydantic.dev/docs/validation/dev/concepts/types/#missing-sentinel) is no longer experimental, and can be imported as `from pydantic import MISSING`.

#### Changes

* Take `ser_json_temporal` into account when generating JSON Schema by @shashiKundur1 in [#13665](https://github.com/pydantic/pydantic/pull/13665)
* Use the field name in `__signature__` when `validate_by_alias` is`False` by @jaideeppyne in [#13730](https://github.com/pydantic/pydantic/pull/13730)
* Add a `deque` core schema by @Viicos in [#13757](https://github.com/pydantic/pydantic/pull/13757)
* Do not mention `MISSING` as a valid value in validation errors by @Viicos in [#13779](https://github.com/pydantic/pydantic/pull/13779)
* Refactor `Decimal` JSON Schema `pattern` constraint by @Viicos in [#13672](https://github.com/pydantic/pydantic/pull/13672)

#### Performance

* Refactor type references logic by @Viicos in [#13643](https://github.com/pydantic/pydantic/pull/13643)
* Improve performance of `GenerateSchema.generate_schema()` dispatching by @Viicos in [#13614](https://github.com/pydantic/pydantic/pull/13614)
* Move schema gathering logic to `pydantic-core` by @Viicos in [#13725](https://github.com/pydantic/pydantic/pull/13725)
* Improve performance of `FieldInfo` construction by @Viicos in [#13726](https://github.com/pydantic/pydantic/pull/13726)

#### Fixes

* Fix support for callable discriminators with PEP 695 type aliases by @Viicos in [#13604](https://github.com/pydantic/pydantic/pull/13604)
* Preserve `re.Pattern` instance for compiled patterns in the experimental pipeline by @soma0212 in [#13611](https://github.com/pydantic/pydantic/pull/13611)
* Fix missing GC traversal on some `pydantic-core` struct fields by @Viicos in [#13624](https://github.com/pydantic/pydantic/pull/13624)
* Fix missing GC traversal in `pydantic-core` for `GeneralFieldsSerializer` by @Viicos in [#13629](https://github.com/pydantic/pydantic/pull/13629)
* Fix JSON schema discriminator mapping keys for `bool` discriminators by @remi-fongaufier in [#13632](https://github.com/pydantic/pydantic/pull/13632)
* Fix application of other constraints in the pipeline API by @Viicos in [#13659](https://github.com/pydantic/pydantic/pull/13659)
* Support bare `None` annotation for discriminated unions by @Viicos in [#13667](https://github.com/pydantic/pydantic/pull/13667)
* Respect runtime alias validation configuration when wrap valida
