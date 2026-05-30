---
title: "[martin-fowler] Bliki: Vibe Coding"
url: "https://martinfowler.com/bliki/VibeCoding.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-05-30T15:08:37Z"
metadata:
  {}
---

# [martin-fowler] Bliki: Vibe Coding

> Source: engineering | Category: engineering | 2026-05-30T15:08:37Z

Bliki: Vibe Coding

Vibe coding is building a software application by prompting an LLM, telling it
  what to build, trying it out, prompting for changes - but without looking at
  any of the code that the LLM generates. This technique can be used by people
  without any knowledge of programming. However the resulting software often
  shows problems with maintainability, correctness, and security - so is best
  used for disposable software written for a limited audience. 

 The term was coined in February 2025 by Andrej Karpathy, an experienced
  programmer, in a post on X: 

 
 There's a new kind of coding I call “vibe coding”, where you fully give
    in to the vibes, embrace exponentials, and forget that the code even exists.
    It's possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting
    too good. Also I just talk to Composer with SuperWhisper so I barely even
    touch the keyboard. I ask for the dumbest things like “decrease the padding
    on the sidebar by half” because I'm too lazy to find it. I “Accept All”
    always, I don't read the diffs anymore. When I get error messages I just
    copy paste them in with no comment, usually that fixes it. The code grows
    beyond my usual comprehension, I'd have to really read through it for a
    while. Sometimes the LLMs can't fix a bug so I just work around it or ask
    for random changes until it goes away. It's not too bad for throwaway
    weekend projects, but still quite amusing. I'm building a project or webapp,
    but it's not really coding - I just see stuff, say stuff, run stuff, and
    copy paste stuff, and it mostly works. 

 --  Andrej Karpathy  
 

 The key point about vibe coding is  “forget that the code even exists” .
  This is what gives it much of its usefulness, but also its limitations. 

 Since the  November Inflection  many programmers are
  getting LLMs to write all their code, commenting that they may never write a
  line of code directly again. However they do care about this code, rev
