---
title: "Server functions in Fitz: call the server from a WASM component, no plumbing"
url: "https://dev.to/martin_palopoli/server-functions-in-fitz-call-the-server-from-a-wasm-component-no-plumbing-55ao"
source: "devto"
category: "news"
tags: ["devto", "opensource", "tech-article"]
date: "2026-09-11T23:58:22Z"
metadata:
  tag: "opensource"
---

# Server functions in Fitz: call the server from a WASM component, no plumbing

> Source: devto | Category: news | 2026-09-11T23:58:22Z

A `@rpc async fn` in a classic Fitz module is callable directly from a client-WASM `.fitzv` — `get_user(42).await?` — as if it were local. The compiler emits both halves from one declaration, typed end-to-end, zero dependencies.

Reactions: 0
