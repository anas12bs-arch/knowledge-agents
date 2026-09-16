---
title: "crewAIInc/crewAI 1.15.22 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.22"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-09-16T22:22:14Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.22"
---

# crewAIInc/crewAI 1.15.22 released

> Source: github-releases | Category: changelog | 2026-09-16T22:22:14Z

## crewAIInc/crewAI — 1.15.22

## What's Changed

### Features
- Support aliases as connection identifiers
- Record reasons for deployment creation failures
- Collect human feedback and pause events in tracing
- Add `llm_overlay` context variable to route agent roles to models
- Carry `task_prompt` and output in agent execution payloads
- Validate platform integrations during crew setup
- Add platform tools to JSON crew wizard
- Expose CrewAI Platform application catalog
- Add OpenRouter as a supported embedding provider

### Bug Fixes
- Accept CRLF in inline skill definitions
- Load text file URLs through the safe fetcher
- Close SQLite connections in kickoff task outputs storage
- Carry `from_cache` on the native tool path's `ToolUsageFinishedEvent`
- Raise `ValueError` instead of bare raise in uploader
- Support non-primitive types in SQLiteFlowPersistence
- Improve coding agents instructions
- Read JSON checkpoints as UTF-8
- Overwrite stale `poetry.lock` backup on Windows
- Key streamed tool calls by wire index in Azure
- Preserve file data content parts in Gemini
- Honor `read_only` on `update()` and `recall()` access times
- Send `reasoning_effort` to every OpenAI reasoning model
- Prevent crashes in the run TUI when streamed output contains a literal `[...]`
- Reject replay when stored tasks differ
- Use `sys.platform` guards for mypy compatibility on Windows
- Request the forced final answer as a user turn
- Keep null in the task output schema embedded in the prompt
- Align `DOCXSearchTool` with standard RAG fixed schema pattern

### Documentation
- Add `xpu` to embedding device options
- List all workspace packages

## Contributors

@ASTion24, @BlueX888, @HUAN2022A, @RaycarlLei, @Rohitkanithi, @SWAPI03, @SharoonSharif, @ShivangiRay, @Theater-ahyeon, @Vidit-Ostwal, @gamal1osama, @github-actions[bot], @joaomdmoura, @lorenzejay, @mhbuehler, @modusensus, @monkscode, @rohitkanithi, @roli-lpci, @vinibrsl, @wangtaotaotao95
