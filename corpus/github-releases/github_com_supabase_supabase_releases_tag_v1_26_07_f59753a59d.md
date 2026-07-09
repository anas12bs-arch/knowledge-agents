---
title: "supabase/supabase v1.26.07 released"
url: "https://github.com/supabase/supabase/releases/tag/v1.26.07"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "supabase"]
date: "2026-07-09T21:43:17Z"
metadata:
  repo: "supabase/supabase"
  version: "v1.26.07"
---

# supabase/supabase v1.26.07 released

> Source: github-releases | Category: changelog | 2026-07-09T21:43:17Z

## supabase/supabase — v1.26.07

Here's everything that happened with Supabase in the last month:

## OpenCode integrates with Supabase

<img width="1200" height="630" alt="opencode-thumb" src="https://github.com/user-attachments/assets/4649228d-56e6-4d1b-a9bf-c84cbd2b95f2" />

OpenCode connects your agent to your Supabase database, Edge Functions, and logs. It configures the MCP setup for you.

[Read the blog →](https://supabase.com/blog/agentic-coding-on-supabase-with-opencode)

## TanStack DB syncs with Supabase

<img width="1200" height="630" alt="tanstack" src="https://github.com/user-attachments/assets/4d2d7894-e7a7-491e-ae77-b7507207a6a2" />

`@supabase-labs/tanstack-db` syncs TanStack DB collections with your Supabase tables over PostgREST and Realtime. It's available in alpha.

[Watch the demo →](https://x.com/supabase/status/2069429278253498562)

## Wrappers adds a MongoDB foreign data wrapper

<img width="1200" height="630" alt="querymongodbwrapper" src="https://github.com/user-attachments/assets/2c77a20b-85af-42cf-bbf9-137d79d6d379" />

Wrappers v0.6.2 lets you query and join MongoDB collections directly from Postgres. It also fixes OpenAPI FDW pagination.

[Read the docs →](https://supabase.com/docs/guides/database/extensions/wrappers/mongodb)

## Multigres supports LISTEN/NOTIFY across pooled connections

<img width="1200" height="630" alt="multigreslistennotify" src="https://github.com/user-attachments/assets/29b5fbe6-4a34-481d-83bb-5c64338f3cbc" />

Multigres keeps Postgres LISTEN/NOTIFY working even when connections are pooled away from clients.

[Read the blog →](https://multigres.com/blog/2026-05-24-listen-notify)

## Realtime Broadcast supports binary payloads

<img width="1200" height="630" alt="binarypayloads" src="https://github.com/user-attachments/assets/f61fca26-3584-4cdc-b909-cb81cf5a0c0c" />

Realtime Broadcast now sends and receives binary payloads in addition to JSON. Binary payloads cut encoding overhead for cases like sensor telemetry and live screenshot streaming.

The Dart, Kotlin, and Python clients don't support binary payloads yet, and older SDK versions silently drop them. Update your client before you rely on it.

[Read the docs →](https://supabase.com/docs/guides/realtime/broadcast)

## Quick Product Announcements

- Postgres `log_connections` now defaults to off for new projects on all tiers as of July 9, and existing Free and Pro projects are being migrated to the new default. [[GitHub Discussion](https://github.com/orgs/supabase/discussions/47197)]
- `pg_graphql` v1.6.2 ships with GraphQL schema introspection off by default, so enable it per schema if you use GraphiQL or codegen tools. [[GitHub Discussion](https://github.com/orgs/supabase/discussions/46320)]
- Audit Log Drains are available, so you can stream your project's audit logs to an external destination. [[Docs](https://supabase.com/docs/guides/security/platform-audit-logs#accessing-audit-log-drains)]
- Connect copies every environment variable `@supabase/server` needs in a single click. [[Demo](https://x.com/softwarecuddler/status/2067649901811609655)]
- Self-hosted Docker defaults changed: `API_EXTERNAL_URL` now includes the `/auth/v1` prefix, and the default image moves to Postgres 17. [[GitHub Discussion](https://github.com/orgs/supabase/discussions/47093)]

## Meet the Supabase team

- **Supabase Live:** Building high quality Supabase apps using TRAE. July 22 at 7 pm PT. [[Register](https://supabase.com/events/supabase-trae-high-quality-apps)]
- Supabase x Claude Community Meetup in Dublin. [[Register](https://luma.com/dublin-8-2026-07-meetup)]
- Hangout with the Supabase team during Casual Wednesdays on Discord at 10:00 am PT. [[Join](https://discord.supabase.com/)]

## Made with Supabase

- Shapeships: A multiplayer browser game using simultaneous-turn mechanics, built on an authoritative Supabase backend. [[Website](https://shapeships.juddmadden.com/)]
- Blind OS: An autonomous outreach and 
