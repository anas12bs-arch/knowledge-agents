---
title: "Show HN: Word in Web – Near MS Word Parity Docx Editor in Web"
url: "https://word-in-web.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-21T19:57:34Z"
metadata:
  score: "6"
---

# Show HN: Word in Web – Near MS Word Parity Docx Editor in Web

> Source: hackernews | Category: news | 2026-07-21T19:57:34Z

Score: 6 | Comments: 0

Word in web is a pure JS docx editor&#x2F;renderer benched against MS Word directly. This was largely inspired by Eigenpal going closed source, and some personal frustrations I had with working on complex Word templates, pleading papers, etc... and not having a clean way to view&#x2F;edit them without owning MS Word (which I did just eventually buy but it sucked).<p>This was also an exercise in highlighting the value of good evals for Agents to bench against. Instead of just throwing the OOXML standard at an agent and letting it spin, I put together a large corpus of Microsoft Word docs - converted them to pdf and then rasterized them to images. The eval then compared the image diffs measuring the actual differences in the actual pixels. This let me (and more importantly, the agent) catch a lot of the edge cases and optimize aggressively while preventing &#x27;whack a mole&#x27; style regressions that would have made this project a lot harder.<p>Edit: I forgot to mention two things,
1. I published the full eval, including the raw diffs and delta over time so you can see all of the fixtures I actually tested against.<p>2. On the DX side, it ships as a typed React package and runs entirely in the browser. You can use it as a viewer or editor, customize the styling and visible toolbar features, build your own controls against the API, and decide where the edited DOCX bytes are saved, so it’s relatively easy to drop into another project
