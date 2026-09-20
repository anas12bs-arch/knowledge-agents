---
title: "Show HN: Sigabrt.dev – cronjob monitor with an SSH TUI"
url: "https://sigabrt.dev"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-20T13:45:31Z"
metadata:
  score: "12"
---

# Show HN: Sigabrt.dev – cronjob monitor with an SSH TUI

> Source: hackernews | Category: news | 2026-09-20T13:45:31Z

Score: 12 | Comments: 3

Hello HN. I built this mostly to monitor the things I host myself. I know it&#x27;s nothing too exciting.<p>Anyway, the TL;DR is: Create an endpoint, and if your script&#x2F;cronjob fails to regularly ping it, you get notified (by email or ntfy). E.g.:<p><pre><code>    0 * * * * .&#x2F;script.sh &amp;&amp; curl -fsS https:&#x2F;&#x2F;sigabrt.dev&#x2F;pulse&#x2F;&lt;id&gt;&#x2F;beat
</code></pre>
It also has an SSH TUI which is currently experimental and read-only, mostly because I&#x27;m not sure whether it is actually useful or just a gimmick :):<p><pre><code>    ssh sigabrt.dev
</code></pre>
To use it, simply add your SSH public key in your account settings.<p>Yes, there are services like this already, and this is minimalistic by comparison. Feedback is welcome.
