---
title: "Show HN: Simulator for a custom 8-bit discreet logic computer"
url: "https://msap2.mehran.dk"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-17T16:46:12Z"
metadata:
  score: "5"
---

# Show HN: Simulator for a custom 8-bit discreet logic computer

> Source: hackernews | Category: news | 2026-07-17T16:46:12Z

Score: 5 | Comments: 0

5 years ago, I made a derivative of SAP-1 (mainly inspired by Ben Eater) on breadboard with few improvement and called it MSAP-1 (<a href="https:&#x2F;&#x2F;github.com&#x2F;mehrantsi&#x2F;MSAP-1" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;mehrantsi&#x2F;MSAP-1</a>) I made my own very primitive Assembly language and a simple Arduino programmer (<a href="https:&#x2F;&#x2F;github.com&#x2F;mehrantsi&#x2F;8-bit_CPU_Programmer" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;mehrantsi&#x2F;8-bit_CPU_Programmer</a>) where I could load my programs onto MSAP-1 and even Debug them (<a href="https:&#x2F;&#x2F;github.com&#x2F;mehrantsi&#x2F;8-bit_CPU_Debugger" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;mehrantsi&#x2F;8-bit_CPU_Debugger</a>).<p>After that I started worked on the second version of it (<a href="https:&#x2F;&#x2F;github.com&#x2F;mehrantsi&#x2F;MSAP-2" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;mehrantsi&#x2F;MSAP-2</a>) by adding Stack, Interrupts and etc. with the goal of having a very primitive OS running on the second version, but changes in life meant I didn&#x27;t have time to work on it as much, but I was progressing.<p>Since 2 years ago, I had this little test of mine to see which one can understand MSAP-1, My own Assembly, the programs I wrote and ultimately if they would understand MSAP-2. none of the models could really understand the whole stack and initial models were quite bad at understanding hardware and electronics in general. Until Fable 5...<p>Same prompt to Fable and it&#x27;s the first model that understood the full stack and my intentions for the second version that is in progress. I asked it to create a simulator which it did (not one shotted ofc) and I managed to finalize the design using that. Then together with Fable I created an OS using my own Assembly (<a href="https:&#x2F;&#x2F;github.com&#x2F;mehrantsi&#x2F;MOS-1" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;mehrantsi&#x2F;MOS-1</a>) and loaded it there and it all works!<p>It&#x27;s all quite fascinating how much better at electronics Fable is compared to the predecessors!<p>Simulator for MSAP-1: <a href="https:&#x2F;&#x2F;msap1.mehran.dk" rel="nofollow">https:&#x2F;&#x2F;msap1.mehran.dk</a><p>Simulator for MSAP-1: <a href="https:&#x2F;&#x2F;msap2.mehran.dk" rel="nofollow">https:&#x2F;&#x2F;msap2.mehran.dk</a>
