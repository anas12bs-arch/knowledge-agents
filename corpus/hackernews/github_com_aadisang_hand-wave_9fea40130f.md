---
title: "Show HN: Sign language translation with smart glasses"
url: "https://github.com/aadisang/hand-wave"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-08T11:01:57Z"
metadata:
  score: "3"
---

# Show HN: Sign language translation with smart glasses

> Source: hackernews | Category: news | 2026-08-08T11:01:57Z

Score: 3 | Comments: 1

Hi!<p>I have relatives that speak sign language, and always found it odd that despite unbelievable advances in AI in recent years, the problem still felt somewhat neglected.<p>Especially with the advent of wearable tech; to my knowledge, this is the first project that integrates the meta glasses w&#x2F; fingerspelling translation software.<p>As for the technical aspect, I trained a neural net on Google&#x27;s FSboard dataset modeling a CNN + GRU temporal encoder architecture (trained with CTC), and then decoded the output with CTC beam search and a KenLM language model to solve some of the deficiencies with my model.<p>I&#x27;ve also made it cross-platform (web + iOS, with both web screen sharing and the ability to use non smart-glasses). The project is entirely FOSS.<p>I&#x27;m currently working on making the on-device model work cleanly, but unfortunately performance takes a bit of hit on lower-end devices so for now I&#x27;ve opted for hosting the model on Modal.<p>There&#x27;s so much room for improvement, but I&#x27;m happy with this starting point. Let me know what you think, and check out the YouTube demo!
