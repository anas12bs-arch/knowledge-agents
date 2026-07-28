---
title: "[hacker-news-sec] Critical OpenWrt DHCPv6 Flaw Could Let Unauthenticated Attackers Run Code as Root"
url: "https://thehackernews.com/2026/07/critical-openwrt-dhcpv6-flaw-could-let.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-28T15:32:54Z"
metadata:
  {}
---

# [hacker-news-sec] Critical OpenWrt DHCPv6 Flaw Could Let Unauthenticated Attackers Run Code as Root

> Source: security | Category: security | 2026-07-28T15:32:54Z

Critical OpenWrt DHCPv6 Flaw Could Let Unauthenticated Attackers Run Code as Root

OpenWrt has shipped version 24.10.8 to close a critical DHCPv6 stack overflow and a wider set of remotely triggerable flaws in network services enabled by default.

The critical issue, tracked as CVE-2026-53921 and rated 9.8 on CVSS 3.1 in OpenWrt's GitHub advisory, lets an unauthenticated attacker able to reach the DHCPv6 server overwrite a stack buffer in odhcpd through a crafted DHCPv6
