---
title: "crewAIInc/crewAI 1.14.7a1 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.14.7a1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-06-03T23:16:22Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.14.7a1"
---

# crewAIInc/crewAI 1.14.7a1 released

> Source: github-releases | Category: changelog | 2026-06-03T23:16:22Z

## crewAIInc/crewAI — 1.14.7a1

## What's Changed

### Features
- Add crew trained agents file support
- Add native Snowflake Cortex LLM provider
- Add Databricks integration guide
- Add Snowflake integration guide

### Bug Fixes
- Fix CLI by restoring `[project.scripts]` in crewai package for UV tool install
- Resolve file input reliability issues
- Fix incomplete tool result histories in Snowflake Claude
- Handle stringified tool calls for Snowflake Claude
- Re-arm multi-source `or_` listeners across router-driven cycles

### Performance
- Improve crewai import speed by lazy-loading docling imports

### Refactoring
- Split `flow.py` into DSL, definition, and runtime

## Contributors

@Luzk, @alex-clawd, @devin-ai-integration[bot], @greysonlalonde, @jessemiller, @lorenzejay, @vinibrsl
