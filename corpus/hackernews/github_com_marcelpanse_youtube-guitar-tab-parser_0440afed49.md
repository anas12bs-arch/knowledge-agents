---
title: "Show HN: YouTube Guitar Tab Parser"
url: "https://github.com/marcelpanse/youtube-guitar-tab-parser"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-13T21:16:51Z"
metadata:
  score: "17"
---

# Show HN: YouTube Guitar Tab Parser

> Source: hackernews | Category: news | 2026-07-13T21:16:51Z

Score: 17 | Comments: 8

I created a simple CLI that turns a YouTube guitar-lesson video into a PDF of the guitar tab.<p>There are services that transcribe music from Youtube videos into tabs, but they never work well enough for me. Instead I&#x27;m taking a simpler approach. 
It downloads the video, samples frames, uses Claude vision to locate the tab region, crops every frame to that region, de-duplicates the crops by the bar number printed on each line of the score, and stitches the distinct tab lines vertically into a PDF.<p>I didn&#x27;t test it on a lot of different Youtube videos yet, so problem will arise for sure.
