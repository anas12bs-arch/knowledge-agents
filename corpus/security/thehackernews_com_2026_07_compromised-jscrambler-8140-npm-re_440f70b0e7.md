---
title: "[hacker-news-sec] Compromised jscrambler 8.14.0 npm Release Drops Rust Infostealer During Install"
url: "https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-11T19:19:20Z"
metadata:
  {}
---

# [hacker-news-sec] Compromised jscrambler 8.14.0 npm Release Drops Rust Infostealer During Install

> Source: security | Category: security | 2026-07-11T19:19:20Z

Compromised jscrambler 8.14.0 npm Release Drops Rust Infostealer During Install

Version&nbsp;8.14.0&nbsp;of the jscrambler npm package shipped with a malicious&nbsp;preinstall&nbsp;hook that silently drops and runs a native infostealer during installation, one build each for Windows, macOS, and Linux.

Published on July 11, 2026, it needs no import and no CLI call. Installing 8.14.0 is enough to run&nbsp;it.

Socket flagged the release&nbsp;six minutes after it was
