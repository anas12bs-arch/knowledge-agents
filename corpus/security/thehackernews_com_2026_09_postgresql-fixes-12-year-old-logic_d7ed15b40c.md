---
title: "[hacker-news-sec] PostgreSQL Fixes 12-Year-Old Logical Decoding Flaw Enabling Replication-Role Code Execution"
url: "https://thehackernews.com/2026/09/postgresql-fixes-12-year-old-logical.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-09-04T17:42:47Z"
metadata:
  {}
---

# [hacker-news-sec] PostgreSQL Fixes 12-Year-Old Logical Decoding Flaw Enabling Replication-Role Code Execution

> Source: security | Category: security | 2026-09-04T17:42:47Z

PostgreSQL Fixes 12-Year-Old Logical Decoding Flaw Enabling Replication-Role Code Execution

PostgreSQL has released updates to address a security flaw that allows an account with the REPLICATION attribute to run arbitrary code as the operating-system user running the database server.

The flaw, tracked as CVE-2026-6471 (CVSS score: 7.2), has been present since logical decoding was introduced in PostgreSQL 9.4 in 2014. Versions before PostgreSQL 18.6, 17.11, 16.15, 15.19, and 14.24 are
