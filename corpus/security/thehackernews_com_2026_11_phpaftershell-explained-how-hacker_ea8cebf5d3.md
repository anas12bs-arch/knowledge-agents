---
title: "[hacker-news-sec] phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution"
url: "https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-11-19T20:54:55Z"
metadata:
  {}
---

# [hacker-news-sec] phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution

> Source: security | Category: security | 2026-11-19T20:54:55Z

phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution

PHP's default file-based session storage can be made to return objects an attacker chose, by cutting off a session write at the right moment. When combined with a second weakness, such as a suitable gadget chain in the app, those objects can allow the attacker to run code on the server.

Today's PHP releases fix the flaw, called phpAfterShell.

The flaw is tracked as CVE-2026-126714 and rated
