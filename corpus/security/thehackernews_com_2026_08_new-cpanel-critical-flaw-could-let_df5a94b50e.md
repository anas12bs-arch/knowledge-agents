---
title: "[hacker-news-sec] New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root"
url: "https://thehackernews.com/2026/08/new-cpanel-critical-flaw-could-let.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-08-04T11:49:59Z"
metadata:
  {}
---

# [hacker-news-sec] New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root

> Source: security | Category: security | 2026-08-04T11:49:59Z

New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root

cPanel has patched a flaw that let an authenticated hosting customer execute SQL in the database's root context, crossing the privilege boundary between a cPanel account and the server's administrative database identity. It shipped in a targeted security release that closes two other routes past account boundaries.

The database bug is tracked as CVE-2026-58048 (CVSS 4.0 score: 9.4) and affects
