---
title: "[hacker-news-sec] 29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests"
url: "https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-06-22T17:52:52Z"
metadata:
  {}
---

# [hacker-news-sec] 29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests

> Source: security | Category: security | 2026-06-22T17:52:52Z

29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests

A heap over-read in the Squid web proxy can leak another user's cleartext HTTP request, including any credentials or session tokens it carries, to anyone already allowed to send traffic through the same proxy.

The bug traces to a 1997 FTP-parsing change and is still live in Squid's default configuration. Researchers at Calif.io&nbsp;disclosed it in June&nbsp;and named it Squidbleed (
