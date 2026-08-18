---
title: "langchain-ai/langchain langchain-openai==1.5.2a1 released"
url: "https://github.com/langchain-ai/langchain/releases/tag/langchain-openai%3D%3D1.5.2a1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "langchain"]
date: "2026-08-18T02:13:32Z"
metadata:
  repo: "langchain-ai/langchain"
  version: "langchain-openai==1.5.2a1"
---

# langchain-ai/langchain langchain-openai==1.5.2a1 released

> Source: github-releases | Category: changelog | 2026-08-18T02:13:32Z

## langchain-ai/langchain — langchain-openai==1.5.2a1

Initial release

release(openai): 1.5.2a1 (#39709)
feat(openai): extract gateway metadata from response headers when available (#39706)
chore(openai): update snapshots (#39657)
fix(openai): support o-series models in `get_num_tokens_from_messages` (#38710)
release(openai): 1.5.1 (#39653)
fix(openai): preserve streamed encrypted reasoning (#39635)
chore(infra): support langsmith gateway in CI (#39651)
release(openai): 1.5.0 (#39629)
feat(openai): support openai 3.0 SDK (#39613)
chore(partners): bump langgraph floor in openai and huggingface lockfiles (#39617)
release(openai): 1.4.3 (#39485)
fix(openai): filter invalid tool calls from content (#39366)
chore(openai): update guidance for responses API for OpenAI-compatible providers (#39327)
chore(openai): update docstring for `include_response_headers` (#39326)
release(openai): 1.4.2 (#39322)
fix(openai): handle `ContextWindowExceededError` (#39300)
chore: bump the minor-and-patch group across 3 directories with 7 updates (#39187)
fix(openai): filter langchain-generated content block IDs (#39209)
fix(openai): preserve Responses `text` options (#39204)
fix(openai): redact MCP `authorization` (#39155)
chore(model-profiles): refresh model profile data (#39050)
release(openai): 1.4.1 (#39045)
feat(anthropic,fireworks,openai): support langsmith gateway through env var (#38742)
fix(openai): correct `gpt-5.3-chat-latest` profile (#39009)
release(openai): 1.4.0 (#38983)
chore: bump pillow from 12.2.0 to 12.3.0 in /libs/partners/openai (#38999)
feat(core): add `reasoning_effort` as a standard chat model parameter (#38887)
chore(model-profiles): refresh model profile data (#38797)
release(openai): 1.3.5 (#38785)
feat(openai): support explicit prompt caching (#38762)
chore(model-profiles): refresh model profile data (#38774)
release(openai): 1.3.4 (#38731)
fix(openai): suppress Pydantic serializer warning on structured output parsed field (#37727)
test(openai): skip Codex VCR tests before cassette setup (#38690)
chore: bump the minor-and-patch group across 3 directories with 11 updates (#38587)
chore: bump langgraph-checkpoint from 4.1.0 to 4.1.1 in /libs/partners/openai (#38476)
fix(core): use `asyncio.get_running_loop()` in async contexts (#38157)
test(openai): clarify async API key sync failure trace (#38379)
release(openai): 1.3.3 (#38375)
fix(openai): drop response item ids when `store` is false (#38372)
fix(langchain,openai): only set `strict=True` on tools for OpenAI-compatible models in `ProviderStrategy` (#38370)
test(openai): clarify expected strict schema error (#38338)
fix(openai): drop `stop` from Responses API payload (#38336)
chore: bump langsmith from 0.8.5 to 0.8.18 in /libs/partners/openai (#38293)
chore: bump vcrpy from 8.1.1 to 8.2.1 in /libs/partners/openai (#38294)
chore(model-profiles): refresh model profile data (#38274)
test(openai): vcr embedding raw equivalence tests (#38199)
release(openai): 1.3.2 (#38130)
fix(openai): build Codex async headers off the event loop in `_agenerate` (#38129)
fix(openai): avoid sync token reads in Codex streaming (#38128)
hotfix(openai): skip Codex live integration tests in CI (#38124)
hotfix(openai): switch version (#38123)
refactor(openai): mark Codex OAuth classes private (#38122)
release(openai): 1.4.0 (#38120)
feat(openai): add ChatGPT OAuth-backed `ChatOpenAICodex` chat model (#37569)
docs: refresh `README` installation and resources (#38119)
test(core,langchain): update tests for explicit deserialization allowlists (#38118)
release(core): 1.4.7 (#38111)
fix(core,partners): rename package version trace metadata (#38110)
style(core,langchain,langchain-classic,partners): replace double backticks in docstrings (#38095)
test(openai): use `gpt-4o` for image token counting (#38089)
release(core): 1.4.6 (#38061)
feat(core,partners): add package version tracking to tracing metadata (#35295)
fix(core,openai): normalize v1 streamed tool calls (#35983)
chore(infra): bump mypy to 2.1 and unify type-check config across the monorepo (#36470)

