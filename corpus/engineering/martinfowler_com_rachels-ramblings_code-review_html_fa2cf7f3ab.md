---
title: "[martin-fowler] Maybe We Shouldn't Be Reviewing All This Code"
url: "https://martinfowler.com/rachels-ramblings/code-review.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-09-02T13:57:21Z"
metadata:
  {}
---

# [martin-fowler] Maybe We Shouldn't Be Reviewing All This Code

> Source: engineering | Category: engineering | 2026-09-02T13:57:21Z

Maybe We Shouldn't Be Reviewing All This Code

TL;DR   Or, perhaps the problem isn't that AI has broken code review, maybe it’s that we've been using code review to solve the wrong problems  
   I was on a panel recently with Brian Houck from DX at Code Remix, hosted by Moderne. It was one of the more interesting panels I’ve done, largely because we disagreed. As my colleague Martin Fowler says, panels are much more interesting when people disagree and both sides have a good argument. Brian and I definitely did. 

 Brian has since written a thoughtful piece called   What are code reviews even for?   He is clearly passionate about his position, and I am passionate enough about mine that I’m writing this response. To be clear, I think we mostly want the same things. I just don’t think code review is the best way to get them. Brian is lovely, by the way, and encouraged me to write this. But I’d be lying if I said I didn’t want you to think I’m right by the end :) 

 So what were we disagreeing about? 

 AI is producing more code than humans can realistically review. Brian cites some pretty striking numbers: at Meta, significant lines of code per human-landed diff reportedly increased 106% in a year, while DX’s own data shows median pull request size increasing 64%. 

 His concern, which I share, is that simply automating code review away risks losing all the other things we use it for. Code review isn’t just about finding bugs. It’s how teams share knowledge, teach junior engineers, build collective ownership and spread architectural understanding. 

 My question is:  why are we waiting until code review to do all of those things?  

 I’ve never particularly liked pull requests as the centre of the software development process. Not because engineers shouldn’t look at each other’s code, but because I’ve always struggled with the idea that we should build something, finish it, package it up, throw it over to somebody else and  then  have the important conversation about whether we built the right thing in the righ
