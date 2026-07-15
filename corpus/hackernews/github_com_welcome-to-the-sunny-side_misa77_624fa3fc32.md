---
title: "Show HN: misa77 - a codec that decodes 2x faster than LZ4 (at better ratios)"
url: "https://github.com/welcome-to-the-sunny-side/misa77"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-15T17:07:54Z"
metadata:
  score: "28"
---

# Show HN: misa77 - a codec that decodes 2x faster than LZ4 (at better ratios)

> Source: hackernews | Category: news | 2026-07-15T17:07:54Z

Score: 28 | Comments: 1

I&#x27;ve spent the last few months working on this codec.<p>It has the following characteristics:<p><pre><code>  - SOTA decompression throughput in its ratio class
  - Decent ratios (comparable to LZ4 at high effort levels)
  - Slow compression
</code></pre>
Most of the gains can be attributed to reducing branches and making decompression very friendly to out-of-order cores, by using a smart format.<p>Results on the tarred Silesia corpus on Intel x86-64 follow:<p><pre><code>  codec       decode      ratio    encode
  misa77 -0   5219 MB&#x2F;s   42.64%   54.5 MB&#x2F;s
  misa77 -1   4274 MB&#x2F;s   39.65%   51.2 MB&#x2F;s
  lz4         2505 MB&#x2F;s   47.59%   371 MB&#x2F;s
  lz4hc -12   2531 MB&#x2F;s   36.45%   7.31 MB&#x2F;s</code></pre>
