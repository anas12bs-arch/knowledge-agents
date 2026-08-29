---
title: "Show HN: Typebase – A single-folder back end you write in TypeScript"
url: "https://typebase.io"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-29T15:11:18Z"
metadata:
  score: "17"
---

# Show HN: Typebase – A single-folder back end you write in TypeScript

> Source: hackernews | Category: news | 2026-08-29T15:11:18Z

Score: 17 | Comments: 1

Hey HN!<p>I built Typebase, a library that gives you Convex&#x27;s DX with Supabase&#x27;s openness.<p>After trying Supabase I liked how fast it is to spin up a DB and auth, but really didn&#x27;t like using RLS and SQL for authorization. With Convex I loved how your server &quot;lives&quot; in your code, but disliked the DB model and the realtime-first defaults.<p>With Typebase you just write TS files inside a typebase&#x2F; folder in your existing repo. You can define your DB tables inside a schema.ts file and export server functions that your frontend calls like local functions, fully typed. Auth is built in.<p>Then one CLI command uploads your server to any of the available providers (Vercel, Cloudflare Workers or Deno Deploy for the servera and Neon for the DB), or generates the code so you can deploy it wherever you want.<p>Built on top of oRPC, Drizzle, and better-auth.<p>Happy to answer any questions or feedback!
