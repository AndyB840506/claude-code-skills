# Handoff: BTQ EP.019 Gladiator — Stage B/C completas, episodio CERRADO

**Date:** 2026-06-29
**Status:** Complete — EP.019 publicado y cerrado; sitio actualizado; EP.020 es el siguiente

---

## What We Accomplished This Session

- **Retomó EP.019** desde el handoff anterior (Stage A completo, guion+artwork listos).
  Andy confirmó que ya había grabado el episodio completo.
- **Stage B (post-grabación):**
  - Audio localizado en `E:\Podcast\BTQ\EP 19\BTQ EP 19.wav` (1.07 GB) — hubo confusión
    inicial porque apareció primero suelto en `E:\Podcast\` (raíz) antes de que Andy lo
    moviera a la subcarpeta correcta; resuelto verificando en vivo en vez de asumir.
  - Transcripción con WhisperX (large-v2, diarización) → `E:\Transcriptor\transcripciones\BTQ EP 19.srt`.
  - Assets generados vía `episode-launch`: Spotify SEO, plan social 4 días, YouTube
    (capítulos con timestamps reales del SRT), 4 quote cards — **revalidadas contra el
    audio real**, no contra el guion escrito (hubo variación natural al grabar: "su
    merced" en vez de "usted" en varios tramos).
  - **Encontrado y corregido:** el audio dice "Tim Collins" pero el autor real de
    "Good to Great" es Jim Collins — confirmado con Andy antes de usar el nombre
    correcto en los assets públicos.
  - Spotify URL confirmada por Andy: https://open.spotify.com/episode/0nNg2ngSzEVxKk7awLe5AK
  - Archivo: `btq-production/launch-assets/EP019-gladiator-launch.md`.
- **Stage C (sitio web) — Andy reportó que el tracklist no estaba actualizado:**
  - Encontrado un bug real: el badge "Última pista" (hero, separado del grid de 4
    tarjetas) llevaba atascado en EP.017 desde que se publicó EP.018 (2026-06-22) — el
    workflow de rotación de grid nunca cubrió ese elemento.
  - Corregido en 2 deploys: primero badge → EP.018 (fix retroactivo), luego badge →
    EP.019 + grid rotado a `[018,017,016,015]` (sale EP.014). Ambos deploys verificados
    HTTP 200 en producción (behind-thequeue.com).
  - **Andy decidió CERRAR el episodio sin generar las 7 imágenes nuevas** (portada 1:1,
    teaser 9:16, thumbnail 16:9, 4 quote cards) — decisión definitiva, no parcial. Los
    prompts quedan documentados por si se reutilizan, pero no son pendiente de EP.019.
- **EP.019 cerrado:** `roadmap-btq.md` → `publicado`; `pipeline-state-ep019.md` →
  `stage_c: complete`.
- **Retrospective aplicada:** `episode-launch/workflows/step2-generate-assets.md` ahora
  incluye un paso de fact-check de entidades reales (nombres/fechas citadas) antes de
  publicar assets, no solo verbatim-match contra el audio.
- **Skill audit:** limpio — todos los `SKILL.md` tocados bajo 50 líneas, sin huecos
  estructurales.

## Where We Paused

**Last action:** session-close (retrospective + audit + este handoff).
**Next action:** Ninguna acción técnica pendiente sobre EP.019 — está cerrado. El
siguiente episodio en el roadmap es **EP.020 (pilar SEO — Métricas/KPIs de call
center)**, investigación ya verificada de una sesión previa (Ley de Goodhart/Strathern,
dato SQM "1% FCR ≈ 1% CSAT").
**Blockers:** ninguno.

## Files to Read First

- `btq-production/roadmap-btq.md` — EP.019 publicado, EP.020 es el siguiente (`en roadmap`)
- `btq-production/pipeline-state-ep019.md` — checkpoint final (todo `complete`)
- `btq-production/pipeline-audit-ep019.md` — bitácora completa de las 3 stages
- `episode-pipeline/workflows/04-grid-rotation.md` — ahora documenta el badge "Última
  pista" como elemento separado del grid (el bug que se encontró y corrigió hoy)
- `.claude/skills/episode-launch/workflows/step2-generate-assets.md` — nuevo paso de
  fact-check de entidades reales

## Notes / Gotchas

- **El badge "Última pista" es un elemento del `index.html` SEPARADO del grid de 4
  tarjetas** — cualquier rotación futura de grid (EP.020 en adelante) debe actualizar
  AMBOS, no solo el grid. Ya está documentado en `04-grid-rotation.md`.
- **EP.019 no tiene cover-art/quote cards nuevas** — si en el futuro se pide generar
  imágenes para EP.019 retroactivamente, los prompts siguen disponibles en
  `EP019-gladiator-artwork.md` y `EP019-gladiator-launch.md` §E, pero recordar que Andy
  cerró el episodio sin ellas a propósito.
- **Verbatim ≠ correcto:** las quote cards se validan contra el audio real (no el
  guion), pero eso solo confirma que el texto coincide con lo dicho — no que lo dicho
  sea un dato correcto (caso Jim/Tim Collins). Ahora hay un paso explícito para esto.

## Questions to Answer

- Ninguna pendiente sobre EP.019.
- Al arrancar EP.020: confirmar con Andy si el tema (Métricas/KPIs) sigue siendo el
  mismo o se revisita, y si esta vez sí se generan las imágenes desde el principio.
