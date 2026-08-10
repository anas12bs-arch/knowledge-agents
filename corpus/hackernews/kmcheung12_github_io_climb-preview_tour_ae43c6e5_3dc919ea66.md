---
title: "Show HN: My local climbing gym from photogrammetry"
url: "https://kmcheung12.github.io/climb-preview/tour/ae43c6e5"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-10T23:54:21Z"
metadata:
  score: "3"
---

# Show HN: My local climbing gym from photogrammetry

> Source: hackernews | Category: news | 2026-08-10T23:54:21Z

Score: 3 | Comments: 0

Commented on yesterday&#x27;s Ask HN: What are you working on? (August 2026), thought I might as well submit a Show HN.<p>If you see climbing world cup&#x2F;championship, there is this 3D modelling thing [1]. I want that for my weekly bouldering.<p>I scanned my local climbing gym into 3D mesh using iphone. Built a simple editor to trim, merge, move&#x2F;rotate meshes. You can interact with the mesh, view routes, view climb, etc. So this is unlike many gaussian splatting projects where the main use is for viewing. I built a pipeline in updating climbing walls. Climbing routes are manually annotated. Climbing videos are registered against the 3D mesh. Based on one input video, body positions resolved into 3D&#x2F;4D space. you can view the body landmarks from different angle.<p>COLMAP, OpenMVS, fastapi, svelte, database is just local json files. A read only build is exported so I can host on github page<p>If you climb, or know someone who climbs, would love to hear your feedback. Do you usually record your climbs? If I make this a service, what will make you use it?<p>[1] <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;shorts&#x2F;8zdUOaCr6DY" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;shorts&#x2F;8zdUOaCr6DY</a>
