---
title: "Show HN: LuaCAD – Parametric CAD Scripted in Lua"
url: "https://luacad.ad-si.com"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-14T18:02:22Z"
metadata:
  score: "16"
---

# Show HN: LuaCAD – Parametric CAD Scripted in Lua

> Source: hackernews | Category: news | 2026-08-14T18:02:22Z

Score: 16 | Comments: 3

LuaCAD models solids in Lua rather than the OpenSCAD language, with operator
overloading for CSG (`a + b`, `a - b`, `a * b`).<p>It ships with a CLI and a desktop app, including a preview area and a text editor.<p>I&#x27;ve always been a big fan of OpenSCAD, but the SCAD language itself is unfortunately quite cobbled-together and is a very poorly designed programming language.<p>LuaCAD takes all the good parts of OpenSCAD and combines them with one of the best scripting languages. It has now completely replaced OpenSCAD for me, and I think it provides a better experience than OpenSCAD for all use cases. I&#x27;d love to hear any reasons why LuaCAD shouldn&#x27;t fully replace OpenSCAD!<p>Tech stack:<p>- It&#x27;s implemented in Rust and uses mlua (<a href="https:&#x2F;&#x2F;github.com&#x2F;mlua-rs&#x2F;mlua" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;mlua-rs&#x2F;mlua</a>) to execute the Lua code.<p>- Uses OpenCSG (<a href="https:&#x2F;&#x2F;opencsg.org" rel="nofollow">https:&#x2F;&#x2F;opencsg.org</a>) for fast and correct rendering of the 3D models (like OpenSCAD)<p>- Uses Manifold (<a href="https:&#x2F;&#x2F;github.com&#x2F;elalish&#x2F;manifold" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;elalish&#x2F;manifold</a>) to create the manifold triangle meshes<p>- Native support for all BOSL2 functions (i.e. implemented in Rust for better performance)
