---
title: "crewAIInc/crewAI 1.14.7 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.14.7"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-06-12T11:32:20Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.14.7"
---

# crewAIInc/crewAI 1.14.7 released

> Source: github-releases | Category: changelog | 2026-06-12T11:32:20Z

## crewAIInc/crewAI — 1.14.7

## What's Changed

### Features
- Add pluggable default backends for memory, knowledge, rag, and flow.
- Surface real finish_reason, sampling params, and response.id on LLM events.
- Type DSL triggers as route-aware decorators.
- Add chat API for conversational flows.
- Make locking backend overridable.
- Build FlowDefinition from Flow DSL metadata.
- Add native Snowflake Cortex LLM provider.
- Add crew trained agents file support.

### Bug Fixes
- Fix checkpoint to rebuild custom BaseLLM as concrete LLM on restore.
- Gate restore on a flag to prevent live snapshots from replaying as resume.
- Scope runtime state per run to bound growth and isolate concurrent runs.
- Fix telemetry setup on crewai-login.
- Respect suppress_flow_events for method-execution events.
- Restore [project.scripts] in crewai package for uv tool install.
- Resolve pip-audit CVEs for aiohttp, docling, and docling-core.
- Fix file input not working reliably.
- Fix Snowflake Claude incomplete tool result histories.

### Documentation
- Update changelog and version for v1.14.7.
- Update OpenTelemetry collector documentation.
- Update NVIDIA Nemotron LLM guide.
- Add Databricks integration guide.
- Add Snowflake integration guide.

### Performance
- Improve crewai import speed by lazy-loading docling imports.

### Refactoring
- Simplify flow condition evaluation to be stateless per event.
- Decouple convo logic from runtime and add a conversational_definition.
- Split `flow.py` into DSL, definition, and runtime.

## Contributors

@Luzk, @alex-clawd, @devin-ai-integration[bot], @greysonlalonde, @gvieira, @jessemiller, @lorenzejay, @lucasgomide, @mattatcha, @vinibrsl
