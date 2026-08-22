---
title: "Show HN: Anonymous age verification with passkey-powered encryption"
url: "https://loginwithone.com/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-22T18:26:43Z"
metadata:
  score: "17"
---

# Show HN: Anonymous age verification with passkey-powered encryption

> Source: hackernews | Category: news | 2026-08-22T18:26:43Z

Score: 17 | Comments: 9

This project has been kicking around in my head since I first heard about the webauthn PRF extension in early 2024. I&#x27;ve slowly chipped away at it since, and finally got things to a shareable state over the summer thanks to a very fun parental leave. Headed back to work tomorrow, so I figure there&#x27;s no time like the present.<p>tldr: A client-held encryption key derived during passkey authentication encrypts all sensitive user data prior to persistence so that only the user is able to decrypt and reuse that data on their device. This allows short-lived, privacy-preserving age proofs to be issued to requesting applications (18+, no PII shared) without requiring users to re-upload their documents. The SSO user experience is built on top of the OAuth 2.0 Authorization Code Flow.<p><a href="https:&#x2F;&#x2F;loginwithone.com" rel="nofollow">https:&#x2F;&#x2F;loginwithone.com</a> - demo video + high-level architecture + FAQ<p>I also made the parody demo apps from the video public if anyone wants to play around with the user experience:<p><a href="https:&#x2F;&#x2F;demo.brainrot.loginwithone.com" rel="nofollow">https:&#x2F;&#x2F;demo.brainrot.loginwithone.com</a> 
<a href="https:&#x2F;&#x2F;demo.dgnrt.loginwithone.com" rel="nofollow">https:&#x2F;&#x2F;demo.dgnrt.loginwithone.com</a>
<a href="https:&#x2F;&#x2F;demo.kirby.loginwithone.com" rel="nofollow">https:&#x2F;&#x2F;demo.kirby.loginwithone.com</a><p>I suspect most will choose to pass on the ID stage for now (no offense taken, doing so is low reward in this context) but if you navigate to <a href="https:&#x2F;&#x2F;app.loginwithone.com" rel="nofollow">https:&#x2F;&#x2F;app.loginwithone.com</a> after onboarding you can demonstrate the passkey-powered encryption on your email via the lock&#x2F;unlock button.<p>Very open to feedback and happy to answer any questions! I plan to pull the client-side encryption functionality into an open-source typescript library for general use, so any thoughts or suggestions on what you’d like to see out of that interface would be supremely useful. Thanks all,<p>Michael
