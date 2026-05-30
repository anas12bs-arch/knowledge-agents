---
title: "prisma/prisma 7.8.0 released"
url: "https://github.com/prisma/prisma/releases/tag/7.8.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "prisma"]
date: "2026-05-30T14:31:23Z"
metadata:
  repo: "prisma/prisma"
  version: "7.8.0"
---

# prisma/prisma 7.8.0 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:23Z

## prisma/prisma — 7.8.0

Today, we are excited to share the `7.8.0` stable release 🎉

**🌟 Star this repo for notifications about new releases, bug fixes & features — or [follow us on X](https://pris.ly/x)!**

# Highlights

## ORM

### Features

**Prisma Client**

- Added a `queryPlanCacheMaxSize` option to the `PrismaClient` constructor for fine-grained control over the query plan cache. Pass `0` to disable the cache entirely, or omit it to use the default cache size. A larger value can improve performance in applications that execute many unique queries, while a smaller one can reduce memory usage. (#29503)

### Bug Fixes

**Prisma Client**

- Fixed an equality filter panic and incorrect `::jsonb` cast when filtering on PostgreSQL JSON list columns. Queries using `where: { jsonListField: { equals: [...] } }` no longer panic with a type mismatch or emit invalid SQL. (prisma/prisma-engines#5804)
- Fixed case-insensitive JSON field filtering (`mode: insensitive`), allowing `where: { jsonField: { equals: "...", mode: "insensitive" } }` to work correctly. (prisma/prisma-engines#5806)
- Fixed incorrect parameterization of enum values that have a custom database name set via `@map`. (#29422)
- Fixed a database parameter limit check (`P2029`), which could incorrectly reject or miss over-limit queries. (#29422)
- Fixed a regression that caused missing SQL Server `VARCHAR` casts for parameterized values. (prisma/prisma-engines#5801)

Schema Engine

- Fixed a misleading error message in `prisma migrate diff` that referenced the `--shadow-database-url` CLI flag, which was removed in Prisma 7. (#29455)
- Fixed `prisma migrate dev` (and shadow database migration replay in general) failing with `CREATE INDEX CONCURRENTLY cannot run inside a transaction block` when a migration contained concurrent index creation statements on PostgreSQL. (prisma/prisma-engines#5799)
- Fixed PostgreSQL introspection silently dropping sequence defaults when the database returns the schema-qualified form `pg_catalog.nextval('sequence_name'::regclass)` instead of the bare `nextval(...)`. Columns backed by sequences now correctly appear as `@default(autoincrement())` in the Prisma schema in all cases. (prisma/prisma-engines#5802)

**Driver Adapters**

- **@prisma/adapter-d1**: Savepoint operations (`createSavepoint`, `rollbackToSavepoint`, `releaseSavepoint`) now silently no-op with debug logging instead of executing SQL statements, consistent with how the D1 adapter already treats top-level transactions. (#29499)

## Open roles at Prisma

Interested in joining Prisma? We're growing and have several exciting opportunities across the company for developers who are passionate about building with Prisma. Explore our open positions on our [Careers page](https://www.prisma.io/careers#current) and find the role that's right for you.

## Enterprise support

Thousands of teams use Prisma and many of them already tap into our Enterprise & Agency Support Program for hands-on help with everything from schema integrations and performance tuning to security and compliance.

With this program you also get priority issue triage and bug fixes, expert scalability advice, and custom training so that your Prisma-powered apps stay rock-solid at any scale. Learn more or join: https://prisma.io/enterprise.
