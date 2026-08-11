---
title: "langchain-ai/langchain langchain==1.3.15 released"
url: "https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.3.15"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "langchain"]
date: "2026-08-11T19:36:59Z"
metadata:
  repo: "langchain-ai/langchain"
  version: "langchain==1.3.15"
---

# langchain-ai/langchain langchain==1.3.15 released

> Source: github-releases | Category: changelog | 2026-08-11T19:36:59Z

## langchain-ai/langchain — langchain==1.3.15

Changes since langchain==1.3.14

release(langchain): 1.3.15 (#39595)
feat(langchain): expose `trace_policy` on `AgentMiddleware` (#38910)
chore(langchain): fix type errors in tests (#39589)
chore: bump h2 from 4.3.0 to 4.4.1 in /libs/langchain_v1 (#39324)
fix(langchain): preserve history on `SummarizationMiddleware` summary failure (#39268)
fix(langchain): handle import error in `LLMToolEmulator` by `model` (#39290)
refactor(langchain): update doc strings (#39305)
feat(langchain): add `state_schema` param to `wrap_tool_call` (#39292)
fix(langchain): re-export `PIIMatch` from `middleware` package (#39291)
fix(langchain): restrict narrowed `ToolStrategy` in bound tools (#39259)
feat(langchain): filter internal middleware model calls from `messages` projection (#39252)
chore: bump aiohttp from 3.14.1 to 3.14.3 in /libs/langchain_v1 (#39242)
chore: bump cryptography from 48.0.1 to 50.0.0 in /libs/langchain_v1 (#39240)
test(langchain): regression test for shell tool + checkpointer msgpack error (#39267)
fix(langchain): handle malformed structured-output responses (#39245)
fix(langchain): prevent orphaned `tool_calls` in `ToolCallLimitMiddleware` end behavior (#39258)
fix(langchain): add aliases for bedrock mantle chat models (#39260)
feat(langchain): add LangSmith provider to `init_chat_model` (#39224)
fix(langchain): clear stale `structured_response` between checkpointed turns (#39248)
fix(langchain): stop HITL approval gates from silently failing open (#39247)
chore: bump the minor-and-patch group across 3 directories with 7 updates (#39187)
fix(langchain): propagate model middleware control flow (#39199)
fix(langchain): update Anthropic config test (#39172)
chore: bump pyasn1 from 0.6.3 to 0.6.4 in /libs/langchain_v1 (#39026)
chore: bump pillow from 12.2.0 to 12.3.0 in /libs/langchain_v1 (#38994)
feat(core): add `reasoning_effort` as a standard chat model parameter (#38887)
docs(langchain): clarify `ToolRetryMiddleware` exception handling (#38884)
