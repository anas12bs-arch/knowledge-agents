---
title: "A restored PDP-11/83 serving this page on 211BSD Unix"
url: "http://pdp1173.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-21T18:41:31Z"
metadata:
  score: "48"
---

# A restored PDP-11/83 serving this page on 211BSD Unix

> Source: hackernews | Category: news | 2026-09-21T18:41:31Z

Score: 48 | Comments: 16

The box is a restored Q-bus PDP-11&#x2F;83 named minerva: Mentec M11 CPU, two chassis tied with M9404&#x2F;M9405, RQDX3, 2xEmulex UC07, KDA50, RLV12, DEQNA, M3104. Storage is RA82 + dual RA92, MFM boot&#x2F;swap, dual RL02, RX50s, and a TKZ50. OS is 2.11BSD.<p>The live panel is top. &#x2F;cgi-bin&#x2F;webtop is the raw snapshot.<p>A 16-bit httpd will not survive the front page, so Varnish&#x2F;Caddy&#x2F;Cloudflare cache the HTML and a 5-second webtop sample. Origin is still the 11 itself, and it handles all of the webtop and visitor count requests.<p>Telnet exists (pdp1173.com, guest) but it is a 40-year-old UNIX with no modern security story. Please do not treat it as a challenge box; I can restore from tape, but that ruins it for everyone else.<p>Happy to answer Mentec, MSCP, Q-bus, or 2.11BSD questions.<p>To get BSD running on the Mentec, I had to customize the BSD kernel to use FPSIM, as the Mentec supports IEEE floating-point and NOT the DEC formats.
