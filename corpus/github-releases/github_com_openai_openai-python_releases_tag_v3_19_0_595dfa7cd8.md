---
title: "openai/openai-python v3.19.0 released"
url: "https://github.com/openai/openai-python/releases/tag/v3.19.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "openai-python"]
date: "2026-09-23T01:50:04Z"
metadata:
  repo: "openai/openai-python"
  version: "v3.19.0"
---

# openai/openai-python v3.19.0 released

> Source: github-releases | Category: changelog | 2026-09-23T01:50:04Z

## openai/openai-python — v3.19.0

## [3.19.0](https://github.com/openai/openai-python/compare/v3.18.0...v3.19.0) (2026-09-22)


### Features

* **api:** add GCP external storage support ([#3943](https://github.com/openai/openai-python/issues/3943)) ([d12d60f](https://github.com/openai/openai-python/commit/d12d60fff9f5624f2dc50ade3d832028f4fecaa7))
* **api:** add GPT-Rosalind research model ([#3940](https://github.com/openai/openai-python/issues/3940)) ([d041d73](https://github.com/openai/openai-python/commit/d041d736f75f03f6c87aa77f932823011691bac5))


### Bug Fixes

* **_utils/_transform:** propagate __api_exclude__ in _async_transform_recursive ([#3324](https://github.com/openai/openai-python/issues/3324)) ([161ae65](https://github.com/openai/openai-python/commit/161ae65ea676a000a156ba0dacfd904532b52473))
* **api:** handle omission markers in queued WebSocket events ([#3944](https://github.com/openai/openai-python/issues/3944)) ([63e4616](https://github.com/openai/openai-python/commit/63e46169a7c6525ec90c7f2815a05d56e795cbcf))
* **client:** retry only replayable request content ([#3771](https://github.com/openai/openai-python/issues/3771)) ([6e0c2be](https://github.com/openai/openai-python/commit/6e0c2beeb639e42ff74f14135151d8bcb1e5b245))
* **client:** tolerate older optional aiohttp installations ([#3941](https://github.com/openai/openai-python/issues/3941)) ([0d91efb](https://github.com/openai/openai-python/commit/0d91efbe5084c2f572688e8e9a05c0a91c8c0319))
* **helpers:** use asyncio.get_running_loop() inside async methods ([#3289](https://github.com/openai/openai-python/issues/3289)) ([bac3545](https://github.com/openai/openai-python/commit/bac3545eee5a0dfd348a6766bca3e904308792dd))
