---
title: "[hacker-news-sec] Critical Pre-Auth MongoDB Flaw (CVE-2026-118383) Can Crash Lagging Servers on Failover"
url: "https://thehackernews.com/2026/11/critical-pre-auth-mongodb-flaw-cve-2026.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-11-12T12:10:02Z"
metadata:
  {}
---

# [hacker-news-sec] Critical Pre-Auth MongoDB Flaw (CVE-2026-118383) Can Crash Lagging Servers on Failover

> Source: security | Category: security | 2026-11-12T12:10:02Z

Critical Pre-Auth MongoDB Flaw (CVE-2026-118383) Can Crash Lagging Servers on Failover

A critical flaw in MongoDB Server allows an unauthenticated attacker to send two requests that trigger a crash on the database server. The crash occurs only if that server is later chosen to take over as the main server while it still lacks some recent changes.

MongoDB, the company that makes the database, released fixed versions earlier this week.

The affected servers are members of a replica
