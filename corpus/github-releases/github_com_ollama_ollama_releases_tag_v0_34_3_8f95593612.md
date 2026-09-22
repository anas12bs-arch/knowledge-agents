---
title: "ollama/ollama v0.34.3 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.34.3"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-09-22T21:29:11Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.34.3"
---

# ollama/ollama v0.34.3 released

> Source: github-releases | Category: changelog | 2026-09-22T21:29:11Z

## ollama/ollama — v0.34.3

## What's Changed

`GET /api/show` now advertises each model's thinking controls and default:

Available in the CLI with:
```
ollama show gemma4
```

```
    thinking
        levels     false, true
        default    true
```

Available in the API with:
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

Also available on ollama.com directly for cloud models.

* **Nemotron H** vision models are now supported on Apple Silicon with MLX
* Ollama's macOS app will now no longer reopen windows you've closed when activating it
* Fix for model pulls from HuggingFace

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.34.2...v0.34.3
