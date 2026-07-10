---
title: "[hacker-news-sec] Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers"
url: "https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-10T13:31:35Z"
metadata:
  {}
---

# [hacker-news-sec] Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers

> Source: security | Category: security | 2026-07-10T13:31:35Z

Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers

A single wrong variable on one line in XQUIC, Alibaba's QUIC and HTTP/3 library, lets any remote client crash the server with a short burst of completely legal traffic. There is no patch.

FoxIO researcher Sébastien Féry&nbsp;disclosed the flaw on July 8&nbsp;and nicknamed it XRING. He says it needs no login and no malformed packets: about 260 bytes of ordinary QPACK traffic takes the server
