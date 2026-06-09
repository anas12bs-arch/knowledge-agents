---
title: "Diferencias TEST vs LIVE en Stripe NO son solo cambiar las api keys. Además del swap de keys, hay qu"
type: "insight"
tags: ["stripe", "live", "produccion", "99cc", "compliance"]
date: "2026-06-07T14:38:58Z"
severity: "info"
---

# Diferencias TEST vs LIVE en Stripe NO son solo cambiar las api keys. Además del swap de keys, hay qu

> Type: insight | Severity: info | 2026-06-07T14:38:58Z

**Context:** N/A
**Cause:** N/A
**Effect:** N/A

---

Diferencias TEST vs LIVE en Stripe NO son solo cambiar las api keys. Además del swap de keys, hay que: (1) completar KYC de la cuenta Stripe para que acepte pagos LIVE, (2) habilitar 3DS/SCA en create-checkout-session porque Europa obliga PSD2 — añadir automatic_payment_methods: enabled true, (3) añadir idempotency keys a refund-order para evitar doble refund si cliente hace doble click, (4) reconfigurar webhook en Stripe dashboard para LIVE mode apuntando a la misma edge function, (5) STRIPE_WEBHOOK_SECRET es distinto en LIVE, (6) manejar errores reales (3DS, fraude, fondos, timeouts) que en TEST no aparecen, (7) flujo de disputas/chargebacks NO es un refund, es separado

---

*Auto-capturado por el sistema de aprendizaje continuo.*
