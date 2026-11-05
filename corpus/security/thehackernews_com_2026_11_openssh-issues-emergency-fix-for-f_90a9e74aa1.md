---
title: "[hacker-news-sec] OpenSSH Issues Emergency Fix for Flaw Letting Long Passwords Bypass SSH Auth on Alpine Linux"
url: "https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-11-05T22:54:18Z"
metadata:
  {}
---

# [hacker-news-sec] OpenSSH Issues Emergency Fix for Flaw Letting Long Passwords Bypass SSH Auth on Alpine Linux

> Source: security | Category: security | 2026-11-05T22:54:18Z

OpenSSH Issues Emergency Fix for Flaw Letting Long Passwords Bypass SSH Auth on Alpine Linux

Attackers can log in to accounts that have no password, such as SSH key-only accounts, on some Alpine Linux servers running the standard openssh-server package. They need network access to the server, an account name, and a password between 257 and 1,024 bytes long.

OpenSSH, which rates the flaw critical, released version 10.6p2 today to block it. Alpine has published fixed packages for every
