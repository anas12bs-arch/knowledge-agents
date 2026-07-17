---
title: "[hacker-news-sec] OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests"
url: "https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-17T20:35:30Z"
metadata:
  {}
---

# [hacker-news-sec] OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests

> Source: security | Category: security | 2026-07-17T20:35:30Z

OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests

Eleven bytes will make an unpatched OpenSSL server set aside up to 131 KB of memory for a message that never arrives. On the glibc systems Okta tested, that memory is gone until the process restarts.

OpenSSL shipped the HollowByte fix in June with no CVE, no advisory, and no changelog entry pointing at it. Okta's Red Team, which reported the denial-of-service bug and named it, published the
