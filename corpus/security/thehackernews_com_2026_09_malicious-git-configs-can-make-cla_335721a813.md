---
title: "[hacker-news-sec] Malicious .git Configs Can Make Claude, Codex, Cursor, and Other AI Agents Run Attacker Code"
url: "https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-09-02T17:31:18Z"
metadata:
  {}
---

# [hacker-news-sec] Malicious .git Configs Can Make Claude, Codex, Cursor, and Other AI Agents Run Attacker Code

> Source: security | Category: security | 2026-09-02T17:31:18Z

Malicious .git Configs Can Make Claude, Codex, Cursor, and Other AI Agents Run Attacker Code

Manifold Security has disclosed eight security flaws across seven command-line AI coding agents in which a repository's own Git configuration names a command that the agent runs on the developer's machine, four of them still unpatched at publication.

The command executes as the user, outside the agent's sandbox and without an approval prompt, and exploitation requires the repository to arrive
