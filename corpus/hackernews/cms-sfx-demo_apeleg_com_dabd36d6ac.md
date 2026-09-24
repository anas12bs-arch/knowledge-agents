---
title: "Show HN: Air-gapped file encryption as self-decrypting HTML page"
url: "https://cms-sfx-demo.apeleg.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-24T19:12:44Z"
metadata:
  score: "16"
---

# Show HN: Air-gapped file encryption as self-decrypting HTML page

> Source: hackernews | Category: news | 2026-09-24T19:12:44Z

Score: 16 | Comments: 6

Air-gapped file encryption packed into a single, self-decrypting HTML page. Repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;ApelegHQ&#x2F;ts-cms-ep-sfx" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;ApelegHQ&#x2F;ts-cms-ep-sfx</a><p>I was inspired by self-extracting archives. I wanted to share files with basically no dependencies. The goal was:<p><pre><code>  1. Something that didn&#x27;t require any installation (assuming a web browser)
  2. Have a single file with no network that could self-decrypt
  3. Be fully auditable
</code></pre>
The second point is done by having (sort of(*)) reproducible builds and embedded OpenPGP signatures.<p>The first point is made by cleverly manipulating the HTML structure so that it can decrypt without breaking the PGP signature. It can even decrypt using bare openssl (which was a design goal too, though getting the exact structure right took some work and bug reports).<p>The third point is accomplished by the first two, and by the source being freely available.<p>(*) Depends on the OS at the moment.
