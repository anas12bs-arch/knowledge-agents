---
title: "crewAIInc/crewAI 1.15.34 released"
url: "https://github.com/crewAIInc/crewAI/releases/tag/1.15.34"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "crewAI"]
date: "2026-11-01T23:52:45Z"
metadata:
  repo: "crewAIInc/crewAI"
  version: "1.15.34"
---

# crewAIInc/crewAI 1.15.34 released

> Source: github-releases | Category: changelog | 2026-11-01T23:52:45Z

## crewAIInc/crewAI — 1.15.34

## What's Changed

### Features
- Add standalone LiteLLM catalog PR before version bump
- Record where crewai run stops before kickoff
- Add crewai skill search to list the organization's skills
- Pass crewai run --inputs to a Python flow
- Add deploy create --zip and print the commit a zip is built from
- Document agent planning with planningconfig and migrate reasoning page

### Bug Fixes
- Stop offering shut-down Gemini models in crewai create
- Raise MissingAPIKeyError for OpenAI-compatible providers
- Count repeated tool call stops in anonymous telemetry
- Count a crewai run whose project script fails
- Let crewai[litellm] import on Python 3.10; raise joserfc, pyasn1, pypdf floors
- Retry an empty LLM answer once and raise a typed error
- Ask for structured output when a tool-using agent finishes
- Refactor JSON that does not match the output model instead of failing
- Warn on repeated tool calls and keep the work when stopping
- Honor context_window_size and warn on the fallback window
- Raise MissingAPIKeyError for a missing or placeholder API key
- Restore removed import paths with deprecation warnings
- Keep the provider's exception on LiteLLM streaming errors
- Tell the model how to recover from an unreadable deferred result
- Offer a login and retry once when AMP rejects the saved login during eval
- Stop rich live panel repainting into redirected logs
- Load from_repository set inside an agent's config
- Save unrestorable callbacks as null instead of breaking restore
- Show AMP's reason on a 401 and let the run app's deploy log in again
- Wait for the whole device-code lifetime at login and exit 1 on timeout
- Keep module identity when crewai rebuilds forward-ref namespaces
- Print upgrade commands instead of rewriting UV projects on crewai update
- Return the post from the flow scaffold's last step
- Exit 1 when a crewai+ command needs a login
- Exit with guidance when a Python conversational flow has no terminal
- Keep deeply nested JSON as text in the run TUI on Python 3.12
- Let the JSON crew runner load against an older crewai-core
- Report token usage for LiteLLM tool-call and structured-output calls

### Breaking Changes
- Document the removal of the 1.15.29 agent executor with migration notes

## Contributors

@Vidit-Ostwal, @alexmarchenko-crewai, @dependabot[bot], @joaomdmoura, @lorenzejay
