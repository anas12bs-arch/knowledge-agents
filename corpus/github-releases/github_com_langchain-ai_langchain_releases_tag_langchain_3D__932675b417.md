---
title: "langchain-ai/langchain langchain==1.4.0a3 released"
url: "https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a3"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "langchain"]
date: "2026-09-01T18:48:56Z"
metadata:
  repo: "langchain-ai/langchain"
  version: "langchain==1.4.0a3"
---

# langchain-ai/langchain langchain==1.4.0a3 released

> Source: github-releases | Category: changelog | 2026-09-01T18:48:56Z

## langchain-ai/langchain — langchain==1.4.0a3

Third alpha of the `1.4.0` line. This release focuses on the new `langchain.mcp` namespace for adapting MCP servers into LangChain tools.

## `langchain.mcp` highlights

- **`MCPAdapter`** adapts any target `fastmcp.Client` accepts — a URL, a local script, an in-process server, an `MCPConfig` naming several servers, or a pre-built client — as well as a FastMCP `ClientGroup` for a fleet of servers behind one client.
- **`MCPAdapter.list_tools(*, cache_mode="use")`** discovers and adapts tools, with optional client-side response caching (SEP-2549): `use` serves a cached list within the server's TTL hint, `refresh` repopulates it, `bypass` skips it.
- **`as_langchain_tool(tool, client, *, elicitation=None)`** converts a single MCP tool for callers managing their own client.
- **Tool metadata** is grouped under an `mcp` namespace on each tool: the tool's `annotations` (snake_case) and `_meta` under `metadata["mcp"]["tool"]`, and the serving server's identity under `metadata["mcp"]["server"]`.
- **`elicitation="interrupt"`** surfaces a server's mid-call questions as LangGraph interrupts, so a human answers and the run resumes.

```python
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter

async with MCPAdapter("https://example.com/mcp") as adapter:
    agent = create_agent("anthropic:claude-sonnet-5", await adapter.list_tools())
```

Requires the `mcp` extra: `pip install "langchain[mcp]"` (and `fastmcp>=4.0.0`).

## Install

```bash
pip install --pre "langchain==1.4.0a3"
```

This is a pre-release; install with `--pre`.

---

*Release notes curated with the assistance of an AI agent.*

