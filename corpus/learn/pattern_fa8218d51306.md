---
title: "En el pipeline knowledge-agents: commitear y pushear corpus/learn/ ANTES de correr core.enrich local"
type: "pattern"
tags: ["knowledge-agents", "pipeline", "git"]
date: "2026-06-10T08:47:15Z"
severity: "info"
---

# En el pipeline knowledge-agents: commitear y pushear corpus/learn/ ANTES de correr core.enrich local

> Type: pattern | Severity: info | 2026-06-10T08:47:15Z

**Context:** N/A
**Cause:** N/A
**Effect:** N/A

---

En el pipeline knowledge-agents: commitear y pushear corpus/learn/ ANTES de correr core.enrich localmente. El enrich archiva los learn files tras vectorizarlos; si se archivan antes del push nunca llegan al CI ni al grafo. Tambien: el archivado de corpus >7d debe hacerlo SOLO el CI (local deja 992 deletes sin commitear que rompen el pull).

---

*Auto-capturado por el sistema de aprendizaje continuo.*
