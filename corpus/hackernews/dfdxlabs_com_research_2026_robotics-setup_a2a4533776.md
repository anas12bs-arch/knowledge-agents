---
title: "Building a robotics research setup that lives next to my desk"
url: "https://dfdxlabs.com/research/2026/robotics-setup/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-19T11:55:41Z"
metadata:
  score: "87"
---

# Building a robotics research setup that lives next to my desk

> Source: hackernews | Category: news | 2026-06-19T11:55:41Z

Score: 87 | Comments: 28

Quick framing, since the post is long: I did robotic manipulation research at OpenAI from 2017–2020, and the tabletop setup back then cost roughly 10x this one and took a team to run. This project is me testing whether a single person can now do meaningful work on the same class of problems: starting with physical and software setup.<p>A few decisions I&#x27;m least settled on, and would love some pushback&#x2F;feedback on:<p>- single arm vs. bimanual (I went single for cost&#x2F;space, knowing it rules out things like folding cloth)<p>- not calibrating camera extrinsics&#x2F;intrinsics for now<p>- RGB vs. RGB-D for from-scratch policies (ACT &#x2F; Diffusion Policy)<p>And one I&#x27;m more confident about but expect disagreement on: not building on ROS 2 &#x2F; LeRobot, and writing my own stack instead. Happy to get into the reasoning.
