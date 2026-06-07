---
title: "Show HN: I Derived a Pancake"
url: "https://www.absurdlyoptimized.com/recipes/pancakes/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-07T23:42:50Z"
metadata:
  score: "64"
---

# Show HN: I Derived a Pancake

> Source: hackernews | Category: news | 2026-06-07T23:42:50Z

Score: 64 | Comments: 20

After 25 years of making other people&#x27;s pancake recipes - always yearning for more tang, more fluff, and more predictability - I decided to derive the pancake recipe from the chemistry.<p>You mark checkboxes for what you have on hand (ricotta, sour cream, kefir, buttermilk, yogurt, cottage cheese, lemon, cream of tartar, etc.) and it  computes the best recipe based on targets for acid, fat, salt, sugar, and CO2.<p>My particular favorite are the yeast-raised lemon ricotta kefir pancakes - the best I&#x27;ve ever had.<p>The math is done in a small pure-ESM library: ingredient composition to component masses and acid moles, a stoichiometry layer, and a bisection solver for the target deficits.<p>I&#x27;m not a chemist, so if something is off, tell me and I will fix it!
