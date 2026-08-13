---
title: "Show HN: OJCP – an open protocol for agent-consumable job data"
url: "https://ojcp.dev/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-13T17:29:13Z"
metadata:
  score: "11"
---

# Show HN: OJCP – an open protocol for agent-consumable job data

> Source: hackernews | Category: news | 2026-08-13T17:29:13Z

Score: 11 | Comments: 1

Author here!<p>Agents are applying to jobs for people right now, with progressively more volume, and there&#x27;s nothing built for it. So they scrape career pages and fight ATS forms with Playwright&#x2F;Browser Use, which breaks constantly (or they get bot blocked). Employers get buried in applications that don&#x27;t fit, candidates hear nothing back, and the resume is now an AI-written thing that another AI scores (which breaks the existing model entirely, btw).<p>OJCP is MCP tools for search and apply, a manifest at &#x2F;.well-known&#x2F;ojcp.json so agents can find providers, and schemas that extend schema.org instead of replacing it. The playground on the site is a live MCP endpoint, so you can throw calls at it right now.<p>Why a spec at all when models keep getting better at figuring things out? Inference can&#x27;t produce authorization. An agent can work out what a form wants. It can&#x27;t establish that someone consented to this specific submission, and then employer has no way to verify who&#x27;s calling. So TL;DR a more capable agent is also a more capable impersonator.<p>In this model, trust runs both direction. Agents sign requests using the same method that CloudFlare and OpenAI are already using, providers sign their manifests, agents can check against a JWKS, and trust tiers cap how much candidate PII can go to a given provider. Validation happens at consent, so browsing costs nothing and you only pay the verify when the interaction occurs.<p>I&#x27;m the CTO of Recruitics (job advertising) and spent time at LinkedIn before that, so I&#x27;ve been at the intersection of hiring and job search for a while and have felt the pain of both sides.<p>Happy to answer any questions!
