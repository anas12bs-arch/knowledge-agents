---
title: "crewAIInc/crewAI 1.15.18 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.18"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-08-28T00:54:29Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.18"
---

# crewAIInc/crewAI 1.15.18 released

> Source: github-releases | Category: changelog | 2026-08-28T00:54:29Z

## crewAIInc/crewAI — 1.15.18

## What's Changed

### Features
- Promote conversational flows to stable
- Record a created deployment with the given UUID
- Enhance conversational flow documentation and APIs
- Let a declaration name the router's response format
- Let a chat flow declare its own state shape
- Accept crew-style LLM config in a conversational declaration
- Report project creation with the minted ID
- Record whether a run had inputs, without recording the inputs
- Backfill project ID from every user-invoked project command

### Bug Fixes
- Preserve tool results when the final answer is empty
- Map default Claude Sonnet 4.6 to its 1M context window
- Raise Anthropic default max_tokens for large tool calls
- Render message content parts as text, not as a Python repr
- Keep message roles when Agent.kickoff gets a conversation
- Skip interception hooks on crewai-internal flows
- Record task failures as failures, not successes
- Emit the flow lifecycle on a suppressed resume
- Open the conversational TUI for a declarative chat flow
- Record crew_memory as a string, not a bool
- Always emit project_id so absent and empty stay distinct

### Documentation
- Clarify Arize Phoenix observability docs

## Contributors

@Vidit-Ostwal, @arizedatngo, @joaomdmoura, @lorenzejay, @lucasgomide
