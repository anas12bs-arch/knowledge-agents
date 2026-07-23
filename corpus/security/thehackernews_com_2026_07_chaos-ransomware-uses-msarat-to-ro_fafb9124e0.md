---
title: "[hacker-news-sec] Chaos Ransomware Uses msaRAT to Route C2 Traffic Through Headless Chrome and Edge"
url: "https://thehackernews.com/2026/07/chaos-ransomware-uses-msarat-to-route.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-23T14:56:38Z"
metadata:
  {}
---

# [hacker-news-sec] Chaos Ransomware Uses msaRAT to Route C2 Traffic Through Headless Chrome and Edge

> Source: security | Category: security | 2026-07-23T14:56:38Z

Chaos Ransomware Uses msaRAT to Route C2 Traffic Through Headless Chrome and Edge

The Chaos ransomware group ran its command-and-control through the victim's own browser. Cisco Talos on Thursday detailed msaRAT, the Rust implant behind it, found on a compromised Windows machine ahead of the encryptor.

The implant never opens an outbound connection of its own. Its process talks to 127.0.0.1 and nothing else. It starts Chrome or Edge in headless mode and drives the browser
