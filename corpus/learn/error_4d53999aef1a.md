---
title: "launchd en macOS NO puede acceder a ~/Desktop por TCC: procesos background fallan con PermissionErro"
type: "error"
tags: ["macos", "launchd", "tcc"]
date: "2026-06-10T08:47:15Z"
severity: "info"
---

# launchd en macOS NO puede acceder a ~/Desktop por TCC: procesos background fallan con PermissionErro

> Type: error | Severity: info | 2026-06-10T08:47:15Z

**Context:** N/A
**Cause:** venv y working directory bajo ~/Desktop para un launchd agent
**Effect:** com.primebot.enrich fallo cada 5 min en silencio desde el 31-may

---

launchd en macOS NO puede acceder a ~/Desktop por TCC: procesos background fallan con PermissionError u Operation not permitted. Alternativas: mover recursos fuera de Desktop/Documents/Downloads, o usar scheduled tasks de Claude que corren en contexto con permisos.

---

*Auto-capturado por el sistema de aprendizaje continuo.*
