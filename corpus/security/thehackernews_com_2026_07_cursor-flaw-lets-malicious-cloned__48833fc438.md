---
title: "[hacker-news-sec] Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution"
url: "https://thehackernews.com/2026/07/cursor-flaw-lets-malicious-cloned.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-15T11:09:43Z"
metadata:
  {}
---

# [hacker-news-sec] Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution

> Source: security | Category: security | 2026-07-15T11:09:43Z

Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution

Open a repository in Cursor&nbsp;on Windows and, if a file named&nbsp;git.exe&nbsp;is sitting in the project root, Cursor runs it. No click, no approval dialog, no warning that anything in the folder is about to execute.

Whatever that binary does, it does as you, with your source, your SSH keys and your cloud tokens. Cursor keeps re-running it for as long as the project stays open.

No prompt
