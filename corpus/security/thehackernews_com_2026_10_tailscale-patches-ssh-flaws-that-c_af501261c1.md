---
title: "[hacker-news-sec] Tailscale Patches SSH Flaws That Could Let Hacked Devices Gain Root Access on Other Servers"
url: "https://thehackernews.com/2026/10/tailscale-patches-ssh-flaws-that-could.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-10-28T13:50:35Z"
metadata:
  {}
---

# [hacker-news-sec] Tailscale Patches SSH Flaws That Could Let Hacked Devices Gain Root Access on Other Servers

> Source: security | Category: security | 2026-10-28T13:50:35Z

Tailscale Patches SSH Flaws That Could Let Hacked Devices Gain Root Access on Other Servers

Tailscale has released&nbsp;version 1.104.4&nbsp;to fix flaws in its built-in SSH server that could let an attacker reach services and files on other servers that only the&nbsp;root&nbsp;user should be able to touch.

The flaws are in how&nbsp;Tailscale SSH&nbsp;forwards network connections, a job the Tailscale background process carries out with root privileges. To use them, an attacker must
