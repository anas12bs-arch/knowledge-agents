---
title: "crewAIInc/crewAI 1.15.29 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.29"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-10-23T20:00:46Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.29"
---

# crewAIInc/crewAI 1.15.29 released

> Source: github-releases | Category: changelog | 2026-10-23T20:00:46Z

## crewAIInc/crewAI — 1.15.29

## What's Changed

### Features
- Add support for LiteLLM-compatible kwargs.
- Implement platform application search in CLI.
- Highlight action picker search in CLI.
- Trace conversation routes and public replies in flow.
- Select organization during login in CLI.
- Add offline jev routing and guardrail evaluation runner.
- Run integration app actions directly with call: tool.
- Promote AgentExecutor out of experimental status.
- Add Azure DocumentDB vector search integration.
- Add read-only notebook text loader and standard-library jsonl loader.
- Ensure crewAI eval keeps the evaluation's full data in the project.
- Enable crewAI eval to run the crew itself for verdict from one command.
- Allow crewAI eval to export evaluations as files.

### Bug Fixes
- Fix platform integration token derivation from login.
- Resolve logging issues by preserving JSON logs on serialization errors.
- Skip non-UTF-8 cached skill metadata.
- Fix tool actions to honor failure policies and get fresh usage budgets per kickoff.
- Prevent private memories without a source from leaking to every recall.
- Fix memory record retrieval order in LanceDBStorage.
- Restore task description when replanning fails.
- Stop agents from repeating the same tool call.
- Escape scope and id values in LanceDB filters.

### Documentation
- Update broken links in crewAI examples and observability guides.
- Fix dead links in tools documentation.

### Refactoring
- Refactor context compaction to be a BaseLLM capability.

## Contributors

@Akaliup, @Arxsher, @Copilot, @D41910, @LindseyZ1205, @RaycarlLei, @Rohitkanithi, @Sakura-798, @Vidit-Ostwal, @Wilson0511, @Winoren, @abdullahajaz14, @bballhaus, @gabemilani, @iris-clawd, @joaomdmoura, @leom1919, @lorenzejay, @marcreniel, @mattatcha, @reubenjrouse, @rohitkanithi, @sandeepsnairms, @stepchanges, @subhashpolisetti, @theCyberTech, @vatsalyd
