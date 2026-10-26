---
title: "[hacker-news-sec] PHP Issues Second Windows Security Update in Five Days to Fix Brotli Code Execution Flaw"
url: "https://thehackernews.com/2026/10/php-issues-second-windows-security.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-10-26T18:54:20Z"
metadata:
  {}
---

# [hacker-news-sec] PHP Issues Second Windows Security Update in Five Days to Fix Brotli Code Execution Flaw

> Source: security | Category: security | 2026-10-26T18:54:20Z

PHP Issues Second Windows Security Update in Five Days to Fix Brotli Code Execution Flaw

PHP has rebuilt its official Windows packages for PHP 8.2 through 8.5 to fix CVE-2026-111497, a flaw in the Brotli compression library that the packages include. The flaw can let an attacker corrupt memory and potentially run code.

PHP says the flaw can be reached through the cURL extension when the extension decompresses HTTP responses automatically. cURL leaves that off by default, but
