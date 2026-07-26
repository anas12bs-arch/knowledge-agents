---
title: "Show HN: A browser-based video editor that renders videos directly with FFmpeg"
url: "https://github.com/thiagoalbrecht/weave"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-26T17:32:38Z"
metadata:
  score: "6"
---

# Show HN: A browser-based video editor that renders videos directly with FFmpeg

> Source: hackernews | Category: news | 2026-07-26T17:32:38Z

Score: 6 | Comments: 2

Weave is a React app that provides a multi-track timeline editor to perform basic video edits like trimming, stitching, transitions, audio tracks etc. which maps directly to an FFmpeg command to render the video.<p>I tried my best to have the React &quot;video&quot; preview closely replicate the FFmpeg lavfi filtergraph output, but naturally this is not perfect (especially replicating the `eq` filter using SVG filters is quite inaccurate).<p>I&#x27;ve built this as a prototype for another project I&#x27;m working on, so I don&#x27;t plan to actively maintain it, but I thought it&#x27;d be cool to share it.<p>Try it live: <a href="https:&#x2F;&#x2F;weave.salviano.xyz&#x2F;" rel="nofollow">https:&#x2F;&#x2F;weave.salviano.xyz&#x2F;</a>
