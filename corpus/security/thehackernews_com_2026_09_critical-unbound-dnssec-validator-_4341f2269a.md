---
title: "[hacker-news-sec] Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone"
url: "https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-09-17T14:52:59Z"
metadata:
  {}
---

# [hacker-news-sec] Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone

> Source: security | Category: security | 2026-09-17T14:52:59Z

Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone

Every release of the Unbound DNS resolver before 1.26.1 has a critical heap overflow in its DNSSEC validator, maintainer NLnet Labs said in an&nbsp;advisory&nbsp;on Wednesday.

An attacker who controls a malicious zone and queries a vulnerable resolver can trigger it, enabling remote code execution.

Unbound 1.26.1, released the same day, fixes the bug, tracked as&nbsp;CVE-2026-81642, along with
