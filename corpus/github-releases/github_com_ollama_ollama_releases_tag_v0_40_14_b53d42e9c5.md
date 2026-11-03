---
title: "ollama/ollama v0.40.14 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.40.14"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-11-03T09:23:30Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.40.14"
---

# ollama/ollama v0.40.14 released

> Source: github-releases | Category: changelog | 2026-11-03T09:23:30Z

## ollama/ollama — v0.40.14

## What's Changed
* `ollama launch claude` now applies the model's output token limit for Claude Code, so cloud models no longer run into the 128k default cap
* Cloud web search responses on `/api/chat` are now decoded correctly, including compressed responses
* OpenAI-compatible endpoints no longer override a model's packaged sampler defaults — clients that send no `temperature`/`top_p` get the model's own values instead of 1.0, matching `/api/chat`
* `/v1/responses` now preserves readable input content, including prior assistant refusals, instead of flattening it
* Ollama's app can now retry ChatGPT disconnect failures instead of leaving the connection in a broken state
* `ollama launch codex` verifies ChatGPT routing before configuring, and reports a clear error when routing is unavailable
* Faster top-k sampling on MLX for large vocabularies

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.13...v0.40.14
