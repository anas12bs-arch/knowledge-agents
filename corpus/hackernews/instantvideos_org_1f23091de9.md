---
title: "Show HN: InstantVideos.org – short documentaries in ~30 seconds"
url: "https://instantvideos.org/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-07T01:26:39Z"
metadata:
  score: "4"
---

# Show HN: InstantVideos.org – short documentaries in ~30 seconds

> Source: hackernews | Category: news | 2026-07-07T01:26:39Z

Score: 4 | Comments: 6

Hiya! So I&#x27;ve been playing around with having Claude make videos for a bit now even had some success posting the results to TikTok (and setup a whole pipeline so Claude can generate and post autonomously). With the release of Nano Banana 2 Lite, I was curious show fast I could make the generation, so last night I gave it a whirl and got down to around 30s for short-form video.<p>It uses GLM-5.2 fast via Fireworks to generate the scripts and image prompts and, like I said, Nano Banana 2 Lite for the images, gpt-4o-mini-tts for the narration, and ffmpeg to string it all together and add the Ken Burns zoom effect (which still has a shake I haven&#x27;t been able to get rid of). The video compilation proved to be the blocker once the rest was in place, but I was able to speed that up by putting it on a 64 vCPU EC2.<p>The cost might be the most interesting aspect as the short form videos tend to be about 25 cents. Almost 90% of that is the images, which are 3.336 cents a piece. Of course, running the big 64 core EC2 to allow for the creation isn&#x27;t cheap.<p>It seems like on-demand AI video is coming, and I thought this was an interesting demo of how close it might be in at least one narrow video domain.
