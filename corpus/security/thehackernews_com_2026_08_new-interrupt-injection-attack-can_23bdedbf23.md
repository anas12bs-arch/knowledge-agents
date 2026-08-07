---
title: "[hacker-news-sec] New Interrupt Injection Attack Can Bypass Spectre v2 Defenses on Intel and AMD CPUs"
url: "https://thehackernews.com/2026/08/new-interrupt-injection-attack-can.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-08-07T00:28:10Z"
metadata:
  {}
---

# [hacker-news-sec] New Interrupt Injection Attack Can Bypass Spectre v2 Defenses on Intel and AMD CPUs

> Source: security | Category: security | 2026-08-07T00:28:10Z

New Interrupt Injection Attack Can Bypass Spectre v2 Defenses on Intel and AMD CPUs

An unprivileged Linux program can time a hardware interrupt to land in the gap between a processor sanitizing its branch predictor and the kernel using it, re-poisoning the predictor after the defense has run.

MIT CSAIL researchers Daniël Trujillo and Mengjia Yan named the technique INTERRUPT INJECTION. On an AMD Zen 2 machine running Linux 6.14 with every default Spectre v2 mitigation on,
