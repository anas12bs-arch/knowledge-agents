---
title: "[hacker-news-sec] Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw"
url: "https://thehackernews.com/2026/06/public-poc-released-for-critical.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-06-29T11:27:00Z"
metadata:
  {}
---

# [hacker-news-sec] Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw

> Source: security | Category: security | 2026-06-29T11:27:00Z

Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw

A public proof-of-concept is now out for CVE-2026-55200, a critical flaw in libssh2 that lets a malicious or compromised SSH server trigger memory corruption on a connecting client, with possible code execution. No credentials, no user interaction. The bug affects every release up to and including 1.11.1 and carries a CVSS 4.0 score of 9.2.

libssh2 is a client-side SSH library, not a server.
