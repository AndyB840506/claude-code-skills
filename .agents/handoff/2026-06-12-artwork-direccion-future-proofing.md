# Handoff: Dirección de artwork congelada + future-proofing + lanzamiento EP.004/EP.017
**Date:** 2026-06-12 (viernes)
**Status:** Complete — sesión cerrada; se retoma esta noche post-grabación de MPD EP.004
---
## What We Accomplished This Session
- **Transcriptor operativo en el desktop** (commits previos de hoy): venv WhisperX en
  `E:\Transcriptor\`, validado con 2 audios reales (~2 min/episodio en la 3080 Ti),
  HF_TOKEN/HF_HOME/TORCH_HOME persistidos como env vars de usuario.
- **EP.004 Kraken listo para grabar HOY en la noche** (live sáb 13 medianoche): guion con
  pasada anti-repetición v4.1 + paquete de publicación para Juan
  (`mrputridsden-production/episodios/entrega-juan-ep004.md`) con calendario corregido
  (Intriga vie 12 → Lanzamiento sáb 13 → Quote dom 14).
- **Dirección de artwork CONGELADA por show, validada con generaciones reales:**
  - BTQ = póster gráfico editorial, siluetas a contraluz sobre dorado — bloques verbatim
    en `episode-launch/docs/brand-constants.md`. Portada EP.017 generada y APROBADA.
  - MPD = fotograma cinematográfico 80s/35mm crimson+dorado, nunca rostros — bloques en
    `podcast-creator/workflows/03-artwork.md`. Portada v2 EP.004 aprobada como prompt.
  - Regla compartida: tipografía exacta letra por letra, máx ~5 palabras/línea, tildes
    fuera del texto en imagen (van al caption).
- **Teasers listos para Flow:** MPD T1/T2 en `mrputridsden-production/episodios/artwork-ep004.md`;
  BTQ intriga + lanzamiento en `btq-production/launch-assets/EP017-cerati-artwork.md`.
- **Future-proofing Fable→Opus 4.8** (deadline plan: 22-jun): `docs/estandar-de-entregables.md`
  (calidad verificable por entregable), `docs/roadmap-future-proofing.md` (3 sesiones 15-19 jun,
  incluye re-evaluación de graphify), regla de transición de modelo en CLAUDE.md del proyecto.
- **Retrospectiva aplicada:** regla "referente en escena, no implícito" agregada a la
  dirección BTQ (feedback "simplón"); CLAUDE.md ahora referencia `/session-close`.

## Where We Paused
**Last action:** audit del kit (limpio salvo 4 SKILL.md marginalmente >50 líneas, diferidos)
y este handoff.
**Next action (esta noche, post-grabación):** copiar el audio de EP.004 a
`E:\Transcriptor\audios\` y correr el transcriptor (comando en
`transcriptor/docs/environment.md`). Con el SRT: (1) confirmar la quote del Día 3
("la materia prima") contra el audio — si cambió, ajustar entrega-juan-ep004.md Y el
prompt T2 antes de generarla; (2) elegir clip 30-60 seg para Reel (candidatos: cartas
de Noruega o Batalla de las Bandas).
**Blockers:** ninguno técnico. Dependen de Andrés: generar en Flow HOY la portada Kraken 1:1
y la Teaser T1 (Juan publica la intriga hoy); grabación esta noche.

## Files to Read First
- `.agents/handoff/2026-06-12-artwork-direccion-future-proofing.md` — este archivo
- `mrputridsden-production/episodios/entrega-juan-ep004.md` — calendario y copy de Juan
- `mrputridsden-production/episodios/artwork-ep004.md` — portada v2 + T1/T2 (prompts Flow)
- `btq-production/launch-assets/EP017-cerati-artwork.md` — portada aprobada + teasers EP.017
- `docs/roadmap-future-proofing.md` — plan de sesiones 15-19 jun

## Notes / Gotchas
- **Pregunta al retomar:** ¿cuáles next steps ya se completaron? (¿se generaron las imágenes?,
  ¿se grabó?, ¿Juan publicó la intriga?) No asumir pendientes.
- SRTs del transcriptor usan numeración SIN cero-padding (`MPD 3.srt`, no `EP.003`).
- En EP.017 (graba sáb 13, live dom 14 8PM): verificar lista de invitados de la gira
  "Gracias Totales" 2020 (¿artistas colombianos?) ANTES de nombrarlos al aire; el refrán
  del guion se repite ~6x — variar wording en la entrega.
- Audit pendiente para la sesión 15-19: recortar SKILL.md de parallel-workflow (58),
  project-map (56), episode-pipeline (55), megamind (51) a <50 líneas.
- Commits de hoy sin comillas dobles dentro del here-string de PS 5.1 (rompe el mensaje).

## Questions to Answer
- ¿La quote del Día 3 salió igual en la grabación? (decide el texto de la Teaser T2)
- ¿Cuándo agendar las 3 sesiones de future-proofing dentro del 15-19 jun?
- EP.018 El Mundial: arrancar producción la próxima semana con el formato nuevo (sirve
  de dry-run para Opus 4.8).
