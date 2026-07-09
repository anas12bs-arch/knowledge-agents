---
title: "Show HN: Pylon Sync, an agent-first full-stack realtime framework"
url: "https://www.pylonsync.com"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-09T21:42:22Z"
metadata:
  score: "6"
---

# Show HN: Pylon Sync, an agent-first full-stack realtime framework

> Source: hackernews | Category: news | 2026-07-09T21:42:22Z

Score: 6 | Comments: 0

I created Pylon to make it easier to move from hobby projects to full production apps.<p>When I work on hobby projects, I usually use React or Next.js because they are quick to set up and easy to deploy on Vercel. For production apps, I separate the frontend and backend, then deploy the backend on AWS. But setting up a full backend on AWS can be complex and costly, especially for simple apps.<p>Pylon is a full-stack, real-time framework that includes server-rendered React, TypeScript functions, entities, policies, real-time sync, built-in authentication, and support for background and scheduled jobs. By default, it uses SQLite, but you can switch to Postgres for production. The authentication system is heavily inspired by better-auth. The runtime is a Rust server that runs TypeScript functions and server-rendered React using Bun.<p>Pylon itself is inspired by Rails and focuses on convention over configuration, so you have fewer decisions to make before deploying. This approach applies to modern React apps, real-time sync, TypeScript server functions, authentication, job management, and deployment.<p>One of Pylon’s main goals is agent compatibility. It lets coding agents build and deploy apps with no setup, quick understanding, secure defaults, and easy deployment, all without requiring any third-party services. Pylon works for both quick projects and production apps where performance, observability, ownership, and self-hosting matter.<p>While it’s easy to self-host Pylon apps, Pylon Cloud provides managed hosting with a developer experience similar to Vercel. You can deploy from git or the CLI, get an instant URL, add custom domains, and go live in seconds. Each app runs on its own server, which can scale to zero, with TLS and global caching enabled.<p>If you have experience with Next.js, Vercel, Convex, Supabase, Firebase, better-auth, or Rails, I’d love to hear your feedback.<p>Create your first app: npm create @pylonsync&#x2F;pylon@latest<p>Website: <a href="https:&#x2F;&#x2F;www.pylonsync.com" rel="nofollow">https:&#x2F;&#x2F;www.pylonsync.com</a><p>Repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;pylonsync&#x2F;pylon" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;pylonsync&#x2F;pylon</a><p>Docs: <a href="https:&#x2F;&#x2F;docs.pylonsync.com&#x2F;introduction" rel="nofollow">https:&#x2F;&#x2F;docs.pylonsync.com&#x2F;introduction</a><p>LLMS: <a href="https:&#x2F;&#x2F;docs.pylonsync.com&#x2F;llms.txt" rel="nofollow">https:&#x2F;&#x2F;docs.pylonsync.com&#x2F;llms.txt</a><p>Skill: npx skills add pylonsync&#x2F;pylon<p>Examples: <a href="https:&#x2F;&#x2F;github.com&#x2F;pylonsync&#x2F;pylon&#x2F;tree&#x2F;main&#x2F;examples" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;pylonsync&#x2F;pylon&#x2F;tree&#x2F;main&#x2F;examples</a>
