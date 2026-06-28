---
title: "Show HN: NanoEuler – GPT-2 scale model in pure C/CUDA from scratch"
url: "https://github.com/JustVugg/nanoeuler"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-28T21:13:32Z"
metadata:
  score: "15"
---

# Show HN: NanoEuler – GPT-2 scale model in pure C/CUDA from scratch

> Source: hackernews | Category: news | 2026-06-28T21:13:32Z

Score: 15 | Comments: 2

Hi everyone,<p>I started working on nanoeuler after the ban of anthropic&#x27;s fable because my ambition and dream is to work in the AI   field in anthropic. The two interesting reasons that led me to create nanoeuler were (1) interfacing with llm does not mean understanding how they are composed and (2), working on llm with a very low-level layer to understand the correlation between parameters and data and growth of the model and how the GPU works and how some layers can be optimized.<p>So I started working on it with a research aspect by making nanoeuler grow more and more but doing one step after another starting from Shakespeare.txt and understanding what a text generation model understands at 23 million parameters. For example, nanoeuler at that number had understood that Name: started a line and wrote that line with sense.<p>I wrote everything in CUDA because I wanted to not use any intermediary between the model in training and inference and what it had to do. Then the use of SFT and much more, even if in small ways, were really useful to understand the various step to make an llm like a chatbot.Any feedback, help, or suggestions are absolutely welcome!
