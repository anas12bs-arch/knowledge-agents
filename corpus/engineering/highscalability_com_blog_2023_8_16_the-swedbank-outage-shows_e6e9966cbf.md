---
title: "[high-scalability] The Swedbank Outage shows that Change Controls don't work"
url: "http://highscalability.com/blog/2023/8/16/the-swedbank-outage-shows-that-change-controls-dont-work.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "high-scalability"]
date: "2026-05-30T15:08:40Z"
metadata:
  {}
---

# [high-scalability] The Swedbank Outage shows that Change Controls don't work

> Source: engineering | Category: engineering | 2026-05-30T15:08:40Z

The Swedbank Outage shows that Change Controls don't work

This week I&rsquo;ve been reading through the recent&nbsp; judgment from the Swedish FSA &nbsp;on the Swedbank outage. If you&rsquo;re unfamiliar with this story, Swedbank had a major outage in April 2022 that was caused by an unapproved change to their IT systems. It temporarily left nearly a million customers with incorrect balances, many of whom were unable to meet payments.&nbsp; 
 After investigation, the regulator found that Swedbank had not followed their change management process and issued a SEK850M (~85M USD) fine. That&rsquo;s a lot of money to you and me, but probably didn&rsquo;t impact their bottom line very much. Either way I&rsquo;m sure the whole episode will have been a big wake up call for the people at the bank whose job it is to ensure adequate risk and change controls. So, what went wrong and how could it have been avoided?&nbsp; 
 How did the Swedbank incident happen? 
 The judgment doesn&rsquo;t describe the technical details behind the incident, but it does provide glimpses into how they assessed what went wrong: 
 
 &ldquo;The deficiencies that were present in Swedbank&rsquo;s internal control made it possible to make changes to one of the bank&rsquo;s most central IT systems without following the process in place at the bank to ensure continuity and reliable operations. This violation is therefore neither minor nor excusable.&rdquo; 
 &ldquo;none of the bank&rsquo;s control mechanisms were able to capture the deviation and ensure that the process was followed&rdquo; 
 &ldquo;one of the main causes underlying the IT incident was non-compliance with the change management process and that it is probable that this also resulted in a slower analysis of the incident and a greater impact on the operations.&rdquo; 
 &ldquo;good internal control is a prerequisite for a bank to be able to fulfill the requirements on risk management&rdquo; 
 
 Even if you think $85M isn&rsquo;t much of a fine - simply the cost of doing business - the full range of o
