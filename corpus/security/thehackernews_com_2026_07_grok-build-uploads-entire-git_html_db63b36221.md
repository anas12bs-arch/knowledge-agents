---
title: "[hacker-news-sec] Grok Build Uploads Entire Git Repositories to xAI Storage, Not Just Files It Reads"
url: "https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-14T09:24:09Z"
metadata:
  {}
---

# [hacker-news-sec] Grok Build Uploads Entire Git Repositories to xAI Storage, Not Just Files It Reads

> Source: security | Category: security | 2026-07-14T09:24:09Z

Grok Build Uploads Entire Git Repositories to xAI Storage, Not Just Files It Reads

xAI's Grok Build coding CLI was uploading entire Git repositories, full commit history and all, to a Google Cloud Storage bucket run by xAI, not just the files a coding task needed.

A researcher publishing as cereblab, testing version 0.2.93, captured one of those uploads, cloned the git bundle out of the intercepted request, and pulled back a file the agent had been told in plain terms not
