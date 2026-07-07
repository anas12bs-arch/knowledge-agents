---
title: "Observability Design for the AI Era — Application / Infrastructure / CI / LLM, Each in Its Own Shape (Part 1)"
url: "https://dev.to/ryantsuji/observability-design-for-the-ai-era-application-infrastructure-ci-llm-each-in-its-own-56eg"
source: "devto"
category: "news"
tags: ["devto", "ai", "tech-article"]
date: "2026-07-07T05:29:16Z"
metadata:
  tag: "ai"
---

# Observability Design for the AI Era — Application / Infrastructure / CI / LLM, Each in Its Own Shape (Part 1)

> Source: devto | Category: news | 2026-07-07T05:29:16Z

The previous code-graph series was about reshaping a static analysis graph so AI could query it. The same kind of reshaping is needed on the observability side. This post walks through four axes — application / infrastructure / CI / LLM — and the deliberately different shapes each one ends up in. The design judgments worth calling out: computing Gemini cost client-side instead of from billing API, sending Claude Code OTel straight to BigQuery instead of Loki, and shipping CI logs via post-hoc pull instead of webhook push.

Reactions: 14
