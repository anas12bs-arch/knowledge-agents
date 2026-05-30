---
title: "microsoft/autogen python-v0.7.5 released"
url: "https://github.com/microsoft/autogen/releases/tag/python-v0.7.5"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "autogen"]
date: "2026-05-30T14:31:31Z"
metadata:
  repo: "microsoft/autogen"
  version: "python-v0.7.5"
---

# microsoft/autogen python-v0.7.5 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:31Z

## microsoft/autogen — python-v0.7.5

## What's Changed
* Fix docs dotnet core typo by @lach-g in https://github.com/microsoft/autogen/pull/6950
* Fix loading streaming Bedrock response with tool usage with empty argument by @pawel-dabro in https://github.com/microsoft/autogen/pull/6979
* Support linear memory in RedisMemory by @justin-cechmanek in https://github.com/microsoft/autogen/pull/6972
* Fix message ID for correlation between streaming chunks and final mes… by @smalltalkman in https://github.com/microsoft/autogen/pull/6969
* fix: extra args not work to disable thinking by @liuyunrui123 in https://github.com/microsoft/autogen/pull/7006
* Add thinking mode support for anthropic client by @SrikarMannepalli in https://github.com/microsoft/autogen/pull/7002
* Fix spurious </think> tags caused by empty string reasoning_content in streaming by @Copilot in https://github.com/microsoft/autogen/pull/7025
* Fix GraphFlow cycle detection to properly clean up recursion state by @Copilot in https://github.com/microsoft/autogen/pull/7026
* Add comprehensive GitHub Copilot instructions for AutoGen development by @Copilot in https://github.com/microsoft/autogen/pull/7029
* Fix Redis caching always returning False due to unhandled string values by @Copilot in https://github.com/microsoft/autogen/pull/7022
* Fix OllamaChatCompletionClient load_component() error by adding to WELL_KNOWN_PROVIDERS by @Copilot in https://github.com/microsoft/autogen/pull/7030
* Fix finish_reason logic in Azure AI client streaming response by @litterzhang in https://github.com/microsoft/autogen/pull/6963
* Add security warnings and default to DockerCommandLineCodeExecutor by @ekzhu in https://github.com/microsoft/autogen/pull/7035
* Fix: Handle nested objects in array items for JSON schema conversion by @kkutrowski in https://github.com/microsoft/autogen/pull/6993
* Fix not supported field warnings in count_tokens_openai by @seunggil1 in https://github.com/microsoft/autogen/pull/6987
* Fix(mcp): drain pending command futures on McpSessionActor failure by @withsmilo in https://github.com/microsoft/autogen/pull/7045
* Add missing reasoning_effort parameter support for OpenAI GPT-5 models by @Copilot in https://github.com/microsoft/autogen/pull/7054
* Update version to 0.7.5 by @ekzhu in https://github.com/microsoft/autogen/pull/7058

## New Contributors
* @lach-g made their first contribution in https://github.com/microsoft/autogen/pull/6950
* @pawel-dabro made their first contribution in https://github.com/microsoft/autogen/pull/6979
* @smalltalkman made their first contribution in https://github.com/microsoft/autogen/pull/6969
* @liuyunrui123 made their first contribution in https://github.com/microsoft/autogen/pull/7006
* @SrikarMannepalli made their first contribution in https://github.com/microsoft/autogen/pull/7002
* @litterzhang made their first contribution in https://github.com/microsoft/autogen/pull/6963
* @kkutrowski made their first contribution in https://github.com/microsoft/autogen/pull/6993
* @seunggil1 made their first contribution in https://github.com/microsoft/autogen/pull/6987

**Full Changelog**: https://github.com/microsoft/autogen/compare/python-v0.7.4...python-v0.7.5
