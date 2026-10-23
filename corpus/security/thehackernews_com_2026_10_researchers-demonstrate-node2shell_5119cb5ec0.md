---
title: "[hacker-news-sec] Researchers Demonstrate Node2Shell RCE Exploit on Node.js Build Using Crafted Brotli Data"
url: "https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-10-23T16:17:30Z"
metadata:
  {}
---

# [hacker-news-sec] Researchers Demonstrate Node2Shell RCE Exploit on Node.js Build Using Crafted Brotli Data

> Source: security | Category: security | 2026-10-23T16:17:30Z

Researchers Demonstrate Node2Shell RCE Exploit on Node.js Build Using Crafted Brotli Data

Malicious Brotli data can make an application on an official build of Node.js run attacker-supplied code, security researchers at Imperva have&nbsp;demonstrated.

Their "Node2Shell" proof of concept ran code on the official Node.js 24.22.0 image for Linux arm64, with no debugger or custom build, by feeding crafted data to the bundled Brotli decoder (CVE-2026-111497). Node.js disclosed the flaw
