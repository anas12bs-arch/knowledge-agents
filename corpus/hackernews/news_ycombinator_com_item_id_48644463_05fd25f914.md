---
title: "Overfitted a 900KB Transformer to Compress a 100MB CSV into 7MB"
url: "https://news.ycombinator.com/item?id=48644463"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-26T04:45:44Z"
metadata:
  score: "58"
---

# Overfitted a 900KB Transformer to Compress a 100MB CSV into 7MB

> Source: hackernews | Category: news | 2026-06-26T04:45:44Z

Score: 58 | Comments: 23

I built an experiment that uses an overfitted transformer and arithmetic coding to compress individual files.<p>Instead of training the model to generalize, I train a 900KB transformer to memorize a single file and predict the next byte. Those predictions are fed into an arithmetic coder to produce the compressed output.<p>On a 100MB NYC taxi CSV, it compresses to about 7MB (~0.5 bits&#x2F;byte). On a 100MB slice of enwik9, it compresses to about 21MB (~1.68 bits&#x2F;byte).<p>It&#x27;s pretty slow right now (roughly 20–30 minutes of training and 45 minutes each for compression and decompression on my AMD 7800XT).<p>Checkout the repo - <a href="https:&#x2F;&#x2F;github.com&#x2F;samyak112&#x2F;pym-particles" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;samyak112&#x2F;pym-particles</a>
