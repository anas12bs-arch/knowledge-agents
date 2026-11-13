---
title: "[hacker-news-sec] PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE"
url: "https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-11-13T21:31:40Z"
metadata:
  {}
---

# [hacker-news-sec] PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE

> Source: security | Category: security | 2026-11-13T21:31:40Z

PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE

A type confusion flaw in PostgreSQL lets a database user who can create objects run code on the server. Updates released yesterday fix it, along with 51 other security flaws. Full protection from this flaw also requires rebuilding any C-language extensions installed on the server.

The flaw, tracked as CVE-2026-6460, has a CVSS score of 8.8. Any code run this way has the rights of the operating
