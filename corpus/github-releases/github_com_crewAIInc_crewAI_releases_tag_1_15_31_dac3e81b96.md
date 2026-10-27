---
title: "crewAIInc/crewAI 1.15.31 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.31"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-10-27T22:20:59Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.31"
---

# crewAIInc/crewAI 1.15.31 released

> Source: github-releases | Category: changelog | 2026-10-27T22:20:59Z

## crewAIInc/crewAI — 1.15.31

## What's Changed

### Features
- Support conversational flow context compaction.

### Bug Fixes
- Update vulnerable audit dependencies.
- Stop sending 'stop' to GPT-6 and newer models.
- Run the provider listing off the loop in `acleanup_provider_files`.
- Emit `LLMGuardrailCompletedEvent` for a malformed guardrail result.
- Name the renamed integration token when it is missing.
- Fix path traversal in `output_file` via template interpolation.
- Patch deserialization, SQL injection, and path traversal vulnerabilities.
- Restore configured logging levels after suppression.
- Drop checkpoint resume state when copying a crew.
- Honor an injected `aioboto3` session in `BedrockFileUploader`.
- Use the right task slice with custom templates.
- Guard against storage listing failures in encoding flow analysis.
- Enforce guardrail result/error exclusivity with model validator.
- Filter categories server-side in Qdrant edge search.

### Documentation
- Use HTTPS for CrewAI AMP link in CLI concept documentation.
- Fix internal anchor links pointing to English slugs on translated pages.
- Fix `CrewBase` imports in documentation examples.

## Contributors

@Kiko0301, @Trenyx, @Velmet44, @Vidit-Ostwal, @Wilson0511, @gabemilani, @iris-clawd, @joaomdmoura, @lakers-abing, @leom1919, @lester076, @lorenzejay, @subhashpolisetti
