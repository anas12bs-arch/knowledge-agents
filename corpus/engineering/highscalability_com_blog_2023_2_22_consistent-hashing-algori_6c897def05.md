---
title: "[high-scalability] Consistent hashing algorithm"
url: "http://highscalability.com/blog/2023/2/22/consistent-hashing-algorithm.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "high-scalability"]
date: "2026-05-30T15:08:40Z"
metadata:
  {}
---

# [high-scalability] Consistent hashing algorithm

> Source: engineering | Category: engineering | 2026-05-30T15:08:40Z

Consistent hashing algorithm

&nbsp; 
 This is a guest article by  NK . You can view the original article  Consistent hashing explained  on  systemdesign.one  website. 
 How does consistent hashing&nbsp;work? 
 At a high level, consistent hashing performs the following operations: 
 
 The output of the hash function is placed on a virtual ring structure (known as the hash ring) 
 The hashed IP addresses of the nodes are used to assign a position for the nodes on the hash ring 
 The key of a data object is hashed using the same hash function to find the position of the key on the hash ring 
 The hash ring is traversed in the clockwise direction starting from the position of the key until a node is found 
 The data object is stored or retrieved from the node that was found 
 
 &nbsp; 
 Terminology
