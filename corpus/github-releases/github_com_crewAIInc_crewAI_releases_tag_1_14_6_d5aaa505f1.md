---
title: "crewAIInc/crewAI 1.14.6 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.14.6"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-05-30T14:31:31Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.14.6"
---

# crewAIInc/crewAI 1.14.6 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:31Z

## crewAIInc/crewAI — 1.14.6

## What's Changed

### Features
- Enhance StdioTransport to prevent environment variable leakage
- Enhance planning configuration and observation handling
- Declare env_vars on DatabricksQueryTool
- Add Agent Control Plane docs

### Bug Fixes
- Fix structured output leaks in tool-calling loops
- Drop unroundtrippable callbacks and adapter state in checkpoint
- Serialize type[BaseModel] fields as JSON schema in checkpoint
- Avoid orphan task_started on resume scope restore
- Allow AgentExecutor to restore from checkpoint
- Correct mongodb typo to pymongo in package_dependencies

### Documentation
- Add ACP (Beta) docs navigation block to Agent Control Plane pages
- Remove consensual process references from processes page
- Restructure checkpointing page
- Document one-time admin package install step
- Migrate Secrets Manager / Workload Identity from replicated-config
- Remove {" "} JSX expressions breaking <Steps> render

### Refactoring
- Move Skills Repository to experimental + CREWAI_EXPERIMENTAL gate

## Contributors

@akaKuruma, @alex-clawd, @github-actions[bot], @greysonlalonde, @heitorado, @iris-clawd, @lorenzejay, @lucasgomide, @mattatcha, @thiagomoretto, @vinibrsl
