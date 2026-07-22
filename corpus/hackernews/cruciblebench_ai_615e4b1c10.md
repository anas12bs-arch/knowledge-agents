---
title: "Can a MUD evaluate LLMs? A $99 proof of concept"
url: "https://cruciblebench.ai/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-22T17:06:58Z"
metadata:
  score: "10"
---

# Can a MUD evaluate LLMs? A $99 proof of concept

> Source: hackernews | Category: news | 2026-07-22T17:06:58Z

Score: 10 | Comments: 0

I&#x27;m the author of a paper my friends and I wrote after we were curious if a MUD, text games originating in the 1970s, could be used to evaluate LLMs. We&#x27;ve spent the last several months on nights and weekends running this experiment and writing the paper on just our personal computers with about $99 in API credits.<p>Our experiment did have an interesting leaderboard but even more surprising was the measurements of each LLM. We scored each on four behavioral dimensions, two of which lean heavily on an LLM classifier. When we removed those two, one of the frontier models fell six positions. When we then checked the classifier against a second judge, the per-model agreement between them ranged from 85% to 22%. The aggregate kappa (0.04 on probe detection) indicated the instrument was noisy without saying which models the noise was hitting. The most affected model shared a model family with the classifier. This isn&#x27;t proof of bias, just one observation we recorded.<p>We realize LLM judges can be unreliable, and while it wasn&#x27;t our original intent to test this, it ended up being the most interesting finding. The divergence between the two judges is the finding we think generalizes to other judge-based benchmarks.<p>We emphasize this is just a proof of concept and not a validated benchmark. We prepared a thorough limitations section in the paper, including just 50 runs per model, overlapping CIs among the top models, no human raters, a tiny environment, etc.<p>Everything we did is publicly available, the paper and data are CC BY 4.0, while the code is MIT. The paper, transcripts, code, and complete API billing export  can be found at <a href="https:&#x2F;&#x2F;doi.org&#x2F;10.5281&#x2F;zenodo.21386663" rel="nofollow">https:&#x2F;&#x2F;doi.org&#x2F;10.5281&#x2F;zenodo.21386663</a><p>If you find issues, please let us know, that&#x27;s why we&#x27;re sharing this. We&#x27;re currently designing Phase 2 and want it to be as robust as possible. We&#x27;re looking at human baselines, multiple judges, more objectives, a larger environment, etc.
