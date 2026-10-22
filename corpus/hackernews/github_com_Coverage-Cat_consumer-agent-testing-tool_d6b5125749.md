---
title: "Show HN: CATT 0.2.1: Test agents/services against a Muse/Instinct-alike, in CI"
url: "https://github.com/Coverage-Cat/consumer-agent-testing-tool"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-22T23:32:09Z"
metadata:
  score: "4"
---

# Show HN: CATT 0.2.1: Test agents/services against a Muse/Instinct-alike, in CI

> Source: hackernews | Category: news | 2026-10-22T23:32:09Z

Score: 4 | Comments: 0

Hey HN, we recently open sourced our Consumer Agent Testing Tool to help teams iterate against proprietary assistants like Muse and Instinct. We built this to reduce our own frustrations with building an MCP&#x2F;API for these agents to consume.<p>The problem: testing against these tools is hard! Agent memory + account statefulness make reproducibility, in the ways required for repeatable&#x2F;reliable outcomes, between agents and the APIs&#x2F;MCPs they interact with very challenging.<p>The solution: CATT lets devs test their services against a surrogate Muse or Instinct agent (not affiliated with either of these companies). Testers define starting conditions, approvals, and success conditions for their service&#x27;s state. CATT then records the full interaction (incl. tool calls, responses) so it can diff what happened from what the agent reports. Runs can be tested in local builds or via CI, with or without LLM backing.<p>CATT is designed to emulate the important parts of personal assistant interactions. Its got:<p>- Tool calls and command-line tool access
- Simulated approvals for service actions
- Outcomes tracking and comparison
- Optional MCP profile based on an unofficial Muse template<p>There are limitations to how much we know about different assistant specific behaviors so the tool labels its assumptions as `documented`, `unofficial`, `assumed` or `unknown` for developer review. We&#x27;ll do our best to keep the tool updated as new insights about the internal workings of these assistants come to light. It is an area of active research and interest, a good example is this recent report on how Instinct uses Exa for web search [0].<p>Are you building a connector or MCP? If yes, we&#x27;d like to hear from you! Have you had assistants behave incoherently, use stale information, or procalim success without evidence? What else should we add tests for?<p>The best way to get started is...to point your coding assistant at the repo and ask it to integrate the tool with your CI or local testing pipeline!<p>Hope it&#x27;s helpful!<p>[0]: <a href="https:&#x2F;&#x2F;www.sunbeam.ai&#x2F;thoughts&#x2F;instinct-is-using-exa-for-web-search" rel="nofollow">https:&#x2F;&#x2F;www.sunbeam.ai&#x2F;thoughts&#x2F;instinct-is-using-exa-for-we...</a>
