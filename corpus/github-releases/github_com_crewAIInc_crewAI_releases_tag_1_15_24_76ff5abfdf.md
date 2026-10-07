---
title: "crewAIInc/crewAI 1.15.24 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.24"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-10-07T21:25:08Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.24"
---

# crewAIInc/crewAI 1.15.24 released

> Source: github-releases | Category: changelog | 2026-10-07T21:25:08Z

## crewAIInc/crewAI — 1.15.24

## What's Changed

### Features
- Add crewai eval to print a markdown brief when run by an agent
- Queue relevant background replies
- Add experimental turn and reply identities
- Add Oracle Integrations
- Add experimental job lifecycle and runner
- Add crewai eval --models, and llm_overlay to swap models as well as roles

### Bug Fixes
- Fix train filename error message in CLI
- Allow a start step to re-run on the events it listens to
- Let human_feedback emit steps expose the review in outputs
- Ensure crewai eval exits with code 1 unless the gate passed and prompt to log in when nothing was traced unattended
- Report tracing sent usage from the grant exporter
- Address multiple dependency advisories and update relevant packages

### Refactoring
- Move message summarization into SummarizeMessages
- Centralize and refresh context windows

## Contributors

@Velmet44, @Vidit-Ostwal, @dependabot[bot], @fileames, @gabemilani, @github-actions[bot], @joaomdmoura, @lorenzejay
