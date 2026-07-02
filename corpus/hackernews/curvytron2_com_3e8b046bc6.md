---
title: "Show HN: Curvytron 2, I rewrote my browser party game, 10 years later"
url: "https://curvytron2.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-02T01:49:44Z"
metadata:
  score: "7"
---

# Show HN: Curvytron 2, I rewrote my browser party game, 10 years later

> Source: hackernews | Category: news | 2026-07-02T01:49:44Z

Score: 7 | Comments: 3

Hi everyone, french web dev here,<p>About 10 years ago I did a little party game in the browser inspired by Achtung die Kurve genre, it reached HN (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=9494619">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=9494619</a>) and everything went crazy, it&#x27;s still largely played in open-spaces all over the world today.<p>This past year, I&#x27;ve been working on a sequel: <a href="https:&#x2F;&#x2F;curvytron2.com" rel="nofollow">https:&#x2F;&#x2F;curvytron2.com</a> is live.<p>Same goal as the first one: challenge myself, perfect my skills, have fun and give back to the internet community the best way I know; by just putting a free little fun game out there. No ads, no tracking, no business plan.<p>A decade of professional web development and hours of GMTK have raised my expectations and this time I aimed for:<p>- a good looking top-down 3D view with improved gameplay and real game juice: I learn Three.JS and WebGL for this project, worked on the camera movements, screen shake, sound design, gameplay feedback and I&#x27;m proud of the portal-like effect of the bonus that allows you to peak and  cross over to the other side of the map.
- a solid 100fps server simulation (in Go) serving clients with a really bandwidth efficient netcode (it&#x27;s binary websocket instead of plain JSON and I open-sourced it: <a href="https:&#x2F;&#x2F;github.com&#x2F;Tom32i&#x2F;netcode" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;Tom32i&#x2F;netcode</a>).
- Instant reconnection, at any time: I had this requirement from day one, in the first curvytron losing connexion meant dropping out of the game permanently. Not anymore. You can just refresh the page mid-game and keep playing, try it yourself.<p>The game runs in any desktop and mobile browser and supports gamepads
I&#x27;ve put up servers in US and Europe to offer a good ping to as much players as I can afford at the moment.<p>I still maintain and host the first game to keep the original experience live.<p>I&#x27;d love to get feedback from HN, and don&#x27;t hesitate to stress-test the game of course!<p>I&#x27;ll be around to answer questions and discuss if you&#x27;re interested.
Cheers!
