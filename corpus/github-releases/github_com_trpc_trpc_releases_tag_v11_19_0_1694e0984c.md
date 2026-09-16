---
title: "trpc/trpc v11.19.0 released"
url: "https://github.com/trpc/trpc/releases/tag/v11.19.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "trpc"]
date: "2026-09-16T22:22:06Z"
metadata:
  repo: "trpc/trpc"
  version: "v11.19.0"
---

# trpc/trpc v11.19.0 released

> Source: github-releases | Category: changelog | 2026-09-16T22:22:06Z

## trpc/trpc — v11.19.0

## What's Changed
* ci(example): fix Playwright e2e ffmpeg failures by @Nick-Lucas with @Copilot in https://github.com/trpc/trpc/pull/7412
* fix(upgrade): clear the query cache on every fixture render by @noahisdai in https://github.com/trpc/trpc/pull/7448
* fix(client): abort JSONL stream on httpBatchStreamLink unsubscribe by @vinamra1102 in https://github.com/trpc/trpc/pull/7390
* fix(deps): update dependency srvx to v0.12.5 by @renovate[bot] in https://github.com/trpc/trpc/pull/7437
* docs: fix broken star history chart by @OctoBored in https://github.com/trpc/trpc/pull/7470
* fix(server): keep middleware factory declarations portable by @1988jimi in https://github.com/trpc/trpc/pull/7557
* fix(server): preserve `this` when chaining to a pre-existing dispose method by @raine-works in https://github.com/trpc/trpc/pull/7457
* chore: approve esbuild by @Nick-Lucas in https://github.com/trpc/trpc/pull/7570
* fix(server): correct assertIsRequestId boolean logic — non-NaN invalid types passed silently by @okxint in https://github.com/trpc/trpc/pull/7477
* fix(docs): fix 19 dead links in llms.txt — use permalink, absolute URLs, and H1 title by @okxint in https://github.com/trpc/trpc/pull/7465
* fix(tanstack-react-query): subscriptionOptions(skipToken).enabled incorrectly returns true by @okxint in https://github.com/trpc/trpc/pull/7464
* docs: add observable deprecation note to subscriptions reference projects by @algojogacor in https://github.com/trpc/trpc/pull/7375
* fix(client): wire the operation AbortSignal in the WebSocket link by @ATKasem in https://github.com/trpc/trpc/pull/7434
* docs: add vscode-toolkit to awesome-trpc by @wszgrcy in https://github.com/trpc/trpc/pull/7363
* docs(www): add Sury to validator library integrations by @DZakh in https://github.com/trpc/trpc/pull/7466
* docs: add Authier to awesome tRPC projects by @capaj in https://github.com/trpc/trpc/pull/7558
* fix(server): delete stale clientSubscriptions entry on subscription task rejection by @Adit-Jain-srm in https://github.com/trpc/trpc/pull/7401
* fix(server): match lazy router keys on a path boundary in getProcedureAtPath by @contactjawad in https://github.com/trpc/trpc/pull/7474
* fix(client): abort httpLink/httpBatchLink requests on unsubscribe by @SnowingFox in https://github.com/trpc/trpc/pull/7469
* chore(deps): bump vitest from 4.0.18 to 4.1.11 by @dependabot[bot] in https://github.com/trpc/trpc/pull/7584
* build(deps): upgrade node to 24.21.0 and @types/node to v24 by @Nick-Lucas in https://github.com/trpc/trpc/pull/7571
* build(deps): upgrade pnpm to v12 by @Nick-Lucas in https://github.com/trpc/trpc/pull/7572
* build(deps): upgrade tsdown to 0.23.0 by @Nick-Lucas in https://github.com/trpc/trpc/pull/7574
* build(deps): upgrade typescript to v7 for packages/* by @Nick-Lucas in https://github.com/trpc/trpc/pull/7575
* build(deps): upgrade eslint to v10 by @Nick-Lucas in https://github.com/trpc/trpc/pull/7576
* build(deps): upgrade prettier to 3.9.6 by @Nick-Lucas in https://github.com/trpc/trpc/pull/7577
* build(deps): upgrade vitest to v5 by @Nick-Lucas in https://github.com/trpc/trpc/pull/7578
* build(deps): upgrade turbo to 2.10.12 by @Nick-Lucas in https://github.com/trpc/trpc/pull/7579
* build(deps): patch security advisories in packages/* by @Nick-Lucas in https://github.com/trpc/trpc/pull/7580
* build(deps): upgrade @hey-api/openapi-ts to 0.99.0 by @Nick-Lucas in https://github.com/trpc/trpc/pull/7586
* build(deps): patch security advisories in www and examples by @Nick-Lucas in https://github.com/trpc/trpc/pull/7581
* build(deps): upgrade lerna to v10 by @Nick-Lucas in https://github.com/trpc/trpc/pull/7582
* build(deps): upgrade docusaurus to 3.10.2 by @Nick-Lucas in https://github.com/trpc/trpc/pull/7583
* fix(openapi): drop function-valued properties from generated schemas by @Nick-Lucas in https://github.com/trpc/trpc/pull/7588

## New Contributors
* @noahisdai made their first contribution in h
