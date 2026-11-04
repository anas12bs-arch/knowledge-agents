---
title: "[hacker-news-sec] Debian and Ubuntu APT Flaw Lets MitM Attackers Swap Verified Packages and Run Code as Root"
url: "https://thehackernews.com/2026/11/debian-and-ubuntu-apt-flaw-lets-mitm.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-11-04T17:28:38Z"
metadata:
  {}
---

# [hacker-news-sec] Debian and Ubuntu APT Flaw Lets MitM Attackers Swap Verified Packages and Run Code as Root

> Source: security | Category: security | 2026-11-04T17:28:38Z

Debian and Ubuntu APT Flaw Lets MitM Attackers Swap Verified Packages and Run Code as Root

A flaw in APT, the package manager for Debian and Ubuntu, allows an attacker who can modify package downloads to swap a checked package for their own.

The attacker's code then runs as root, according to advisories that&nbsp;Debian,&nbsp;Ubuntu, and&nbsp;APT's developers&nbsp;published on November 4. The attack needs APT to retry failed downloads, which it does by default from Debian 12 and
