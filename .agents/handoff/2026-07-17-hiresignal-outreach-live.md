# Handoff: HireSignal Outreach — construido, deployado y certificado 9.9/10
**Date:** 2026-07-17 (viernes)
**Status:** Complete — sistema live en producción; el piloto espera solo el sign-off de Hugo

---

## What We Accomplished This Session

**Build completo del plan 2026-07-16 (Phases 0–4 técnicas) en un día, en el portátil:**

- **Scraper de prospectos** (`kuma-talent-sourcing/ontario-outreach/ontario_prospects.py`, commits `0e32070` + `bd8b237` pushed): postings directas de Ontario en Job Bank (`fprov=ON&fsrc=16` — verificado en vivo; los facet-params por GET NO funcionan), revelado del email de aplicación replicando el POST partial-ajax de "Show how to apply" (jakarta.faces, `action=applynowbutton`). Consent logging CASL por fila. Cosecha real: **39 empleadores, 20 Tier 1, 6 Tier 2, 13 Tier 3** en `data/prospects-20260717-082516.csv` (**solo en el portátil**, gitignored — datos de contacto).
- **Sender en hiresignal** (commits `83c6ada` + `bc7f365` pushed = deployado en DO): `api/outreach-lib.php` (tablas PG, transporte `OUTREACH_SMTP_*` separado del transaccional, guard CASL de dirección postal, tokens HMAC, templates A/B/followup EN, batch con cap 15/día + espaciado 4–9s + aborto en 3 fallos), `unsubscribe.php` público RFC 8058, `admin/outreach.php` (import CSV, batch, follow-ups, test send, supresión), runbook `docs/outreach-runbook.md`.
- **Transporte resuelto:** GoDaddy `hello@kumatalent.com` / **puerto 3535/tls** — GoDaddy bloquea auth desde IPs de DO en 465/587 con creds válidas (verificado A/B; explica el cambio GoDaddy→Gmail no documentado del 2026-06-09). Memoria: `godaddy-smtp-do-port-3535`.
- **Verificación completa:** footer CASL ✓ (Waterloo temporal), unsubscribe E2E ✓, DMARC agregado en DO DNS (`_dmarc` TXT, propagado) ✓, **mail-tester 9.9/10** (subió de 7.7 solo con DMARC; GoDaddy no firma DKIM y no hizo falta).
- **Decisión de enriquecimiento (aprobada):** Tier 3 se enriquece post-piloto con el kit **AI Lead Generator** (`kit-ai-lead-generator`, modo native $0) — NO Apify. Reglas CASL en el README de ontario-outreach. Memoria nueva: `reference_ai_lead_generator_kit`.
- **Retrospective aplicado:** Paso 8 (Email DNS) agregado a `deploy-preflight`; audit del kit limpió `__pycache__` trackeado en `ui-ux-pro-max` + `__pycache__/` al `.gitignore`.
- Env vars configuradas en DO por Andres (SMTP 3535, postal Waterloo, cap 15, token secret). Portátil ahora tiene Python 3.12 (winget) + requests/bs4/lxml.

## Where We Paused

**Last action:** `/session-close` tras certificar mail-tester 9.9/10.
**Next action:** Cuando Hugo dé el OK → importar el CSV en Admin → Outreach y enviar el primer batch (10–15 Tier 1, template A).
**Blockers:** Sign-off de Hugo (hugolancheros@outlook.com — guardado en memoria).

## Next Steps

1. **NEEDS USER INPUT (Hugo, vía Andres):** aprobar templates A/B/followup, revisar/tachar la lista de 20 Tier 1 del CSV, y confirmar la **dirección postal definitiva** (2300 University Ave E, Waterloo es temporal → actualizar `OUTREACH_POSTAL_ADDRESS` en DO si cambia).
2. Andres le envía a Hugo: test send desde el admin + los 3 templates + el CSV (está solo en este portátil: `kuma-talent-sourcing\ontario-outreach\data\prospects-20260717-082516.csv`).
3. Con el OK: import CSV → primer batch → observar respuestas/bounces 1 semana antes de subir el cap (warmup +10/semana).
4. Post-piloto: enriquecer los 13 Tier 3 con AI Lead Generator (reglas en `ontario-outreach/README.md` — solo modo native, URL de fuente exacta, nunca Hunter).
5. Quedan 74 postings de Job Bank sin procesar (el scraper retoma con `seen_jobids.json`).

## Files to Read First

- `hiresignal/docs/outreach-runbook.md` — env vars, mapa CASL, checklist del piloto, gotcha GoDaddy/3535.
- `kuma-talent-sourcing/ontario-outreach/README.md` — mecánica del scraper + reglas de enriquecimiento Tier 3.
- Memoria: `project_hiresignal_outreach` (estado completo), `godaddy-smtp-do-port-3535`, `reference_ai_lead_generator_kit`.

## Notes / Gotchas

- **Push a hiresignal = deploy a producción.** El sistema ya está live; cualquier edit futuro pasa por ese pipeline.
- Los batches reales están protegidos: cap diario 15, supresión re-verificada por envío, guard de dirección postal, confirm dialog en el admin.
- El test de unsubscribe suprimió la dirección de prueba de Andres — inofensivo (los test sends no pasan por supresión), pero si algún día hay que des-suprimir, es un DELETE manual en `outreach_suppression` (no hay UI).
- mail-tester usa dirección nueva por verificación; el 9.9 es con template A real.
- Bounces asíncronos llegan al buzón `hello@kumatalent.com` — suprimirlos manualmente desde el admin (limitación v1 documentada).

## Questions to Answer

- ¿Hugo firma con su nombre? (`OUTREACH_FROM_NAME` hoy = "Kuma Talent"; cambiarlo es 1 env var).
- Dirección postal definitiva de Kuma (Waterloo es placeholder temporal).
