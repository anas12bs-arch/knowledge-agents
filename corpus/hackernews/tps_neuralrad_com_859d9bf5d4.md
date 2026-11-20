---
title: "Show HN: Radiotherapy Delivery Demo"
url: "https://tps.neuralrad.com"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-11-20T17:55:12Z"
metadata:
  score: "18"
---

# Show HN: Radiotherapy Delivery Demo

> Source: hackernews | Category: news | 2026-11-20T17:55:12Z

Score: 18 | Comments: 6

The treatment planning station (TPS) software field is currently monopolized by Varian&#x27;s Eclipse and Raystation from Raysearch. Current software is still using technology stack 2 decades old.<p>At UT Southwest Medical Center, we are working on a technology stack which is leveraging modern browser technology using WebAseembly and WebGPU for implementing not only the 2D and 3D display of treatment delivery but also GPU-accelerated dose calculation engine running inside browser to simulating dose deposition and plan delivery.<p>This would enable accessibility of the technology and much easier to explain the treatment planning process to the patients. This post is a demo of how the system works.<p>Originally developed by Chris Kabat at UT Southwestern Medical Center using three.js. Neuralrad rewrote it with Rust stack and build into wasm module.
