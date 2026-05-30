---
title: "[martin-fowler] Fragments: May 14"
url: "https://martinfowler.com/fragments/2026-05-14.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-05-30T15:08:37Z"
metadata:
  {}
---

# [martin-fowler] Fragments: May 14

> Source: engineering | Category: engineering | 2026-05-30T15:08:37Z

Fragments: May 14

Last week I spent a day at The Orchard Retreat, hosted by  Mechanical Orchard . that brought together several people working in software development to talk about the profession’s future with the rise of agentic programming. The event was help under the  Chatham House Rule , so I can’t attribute the comments and stories I heard. (If anyone recognizes themselves, and would like attribution, let me know.) Here are a few tidbits that caught my notebook. 

  ❄                ❄ 

 One group developed a behavioral clone of GNU Cobol compiler in Rust. The result is 70K lines of Rust and was built in 3 days. This is yet another sign of the ability of LLMs to do a good job of porting existing code to a new platform. Good regression tests are extremely valuable here (and I don’t know how good GNU Cobol’s are). There’s also the possibility of building a test suite if you have access an existing implementation. 

  ❄                ❄ 

 Large spec documents can be complex for a human to review. One attendee shared the idea of getting the LLM to interview a human expert, asking the human questions to verify the correctness of the specification, a form of  Interrogatory LLM . 

  ❄                ❄ 

 Not specifically about AI - but I liked how one attendee commented that the first thing they do when consulting with an organization is to read the guidelines for their change-control board. This is the scar tissue of what’s gone wrong in the past. I’ve often said that to understand why a thing is the way it is, you need to understand the history of how it got there. This seems like an excellent way to tap into important parts of that history. 

  ❄                ❄ 

 My colleagues who work with modernizing legacy systems have long been rather sniffy about “Lift and Shift” - porting a legacy system to a new platform while retaining  Feature Parity . 

 
   We see this pattern as a huge missed opportunity. Often the old systems have bloated over time, with many features unused by u
