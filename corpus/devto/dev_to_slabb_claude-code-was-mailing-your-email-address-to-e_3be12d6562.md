---
title: "Claude Code was mailing your email address to every website it visited: the User-Agent leak, the 5-month system-prompt issue, and the 5-point check"
url: "https://dev.to/slabb/claude-code-was-mailing-your-email-address-to-every-website-it-visited-the-user-agent-leak-the-12k6"
source: "devto"
category: "news"
tags: ["devto", "ai", "tech-article"]
date: "2026-11-06T22:04:05Z"
metadata:
  tag: "ai"
---

# Claude Code was mailing your email address to every website it visited: the User-Agent leak, the 5-month system-prompt issue, and the 5-point check

> Source: devto | Category: news | 2026-11-06T22:04:05Z

Claude Code put your account email in the User-Agent header of its web requests, so every server log on the agent's path harvested a scam-ready lead, and the same email ships in the system prompt of every session, an issue open since July. Fixed by a built-in mod in 2.1.317 after the issue went viral. The mechanics, the timeline, and the runtime test for your install.

Reactions: 9
