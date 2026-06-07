---
title: "Show HN: Nightwatch, The open-source, read-only AI SRE"
url: "https://github.com/ninoxAI/nightwatch"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-07T23:42:57Z"
metadata:
  score: "4"
---

# Show HN: Nightwatch, The open-source, read-only AI SRE

> Source: hackernews | Category: news | 2026-06-07T23:42:57Z

Score: 4 | Comments: 2

nightwatch is a local-first, read-only layer on top of your monitoring. it groups alert storm into incidents, flags noisy checks and has an agent that can investigate for you live systems. You can e.g. jump from the incident into the agent directly.<p>the reason for this weekend project is that we had a kubernetes upgrade that went wrong, and at some point a rollback wasn&#x27;t possible anymore, so it had to be fixed live during the night while several problems came together. We run a lot of different systems, on-prem and several Kubernetes clusters, and in a situation like that you spend most of the time just figuring out what is actually broken and where.<p>So i thought that it would be pretty cool to have eyes in the dark in each system that can talk to your &quot;brain&quot;.<p>so the idea is to put a baby owl into each environment. Each owl runs where the systems live, keeps that environment&#x27;s credentials local, and only dials outbound to a central brain, so there is no inbound hole into prod. It exposes a set of read-only skills, and the agent uses them to gather evidence and form a root-cause hypothesis, so the on-call engineer starts with a head start instead of from zero.<p>read-only for now, i don&#x27;t trust it near prod yet and honestly neither should you.<p>llocal-first for easy self-hosting and to keep credentials on your side. the clustering and recommendations run fully offline with no llm at all. the agent needs a tool-calling llm, you can point it at a remote one, or self-host one (ollama etc.) if you want to stay fully offline.<p>for non selfhosters: before every remote llm call, nightwatch strips real secrets (unrestorable) and swaps identifiers like ips, hostnames and paths for reversible placeholders, so the model only sees masked data while real values are restored only in the proposed commands and tool calls<p>Would love if you try it in your Systems
