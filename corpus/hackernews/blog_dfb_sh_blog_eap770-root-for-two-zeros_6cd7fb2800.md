---
title: "Wanted to download an ISO, ended up writing a kernel exploit"
url: "https://blog.dfb.sh/blog/eap770-root-for-two-zeros/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-15T09:52:53Z"
metadata:
  score: "84"
---

# Wanted to download an ISO, ended up writing a kernel exploit

> Source: hackernews | Category: news | 2026-10-15T09:52:53Z

Score: 84 | Comments: 31

Author here. Does anyone know what to do with the rest of the drivers? I found at least 13 in-tree drivers with the same bug class. The nasty part is they work fine on x86 and silently corrupt data on arm and other non-coherent archs, and I don&#x27;t have the hardware to test them.<p>I&#x27;d guess that&#x27;s what the DMA API is for and drivers shouldn&#x27;t be doing cache maintenance by hand, but I&#x27;m not a kernel dev, so maybe I&#x27;m missing something.
