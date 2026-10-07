---
title: "anthropics/anthropic-sdk-python v1.12.0 released"
url: "https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.12.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "anthropic-sdk-python"]
date: "2026-10-07T21:24:59Z"
metadata:
  repo: "anthropics/anthropic-sdk-python"
  version: "v1.12.0"
---

# anthropics/anthropic-sdk-python v1.12.0 released

> Source: github-releases | Category: changelog | 2026-10-07T21:24:59Z

## anthropics/anthropic-sdk-python — v1.12.0

## 1.12.0 (2026-10-07)

Full Changelog: [v1.11.0...v1.12.0](https://github.com/anthropics/anthropic-sdk-python/compare/v1.11.0...v1.12.0)

### Features

* **api:** add claude-haiku-5-5 and typed computer and browser toolset tool calls ([f6346e6](https://github.com/anthropics/anthropic-sdk-python/commit/f6346e63b7507a596e6e8acc9425cae2dfc7bf24))
* **api:** add disabled to thinking types in model capabilities ([78d815d](https://github.com/anthropics/anthropic-sdk-python/commit/78d815d78b33cfea5f4aa78c57a30b341fa8ff42))
* **api:** add display_name to RBAC roles and deprecate name ([f63f99c](https://github.com/anthropics/anthropic-sdk-python/commit/f63f99c17583fbdc7e0ba7b92f8f259724403146))
* **api:** add include_default parameter to list workspaces ([5d4b37b](https://github.com/anthropics/anthropic-sdk-python/commit/5d4b37b36b96e24fb605993216c39db378b14d4c))
* **api:** add lifecycle stage fields and filter to /v1/models ([0c96c02](https://github.com/anthropics/anthropic-sdk-python/commit/0c96c0212f4bfb6f592639c59378583cd80ee352))
* **api:** add line to model objects ([a85c649](https://github.com/anthropics/anthropic-sdk-python/commit/a85c649ff834f54c6809eaceb38e3317c3805fb4))
* **api:** add url_sources to the Managed Agents web_fetch tool config ([78d815d](https://github.com/anthropics/anthropic-sdk-python/commit/78d815d78b33cfea5f4aa78c57a30b341fa8ff42))
* **api:** add web search and code execution support to model capabilities ([78d815d](https://github.com/anthropics/anthropic-sdk-python/commit/78d815d78b33cfea5f4aa78c57a30b341fa8ff42))


### Bug Fixes

* **api:** send the beta header by default when listing spend limits ([e2690b4](https://github.com/anthropics/anthropic-sdk-python/commit/e2690b4e733b0453d05bb770f32743618cfc9c92))
* **client:** send empty strings in query params and multipart forms ([80e69f1](https://github.com/anthropics/anthropic-sdk-python/commit/80e69f1a204bd5bfdd090e6d32ce36c846544c1a))
* **tools:** keep a local edit made after a memory upload whose response was lost ([#990](https://github.com/anthropics/anthropic-sdk-python/issues/990)) ([78d815d](https://github.com/anthropics/anthropic-sdk-python/commit/78d815d78b33cfea5f4aa78c57a30b341fa8ff42))


### Chores

* **client:** track whether the client timeout was set explicitly ([36a223f](https://github.com/anthropics/anthropic-sdk-python/commit/36a223feb1cc309bb9e2fcba371b430455a5555a))
* **docs:** correct example groups in rate limit list description ([71fcf2f](https://github.com/anthropics/anthropic-sdk-python/commit/71fcf2fbf2caa7b28b228c50b23b94acc78467a9))
* **docs:** describe a federation rule's target by its type ([78d815d](https://github.com/anthropics/anthropic-sdk-python/commit/78d815d78b33cfea5f4aa78c57a30b341fa8ff42))
* **docs:** fix example IDs in sessions, agents and vault credentials ([78d815d](https://github.com/anthropics/anthropic-sdk-python/commit/78d815d78b33cfea5f4aa78c57a30b341fa8ff42))
* **docs:** update Managed Agents multiagent and thread descriptions ([78d815d](https://github.com/anthropics/anthropic-sdk-python/commit/78d815d78b33cfea5f4aa78c57a30b341fa8ff42))
* **docs:** update the activity summaries endpoint description ([d9bd4bf](https://github.com/anthropics/anthropic-sdk-python/commit/d9bd4bf6f558822e16a2d6a65fd333ee4d3596ab))
* **docs:** update the description of the Model line field ([4444463](https://github.com/anthropics/anthropic-sdk-python/commit/4444463ed4f434b248e92c6757b60b8b10a66285))
* **internal:** add REVIEW.md with review instructions ([78d815d](https://github.com/anthropics/anthropic-sdk-python/commit/78d815d78b33cfea5f4aa78c57a30b341fa8ff42))
* **internal:** format the code blocks of the docs with one run of ruff ([78d815d](https://github.com/anthropics/anthropic-sdk-python/commit/78d815d78b33cfea5f4aa78c57a30b341fa8ff42))
* **internal:** refactor deprecated models ([7b0c7d5](https://github.com/anthropics/anthropic-sdk-python/commit/7b0c7d5f4febd73b102559cbf7abcf72ff6ea775))
* **tests:** run tests skipped for a
