---
title: "Show HN: Manim (3Blue1Brown's animation engine) in the browser via WebGPU"
url: "https://studio.academa.ai/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-29T01:10:42Z"
metadata:
  score: "13"
---

# Show HN: Manim (3Blue1Brown's animation engine) in the browser via WebGPU

> Source: hackernews | Category: news | 2026-07-29T01:10:42Z

Score: 13 | Comments: 6

Grant Sanderson (3Blue1Brown) created Manim, the Python library he uses to make the math animations in his videos.<p>We reimplemented Manim with the same Python API, but the implementation underneath is Rust, connected to Python through PyO3. The Rust code uses wgpu, so rendering happens on the GPU.<p>To run it in the browser, we compiled the Rust parts to WebAssembly so the PyO3 extension loads in Pyodide. In the browser, wgpu targets the WebGPU API, so animations render in real time on your GPU through the browser.<p>The editor is Monaco (the editor that powers VS Code) with a live preview: write your Manim code on one side, watch the animation update on the other.<p>There&#x27;s also a built-in AI agent if you&#x27;d rather vibe-code your animations.
