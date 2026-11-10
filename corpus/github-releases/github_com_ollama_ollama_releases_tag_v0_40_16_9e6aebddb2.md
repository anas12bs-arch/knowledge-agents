---
title: "ollama/ollama v0.40.16 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.40.16"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-11-10T02:26:37Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.40.16"
---

# ollama/ollama v0.40.16 released

> Source: github-releases | Category: changelog | 2026-11-10T02:26:37Z

## ollama/ollama — v0.40.16

## Ripple Preview

[Ripple Preview](https://ollama.com/library/ripple-preview) from Ricursive Intelligence is a 65B dense model built for agentic coding.

```sh
ollama run ripple-preview
```

## What's Changed

- Qwen3.8 Flash Next uses about 27 GiB less memory on Apple silicon
- `ollama launch claude` always routes Claude Code to the selected model
- `ollama launch` explains when a cloud model has been retired
- `/v1/responses` respects `truncation` and no longer silently truncates by default
- `/v1/models` returns an empty list instead of `null` when no models are installed
- CUDA 13.5 support for Windows on ARM
- Updated llama.cpp

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.15...v0.40.16
