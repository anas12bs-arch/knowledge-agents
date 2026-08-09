---
title: "Show HN: Lumabri – What if LLMs worked like Napster?"
url: "https://github.com/JustVugg/lumabri"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-09T23:05:04Z"
metadata:
  score: "6"
---

# Show HN: Lumabri – What if LLMs worked like Napster?

> Source: hackernews | Category: news | 2026-08-09T23:05:04Z

Score: 6 | Comments: 1

A while ago I started working on Colibrì to see if it was possible to run huge LLMs on a normal computer. The project grew far beyond what I expected, thanks in large part to the HackerNews community.<p>That led me to a new question:<p>What if we stopped thinking about one computer?<p>This is the idea behind Lumabri.<p>Instead of requiring a single machine to store and run an entire huge model, Lumabri treats a network of normal computers as a shared pool of resources.<p>One machine might provide disk space, another compute, another a different part of the model. If a required block or expert isn’t available locally, the system can retrieve or execute it on a peer.<p>This is particularly interesting for Mixture-of-Experts models. A model can have hundreds of billions of parameters, while only a fraction are activated for each token. Rather than moving huge expert weights over the network, Lumabri can send the small activation to a peer that already has the expert and let it execute it.<p>The goal is for machines to contribute whatever resources they can afford while using the swarm for the rest.<p>The idea is very much inspired by peer-to-peer systems: users are the infrastructure.<p>There are obviously major challenges, especially network latency and security. I’m experimenting with peer verification, SHA-256 verification, signed model state, replica selection, failover, and deterministic execution.<p>Lumabri is still an early experiment. I don’t have a datacenter or a huge GPU cluster, so I’m building it with the hardware I have and trying to find out whether the idea actually makes sense.<p>With Colibrì I asked:<p>Can one normal computer run a huge LLM?<p>With Lumabri I’m asking:<p>What if many normal computers could become one huge computer?<p>Feedback welcome.<p>Repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;JustVugg&#x2F;lumabri" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;JustVugg&#x2F;lumabri</a>
