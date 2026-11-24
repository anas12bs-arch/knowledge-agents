---
title: "crewAIInc/crewAI 1.15.45 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.45"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-11-24T04:27:40Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.45"
---

# crewAIInc/crewAI 1.15.45 released

> Source: github-releases | Category: changelog | 2026-11-24T04:27:40Z

## crewAIInc/crewAI — 1.15.45

## What's Changed

### Features
- Add ability to save HTML or markdown output as a PDF artifact.

### Bug Fixes
- Fix dependency issue by bumping e2b for Python >=3.11 to pull patched wcmatch.
- Wrap file-like inputs in `normalize_input_files`.
- Reject negative checkpoint prune retention counts.
- Report MongoDB tool's real environment variables.
- Enable Bedrock S3 uploads with `prefer_upload`.
- Validate foreign models against the target schema.
- Preserve narrow dimensions when resizing images.
- Reject empty credentials and use constant-time comparison in server authentication.
- Make `HyperbrowserLoadTool` parameters optional in its schema.
- Keep fields with explicit non-null defaults as non-nullable.
- Maintain a streamed Azure delta when its chunk also carries usage.
- Reject non-positive text chunk sizes.
- Drop credentials on cross-origin redirects.
- Stop chunking once a chunk reaches the end of the text.
- Serialize enums by value in `CrewJSONEncoder`.
- Never cache `save_artifact` tool results.
- Set `from_cache` on the native tool finished event.

### Documentation
- Document that anthropic file blocks carry no cache control.

## Contributors

@Ayushraj06-bit, @Kelvin-Waititu, @Kiko0301, @MaiAditya, @SDLSY, @Sakura-798, @Vidit-Ostwal, @YeChenglin8888, @gabemilani, @houyunsun, @jjhong011001, @joaomdmoura, @kushagra0526, @lkuko, @nazek52, @nurlanmnn
