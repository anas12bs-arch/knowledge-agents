---
title: "Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly"
url: "https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-03T19:49:07Z"
metadata:
  score: "75"
---

# Porting my 1993 Amiga game to Godot, with an LLM reading the 68000 assembly

> Source: hackernews | Category: news | 2026-09-03T19:49:07Z

Score: 75 | Comments: 26

These are my notes from porting my Amiga game, which I originally built in Baghdad in 1993 in MC68000 assembly, to Godot, using Claude Fable 5 during last July holiday.  It took an evening! Getting the feel right and shipping it took a few more weekends and evenings.<p>I spent the last few weeks analyzing what Claude did, feeding it my 33 years of memory of how I built the game, my notes and the git repos. It wrote the first draft of the article, and I edited line by line over a week. The screenshots of my 1993 map editor is the first I have run it since then. The one thing I never verified myself is the 108-byte explanation.<p>&quot;Before starting everything, the model assembled the code using vasm on my Mac, and kept going till the binary is byte-identical to the binaries I had in my original game. Even after that, the there was mismatch of about 108 bytes. I originally used AsmOne  which assembles into memory, and the game saved into the disk by saving that memory after running the game. So the original shipped files are a snapshot of the game that had already been running, not clean asm-one output.&quot;<p>Please post any questions. I am also releasing the original game for free.
