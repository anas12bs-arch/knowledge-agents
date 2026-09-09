---
title: "[hacker-news-sec] DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval"
url: "https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-09-09T13:47:18Z"
metadata:
  {}
---

# [hacker-news-sec] DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval

> Source: security | Category: security | 2026-09-09T13:47:18Z

DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval

A flaw in DeepSeek Harness, DeepSeek's open-source tool for running AI coding agents on a developer's machine, let a sandboxed agent turn off its own sandbox with a single command.

The tool runs an agent's commands inside an operating-system sandbox, so that an agent working on untrusted files cannot write outside its workspace. The agent could remove that limit by calling the tool's own web
