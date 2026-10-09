---
title: "Show HN: Proton Drive for Linux"
url: "https://oss.lsantos.dev/proton-drive-linux-fs/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-09T22:58:27Z"
metadata:
  score: "15"
---

# Show HN: Proton Drive for Linux

> Source: hackernews | Category: news | 2026-10-09T22:58:27Z

Score: 15 | Comments: 3

Hello everyone, I wanted to share this small project that I have.
It&#x27;s born out of a necessity that I had, because Proton doesn&#x27;t ship a Linux version of the drive yet (it&#x27;s apparently coming out later this year but who knows?) and all the current solutions are hacky and wonky at best. But for the time being I really needed to mount my Proton drive on my Linux machine the way I mounted it on my Mac, so I (and my faithful AI slave) did this small utility that allows you to mount your Proton Drive in a FUSE FS like if it is a local folder.<p>It&#x27;s fully written in Go because Proton&#x27;s drive SDK and API libs are all in Go, and there&#x27;s a community project on top of the reverse engineered proton API there too. I am not a Go developer, I know the foundations, so of course I used AI quite a lot, I am not super proud of it, but I am using it daily and testing it myself for a few months before releasing here.<p>Hope you like it, feedbacks are welcome, just please be mindful of the person on the other side :)
