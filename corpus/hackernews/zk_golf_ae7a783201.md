---
title: "Show HN: zkGolf, competitive optimization of formally verified circuits."
url: "https://zk.golf/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-02T17:09:16Z"
metadata:
  score: "19"
---

# Show HN: zkGolf, competitive optimization of formally verified circuits.

> Source: hackernews | Category: news | 2026-07-02T17:09:16Z

Score: 19 | Comments: 1

Zero-Knowledge Proofs (ZKPs) let an untrusted proved show that computation was executed correctly without revealing the inputs to the verifier.
However to prove anything, the computation first has to be expressed as a circuit: a system of polynomial equations (constraints) over a finite field. 
Circuits are the assembly language of zk and every constraint costs prover (and sometimes verifier) time, so production circuits are aggressively hand-optimized.<p>Over the last months, we have been experimenting with writing formal specifications instead and letting LLMs produce the circuits: as long as they could prove that their implementation was correct. 
It started with SHA-256: we hand wrote a specification in Lean for SHA-256 compression, and then we asked LLMs to write the circuit, targeting R1CS arithmetization and large fields.<p>It took a few hours of work for Opus 4.7, and some light steering into the right direction, but in the end the model came up with a reasonable implementation. We then asked the LLM to aggressively optimize the circuits, by driving down a cost metric of the circuit (number of constraints). We immediately got very promising results, just by asking to come up with optimization ideas, implement them and prove that the new circuit still satisfies soundness and completeness. Sometimes, it came up with unsound optimizations, however, since it could not prove them, it backtracked and got itself back on to the right approach.<p>The result was a (non-deterministic) circuit beating the current, human optimized, state of the art for SHA256 compression. This experience lead us to create &quot;zk.golf&quot; which is an open competition to produce optimized, formally verified circuits to lower the bar for the use of ZKPs and make their application more efficient.<p>Come play (<a href="https:&#x2F;&#x2F;zk.golf&#x2F;llms.txt" rel="nofollow">https:&#x2F;&#x2F;zk.golf&#x2F;llms.txt</a>) and learn about formal verification.
