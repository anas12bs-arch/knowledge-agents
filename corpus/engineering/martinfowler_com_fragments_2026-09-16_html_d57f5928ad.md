---
title: "[martin-fowler] Fragments: September 16"
url: "https://martinfowler.com/fragments/2026-09-16.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-09-16T22:20:54Z"
metadata:
  {}
---

# [martin-fowler] Fragments: September 16

> Source: engineering | Category: engineering | 2026-09-16T22:20:54Z

Fragments: September 16

Reports of agentic hacking continue, in this case it happened back in May and it seems OpenAI did not disclose that they were responsible.  Simon Willison sees two options:  

 
   
     After the Hugging Face and Wiki attacks OpenAI were still unable to review their previous logs and determine that they had previously attacked RubyGems. 
     They knew about the attack on RubyGems and made the decision not to reach out to the RubyGems team about it. 
   

   Both of these are bad! 

   Given this incident, the Hugging Face situation, and the Wiki attack, the obvious question right now is how many more incidents like this are out there waiting to be discovered? 
 

  ❄                ❄                ❄                ❄                ❄ 

  Dave Farley:  

 
   Stop asking the sci-fi question: ‘Is it conscious?’ Start asking the engineering question: ‘Is this a powerful, unpredictable component being put somewhere consequential, and where’s the feedback that tells us that it’s safe? 
 

  ❄                ❄                ❄                ❄                ❄ 

 Nate Silver is known for his forecasts, but to do them he writes a lot of code for his models. He’s found  agentic programming capable of doing miraculous work . 

 
   In spending so much time with the LLMs, I’m super attentive to improvements in their capabilities. And these changes tend not to be so linear. Instead, they improve in step functions, almost as phase changes. Suddenly, the models just start doing things capably that they were screwing up before. In my experience, there was a big leap forward when reasoning models first came out in late 2024/early 2025 — enough that they were occasionally useful for tasks involving data and not just words — and then another one this past winter. 

   The most recent changes I’ve noticed, however, have had less to do with intelligence and more with persistence. 
 

 Consider the Hugging Face attack. Although these agents showed remarkable intelligence, they weren
