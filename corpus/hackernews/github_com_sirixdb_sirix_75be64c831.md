---
title: "Show HN: SirixDB 1.0 Beta – Git-Like Versioning, Diffs, Time-Travel Queries"
url: "https://github.com/sirixdb/sirix"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-15T21:34:43Z"
metadata:
  score: "9"
---

# Show HN: SirixDB 1.0 Beta – Git-Like Versioning, Diffs, Time-Travel Queries

> Source: hackernews | Category: news | 2026-07-15T21:34:43Z

Score: 9 | Comments: 0

Hi HN! I&#x27;ve posted SirixDB here before, back in 2019 (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=19834681">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=19834681</a>) and again in 2023 (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=38252963">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=38252963</a>).<p>The core idea behind SirixDB is, that history is a first-class citizen. Every commit stores a lightweight, queryable revision. You can query any point in time, even individual nodes (for instance JSON values), diff arbitrary revisions, and efficiently track how data evolved without replaying events.<p>Unlike traditional event stores, historical states do not need to be reconstructed by replaying events nor do we have to think about projections. Revisions are directly queryable.<p>A simple example:<p>Jan 1: Record &quot;Price = $100, valid from Jan 1&quot;. Stored on Jan 1 (transaction time).<p>Jan 20: Discover price was actually $95 on Jan 1. Commit correction.<p>After correction, you can ask across both axes:<p>- &quot;What did we THINK the price was on Jan 16?&quot; -&gt; $100 (Transaction time)<p>- &quot;What WAS the price on Jan 1?&quot; -&gt; $95 (Valid time)<p>I&#x27;ve worked on this in my spare time since 2013, following its academic precursor (Idefix&#x2F;Treetank) at the University of Konstanz. The architecture relies on an append-only physical log and a persistent copy-on-write page trie.<p>A high level view of the architecture:<p>Physical Log (append-only, sequential writes)<p><pre><code>  ┌────────────────────────────────────────────────────────────────────────┐
  │ [R1:Root] [R1:P1] [R1:P2] [R2:Root] [R2:P1&#x27;] [R3:Root] [R3:P2&#x27;] ...    │
  └────────────────────────────────────────────────────────────────────────┘
       t=0      t=1     t=2      t=3      t=4       t=5       t=6    → time
</code></pre>
Each revision is indexed, and unchanged pages are shared:<p><pre><code>  [Rev 1]          [Rev 2]          [Rev 3]
     │                │                │
     ▼                ▼                ▼
  [Root₁]          [Root₂]          [Root₃]
   │   │            │   │            │   │
   │   └─────────┐  │   └────────┐   │   └─────────┐
   ▼             ▼  ▼            ▼   ▼             ▼
  ┌──────┐       ┌──────┐       ┌──────┐       ┌──────┐
  │  P1  │       │  P2  │       │ P1&#x27;  │       │ P2&#x27;  │
  └──────┘       └──────┘       └──────┘       └──────┘
   Rev 1         Rev 1+2        Rev 2+3         Rev 3
                 (shared)       (shared)
</code></pre>
Beneath the root pages sit node and secondary indexes, using a 
novel sliding-snapshot algorithm to balance read&#x2F;write performance.
Everything is queryable using JSONiq via the Brackit compiler.<p>Back in 2019, and even in 2023, SirixDB was very slow due to GC pressure. Unlike most other document stores, SirixDB stores fine-grained nodes, and I came to realize that an on-heap (JVM) representation made up of lots of small objects simply didn&#x27;t make sense. I measured it with async-profiler — with some help from Andrei Pangin himself — and the result was that the poor throughput was due to the sheer amount of allocations which scaled almost linearly with the number of open transactions.<p>Working a full-time software engineering job, I lacked the energy for a massive spare-time rewrite. About a year ago, I started experimenting with AI. It turned out to be ideal for automating the tedious, repetitive parts of migrating the storage layer to Java&#x27;s Foreign Function &amp; Memory API, storing pages completely off-heap.<p>Looking further ahead, the append-only, immutable-page design maps naturally onto object storage like S3 and distributed logs like Kafka for a cloud version, and initial prototypes already exist. Maybe that becomes a commercial service one day, but for now, I&#x27;m just thrilled to see these core design principles finally proven out.There&#x27;s an interactive demo, documentation, and the code is on GitHub. I&#x27;d love feedback and am happy to answer questions!<p>kind regards<p>Johannes<p>[1] <a href="https:&#x2F;&#x2F;sirix.io" rel="nofollow">https:&#x2F;&#x2F;sirix.io</a> | <a href="https:&#x2F;&#x2F;github.com&#x2F;sirixdb&#x2F;sirix" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;sirixdb&#x2F;sirix</a><p>[2] <a href="https:&#x2F;&#x2F;sirix.io&#x2F;docs&#x2F;architecture.html" rel="nofollow">https:&#x2F;&#x2F;sirix.io&#x2F;docs&#x2F;architecture.html</a><p>[3] <a href="https:&#x2F;&#x2F;demo.sirix.io" rel="nofollow">https:&#x2F;&#x2F;demo.sirix.io</a><p>[4] <a href="https:&#x2F;&#x2F;sirix.io&#x2F;docs&#x2F;" rel="nofollow">https:&#x2F;&#x2F;sirix.io&#x2F;docs&#x2F;</a><p>[5] <a href="http:&#x2F;&#x2F;brackit.io" rel="nofollow">http:&#x2F;&#x2F;brackit.io</a>
