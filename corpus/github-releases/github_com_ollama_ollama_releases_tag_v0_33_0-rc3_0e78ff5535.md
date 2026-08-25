---
title: "ollama/ollama v0.33.0-rc3 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.33.0-rc3"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-08-25T04:23:20Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.33.0-rc3"
---

# ollama/ollama v0.33.0-rc3 released

> Source: github-releases | Category: changelog | 2026-08-25T04:23:20Z

## ollama/ollama — v0.33.0-rc3

## What's Changed

### Claude Desktop

* Turn individual Ollama models on or off for use in Claude, directly from the menu bar
* Choose from your available Ollama models from within Claude; cloud models appear only when you're signed in
* A new **Apps** view manages app integrations with copyable commands

### Improved caching

* Fixed a hang where agent clients that cancel long prefills
* Prefill restore points are now trustworthy by construction: a cancelled prefill keeps every restore point it crossed, so retries resume where they stopped instead of restarting from scratch
* Resumed prefills no longer record restore points that fail to cover what they claim; on models with recurrent layers this previously forced a request matching 46k of 47k tokens to reprocess from zero
* Disabled Claude Code's "tokens left" token-countdown system message, which Ollama moved to the front of the prompt and broke the KV cache on every request

### Other improvements

* DeepSeek Harness launcher now falls back to `npx` when the global npm install fails, with Windows command-shim support
* Onboarding flow has clearer introductory copy, a macOS header aligned with the native traffic-light controls, and Cmd/Ctrl zoom shortcuts disabled during onboarding so the fixed window keeps its intended scale
* MLX dependency update (#17886)
* Fixed broken default packaging caused by macOS-specific assumptions affecting Linux/Windows builds
* Fixed the Apps header overlapping the macOS traffic lights during sidebar open transitions by synchronizing the header padding animation with the sidebar width animation 

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.32.15...v0.33.0-rc2
