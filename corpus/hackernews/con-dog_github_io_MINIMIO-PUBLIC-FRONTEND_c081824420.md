---
title: "Show HN: Watch 14-Byte AI 'brains' attempt to solve a 2D maze (Its hard)"
url: "https://con-dog.github.io/MINIMIO-PUBLIC-FRONTEND/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-27T11:42:42Z"
metadata:
  score: "6"
---

# Show HN: Watch 14-Byte AI "brains" attempt to solve a 2D maze (Its hard)

> Source: hackernews | Category: news | 2026-07-27T11:42:42Z

Score: 6 | Comments: 2

Hey HackerNews,<p>I built this project over the last few weeks as a palette cleanser from a failed game launch.<p>I wanted to learn a bit about AI&#x2F;Neural-Networks and naively thought I could build a tiny maze-solving AI in a weekend with a 100% solve rate.<p>Well - I couldn&#x27;t, but I got pretty close. 14 Bytes total model size, and a 96.5% solve rate on unseen mazes. Trained across 46 phases experimenting with different ideas to improve the model (better performance, smaller size).<p>Its quite fun to watch the model attempt to solve the maze, when they fail its usually due to getting stuck in a loop. The models have no access to coordinates, map-data, or external memory scratches - they must navigate using only immediate local neighbourhood observations.<p>There is a model dropdown and you can see how the model has progressed over each phase, constantly getting smaller and increasing its solve rate. Total trained models number in the thousands - I just expose the winning models from each phase.<p>Overall a fun experiment, with much implementation help from AI agents to scaffold and implement the code (I&#x27;m a lazy software dev).
