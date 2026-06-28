---
title: "Show HN: Metaspec: The DpANS3R Common Lisp Spec in S-Expr and HTML Format"
url: "https://metaspec.dev/#"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-28T08:14:17Z"
metadata:
  score: "6"
---

# Show HN: Metaspec: The DpANS3R Common Lisp Spec in S-Expr and HTML Format

> Source: hackernews | Category: news | 2026-06-28T08:14:17Z

Score: 6 | Comments: 0

I started this project back in 2015, to translate the TeX original specification into an easily parsed format (s-doc), and to create an HTML rendering of that format as a proof of concept.<p>The project is homed here: <a href="https:&#x2F;&#x2F;codeberg.org&#x2F;dlowe&#x2F;metaspectre&#x2F;" rel="nofollow">https:&#x2F;&#x2F;codeberg.org&#x2F;dlowe&#x2F;metaspectre&#x2F;</a><p>Differences from the Hyperspec (from the README):<p><pre><code>  - Most importantly, it is free to modify and distribute.
  - The original TeX is very hard to parse and use for things other than
    generating a printed copy. The Hyperspec is an HTML rendering which
    can be parsed as HTML, but loses a lot of information. The Metaspec
    has an easily parsed intermediate form that can be used for all kinds
    of purposes, like converting into lookups.
  - Math equations are rendered using MathML.
  - Includes the acknowledgements and appendix sections.
  - Uses progressively enhanced Javascript to provide search and
    light&#x2F;dark theme switching.
  - Incorporates over 145 patches for content, using corrections
    accumulated over the years, and documented in the errata page.
  - Includes TeX comments, which can contain interesting historical data.
  - Includes links and identifiers to bibliographical references.</code></pre>
