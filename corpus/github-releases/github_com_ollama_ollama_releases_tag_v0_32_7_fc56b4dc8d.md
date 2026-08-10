---
title: "ollama/ollama v0.32.7 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.32.7"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-08-10T10:53:55Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.32.7"
---

# ollama/ollama v0.32.7 released

> Source: github-releases | Category: changelog | 2026-08-10T10:53:55Z

## ollama/ollama — v0.32.7

## Muse Glimmer

**Muse Glimmer**, Meta's newest open model and the first released by Meta Superintelligence Labs, is now available on Ollama. It's a 30B multimodal model purpose-built for agent workloads that run locally.

With Ollama, you can now use Muse Glimmer to power coding agent applications such as Claude Code, Codex, Pi and more, as well as long-running personal assistants such as OpenClaw and Hermes.

Ollama's MLX engine provides state-of-the-art performance on Apple Silicon for this model, with support for DFlash and image input as of Ollama 0.32.7.

To download and run Muse Glimmer locally:

```bash
ollama run muse-glimmer:30b-mlx
```

> Note: Muse Glimmer is currently supported via Ollama's MLX engine on Apple Silicon. Support for NVIDIA, AMD, and other platforms will be available shortly.

To run Muse Glimmer on Apple Silicon with Claude Code, [download Ollama](https://ollama.com/download) and run:

```bash
ollama launch claude --model muse-glimmer:30b-mlx
```

For a lighter-weight coding agent, try [Pi](https://pi.dev):

```bash
ollama launch pi --model muse-glimmer:30b-mlx
```

For personal assistant frameworks such as OpenClaw and Hermes, use:

```bash
ollama launch openclaw --model muse-glimmer:30b-mlx
```

```bash
ollama launch hermes --model muse-glimmer:30b-mlx
```

