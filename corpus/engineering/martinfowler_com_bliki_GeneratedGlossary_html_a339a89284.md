---
title: "[martin-fowler] Bliki: Generated Glossary"
url: "https://martinfowler.com/bliki/GeneratedGlossary.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-11-12T19:53:41Z"
metadata:
  {}
---

# [martin-fowler] Bliki: Generated Glossary

> Source: engineering | Category: engineering | 2026-11-12T19:53:41Z

Bliki: Generated Glossary

When we use LLMs in a specialized domain, such as the operations of any
  reasonably-large organization, there is a lot of specialized vocabulary. Such
  words and specialized meanings will be foreign to an LLM because they aren't
  in its training set, making it harder for the LLM to be effective when doing
  tasks in that domain. One technique to aid this is to use an LLM to generate a
  glossary of the terminology in that domain, and make this glossary available
  for any LLMs doing work in those circumstances. 

 The sources for the LLM can be any material within the organization
  concerned such as documents, emails, and chat logs. In some cases getting
  transcripts of audio or video may be helpful, although most organizations
  generate enough text to do the job. 

 The glossary-generating LLM should look for single words, and phrases of
  several words that regularly hang out together to form a meaningful term. The
  generator should be asked to identify terms that are new to it, but also known
  terms that are being used in unfamiliar ways. The latter can often cause the
  most confusion. 

 Once we have a list of specialized vocabulary we can ask the agent to
  produce a glossary, with definitions for each term. Some terms may
  be used in different ways, in which case the LLM should provide alternative
  definitions, with a note as to what context the differences appear in. The LLM
  can be asked to follow the output format of a dictionary, with a focus on
  precision and conciseness. 

 Once we have a draft glossary, then  human experts in that domain should
  review it, and amend it for cases where the LLM has got the wrong ends of
  sticks. 

 We then put the glossary somewhere where any other LLM can use it. It
  should be in a form that's easy for the LLM to consult, and minimize the
  tokens the LLM should consume in order to find meaning. We should set up a
  schedule to review and refresh the glossary at regular intervals, by agents
  and humans
