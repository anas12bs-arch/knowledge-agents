---
title: "ollama/ollama v0.34.1 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.34.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-09-15T21:39:37Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.34.1"
---

# ollama/ollama v0.34.1 released

> Source: github-releases | Category: changelog | 2026-09-15T21:39:37Z

## ollama/ollama — v0.34.1

## What's Changed
* MLX safetensors `ollama create` no longer experimental.  GGUF model creation now requires using llama.cpp tooling for safetensor conversion and quantization.
* Improved MLX memory handling on Apple Silicon
* Runaway repeat token detection now requires 100 repeat tokens for reduced false positives (e.g. OCR)
* `/api/tags` is much faster on large model libraries (3.1 s → 294 ms cold in testing), and model capabilities are now reported consistently.
* Deprecated `typical_p`: it can no longer be set when creating new models, existing GGUF models retain support.
* MLX and llama.cpp updates


**Full Changelog**: https://github.com/ollama/ollama/compare/v0.34.0...v0.34.1-rc1
