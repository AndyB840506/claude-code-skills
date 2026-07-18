# Handoff: MPD — Juan sale del proyecto, EP.005 solo grabado y listo para publicar
**Date:** 2026-07-17 (viernes)
**Status:** Complete — EP.005 programado para publicar la noche del sábado 2026-07-18

---

## What We Accomplished This Session

**Cambio de formato — Juan dejó Mr. Putrid's Den (2026-07-17):**
- Andrés continúa solo desde EP.005 en adelante. Actualizado en `podcast-profile.json`,
  `CLAUDE.md`, `SKILL.md`, `glosario-cachaco.md`, `eventos.json` (deprecado), y sitio web
  (`mrputridsden-production/website/index.html` — Juan removido de meta/schema/hero/EL SHOW,
  descripciones históricas de EP.001/EP.003 quedaron intactas porque son ciertas).
- Segmento de Promoción (eventos underground) **retirado, no reasignado** — dependía del
  conocimiento insider de Juan como promotor.
- Default de 2 partes **retirado** (memoria `project_mpd_episodes_two_parts`, RETIRED) — nuevo
  target: episodio único ~43 min.
- Contacto `Juan@mrputridsden.com` marcado inactivo, no borrado (registro histórico).

**EP.005 (Aterciopelados) reescrito, grabado, transcrito, calibrado:**
- Guion co-host original (P1+P2, ~90 min) descartado (recuperable vía git history), reescrito
  el mismo día como episodio único solo — 4.616 palabras, `mrputridsden-production/scripts/EP005-aterciopelados.html`.
- Grabado el mismo día: `E:\Podcast\MPD\EP 05\MPD EP 05.mp3`.
- Transcrito vía `transcriptor` (WhisperX, sin diarización — un solo host) →
  `E:\Transcriptor\transcripciones\MPD EP 05.srt`.
- **Calibración real reemplaza la fórmula prestada de BTQ:** Andrés habla a 159 wpm en MPD
  (vs 150 en BTQ) pero expande solo +23.5% en vivo (vs +35.5% de BTQ) → duración real ~35.8 min
  de habla, corta vs el target de 43 min. Nuevo archivo `mrputridsden-production/guion-style-mpd.md`
  (mismo patrón que `guion-style-btq.md`) con la tabla completa. `podcast-profile.json`
  `word_count_target` corregido a 5543 palabras para EP.006 en adelante.
- **Decisión de Andrés:** EP.005 se publica AS-IS, sin padding, pese a salir corto.

**Show notes / metadata:** `mrputridsden-production/episodios/ep005-metadata.md` — título,
descripción (plano + HTML Spotify), keywords SEO, capítulos con timestamps reales del SRT.
Título alineado con el tagline del artwork ("De un bar de Bogotá al continente.") tras detectar
que la primera versión usaba el tagline del guion en su lugar — corregido en esta sesión.

**Artwork — primera vez que MPD usa el pipeline local (ComfyUI + PIL), antes solo BTQ/CCC:**
- Portada 1:1 (3000×3000 print + JPEG q85/477KB para upload), 16:9, 9:16, y 4 quote cards
  generados en `E:\Podcast\MPD\EP 05\artwork-local\`.
- Herramientas nuevas reusables: `comfyui/templates/mpd-portada-compose.py` y
  `mpd-quote-card-compose.py` (footer con flor + iconos de plataforma, importables como función
  para evitar pérdida de tildes al pasar argumentos por shell).
- Icon strip del footer reutilizado (recortado) del de BTQ EP.022 — mismos iconos reales.
- Q3 cambió de concepto: de "la voz" (un solo cantante, mostró detalle facial no deseado en 2
  intentos) a un dúo Cerati/Andrea cantando juntos evocando el Unplugged 1996 — nueva cita:
  "Una canción secreta, escrita para Cerati — nadie lo supo hasta que él murió."
- Prompts originales de Flow (2026-06-17, pre-cambio de formato) documentados como referencia
  histórica en `artwork-ep005.md`, ya no vigentes.

**Retrospectiva aplicada (5 learnings):**
1. `episode-pipeline/workflows/02-assets.md` — chequeo de consistencia título/tagline entre
   guion/metadata/artwork antes de cerrar Stage B (el gap que causó la corrección de arriba).
2. `comfyui/docs/prompting.md` — segunda instancia confirmada de la trampa de la negación en
   rasgos faciales (describir ángulo de luz, no negar anatomía).
3. `comfyui/docs/prompting.md` — consistencia visual de un sujeto recurrente a través de varias
   generaciones (el pelo de Andrea cambió entre portada y quote card hasta corregirlo).
4. `comfyui/docs/prompting.md` — reusar íconos/logos reales entre shows antes de regenerar.
5. `comfyui/docs/stack-reference.md` — compose scripts con texto acentuado deben exponer una
   función importable, no depender de `sys.argv`.

## Where We Paused

**Last action:** Handoff (este archivo) tras confirmar que EP.005 está programado para publicar
la noche del sábado 2026-07-18.
**Next action:** Cuando el episodio esté en Spotify, agregar la URL real al placeholder
`[PENDIENTE]` en `ep005-metadata.md` y actualizar `roadmap-mpd.md` a "en Spotify"/"publicado".
**Blockers:** Ninguno técnico — solo falta la URL de Spotify, que llega al publicar.

## Files to Read First

- `mrputridsden-production/roadmap-mpd.md` — estado completo de EP.005 y las notas de contexto de todo el cambio de formato.
- `mrputridsden-production/guion-style-mpd.md` — calibración real de duración, usar para EP.006.
- Memoria: `project_mpd_juan_departure` (estado completo del cambio de formato), `reference_mpd_guion_style`.

## Notes / Gotchas

- **EP.005 quedó corto (~35.8 min vs 43 min target) — decisión ya tomada de publicarlo as-is.**
  No hace falta volver a tocar esto; el próximo guion (EP.006) ya usa el target corregido.
- Las imágenes viejas de artwork en `E:\Podcast\MPD\EP 05\` (jpeg fechados 2026-06-17) son
  pre-cambio de formato — los assets vigentes están en la subcarpeta `artwork-local\`.
- `roadmap-mpd.md` todavía dice "Aterciopelados: una gomela, un punkero" en la columna de título
  de la tabla (no se tocó — el usuario solo pidió alinear la metadata, no el roadmap). Si se
  quiere consistencia total, falta ese ajuste.

## Questions to Answer

- **NEEDS USER INPUT** (`EP005-aterciopelados.html`, nota de producción): ¿se menciona el paso a
  formato solo (salida de Juan) en el episodio al aire, o solo en show notes? Ni el guion ni la
  metadata lo mencionan todavía — decisión pendiente de Andrés, no decidida unilateralmente.
- Reemplazo para el segmento de eventos underground / booking de invitados de EP.008 — sin
  fuente definida todavía (Juan cubría ambos como promotor).
- Qué tema toma EP.009 ahora que su pillar original ("Spotlight: eventos underground") fue
  retirado junto con el segmento de promoción.
