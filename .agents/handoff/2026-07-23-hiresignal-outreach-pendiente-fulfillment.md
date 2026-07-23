# Handoff: HireSignal Outreach — revisión de templates + memorias recuperadas
**Date:** 2026-07-23 (jueves)
**Machine:** desktop (E:\) — importante: varios next steps NO corren desde aquí (ver Gotchas)
**Status:** In progress — diagnóstico hecho, sin cambios de código; el bloqueo real es el plan de fulfillment, NO el sign-off de Hugo

> **CORRECCIÓN aplicada al final de la sesión.** La primera versión de este handoff decía
> que el piloto esperaba el sign-off de Hugo y que faltaba definir la dirección postal.
> **Ambas cosas eran falsas.** Se recuperó la memoria del portátil (ver Gotchas) que
> registra el sign-off de Hugo del 2026-07-17 y la postal definitiva; Andrés lo confirmó.
> El bloqueo real es otro: **el plan de fulfillment.**

> **La sesión siguió después de escribir esto.** El error de arriba desató una investigación
> de causa raíz cuyo resultado vive en `2026-07-23-procedencia-causa-raiz.md` — leer ese
> primero si lo que te interesa es el proceso y no HireSignal.

---

## What We Accomplished This Session

Sesión corta de diagnóstico. No se tocó código de producción.

- **Sync de 3 repos** (todos estaban atrás): `hiresignal` 3 commits atrás → `249604f`;
  `kuma-talent-sourcing` 3 atrás → `a613d24`; repo de skills ya al día.
- **Verificación del estado real del piloto** contra el handoff del 2026-07-17. Primero se
  asentó (mal) que Hugo no había aprobado; al recuperar la memoria del portátil se descubrió
  lo contrario y Andrés lo confirmó: **Hugo firmó el 2026-07-17** (WhatsApp) los templates y
  la lista, y dio la **postal definitiva: 8B Macville Ave, Kitchener, ON N2K 1T1**. El
  bloqueo real es el **plan de fulfillment** — si un empleador contrata la búsqueda, Kuma
  todavía no tiene pool de candidatos. Pausa puesta por Andrés el 07-17.
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

**Last action:** recuperación de las 3 memorias del portátil desde el repo de continuity,
restauradas en este workspace con el estado corregido, + corrección de este handoff.
**Next action:** definir con Hugo el **plan de fulfillment** (cómo se atiende a un empleador
que diga que sí, sin pool de candidatos). Nada de envíos antes de eso.
**Blockers:** plan de fulfillment. El sign-off de Hugo YA está dado.

## Next Steps

1. **NEEDS USER INPUT (Andrés + Hugo): plan de fulfillment.** Es el bloqueo que manda —
   sin él no sale ningún batch, aunque todo lo técnico esté listo.
2. **Actualizar `OUTREACH_POSTAL_ADDRESS` en DO** a `8B Macville Ave, Kitchener, ON N2K 1T1`
   (hoy tiene el placeholder de Waterloo). Los envíos están hard-blocked mientras esa var no
   sea la real — es un cambio de env var, no de código.
3. **Decidir sobre los 4 hallazgos de templates.** El #1 (`strtolower`) y el #3
   (`"last week"`) se pueden arreglar sin nadie más; el #2 y el #4 dependen de Hugo
   (¿firma con su nombre?). **Ojo: push a hiresignal = deploy a producción.**
4. **[SOLO PORTÁTIL]** Importar el CSV en Admin → Outreach y mandar el primer batch —
   `prospects-20260717-082516.csv` está gitignored (`ontario-outreach/.gitignore` = `data/`)
   y solo existe en el portátil. **Bloqueado por el paso 1.**
5. **[SOLO PORTÁTIL]** Retomar los 74 postings de Job Bank sin procesar — el scraper
   depende de `seen_jobids.json`, que también vive bajo `data/` y por lo tanto solo en el
   portátil. Correrlo desde el desktop re-cosecharía los mismos 39 desde cero.
6. **[SOLO PORTÁTIL]** Post-piloto: enriquecer los 13 Tier 3 con AI Lead Generator (modo
   native $0, nunca Hunter) — reglas en `ontario-outreach/README.md`. Necesita el CSV.

## Files to Read First

- `hiresignal/docs/outreach-runbook.md` — env vars, mapa CASL, checklist del piloto,
  gotcha GoDaddy/puerto 3535.
- `hiresignal/api/outreach-lib.php:159-205` — los 3 templates y los 4 hallazgos de arriba.
- `.agents/handoff/2026-07-17-hiresignal-outreach-live.md` — el build completo del sistema.
  **Su sección de bloqueos está muerta** (decía "falta el sign-off de Hugo"); ya lleva aviso
  de supersedido. Lo técnico sigue válido.
- `kuma-talent-sourcing/ontario-outreach/README.md` — mecánica del scraper + reglas Tier 3.

## Notes / Gotchas

- **RESUELTO — la memoria del portátil no se pierde, pero tampoco cruza sola de máquina.**
  Las 3 memorias del 07-17 (`project_hiresignal_outreach`, `godaddy-smtp-do-port-3535`,
  `reference_ai_lead_generator_kit`) no estaban en este desktop porque la sesión del portátil
  corrió desde el workspace **`C:\Users\andre\repos\kit-skill-creator`**, así que se
  escribieron bajo el slug `C--Users-andre-repos-kit-skill-creator`, no bajo el de skills.
  Sí llegaron al repo de continuity (commit `7beeb64`), pero **`sync.ps1` es one-way**
  (`~/.claude` → repo; verificado leyéndolo, solo hay `Copy-Item` en esa dirección) — el
  restore lo hace `install.ps1`, que se corre una vez al montar máquina. Esta sesión las
  restauró **en el workspace de skills** con el estado corregido, para que carguen acá.
  **Implicación general: una memoria escrita en otro workspace NO aparece en este, aunque
  el sync haya corrido bien.** Si algo importante se escribió en el portátil, buscarlo en
  `repos\claude-continuity\memory\<slug>\` antes de darlo por perdido.
- **El estado del piloto vive en producción, no en el repo.** Las tablas
  `outreach_prospects` / `outreach_sends` / `outreach_suppression` están en el PostgreSQL de
  DO; desde el repo no se puede saber qué se envió. Mirar Admin → Outreach.
- **Push a hiresignal = deploy a producción.** El sistema de outreach ya está live.
- Bounces asíncronos llegan a `hello@kumatalent.com` y se suprimen a mano desde el admin
  (limitación v1). Las respuestas también se marcan a mano en la tabla de queue.

## Questions to Answer

- **¿Cuál es el plan de fulfillment?** Es la pregunta que destraba todo lo demás.
- ¿Hugo firma con su nombre? (`OUTREACH_FROM_NAME` hoy = "Kuma Talent"). Esto decide el
  hallazgo #2 de los templates.
- El test send a Hugo cayó en spam en Outlook (GoDaddy sin DKIM, Microsoft agresivo).
  ¿Se monitorea en el piloto o se resuelve antes? Ver la memoria restaurada.
