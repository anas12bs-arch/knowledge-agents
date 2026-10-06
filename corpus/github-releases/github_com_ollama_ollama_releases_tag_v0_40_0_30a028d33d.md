---
title: "ollama/ollama v0.40.0 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.40.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-10-06T19:54:00Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.40.0"
---

# ollama/ollama v0.40.0 released

> Source: github-releases | Category: changelog | 2026-10-06T19:54:00Z

## ollama/ollama — v0.40.0

## What's Changed

**Models run on MLX on Apple Silicon by default**

In this release, on Apple Silicon devices, model architectures supported by the MLX runtime will automatically run on MLX.

```
ollama pull qwen3.8
ollama run qwen3.8
```

Additional models include [gemma4](https://ollama.com/library/gemma4), [qwen3.6](https://ollama.com/library/qwen3.6) and [qwen3.5](https://ollama.com/library/qwen3.5)

Decision models are now available on MLX as well: [Nimble](https://ollama.com/library/nimble) [tev1](https://ollama.com/library/tev1)  [clef](https://ollama.com/library/clef) [clef-flash](https://ollama.com/library/clef-flash) 

MLX now has support for an embedding model: [embeddinggemma-2](https://ollama.com/library/embeddinggemma-2)

We will continue testing and enabling additional models.


**Full Changelog**: https://github.com/ollama/ollama/compare/v0.35.1...v0.40.0
