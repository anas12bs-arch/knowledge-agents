---
title: "[hacker-news-sec] Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data"
url: "https://thehackernews.com/2026/11/nodejs-fixes-16-flaws-including-http2.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-11-12T12:10:02Z"
metadata:
  {}
---

# [hacker-news-sec] Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data

> Source: security | Category: security | 2026-11-12T12:10:02Z

Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data

A flaw fixed in Node.js this week lets unauthenticated clients crash servers that use the runtime's built-in HTTP/2 support on the 24.x and 26.x release lines. A second HTTP/2 flaw can cause a server to send a client pieces of its memory, including responses intended for other connections.

Fixed versions were released for all three supported lines: 22.23.5, 24.22.3, and 26.13.1.

The crash
