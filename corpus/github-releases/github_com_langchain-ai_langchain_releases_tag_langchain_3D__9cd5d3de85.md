---
title: "langchain-ai/langchain langchain==1.4.0a2 released"
url: "https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.0a2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "langchain"]
date: "2026-08-28T22:26:36Z"
metadata:
  repo: "langchain-ai/langchain"
  version: "langchain==1.4.0a2"
---

# langchain-ai/langchain langchain==1.4.0a2 released

> Source: github-releases | Category: changelog | 2026-08-28T22:26:36Z

## langchain-ai/langchain — langchain==1.4.0a2

Alpha preview of `langchain.mcp` — a first-party adapter that turns any MCP server into LangChain tools you can hand straight to `create_agent`.

Connection handling is [FastMCP](https://gofastmcp.com/clients/client)'s, so its client features are available as-is rather than re-implemented behind a narrower interface.

```bash
pip install "langchain[mcp]==1.4.0a2"
```

## Connect

`MCPAdapter` takes any target `fastmcp.Client` accepts — transport is inferred, so there is one entry point rather than one per protocol.

```python
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter

async with MCPAdapter("https://example.com/mcp") as adapter:
    agent = create_agent("anthropic:claude-sonnet-5", await adapter.get_tools())
    result = await agent.ainvoke({"messages": [{"role": "user", "content": "..."}]})
```

Valid targets: a URL, a local script path (launched over stdio), an in-process `FastMCP` server, a config naming several servers at once, or a `fastmcp.Client` you built yourself.

Tools returned by `get_tools()` hold the adapter's client, so they stay callable after the context exits — the `async with` block scopes discovery, not tool lifetime.

## Auth, caching, timeouts — build the client

`MCPAdapter` takes two arguments: the target and `elicitation`. Everything else FastMCP supports is configured on a `fastmcp.Client` that you build and hand over as the target. This is the pattern to reach for whenever you need more than a bare connection:

```python
from fastmcp.client import Client
from langchain.mcp import MCPAdapter

client = Client(
    "https://example.com/mcp",
    auth="oauth",       # or a bearer token string, or any httpx auth
    cache=True,         # opt-in response caching
    timeout=30,
)

async with MCPAdapter(client) as adapter:
    tools = await adapter.get_tools()
```

**Auth** accepts `"oauth"` to run the OAuth flow, a token string for bearer auth, or an `httpx.Auth` instance for anything custom — see [FastMCP's auth docs](https://gofastmcp.com/clients/auth). Per-server headers and auth can also be set in a multi-server config (below).

**Caching** is opt-in and off by default: `cache=True` enables it with defaults, honoring the server's own `ttlMs` and `cacheScope` hints; a `CacheConfig` customizes it. The cache is per-client and in-memory.

**Everything else** on [`fastmcp.Client`](https://gofastmcp.com/clients/client) — `timeout`, `log_handler`, `progress_handler`, `message_handler`, `roots`, `sampling_handler` — works the same way. The adapter passes your client through untouched, so FastMCP behavior is not re-implemented or restricted.

One caveat: with `elicitation="interrupt"`, the adapter clones your client so it does not overwrite a callback you set. Configuration (auth, cache settings, handlers) carries over to the clone; cached *entries* do not, since the clone gets its own store.

`adapter.client` exposes the underlying client for prompts, resources, and anything else the adapter does not wrap.

## Multiple servers

Point the adapter at a config and it fans out to every server through one connection, presenting a single tool list to your agent.

```python
config = {
    "mcpServers": {
        "weather": {"url": "https://weather.example.com/mcp"},
        "calendar": {
            "url": "https://calendar.example.com/mcp",
            "headers": {"Authorization": "Bearer ..."},
        },
    }
}

async with MCPAdapter(config) as adapter:
    agent = create_agent("anthropic:claude-sonnet-5", await adapter.get_tools())
```

With more than one server, tools are namespaced by server name — `weather_get_forecast`, `calendar_create_event` — so collisions between servers are impossible. With exactly one server, the adapter connects directly and names are unprefixed. Each entry takes its own `headers`, `auth`, `transport`, and `timeout`, so servers with different credentials compose in one agent. A local server uses `command`/`args` instead of `url` and is launched over
