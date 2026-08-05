---
title: "ollama/ollama v0.32.6 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.32.6"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-08-05T20:01:49Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.32.6"
---

# ollama/ollama v0.32.6 released

> Source: github-releases | Category: changelog | 2026-08-05T20:01:49Z

## ollama/ollama — v0.32.6

## What's Changed
  - Qwen3.5 is faster on Apple GPUs: the MLX engine now uses the model's MTP head for speculative decoding automatically
  - `/v1/chat/completions` streaming now matches OpenAI's wire format: `role` only on the first chunk, `finish_reason` on its own chunk,
  and usage in a separate chunk with `stream_options.include_usage`.
  - Truncated OpenAI responses now report `finish_reason: "length"` instead of `"tool_calls"`.
  - `ollama run kimi-k3` now offers `kimi-k3:cloud` for cloud-only models that publish no default tag, instead of failing.
  - TUI fixes: pipe-delimited prose no longer renders as a table, Enter accepts the highlighted `@` file completion, and `/prompt`
  scrolling is no longer laggy.
  - Experimental image generation has been temporarily removed. Continue using 0.32.5 for image generation support
  - Updated the MLX and llama.cpp engines.

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.32.5...v0.32.6-rc0
