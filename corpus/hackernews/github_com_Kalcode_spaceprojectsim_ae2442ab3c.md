---
title: "Show HN: A self-running space economy SIM in Rust and Bevy"
url: "https://github.com/Kalcode/spaceprojectsim"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-21T19:57:30Z"
metadata:
  score: "25"
---

# Show HN: A self-running space economy SIM in Rust and Bevy

> Source: hackernews | Category: news | 2026-07-21T19:57:30Z

Score: 25 | Comments: 4

I built this with Claude cause I always wanted to tinker with a simulation economoy and I love space themes.<p>A space-economy sim where nothing is scripted. A few hundred autonomous ships each run their own planner. Some chase the best trade route, take a delivery contract, refuel, retrofit at a shipyard, or dock so the crew can rest before morale tanks.<p>Markets price everything off supply with shortage-urgency multipliers, factions tax and subsidize, populations migrate when they&#x27;re unhappy, and stations that go broke get abandoned and rot.<p>It started as an Elixir&#x2F;Phoenix prototype, but the BEAM scheduler struggled on Windows gaming PCs, so I had Claude rewrite the engine in Rust.<p>The sim core is pure, synchronous, IO-free (its own hecs ECS), and the Bevy client embeds it directly as a library, sim and renderer share one world with zero marshalling. Ship AI is a GOAP planner over a world state; ships replan mid-flight when a better option appears. ~485 agents today at p50 ~10-20ms&#x2F;tick, architected to push toward 100k+. Single native binary, bundled SQLite, no runtime deps. Getting into 100k has been a struggle, but I have pushed it into the thousand and it was running fine.<p>It&#x27;s a sandbox, not a game yet, there&#x27;s no objective yet, and I&#x27;m not actively pushing it toward &quot;shippable.&quot; Anyone can fork it and take it over. Or it can stay as some type of AI slop, but part of me thinks it is already in a pretty good shape for a simulation use for various games or ideas.<p>(Full disclosure: a lot of this was built pairing with Claude. That&#x27;s how I had the bandwidth to take it this far. Happy to talk about what that workflow actually looked like.)
