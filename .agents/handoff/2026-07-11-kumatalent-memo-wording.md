# Handoff: Kumatalent — cambios de wording "global" de Memo (live)
**Date:** 2026-07-11
**Status:** Complete — cambios live y verificados en producción; 2 pendientes de decisión ajena
---
## What We Accomplished This Session
- Bajé el `index.html` live de kumatalent.com, verifiqué que era byte-idéntico al repo `kuma-talent-web`, y subí copia a Drive de berandre2 (`kumatalent-landing-EN-2026-07-10.html`, id `1pgKqzfpt9bl00rT5GXR2gOS3RPA0BT5Z`) — verificada por fileSize (67,102 bytes).
- Leí el change-spec de Memo (Google Doc `1c3LViMzq-cxav9T35SFJQrFUOWv8TjruMyAc1jfONiU`) y apliqué en `kuma-talent-web` (commit `68d3e67`, EN + FR en sync): doble camino Canadá/LatAm (paso 3 del ROI card + sección nueva "Two ways to hire" `#ways`), lead "vetting is our specialty" (hero/entry/card), SEO ampliado (title, description, og:description).
- **NO se aplicaron** (decisión de Andrés, "por ahora"): cambios 1a/1b/2 del spec — los time-promises ("5 days to shortlist", "productive from week one", "first quarter") siguen live.
- Fix sobre el spec: su grid inline style rompía el collapse móvil (inline > media query) → implementado como `#ways .pillars` + override en la media query de 1000px.
- Deploy verificado en producción (curl + grep de marcadores EN y FR, title nuevo, time-promise intacto).
- Session close: retrospectiva aplicada (4 items), audit del kit aplicado (3 SKILL.md al cap de 50 líneas), memorias nuevas `feedback_client_spec_qa` y `reference_drive_mcp_limits`.

## Where We Paused
**Last action:** session close (este handoff).
**Next action:** ninguna acción técnica pendiente. Cuando Memo responda: (1) decisión sobre quitar los time-promises (sus find/replace listos en el Doc, cambios 1a/1b/2), (2) revisión del copy FR-CA y SEO que redactó Claude (live sin revisión nativa).
**Blockers:** ambas cosas esperan a Memo/Andrés, no al agente.

## Files to Read First
- `C:\Users\andre\.claude\projects\c--Users-andre--claude-skills\memory\project_kumatalent_wording_global.md` — estado completo + flags pendientes
- Google Doc de Memo (id arriba) — spec original con los cambios no aplicados
- `C:\Users\andre\repos\kuma-talent-web\index.html` / `fr.html` — estado live (push a master = deploy DO)

## Notes / Gotchas
- Specs HTML de cliente se revisan como código de terceros (inline styles vs media queries, encoding del destino) — ver memoria `feedback_client_spec_qa`.
- fr.html mezcla acentos literales y entidades HTML por zonas — matchear el estilo del contexto al editar.
- Drive no renderiza HTML (muestra código); conector MCP fijo a berandre2, sin share/move/delete — ver memoria `reference_drive_mcp_limits`. kumatalent49 no comparte ninguna carpeta escribible.
- La copia en Drive quedó desactualizada vs producción (es la versión pre-cambios); Andrés decidió no refrescarla por ahora.
- Hubo caída temporal del clasificador de permisos (Bash/PowerShell bloqueados ~minutos); el push lo hizo Andrés a mano con el comando que le pasé.

## Questions to Answer
- ¿Memo aprueba quitar los time-promises? (cambios 1a/1b/2 de su spec, listos para aplicar)
- ¿Quién revisa el FR-CA nuevo? (redacción de Claude, live sin revisión nativa)
