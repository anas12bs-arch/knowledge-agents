---
title: "Show HN: Breathe CLI – Paced resonance breathing in the macOS terminal"
url: "https://github.com/marekkowalczyk/breathe-cli"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-05-31T09:50:31Z"
metadata:
  score: "25"
---

# Show HN: Breathe CLI – Paced resonance breathing in the macOS terminal

> Source: hackernews | Category: news | 2026-05-31T09:50:31Z

Score: 25 | Comments: 5

I built a terminal app that paces slow breathing at 6 breaths per minute for vagal tone training. It&#x27;s a single Python file, stdlib only, no dependencies — just run breathe and follow the bar.<p>I&#x27;m a cardiology patient (HFrEF). Slow breathing at resonance frequency is one of the few non-pharmacological interventions shown to improve cardiac vagal tone and baroreflex sensitivity (Bernardi et al., Circulation 2002; Lancet 1998). I wanted a frictionless daily habit tool — no app store, no account, no subscription, just open terminal and go.<p>Design constraints, all grounded in the clinical literature:<p>- No breath retention — Valsalva risk in cardiac patients<p>- No rapid breathing — minimum 8-second cycles<p>- Exhale ≤ 2x inhale — no evidence for extreme ratios<p>- Immediate exit, always — q or Ctrl+C restores the terminal even on crash<p>The README includes a resonance frequency measurement protocol for anyone with a chest-strap HRV monitor who wants to find their individual optimum instead of using the 6 bpm default.<p>macOS only (uses afplay for audio cues). MIT licensed.<p>pip install breathe-cli<p>or<p>brew tap marekkowalczyk&#x2F;breathe &amp;&amp; brew install breathe.
