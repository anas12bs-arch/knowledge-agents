---
title: "ollama/ollama v0.30.0 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.30.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-06-02T00:00:01Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.30.0"
---

# ollama/ollama v0.30.0 released

> Source: github-releases | Category: changelog | 2026-06-02T00:00:01Z

## ollama/ollama — v0.30.0

This version of Ollama will change the architecture to directly support llama.cpp instead of building on top of GGML, and allows for compatibility with GGUF file format. MLX is used to accelerate model inference on Apple Silicon.

While in pre-release we'd love [feedback](https://github.com/ollama/ollama/pull/16031) on:

* Performance improvements or degradation
* Errors or crashes that did not previously occur
* Memory utilization improvements or degradation

## Known issues:

* `laguna-xs.2` is not yet supported on Windows/Linux.
* `llama3.2-vision` is not yet supported
* `nomic-embed-text` now converts inputs to lowercase per the model card where prior Ollama versions incorrectly preserved mixed case

## Installing:

**Mac/Linux**

```
curl -fsSL https://ollama.com/install.sh | OLLAMA_VERSION=0.30.0-rc31 sh
```

**Windows**

```
$env:OLLAMA_VERSION="0.30.0-rc31"; irm https://ollama.com/install.ps1 | iex
```
