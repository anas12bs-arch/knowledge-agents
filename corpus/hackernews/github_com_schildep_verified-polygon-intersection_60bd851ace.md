---
title: "Show HN: Formally verified polygon intersection – Opus 4.8 oneshots, prev failed"
url: "https://github.com/schildep/verified-polygon-intersection"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-04T22:57:27Z"
metadata:
  score: "26"
---

# Show HN: Formally verified polygon intersection – Opus 4.8 oneshots, prev failed

> Source: hackernews | Category: news | 2026-06-04T22:57:27Z

Score: 26 | Comments: 2

To my knowledge, this is the first formally verified implementation of an intersection algorithm for polygons.<p>The experience of working with AI agents on this project changed a lot with recent model releases, as I describe in the readme. Opus 4.8 is able to provide algorithm implementation with formal proof in one shot, whereas previous models required me to provide proof strategies in multiple steps.<p>Trust in the correctness comes entirely from the Lean checker and human review of a small specification, not from the LLM.<p>Also check out the web demo built around the verified core linked in the readme: <a href="https:&#x2F;&#x2F;schildep.github.io&#x2F;verified-polygon-intersection&#x2F;" rel="nofollow">https:&#x2F;&#x2F;schildep.github.io&#x2F;verified-polygon-intersection&#x2F;</a>. It supports multipolygons including holes, self intersections, and overlapping edges.
