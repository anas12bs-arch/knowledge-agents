---
title: "Show HN: DocCharm – The help center that keeps itself up to date"
url: "https://doccharm.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-21T19:57:34Z"
metadata:
  score: "5"
---

# Show HN: DocCharm – The help center that keeps itself up to date

> Source: hackernews | Category: news | 2026-07-21T19:57:34Z

Score: 5 | Comments: 0

Hello HN!<p>We were finding it too much work to keep our Zendesk help center up to date as our product kept changing, so I built DocCharm — it keeps a help center up to date automatically by watching PRs as they land in your GitHub repository. It suggests updates (with AI) to existing articles, or drafts entirely new ones if nothing appropriate exists yet.<p>Everything goes into a review queue first, so a human always checks (and can optionally edit) before anything publishes. In practice this has proven to be a pretty slick workflow (in my opinion anyway, but not only!).<p>We’ve been using it at my main job for a while now and it’s a big time saver. It’s also gaining some traction with other companies in the same investor portfolio. My sales process so far has been high-touch outbound. This probably won’t scale in the long run, but I’m hoping to learn as much as I can by nurturing all of the initial relationships. If you run a business with a help center that’s drifting out of date, email me and I’ll comp your first couple of months. Email is in my HN profile.<p>Both Zendesk and Mintlify help centers can already be automatically imported into DocCharm. If you use a different help center, let me know and I’ll get it automatically imported one way or another. I&#x27;ve also implemented some support for theming, so you can keep your own branding.<p>The tech is essentially the same that I use for most of my work (and it&#x27;s not a differentiator, but we&#x27;re all tech-curious here):<p>- Haskell&#x2F;Yesod<p>- NixOS<p>- SQLite with Litestream (db per tenant; backed up on both Hetzner and Cloudflare; encrypted)<p>- Sentry for error reporting<p>- Stripe for billing<p>- Healthchecks.io as a dead man’s switch<p>- Prometheus and Grafana for telemetry<p>- Resend for transactional email<p>There&#x27;s plenty still to do on the roadmap, but this is already working nicely and providing value as is. I&#x27;m not building in the open, though what I prioritise will naturally be heavily guided by the needs of the earliest users.<p>WDYT?
