---
title: "shadcn-ui/ui shadcn@4.23.0 released"
url: "https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.23.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ui"]
date: "2026-10-27T12:46:44Z"
metadata:
  repo: "shadcn-ui/ui"
  version: "shadcn@4.23.0"
---

# shadcn-ui/ui shadcn@4.23.0 released

> Source: github-releases | Category: changelog | 2026-10-27T12:46:44Z

## shadcn-ui/ui — shadcn@4.23.0

### Minor Changes

- [#12296](https://github.com/shadcn-ui/ui/pull/12296) [`15f59b4`](https://github.com/shadcn-ui/ui/commit/15f59b41750542ef5d41ee34601a85a4e7c1be17) Thanks [@mattzcarey](https://github.com/mattzcarey)! - Upgrade the MCP server to MCP TypeScript SDK v2 (`@modelcontextprotocol/server`). `shadcn mcp` now serves MCP protocol 2026-07-28 as well as earlier versions. The `shadcn/mcp` export is now an `McpServer`, and a new `createServer()` export returns a fresh instance per connection. Code that called `server.setRequestHandler(...)` on the old `Server` export should use `server.registerTool(...)` or `server.server.setRequestHandler(...)` instead.
