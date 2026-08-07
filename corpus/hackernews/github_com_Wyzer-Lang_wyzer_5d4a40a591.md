---
title: "Show HN: Wyzer Programming Language"
url: "https://github.com/Wyzer-Lang/wyzer"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-07T14:28:11Z"
metadata:
  score: "22"
---

# Show HN: Wyzer Programming Language

> Source: hackernews | Category: news | 2026-08-07T14:28:11Z

Score: 22 | Comments: 9

So i&#x27;ve been working on this project since a few days (or months i should say), it&#x27;s called wyzer (meaning wiser) it&#x27;s a statically typed, compiled, resource-oriented programming language with integrated distributed safety via choreographic programming and perceus memory model, The reason why i began this project is out of frustration from Rust, you see it does provide safety for your memory by the strict type checking but what it does not gurantee safety against are distributed deadlocks which is basically a few independent nodes or services wait permanently for resources or messages held by each other, forming a circular wait, the rest are cross-service correctness and protocol mismatch as well. If we are specific over here Wyzer works on mainly generalizing the concept of choreographic programming in a high level programming language because its the very few attempts of actually solving these gaps of safety. Instead of borrow checkers and lifetimes wyzer has linear&#x2F;affine types and a perceus reference counting which is computationally much simpler for an LSP to understand as well<p>after 5 months of research and a few weeks of development i am soon going to release version 0.1.0 of it, if you would like to contribute to it you&#x27;re most welcome!
