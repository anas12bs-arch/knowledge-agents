---
title: "Show HN: SIMD Viterbi Decoder in Rust"
url: "https://github.com/brian-armstrong/fec"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-04T23:42:43Z"
metadata:
  score: "3"
---

# Show HN: SIMD Viterbi Decoder in Rust

> Source: hackernews | Category: news | 2026-08-04T23:42:43Z

Score: 3 | Comments: 0

I wrote libcorrect in C in 2016 and wanted to revisit it in Rust. Instead of doing just a direct conversion, I went down the rabbit hole of making Rust&#x27;s std::simd work for me. I ended up with a templated, generic Viterbi decoder for convolutional codes that dispatches the decode at runtime depending on which instruction sets are available. For small rates and orders, the entire decode lives in registers. Larger codes work through memory but take advantage of some acceleration structures.<p>I also spent some time building a tool to find optimal (max d_free) conv codes for a given rate and order. Of course, there are better mechanisms available today, but I&#x27;m happy to talk through anything I learned in the process.
