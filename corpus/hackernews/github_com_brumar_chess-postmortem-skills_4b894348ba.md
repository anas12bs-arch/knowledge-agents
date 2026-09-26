---
title: "Show HN: A Claude Code skill to analyze your chess games"
url: "https://github.com/brumar/chess-postmortem-skills"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-26T17:51:01Z"
metadata:
  score: "37"
---

# Show HN: A Claude Code skill to analyze your chess games

> Source: hackernews | Category: news | 2026-09-26T17:51:01Z

Score: 37 | Comments: 26

Hello HN,<p>It started as an experiment: can Claude play chess properly if it uses vision instead of PGN notation? Somehow it can.<p>The next experiment was to see whether Claude + Stockfish could explain a game. Somehow it can too.<p>A few sessions later, I had a system that takes my live audio notes (or text, for that matter) and a vague instruction like &quot;analyze my last lichess game&quot;, and gives me a commented video of the game. The result is not perfect and it takes time to deliver (an hour or so), but for me it is a much more pleasant and memorable experience than clicking around Stockfish branches. It burns tokens, so make sure you have enough quota. From the session logs, the last analyzed game would have cost around $15 at API prices.<p>The fact that it reflects on my own thinking during the game makes it interesting from a teaching point of view, so I thought it was worth sharing.
