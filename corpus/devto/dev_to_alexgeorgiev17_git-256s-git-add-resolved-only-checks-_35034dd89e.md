---
title: "Git 2.56's git add --resolved only checks conflict markers while git still calls a file unmerged"
url: "https://dev.to/alexgeorgiev17/git-256s-git-add-resolved-only-checks-conflict-markers-while-git-still-calls-a-file-unmerged-jgm"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-17T17:57:20Z"
metadata:
  tag: "programming"
---

# Git 2.56's git add --resolved only checks conflict markers while git still calls a file unmerged

> Source: devto | Category: news | 2026-11-17T17:57:20Z

I tested Git 2.56's new add --resolved flag: it kept an unrelated edit out of a merge commit, but its conflict-marker check stopped working the moment the index stopped calling a file unmerged.

Reactions: 11
