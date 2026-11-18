---
title: "crewAIInc/crewAI 1.15.42 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.42"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-11-18T23:02:09Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.42"
---

# crewAIInc/crewAI 1.15.42 released

> Source: github-releases | Category: changelog | 2026-11-18T23:02:09Z

## crewAIInc/crewAI — 1.15.42

## What's Changed

### Features
- Make ChromaDB an optional extra
- Default Knowledge to local Qdrant and decouple storage from ChromaDB
- Pick tools for standalone agents and add them later

### Bug Fixes
- Store output_json values as JSON to prevent date issues in .json and output_file
- Give each Flow its own ID from an initial_state instance
- Honor max_execution_time without waiting for the worker
- Save task outputs that hold URLs and other Pydantic types
- Read the experiment baseline as UTF-8
- Prefix sanitized tool names that start with a digit
- Count scoped LanceDB records exactly above 50,000 rows
- Report Serply's hybrid flag from its own field
- Let TavilyResearchTool's configured defaults apply
- Normalize flat Chroma metadata filters
- Handle CSV record newlines without translating cell values
- Load JSON crew and agent files saved with a UTF-8 BOM
- Preserve validated converter output in the configured format
- Read and write .env as UTF-8
- Keep a streamed delta when its chunk also carries usage
- Honor caller-provided Weaviate headers
- Exit with the UV status when crewai install fails
- Read pyproject.toml as UTF-8 in project helpers
- Accept an LLM mapping in agents.yaml
- Raise soupsieve floor to 4.0 for CVE-2026-126190

### Documentation
- Align crew endpoint path with runtime example
- Update FAQ links to AMP headings

## Contributors

@HhH666-ux, @Kiko0301, @Pranav-Singh-Devloper, @TejasLamba2006, @Varshith-Kali, @Vidit-Ostwal, @adityajai119, @ats3v, @bballhaus, @github-actions[bot], @iris-clawd, @jjhong011001, @lakers-abing, @lorenzejay, @lxcxjxhx, @xu-song
