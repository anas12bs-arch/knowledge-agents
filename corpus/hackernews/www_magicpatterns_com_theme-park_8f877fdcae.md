---
title: "Show HN: Build your own theme park"
url: "https://www.magicpatterns.com/theme-park"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-26T23:36:14Z"
metadata:
  score: "23"
---

# Show HN: Build your own theme park

> Source: hackernews | Category: news | 2026-08-26T23:36:14Z

Score: 23 | Comments: 14

I built an agent that helps you build Rollercoaster Tycoon-influenced theme parks. You can prompt something like “Build me a cool theme park” and it’ll build a cohesive theme park with multiple worlds and connected with paths and rides.<p>The weird part is that I built it using the same ideas we use to make AI-generated websites follow a company’s design system.<p>I work as an engineer at Magic Patterns, focused on building our Design System Agent, aimed to use your existing brand, components, and conventions instead of producing something that looks like generic AI-generated UI.<p>By default, models tend to converge on similar-looking designs. This is part of that “vibe coded slop” feeling: the same typography treatments, shadows, cards, icons, animations, etc…  My job is to figure out the right context and guardrails so that when you prompt “Build me a dashboard,” the result actually looks like your existing product.<p>At some point I realized those same ideas could be applied to RCT.<p>While in web, you might have rules about which typography, colors, spacing, and components should be used together.<p>In a theme park, you need rules like: rollercoasters need complete tracks, rides need entrances connected to paths, paths need to connect different areas of the park, and a pirate-themed world should actually use pirate-themed scenery.<p>It was interesting seeing how closely the problem of building a coherent theme park resembled the problem of building a coherent product UI. Similarly with web design, simply giving the model the right components wasn&#x27;t enough.<p>I ended up building an eval loop where Magic Patterns would generate a park, another agent would grade it against a rubric, and then the agent would update its rules and skill files before trying again.<p>The rubric checked things like whether rollercoasters formed valid tracks with at least one drop, whether rides were accessible by paths, whether each world used the appropriate themed scenery, and whether the park worked as a whole.<p>After a lot of iterations, you can now prompt something as simple as “Build me a cool theme park.” and you should get back a fully functioning park with guests, rides, paths, rollercoasters, and themed worlds.<p>Best yet, you can also follow the guests, listen to their thoughts, and watch them ride the rides in RCT fashion.<p>Happy to answer any questions, but would love to see the parks you all create!
