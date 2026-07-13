---
title: "Show HN: Jacquard, a programming language for AI-written, human-reviewed code"
url: "https://github.com/jbwinters/jacquard-lang"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-13T21:16:53Z"
metadata:
  score: "5"
---

# Show HN: Jacquard, a programming language for AI-written, human-reviewed code

> Source: hackernews | Category: news | 2026-07-13T21:16:53Z

Score: 5 | Comments: 0

I&#x27;m fascinated by the generative AI wave rolling over us, and wondered if AI could create a language that it might prefer using over the ones created by and for humans.<p>To create the design, I had AI analyze the ASTs of several mainstream languages plus a few of the conceptually groundbreaking but esoteric ones (listed in the README) and then create a new structure and new syntax. It was named after the Jacquard machine (<a href="https:&#x2F;&#x2F;en.wikipedia.org&#x2F;wiki&#x2F;Jacquard_machine" rel="nofollow">https:&#x2F;&#x2F;en.wikipedia.org&#x2F;wiki&#x2F;Jacquard_machine</a>), a precursor to Babbage&#x27;s Analytical Engine (and punch cards).<p>The result reused a lot of existing ideas but combined them in what I found to be an interesting way. External&#x2F;world effects are visible in function signatures, and the runtime requires explicit permission to touch the filesystem, network, etc. Effect interactions can be recorded and replayed to see what happens under different conditions or code. And since code is given a content-addressed semantic identity internally, renames and formatting changes don&#x27;t require recompile or retesting.<p>Another piece that fell out of this was a testing framework called Warp, which combines replay, results caching, handler substitution, and a few other tools that I frankly wish I had when writing Python. There are a few examples available in the demos directory.<p>There&#x27;s more to do, but it&#x27;s installable and usable. I&#x27;m hoping people will have their agents digest the docs&#x2F;SKILL.md file and maybe write a few programs or see where it might fit in their projects. It should be particularly useful in agent systems. If an agent says something is painful or you as a human find the code tough to understand, I&#x27;d like to hear about it so I can address it.<p>More detail here:<p>Repository: <a href="https:&#x2F;&#x2F;github.com&#x2F;jbwinters&#x2F;jacquard-lang" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;jbwinters&#x2F;jacquard-lang</a><p>Further intro&#x2F;human-oriented write-up here: <a href="https:&#x2F;&#x2F;research.friendmachine.co&#x2F;jacquard&#x2F;" rel="nofollow">https:&#x2F;&#x2F;research.friendmachine.co&#x2F;jacquard&#x2F;</a>
