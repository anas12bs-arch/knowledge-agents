---
title: "Tell HN: Lots of Ask HNs again"
url: "https://news.ycombinator.com/item?id=50649864"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-11-26T08:09:21Z"
metadata:
  score: "244"
---

# Tell HN: Lots of Ask HNs again

> Source: hackernews | Category: news | 2026-11-26T08:09:21Z

Score: 244 | Comments: 89

There have been questions about why the &#x2F;ask page (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;ask">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;ask</a>) was running dry of Ask HNs - e.g.:<p><i>Ask HN: Why is Ask HN only showing me 14 posts?</i> - <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=49984484">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=49984484</a> - Oct 2026 (47 comments)<p><i>Ask HN: Why is pagination gone on &quot;Ask HN&quot;, and showing only 19 items?</i> - <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=50280719">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=50280719</a> - Oct 2026 (3 comments)<p>I believe I found the problem. The pool of stories for <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;ask">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;ask</a> has traditionally been drawn from the ranked stories list from which we generate the frontpage. That list is restricted to the top 1500 ranked submissions, and it seems the % of submissions which are text posts (i.e. no linked URL) had declined enough to starve the Ask HN feed. The solution is to compute a separate list of ranked Ask HNs.<p>p.s. &quot;Ask HN&quot; is the conventional name but it means text posts. The title can also start with &quot;Tell HN&quot; or nothing in particular. They&#x27;re just posts which were submitted without a URL.
