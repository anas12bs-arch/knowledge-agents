---
title: "Why can AI generate Super Mario but not a wedge ramp for my robot vacuum?"
url: "https://news.ycombinator.com/item?id=49405520"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-23T04:52:13Z"
metadata:
  score: "8"
---

# Why can AI generate Super Mario but not a wedge ramp for my robot vacuum?

> Source: hackernews | Category: news | 2026-08-23T04:52:13Z

Score: 8 | Comments: 5

I&#x27;ve been puzzled by something: AI generation can produce an elaborate
  figurine, a cartoon character, even a convincing Super Mario — yet it
  can&#x27;t reliably make a simple wedge ramp so my robot vacuum can climb a
  step.<p><pre><code>  For context: I bought a Bambu P2S but can&#x27;t model. I tried the &quot;describe
  it and get a model&quot; AIs — the output is unusable, you can&#x27;t adjust it,
  it&#x27;s never quite what I meant. I tried having an agent write Python to
  build geometry directly — it tops out at simple primitives.
 
  What finally worked: geometric decomposition. I break a complex part into
  ordered, grouped steps, describe each as a small spec, and let an agent
  execute them in Blender (via blender-mcp). That process turned out to
  abstract into a small engine — the key insight being it converts the 3D
  spatial reasoning LLMs are bad at, into the structured code they&#x27;re good
  at. I wrote it up here: https:&#x2F;&#x2F;github.com&#x2F;zhuchaokn&#x2F;spec-3d-model
 
  My questions:
  - Why is &quot;functional part&quot; generation so much weaker than
  &quot;figurine&#x2F;aesthetic&quot; generation? Is it data (no parametrized-CAD training
  sets), representation (mesh vs B-rep), or evaluation (nobody benchmarks
  &quot;does it print &#x2F; is it watertight&quot;)?
  - Is &quot;turn 3D modeling into code for an LLM&quot; the right framing, or am I
  missing something better?</code></pre>
