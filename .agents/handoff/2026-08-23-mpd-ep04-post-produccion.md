# Handoff: MPD EP.04 "Paul is Dead" — Stage B completa, Stage C parcial

**Date:** 2026-08-23 (domingo)
**Machine:** desktop (E:\ existe, RTX 3080 Ti usada para WhisperX)
**Status:** In progress — bloqueado en un solo punto: falta la URL real de Spotify.

---

## What We Accomplished This Session

- **Retomado desde el handoff previo** (`2026-08-20-mpd-ep04-guion-artwork.md`): Andrés
  grabó el episodio. Verificado en disco antes de actuar — `E:\Podcast\MPD\Temporada 2\EP 04\MPD EP 04.mp3/.wav`,
  duración real 31:53 (ffprobe), consistente con el guion de Stage A (~35 min estimados).
- **Transcripción (Stage B.1):** WhisperX large-v2 + diarización, corrido en background
  (proceso detached, PID 2720) — `E:\Transcriptor\transcripciones\MPD EP 04.srt`.
  Verificado sin señales de alucinación (última línea real a 31:35 vs. 31:53 de audio).
- **Assets de Stage B.2 generados y publicados como Artifacts:**
  - Show notes: `episodios/temporada-2/ep04-metadata.md` — https://claude.ai/code/artifact/71ed2f0c-c970-4211-87a9-77cfec74f658
  - YouTube: `episodios/temporada-2/youtube-ep04.md` — https://claude.ai/code/artifact/d08dba07-0dcc-4084-917b-aad172a68e06
  - Plan social: `episodios/temporada-2/social-ep04.md` — https://claude.ai/code/artifact/bb74917a-17a8-4d64-bb97-9474cd4efa1e
  - Todos los timestamps son REALES (del SRT), no las estimaciones de 43 min del guion.
- **Checkpoint de Spotify:** Andrés pegó una URL (`episode/6oddT7be7iK4Ikgh0Hwith`) que
  se verificó con `curl` → 404 real ("Page not found"). Confirmado con Andrés que el
  episodio todavía NO está publicado. Se descartó la URL, `spotify_url` sigue `pending`.
  Publicación planeada: **lunes 2026-08-24** (verificado con `date -d`, no de memoria).
- **Stage 3 — validación de imágenes:** las 3 imágenes finales de Stage A (portada
  1:1/16:9/9:16) se re-leyeron con `Read` y se validaron contra las reglas de marca de
  MPD (sin rostros, sin ocultismo, paleta "La Guarida") — 3/3 PASS, no se regeneraron.
- **Stage 3b — marketing:** 4 quote cards generadas (`comfyui/templates/mpd-quote-card-ep04-t2.py`,
  nuevo archivo) + clip de audio de 48.5s para redes (`social-clip/MPD-EP04-clip-maquinaria.mp3`,
  verificado con `volumedetect`, no silencio). Los 3 assets de marketing (plan/cards/clip)
  quedaron completos.
- **Stage 4 — sitio web: BLOQUEADO a propósito.** MPD usa acumulación de expedientes
  (no rotación de grid). La regla dura es nunca escribir "pending" en un `href`
  publicado — no se tocó `website/index.html`.
- **Retrospectiva aplicada (4 cambios):** resumen de pausa debe listar TODOS los
  pendientes trackeados (no solo el bloqueo — el clip de audio se había registrado en
  la bitácora pero no se comunicó, el usuario tuvo que re-pedirlo); regla de verificar
  el día de la semana real antes de calcular fechas relativas; paleta de quote cards de
  MPD corregida en la doc del pipeline (estaba desactualizada a "silver/crimson"); memoria
  de validación de texto de quote cards ampliada a generación local PIL, no solo Flow.
  Auditoría de skills: 0 colisiones de triggers, todos los `SKILL.md` bajo 50 líneas.

---

## Where We Paused

**Last action:** commit + push de los fixes de retrospectiva (`7fa7adf`).
**Next action:** Andrés publica EP.04 en Spotify (planeado lunes 2026-08-24) y pasa la
URL real. Al recibirla:
1. Actualizar `pipeline-state-ep04.md` (`spotify_url`) y `ep04-metadata.md` §F.
2. Retomar Stage 4 (`episode-pipeline/workflows/04-grid-rotation.md` § MPD): duplicar
   la sección `.case` del expediente anterior en `website/index.html`, cambiar el hero,
   actualizar `#escucha` y el nav.
3. Seguir a Stage 5 (`05-deploy-verify.md`): preflight → deploy → verificar HTTP 200 +
   Spotify.
**Blockers:** `spotify_url` sigue `pending` — es el único bloqueo real, todo lo demás de
Stage B y la mitad de Stage C ya está cerrado.

---

## Files to Read First

- `mrputridsden-production/pipeline-state-ep04.md` — estado exacto por stage
- `mrputridsden-production/pipeline-audit-ep04.md` — bitácora completa, stage por stage
- `episode-pipeline/workflows/04-grid-rotation.md` § "MPD — acumulación de Expedientes" — próximo paso exacto

---

## Notes / Gotchas

- El clip de audio y las 4 quote cards viven en `E:\Podcast\MPD\Temporada 2\EP 04\artwork\`
  (y `\artwork\social-clip\`) — no en el repo, por la regla de assets de producción en `E:\`.
- `comfyui/templates/mpd-quote-card-ep04-t2.py` es nuevo — copiado del patrón real de
  EP.03, NO de la nota desactualizada que tenía `03b-marketing.md` (ya corregida esta sesión).
- El `.file-status` del hero en el sitio (si se despliega con "Disponible el lunes"
  antes de que el episodio esté realmente en vivo) necesita un paso de vuelta explícito
  para cambiarlo a "Ya disponible" — mordió en EP.03, ya anotado en `04-grid-rotation.md`.

---

## Questions to Answer

- Ninguna decisión de contenido pendiente — todo lo de Stage A y B ya se cerró con
  Andrés. Lo único abierto es operativo: la URL real de Spotify.
