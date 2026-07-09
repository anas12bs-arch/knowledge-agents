---
title: "Show HN: Arcaide – Explore code with multi-level call graphs"
url: "https://arcaide.foo"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-09T14:08:29Z"
metadata:
  score: "7"
---

# Show HN: Arcaide – Explore code with multi-level call graphs

> Source: hackernews | Category: news | 2026-07-09T14:08:29Z

Score: 7 | Comments: 2

One of the things I do when approaching a new codebase is to find the entry points and start exploring down the call paths. This gives a good overview of the different components in the code and how they&#x27;re connected. I wanted to translate that to a visual experience, similar to how you would use call graphs, but there&#x27;s a couple of problems with classical call graphs. One, call graphs represent flow at the function level, so the architectural context is lost. And call graphs tend to get very large and can grow exponentially with program size.<p>The approach I&#x27;m exploring is to construct &quot;multi-level&quot; call graphs. These are call graphs represented in the form of program structure showing control flow not just at the function level, but rolled up to higher level units such as classes and packages. This gives you the ability to zoom in and out and see your code at different levels of abstraction, à la C4 diagrams, allowing you to navigate large graphs by expanding the areas you care about and collapsing the rest.<p>The graph is then fed to an LLM for semantic analysis. This does two things, detects telemetry, trivial utilities to strip them out of the graph further condensing it, and identifies external interfaces and dependencies to enrich the graph. The result is a single graph which incorporates both structural and behavioral aspects. You can see package level dependencies, class composition and relationships, as well as external services, databases and user interactions. Think of it as a package diagram + class diagram + use case diagram combined into a single composite diagram.<p>Of course, ultimately source is king. There is no substitute for reading code to understand the details of what it is doing. But a map doesn&#x27;t replace the terrain, it tells you where to walk. As we shift from hand coding each line to orchestrating agents that are generating all the code, maintaining the &quot;big picture&quot; becomes ever more important. We need better maps to help us navigate the terrain.<p>I would love to hear what you think though. Do check out some of the example diagrams in the link [1] and share your feedback. Also interested in your general thoughts on program comprehension!<p>[1] Link: <a href="https:&#x2F;&#x2F;arcaide.foo" rel="nofollow">https:&#x2F;&#x2F;arcaide.foo</a>
