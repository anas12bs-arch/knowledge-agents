---
title: "[hacker-news-sec] curl Patches HTTP/2 Upload Flaw After PoC Demonstrates Client-Side Code Execution"
url: "https://thehackernews.com/2026/10/curl-patches-http2-upload-flaw-after.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-10-14T15:21:08Z"
metadata:
  {}
---

# [hacker-news-sec] curl Patches HTTP/2 Upload Flaw After PoC Demonstrates Client-Side Code Execution

> Source: security | Category: security | 2026-10-14T15:21:08Z

curl Patches HTTP/2 Upload Flaw After PoC Demonstrates Client-Side Code Execution

A flaw in how curl handles HTTP/2 uploads lets a malicious server receiving an upload corrupt the client's memory, and the researcher who reported it turned that into code execution on the uploading machine.

The curl project fixed it on October 14 in&nbsp;curl 8.23.0. Taking over a client needs exact knowledge of its build and memory layout, and curl expects a real attack to end in a crash
