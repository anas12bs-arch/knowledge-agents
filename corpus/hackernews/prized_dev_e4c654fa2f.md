---
title: "Launch HN: Prized (YC S26) – Let non-engineer staff build secure internal tools"
url: "https://prized.dev"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-30T16:10:24Z"
metadata:
  score: "35"
---

# Launch HN: Prized (YC S26) – Let non-engineer staff build secure internal tools

> Source: hackernews | Category: news | 2026-07-30T16:10:24Z

Score: 35 | Comments: 19

Hi HN, we&#x27;re Marinos and Hudson, founders of Prized (<a href="https:&#x2F;&#x2F;prized.dev">https:&#x2F;&#x2F;prized.dev</a>)! Prized lets non-engineer employees describe the internal tool they need and get a full-stack app, wired to their company’s data and deployed behind the company’s sign-in, without them ever juggling API keys or connectors.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=730MuYOfZTY" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=730MuYOfZTY</a><p>The way Prized provides security is by limiting what the agent can reach at the network layer and by keeping credentials out of the sandbox entirely. The sandbox never holds any keys or connector secrets, it only uses scoped session tokens that are stored as opaque placeholders. The real values are swapped into the request headers on our egress proxy. When production data is connected, the sandbox&#x27;s network policy is set to deny by default so the only path out is via the proxy. Any call the agent makes to an external connector is reviewed by an LLM judge to prevent dangerous operations.<p>Prized is meant for the internal workflows that start as notebooks or spreadsheets but never become real tools because engineering has more important things to work on. One customer’s data scientist pasted in his personal fraud-detection notebook with hardcoded thresholds and all. After a few prompts, it became a published risk console connected to the company’s data with those thresholds turned into UI controls. Earlier today, we got off a call with them and most of their company is using it.<p>To do this, you need to give people the freedom to build without having unaudited access to company systems. We allow admins to scope data to specific users or teams and data access is recorded in an audit log. Each tool is built with its own Postgres schema and role, with queries running via an authenticated SQL gateway as that role.<p>We think Prized sits between products like Lovable and Retool. Lovable makes it easy to generate and host software, but it isn’t designed around distribution with permissions. Retool generally assumes that a technical builder is creating an app for an end user.<p>Prized treats internal tools as shared objects. Anyone in the workspace can see what others have built, fork, and connect different data. For example, one customer’s marketing lead built a promotional analytics tool. A data scientist at the same company then forked it and added confidence intervals with the existing tool as a starting base. This way workspaces become libraries of tools that people can reuse.<p>We’re live and self-serve. Our free tier includes 2 tool builds&#x2F;month and our Teams tier is $100&#x2F;month. The Enterprise tier is custom and supports personalized features like on-prem deployment.<p>We&#x27;re still working out the right boundary between control and freedom. If you&#x27;ve built internal tools before we&#x27;d appreciate your feedback!
