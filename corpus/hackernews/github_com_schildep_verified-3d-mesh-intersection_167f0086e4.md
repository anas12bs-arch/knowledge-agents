---
title: "Show HN: Formally verified 3D CSG: Trust 93 lines spec, not 1000 lines AI code"
url: "https://github.com/schildep/verified-3d-mesh-intersection"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-28T15:32:54Z"
metadata:
  score: "68"
---

# Show HN: Formally verified 3D CSG: Trust 93 lines spec, not 1000 lines AI code

> Source: hackernews | Category: news | 2026-07-28T15:32:54Z

Score: 68 | Comments: 22

To my knowledge, this is the first formally verified implementation of a 3D constructive solid geometry (CSG) operation: mesh intersection, implemented in Lean 4 and verified against a concise specification that pins down the surface of the resulting mesh exactly and guarantees practical well-formedness conditions on the triangulation.<p>This project is also an experiment in avoiding having to trust AI-generated code. A human reviewer only needs to read 93 lines of formal specification and run the Lean checker to certify the correctness of the kernel, skipping the intricate 1000+ lines of AI-written implementation. To prove correctness, AI autonomously wrote over 60,000 lines of Lean proofs, which also never have to be inspected by a human. The Lean checker guarantees conformance to the specification at compile time, with zero trust placed in any LLM. This allows us to treat the implementation and proofs as a black box. I guided the agent through the milestones described in the readme to arrive at the result presented here.<p>Also take a look at the web demo <a href="https:&#x2F;&#x2F;schildep.github.io&#x2F;verified-3d-mesh-intersection&#x2F;" rel="nofollow">https:&#x2F;&#x2F;schildep.github.io&#x2F;verified-3d-mesh-intersection&#x2F;</a>, which runs the verified mesh intersection kernel compiled to WebAssembly in your browser.
