---
title: "langchain-ai/langchain langchain==1.4.0a4 released"
url: "https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a4"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "langchain"]
date: "2026-09-02T05:47:48Z"
metadata:
  repo: "langchain-ai/langchain"
  version: "langchain==1.4.0a4"
---

# langchain-ai/langchain langchain==1.4.0a4 released

> Source: github-releases | Category: changelog | 2026-09-02T05:47:48Z

## langchain-ai/langchain — langchain==1.4.0a4

Initial release

release(langchain): 1.4.0a4
test(langchain): cover mixed-era ClientGroup and group elicitation
Update libs/langchain_v1/langchain/mcp/adapter.py
fix(langchain): drive MCP elicitation via member session for fastmcp 4.0.1
fix(sdk): use latest fastmcp and rm reentrant impl
cr
cr
refactor(langchain): inline MCP client arming into `__init__`
refactor(langchain): stamp an arm marker instead of introspecting the handler closure
fix(langchain): gate MCP interrupt routing on the negotiated protocol era
refactor(langchain): drop MCP `elicitation` flag, derive interrupt routing from the client
fix(sdk): add _ReentrantClientGroup
fix(langchain): narrow `MCPAdapter.client` union in mcp tests for mypy
chore(langchain): format `mcp/adapter.py`
release(langchain): 1.4.0a3
feat(langchain): group MCP tool metadata under an `mcp` namespace
refactor(langchain): stop exporting `MCPAdapterTarget` from `langchain.mcp`
refactor(langchain): rename `convert_mcp_tool_to_langchain_tool` to `as_langchain_tool`
refactor(langchain): rename `MCPAdapter.get_tools` to `list_tools`
feat(langchain): expose `cache_mode` on `MCPAdapter.get_tools`
chore(langchain): require `fastmcp` 4.0.0
feat(langchain): accept a `ClientGroup` as an `MCPAdapter` target
feat(langchain): mark the `langchain.mcp` namespace as beta
Revert "feat(langchain): accept a `ClientGroup` as an `MCPAdapter` target"
feat(langchain): accept a `ClientGroup` as an `MCPAdapter` target
chore(langchain): require `fastmcp` 4.0.0b5
fix(langchain): require a `str` MCP target to be an http(s) URL
release(langchain): 1.4.0a2
fix(langchain): require full `fastmcp` for the `mcp` extra
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
fix(langchain): re-raise non-retryable
