---
title: "[infoq] Cloudflare Adds Agent Tracing, with Truncation Limits and Uneven Payload Defaults"
url: "https://www.infoq.com/news/2026/08/cloudflare-agent-tracing/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-08-15T11:03:49Z"
metadata:
  {}
---

# [infoq] Cloudflare Adds Agent Tracing, with Truncation Limits and Uneven Payload Defaults

> Source: engineering | Category: engineering | 2026-08-15T11:03:49Z

Cloudflare Adds Agent Tracing, with Truncation Limits and Uneven Payload Defaults

Cloudflare launched agent tracing, adding spans for agent invocations, model calls, tool runs, and approvals to existing Workers traces. Sessions replay turn by turn, though the docs warn traces are not lossless and payloads may be truncated. Payload recording defaults differ by framework, and from October 1, 2026 every span counts as a billable event.   By Steef-Jan Wiggers
