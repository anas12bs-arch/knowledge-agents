---
title: "[martin-fowler] Fragments: July 13"
url: "https://martinfowler.com/fragments/2026-07-13.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-07-13T17:44:05Z"
metadata:
  {}
---

# [martin-fowler] Fragments: July 13

> Source: engineering | Category: engineering | 2026-07-13T17:44:05Z

Fragments: July 13

Some more of my notes from  Thoughtworks Future of Software Development Retreat . 

 When we had our first retreat in Utah early this year, nobody had heard of  Harness Engineering . This time we had a whole session on it. 

 When comes to the guide side of harnesses, most of the discussion is about context management. While context windows have increased is size as models get more sophisticated, that doesn’t mean that models will properly focus on the right bits. Models typically only focus attention on part of the context, and to get the best behavior, we need to manage that focus. One attendee keeps their context small, limiting the  agents.md  file to less than 200 lines 

 On the sensor side, we see more attention on computational sensors. Two patterns from one participant was shifting to languages with greater controls, (eg Rust rather than Python) and “leveling up” validation approaches, using more property-based testing and techniques from formal methods. One commented that while they aren’t smart enough to write specifications in a formal specification language, they are smart enough to read it and check it makes sense for their domain. 

 Will our attention on harnesses last long enough for our next retreat? Will the models just get so good that harnesses become unnecessary? Those with some  mechanical sympathy  for LLMs seem to think not - but are they overly coupled to the current state of technology? I find such speculation tends not to lead anywhere useful, I’ve not seen much success in guessing the future in the past, and with technology as radical as this, I don’t see it being any easier. So for the moment, attention to harnesses pays off. We find it reduces token usage, and also allows weaker models to be useful, supporting such things as local hosting of open-weight models. 

  ❄                ❄ 

 Which naturally segues me to a session on self-hosted models. Increasing token costs have made hosting an open-weight model more attractive, particula
