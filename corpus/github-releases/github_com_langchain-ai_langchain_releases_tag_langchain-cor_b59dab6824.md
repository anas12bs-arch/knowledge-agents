---
title: "langchain-ai/langchain langchain-core==1.7.0 released"
url: "https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.7.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "langchain"]
date: "2026-10-22T23:33:07Z"
metadata:
  repo: "langchain-ai/langchain"
  version: "langchain-core==1.7.0"
---

# langchain-ai/langchain langchain-core==1.7.0 released

> Source: github-releases | Category: changelog | 2026-10-22T23:33:07Z

## langchain-ai/langchain — langchain-core==1.7.0

Changes since langchain-core==1.6.13

release(core): 1.7.0 (#41418)
feat(core): emit `tool-call-delta` for streamed tool-call args (#41257)

## Notes

- Tool-call args now stream as `tool-call-delta` slices instead of `block-delta` snapshots of the args so far. If you read raw stream events and their `block-delta` args mid-stream, read `tool-call-delta` instead. `.tool_calls.get()` and `.output` are unchanged. To keep snapshots, pin `langchain-core<1.7`.
- Since 1.6.13, iterating `ChatModelStream.tool_calls` yields each call's new args slice, not a snapshot of the args so far.
