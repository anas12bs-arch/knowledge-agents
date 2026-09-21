---
title: "Show HN: Foremerge – Catch intent conflicts between parallel coding agents"
url: "https://github.com/naw103/foremerge"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-21T22:14:09Z"
metadata:
  score: "30"
---

# Show HN: Foremerge – Catch intent conflicts between parallel coding agents

> Source: hackernews | Category: news | 2026-09-21T22:14:09Z

Score: 30 | Comments: 0

At, GPTree, we run several coding agents across our team on one repo using parallel worktrees. Apart from wasted time reviewing and fixing conflicts at PR time, the failures that hurt the most are when multiple plans or tickets cause architecture changes that cannot both be true. Ex. one agent replaces a class while another one is in the process of extending it. Git only notices if the resulting patches happen to touch the same lines and the review only catches it if they are familiar with both tickets.<p>Foremerge is a local &quot;git like&quot; coordination layer that sits above git (ie. does not interact with or change the way git and worktrees function), Before editing each agent publishes an intent and the scopes it will change, with the operation it plans to complete on each one.<p><pre><code>    foremerge intent publish --agent &quot;$A&quot; \
        --summary &quot;Replace PaymentService with StripePaymentService&quot; \
        --scope symbol:PaymentService=replace
    foremerge intent publish --agent &quot;$B&quot; \
        --summary &quot;Add PayPal support to PaymentService&quot; \
        --scope symbol:PaymentService=extend
</code></pre>
The publish by the 2nd agent returns a HIGH destructive_vs_additive finding before writing any code. Agents keep their own worktrees and the shared state is one SQLite file in gits common direectory. No hooks, no merge drivers, nothing rewrites your history.<p>It ships as one Rust binary with a CLI and MCP server with 18 tools and `foremerge setup all` wires it into Claude Code, Codex and Cursor. Because the protocol has nothing provider specific, a Claude agent and a Codex agent coordinate through the same store. Before any work is accepted, Foremerge runs a named check that you configured against the exact git state of the change. An agent that says tests pass is recorded but it dosnt satisfy the acceptance gate without running the check itself.<p>Detection is deterministic, no judge model reading your code. HIGH conflicts are only asserted for declared operations, ie. matches inferred from prose cap out below high. Claims are advisory leases, not locks so two agents can still hold the same scope without deadlock. The open source version is single matching and so not a distributed consensus.<p>We have tested this up to 98 parallel agents all working on the same repo with zero conflicts (was supposed to be 100 but 2 agents failed to run due to resource limitations)<p>I replayed 76 intents on my own agents from a build last week in the order they happened. The sample had exactly 1 conflict (which was flagged) and the review found a blind spot where one agent claimed scope by class name and the other claimed it by an internal method. We are working on fixing that for the next release.<p>Setup is a 30s install by pasting the quickstart instructions from the readme.md into your agent or manually: 
`curl -fsSL <a href="https:&#x2F;&#x2F;foremerge.com&#x2F;install.sh" rel="nofollow">https:&#x2F;&#x2F;foremerge.com&#x2F;install.sh</a> | sh` or `cargo install
--locked foremerge`, then `foremerge init &amp;&amp; foremerge setup all` in a repo.
Apache-2.0.<p>The feedback I want most is which conflicts between your agents plans would you actually want flagged and which would you tollerate as noise?<p>Repo here: <a href="https:&#x2F;&#x2F;github.com&#x2F;naw103&#x2F;foremerge" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;naw103&#x2F;foremerge</a>
Website: <a href="https:&#x2F;&#x2F;foremerge.com" rel="nofollow">https:&#x2F;&#x2F;foremerge.com</a><p>More information on the problems this solves: <a href="https:&#x2F;&#x2F;foremerge.com&#x2F;blog&#x2F;" rel="nofollow">https:&#x2F;&#x2F;foremerge.com&#x2F;blog&#x2F;</a>
