---
title: "langchain-ai/langchain langchain==1.4.0a1 released"
url: "https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "langchain"]
date: "2026-08-28T00:54:16Z"
metadata:
  repo: "langchain-ai/langchain"
  version: "langchain==1.4.0a1"
---

# langchain-ai/langchain langchain==1.4.0a1 released

> Source: github-releases | Category: changelog | 2026-08-28T00:54:16Z

## langchain-ai/langchain — langchain==1.4.0a1

Initial release

fix(langchain): name the content type MCP conversion could not handle
release(langchain): 1.4.0a1
test(langchain): skip MCP tests on a pydantic older than `mcp` supports
test(langchain): drive MCP tests through FastMCP's own utilities
fix(langchain/mcp): review edits (#39974)
Merge remote-tracking branch 'origin/master' into sydney-runkle/langchain/simplify-mcp-adapter
fix(langchain): import `assert_never` from `typing_extensions`
test(langchain): fix type errors in the MCP test suite
test(langchain): cover protocol eras across a multi-server fleet
test(langchain): cover both MCP protocol eras through one adapter
refactor(langchain): one elicitation request type per mode
refactor(langchain): keep the elicitation types out of `langchain.mcp`
fix(langchain): make the two FastMCP-private dependencies fail loudly
refactor(langchain): one elicitation response type per action
refactor(langchain): refuse MCP continuation rounds instead of polling
release(langchain): 1.3.18 (#39966)
refactor(langchain): tighten the elicitation answer types
refactor(langchain): move `_declare_elicitation_capability` to `elicitation`
docs(langchain): trim the `langchain.mcp` docstrings
fix(langchain): bound the MCP input-required retry loop
refactor(langchain): trim the `MCPAdapterTarget` docs
refactor(langchain): use `ELICITATION_INTERRUPT_TYPE` as the discriminator
refactor(langchain): drop `MCPAdapter.aclose`
fix(langchain): preserve content-block shape in PIIMiddleware redaction (#39894)
fix(core): shore up indexing in genai v1 streaming content (#39964)
fix(langchain): guard MCP elicitation calls against a dying session
feat(langchain): answer MCP elicitation with a LangGraph interrupt
feat(langchain): port MCP tool conversion from `langchain-mcp-adapters`
feat(langchain): drop elicitation from `MCPAdapter`
chore(langchain): require FastMCP 4.0.0b4 for the `mcp` extra
feat(langchain): simplify `MCPAdapter` construction
feat(langchain): langchain.mcp namespace, `MCPAdapter`
release(langchain): 1.3.17 (#39893)
fix(langchain): frame custom HITL rejection reasons (#39773)
chore(deps): bump minor and patch dependencies (#39869)
release(langchain): 1.3.16 (#39806)
feat(core): add standard model exception types (#39538)
feat(langchain): support custom token_counter in ContextEditingMiddleware (#39754)
fix(langchain): re-raise non-retryable exceptions in ModelRetryMiddleware (#38960)
chore(langchain): update docs on error handling for json schema (#39632)
fix(langchain): preserve final repeated schema ordering (#39284)
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
