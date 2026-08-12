---
title: "ollama/ollama v0.32.10-rc1 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.32.10-rc1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-08-12T23:10:20Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.32.10-rc1"
---

# ollama/ollama v0.32.10-rc1 released

> Source: github-releases | Category: changelog | 2026-08-12T23:10:20Z

## ollama/ollama — v0.32.10-rc1

## What's Changed
- Models that don't set a `repeat_penalty` now default to 1.0 (off) instead of 1.1, matching other engines and speeding up speculative decoding; set a per-model parameter if an older model repeats itself.
- Faster prefill on NVFP4 MLX models with a global scale, about 7–8% on Qwen3.6 and Muse Glimmer.
- Fixed blob verification being skipped when an OCI manifest's config and layer share a digest.

## New Contributors
* @vigneshakaviki made their first contribution in https://github.com/ollama/ollama/pull/15504

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.32.8...v0.32.10-rc1
