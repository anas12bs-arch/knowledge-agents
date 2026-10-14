---
title: "[hacker-news-sec] AI-Found Linux Kernel Flaw Gives Local Users Root, and Can Break a Guest Out to the Host"
url: "https://thehackernews.com/2026/10/ai-found-linux-kernel-flaw-gives-local.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-10-14T15:21:08Z"
metadata:
  {}
---

# [hacker-news-sec] AI-Found Linux Kernel Flaw Gives Local Users Root, and Can Break a Guest Out to the Host

> Source: security | Category: security | 2026-10-14T15:21:08Z

AI-Found Linux Kernel Flaw Gives Local Users Root, and Can Break a Guest Out to the Host

A flaw in Linux's vhost subsystem lets a local user read and write kernel memory at will and become root across nearly a decade of kernel versions. In one virtualization setup, it lets an untrusted virtual machine write to the host's memory and hijack the program that runs the virtual machine.

The bug is tracked as&nbsp;CVE-2026-74580&nbsp;and named Vghost. Tencent Zhuque Lab, which found the
