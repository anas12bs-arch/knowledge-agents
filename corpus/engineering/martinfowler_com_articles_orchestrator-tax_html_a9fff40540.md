---
title: "[martin-fowler] The Orchestrator's Tax"
url: "https://martinfowler.com/articles/orchestrator-tax.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-07-28T13:12:27Z"
metadata:
  {}
---

# [martin-fowler] The Orchestrator's Tax

> Source: engineering | Category: engineering | 2026-07-28T13:12:27Z

The Orchestrator's Tax

Subagents get justified by time saved and parallel execution, but
       Rahul Garg  explains that's not what matters most. Every
      token in the orchestrator's context is competing for its attention, and
      the real value of a subagent is what it keeps out of that context.
      Subagents should be treated as a tool for protecting the orchestrator's
      working memory, offloading reasoning it doesn't need to hold onto. Doing
      this well means giving the orchestrator explicit ground rules for when and
      how to delegate.  

  more…
