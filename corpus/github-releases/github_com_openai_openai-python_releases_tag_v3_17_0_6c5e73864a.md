---
title: "openai/openai-python v3.17.0 released"
url: "https://github.com/openai/openai-python/releases/tag/v3.17.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "openai-python"]
date: "2026-09-22T05:30:21Z"
metadata:
  repo: "openai/openai-python"
  version: "v3.17.0"
---

# openai/openai-python v3.17.0 released

> Source: github-releases | Category: changelog | 2026-09-22T05:30:21Z

## openai/openai-python — v3.17.0

## [3.17.0](https://github.com/openai/openai-python/compare/v3.16.2...v3.17.0) (2026-09-22)


### Features

* **api:** add external storage configuration management ([#3909](https://github.com/openai/openai-python/issues/3909)) ([6332577](https://github.com/openai/openai-python/commit/6332577d3fb5f83f7f381a431460262f7192402d))
* **api:** add safety case retrieval ([#3911](https://github.com/openai/openai-python/issues/3911)) ([a87b938](https://github.com/openai/openai-python/commit/a87b938545b34c1880b9914b43a5039072f40b09))
* **api:** add safety warning and deactivation webhook events ([#3908](https://github.com/openai/openai-python/issues/3908)) ([19f1f37](https://github.com/openai/openai-python/commit/19f1f3769f4d2e907b6970c52f647a750de625e6))
* **api:** add session environment reset events ([#3913](https://github.com/openai/openai-python/issues/3913)) ([69a2c1d](https://github.com/openai/openai-python/commit/69a2c1db6feacf32be6693809e7cab1c3b49cad7))
* **api:** add SIP media security to incoming call events ([#3907](https://github.com/openai/openai-python/issues/3907)) ([c377eb2](https://github.com/openai/openai-python/commit/c377eb21f03efb223180730d6da61f9e8d500063))
* **api:** support environment variable vault credentials ([#3905](https://github.com/openai/openai-python/issues/3905)) ([eeebc53](https://github.com/openai/openai-python/commit/eeebc535572dfe034e2c82958df4d0c22f94301e))


### Bug Fixes

* **api:** correct model types and network policy docs ([618bb31](https://github.com/openai/openai-python/commit/618bb312e52c2b62f75f56602b7388e6d023aa33))
* **api:** preserve model choices and defer error response docs ([#3931](https://github.com/openai/openai-python/issues/3931)) ([6e7a90f](https://github.com/openai/openai-python/commit/6e7a90f18b92dcf320e94b1edf98187568ac6fbd))
* **lib:** treat null message content as empty in parse_response ([#3851](https://github.com/openai/openai-python/issues/3851)) ([fab5283](https://github.com/openai/openai-python/commit/fab5283255ad76d9e79e202e1cf46b6eea783f4b))
* **lib:** use log.warning instead of the deprecated log.warn ([#3878](https://github.com/openai/openai-python/issues/3878)) ([56b1708](https://github.com/openai/openai-python/commit/56b17081e22d8e168421e91bb400017ec2b0be89))


### Chores

* **api:** document API error response contracts ([#3917](https://github.com/openai/openai-python/issues/3917)) ([fededc9](https://github.com/openai/openai-python/commit/fededc9e51f4fef2b251e25542766c83065373b0))
* **api:** document response management resources ([#3912](https://github.com/openai/openai-python/issues/3912)) ([eaa5b77](https://github.com/openai/openai-python/commit/eaa5b77912a2c3c4feff0a734b6ca087ccf52a01))
* **deps:** bump actions/github-script from 7.1.0 to 9.0.0 ([#3769](https://github.com/openai/openai-python/issues/3769)) ([32e07e1](https://github.com/openai/openai-python/commit/32e07e19438abada5da5bfb530c49f385ed849d4))
* **deps:** bump actions/upload-artifact from 5.0.0 to 7.0.1 ([#3767](https://github.com/openai/openai-python/issues/3767)) ([b413abe](https://github.com/openai/openai-python/commit/b413abed3e9d5e998743c0b46f5011eece2dd4ed))
* **deps:** bump CodeQL init and analyze to 4.37.8 ([#3765](https://github.com/openai/openai-python/issues/3765)) ([f95237f](https://github.com/openai/openai-python/commit/f95237f6d132d04ee65c5af6a8891e9b9f9708e4))
* **deps:** bump CodeQL init and analyze to 4.37.8 ([#3766](https://github.com/openai/openai-python/issues/3766)) ([690a8b5](https://github.com/openai/openai-python/commit/690a8b5c1cb2ea8f23bcc5d23a78fd22352d6999))
* **deps:** bump httpx2 from 2.7.0 to 2.12.0 in the python-security group across 1 directory ([#3823](https://github.com/openai/openai-python/issues/3823)) ([9b8e399](https://github.com/openai/openai-python/commit/9b8e3998d99aedb446626906096ee3181a6cf62f))
* **deps:** bump openai/codex-action from 1.11 to 1.12 ([#3768](https://github.com/openai/openai-python/issues/3768)) ([9c1579b](https://github.com/openai/o
