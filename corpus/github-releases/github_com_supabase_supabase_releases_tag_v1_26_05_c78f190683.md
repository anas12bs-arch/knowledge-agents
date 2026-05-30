---
title: "supabase/supabase v1.26.05 released"
url: "https://github.com/supabase/supabase/releases/tag/v1.26.05"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "supabase"]
date: "2026-05-30T14:31:22Z"
metadata:
  repo: "supabase/supabase"
  version: "v1.26.05"
---

# supabase/supabase v1.26.05 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:22Z

## supabase/supabase — v1.26.05

Here's everything that happened with Supabase in the last month:

## Custom OAuth/OIDC providers for Supabase Auth

<img width="1200" height="630" alt="customoidcproviders" src="https://github.com/user-attachments/assets/97a1bc92-f8a9-4bf4-894d-ede6a762ab2b" />

Connect any OAuth2 or OpenID Connect identity provider to your Supabase project, including GitHub Enterprise, regional IdPs, and any standards-compliant provider, with PKCE enabled by default.

[[Blog](https://supabase.com/blog/custom-oauth-oidc-providers)]

## New tables in the public schema are no longer auto-exposed to the Data API

<img width="1200" height="630" alt="schematables" src="https://github.com/user-attachments/assets/e4b0c2dc-8c7b-4361-b2fb-6eb48ff6d098" />

Starting April 28, new Supabase projects can opt out of automatic Data API exposure for public schema tables. Explicit Postgres grants are now required to make a table reachable via PostgREST or GraphQL. This becomes the default for all new projects on May 30.

[[GitHub Discussion](https://github.com/orgs/supabase/discussions/45329)]

## Supabase is now ISO 27001 certified

<img width="1200" height="630" alt="security" src="https://github.com/user-attachments/assets/34e5e97f-af0c-46f8-86b8-db09267c0b6f" />

Supabase is certified to ISO/IEC 27001:2022, covering the information security management system across the entire platform.

[[Blog](https://supabase.com/blog/supabase-is-now-iso-27001-certified)]

## Stripe Sync Engine moves to Stripe

<img width="1200" height="630" alt="stripesyncenginethumb" src="https://github.com/user-attachments/assets/3597cc93-7da2-4d0f-875c-eb1185997d8d" />

The Stripe Sync Engine, originally built by Supabase, is now part of the Stripe GitHub org. It is open source and maintained by Stripe going forward.

[[Blog](https://supabase.com/blog/stripe-sync-engine-transfer)]

## Supabase brand survey

<img width="2400" height="1260" alt="baseline-brand-survey" src="https://github.com/user-attachments/assets/8cd9c5de-bb4a-4eb5-905d-c1baefbe24ff" />

Help shape the direction of Supabase. The brand survey takes a few minutes and closes soon.

[[Take the survey](https://supabase-brand-survey-2026.lovable.app/)]

## @supabase/server

<img width="1200" height="630" alt="LinkedIn   X (1)" src="https://github.com/user-attachments/assets/0c97bc2d-e4d3-47c4-bee0-9611a3ad0370" />

A new SDK that handles auth, client creation, CORS, and context injection across runtimes. Works on Edge Functions, Vercel Functions, Deno, Bun, and Cloudflare Workers.

[[Blog](https://supabase.com/blog/introducing-supabase-server)] [[Docs](https://supabase.github.io/server/)]

## Quick Product Announcements

- The Supabase app in the Stripe Marketplace is now generally available. [[Stripe Marketplace](https://marketplace.stripe.com/apps/supabase)]
- Branching without Git is now the default. Create branches directly from the dashboard without a GitHub integration. [[Blog](https://supabase.com/blog/branching-without-git-is-now-the-default)]
- Data API settings revamped: new per-table and per-function toggles let you control which tables are exposed to PostgREST and GraphQL, with a default-privileges switch at project creation. [[Docs](https://supabase.com/docs/guides/database/data-api)]
- The Supabase changelog now has RSS feeds, tag filtering, and a `.md` feed, plus links to copy any entry as Markdown or ask Claude/ChatGPT. [[Changelog](https://supabase.com/changelog)]
- Wrappers v0.6.0 ships with a new OpenAPI FDW, Snowflake timeout support, Clerk CRUD, and several bug fixes. [[GitHub](https://github.com/supabase/wrappers/releases/tag/v0.6.0)] [[Docs](https://fdw.dev/)]
- Supabase Agent Skills: an open-source set of instructions that teach AI coding agents how to build on Supabase correctly. [[Blog](https://supabase.com/blog/supabase-agent-skills)]
- Terraform Provider v1.9.0 adds Edge Functions resource, Edge Function secrets resource, and a network ba
