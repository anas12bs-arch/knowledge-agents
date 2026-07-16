---
title: "crewAIInc/crewAI 1.15.3 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.3"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-07-16T20:07:27Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.3"
---

# crewAIInc/crewAI 1.15.3 released

> Source: github-releases | Category: changelog | 2026-07-16T20:07:27Z

## crewAIInc/crewAI — 1.15.3

## What's Changed

### Features
- Add organization ID parameter to PlusAPI client
- Add step interception points and rework execution hooks documentation around @on
- Wire execution-boundary interception points
- Add generic interception-hook dispatcher
- Run declarative flows on the TUI (headless terminal fallback)

### Bug Fixes
- Sync kickoff-completed event with OUTPUT hook result
- Fix null repository agent attributes
- Ensure after_llm_call hooks do not break native tool execution
- Avoid double-append of the turn reply when a handler trims history
- Make tool-result caching opt-in instead of on by default
- Stop rewriting the authored tool description at construction
- Expose token usage under both names on agent and crew results
- Report per-call usage metrics on kickoff results
- Stop replaying previous turn's intent when route_turn() returns falsy

### Documentation
- Update execution hooks grouping and document all hook contexts

## Contributors

@joaomdmoura, @lorenzejay, @lucasgomide, @vinibrsl
