---
title: "crewAIInc/crewAI 1.15.28 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.28"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-10-14T05:33:00Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.28"
---

# crewAIInc/crewAI 1.15.28 released

> Source: github-releases | Category: changelog | 2026-10-14T05:33:00Z

## crewAIInc/crewAI — 1.15.28

## What's Changed

### Features
- Add crewai eval command to report where a stopped model broke.
- Use LiteLLM catalog for context windows.

### Bug Fixes
- Fix flow to learn from resumed human feedback and preserve reviewed output types.
- Warn when non-empty apps resolve to zero platform tools.
- Fix flow add-crew to correctly find the package from pyproject.
- Show reasons for deployment failures and fix deploy remove and lockfile checks.
- Fix trigger list and payload requests timeout to 60 seconds.
- Read AMP's source_type during deploy push to ensure ZIP deployments use the new code.
- Decode local JSON files with UTF-8 BOM in rag.
- Allow image input_files for OpenAI GPT-6 Sol/Luna/Astra.
- Emit call completed event for streamed anthropic tool calls.
- Stop JSON-schema models from warning about BaseModel-shadowing fields.
- Preserve native tool aborts and post-hook cache identity.
- Refresh LiteLLM catalog after the version-bump PR merges.
- Repair rotted evaluator regression tests.

### Documentation
- Consolidate improvements in MongoDB documentation.
- Correct deploy and platform-tool guidance in AGENTS.md.
- Fix README imports for RagTool and XMLSearchTool.

## Contributors

@SIDDARTHAREDDY8, @Vidit-Ostwal, @joaomdmoura, @kimnamu, @lorenzejay, @norareidy, @shaikn6, @zouyonghe
