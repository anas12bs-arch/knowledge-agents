---
title: "[hacker-news-sec] Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code Remotely"
url: "https://thehackernews.com/2026/10/unpatched-critical-lmcache-flaw-lets.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-10-07T16:21:18Z"
metadata:
  {}
---

# [hacker-news-sec] Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code Remotely

> Source: security | Category: security | 2026-10-07T16:21:18Z

Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code Remotely

A critical vulnerability in LMCache, open-source software that speeds up large language model (LLM) servers such as vLLM, lets an attacker run code on the cache server without logging in, and no fixed version is available.

The flaw is in LMCache's&nbsp;multiprocess mode, where the cache runs as a standalone server that LLM workers reach over the ZeroMQ messaging library. A single network
