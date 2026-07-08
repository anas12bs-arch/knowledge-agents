---
title: "crewAIInc/crewAI 1.15.2 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-07-08T04:27:13Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.2"
---

# crewAIInc/crewAI 1.15.2 released

> Source: github-releases | Category: changelog | 2026-07-08T04:27:13Z

## crewAIInc/crewAI — 1.15.2

## What's Changed

### Features
- Pull latest LLM models dynamically in the crew wizard.
- Support inline skill definitions.
- Add generated Flow Definition authoring skill.
- Support templated Flow action inputs.
- Add text helper for flow CEL prompts.
- Add text helper to flow skill example.
- Implement message setup and feedback handling in AgentExecutor.
- Add repository agents to flow definitions.
- Define stream frame protocol for flows.
- Type tool and app in CrewDefinition.
- Repoint template commands to crewAIInc-fde org.

### Bug Fixes
- Key model-catalog cache by exact API key, shorten TTL, and skip Ollama.
- Unify `crewai run` flow input resolution and prompt from the state schema.
- Resolve pip-audit failures for onnx 1.22.0 and nltk PYSEC-2026-597.
- Ensure we are writing version for flows.
- Include aiobotocore in the bedrock extra.
- Reject self-listening flow methods.
- Cut docs version nav from Edge so new pages aren't dropped.

### Documentation
- Update language from Rules to Policies to match new dashboard changes.
- Document flow agent options.
- Add streaming docs to the navigation.
- Document Cost Limit rule type in Agent Control Plane.
- Drop CREWAI_LOG_FORMAT references from Datadog guide.

## Contributors

@akaKuruma, @danielfsbarreto, @github-code-quality[bot], @joaomdmoura, @lorenzejay, @lucasgomide, @manisrinivasan2k1, @renatonitta, @vinibrsl
