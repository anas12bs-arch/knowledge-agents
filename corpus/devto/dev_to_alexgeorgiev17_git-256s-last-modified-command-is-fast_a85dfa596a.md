---
title: "Git 2.56's last-modified command is fast on one directory and slow on scattered files"
url: "https://dev.to/alexgeorgiev17/git-256s-last-modified-command-is-fast-on-one-directory-and-slow-on-scattered-files-2ggm"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-22T23:32:17Z"
metadata:
  tag: "devops"
---

# Git 2.56's last-modified command is fast on one directory and slow on scattered files

> Source: devto | Category: news | 2026-10-22T23:32:17Z

I benchmarked Git's new last-modified command against a per-file git log loop on git/git: 861ms versus 2981ms listing one real directory, but slower once the same 40 paths were scattered across the tree, and a parent-then-child pathspec order silently drops a row.

Reactions: 13
