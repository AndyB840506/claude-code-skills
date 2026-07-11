# Handoff: BTQ EP.021 — Stage B completa + Stage C 3/5; pipeline de artwork local institucionalizado

**Date:** 2026-07-11
**Status:** In progress — esperando URL de Spotify (Andy la pasa "mañana cuando esté live"); todo lo demás de C.3/C.3b cerrado.

---

## What We Accomplished This Session

- **Stage B completa (commit `2cd86fe`):** audio confirmado (`E:\Podcast\BTQ\EP 21\BTQ EP 21.mp3`),
  transcripción WhisperX con diarización (`E:\Transcriptor\transcripciones\BTQ EP 21.srt`, ~41:10),
  fact-check de entidades reales vs fuentes del guion (sin errores), y launch assets completos vía
  `episode-launch`: Spotify SEO (descripción 310 palabras contadas programáticamente + versión HTML),
  plan social 4 días (calendario corrido: grabó viernes, lanza domingo 12 · 8PM), YouTube con 14
  capítulos de timestamps reales del SRT, prompts de artwork. Artifact publicado:
  https://claude.ai/code/artifact/f7ef9139-41a8-484a-b82d-51a41d1561fe
- **Regla nueva de marca (Andy, en el gate):** aros/círculos concéntricos VETADOS en TODAS las
  imágenes BTQ (portadas Y quote cards; antes "reservado para portada"). Aplicado en
  `brand-constants.md` §Reglas #3, checklist, §Quote Cards, §Patrones de Flow + memoria.
- **Saga del artwork (la parte larga):** Flow rechazó los prompts por copyright → se movió todo a
  ComfyUI local. Iteraciones documentadas en `pipeline-audit-ep021.md`: composición Pillow rechazada
  ("figura flotando en negro"), conversiones img2img "super picasso" (identidad descrita de memoria),
  diagnóstico raíz = trampa de la negación de Z-Image Turbo (a CFG 1 el negativo no actúa; "DO NOT
  render X" evoca X; pedir "test-card geometry" garantiza círculos). **Portada oficial: la que generó
  Andy en la UI de ComfyUI (`E:\AI\outputs\ComfyUI_00042_.png`, 3D dorada)** — la 2D con shading
  (BTQ-EP021-1x1-2D_00004) quedó como candidata descartada por él.
- **3 quote cards finales en 16:9** (formato nuevo por decisión de Andy) en
  `E:\Podcast\BTQ\EP 21\BTQ Artwork EP 21\BTQ-EP021-CARD{1,2,3}-16x9.png`: escenas ComfyUI
  (micrófono/CRT estática/vela+standby) + texto PIL determinista, citas verbatim validadas contra el
  SRT (~05:09, ~24:10, ~39:20). Descartes en subcarpeta `descartes\`.
- **Proceso institucionalizado para BTQ/MPD/CCC (pedido explícito de Andy, commit `0a6e220`):**
  generación local primaria en `03-image-validation.md` Paso 1 y `03b-marketing.md` Paso 2 (Flow =
  fallback), lecciones técnicas en `comfyui/docs/prompting.md` (negación, SetLatentNoiseMask,
  proporciones canon, flat-in-flat-out), plantilla API en `comfyui/templates/zimage-txt2img-api.json`,
  metadata-PNG tip en `stack-reference.md`, `pause-points.md` #6 actualizado (generación ya no es
  pausa estructural). Memorias: `feedback_local_artwork_pipeline`, `feedback_polish_is_a_set`,
  `feedback_design_references` generalizada a likeness.
- Checkpoint `pipeline-state-ep021.md`: `stage_b: complete`, Stage C 3/5, `spotify_url: pending`
  (commit `75d8334`).

## Where We Paused

**Last action:** cierre de sesión (retrospectiva 6/6 aplicada, audit del kit con 1 fix, este handoff;
sigue continuity sync + memory-audit check).
**Next action:** Andy publica EP.021 en Spotify (metadata lista en el artifact §A — pegar la versión
HTML) y pasa la URL. Con ella: `00-intake.md` Paso 0 detecta el estado → rotación de grid
(`04-grid-rotation.md`: hero → EP.021, tracklist BTQ DESCENDENTE `020,019,018,017`) → deploy-preflight
→ gate → `vercel --prod` desde `btq-production/website/` → verificar HTTP 200 + Spotify.
**Blockers:** solo la URL de Spotify. Lanzamiento oficial: domingo 13 de julio, 8PM Colombia (el plan
social del artifact ya trae el calendario corrido).

## Files to Read First

- `btq-production/pipeline-state-ep021.md` — checkpoint exacto.
- `btq-production/pipeline-audit-ep021.md` — bitácora completa (incluye toda la saga del artwork).
- `btq-production/launch-assets/EP021-simpsons-launch.md` — metadata de Spotify/YouTube/social lista.
- `episode-pipeline/workflows/03-image-validation.md` + `03b-marketing.md` — el proceso local nuevo.

## Notes / Gotchas

- **Portada oficial = la de Andy** (`ComfyUI_00042_.png`), no las candidatas mías. Tiene un typo
  conocido en el footer ("Behind the Queee") — existe versión parcheada+upscaled en
  `E:\AI\outputs\BTQ-EP021-1x1-FINAL-3000.png` (typo corregido, 3000×3000) por si la quiere para
  Spotify; confirmar con él cuál sube, no asumir.
- Los formatos 9:16 y 16:9 de la PORTADA no se produjeron (Andy saltó a quote cards) — si los pide,
  recomposición desde su portada oficial o regeneración con la receta 2D/3D limpia.
- El servidor ComfyUI corre como background task de la sesión — muere al cerrar Claude Code;
  relanzar con el comando de `stack-reference.md` §Launch.
- Z-Image Turbo: TODO el control va en el prompt positivo (CFG 1 apaga el negativo) — leer
  `comfyui/docs/prompting.md` antes de escribir cualquier prompt de imagen.
- La memoria NO viaja en este repo — el continuity sync del cierre es lo que la respalda.

## Questions to Answer

- ¿URL de Spotify de EP.021? (bloqueante de C.4/C.5)
- ¿Cuál portada sube a Spotify: su original con typo o la versión parcheada 3000×3000?
- ¿Quiere producir 9:16/16:9 de la portada para stories/YouTube antes del domingo?
