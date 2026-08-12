---
title: "Show HN: Woxi - Open-source Mathematica / Wolfram Language reimplementation"
url: "https://woxi.ad-si.com"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-12T10:39:05Z"
metadata:
  score: "25"
---

# Show HN: Woxi - Open-source Mathematica / Wolfram Language reimplementation

> Source: hackernews | Category: news | 2026-08-12T10:39:05Z

Score: 25 | Comments: 1

Woxi is an interpreter for the Wolfram Language written in Rust.<p>It comes with Woxi Studio, a Mathematica-like GUI built with iced, but you can also use Woxi through a CLI, Jupyter kernel, Python package, npm package, or WASM module.<p>Compared with wolframscript &#x2F; Mathematica, the main differences are:<p>- Free and open source
- Very fast startup - Typically milliseconds rather than seconds for the Wolfram kernel, making Woxi practical for shell scripts, one-liners, and other short-lived processes
- Embeddable - It can run in a browser via WASM or be embedded into another application as a scripting language<p>A more detailed comparison with Mathematica is available here:
<a href="https:&#x2F;&#x2F;woxi.ad-si.com&#x2F;docs&#x2F;comparison&#x2F;mathematica&#x2F;" rel="nofollow">https:&#x2F;&#x2F;woxi.ad-si.com&#x2F;docs&#x2F;comparison&#x2F;mathematica&#x2F;</a>.<p>Conformance is ensured with ~26&#x27;000 unit tests and ~900 .wls script snapshot tests.<p>The current focus is on fixing remaining edge cases, improving performance, and growing the community.<p>If you use the Wolfram Language, I&#x27;d be particularly interested in feedback on compatibility and missing functionality.
Contributions and bug reports are also very welcome: <a href="https:&#x2F;&#x2F;github.com&#x2F;ad-si&#x2F;Woxi" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;ad-si&#x2F;Woxi</a>
