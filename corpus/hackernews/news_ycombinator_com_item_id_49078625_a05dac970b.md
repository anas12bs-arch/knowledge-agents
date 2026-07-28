---
title: "Show HN: SeaTicket – AI agent that resolve GitHub and Discord issues"
url: "https://news.ycombinator.com/item?id=49078625"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-28T06:43:51Z"
metadata:
  score: "6"
---

# Show HN: SeaTicket – AI agent that resolve GitHub and Discord issues

> Source: hackernews | Category: news | 2026-07-28T06:43:51Z

Score: 6 | Comments: 2

<a href="https:&#x2F;&#x2F;seaticket.ai&#x2F;" rel="nofollow">https:&#x2F;&#x2F;seaticket.ai&#x2F;</a><p>After maintaining Seafile, open-source file-sync software, since 2012. Somewhere across those fourteen years, &quot;go check if someone already reported this&quot; turned into one of the most common lines in our team chat. Because the same bug tended to show up multiple times. Nothing connected Github and Discord Issues until my team happened to remember seeing &quot;that thing&quot; somewhere else.<p>SeaTicket is what we built to fix that for ourselves before opening it up. It connects GitHub Issues, and Discords with a handful of other sources like Notion, Confluence, Linear, Jira into one workspace. When something new comes in, the AI agent pulls together related issues, past resolutions, and anything relevant in your knowledge base, and proposes a next step. It doesn&#x27;t send, reply, or close anything by itself because it waits for the approval of its suggestion first. We didn&#x27;t want to ship something that talks to our own users unsupervised, so we&#x27;re not asking anyone else to either.<p>The genuinely hard part has been matching the same underlying issue across sources that describe it in almost no shared vocabulary like a two-line Discord comment and a ten-line Github Bug can be trace to the same bug and share zero keywords. Happy to go into how we approach that in the comments if HNPs want it; it&#x27;s the part I&#x27;d most enjoy having picked apart.<p>It&#x27;s built for teams whose issues don&#x27;t arrive through one queue like open-source maintainers especially, but also product and support teams managing multiple repos and Discord servers. It&#x27;s deliberately not trying to be Zendesk or Fin: those assume a support team working a shared ticket queue, and we assume your team already lives in GitHub and wants issues handled there, not in a separate tool. Pricing has no per-seat cost on any plan, including a free one<p>i think bug reports scattered across repos and Discord must have a one place that they can be resolved, I&#x27;d like to know whether this is actually useful to you or whether we&#x27;re solving a problem you don&#x27;t have. Happy to answer anything about how it works under the hood.
