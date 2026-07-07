---
title: "Show HN: Halo – open-source, tamper-evident runtime evidence for AI agents"
url: "https://github.com/bkuan001/halo-record"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-07T20:13:45Z"
metadata:
  score: "7"
---

# Show HN: Halo – open-source, tamper-evident runtime evidence for AI agents

> Source: hackernews | Category: news | 2026-07-07T20:13:45Z

Score: 7 | Comments: 1

Hi HN, I&#x27;m Brian, I spent the last few years at Vanta (YC W18), helping startups and enterprises become compliant and I recently started exploring what that might look like in a post-agentic world.<p>The problem Halo solves is: when a company buys an AI agent from a vendor and gives it access to their data, they have no way to check what the agent did with that data. Vendors may have built observability dashboards and audit logs, but those are editable and partisan. SOC 2 and ISO 27001 audit a company&#x27;s controls, but controls are less predictive when the software is agentic. TLDR: give an agent the same prompt 50 times, and you get 50 slightly different actions&#x2F;answers - so the only thing worth auditing in a post-agentic world is what happened at runtime.<p>Halo is an open-source project that produces agent runtime evidence. It&#x27;s a small recorder that records every action an agent takes (eg. tool calls, model calls, data access, etc), and becomes a record in an append-only log. It&#x27;s hash-chained, so anyone can re-verify.<p>Run the following command to see a fictional example:<p><pre><code>     uvx --from halo-record halo demo --serve
</code></pre>
Then, delete a line from one of the .jsonl files and reload, and the report will catch that it&#x27;s been tampered with.<p>To wire up your own agent, run this line of Python:<p><pre><code>     agent = trace(run_my_agent, profile=&quot;my-agent&quot;, log=&quot;audit.jsonl&quot;)
</code></pre>
Then use this to generate a real report and give it to your customers:<p><pre><code>     halo report audit.jsonl -o report.html
</code></pre>
Disclaimer: this proves integrity, not completeness (as a self-held chain proves nothing was edited but does NOT prove that nothing was omitted). Catching this requires a witness outside the vendor and is what I&#x27;m working on next.<p>Halo is Apache-2.0, contains zero runtime dependencies, and is about 4,300 lines of Python with 125 tests (if you prefer TypeScript, here&#x27;s that repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;bkuan001&#x2F;halo-record-ts" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;bkuan001&#x2F;halo-record-ts</a>).<p>Give it a try, and please let me know if you have any feedback!
