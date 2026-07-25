---
title: "[hacker-news-sec] Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git"
url: "https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-25T10:02:54Z"
metadata:
  {}
---

# [hacker-news-sec] Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git

> Source: security | Category: security | 2026-07-25T10:02:54Z

Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git

Security researcher Yuhang Wu at depthfirst has published a working proof-of-concept (PoC) exploit that executes commands as git on an unpatched self-managed GitLab 18.11.3 server.

An ordinary authenticated user triggers it by committing two crafted Jupyter notebooks and requesting their diff. The chain needs no administrator rights, continuous integration (CI) runner access, victim interaction
