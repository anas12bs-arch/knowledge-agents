---
title: "Show HN: TerrainSR – fast, realistic heightmap upscaling model"
url: "https://huggingface.co/joe-gibbs/terrainsr"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-09T00:18:30Z"
metadata:
  score: "23"
---

# Show HN: TerrainSR – fast, realistic heightmap upscaling model

> Source: hackernews | Category: news | 2026-10-09T00:18:30Z

Score: 23 | Comments: 5

This is a model that I made for a historical game. I wanted to have a 1:1 scale model of Europe, but my problem was that 100m data was too low-res while 10m LIDAR data was patchy, took hundreds of GBs to store and was full of manmade objects like mines, buildings and so on.<p>I trained this model on undeveloped landscape so that it can quickly add plausible erosion features, rocks, etc to the low-resolution height data and sort of reconstruct what the terrain would look like before any human interference.
