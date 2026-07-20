# Handoff: BTQ EP.022 — publicado y verificado, pipeline cerrado

**Date:** 2026-07-20
**Status:** Complete — episodio en vivo, nada pendiente de agente

---

## What We Accomplished This Session

- Retomé desde el handoff de 2026-07-17 (post-transcripción/assets, esperando Spotify).
  Andy confirmó la URL: https://open.spotify.com/episode/6ewMTUO0FGNxfIMS0u55Yu
- Cerré `episode-pipeline` Stage B→C completo para EP.022:
  - **Stage 3 (validación cover-art):** re-leídas las 3 imágenes ya aprobadas, veredicto
    formal PASS 3/3 contra el checklist de `brand-constants.md`.
  - **Stage 3b (quote cards):** 3 cards nuevas (16:9) a partir de los REMATE del guion,
    generadas local (ComfyUI Z-Image Turbo) + texto PIL. 2-3 rondas por el patrón de
    anillo/diana vetado reapareciendo (confirmado que también pasa en generación LOCAL,
    no solo Flow — una vez incluso disfrazado de textura de tela). Calendario de
    publicación agregado al launch file: Mié 22 / Vie 24 / Dom 26-jul.
  - **Stage 4 (grid del sitio):** BTQ rotado de `020,019,018,017` a `021,020,019,018`
    (entra EP.021, sale EP.017); badge "última pista" actualizado a EP.022.
  - **Stage 5 (deploy + verificación):** preflight PASS → gate aprobado por Andy →
    `vercel --prod` → `https://behind-thequeue.com` HTTP 200 (verificado con cache-bust,
    contenido nuevo confirmado, no caché viejo) → EP.22 confirmado en la página pública
    de Spotify (primer lugar del listado).
- Andy confirmó que el plan social ya quedó programado en Meta por fuera del pipeline —
  no hace falta acción de agente ahí.
- Retrospectivo aplicado (4 fixes, ver Notes/Gotchas) y commiteado.

## Where We Paused

**Last action:** retrospectivo pusheado, cerrando el resto de `/session-close`
(skill-kit audit hecho sin hallazgos; falta continuity sync + chequeo de memoria).
**Next action:** ninguna acción de agente pendiente para EP.022 — el episodio está
publicado y verificado. Las 3 quote cards se suben manualmente por Andy los días
Mié 22 / Vie 24 / Dom 26-jul (captions ya listos en el launch file).
**Blockers:** ninguno.

## Files to Read First

- `btq-production/pipeline-state-ep022.md` — `stage_c: complete`, episodio cerrado
- `btq-production/pipeline-audit-ep022.md` — bitácora completa de las 5 stages
- `btq-production/launch-assets/EP022-costo-calidad-launch.md` — calendario de quote
  cards con captions listos para copiar/pegar

## Notes / Gotchas

- **El anillo/diana vetado también aparece en generación LOCAL** (no solo Flow) —
  puede colarse como textura repetida (mini-círculos en una tela), invisible sin zoom.
  Documentado en `episode-launch/docs/brand-constants.md` y `comfyui/docs/troubleshooting.md`.
- **`quote-card-compose.py` (BTQ) ahora expone `compose_quote_card()` importable**
  (igual que los scripts de MPD) — invocar así para citas con tildes, nunca por
  `sys.argv` desde shell (se pierden acentos por escaping silenciosamente).
- **El label "team-slug/proyecto" del output de `vercel --prod` no es evidencia de la
  colisión de proyecto ya conocida** — lo que importa es `project.json` + la línea
  final "Aliased". Documentado en `deploy-preflight/workflows/checks.md`.
- Próximo episodio (EP.023): teaser quedó genérico en el guion de EP.022, tema todavía
  sin definir — ver nota en `pipeline-state-ep022.md`.

## Questions to Answer

Ninguna — episodio cerrado. Cuando Andy quiera arrancar EP.023, el pipeline empieza
desde cero en `episode-pipeline/workflows/00-roadmap.md` (Stage A).
