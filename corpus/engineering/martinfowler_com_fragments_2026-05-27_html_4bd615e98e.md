---
title: "[martin-fowler] Fragments: May 27"
url: "https://martinfowler.com/fragments/2026-05-27.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-05-30T15:08:37Z"
metadata:
  {}
---

# [martin-fowler] Fragments: May 27

> Source: engineering | Category: engineering | 2026-05-30T15:08:37Z

Fragments: May 27

At the GOTO Conference in Copenhagen in 2025,  Kent Beck and I spent some time on stage  talking and answering questions from the audience - a format I refer to as “two old geezers on a park bench”. We talk about our experiences with LLM-augmented programming (at that point - October 2025), we show our frustration that things we’ve been saying for thirty years  still need to be said, we say how anything like a manifesto reunion needs to be led by a younger generation, and opine on what junior developers should be focusing on in their career. 

     

  ❄                ❄                ❄                ❄                ❄ 

 Ian Johnson has written a series of posts about  restructuring a gnarly codebase  

 
   The story follows a real Laravel + React codebase over ~3 months and ~258 commits from a legacy monolith with no tests to a well-structured application with automated quality gates, a React SPA migration in progress, and an AI agent that reliably ships production code with minimal supervision. 
 

 The series covers the steps in decent detail, and his approach follows the kinds of steps I’d use. First get everything under the control of decent characterization tests, add static analysis, introduce the right patterns to make things flow easily. 

 With all of this, is his use of AI, which changed during the exercise: 

 
   For the first two months of this project, I used Claude Code with auto-approve turned off. Every file edit, every terminal command, every change… I reviewed it before it executed. […] The results were good. The code was clean. But I was doing most of the thinking and half the typing. The agent was a fancy autocomplete with better suggestions. I wasn’t getting the leverage I’d hoped for. 

   I read an article about “on-the-loop” versus “in-the-loop” human-AI collaboration. The framing clicked immediately […]  I was micromanaging because I didn’t trust the agent to do the right thing. And I didn’t trust the agent because there was nothing f
