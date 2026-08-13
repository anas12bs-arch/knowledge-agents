---
title: "anthropics/anthropic-sdk-python v0.122.0 released"
url: "https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.122.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "anthropic-sdk-python"]
date: "2026-08-13T19:34:05Z"
metadata:
  repo: "anthropics/anthropic-sdk-python"
  version: "v0.122.0"
---

# anthropics/anthropic-sdk-python v0.122.0 released

> Source: github-releases | Category: changelog | 2026-08-13T19:34:05Z

## anthropics/anthropic-sdk-python — v0.122.0

## 0.122.0 (2026-08-13)

Full Changelog: [v0.121.0...v0.122.0](https://github.com/anthropics/anthropic-sdk-python/compare/v0.121.0...v0.122.0)

### Features

* **api:** add output_behavior to dream creation (create a new memory store or update the input store in place) ([852c4bb](https://github.com/anthropics/anthropic-sdk-python/commit/852c4bbe4a3a425a8780e89ea6c3cae54836e8bb))


### Bug Fixes

* **bedrock,aws:** run SigV4 signing off the event loop in async clients ([#334](https://github.com/anthropics/anthropic-sdk-python/issues/334)) ([2bae6c8](https://github.com/anthropics/anthropic-sdk-python/commit/2bae6c8cb86f693f4e1e3dd13bb64e03b01fe720))
* **bedrock:** expose beta.messages.parse, stream and tool_runner ([#366](https://github.com/anthropics/anthropic-sdk-python/issues/366)) ([6eca7bb](https://github.com/anthropics/anthropic-sdk-python/commit/6eca7bb19f968856b5652d5471e3ca9fc3fe8641))
* **client:** add models ([52e9d94](https://github.com/anthropics/anthropic-sdk-python/commit/52e9d9453a46a281846f9860e742bfc938bafebc))
* **client:** keep token exchange bound per client across copy() ([#388](https://github.com/anthropics/anthropic-sdk-python/issues/388)) ([c13e6e3](https://github.com/anthropics/anthropic-sdk-python/commit/c13e6e30b75d73b9af51468ae0deae6e6aca1ba0))
* **client:** read PathLike contents passed inside a file tuple ([070f953](https://github.com/anthropics/anthropic-sdk-python/commit/070f95332daea9dc3ed19fe91251d6e5285e5560))
* **client:** treat empty ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN as unset ([#341](https://github.com/anthropics/anthropic-sdk-python/issues/341)) ([76a2e68](https://github.com/anthropics/anthropic-sdk-python/commit/76a2e68531d50c9043a5ac58919527287e56a842))
* **streaming:** add context to malformed tool input JSON errors in the non-beta accumulator ([#339](https://github.com/anthropics/anthropic-sdk-python/issues/339)) ([a343e17](https://github.com/anthropics/anthropic-sdk-python/commit/a343e17b7bc970f656fa02a980b0baa2bf8c3b80))
* **streaming:** apply all message_delta fields when accumulating streamed messages ([#380](https://github.com/anthropics/anthropic-sdk-python/issues/380)) ([fc1599b](https://github.com/anthropics/anthropic-sdk-python/commit/fc1599bd4c25ad5550d55f8f1c8f5c5664e19ed1))
* **streaming:** emit input_json events for server tool use blocks ([#336](https://github.com/anthropics/anthropic-sdk-python/issues/336)) ([ccfc8e1](https://github.com/anthropics/anthropic-sdk-python/commit/ccfc8e140e8e6b824e74c8fd9bed2587e60c5b6f))
* **streaming:** keep omitted content block fields unset in accumulated messages ([#346](https://github.com/anthropics/anthropic-sdk-python/issues/346)) ([cd40aab](https://github.com/anthropics/anthropic-sdk-python/commit/cd40aab995181aa44e9fbdb7b6ce1fa82357c18b))
* **streaming:** run the request transform once in messages.stream() ([#347](https://github.com/anthropics/anthropic-sdk-python/issues/347)) ([81a92da](https://github.com/anthropics/anthropic-sdk-python/commit/81a92dafa2efd87c850950d7d84af727d01c2e47))
* **streaming:** silence pydantic serializer warnings on message_stop events ([#338](https://github.com/anthropics/anthropic-sdk-python/issues/338)) ([41f9cdc](https://github.com/anthropics/anthropic-sdk-python/commit/41f9cdcac36d4c6a3d9d2c8becaa632c75a44054))
* **tools:** reject symlink loops in tool paths and skip special skill-archive members ([#322](https://github.com/anthropics/anthropic-sdk-python/issues/322)) ([43e8669](https://github.com/anthropics/anthropic-sdk-python/commit/43e8669d066a1d18ffdbff505fc99ac45aa7492e))
* **vertex:** expose beta.messages.parse and tool_runner ([#367](https://github.com/anthropics/anthropic-sdk-python/issues/367)) ([96723a0](https://github.com/anthropics/anthropic-sdk-python/commit/96723a000b6179f0bee51a0b5aa0129e360dc323))


### Chores

* **ci:** run breaking-change detection as a ci.yml job on every push ([6dfd16e](https://github.com/anthropics/anthropic-sdk-python/commit/6dfd16ea7a650dc65253c72264cbcb14
