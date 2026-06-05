---
title: "crewAIInc/crewAI 1.14.7a2 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.14.7a2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-06-05T22:46:03Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.14.7a2"
---

# crewAIInc/crewAI 1.14.7a2 released

> Source: github-releases | Category: changelog | 2026-06-05T22:46:03Z

## crewAIInc/crewAI — 1.14.7a2

## What's Changed

### Features
- Add conversational flow traces support.
- Update conversational flow documentation to utilize `handle_turn`.
- Surface real `finish_reason`, sampling parameters, and `response.id` in LLM events.
- Type DSL triggers as route-aware decorators.
- Implement chat API for conversational flows.
- Make locking backend overridable in lock store.
- Split flow DSL monolith into focused decorator modules.
- Flatten LiteLLM cache/reasoning usage sub-counts in `_usage_to_dict`.
- Build `FlowDefinition` from Flow DSL metadata.

### Documentation
- Add NVIDIA Nemotron LLM guide.
- Document monorepo deployments.
- Update changelog and version for v1.14.7a1.

## Contributors

@alex-clawd, @gvieira, @lorenzejay, @lucasgomide, @mattatcha, @vinibrsl
