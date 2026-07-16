---
title: "crewAIInc/crewAI 1.15.3a1 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.3a1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-07-16T17:58:34Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.3a1"
---

# crewAIInc/crewAI 1.15.3a1 released

> Source: github-releases | Category: changelog | 2026-07-16T17:58:34Z

## crewAIInc/crewAI — 1.15.3a1

## What's Changed

### Features
- Add organization ID parameter to PlusAPI client.
- Add step interception points and rework execution hooks documentation around `@on`.
- Wire execution-boundary interception points.
- Add generic interception-hook dispatcher.
- Run declarative flows on the TUI (headless terminal fallback).
- Improve custom OpenAI URLs.

### Bug Fixes
- Fix null repository agent attributes.
- Fix `after_llm_call` hooks to prevent breaking native tool execution.
- Stop double-appending the turn reply when a handler trims history.
- Make tool-result caching opt-in instead of on by default.
- Stop rewriting the authored tool description at construction.
- Expose token usage under both names on agent and crew results.
- Report per-call usage metrics on kickoff results.
- Stop replaying the previous turn's intent when `route_turn()` returns falsy.
- Drain memory writes before kickoff and flow completion events.

### Documentation
- Group execution hooks and document all hook contexts.
- Update documentation for execution hooks.

## Contributors

@joaomdmoura, @lorenzejay, @lucasgomide, @vinibrsl
