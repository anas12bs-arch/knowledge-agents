---
title: "Show HN: Omacosy – Omarchy-style tiling desktop for macOS, no SIP"
url: "https://github.com/paulsp94/omacosy"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-20T18:05:48Z"
metadata:
  score: "7"
---

# Show HN: Omacosy – Omarchy-style tiling desktop for macOS, no SIP

> Source: hackernews | Category: news | 2026-08-20T18:05:48Z

Score: 7 | Comments: 4

I have been using omarchy on my tower since nearly a year now, shortly after it was released first. I really love the experience I am having with it but I still use my macbook for daly work, so I wanted to recreate a similar experience on it. Thats why I created omacosy, a setup for tiling windows, custom menu bar, some themes from omarchy, focus follows mouse, focus rings around windwos, some mac flavors with trackpad events and a custom mission control overview for your workspaces.<p>I used AeroSpace over yabai for the tiling window manager because I didnt wanted to compromise on SIP which is a mac security feature.
It is supposed to be keyboard first like omarchy to move windows organize workspaces etc
The setup runs around 157mb of ram and consists of AeroSpace, Karabiner (for the super key), and five small self build swift binaries.<p>I am running it daily on my M1 max macbook, currently on macOS26. I havent tested it much on other macbooks or macOS versions.
The install script creates a manifest file to backup what was installed before and what it installed itself, the uninstall script takes that into account to clean up the macbook to exactly the state it was in before. 
It needs quite some permissions for it sfunctionality which I layed our in the project readme. I wanted to be really transparent about which permissions it uses and for what reason.<p>I would love to get some feedback or see people trying it out and hearing your opinion. Mostly about what still doesnt feel smooth in the experience or if you find any performance issues.
