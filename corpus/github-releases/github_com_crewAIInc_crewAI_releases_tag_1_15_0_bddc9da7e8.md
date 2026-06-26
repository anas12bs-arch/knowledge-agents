---
title: "crewAIInc/crewAI 1.15.0 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-06-26T00:22:22Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.0"
---

# crewAIInc/crewAI 1.15.0 released

> Source: github-releases | Category: changelog | 2026-06-26T00:22:22Z

## crewAIInc/crewAI — 1.15.0

## What's Changed

### Features
- Track conversational flow turn usage in telemetry
- Support conversational flows in the CLI TUI
- Add unified declarative flow loading
- Add declarative Flow CLI support
- Add optional if expression to each.do steps
- Add single agent action to Flow definitions
- Add crew actions to FlowDefinition
- Add inline crew definition loading
- Add `each` composite action to FlowDefinition
- Implement DMN mode support in crew creation and execution

### Bug Fixes
- Fix owner-only permissions enforcement on credential files
- Fix JSON schema flow state kickoff inputs
- Fix symlink path traversal in skill archive extraction
- Aggregate token usage across all LLM calls
- Remove duplicated Exa tool
- Resolve JSON crew issues
- Fix JSON crew handling and enhance memory reset functionality

### Documentation
- Update installation and quickstart documentation for JSON-first crew projects
- Add Datadog integration guide with importable operations dashboard
- Add "One Card per Step" Studio page
- Add snapshots and changelogs for previous versions leading to v1.15.0

### Performance
- Improve crewai run startup UX
- Keep flow method progress visible for nested crews

### Refactoring
- Remove `StateProxy` from flow state access
- Consolidate `crewai run` and `crewai flow kickoff`
- Discriminate FlowDefinition state types
- Wire config and persistence from FlowDefinition into the runtime

## Contributors

@gabemilani, @github-code-quality[bot], @greysonlalonde, @iris-clawd, @jessemiller, @joaomdmoura, @lorenzejay, @lucasgomide, @theCyberTech, @vinibrsl
