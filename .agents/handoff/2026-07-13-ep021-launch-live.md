# Handoff: BTQ EP.021 — lanzado, verificado y pipeline cerrado

**Date:** 2026-07-13 (lunes)
**Status:** Complete — pipeline EP.021 cerrado end-to-end; solo queda que Andy publique las quote cards según el calendario B2 (acción humana, no de agente).

---

## What We Accomplished This Session

- **URL de Spotify de EP.021 recibida y propagada** (commit `7f610e6`):
  `https://open.spotify.com/episode/0VH2eMppsNMBl3JqTEq4T0` → launch file EP021, roadmap
  ("publicado"). De paso se registró la URL de EP.020 en SU launch file (estaba "pendiente"
  desde su propio lanzamiento; se recuperó del badge del sitio live cruzada con el roadmap).
- **Stage C.4 — grid rotado:** `019,018,017,016` → `020,019,018,017` (entra EP.020 Ley de
  Goodhart, sale EP.016 The Wall); badge "Última pista" → 021 · Los Simpson. OJO: el markup
  real del grid BTQ es `stag`/`track`/`.t-*` (el workflow 04 decía `ep-list`/`ep-row` — ya
  corregido en la retro).
- **Stage C.5 — deploy verificado:** preflight PASS → gate aprobado → `vercel --prod`
  (dpl_Ht8jFrWiHL2rNWihx54LnQ6McYTR, aliased) → HTTP 200 con los 3 marcadores nuevos en el
  HTML servido → EP.21 visible en la página pública de Spotify. `pipeline-state-ep021.md`:
  **stage_c: complete**. Bitácora completa en `pipeline-audit-ep021.md`.
- **Calendario de quote cards (§B2 del launch file, commit `a8cb2e9`):** ejecutado por un
  agente Sonnet con contrato de Fable. 3 cards 16:9 existentes (NO se regeneran, NO hay
  derivados 1:1/9:16 — decisión de Andy): lun 13 tarde CARD1 (micrófono), mié 15 CARD2 (CRT),
  vie 17 CARD3 (vela). LinkedIn prioritaria (link en 1er comentario) + IG/FB (link en bio).
  Las citas de los captions se corrigieron para coincidir letra por letra con el texto
  RENDERIZADO en las cards (verificado contra las 3 imágenes), no con el SRT crudo.
- **Corrección de fechas:** el lanzamiento fue el domingo 12-jul 8PM (no "domingo 13" como
  decía el handoff anterior — el 13 es lunes). El plan social del launch file siempre estuvo
  bien; el error venía del handoff.
- **Retrospectiva aplicada (6/6, commit `5de410e`):** regla de coherencia fecha+día en
  handoff/SKILL.md; captions = texto de card en 03b; markup BTQ actualizado en 04; propagar
  URL del episodio lanzado a su launch file en 04 Paso 0; referencia stale al hook
  `deploy-preflight-gate.ps1` eliminada de 05; memoria `user_delegation_model` reforzada
  (producción de contenido en pipelines se delega a Sonnet por defecto, sin recordatorio).

## Where We Paused

**Last action:** cierre de sesión (retro aplicada, audit del kit sin hallazgos, este handoff;
siguen continuity sync + chequeo de memory-audit).
**Next action:** nada de agente para EP.021 — Andy publica las 3 quote cards según §B2 de
`EP021-simpsons-launch.md` (lun 13 tarde / mié 15 / vie 17). Próximo trabajo de pipeline:
EP.022 (tema aún sin definir — el teaser en el episodio quedó genérico a propósito).
**Blockers:** ninguno.

## Files to Read First

- `btq-production/launch-assets/EP021-simpsons-launch.md` §B2 — calendario + captions de cards.
- `btq-production/pipeline-state-ep021.md` — checkpoint cerrado (stage_c: complete).
- `btq-production/roadmap-btq.md` — para elegir tema de EP.022 (candidatos: Metallica, Matrix,
  Star Wars; toca pilar SEO cada 3–4 episodios pop).

## Notes / Gotchas

- Los formatos 9:16/16:9 de la PORTADA de EP.021 nunca se produjeron (solo 1:1 de Andy +
  cards 16:9). Si los pide, recomposición desde `E:\AI\outputs\ComfyUI_00042_.png`.
- El grid BTQ es DESCENDENTE y el episodio nuevo NO entra al grid (su badge lo cubre) —
  re-verificado en vivo hoy.
- Captions que citan una card: usar el texto renderizado de la card (limpieza aprobada),
  no el SRT — el SRT trae además el typo de WhisperX "calentario".
- Deploy BTQ: `vercel --prod` normal desde `btq-production/website/` (sin ignoreCommand);
  `.vercel/project.json` local existe en esta máquina (desktop).

## Questions to Answer

- ¿Tema de EP.022? (Metallica / Matrix / Star Wars / pilar SEO — pendiente de Andy.)
