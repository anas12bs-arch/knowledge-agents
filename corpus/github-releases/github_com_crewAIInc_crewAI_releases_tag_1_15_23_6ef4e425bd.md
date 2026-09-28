---
title: "crewAIInc/crewAI 1.15.23 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.23"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-09-28T23:55:32Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.23"
---

# crewAIInc/crewAI 1.15.23 released

> Source: github-releases | Category: changelog | 2026-09-28T23:55:32Z

## crewAIInc/crewAI — 1.15.23

## What's Changed

### Features
- Add support for native Gemini 3.8 Flash
- Implement evaluation of the last traced run through AMP in crewai eval
- Record the last traced run for crewai eval instead of printing it
- Improve platform integration setup UX
- Prioritize popular platform integrations
- Enhance tracing task spans to include declared output format and results

### Bug Fixes
- Fix visibility of the panel for viewing traces
- Resolve issue with turning tracing on and add an Evaluate button in the TUI
- Retry throttled provider calls in LLM
- Fall back to synchronous calls from acall in Bedrock
- Print areas graded by the evaluation in CLI
- Ensure link is shown after finalizing traces
- Keep Selenium driver reusable
- Close S3 response bodies properly
- Collapse multimodal content with shared helper
- Match roles in LLM overlay that differ only by surrounding whitespace
- Close SQLite connections in flow persistence and SQLite provider
- Preserve directory listing paths

### Documentation
- Update guides for assistants to platform tools

## Contributors

@Copilot, @Mairaarshad19, @SharoonSharif, @Vidit-Ostwal, @gaoanze888, @joaomdmoura, @lorenzejay, @sclfcz, @stepchanges, @vinibrsl
