---
title: "Show HN: Syq – copy files between machines fast (better than rsync)"
url: "https://greaber.github.io/syq/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-10T18:26:02Z"
metadata:
  score: "19"
---

# Show HN: Syq – copy files between machines fast (better than rsync)

> Source: hackernews | Category: news | 2026-09-10T18:26:02Z

Score: 19 | Comments: 21

I got frustrated with the slowness of rsync and made an alternative that works faster by using multiple parallel connections, direct encrypted TCP when available, and other optimizations. I also added cool features like the ability to maintain a persistent ssh connection to the server for fast one-offs, the ability to download to your laptop while working in an ssh shell on a server, and the ability to do direct remote-remote transfers without forwarding your ssh agent (by using restricted ssh keys on the receiver that will only execute a specific request signed with the key on your laptop). It is also designed to be more robustly&#x2F;flexibly scriptable than alternatives.
