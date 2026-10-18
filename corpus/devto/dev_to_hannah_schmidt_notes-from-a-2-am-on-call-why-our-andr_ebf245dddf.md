---
title: "Notes from a 2 AM On-Call: Why Our Android CI Containers Silently Froze (And the iptables Rule That Fixed It)"
url: "https://dev.to/hannah_schmidt/notes-from-a-2-am-on-call-why-our-android-ci-containers-silently-froze-and-the-iptables-rule-that-8pg"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-18T19:05:24Z"
metadata:
  tag: "devops"
---

# Notes from a 2 AM On-Call: Why Our Android CI Containers Silently Froze (And the iptables Rule That Fixed It)

> Source: devto | Category: news | 2026-10-18T19:05:24Z

Postmortem of a production freeze in budtmo/docker-android when emulator ADB ports leaked outside the bridge network, causing silent deadlocks under concurrent load.

Reactions: 1
