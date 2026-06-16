---
title: "ollama/ollama v0.30.8 released"
url: "https://github.com/ollama/ollama/releases/tag/v0.30.8"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ollama"]
date: "2026-06-16T18:13:18Z"
metadata:
  repo: "ollama/ollama"
  version: "v0.30.8"
---

# ollama/ollama v0.30.8 released

> Source: github-releases | Category: changelog | 2026-06-16T18:13:18Z

## ollama/ollama — v0.30.8

## What's Changed
* Fixed `ollama launch` selecting the wrong provider in some cases
* Improved prompt caching by decoupling it from context shift for better KV cache reuse
* More stable MLX inference with hardened linear and embedding layers
* MLX runner now creates snapshots during prompt processing and speculative decoding for improved reliability
* Improved recurrent model support with per-boundary states from the gated-delta kernels

**Full Changelog**: https://github.com/ollama/ollama/compare/v0.30.7...v0.30.8
