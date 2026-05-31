---
title: "Hook PostToolUse en settings.json captura errores bash automaticamente sin que Claude tenga que reco"
type: "pattern"
tags: ["hooks", "auto-learning", "bash"]
date: "2026-05-31T13:04:06Z"
severity: "info"
---

# Hook PostToolUse en settings.json captura errores bash automaticamente sin que Claude tenga que reco

> Type: pattern | Severity: info | 2026-05-31T13:04:06Z

**Context:** N/A
**Cause:** Claude olvidaba ejecutar core.learn manualmente despues de errores
**Effect:** ahora cada bash con exit != 0 genera automaticamente un archivo en corpus/learn/ para vectorizacion

---

Hook PostToolUse en settings.json captura errores bash automaticamente sin que Claude tenga que recordar — exit code != 0 dispara core.learn con causa y efecto

---

*Auto-capturado por el sistema de aprendizaje continuo.*
