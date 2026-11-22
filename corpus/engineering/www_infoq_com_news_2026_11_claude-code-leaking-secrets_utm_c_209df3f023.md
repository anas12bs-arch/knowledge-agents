---
title: "[infoq] Claude Code Has Been Leaking Secrets Through Its 'Don't Ask Again' Feature"
url: "https://www.infoq.com/news/2026/11/claude-code-leaking-secrets/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-11-22T12:04:39Z"
metadata:
  {}
---

# [infoq] Claude Code Has Been Leaking Secrets Through Its "Don't Ask Again" Feature

> Source: engineering | Category: engineering | 2026-11-22T12:04:39Z

Claude Code Has Been Leaking Secrets Through Its "Don't Ask Again" Feature

Agentic security firm Apiiro found that Claude Code has been exposing secrets in public repositories due to how it stores them in local file on developers' machines to implement "Don't Ask Again". The company identified 1,122 secrets in claude/settings.local.json files and another 1,160 in git history, in the shared settings.json, and in agent chat transcripts stored in repos.   By Sergio De Simone
