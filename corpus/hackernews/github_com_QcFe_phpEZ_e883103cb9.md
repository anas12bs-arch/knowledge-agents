---
title: "Show HN: PhpEZ – A tiny PHP framework for shared LAMP hosting"
url: "https://github.com/QcFe/phpEZ"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-29T21:03:34Z"
metadata:
  score: "4"
---

# Show HN: PhpEZ – A tiny PHP framework for shared LAMP hosting

> Source: hackernews | Category: news | 2026-08-29T21:03:34Z

Score: 4 | Comments: 1

I needed to make a tiny webapp backend to upload to shared LAMP hosting (they still exist, and I think they&#x27;re fun despite us being well beyond 2005), but I couldn&#x27;t face waiting for FTP to sync down however thousands files Laravel or similar frameworks need.<p>So I made a tiny PHP framework that gets packaged into a single file.<p>I&#x27;m using it for my own shady purposes, but I decided to put it on GitHub in case anyone else finds the approach useful.<p>It has typed request&#x2F;response handling, filesystem-based routing, object serialization, database models&#x2F;schema generation, and a little schema alignment tool. It has no Composer dependencies.<p>It&#x27;s very much a tiny thing, but if anyone wants to try it and tell me where it breaks, I&#x27;d appreciate it :)
