---
title: "Launch HN: Adam (YC W25) – Open-Source AI CAD"
url: "https://github.com/Adam-CAD/CADAM"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-17T20:37:13Z"
metadata:
  score: "102"
---

# Launch HN: Adam (YC W25) – Open-Source AI CAD

> Source: hackernews | Category: news | 2026-06-17T20:37:13Z

Score: 102 | Comments: 51

Hey HN! I&#x27;m Zach from Adam (<a href="https:&#x2F;&#x2F;adam.new&#x2F;">https:&#x2F;&#x2F;adam.new&#x2F;</a>). We&#x27;re building AI agents for mechanical CAD software. We’ve built the company on two fundamental beliefs:<p>- AI will be the primary medium for creating mechanical designs just like it is in software today.<p>- The best paradigm for CAD generation is to generate CAD as code (text -&gt; code -&gt; CAD).<p>We’re building CADAM, an open source Text to CAD platform. It&#x27;s a React app (TanStack Start) with a Supabase backend for auth, database, and file storage. Think of it like AI TinkerCAD.<p>Demo: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iESOr7EGWqk" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iESOr7EGWqk</a>
Try it: <a href="https:&#x2F;&#x2F;adam.new&#x2F;cadam&#x2F;">https:&#x2F;&#x2F;adam.new&#x2F;cadam&#x2F;</a><p>What it does:<p>- Generates parametric 3D models from natural language, with support for both text prompts and image references.<p>- Outputs OpenSCAD code with automatically extracted parameters that surface as interactive sliders for instant dimension tweaking<p>- Exports as .STL or .SCAD (plus OBJ, GLB&#x2F;GLTF, FBX, and DXF)<p>Under the hood:<p>- One agentic endpoint with two modes that swap system prompts and tools: a parametric mode that writes&#x2F;edits OpenSCAD via a build_parametric_model tool, and a mesh mode that generates 3D textured meshes.<p>- Simple parameter tweaks bypass the model entirely; adjusting a slider does a deterministic regex update on the SCAD source, requiring no LLM call.<p>- Model-agnostic via the Vercel AI SDK: Anthropic (Claude), Google (Gemini), and OpenAI&#x2F;others through OpenRouter, with adaptive thinking auto-enabled on newer models. Surprisingly, in our evals Gemini 3.1 Pro is the top model.<p>- Runs fully in-browser by compiling OpenSCAD to WebAssembly (in a Web Worker, so the UI never blocks) and rendering with Three.js via React Three Fiber<p>- Supports BOSL, BOSL2, and MCAD libraries, plus custom font support (Geist) for text in models<p>Future improvements:<p>- Support both build123d and CadQuery. This will allow us to move beyond CSG primitives to constraint-driven modeling and provide direct comparisons to other code-as-CAD primitives.<p>- Better spatial context: UI for face&#x2F;edge selection and viewport image integration to give LLMs spatial understanding<p>You can clone the repo and run it locally! Contributions are very welcome.
