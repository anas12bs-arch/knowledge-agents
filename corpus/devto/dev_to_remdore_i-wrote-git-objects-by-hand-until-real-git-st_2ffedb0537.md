---
title: "I wrote Git objects by hand until real Git stopped complaining"
url: "https://dev.to/remdore/i-wrote-git-objects-by-hand-until-real-git-stopped-complaining-6i1"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-09-25T19:20:08Z"
metadata:
  tag: "programming"
---

# I wrote Git objects by hand until real Git stopped complaining

> Source: devto | Category: news | 2026-09-25T19:20:08Z

No library, just hashlib and zlib writing into .git/objects. Blobs matched on the first try, trees failed on a sorting rule about slashes, and the index turned out to be the third of Git's structures that nobody draws. Then I packed 50 revisions and found 49 of them stored as 48-byte deltas.

Reactions: 6
