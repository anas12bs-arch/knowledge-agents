---
title: "crewAIInc/crewAI 1.15.19 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.19"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-09-04T14:28:12Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.19"
---

# crewAIInc/crewAI 1.15.19 released

> Source: github-releases | Category: changelog | 2026-09-04T14:28:12Z

## crewAIInc/crewAI — 1.15.19

## What's Changed

### Features
- Add Clipper integrations client
- Add `now()` to the CEL expression environment
- Record how a crew run ended for every user
- Report machine size as a coarse band, not a core count
- Add injectable client for CrewAI platform tools

### Bug Fixes
- Fix reading of octet-stream and xlsx URLs in `urlreadtool`
- Fix appending trailing user turn in native Gemini provider
- Normalize scheme and port in Ollama base URL
- Preserve reusable scope configs in memory
- Bump `pypdf` to 6.16.2 for security vulnerability
- Bump `nltk` to 3.10.3 for security vulnerability
- Fix native structured outputs for current Claude models and Snowflake CVE floor
- Run model call hooks on every path and propagate a deny

### Documentation
- Remove `CodeInterpreterTool` from AI/ML overview examples
- Point `prompt-template` link at its current path
- Update channels guide to current CopilotKit channels API
- Refresh retired Gemini model IDs

## Contributors

@Vidit-Ostwal, @a-yeyang, @github-actions[bot], @hvlcrs, @joaomdmoura, @kikifrost, @lorenzejay, @lucasgomide, @parthiban-sivakumar, @ranst91, @tandede, @thiagomoretto, @vinibrsl
