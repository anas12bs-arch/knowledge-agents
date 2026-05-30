---
title: "ollama/ollama v0.24.0 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.24.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-05-30T14:31:21Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.24.0"
---

# ollama/ollama v0.24.0 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:21Z

## ollama/ollama — v0.24.0

## Codex App

Ollama 0.24 includes support for the Codex App, OpenAI's desktop experience for working on Codex threads in parallel with built-in worktree support and git functionality.

```bash
ollama launch codex-app
```

<img width="2088" height="1404" alt="CleanShot 2026-05-14 at 15 04 18@2x" src="https://github.com/user-attachments/assets/53bd7997-19fd-4809-b8f2-b6ed284369c9" />


### Built-in browser
Codex can load local servers and sites in its built-in browser, enabling you to directly annotate on the page to request changes.

<img width="1073" height="668" alt="codex-annotate copy" src="https://github.com/user-attachments/assets/c9b762b3-83f2-47f1-8f28-d9eebc1bf5e0" />


### Review mode
Review code inside the app, leave comments, and iterate without leaving your workspace.

<img width="1137" height="696" alt="codex-comments copy 2" src="https://github.com/user-attachments/assets/56316d33-59ed-4f24-aaa7-a7c0310014c4" />

### Choosing a model

For difficult coding and agentic tasks:

- **kimi-k2.6** (with vision support)
- **glm-5.1**

For local use without an Ollama Cloud subscription:

- **nemotron-3-super**
- **gemma4:31b**
- **qwen3.6** 

### Restore anytime

To restore the previous configuration of Codex App, run:

```bash
ollama launch codex-app --restore
```

## What's Changed

* Reworked the MLX sampler for improved generation quality on Apple Silicon

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.23.0...v0.24.0

