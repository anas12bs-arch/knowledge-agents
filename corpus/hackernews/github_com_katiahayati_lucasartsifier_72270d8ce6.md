---
title: "Show HN: Automatically detect and patch walking-dead states in Sierra games"
url: "https://github.com/katiahayati/lucasartsifier/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-19T04:09:13Z"
metadata:
  score: "5"
---

# Show HN: Automatically detect and patch walking-dead states in Sierra games

> Source: hackernews | Category: news | 2026-08-19T04:09:13Z

Score: 5 | Comments: 2

Hi HN, I&#x27;ve become lazier in my old age and struggle to replay my favorite Sierra games from the 80s and 90s because I keep getting into those situations where I need an item from 3 acts ago, I have no save game handy, and now I gotta make dinner.<p>So I&#x27;m building the Lucasartsifier: a static analysis tool that decompiles Sierra resource files, automatically finds those states, automatically generates code to prevent the player from getting into those states, then emits loose patch files that can be placed alongside the original game resources. There&#x27;s no game-specific code involved; all the logic is generic, though of course Sierra introduces new idioms and mechanics in every game so every new supported game needs a bunch of engine work.<p>So for example in Leisure Suit Larry 2, the patched game prevents you from boarding the cruise ship until you have both the sunscreen and the Grotesque Gulp. Without them you die on the raft 3 play-hours later.<p>So far this works on Leisure Suit Larry 2 (SCI0), King&#x27;s Quest 4 (SCI0), King&#x27;s Quest 6 (SCI1.1), and Laura Bow 2 (SCI1.1). I&#x27;m currently working on King&#x27;s Quest 5 (SCI1.0).<p>This is work done with Claude -- I do the design and playtesting and it does the rest :D<p>Any feedback, play testing, and suggestions would be great!
