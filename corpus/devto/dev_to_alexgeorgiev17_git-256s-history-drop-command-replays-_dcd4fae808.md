---
title: "Git 2.56's history drop command replays commits 40 to 77 times faster than rebase"
url: "https://dev.to/alexgeorgiev17/git-256s-history-drop-command-replays-commits-40-to-77-times-faster-than-rebase-45jm"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-13T15:31:05Z"
metadata:
  tag: "devops"
---

# Git 2.56's history drop command replays commits 40 to 77 times faster than rebase

> Source: devto | Category: news | 2026-11-13T15:31:05Z

I measured git history drop against the classic worktree-and-rebase way of removing a commit: 1.4s vs 0.03s at 20 descendants, 26.5s vs 0.36s at 400.

Reactions: 13
