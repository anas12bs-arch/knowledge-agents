---
title: "Show HN: Let's Seal – Let's Encrypt for document signing, free and self-hosted"
url: "https://github.com/letsseal/letsseal"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-27T20:39:34Z"
metadata:
  score: "29"
---

# Show HN: Let's Seal – Let's Encrypt for document signing, free and self-hosted

> Source: hackernews | Category: news | 2026-07-27T20:39:34Z

Score: 29 | Comments: 11

TLDR, Let&#x27;s Seal gives the finger to Adobe and every doc signing tool (docusign, google, etc) who pay to play with the Adobe Approved Trust List and then charge you for something that should be free.<p>Currently even the person checking if a document&#x2F;contract is sealed or code is authentic has to also be inside the same Adobe walled garden too. Verification, the part that should be free is the part everyone charges for. Thats the shape Let&#x27;s Encrypt fixed for TLS, and I wanted the same thing for documents and files.<p>The core idea therefore needed to go a bit beyond e signatures and i created an open standard (SEAL), plus free tools that implement it.<p>When you seal a file, three independent things happen.<p>1. it gets a signature from a certificate authority, chaining to a public root. 
2. its record is appended to an RFC 6962 transparency log. and 
3. its SHA256 is timestamped on a public blockchain (Bitcoin) via OpenTimestamps. 
Those three give you integrity, transparency and a timestamped proof. And importantly, none of those depend on Let&#x27;s Seal and none are gated.<p>You can verify with the tools you already have, no Let&#x27;s Seal account and no Let&#x27;s Seal software. A sealed PDF carries a standard PAdES signature, so any PDF reader validates it. A sealed build artefact carries a cosign compatible signature and a SLSA provenance attestation. The Bitcoin timestamp verifies with stock ots.<p>3 ways to use it.<p>1. The free web app. We kindly have backing from Backblaze to cover storage costs for the foreseeable. So you can upload or issue any number of documents, get a public proof page at &#x2F;d&#x2F;&lt;hash&gt; and verify it at <a href="https:&#x2F;&#x2F;verify.letsseal.org" rel="nofollow">https:&#x2F;&#x2F;verify.letsseal.org</a> for free. Multiple accounts, multiple seats, enterprise functions. Free.<p>2. Self host the whole thing. Apache-2.0, one Next.js app plus a signing service that holds the CA key on localhost. Storage is any S3-compatible bucket or local disk. If you&#x27;d rather run your own root of trust, you can.<p>3. Programmatically. via the CLI and a hosted API. This is the Let&#x27;s Encrypt&#x2F;certbot angle. Seal or anchor things from CI, or have a backend seal every invoice or report as its generated.<p>The CLI is sealbot. It runs anywhere Node runs (npx sealbot) and there are native binaries for macOS, Linux and Windows with no runtime needed.<p>Theres a GitHub Action wrapping the same tool, so a release workflow can seal its own artifacts. Its what proves our own releases.<p>KYC is semi-handled (to a degree) it&#x27;s hard to do for free (at least for now), but issuers (your companies or websites) domains can be authenticated with a DNS record added, which proves the issuer has control over a domain. Sign-in can be authenticated to an email via Google Sign in and a few others will be added to the web app in time (Same as Docusign currently). Ideas welcome on future KYC should there be a demand.<p>Feedback welcome on the standard (SPEC.md in the repo).<p>Repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;letsseal&#x2F;letsseal" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;letsseal&#x2F;letsseal</a>
Site: letsseal.org<p>Thx
