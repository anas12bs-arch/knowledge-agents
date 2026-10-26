---
title: "openai/openai-python v3.38.0 released"
url: "https://github.com/openai/openai-python/releases/tag/v3.38.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "openai-python"]
date: "2026-10-26T18:55:29Z"
metadata:
  repo: "openai/openai-python"
  version: "v3.38.0"
---

# openai/openai-python v3.38.0 released

> Source: github-releases | Category: changelog | 2026-10-26T18:55:29Z

## openai/openai-python — v3.38.0

## [3.38.0](https://github.com/openai/openai-python/compare/v3.37.0...v3.38.0) (2026-10-25)


### Features

* **api:** add delegation controls and prompt cache lifetimes ([#4169](https://github.com/openai/openai-python/issues/4169)) ([43045fc](https://github.com/openai/openai-python/commit/43045fcaf91aec08571e54c57706597cefd32d45))
* **api:** expand Live Decision item and question types ([#4175](https://github.com/openai/openai-python/issues/4175)) ([5d72315](https://github.com/openai/openai-python/commit/5d72315876ffd8b72b958623ef4db26da3fb1e61))


### Bug Fixes

* **agents:** clarify result schema warnings ([#4165](https://github.com/openai/openai-python/issues/4165)) ([cfa0a79](https://github.com/openai/openai-python/commit/cfa0a79b6395bb0561b28879122a9f90a87cdada))
* format API status errors using the server message ([#4161](https://github.com/openai/openai-python/issues/4161)) ([6ce5f05](https://github.com/openai/openai-python/commit/6ce5f058b3369dcf9f2a25f9fa67de0cca1451ab))
* preserve fallback parsing for PEP 604 unions ([#4160](https://github.com/openai/openai-python/issues/4160)) ([05dfea0](https://github.com/openai/openai-python/commit/05dfea0a1cb41a3e6ae1cc3bd13145b57cf3ffb8))
* **responses:** resolve function arguments within their namespace ([#4166](https://github.com/openai/openai-python/issues/4166)) ([81792ff](https://github.com/openai/openai-python/commit/81792ff040a2ca2b70348163049d3d69d5ba95cf))
* **responses:** validate tool namespaces before runner dispatch ([#4167](https://github.com/openai/openai-python/issues/4167)) ([56a55f2](https://github.com/openai/openai-python/commit/56a55f243960e05e6268bb48ba6bf45299b8f90b))


### Chores

* **api:** preserve client and resource compatibility ([#4157](https://github.com/openai/openai-python/issues/4157)) ([56f33a1](https://github.com/openai/openai-python/commit/56f33a12591516e9ce88ee72e3a59b15ac518641))
* enforce zero custom code in generated Python files ([#4168](https://github.com/openai/openai-python/issues/4168)) ([d622f28](https://github.com/openai/openai-python/commit/d622f28ad5cb3f947541936c0c139891211a42c5))
