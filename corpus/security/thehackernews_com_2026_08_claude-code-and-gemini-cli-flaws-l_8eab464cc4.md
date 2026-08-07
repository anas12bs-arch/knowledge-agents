---
title: "[hacker-news-sec] Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets"
url: "https://thehackernews.com/2026/08/claude-code-and-gemini-cli-flaws-let.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-08-07T09:38:16Z"
metadata:
  {}
---

# [hacker-news-sec] Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets

> Source: security | Category: security | 2026-08-07T09:38:16Z

Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets

A GitHub issue opened by an account with no repository privileges was enough to execute code on the CI runners behind Anthropic's and Google's own coding-agent repositories. On OpenAI's, it was enough to hijack the next agent run.

Novee Security ran the attack against each vendor's agent in the configuration that the vendor ships by default, and presented the work at Black Hat USA on August 5.
