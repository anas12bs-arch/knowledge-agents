---
title: "[hacker-news-sec] Attackers Compile khunt Inside Oracle to Turn SQL Injection Into Windows SYSTEM Access"
url: "https://thehackernews.com/2026/08/attackers-compile-khunt-inside-oracle.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-08-06T11:30:42Z"
metadata:
  {}
---

# [hacker-news-sec] Attackers Compile khunt Inside Oracle to Turn SQL Injection Into Windows SYSTEM Access

> Source: security | Category: security | 2026-08-06T11:30:42Z

Attackers Compile khunt Inside Oracle to Turn SQL Injection Into Windows SYSTEM Access

Attackers broke into an organization's Oracle database through a SQL injection flaw in a public-facing web application, then installed a post-exploitation toolkit without writing an executable to disk. They fed Java source code to the database, let Oracle compile it into stored schema objects, and ran commands from inside the database engine.

Huntress, which tracks the toolkit as khunt,
