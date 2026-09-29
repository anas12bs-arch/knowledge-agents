---
title: "[martin-fowler] Fragments: September 29"
url: "https://martinfowler.com/fragments/2026-09-29.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-09-29T15:44:35Z"
metadata:
  {}
---

# [martin-fowler] Fragments: September 29

> Source: engineering | Category: engineering | 2026-09-29T15:44:35Z

Fragments: September 29

Simon Willison:  

 
   The more time I spend working with coding agents, the more convinced I am that they make software engineering even harder 

   We can do amazing things with them, but unlocking their full potential requires extraordinary discipline and knowledge 
 

 This has been a constant impression I get from following Willison’s writing. While things like  vibe coding  get a lot of attention, the real strength of  agentic programming  relies on more sophisticated techniques - and these are not easy to learn or execute. It’s a reason I’m wary of extrapolating my own dabblings into firm opinions about how to use the genie. 

  ❄                ❄                ❄                ❄                ❄ 

 Harper Reed explored what turns agents into hackers by  creating a breakaway agent  

 
   It ran and ran attacking all the machines on the same subnet, and was very effective. It didn’t really get very far, but it exhausted a lot of options, and was pretty fun to watch. (Just a reminder that this was on my local network with local boxes - don’t do this on a hosted box. That would be very rude.) 
 

 The interesting observation from this was that a core enabler for this was “unlimited tokens”. He usually doesn’t see agents trying to do stuff like this because there’s a limit on how many turns they can take. For this experiment he gave them unlimited tokens by using an open weight model. 

 
   This type of experience must be part of a lot of these LLMs training. They are very effective at attacking these types of problems. They don’t give up once it appears impossible, they just keep trying to figure out how to solve it. 
 

 This echoes Nate Silver’s observation that the striking capability of these models is that they not that they are super-intelligent - but they are  super-persistent . Which is especially worrying when we are  wiring them into everything . 

  ❄                ❄                ❄                ❄                ❄ 

 Which all makes me think
