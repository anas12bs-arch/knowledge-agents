---
title: "Making the Context Across 46 Repositories Semantically Searchable for AI (Part 2)"
url: "https://dev.to/ryantsuji/making-the-context-across-46-repositories-semantically-searchable-for-ai-part-2-51d9"
source: "devto"
category: "news"
tags: ["devto", "ai", "tech-article"]
date: "2026-06-30T00:19:19Z"
metadata:
  tag: "ai"
---

# Making the Context Across 46 Repositories Semantically Searchable for AI (Part 2)

> Source: devto | Category: news | 2026-06-30T00:19:19Z

The biggest issue Part 1 left open was that AI couldn't reach the 46-repo codebase by natural-language query (the entry-point problem). This post is how I solved it — by reusing the pattern proven in db-graph (1,133-table semantic search), then layering minimal annotations only around boundary nodes. Covers the separate-branch operation that keeps engineers' daily workflow untouched, the SLO that protects the joins between three graphs, the SAME_ENTITY normalization, and the April–May trial-and-error timeline traced through real commits.

Reactions: 12
