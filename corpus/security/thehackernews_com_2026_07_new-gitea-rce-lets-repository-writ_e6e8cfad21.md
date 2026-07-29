---
title: "[hacker-news-sec] New Gitea RCE Lets Repository Writers Plant a Git Hook to Run Shell Commands"
url: "https://thehackernews.com/2026/07/new-gitea-rce-lets-repository-writers.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-29T09:50:40Z"
metadata:
  {}
---

# [hacker-news-sec] New Gitea RCE Lets Repository Writers Plant a Git Hook to Run Shell Commands

> Source: security | Category: security | 2026-07-29T09:50:40Z

New Gitea RCE Lets Repository Writers Plant a Git Hook to Run Shell Commands

Gitea, the self-hosted Git platform, has patched a critical remote code execution vulnerability. A user with ordinary repository write access can turn attacker-controlled patch content into a live Git hook and run shell commands as the Gitea service account.

Tracked as CVE-2026-60004 (CVSS score: 9.8), the flaw affects Gitea versions 1.17 and later before 1.27.1 and is fixed in 1.27.1. The
