---
title: "openai/openai-python v3.4.0 released"
url: "https://github.com/openai/openai-python/releases/tag/v3.4.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "openai-python"]
date: "2026-08-26T23:36:56Z"
metadata:
  repo: "openai/openai-python"
  version: "v3.4.0"
---

# openai/openai-python v3.4.0 released

> Source: github-releases | Category: changelog | 2026-08-26T23:36:56Z

## openai/openai-python — v3.4.0

## [3.4.0](https://github.com/openai/openai-python/compare/v3.3.1...v3.4.0) (2026-08-25)


### Features

* **api:** Add obfuscation field to ChatCompletionChunk ([#3690](https://github.com/openai/openai-python/issues/3690)) ([c7d8e1d](https://github.com/openai/openai-python/commit/c7d8e1d26be1f958e55c80f26b648f768afabdf2))
* **api:** add project residency configuration and cost quantity units ([#3726](https://github.com/openai/openai-python/issues/3726)) ([bc4f8ef](https://github.com/openai/openai-python/commit/bc4f8efdbc1f8fa6b78935e205780e259d83576d))


### Bug Fixes

* **api:** encode Realtime call offers and session configuration ([#3736](https://github.com/openai/openai-python/issues/3736)) ([555ac48](https://github.com/openai/openai-python/commit/555ac487f450f24928d859478ea2f41b58906206))
* apply consistent origin checks to WebSocket redirects ([#3693](https://github.com/openai/openai-python/issues/3693)) ([1b324d0](https://github.com/openai/openai-python/commit/1b324d044dcedc377e688c405416f928b0aedfb6))
* **azure:** encode deployment names consistently ([#3683](https://github.com/openai/openai-python/issues/3683)) ([689538d](https://github.com/openai/openai-python/commit/689538d531692e30ac1928779e6f1b97cc95db45))
* **azure:** keep provider validation errors value-free ([#3691](https://github.com/openai/openai-python/issues/3691)) ([72529c0](https://github.com/openai/openai-python/commit/72529c013707e7b5ed99edbc836603618a1e4be6))
* **azure:** resolve one authentication mode ([#3689](https://github.com/openai/openai-python/issues/3689)) ([e3d0681](https://github.com/openai/openai-python/commit/e3d06812535d7f2fe1bc6e57c12bd0ac0dd4acd1))
* compute custom-code summaries from trusted workflow code ([#3692](https://github.com/openai/openai-python/issues/3692)) ([2b5868d](https://github.com/openai/openai-python/commit/2b5868da23cb61876ec27d76591ea5fdb2b8c14d))
* create upload example fixtures in private directories ([#3686](https://github.com/openai/openai-python/issues/3686)) ([f36e6f7](https://github.com/openai/openai-python/commit/f36e6f79662b22e9d8f1660d4576b4b15cd8ac76))
* decode SSE incrementally without limiting event size ([#3687](https://github.com/openai/openai-python/issues/3687)) ([2598d53](https://github.com/openai/openai-python/commit/2598d530cf682784465e9f82558a830ac5f94486))
* keep Python SDK diagnostics metadata-only ([#3685](https://github.com/openai/openai-python/issues/3685)) ([600aa8d](https://github.com/openai/openai-python/commit/600aa8daade4c9df87deb76f6b8442ee828a7cbc))
* Preserve Azure authentication boundaries across transports ([#3684](https://github.com/openai/openai-python/issues/3684)) ([06ef57c](https://github.com/openai/openai-python/commit/06ef57caafe73d625ad4458ab5d29241e30c44bc))
* preserve the configured TLS hostname ([#3694](https://github.com/openai/openai-python/issues/3694)) ([aa5fbc4](https://github.com/openai/openai-python/commit/aa5fbc401f179fc515905d84623718c2b66ec653))
* preserve WebSocket send queue byte accounting during flush ([#3688](https://github.com/openai/openai-python/issues/3688)) ([96f966d](https://github.com/openai/openai-python/commit/96f966d77bddc7449ae23fda5b29ef44c3f98cc2))


### Chores

* **api:** Clarify image background docs and preview support ([#3703](https://github.com/openai/openai-python/issues/3703)) ([bedb9a7](https://github.com/openai/openai-python/commit/bedb9a7b8839e193107e88b92f7cc166f08ac83d))
* **api:** document supported image generation models ([#3695](https://github.com/openai/openai-python/issues/3695)) ([8edd9ae](https://github.com/openai/openai-python/commit/8edd9ae411f9d0a5385447a4697c9f7042868213))
* **api:** move chat validation tests out of generated code ([#3698](https://github.com/openai/openai-python/issues/3698)) ([9d3ba20](https://github.com/openai/openai-python/commit/9d3ba20f9567a62b2ebb3542661a60dc4ed2fd67))
* **api:** move webhook tests out of generated code ([#3700](https://github.com/openai/openai-python/issues/3700)) ([04ecb3c](h
