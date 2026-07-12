---
title: "Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k"
url: "https://systima.ai/blog/claude-code-vs-opencode-token-overhead"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-12T19:21:39Z"
metadata:
  score: "93"
---

# Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k

> Source: hackernews | Category: news | 2026-07-12T19:21:39Z

Score: 93 | Comments: 46

This started based off of a hunch. We usually use OpenCode, but were &#x27;forced&#x27; to use Claude Code for a while due to issues with Meridian. In that time, we saw the usage meter rise much, much more quickly than when using OpenCode.<p>This was the initial anecdotal evidence, but we undertook this small study to collect empirical data:<p>We added logging between the agentic coding tool (Claude Code and OpenCode) and Anthropic&#x27;s endpoint, and captured all requests (and the returned usage blocks).<p>With one caveat (toward the end of the post) we found unambiguously that Claude Code was far more inefficient in terms of its cache strategy and its harness token usage than OpenCode.
