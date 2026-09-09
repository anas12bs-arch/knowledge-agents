---
title: "crewAIInc/crewAI 1.15.21 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.21"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-09-09T23:54:49Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.21"
---

# crewAIInc/crewAI 1.15.21 released

> Source: github-releases | Category: changelog | 2026-09-09T23:54:49Z

## crewAIInc/crewAI — 1.15.21

## What's Changed

### Features
- Add telemetry to track checkpoint runtime and CLI usage.

### Bug Fixes
- Fix gateway errors reported inside an HTTP 200 response.
- Keep deploy push on the AMP create source.
- Report scrape failures instead of raising IndexError in the Oxylabs integration.
- Route all DashScope models through the native provider.
- Persist JSON checkpoints as UTF-8.
- Drop stray $ in f-string search URLs for BrightData.
- Support list-form type arrays in JSON schema conversion.
- Correct gpt-4o-mini context window from 200000 to 128000.
- Preserve streaming tool call arguments at contentBlockStop.
- Make pre-commit hooks portable on Windows.

### Documentation
- Clarify that tracing is managed separately from telemetry.
- Fix parallel search reference link.
- Remove stale parameters from handle_llm_stream_chunk docstring.
- Fix streaming output docstring examples.
- Use organization UUIDs in the skill install reference.

## Contributors

@Alphaxiaoteng, @DrewWhittleNZ, @Ghraven, @Shxiao101, @Vaishnavi220506, @Vidit-Ostwal, @danielfsbarreto, @georgeatparallel, @github-actions[bot], @jessemiller, @joaomdmoura, @kimnamu, @kiwoongyoon, @liang0417, @lorenzejay, @oxy-giedrius, @simpleqt, @uoparaji
