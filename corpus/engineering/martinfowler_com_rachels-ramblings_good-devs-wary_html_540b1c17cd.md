---
title: "[martin-fowler] Why are good developers so wary of agentic development?"
url: "https://martinfowler.com/rachels-ramblings/good-devs-wary.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-10-29T15:34:48Z"
metadata:
  {}
---

# [martin-fowler] Why are good developers so wary of agentic development?

> Source: engineering | Category: engineering | 2026-10-29T15:34:48Z

Why are good developers so wary of agentic development?

TL;DR   Good developers’ caution about agentic development comes from knowing that built isn’t the same as working in production.  
   I’ve been surprised by how many excellent developers have been hesitant to go all in on coding agents. These are people who usually try new ways of working before anyone else and in many cases invent new tools and practices that support building the application well. So why have we had so much reluctance? 

 The easy (lazy?) answer is that they love writing code, or they’re worried about their jobs. I’m sure that’s true for some people, some of the time. And I know it is true for some of the developers I talk to but I always felt there was something else, another fear hiding behind those obvious ones. When we put together the  Technology Radar  every six months I try to block out a chunk of time for us to do an open space. In September, a discussion we had on agentic development, which pushed it to its limits, finally helped me see clearly what that fear is. 

 Building it right 

 Thoughtworkers care deeply about  building the right thing and building it right . It’s pretty much our default way of working and thinking and it’s where many of the practices and technologies we invented and championed came from. We want software that is useful and helpful, can be changed next year, and doesn’t fall over in production. Our developers adopted, championed or invented some of the first versions of continuous integration, pairing, automated testing, continuous delivery, microservices and many others early because they helped us build the software right. 

 Early coding agents made it very easy to produce code, including code we wouldn’t have wanted anywhere near production, written by people who have not learned about the chasm between building something and making it run in production safely. The tools have improved enormously, but experienced developers still have questions. Are we confident this is the right behaviour? Does it work as
