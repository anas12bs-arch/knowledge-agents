---
title: "Show HN: SlideOps – slides from a repo that flag when they drift from the code"
url: "https://github.com/glukicov/slideops"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-31T22:48:26Z"
metadata:
  score: "18"
---

# Show HN: SlideOps – slides from a repo that flag when they drift from the code

> Source: hackernews | Category: news | 2026-08-31T22:48:26Z

Score: 18 | Comments: 5

I kept generating slide decks about my codebases with an agent, and weeks later they would go stale. Updating them was quite costly (time &amp; tokens), as the agent would have to re-scan the whole repo to re-generate the slides. So I made the slide deck carry its own provenance: SlideOps skill turns a repo into a slide deck, with all references to files carrying exact line range and a hash.<p>Checking is done with standard-library Python: no model calls, no network, and very fast. For example, it distinguishes MOVED (the code shifted) from CHANGED (the content differs). Updating the slides costs tokens, but now the checking part has already given the agent just the relevant context on what exactly needs to be repaired.<p>SlideOps ships as a Claude Code plugin and runs as a plain agent skill in Codex, Copilot CLI and OpenCode.<p>Longer write-up: <a href="https:&#x2F;&#x2F;medium.com&#x2F;@lukicov&#x2F;your-documentation-is-a-build-artifact-start-treating-it-like-one-ab48df61b1e0" rel="nofollow">https:&#x2F;&#x2F;medium.com&#x2F;@lukicov&#x2F;your-documentation-is-a-build-ar...</a><p>GitHub repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;glukicov&#x2F;slideops" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;glukicov&#x2F;slideops</a>
