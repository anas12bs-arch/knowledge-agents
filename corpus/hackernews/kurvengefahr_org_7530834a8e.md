---
title: "Show HN: Kurvengefahr – browser CAD/CAM for pen plotters"
url: "https://kurvengefahr.org/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-12T17:16:22Z"
metadata:
  score: "4"
---

# Show HN: Kurvengefahr – browser CAD/CAM for pen plotters

> Source: hackernews | Category: news | 2026-07-12T17:16:22Z

Score: 4 | Comments: 0

A few years ago I made a pen plotter attachment for Prusa MK4 (<a href="https:&#x2F;&#x2F;www.printables.com&#x2F;model&#x2F;827264-pen-plotter-attachment-for-prusa-mk4" rel="nofollow">https:&#x2F;&#x2F;www.printables.com&#x2F;model&#x2F;827264-pen-plotter-attachme...</a>) and at the time I didn&#x27;t have a good way to turn artwork into G-code for it, and I put the project on ice for a while.<p>I recently wanted to dabble in line art again and made a small browser app to make it easier. As agentic AI tools of 2026 are quite addictive, it rather quickly grew into something quite a bit more - an integrated browser CAD&#x2F;CAM for pen plotters that covers everything from importing existing artwork, creating artwork from scratch, preparing for plotting and hardware integration. It includes some off-beat features like a Logo interpreter for turtle art and Graves RNN for handwriting synthesis and in addition to 3D printer pretending to be pen plotters it now also supports actual pen plotters based on EBB (AxiDraw) and GRBL firmwares through Web Serial.<p>If you own an AxiDraw or a GRBL plotter, I&#x27;d very much appreciate it you gave it a try and give feedback. As I don&#x27;t own those, I did all the testing with a hardware mock on STM32, so I am not sure how well it works attached to an actual plotter.<p>Source code and docs are on GitHub:
<a href="https:&#x2F;&#x2F;github.com&#x2F;tibordp&#x2F;kurvengefahr" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;tibordp&#x2F;kurvengefahr</a>
