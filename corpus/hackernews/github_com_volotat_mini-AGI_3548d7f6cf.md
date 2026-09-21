---
title: "Show HN: Mini-AGI – Dynamic continual learning model trained on 8GB VRAM"
url: "https://github.com/volotat/mini-AGI/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-21T13:13:28Z"
metadata:
  score: "170"
---

# Show HN: Mini-AGI – Dynamic continual learning model trained on 8GB VRAM

> Source: hackernews | Category: news | 2026-09-21T13:13:28Z

Score: 170 | Comments: 30

Sorry for the pretentious name, I know, I know.. It just contains all the pieces I would like to see a AGI model to have, and I can&#x27;t stand the temptation. Before throwing rocks at me, please take a glance at the Readme, and I hope it will cover your mood a little bit.<p>So, first of all it does work and you can see the sample from the whole training run here: <a href="https:&#x2F;&#x2F;raw.githubusercontent.com&#x2F;volotat&#x2F;mini-AGI&#x2F;refs&#x2F;heads&#x2F;main&#x2F;runs&#x2F;samples.txt" rel="nofollow">https:&#x2F;&#x2F;raw.githubusercontent.com&#x2F;volotat&#x2F;mini-AGI&#x2F;refs&#x2F;head...</a><p>Here is the scaling law graph I have so far, and it looks very promising:
<a href="https:&#x2F;&#x2F;github.com&#x2F;volotat&#x2F;mini-AGI&#x2F;blob&#x2F;main&#x2F;assets&#x2F;scaling.png" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;volotat&#x2F;mini-AGI&#x2F;blob&#x2F;main&#x2F;assets&#x2F;scaling...</a><p>The model was built under my deep dissatisfaction so we cannot really train even moderately big models (1B+ scale) on the consumer&#x27;s hardware. We can inference and fine-tune them for sure, but I would like to have full control over what the model sees over the training run, so it is fully aligned with my interests, not some corporations.<p>I was thinking about for some time and come up with two interesting ideas I thought worth pursuing: MoE with a lot of experts that gets added and pruned from the model while it trains, where only a small subset of of experts are actually in use at any particular moment + batch 1 training on the single continuous stream of data.<p>First allows us to be bounded only by the disk space in terms of number of parameters and load and unload experts only when they are needed. The second (if figured out and it turns out to be doable) allows us to get aways with small VRAM capacity because we do not need to store big randomized batches and their respective gradients.<p>I started brainstorming with Claude and after some time we found an approach that seems to be promising, and low and behold, a few weeks pass and you can see the results yourself.<p>Obviously, I did use AI in the process of making this project and I am pretty sure it would be completely impossible for me to do something like this without it, so I hope it is more than justified.<p>The model is still running over the first of 7.8B characters corpus I selected for training, so the weights are not out yet, and it&#x27;s about a couple weeks of waiting until they are cooked at the current reading speed. And yeah, the model just read continuous interleaved passages from the dataset, each by 32K characters long each as a single stream. Just as you or I would do.<p>The set up seems to be really simple so you can git clone the project, run it and observe everything for yourself.<p>Thanks for your attention.
