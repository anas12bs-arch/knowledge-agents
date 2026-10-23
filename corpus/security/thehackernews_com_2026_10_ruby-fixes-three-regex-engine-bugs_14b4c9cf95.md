---
title: "[hacker-news-sec] Ruby Fixes Three Regex Engine Bugs Responsible for Four Critical GitLab RCE Flaws"
url: "https://thehackernews.com/2026/10/ruby-fixes-three-regex-engine-bugs.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-10-23T19:59:31Z"
metadata:
  {}
---

# [hacker-news-sec] Ruby Fixes Three Regex Engine Bugs Responsible for Four Critical GitLab RCE Flaws

> Source: security | Category: security | 2026-10-23T19:59:31Z

Ruby Fixes Three Regex Engine Bugs Responsible for Four Critical GitLab RCE Flaws

Ruby has released versions 4.0.9, 3.4.12, and 3.3.13 to fix three bugs in Onigmo, the regular expression engine built into the language. The bugs lie behind four critical security flaws that GitLab patched over the past month.

GitLab found that a specially crafted pattern could corrupt memory while Ruby compiles it, potentially leading to code execution on its own servers.

Ruby says any
