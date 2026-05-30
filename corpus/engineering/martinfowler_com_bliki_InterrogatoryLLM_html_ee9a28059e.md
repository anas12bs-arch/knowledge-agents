---
title: "[martin-fowler] Bliki: Interrogatory LLM"
url: "https://martinfowler.com/bliki/InterrogatoryLLM.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-05-30T15:08:37Z"
metadata:
  {}
---

# [martin-fowler] Bliki: Interrogatory LLM

> Source: engineering | Category: engineering | 2026-05-30T15:08:37Z

Bliki: Interrogatory LLM

When we need an LLM to perform a complex task, we often need to feed it a
  lot of context. Coming up with a design for a new feature requires
  descriptions of how we want the feature to appear to the user, guidelines on
  how it should be implemented, information on external systems to consult, and
  so on. All this can be several pages of markdown. The obvious way to do
  this is for a human to write this context, but an alternative is to use an LLM to write
  this context after interviewing a human. 

 The way I can do this is to prompt the LLM to interrogate me. It should ask me
  all the questions it needs to create this appropriate context. I can feed much
  of the information it needs, and tell it other sources it needs to consult if
  it can't figure those out itself. Once it's done, it can then create the
  context report for another session (perhaps with another model) to carry out
  the next step. 

 I first saw a decent description of this approach in  Harper
  Reed's blog . A striking element of his approach is insisting that the LLM
  ask only one question at a time. (When I tried it, I found it needed to be
  frequently reminded of this.) 

 Another way to use an interrogatory LLM is to give it a document, such as a
  software specification, that captures knowledge about a domain - and then ask
  the LLM to interview a human expert to determine if the document is accurate.
  This is an alternative to getting the human expert to read the document to
  review it. People often find reviewing hard, so a conversation with an LLM
  might be more fruitful, particularly if the document isn't well-written. 

 Naturally we can use both of these, using one interrogatory LLM to build a
  document, then using other interrogatory LLMs to review it with other experts.
   

 The above is getting an LLM to create or assess context for a particular
  use of an LLM. But the technique is more broadly applicable. I've become a
  natural writer, someone who finds the pr
