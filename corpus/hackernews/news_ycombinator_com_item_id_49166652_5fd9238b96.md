---
title: "Ask HN: Has anyone solved P2P routing at 100B+ nodes without DHT degradation?"
url: "https://news.ycombinator.com/item?id=49166652"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-04T11:50:04Z"
metadata:
  score: "4"
---

# Ask HN: Has anyone solved P2P routing at 100B+ nodes without DHT degradation?

> Source: hackernews | Category: news | 2026-08-04T11:50:04Z

Score: 4 | Comments: 0

The two of us (PhD in Physics and Mathematics and Philosophical Anthropology) have spent many years working on a mathematically protected secret voting system suitable for making socially significant decisions. During the design process, we realized that such a system must be a peer-to-peer network satisfying six absolute requirements. 
We have not been able to find a single existing protocol or academic paper that simultaneously satisfies more than two of them:
First: anonymous user authentication that guarantees the uniqueness of the user&#x27;s representation in the network (preventing one person from creating multiple accounts) without storing their personal data and without using any external resources, such as certificate authorities or a trusted third party.
Second: a network providing such anonymous authentication must be capable of covering all inhabitants of the Earth. Currently that is just over 8 billion people, but this number grows by more than 100 million every year. Moreover, the deceased must not be excluded from the system, which means monotonic growth is endless.
Third: a network that guarantees anonymity must not have any distinguished nodes—that is, it must be strictly peer-to-peer, consisting of nodes formed by users&#x27; devices. However, each user may have not one but several devices, and devices can fail, get lost, become obsolete, or even simply go out of fashion. This immediately changes the scale of the network—it must handle hundreds of billions of nodes.
Fourth: it is necessary to provide each user with access to their account from any device without using passwords, tokens, seed phrases, or anything similar.
Fifth: the key requirement becomes performing a search that enables user recognition in less than 1 second (so that it is imperceptible to the user). That is, any device must locate any other device or data in less than 1 second, while the amount of routing information stored by a single device must be negligibly small, preferably under 100 KB.
Sixth: to guarantee data preservation on unreliable user devices, first, the replication factor must be ~100 or even ~1000x, and second, there must be verification and recovery of routing and data based on consensus without a central arbiter or trusted nodes. At the same time, background synchronization traffic must remain below a few hundred bytes&#x2F;sec per device to avoid overwhelming mobile data plans.
Our question to HN:
Is the community aware of any existing P2P protocol, DHT, or academic proposal that even attempts to simultaneously satisfy these constraints? We have studied Kademlia, Chord, BATMAN, GNUnet, I2P, etc., and all of them seem to fail at scalability or traffic efficiency. Are we missing something fundamental, or is this truly a blind spot?
(This question is motivated by the fact that we have developed a candidate architecture that, in our opinion, solves all six problems. A brief description can be found on our GitHub [https:&#x2F;&#x2F;github.com&#x2F;ikhrabry-spec&#x2F;A-P2P-Network-Architecture-for-100B-Nodes]. Patent applications have been filed, and one patent has been granted. However, we doubt the novelty of our solutions and the absence of analogues—please point us to anything we may have missed.)
