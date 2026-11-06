---
title: "crewAIInc/crewAI 1.15.36 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.36"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-11-06T10:02:07Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.36"
---

# crewAIInc/crewAI 1.15.36 released

> Source: github-releases | Category: changelog | 2026-11-06T10:02:07Z

## crewAIInc/crewAI — 1.15.36

# What's Changed

### Features
- Add experimental conversational Agent sessions.
- Ask for a missing API key when crewai run starts.
- Record the error class when crewai run cannot load a project.
- Name the apps CrewAI AMP cannot resolve for an agent.

### Bug Fixes
- Fix async call execution in the caller's context for sync tools.
- Resolve issue with empty value precedence in the run's key check.
- Stop a JSON crew run cleanly when its API key is missing.
- Call GPT-6 Astra and GPT-6.1 Sol tools through the Responses API.
- Handle the sourcedAnswer output shape correctly.
- Drop None metadata values before writing to ChromaDB.
- Add the chosen provider's crewai extra to new projects.
- Pin crewai-files in the file-processing extra like its siblings.

### Documentation
- Update snapshot and changelog for v1.15.35.

## Contributors

@Kiko0301, @StoyanD, @joaomdmoura, @lorenzejay
