---
title: "[eff] Secure Messaging and AI Remain In Conflict Despite the Promise of TEEs"
url: "https://www.eff.org/deeplinks/2026/09/secure-messaging-and-ai-remain-conflict-despite-promise-tees"
source: "legal"
category: "legal"
tags: ["legal", "privacy", "compliance", "gdpr", "regulation", "eff"]
date: "2026-09-18T22:55:02Z"
metadata:
  {}
---

# [eff] Secure Messaging and AI Remain In Conflict Despite the Promise of TEEs

> Source: legal | Category: legal | 2026-09-18T22:55:02Z

Secure Messaging and AI Remain In Conflict Despite the Promise of TEEs

Secure messaging platforms, like Signal, WhatsApp, and recently,    encrypted RCS   , operate on a straightforward assumption: the content at each end of a conversation is private to the participants in the conversation. End-to-end encryption helps provide the mathematical guarantees that the companies who operate these messaging platforms cannot access the contents of messages. But there’s no way to guarantee what happens once the message arrives on a phone. As more devices and services introduce more artificial intelligence (AI) features into messaging apps, that line begins to blur.   
  When AI features are computed entirely on device, it’s less concerning. Yet sometimes the computing requirements are heavy enough that the computation has to be done on a company server. Tech companies tell us they have a solution for this: trusted execution environments (TEEs). But do server-side TEEs really solve the problem?  
  TEEs exist to serve many different functions, ranging from digital rights management (DRM) content protections to securely storing information in your phone's mobile wallet, but for our purposes, we’ll be focusing on how tech companies use them for their AI tools.   
  The basic idea is straightforward: most consumer devices aren’t powerful enough to handle the sorts of AI features companies want to offer, so sometimes they send data off your device to more powerful cloud servers to do the computing, then display the results on your device. Since your data is leaving your device, there’s a privacy compromise. For example, if you ask for a messaging app to summarize a conversation, it may offload that computing power to a cloud server, sending the entire contents of your messages to the cloud, then back to your phone.  
  TEEs supposedly offer a way to keep those requests private. There are several implementations out there, like Apple’s    Private Cloud Compute   , Google’s    Private AI Compute   , and WhatsApp’s    Private Processing   . It’s no
