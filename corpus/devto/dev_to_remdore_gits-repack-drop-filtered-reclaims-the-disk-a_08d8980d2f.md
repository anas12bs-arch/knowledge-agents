---
title: "Git's repack --drop-filtered reclaims the disk a partial clone quietly took back"
url: "https://dev.to/remdore/gits-repack-drop-filtered-reclaims-the-disk-a-partial-clone-quietly-took-back-3bk2"
source: "devto"
category: "news"
tags: ["devto", "opensource", "tech-article"]
date: "2026-09-09T13:47:29Z"
metadata:
  tag: "opensource"
---

# Git's repack --drop-filtered reclaims the disk a partial clone quietly took back

> Source: devto | Category: news | 2026-09-09T13:47:29Z

A blob:limit partial clone of a 397 MiB repo started at 36 MiB and was back at 360 MiB after ten checkouts. Git's unreleased repack --drop-filtered got 324 MiB of that back in 0.04s, but it aborts outright if a single large file is in your index, and sparse-checkout does not save you.

Reactions: 5
