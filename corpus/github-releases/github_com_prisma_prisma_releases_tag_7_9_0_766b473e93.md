---
title: "prisma/prisma 7.9.0 released"
url: "https://github.com/prisma/prisma/releases/tag/7.9.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "prisma"]
date: "2026-07-21T08:45:48Z"
metadata:
  repo: "prisma/prisma"
  version: "7.9.0"
---

# prisma/prisma 7.9.0 released

> Source: github-releases | Category: changelog | 2026-07-21T08:45:48Z

## prisma/prisma — 7.9.0

Today, we are excited to share the `7.9.0` stable release 🎉

**🌟 Star this repo for notifications about new releases, bug fixes & features — or [follow us on X](https://pris.ly/x)!**

# Highlights

## ORM

### Tab completions for the Prisma CLI

Typing out CLI commands from memory is now optional. Prisma ships **shell tab completions** for `bash`, `zsh`, `fish`, and PowerShell, covering commands, subcommands, options, flags, and even option values.

**Setting it up.** Most projects run Prisma through a package manager, so completions are enabled through `@bomb.sh/tab`'s package-manager integration — install it once, then source the completion for your package manager and shell:

```bash
# 1. Install @bomb.sh/tab globally
npm install -g @bomb.sh/tab

# 2. Wire up your package manager + shell (pnpm shown; swap in npm / yarn / bun):
echo 'source <(tab pnpm zsh)'  >> ~/.zshrc            # zsh
echo 'source <(tab pnpm bash)' >> ~/.bashrc           # bash
tab pnpm fish > ~/.config/fish/completions/pnpm.fish  # fish
tab pnpm powershell > ~/.tab-pnpm.ps1                 # PowerShell (then dot-source it from $PROFILE)
```

`@bomb.sh/tab` delegates to any locally-installed CLI that ships completions, so `pnpm prisma <TAB>`, `pnpm exec prisma <TAB>`, `yarn prisma <TAB>`, and `bun x prisma <TAB>` all complete Prisma's commands, options, and values — no per-project setup. (`npx` and `bunx` don't support completion themselves; use `npm exec` and `bun x`.)

If instead you have Prisma installed globally on your `PATH`, source its own completion directly: `source <(prisma complete zsh)` (or the `bash` / `fish` / `powershell` variant).

This is built on [`@bomb.sh/tab`](https://github.com/bombshell-dev/tab/), the same completion library that powers other CLIs in the ecosystem — including Cloudflare, Nuxt, and Vitest — so the package-manager completions you enable for Prisma work for those tools too. A wonderful community contribution from [@AmirSa12](https://github.com/AmirSa12) ([#28351](https://github.com/prisma/prisma/pull/28351)) — thank you!

https://github.com/user-attachments/assets/1f916a60-ee4d-40be-bb7d-74035d48ca83

### Prisma ORM, ready for AI agents

Coding agents are now a first-class audience for Prisma, and 7.9.0 brings the first wave of work to make Prisma projects safe and productive for them to work in.

**Agent skills installed with `prisma init`** ([#29689](https://github.com/prisma/prisma/pull/29689))

`prisma init` now installs the [prisma/skills](https://github.com/prisma/skills) catalog into freshly scaffolded projects. Agents such as Claude Code, Cursor, Codex, and Windsurf start out with current, version-relevant Prisma knowledge instead of relying on whatever happened to be in their training data. The install is best-effort and never blocks scaffolding; opt out at any time with `--no-skills`.

```terminal
npx prisma@latest init
```

![prisma init scaffolds a project and installs the Prisma agent skills catalog](https://github.com/user-attachments/assets/8244a6dc-cdad-4028-a652-bb5ac6e4b271)

**A safer default around destructive commands** ([#29684](https://github.com/prisma/prisma/pull/29684), [#29691](https://github.com/prisma/prisma/pull/29691), [#29713](https://github.com/prisma/prisma/pull/29713))

Prisma's AI safety checkpoint refuses to run destructive commands when it detects that an AI agent is at the keyboard, unless the user has given explicit consent. In this release we:

- **Broadened agent detection** to cover today's landscape — Codex CLI (now on Linux as well as macOS), Qwen Code, GitHub Copilot CLI, OpenCode, Cline, Goose, Amp, Crush, Augment Code, Antigravity, Replit Agent, and Devin — plus generic `AI_AGENT` / `AGENT` conventions so future agents are caught without a code change.
- **Extended the guard to `db push --accept-data-loss`**, which previously bypassed the checkpoint even though it can drop data.
- **Removed the `migrate-reset` tool from 
