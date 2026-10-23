---
title: "ollama/ollama v0.40.9 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.40.9"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-10-23T16:18:56Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.40.9"
---

# ollama/ollama v0.40.9 released

> Source: github-releases | Category: changelog | 2026-10-23T16:18:56Z

## ollama/ollama — v0.40.9

## Speech

Ollama can now generate [speech](https://docs.ollama.com/capabilities/speech) with Phonon on Apple Silicon. `ollama run` plays text or a chat model's reply aloud as the audio is generated, and apps can stream audio through the OpenAI-compatible `/v1/audio/speech` endpoint.

```sh
ollama run phonon "Hello from Ollama."
```

## d3 decision models

[d3](https://ollama.com/library/d3) brings vLLM Semantic Router's decision models to Ollama. Give a model text, structured state, or an image, and ask it to classify, answer yes or no, or score options with probabilities. The family includes 2B, 4B, 9B, and 27B sizes.

```sh
ollama run d3 "A customer says their card was charged twice." --ask "Is this a billing issue?"
```

## Flint on Linux and Windows

[Flint](https://ollama.com/library/flint) now runs on Linux and Windows as well as macOS.

## Other improvements

- Streaming OpenAI Responses and Anthropic Messages requests now report generation failures instead of ending silently after partial output.
- `ollama launch` now passes cloud models' context lengths and capabilities to coding tools, fixing incorrect context and compaction settings.
- Anthropic-compatible web search now uses the model's supported thinking setting in follow-up requests, preventing avoidable failures.

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.8...v0.40.9
