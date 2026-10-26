---
title: "[eff] Lessons Learned From 'AdFection' and What To Do Next"
url: "https://www.eff.org/deeplinks/2026/10/lessons-learned-adfection"
source: "legal"
category: "legal"
tags: ["legal", "privacy", "compliance", "gdpr", "regulation", "eff"]
date: "2026-10-26T18:54:20Z"
metadata:
  {}
---

# [eff] Lessons Learned From 'AdFection' and What To Do Next

> Source: legal | Category: legal | 2026-10-26T18:54:20Z

Lessons Learned From 'AdFection' and What To Do Next

Last week,    researchers at Citizen Lab revealed    a horrifying new malware campaign, dubbed “AdFection.” It used an ad network to distribute spyware to journalist’s devices to infect them without the target ever needing to click anything. This sort of attack on journalists is dangerous and incredibly concerning, especially since it’s built on the backbone of a technology we already object to:    behavioral advertising   . Although this type of attack has only been described targeting journalists, you can take a few steps we outline in the next section to mitigate the risk no matter who you are.  
  A few factors combined to make this attack a noteworthy first-of-its-kind. First, it utilized the surveillance ad-tech ecosystem to specially target the malicious code. Second, the spyware it delivered was so-called “zero-click,” meaning it required no interaction from the user to be infected: all that is required is for the ad to be delivered and code bundled along with it to be run, which happens automatically. Neither    malvertising    nor    zero-click attacks    are new on their own. What’s novel about the AdFection attack is combining them, creating a highly targeted, extremely dangerous attack which is difficult to defend against and even harder to detect.  
  Let’s take a deeper look from the perspective of one of the Windows devices supplied to the researchers from Al Jazeera. Here’s how the report describes the infection happening:   
 
  Someone browsing the web or using an app on that machine is served an ad created by Discover-Tech, a company exposed in the report as “purporting to be a legitimate advertising company, [but] appears to be a front for large-scale ad espionage abuse.”   
  The ad contains a small snippet of JavaScript code which is automatically executed when rendered in the app or website.   
  This code reaches back out to a Discover-Tech server, referred to as their “NOAS server,” with detailed information about the machine rendering
