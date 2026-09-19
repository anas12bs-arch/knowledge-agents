---
title: "ollama/ollama v0.34.3-rc0 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.34.3-rc0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-09-19T00:46:39Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.34.3-rc0"
---

# ollama/ollama v0.34.3-rc0 released

> Source: github-releases | Category: changelog | 2026-09-19T00:46:39Z

## ollama/ollama — v0.34.3-rc0

## What's Changed

`GET /api/show` now advertises each model's thinking controls and default:
```sh 
curl http://localhost:11434/api/show -d '{"model": "glm-5.3-flash:cloud"}'
```
```json
{
  "thinking": {
    "values": ["low", "high", "max"],
    "default": "max"
  }
}
```
* **Nemotron H** vision models are now supported on Apple Silicon with MLX
* Ollama's macOS app will now no longer reopen windows you've closed when activating it

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.34.2...v0.34.3-rc0
