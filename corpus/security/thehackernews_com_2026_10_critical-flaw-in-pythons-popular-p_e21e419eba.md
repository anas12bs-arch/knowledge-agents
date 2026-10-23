---
title: "[hacker-news-sec] Critical Flaw in Python’s Popular Pillow Image Library Allows Code Execution via a Crafted Image"
url: "https://thehackernews.com/2026/10/critical-flaw-in-pythons-popular-pillow.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-10-23T16:17:30Z"
metadata:
  {}
---

# [hacker-news-sec] Critical Flaw in Python’s Popular Pillow Image Library Allows Code Execution via a Crafted Image

> Source: security | Category: security | 2026-10-23T16:17:30Z

Critical Flaw in Python’s Popular Pillow Image Library Allows Code Execution via a Crafted Image

Pillow, the most widely used image library for Python, can be made to run operating system commands on a server by specifying the name of a file it is told to open.

The flaw,&nbsp;CVE-2026-112900, is in the way Pillow handles EPS images, which it opens by passing the file's name to Ghostscript, a separate program it runs to turn the image into pixels, without checking the name first.
