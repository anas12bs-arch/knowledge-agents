---
title: "[martin-fowler] Fragments: July 21"
url: "https://martinfowler.com/fragments/2026-07-21.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-07-21T14:20:21Z"
metadata:
  {}
---

# [martin-fowler] Fragments: July 21

> Source: engineering | Category: engineering | 2026-07-21T14:20:21Z

Fragments: July 21

With this post, I’ll wrap up my notes from  the second  Future of Software Development Retreat . But before I do, I should note that the  full Thoughtworks report on the retreat is now available . They have five headline findings: 

 
   
     Code generation is no longer the bottleneck — verification is. 
     ‘Harness engineering’ is emerging as a distinct, ownable discipline. 
     Organizations are colliding with a real apprenticeship crisis. 
     The executive/engineer expectation gap is a bigger risk than any technical
limitation. 
     Legacy modernization is the clearest, most defensible near-term value pool. 
   
 

  ❄                ❄ 

 A session convened around the mismatch of views about using LLMs between engineers using it and the C-suite and boards that were calling for it. The concern is that boards are looking at promised productivity gains, and not concerned enough about the risks, particularly about security. 

 This was illustrated by one tale of a company that used ML-trained software to optimize the replacement of air filters on their field equipment. They were pleased to see that they were able to change the air filters less frequently, saving them $50 million. But the problem was the ML models were trained on equipment used in the desert, while their equipment was used in the arctic. Air filters in the desert deal with dust, but in the arctic the thing to remove is mosquitoes. There’s an important difference here, mosquitoes rot, and enough decaying mosquitoes is a serious fire risk. Fires from such dead mosquitoes around infrequently replaced air filters cost the company $100  billion . 

 Now such a tale could told of many situations without AI in the mix. Plenty of human situations have gone wrong when solutions are applied in a new context (which is why context is such a key word among pattern-writers). But the tale does remind us to be wary of an AI’s suggestions, and to always think of how to build sensors to provide rapid feedback.
