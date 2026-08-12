---
title: "Show HN: Line9 – A Mermaid rendering engine with its own layout"
url: "https://line9.ai/diagram"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-12T02:36:16Z"
metadata:
  score: "31"
---

# Show HN: Line9 – A Mermaid rendering engine with its own layout

> Source: hackernews | Category: news | 2026-08-12T02:36:16Z

Score: 31 | Comments: 6

Line9 is a new rendering engine for Mermaid flowchart diagrams that aims to remove the need for manual adjustment of layout. Mermaid is a popular text-based language for describing multiple types of diagrams.<p>Several Mermaid rendering engines already exist. Most, like the original mermaid.js, use Dagre or ELK graph drawing libraries to automatically lay out their diagrams. I’ve used Mermaid for the past four years but often recreated my flowcharts in a diagram editor so that I could modify the layout to something that better suited my needs.<p>Use Line9 when you want an automatic flowchart arrangement that optimises for clear communication. It seeks to layout flowcharts with regular grid spacing, closer positioning of related nodes, shorter, straighter edges and targets a page-like aspect ratio. The Compare button in the &#x2F;diagram page (share panel on the left) shows you the Line9 and mermaid.js renders next to each other.<p>Use for free, no account required. A CLI tool can also be downloaded for Mac, Windows and Linux. Free-use diagrams carry a watermark. Commercial use of the CLI requires a paid account and you also get diagrams without watermarks. Line9 is not open source (I need to create an income and the business model is being tested).<p>I’ve tried to encode and automate the layout principles I use when creating flowcharts by hand. All rendering takes place in the browser, so no private data is sent to the web service. The CLI is written in Rust and embeds the renderer so you get a single binary install and all data and processing remains local. It’s currently a little slower than mermaid.js, due to the difficulty of solving node positioning and edge routing simultaneously to find the layout that best meets the design principles.<p>Output is produced in SVG or PNG formats. Diagrams can also be shared via a URL with a fragment that embeds the Mermaid text.<p>Things I know still need improvement: positioning and rotating subgraphs, folding graphs to hit good aspect ratios more often, further improvement on edge label placement, better interaction with long node labels and tidying up the display when scaling down. Then I also want to support more diagram types and the website needs lots of work.<p>Please paste your own Mermaid flowcharts into Line9 – particularly the ones that you previously discarded because the layout was bad. Let me know whether they improve, or what other work is needed.
