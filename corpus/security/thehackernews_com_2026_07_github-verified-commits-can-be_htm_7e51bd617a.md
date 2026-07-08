---
title: "[hacker-news-sec] GitHub 'Verified' Commits Can Be Rewritten Into New Hashes Without Breaking Signatures"
url: "https://thehackernews.com/2026/07/github-verified-commits-can-be.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-08T12:53:41Z"
metadata:
  {}
---

# [hacker-news-sec] GitHub 'Verified' Commits Can Be Rewritten Into New Hashes Without Breaking Signatures

> Source: security | Category: security | 2026-07-08T12:53:41Z

GitHub 'Verified' Commits Can Be Rewritten Into New Hashes Without Breaking Signatures

New research shows that a signed Git commit's hash is not the one-of-a-kind name that much of the software world assumes it to be. Given any signed commit, someone without the signing key can mint a second commit with the same files, author, and date, and a valid signature, GitHub still stamps "Verified."

Everything a reviewer would check matches. The commit's hash does not. That matters
