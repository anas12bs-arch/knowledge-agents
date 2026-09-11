---
title: "[eff] Cold TAKE: Amazon's New Encryption Method Still Doesn't Deliver Real Privacy"
url: "https://www.eff.org/deeplinks/2026/09/cold-take-amazons-new-encryption-method-still-doesnt-deliver-real-privacy"
source: "legal"
category: "legal"
tags: ["legal", "privacy", "compliance", "gdpr", "regulation", "eff"]
date: "2026-09-11T17:22:38Z"
metadata:
  {}
---

# [eff] Cold TAKE: Amazon's New Encryption Method Still Doesn't Deliver Real Privacy

> Source: legal | Category: legal | 2026-09-11T17:22:38Z

Cold TAKE: Amazon's New Encryption Method Still Doesn't Deliver Real Privacy

Amazon recently debuted a new feature for its Ring cameras that the company is calling    Throw Away the Key Encryption    (TAKE). The idea is to cut back on the amount of video content available to the company, and thus potentially available to law enforcement. But while it might technically add a speed bump to accessing full video content, it doesn’t deliver nearly the level of privacy we should be demanding from video doorbells and other security cameras.  
  TAKE introduces a new way for Ring to manage encryption keys, where the user’s device has its key, then the company holds encryption keys temporarily within its own cloud infrastructure. Ring’s servers receive the keys temporarily so it can offer a variety of the features it says it can’t offer when a user chooses to use end-to-end encryption, like video descriptions, smart alerts, video search,    and more   , then deletes the key after 24 hours.   
  This differs from how it works now, where footage is encrypted in transit and at rest, then decrypted by Ring, which always has access to the footage, to process those features.   
  Comparatively, this is an improvement to the default settings Ring has now, because it at least puts some restrictions on historical footage, but it has some serious holes worth exploring.  
  Ring Gets Access to Unencrypted Video for a Short Period  
  Ring has designed its service so many of its camera features, including smart alerts and video search, need cloud processing to work. That means to provide those features, Ring needs to decrypt the footage while it’s stored in Ring’s cloud servers.   
  With TAKE, in order to decrypt footage to offer these features, Ring gets access to footage stored in the cloud for 24 hours. TAKE adds some small measures using secure enclaves to make base key material harder to directly export, but keys are still released to services that can be modified. With access to the keys, the cloud processing does its thing and delivers the requested
