---
title: "Show HN: SeasonMap – when to travel where? visualized with climate data"
url: "https://seasonmap.app"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-16T22:21:00Z"
metadata:
  score: "8"
---

# Show HN: SeasonMap – when to travel where? visualized with climate data

> Source: hackernews | Category: news | 2026-09-16T22:21:00Z

Score: 8 | Comments: 8

Author here. I&#x27;m trying to visit every country and I&#x27;ve been to 158 so far.<p>Before I decide where to travel, I&#x27;d ask a local friend which season to avoid, or open up dozens of browser tabs on climate data to figure out what the place is like in a given month.<p>Climate data still miss things. Cancun in September looks great on paper, with 31°C and 10 hours of sun, but it&#x27;s hurricane season and the beaches can be covered in seaweed.<p>Typical info that locals would know, which can also be captured as static data.<p>So I built SeasonMap to answer &quot;when should I go to &lt;place&gt;?&quot;<p>What you can do:<p>- Pick a travel style (city walk, beach, hiking, skiing, max sun, low humidity, etc.) and see every place ranked on a map<p>- See what&#x27;s in season and what to avoid, and why: monsoon, hurricanes, extreme heat, bad air, peak crowds<p>- Filter destinations by temperature, rainfall, sunshine, air quality and hazard seasons<p>- Open a place to see its whole year: month by month weather, events (festivals, whale watching, cherry blossom), crowd levels, practical notes like scams, and traveller anecdotes summarized by AI with links to the sources<p>Data Source &amp; how I made it:
- The climate data is ERA5 normals via Open-Meteo (2016–2025), corrected with NOAA station data where available.<p>- Events, hazards and traveller notes were researched and by AI agents, and every one links to its source. Gathering it was easy. Checking it was the hard part.<p>- Yes, I&#x27;ve used AI heavily on this project before anyone call it an AI slop. Making was easy, but it took billons of tokens of beating whack-a-mole ai to polish and tweak to make it usable and decent. Through that, I&#x27;ve created many skills and evals ranging from visual qa, evals for irregular data, automated i18n and others. It still feels much like AI as I was using Claude Design, which i want to improve on. I tried using local llm, but the throughput was so low.<p>Pricing: the first 5 minutes are fully open, no signup. After that, the top 3 destinations and 25 place breakdowns a month are free. A 30-day pass is $7, $39 a year or $69 lifetime.<p>iOS and Android apps are coming soon.<p>Any feedback welcome.
