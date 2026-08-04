---
title: "[martin-fowler] Fragments: August  4"
url: "https://martinfowler.com/fragments/2026-08-04.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-08-04T13:27:12Z"
metadata:
  {}
---

# [martin-fowler] Fragments: August  4

> Source: engineering | Category: engineering | 2026-08-04T13:27:12Z

Fragments: August  4

There’s been a fair bit of publicity of the  Open AI “rogue agent” that hacked into Hugging Face . This prompted Anthropic to check what their models were up to and, to my complete lack of surprise,  discovered three incidents where models had gained unauthorized access  to data in other organizations.  Simon Wilison concluded : 

 
   It’s abundantly clear now that running evals of cyberattack potential in models is a spectacularly risky business. Every AI lab needs to pay attention to this. Keeping a close eye on what’s happening in those sandboxes is crucial 
 

 It strikes me that this is akin to a virus escaping from a laboratory. It makes clear that the model builders are not putting sufficient controls in place to prevent these lab escapes. They are morally responsible for any consequences of this, and that should extend to legal liability too. The bigger concern however is that this same kind of thing can happen with any organization running open-weight models. Lots of labs playing around with dangerous tools and little idea how to contain them. 

 We are sitting in state that Johann Rehberger describes as  the Normalization of Deviance in AI . No big disasters have occurred yet, despite all of these worrying signs. But when does our Challenger-moment appear? 

  ❄                ❄                ❄                ❄                ❄ 

 If the sense that we’re in the calm before a storm of rogue AIs worming their way into sensitive software systems isn’t enough, there’s also knowledge that AI is also a financial bubble. Big advances in technology, whether it be railways or the internet, come with bubbles, and those of us old enough to remember the dotcom bubble see all the signs of that now - only bigger. The problem is that bubbles may be obvious, but the way they grow and pop, particularly  when  they pop, isn’t as clear. The dotcom bubble was widely understood to be one, indeed the chairman of US Federal Reserve talked of  irrational exuberance . The troub
