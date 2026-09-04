---
title: "[schneier] Security Vulnerability in a Voting System"
url: "https://www.schneier.com/blog/archives/2026/09/security-vulnerability-in-a-voting-system.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-09-04T14:27:09Z"
metadata:
  {}
---

# [schneier] Security Vulnerability in a Voting System

> Source: security | Category: security | 2026-09-04T14:27:09Z

Security Vulnerability in a Voting System

It&#8217;s a vulnerability that allows someone to recover the order of ballots cast,  newly exploited  with AI tools. 
  Nearly four years since the original vulnerability was disclosed, I was still able to use it to analyze voter behavior in Georgia (one of the 21 states that uses affected scanners) in the recent May 2026 primary. 
  Notably, I never touched a voting machine, exploited a network, examined source code, or accessed anything non-public.  
 After pointing a coding agent to the original vulnerability paper, I supplied it with two data sources highlighted in the paper: the early-voting list for each county, and the  &#8220;CVR&#8221; (cast-vote record) file, containing every ballot and its selections (but not the voters&#8217; names or other identifying information). The CVR file is available upon request, precisely because a public, ballot-level record is what makes election results independently verifiable...
