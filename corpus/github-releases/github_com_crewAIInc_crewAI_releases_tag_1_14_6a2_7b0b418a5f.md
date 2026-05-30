---
title: "crewAIInc/crewAI 1.14.6a2 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.14.6a2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-05-30T14:31:31Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.14.6a2"
---

# crewAIInc/crewAI 1.14.6a2 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:31Z

## crewAIInc/crewAI — 1.14.6a2

## What's Changed

### Features
- Enhance `StdioTransport` to prevent environment variable leakage
- Enhance planning configuration and observation handling
- Declare `env_vars` on `DatabricksQueryTool`
- Add Agent Control Plane documentation

### Bug Fixes
- Fix structured output leaks in tool-calling loops
- Drop unroundtrippable callbacks and adapter state in checkpointing
- Serialize `type[BaseModel]` fields as JSON schema in checkpointing
- Avoid orphan `task_started` on resume scope restore
- Allow `AgentExecutor` to restore from checkpoint
- Correct MongoDB typo to `pymongo` in package dependencies

### Documentation
- Restructure checkpointing page
- Document one-time admin package install step
- Migrate Secrets Manager / Workload Identity from replicated-config
- Remove Skills Repository entry from changelog

## Contributors

@github-actions[bot], @greysonlalonde, @heitorado, @iris-clawd, @lorenzejay, @lucasgomide, @mattatcha, @thiagomoretto, @vinibrsl
