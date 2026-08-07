---
title: "supabase/supabase v1.26.08 released"
url: "https://github.com/supabase/supabase/releases/tag/v1.26.08"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "supabase"]
date: "2026-08-07T14:29:11Z"
metadata:
  repo: "supabase/supabase"
  version: "v1.26.08"
---

# supabase/supabase v1.26.08 released

> Source: github-releases | Category: changelog | 2026-08-07T14:29:11Z

## supabase/supabase — v1.26.08

Here’s everything that happened with Supabase in the last month:

## Supabase Select SF 2026

<img width="1200" height="486" alt="select" src="https://github.com/user-attachments/assets/45a7d284-e240-424f-ae78-3c5f301be89a" />

Supabase Select returns to San Francisco on October 2, a curated day of talks, feature deep dives, and more activations. Tickets are now available by application.

[Get your ticket →](https://select.supabase.com/)

## Supabase Pipelines is now in public alpha

<img width="1200" height="485" alt="pipelines (2)" src="https://github.com/user-attachments/assets/58787029-7894-480a-a8ac-6c95ce84e136" />

Supabase Pipelines streams Postgres changes to BigQuery in near real time, a managed CDC service you configure in the Dashboard, now available on all paid plans.

[Read the blog →](https://supabase.com/blog/supabase-pipelines-public-alpha)

## Sign in with ChatGPT is now in beta

!chatgpt.png

Sign in to Supabase with your ChatGPT account, or connect Supabase to ChatGPT on desktop, web, and mobile through the ChatGPT plugins directory.

[Read the blog →](https://supabase.com/blog/sign-in-with-chatgpt-beta)

## Unified Logs is now in open beta

<img width="2400" height="970" alt="logs" src="https://github.com/user-attachments/assets/f0d56e38-6aa2-49f7-99e9-4324104b52c3" />

Unified Logs gives you one searchable view across every Supabase service, with live tail, filtering, and a timeline.

[Read the blog →](https://supabase.com/blog/unified-logs-open-beta)

## Observability for every project with Grafana Cloud

<img width="1200" height="485" alt="grafana" src="https://github.com/user-attachments/assets/8b94a3dd-876c-429f-a291-519b35d20d3a" />

Connect any Supabase project to Grafana Cloud in one click for a pre-built dashboard, alerting, and metrics, available on every plan including Free.

[Read the blog →](https://supabase.com/blog/observability-for-every-supabase-project-with-grafana-cloud)

## Introducing Supabase Evals

<img width="1200" height="485" alt="evals" src="https://github.com/user-attachments/assets/68dcf669-0a46-42e9-814d-8e3dcb440b1c" />

Supabase Evals is now open source, a benchmark that runs AI coding agents like Claude Code and Codex against real Supabase tasks and publishes the scores.

[Read the blog →](https://supabase.com/blog/introducing-supabase-evals) 

## Searchable field-level encryption with CipherStash

<img width="1200" height="485" alt="cipherstash" src="https://github.com/user-attachments/assets/df164a2e-2779-4588-b828-7e278bfa3282" />

CipherStash adds field-level encryption to Supabase with queryable ciphertext, zero-knowledge key management, and no schema changes.

[Read the blog →](https://supabase.com/blog/searchable-field-level-encryption-with-cipherstash)

## Quick Product Announcements

- The Edge Functions overview page now shows each function's error rates, execution time, and CPU and memory use in one place. [[Twitter](https://x.com/supabase/status/2080669559967657995)]
- Extension version pinning is deprecated: from August 5, an explicit version in `CREATE` or `ALTER EXTENSION` is ignored and the default version installs with a warning. [[Changelog](https://supabase.com/changelog/extension-version-pinning-ignored)]
- The Management API `analytics/endpoints/logs.all` endpoint is migrating to the new logs endpoint, so update any clients that query project logs. [[Changelog](https://supabase.com/changelog/48235-migration-of-supabase-management-api-logs-all-analytics-endpoint-to-logs-endpoint)]
- Supabase now blocks all changes to the `realtime` schema: creating, altering, or dropping objects fails with a permission error, and RLS policies on `realtime.messages` keep working. [[Changelog](https://supabase.com/changelog/realtime-schema-locked-down-against-modification)]

## Made with Supabase

- byTheLab GEO Score measures how visible your brand is across AI search engines like ChatGPT, Claude, Perplexi
