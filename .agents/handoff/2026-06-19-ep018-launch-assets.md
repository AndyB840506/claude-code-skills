# Handoff: EP.018 BTQ (El Mundial) — pipeline hasta Stage 3b (assets + portadas + quote cards)

**Date:** 2026-06-19
**Status:** In progress — episode-pipeline corrido de punta hasta Stage 3b. Intake + transcripción + assets + 3 portadas validadas (3/3 PASS) + 4 quote cards generadas y commiteadas. **Bloqueado hasta dom 21-jun:** falta publicar en Spotify y traer la URL en vivo para correr Stage 4 (grid) y Stage 5 (deploy).

---

## NEXT STEP principal (dirección de Andy)

**Esperar al domingo 21-jun 8:00 PM (hora Colombia) para publicar el EP.018 en Spotify.** Cuando esté publicado:
1. Andy pega la **URL en vivo de Spotify** (verificada en el browser — ojo regla EP.016: si hubo re-upload, la URL puede cambiar).
2. Con esa URL se actualiza `pipeline-state-ep018.md` → `stage_b: complete, spotify_url: [URL]` y se corre **Stage 4 (rotación del grid de la web)** y **Stage 5 (deploy + verificación HTTP 200 + Spotify)**.
3. En paralelo / cuando pueda: Andy **genera las 4 quote cards en Flow** (prompts §E del launch file) y pasa las rutas (revisión visual rápida, no requieren subagent).

Al retomar, el checkpoint `pipeline-state-ep018.md` dice `stage_b: complete, spotify_url: pending` → el Paso 0 de `00-intake.md` se detendrá ahí pidiendo la URL (comportamiento correcto, igual que EP.16).

---

## What We Accomplished This Session

- **Pipeline EP.018 ejecutado desde "acabo de grabar" hasta Stage 3b.** Episodio de 1 sola parte.
- **Stage 0 — Intake:** audio consolidado en `E:\Podcast\BTQ\EP 18\BTQ EP 18.wav` (923.7 MB). La grabadora dejó ~130 clips sueltos (`02-My Vocal-*`); Andy los unió en el .wav. Checkpoint + bitácora creados.
- **Stage 1 — Transcripción:** WhisperX (large-v2, es, diarize) → `E:\Transcriptor\transcripciones\BTQ EP 18.srt` (70.2 KB, sin alucinaciones, marcadores `[ACTUALIZAR AL GRABAR]` del Mundial resueltos al grabar: 3-1, 48 selecciones, 3 países).
- **Stage 2 — Assets (episode-launch):** `btq-production/launch-assets/EP018-mundial-launch.md` — Spotify SEO (título `EP.18 — El Mundial: liderazgo cuando no puedes tocar el balón`, preview, desc HTML+texto, tags), plan social 4 días (intriga vie 19/sáb 20, **launch dom 21 8PM**, pico lun 22, refuerzo mar 23), YouTube (título + desc 5 bloques + 17 capítulos con timestamps REALES del SRT + 20 tags + thumbnail), 3 prompts de portada. Gate aprobado por Andy.
- **Stage 3 — Portadas validadas 3/3 PASS:** generadas en Flow, en `E:\Podcast\BTQ\EP 18\BTQ EP 18 Artwork\` (1:1 ...2131.jpeg / 9:16 ...2132.jpeg / 16:9 ...2132 (1).jpeg). Validadas leyéndolas directo (1 figura, cero caras, texto letra por letra sin tildes, footer EP.018, regla de margen).
- **Fix pedido por Andy:** la portada debía llevar el **título del episodio** (`EL MUNDIAL` / `LIDERAZGO SIN TOCAR EL BALON`), que los prompts iniciales del 1:1 y 9:16 omitieron (solo footer). Corregido antes de generar.
- **Stage 3b — 4 quote cards** (§E del launch file): Q1 preparar/Bielsa, Q2 Obdulio/pulso, Q3 Zander/ojos, Q4 cierre/tesis (16:9 split-scene, derivables a 1:1/9:16). Plan social ya venía del Stage 2, no se regeneró.
- **Retrospective aplicada (3 reglas, aprobadas por Andy):**
  - `episode-pipeline/workflows/00-intake.md`: auto-descubrir audio BTQ ahora prioriza `E:\Podcast\BTQ\EP NN\BTQ EP NN.wav` (subcarpeta + wav); los clips `02-My Vocal-*` no son el audio.
  - `.claude/skills/episode-launch/workflows/step2-generate-assets.md` §D: regla obligatoria de que la portada 1:1 y 9:16 lleven el título del episodio (referente gold + tagline con keyword); 16:9 usa hook de thumbnail.
  - `episode-pipeline/workflows/03-image-validation.md`: validar inline con `Read` es el default; spawnear subagent solo es opcional.
- **Audit de skills:** limpio (SKILL.md ≤50 líneas, sin sueltos, sin corrupción).
- **Commits:** `1c2f2a3` (Stage B), `801ac1a` (portadas + quote cards + fix título), `053ba8e` (retrospective).

## Where We Paused

**Last action:** session-close (retrospective aplicada y commiteada → audit limpio → este handoff).
**Next action:** esperar la publicación en Spotify del domingo y la URL en vivo; luego Stage 4 + Stage 5.
**Blockers:** la URL de Spotify (sale dom 21-jun 8PM) bloquea Stage 4 y 5. Las 4 quote cards faltan de generar en Flow (no bloqueante para nada más).

## Files to Read First

- `btq-production/pipeline-state-ep018.md` — checkpoint (`stage_b: complete, spotify_url: pending`)
- `btq-production/launch-assets/EP018-mundial-launch.md` — todos los assets (Spotify, social, YouTube, §D portadas, §E quote cards)
- `btq-production/pipeline-audit-ep018.md` — bitácora stage por stage
- `episode-pipeline/workflows/04-grid-rotation.md` y `05-deploy-verify.md` — lo que sigue al tener la URL

## Notes / Gotchas

- **EP.018 = 1 solo episodio** (adquisición + ventana cultural Mundial 2026).
- **Calendario:** grabó viernes 19-jun (no sábado); launch domingo 21-jun 8PM. El plan social ya está fechado con esto.
- **143 wpm sigue siendo el número de oro de BTQ** (de la sesión del guion). El episodio salió ~60 min según el SRT.
- **Placeholders intencionales** en el launch file: `[URL SPOTIFY EP.018]` en §B (primer comentario) y §C (YouTube) — se rellenan al publicar. NO son TODOs de código.
- **Audio BTQ cambió de ubicación** respecto a episodios viejos: ahora `E:\Podcast\BTQ\EP NN\BTQ EP NN.wav`. Ya quedó en el workflow de intake.
- EP.005 MPD sigue sin grabar (de handoffs anteriores). EP.017 grabado — verificar si ya está en Spotify.

## Questions to Answer (al retomar)

- ¿Alguno de los next steps ya se hizo? (preguntar antes de asumir)
- ¿Ya se publicó el EP.018 en Spotify? ¿URL en vivo (verificada en browser)?
- ¿Andy ya generó las 4 quote cards en Flow? ¿Rutas?
- ¿Se corre ya Stage 4 (grid) + Stage 5 (deploy)?
- ¿EP.018 pasa a "en Spotify" en el roadmap-btq?
