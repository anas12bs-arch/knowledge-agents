---
title: "Show HN: Cynative – Read-only CLI in Go that explains your live infrastructure"
url: "https://github.com/cynative/cynative"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-28T18:19:23Z"
metadata:
  score: "6"
---

# Show HN: Cynative – Read-only CLI in Go that explains your live infrastructure

> Source: hackernews | Category: news | 2026-07-28T18:19:23Z

Score: 6 | Comments: 2

Hey, we built an open-source CLI in Go purposed to help you answer security questions across your cloud, code and runtime. It connects to your GitHub, GitLab, AWS, GCP, Azure &amp; K8s using the credentials that are already in your shell, while limiting itself to read-only.<p>The core innovation here is the trust boundary - our agent has a built-in code execution sandbox with no host or network access; it is exposed to an internal tool which we call an “action gate” that performs read-only HTTP requests to your own infrastructure. Since the cloud providers constantly expand actions and services, the read-only allowed set comes from the providers themselves, refreshed every 24 hours (and is configurable).<p>Some additional neat features: verifiers that recheck every finding, fail-closed audit log, host-pinning to your own infra, STS rescoping to SecurityAudit in AWS AssumeRole, secret redaction so the LLM never sees them, and much more.<p>Even though the frontier models are becoming quite capable at answering broad security questions like “review my code” or “audit my cloud security posture”, we’d recommend starting with something more specific, like “what in my cloud is publicly exposed and shouldn’t be?” or “can my CI escalate to cloud admin?”.<p>Repo and documentation available here: <a href="https:&#x2F;&#x2F;github.com&#x2F;cynative&#x2F;cynative" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;cynative&#x2F;cynative</a><p>Would love to hear any feedback &#x2F; feature requests.
