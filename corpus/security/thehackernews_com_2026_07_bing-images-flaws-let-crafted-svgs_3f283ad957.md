---
title: "[hacker-news-sec] Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers"
url: "https://thehackernews.com/2026/07/bing-images-flaws-let-crafted-svgs-run.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-24T14:05:22Z"
metadata:
  {}
---

# [hacker-news-sec] Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers

> Source: security | Category: security | 2026-07-24T14:05:22Z

Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers

A crafted SVG submitted to Bing's image search ran commands as NT AUTHORITY\SYSTEM on Microsoft's production image-processing workers, and as root on the Linux machines in the same fleet.

XBOW's testing got the same result on workers across different hosts and network ranges, so the problem sat in Bing's image tier, not on one bad machine. Microsoft issued two critical CVEs, CVE-2026-32194 and
