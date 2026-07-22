# Handoff: HireSignal Outreach — revisión de templates, piloto sigue esperando a Hugo
**Date:** 2026-07-22 (miércoles)
**Machine:** desktop (E:\) — importante: varios next steps NO corren desde aquí (ver Gotchas)
**Status:** In progress — diagnóstico hecho, sin cambios de código; el paquete de sign-off para Hugo quedó pendiente por decisión del usuario

---

## What We Accomplished This Session

Sesión corta de diagnóstico. No se tocó código de producción.

- **Sync de 3 repos** (todos estaban atrás): `hiresignal` 3 commits atrás → `249604f`;
  `kuma-talent-sourcing` 3 atrás → `a613d24`; repo de skills ya al día.
- **Verificación del estado real del piloto** contra el handoff del 2026-07-17: confirmado
  con el usuario que **Hugo aún no aprueba**, o sea el bloqueo no se movió en 5 días.
- **Revisión crítica de los 3 templates de outreach** (`api/outreach-lib.php:159-205`) —
  4 hallazgos, ninguno aplicado (2 dependen de decisiones de Hugo):
  1. **`strtolower($roles[0])` sin excepciones** (línea 163) destroza siglas en el asunto:
     un posting "IT support technician" sale como *"Your it support technician posting —
     a faster way to a shortlist"*. Verificado en código; **no probado contra los títulos
     reales** — el CSV con los 39 empleadores está solo en el portátil.
  2. **Voz inconsistente:** el template A dice *"**We** built HireSignal"*, el follow-up
     dice *"a quick follow-up on **my** note last week"*. Con `OUTREACH_FROM_NAME = "Kuma
     Talent"` (empresa), "my note" no cuadra. Se resuelve junto con la pregunta abierta
     de si Hugo firma con su nombre.
  3. **`"last week"` hardcodeado** en el follow-up (línea 175). El admin filtra por
     `sent_at <= now() - interval '7 days'` (`admin/outreach.php:95`), o sea 7 días **o
     más**, y el botón es manual: si sale a las 3 semanas, el email miente sobre su propia
     cronología. Menor, pero roza el "no misleading" de CASL.
  4. **Los 3 abren con "Hi," pelado**, sin nombre de contacto (el scraper solo consigue el
     email de aplicación). No es compliance, es el mayor lastre de respuesta. Decisión de Hugo.
- **Retrospective aplicado** a `handoff/workflows/file-handoff.md`: campo `**Machine:**` en
  la plantilla + regla nueva en el paso 3 para marcar next steps atados a una máquina.
  Nació de que 2 de los 5 next steps del handoff del 17 son inejecutables desde el desktop.

## Where We Paused

**Last action:** el usuario pidió dejar el paquete de sign-off pendiente y cerrar sesión,
justo antes de que yo eligiera idioma para ese documento.
**Next action:** decidir si se arma el paquete de sign-off para Hugo (los 3 templates
renderizados + las 4 observaciones + las 2 preguntas abiertas) o si Andrés lo habla con él
directo.
**Blockers:** sign-off de Hugo (hugolancheros@outlook.com). Sin eso no sale ningún batch.

## Next Steps

1. **NEEDS USER INPUT (Hugo, vía Andrés)** — sigue igual que el 17: aprobar templates
   A/B/followup, revisar la lista de 20 Tier 1, y confirmar la **dirección postal
   definitiva** (2300 University Ave E, Waterloo es temporal → `OUTREACH_POSTAL_ADDRESS`
   en DO). Los envíos están hard-blocked mientras esa var no tenga valor real.
2. **Decidir sobre los 4 hallazgos de templates.** El #1 (`strtolower`) y el #3
   (`"last week"`) se pueden arreglar sin Hugo; el #2 y el #4 no. **Ojo: push a hiresignal
   = deploy a producción.**
3. **[SOLO PORTÁTIL]** Importar el CSV en Admin → Outreach y mandar el primer batch —
   `prospects-20260717-082516.csv` está gitignored (`ontario-outreach/.gitignore` = `data/`)
   y solo existe en el portátil.
4. **[SOLO PORTÁTIL]** Retomar los 74 postings de Job Bank sin procesar — el scraper
   depende de `seen_jobids.json`, que también vive bajo `data/` y por lo tanto solo en el
   portátil. Correrlo desde el desktop re-cosecharía los mismos 39 desde cero.
5. **[SOLO PORTÁTIL]** Post-piloto: enriquecer los 13 Tier 3 con AI Lead Generator (modo
   native $0, nunca Hunter) — reglas en `ontario-outreach/README.md`. Necesita el CSV.
6. **Diagnosticar el hueco de memoria** (ver Gotchas) — requiere tener el portátil a mano.

## Files to Read First

- `hiresignal/docs/outreach-runbook.md` — env vars, mapa CASL, checklist del piloto,
  gotcha GoDaddy/puerto 3535.
- `hiresignal/api/outreach-lib.php:159-205` — los 3 templates y los 4 hallazgos de arriba.
- `.agents/handoff/2026-07-17-hiresignal-outreach-live.md` — el build completo del sistema.
- `kuma-talent-sourcing/ontario-outreach/README.md` — mecánica del scraper + reglas Tier 3.

## Notes / Gotchas

- **3 memorias citadas por el handoff del 17 no existen en este desktop:**
  `project_hiresignal_outreach`, `godaddy-smtp-do-port-3535`, `reference_ai_lead_generator_kit`.
  Verificado: `git log --all -- "*outreach*" "*godaddy*" "*lead_generator*"` en el repo de
  memoria no devuelve nada, y su último commit es del 2026-07-12 (anterior a la sesión del 17).
  **No está diagnosticado dónde falló** — puede ser que la sesión del portátil nunca corriera
  el sync, o que el sync no cubra esa dirección. No asumir que el contenido de esas memorias
  está perdido: probablemente está vivo en el portátil. Revisar con esa máquina a mano.
- **El estado del piloto vive en producción, no en el repo.** Las tablas
  `outreach_prospects` / `outreach_sends` / `outreach_suppression` están en el PostgreSQL de
  DO; desde el repo no se puede saber qué se envió. Mirar Admin → Outreach.
- **Push a hiresignal = deploy a producción.** El sistema de outreach ya está live.
- Bounces asíncronos llegan a `hello@kumatalent.com` y se suprimen a mano desde el admin
  (limitación v1). Las respuestas también se marcan a mano en la tabla de queue.

## Questions to Answer

- ¿Se arma el paquete de sign-off para Hugo, y en qué idioma? (quedó sin responder al
  cerrar — la duda era si Hugo lo reenvía a alguien del lado canadiense).
- ¿Hugo firma con su nombre? (`OUTREACH_FROM_NAME` hoy = "Kuma Talent"). Esto decide el
  hallazgo #2 de los templates.
- Dirección postal definitiva de Kuma (Waterloo es placeholder).
