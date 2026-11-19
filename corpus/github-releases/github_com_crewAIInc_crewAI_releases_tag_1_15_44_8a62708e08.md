---
title: "crewAIInc/crewAI 1.15.44 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.44"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-11-19T20:55:56Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.44"
---

# crewAIInc/crewAI 1.15.44 released

> Source: github-releases | Category: changelog | 2026-11-19T20:55:56Z

## crewAIInc/crewAI — 1.15.44

## What's Changed

### Features
- Add capability to save files as versioned, shareable artifacts.

### Bug Fixes
- Fix inline agent and crew action references relative to the flow file.
- Stop duplicating kept separators when merging chunks.
- Isolate nested defaults from a shared flow declaration.
- Restrict Pillow to PNG, JPEG, GIF, and WEBP when opening images.
- Reset cache eviction order on clear.
- Treat a docs path on GitHub as a repository.
- Exit with the script's status when crewai train fails.
- Relax av pin to ensure current FFmpeg installs.
- Keep a deeply nested span that the run app cannot render as text in one step.
- Stop stamping cache_control on every anthropic file block.
- Detect vision for any Claude 3+ model and geo profile.
- Export structured output from non-str guardrail results.
- Enforce cwd containment for all FilePath paths.

### Documentation
- Teach the flow skill to save and read artifacts.

## Contributors

@HanYuanLu, @Kiko0301, @Vidit-Ostwal, @adityajai119, @anilkr09, @gabemilani, @joaomdmoura, @kuquert, @nurlanmnn, @willnhansen
