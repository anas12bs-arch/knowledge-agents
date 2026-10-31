---
title: "trpc/trpc v11.22.1 released"
url: "https://github.com/trpc/trpc/releases/tag/v11.22.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "trpc"]
date: "2026-10-31T12:54:03Z"
metadata:
  repo: "trpc/trpc"
  version: "v11.22.1"
---

# trpc/trpc v11.22.1 released

> Source: github-releases | Category: changelog | 2026-10-31T12:54:03Z

## trpc/trpc — v11.22.1

## What's Changed
* Rename workflow for trusted publishing by @Nick-Lucas in https://github.com/trpc/trpc/pull/7617
* chore(ci): run lerna publish at verbose loglevel by @Nick-Lucas in https://github.com/trpc/trpc/pull/7618
* fix(publishing) pass explicit provenance settings to lerna by @Nick-Lucas in https://github.com/trpc/trpc/pull/7624
* fix(deps): update dependency srvx to v0.12.8 by @renovate[bot] in https://github.com/trpc/trpc/pull/7630
* chore(deps): update dependency docusaurus-plugin-typedoc to v1.4.3 by @renovate[bot] in https://github.com/trpc/trpc/pull/7631
* chore(deps): update dependency bun to v1.4.2 by @renovate[bot] in https://github.com/trpc/trpc/pull/7633
* chore(deps): update dependency @oxc-project/runtime to v0.152.0 by @renovate[bot] in https://github.com/trpc/trpc/pull/7632
* fix(deps): update dependency @clack/prompts to v1.8.1 by @renovate[bot] in https://github.com/trpc/trpc/pull/7636
* fix(deps): update dependency effect to v3.22.2 by @renovate[bot] in https://github.com/trpc/trpc/pull/7638
* fix(deps): update dependency jscodeshift to v17.4.0 by @renovate[bot] in https://github.com/trpc/trpc/pull/7640
* chore(deps): update actions/cache action to v6 by @renovate[bot] in https://github.com/trpc/trpc/pull/7641
* chore(deps): update actions/labeler action to v7 by @renovate[bot] in https://github.com/trpc/trpc/pull/7643
* chore(deps): update babel monorepo to v8 by @renovate[bot] in https://github.com/trpc/trpc/pull/7645
* chore(deps): update actions/setup-node action to v7 by @renovate[bot] in https://github.com/trpc/trpc/pull/7644
* chore(deps): update codecov/codecov-action action to v7 by @renovate[bot] in https://github.com/trpc/trpc/pull/7646
* chore(deps): update actions/checkout action to v7 by @renovate[bot] in https://github.com/trpc/trpc/pull/7642
* chore(deps): update denoland/setup-deno action to v2 by @renovate[bot] in https://github.com/trpc/trpc/pull/7647
* chore(deps): update dependency node to v24 by @renovate[bot] in https://github.com/trpc/trpc/pull/7651
* chore(deps): update dependency bun to v1.4.3 by @renovate[bot] in https://github.com/trpc/trpc/pull/7657
* fix(server): avoid `using` under a switch case to unbreak Bun e2e by @Nick-Lucas in https://github.com/trpc/trpc/pull/7659
* docs: fix broken trpc.io links in JSDoc and concepts chart by @SatvikMishra08 in https://github.com/trpc/trpc/pull/7658
* switch to lerna-lite by @Nick-Lucas in https://github.com/trpc/trpc/pull/7669
* chore: don't publicly hoist stub `@types/parse-path` by @KATT in https://github.com/trpc/trpc/pull/7673
* docs: note default JSON serialization on the data transformers page by @emmayusufu in https://github.com/trpc/trpc/pull/7397
* ci: run required checks in the merge queue by @KATT in https://github.com/trpc/trpc/pull/7676
* docs: sponsors sync by @KATT in https://github.com/trpc/trpc/pull/7672
* chore(ci): gate npm publishing behind npm-publish environment and admin check by @KATT in https://github.com/trpc/trpc/pull/7675
* fix(server): cancelling a streamed response aborts its calls' signals by @KATT in https://github.com/trpc/trpc/pull/7683
* fix(server): resolve record values lazily in Serialize by @musatoktas in https://github.com/trpc/trpc/pull/7660
* fix(server): preserve lazy routes when composing routers by @Marve10s in https://github.com/trpc/trpc/pull/7667
* feat(react-query): pass `trpc.context` to links in `useSubscription` by @joako1721 in https://github.com/trpc/trpc/pull/7655
* fix(server): cancel backpressured responses on disconnect by @Arthur031221 in https://github.com/trpc/trpc/pull/7661
* fix(server): keep inferred types portable without baseUrl by @HawkForge in https://github.com/trpc/trpc/pull/7662
* fix(react-query,tanstack-react-query): keep falsy inputs in query keys by @giaBaoJS in https://github.com/trpc/trpc/pull/7623
* fix(server): match content-type header case-insensitively by @kwy404 in https://github.com/trpc/trpc/pull/7614
* fix(
