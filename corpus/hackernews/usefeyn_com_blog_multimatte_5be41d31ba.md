---
title: "Show HN: MultiMatte, a Promptable Image Background Removal Model"
url: "https://usefeyn.com/blog/multimatte/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-10T18:26:01Z"
metadata:
  score: "10"
---

# Show HN: MultiMatte, a Promptable Image Background Removal Model

> Source: hackernews | Category: news | 2026-09-10T18:26:01Z

Score: 10 | Comments: 3

Hey HN, I&#x27;m Shreyash from Feyn. We help companies build custom models from their data.<p>Today we&#x27;re releasing MultiMatte, a background removal model you can aim with words. Name an object in your image. MultiMatte keeps just that thing, and removes everything else.<p>Try it out on your images: <a href="https:&#x2F;&#x2F;usefeyn.com&#x2F;multimatte&#x2F;">https:&#x2F;&#x2F;usefeyn.com&#x2F;multimatte&#x2F;</a>.<p>Demo video: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;XZ5BJWAkOjs" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;XZ5BJWAkOjs</a><p>MultiMatte is open source. Build with it using our NoBg library <a href="https:&#x2F;&#x2F;github.com&#x2F;feyninc&#x2F;nobg" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;feyninc&#x2F;nobg</a>. Model card here: <a href="https:&#x2F;&#x2F;hf.co&#x2F;feyninc&#x2F;multimatte" rel="nofollow">https:&#x2F;&#x2F;hf.co&#x2F;feyninc&#x2F;multimatte</a><p>MultiMatte is the second iteration of our background removal models. The first was FeyNoBg, which we released here <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=49072462">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=49072462</a>.<p>The big upgrade is promptability. Most models keep all foreground elements when cutting the background. MultiMatte lets you prompt the exact objects you want to keep and remove everything else. For example, If you have an image with a dog and a bowl, you can ask MultiMatte to keep just the dog.<p>MultiMatte is built on Meta&#x27;s SAM 3, a concept-promptable detector that already understands phrases. Our biggest change was in masking. Instead of binary masks that classify each pixel as being inside or outside an object, MultiMatte uses alpha mattes that assign an opacity value to each pixel, with respect to an object. This allows us to better represent hair, fur, motion blur, and other kinds of fuzzy boundaries.<p>Across all our measured benchmarks, MultiMatte shows a step improvement over SAM 3. On DIS5K, S-measure rises from 0.674 to 0.908 (a 34.6% relative gain), and on DUT-OMRON from 0.792 to 0.901 (13.7%).<p>Our blog covers more of the training details and results <a href="https:&#x2F;&#x2F;usefeyn.com&#x2F;blog&#x2F;multimatte">https:&#x2F;&#x2F;usefeyn.com&#x2F;blog&#x2F;multimatte</a>.<p>Happy to answer any questions!
