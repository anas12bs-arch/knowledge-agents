---
title: "Claude Code PostToolUse hooks NO reciben exit_code para Bash: tool_response solo trae stdout, stderr"
type: "error"
tags: ["claude-code", "hooks", "bash"]
date: "2026-06-10T08:47:15Z"
severity: "info"
---

# Claude Code PostToolUse hooks NO reciben exit_code para Bash: tool_response solo trae stdout, stderr

> Type: error | Severity: info | 2026-06-10T08:47:15Z

**Context:** N/A
**Cause:** hook comparaba exit_code inexistente, siempre 0
**Effect:** el hook de captura de errores nunca se disparo durante meses

---

Claude Code PostToolUse hooks NO reciben exit_code para Bash: tool_response solo trae stdout, stderr, interrupted, isImage, noOutputExpected. Detectar fallos por patrones en stderr, no por exit code.

---

*Auto-capturado por el sistema de aprendizaje continuo.*
