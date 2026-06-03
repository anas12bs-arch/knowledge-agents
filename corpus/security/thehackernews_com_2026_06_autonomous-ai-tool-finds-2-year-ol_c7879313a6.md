---
title: "[hacker-news-sec] Autonomous AI Tool Finds 2-Year-Old RCE Flaw in Redis (CVE-2026-23479)"
url: "https://thehackernews.com/2026/06/autonomous-ai-tool-finds-2-year-old-rce.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-06-03T23:15:18Z"
metadata:
  {}
---

# [hacker-news-sec] Autonomous AI Tool Finds 2-Year-Old RCE Flaw in Redis (CVE-2026-23479)

> Source: security | Category: security | 2026-06-03T23:15:18Z

Autonomous AI Tool Finds 2-Year-Old RCE Flaw in Redis (CVE-2026-23479)

Redis has  patched  a use-after-free in its blocking-client code that lets an authenticated user run arbitrary OS commands on the machine hosting the database. The flaw was found by an autonomous AI tool built to hunt bugs in large codebases.
Tracked as CVE-2026-23479, the flaw was introduced in Redis 7.2.0 and remained in every stable branch until the May 5 fixes, unnoticed for over two years.
