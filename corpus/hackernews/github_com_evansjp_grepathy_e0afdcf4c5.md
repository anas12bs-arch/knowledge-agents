---
title: "Show HN: Grepathy – Claude made a decision nobody approved"
url: "https://github.com/evansjp/grepathy"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-15T14:24:37Z"
metadata:
  score: "9"
---

# Show HN: Grepathy – Claude made a decision nobody approved

> Source: hackernews | Category: news | 2026-07-15T14:24:37Z

Score: 9 | Comments: 11

hey HN - Claude pre-created users in Clerk with null emails&#x2F;names as &quot;guest users&quot; on a contract job. Wasn&#x27;t in any plan. The CTO asked why, and I didn&#x27;t know! I didn&#x27;t make that decision!<p>The reasoning was in a transcript on my laptop. Claude Code deletes those after 30 days by default. Two of my projects lost their whole history that way.<p>Grepathy distills transcripts locally into markdown committed with the code. Decisions only, never your messages, no server.<p>List every decision nobody approved:<p><pre><code>  grep -rn &quot;agent-initiated&quot; .ai&#x2F;why&#x2F;
</code></pre>
Ran a blind eval before shipping, published it including the misses (REPORT.md). Agents with Grepathy answered the &quot;why&quot; questions right. Baseline agents made up confident wrong answers.
