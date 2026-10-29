---
title: "crewAIInc/crewAI 1.15.33 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.33"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-10-29T08:44:18Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.33"
---

# crewAIInc/crewAI 1.15.33 released

> Source: github-releases | Category: changelog | 2026-10-29T08:44:18Z

## crewAIInc/crewAI — 1.15.33

## What's Changed

### Features
- Add `crewai skill search` to list the organization's skills
- Pass `crewai run --inputs` to a Python flow
- Add `deploy create --zip` and print the commit a zip is built from

### Bug Fixes
- Report token usage for LiteLLM tool-call and structured-output calls
- Restore recent backwards-compatible imports and token
- Let the JSON crew runner load against an older crewai-core
- Keep deeply nested JSON as text in the run TUI on Python 3.12
- Export `persist` from `crewai.flow.flow`
- Load JSON crews in `crewai chat`
- Treat an env tracing `false` as off in `is_tracing_enabled`
- Exit with guidance when a Python conversational flow has no terminal
- Exit 1 when a crewai+ command needs a login
- Return the post from the flow scaffold's last step
- Make `crewai update` print upgrade commands instead of rewriting uv projects
- Keep module identity when rebuilding forward-ref namespaces in flows
- Wait the full device-code lifetime at login and exit 1 on timeout
- Show AMP's reason on a 401 and let the run app's deploy log in again
- Save unrestorable checkpoint callbacks as null instead of breaking restore
- Load `from_repository` set inside an agent's config
- Stop the Rich live panel repainting into redirected logs

### Documentation
- Document agent planning with `PlanningConfig` and migrate the reasoning page

### CI & Tests
- Run the lib/cli, crewai-core and crewai-files tests in the PR matrix
- Respect maintainer PR reopen actions
- Stabilize flaky CLI memory and tracing/telemetry tests

## Contributors

@Vidit-Ostwal, @alexmarchenko-crewai, João Moura

