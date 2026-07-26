---
title: "crewAIInc/crewAI 1.15.7a1 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.7a1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-07-26T17:33:50Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.7a1"
---

# crewAIInc/crewAI 1.15.7a1 released

> Source: github-releases | Category: changelog | 2026-07-26T17:33:50Z

## crewAIInc/crewAI — 1.15.7a1

## What's Changed

### Bug Fixes
- Fix registry skills resolution through the runtime's CrewAI+ client.
- Recover from the GPT-5.6 tools and reasoning_effort 400 errors.
- Make tool calling work on the Responses API path.
- Route responses-only models to prevent 404 errors.
- Bump bedrock-agentcore dependency to patch CVE-2026-16796.

### Observability
- Emit skill usage events at runtime for improved observability.

### Documentation
- Snapshot and changelog updates for version 1.15.6.

## Contributors

@alex-clawd, @joaomdmoura, @lorenzejay
