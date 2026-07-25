---
title: "Ask HN: Which Jabber clients support SCRAM+ and XEP-0474"
url: "https://news.ycombinator.com/item?id=49049796"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-25T20:17:24Z"
metadata:
  score: "7"
---

# Ask HN: Which Jabber clients support SCRAM+ and XEP-0474

> Source: hackernews | Category: news | 2026-07-25T20:17:24Z

Score: 7 | Comments: 0

Related to this thread [1] which Jabber clients not only detect MitM tampering when a valid cert is used in the middle but is not the cert on the server, meaning an entity obtained a certificate, used it to MitM the connection and the client not only rejects this alternate valid certificate but also alerts the user to the MitM. XEP-0474 SASL SCRAM Downgrade Protection <i>(Experimental)</i> [2]  Claude does not seem to know and I can&#x27;t find any clarifying documentation, just lots of open issues.<p>The purpose is for writing an article on E2EE but I want to suggest clients that will alert on MitM tampering in a manor the person using the client can not accidentally ignore it. <i>i.e. just click through a warning</i><p>On the server side eJabberd and Prosody appear to be the only server daemons supporting XEP-0474 but I just can&#x27;t find a definitive list of supported clients even if they are in the experimental phase.  One may wish to experiment.<p>[1] - https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=37955264<p>[2] - https:&#x2F;&#x2F;xmpp.org&#x2F;extensions&#x2F;xep-0474.html
