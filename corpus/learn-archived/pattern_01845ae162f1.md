---
title: "Mobile responsiveness root cause in lex-premium: navbar (.nav-99 + .nav-inner) and customizer (.cust"
type: "pattern"
tags: ["css", "mobile", "responsive", "overflow", "lex-premium"]
date: "2026-05-31T07:45:01Z"
severity: "info"
---

# Mobile responsiveness root cause in lex-premium: navbar (.nav-99 + .nav-inner) and customizer (.cust

> Type: pattern | Severity: info | 2026-05-31T07:45:01Z

**Context:** N/A
**Cause:** fixed-width flex/grid children expand beyond container without min-width:0
**Effect:** horizontal scroll on viewports < container minimum forces body wider than viewport

---

Mobile responsiveness root cause in lex-premium: navbar (.nav-99 + .nav-inner) and customizer (.customizer-builder + .order-hpan-*) lacked min-width:0 / minmax(0,1fr) / max-width:100vw, causing 57px horizontal overflow on 375px viewports. Fix: add box-sizing:border-box + max-width:100vw on root, min-width:0 on flex/grid children, minmax(0,1fr) on grid templates with text content, and html overflow-x:hidden alongside body.

---

*Auto-capturado por el sistema de aprendizaje continuo.*
