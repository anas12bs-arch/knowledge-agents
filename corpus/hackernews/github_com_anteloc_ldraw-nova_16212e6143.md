---
title: "Show HN: Made an open-source Lego AI generator"
url: "https://github.com/anteloc/ldraw-nova"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-02T21:52:19Z"
metadata:
  score: "39"
---

# Show HN: Made an open-source Lego AI generator

> Source: hackernews | Category: news | 2026-10-02T21:52:19Z

Score: 39 | Comments: 25

Hi there :-) New on HN, first time posting.<p>Past year, around December, I started experimenting with making ChatGPT and Claude generate source code in LDraw language.<p>This LDraw is literally an &quot;assembly&quot; language, a low-level programming language that describes how to assemble LEGO pieces together into models, one placement instruction at a time.<p>When executed by specific tools, like e.g. LDView, LeoCAD, Studio... these instructions become LEGO CAD models, that can be interacted with, modified, etc.<p>Or, in other words: one LDraw source file in .mpd or .ldr format is equivalent to one LEGO CAD model.<p>So, the idea I had was: if I manage for maybe ChatGPT or Claude to generate high-quality LDraw source files... then, they would actually be generating high-quality LEGO CAD models, right?<p>Then, after months of iterations and trying one thing after the other... it worked!!!<p>Long story short: using GPT-6 Astra and Opus 5.5, I&#x27;ve managed to create a python toolset, instructions, and docs for agents in general. Now, these can be used by them to generate LDraw models.<p>I&#x27;ve packed it all as a dockerized web app for others to try and experiment, with several providers (and agents) to choose from: OpenAI, Claude and OpenRouter.<p>I&#x27;d really appreciate feedback and comments, let&#x27;s see where this goes =)
