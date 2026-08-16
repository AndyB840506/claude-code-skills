# Handoff: MPD EP.03 — post-producción completa, en espera del lunes

**Date:** 2026-08-15
**Machine:** desktop (E:\ existe, verificado; ComfyUI corrió esta sesión — confirmar si sigue arriba antes de asumir su estado)
**Status:** Complete — episodio grabado, todos los assets listos, sitio desplegado. Solo falta que Spotify publique el episodio el lunes.

---

## What We Accomplished This Session

**1. Transcripción con un hallazgo real de producción:**
- Audio grabado en `E:\Podcast\MPD\Temporada 2\EP 03\` transcrito con WhisperX (large-v2, es, diarize).
- **Bug encontrado:** el máster original (50:28) tenía 18 min de música de fondo sin recortar al final (bug de export en Reaper) — el SRT mostraba diálogo real hasta 32:45 y después solo boilerplate alucinado por WhisperX. Detectado cruzando el timestamp final del SRT contra `ffprobe` + confirmado con `volumedetect` (no era silencio, -25dB mean). Andrés lo corrigió en Reaper y regeneró el export (33:01.8, limpio) — se re-transcribió sobre el archivo nuevo.
- **Duración real del episodio: 32:45** — bastante corto vs el target de ~43 min. Mismo patrón que EP.005 (se publica as-is, sin regrabar ni rellenar).

**2. Cerrados los 3 bloques `.verificar` del guion** (Sgt. Pepper's "+70 figuras", Batalla de Blythe Road, Bowie en LA 1975-76) con fuentes cruzadas (WebFetch + WebSearch) antes de escribir la metadata pública — los 3 se confirmaron. Editado directamente en `scripts/EP03-la-bestia-que-el-rock-volvio-inmortal.html`.

**3. Assets generados** (todos en `episodios/temporada-2/`, publicados como Artifacts):
- `ep03-metadata.md` — show notes/Spotify (título 44/80 chars, descripción corta 124/150)
- `youtube-ep03.md` — título 45/60, 7 capítulos verificados contra el SRT real (3 reglas duras de YouTube OK)
- `social-ep03.md` — plan 3 días (Día 1 sábado 15, Día 3 lanzamiento lunes 17 00:00)

**4. Artwork producción final + quote cards** (en `E:\Podcast\MPD\Temporada 2\EP 03\artwork\`):
- Escena regenerada a 1536×1536 (mismo prompt/seed 3082026 del concepto v3 aprobado en Stage A) → upscale 3000×3000 (RealESRGAN) → `night_grade` variante E → compuesta con `comfyui/templates/mpd-portada-ep03-t2.py` (nuevo) + `mpd-quote-card-ep03-t2.py` (nuevo, 4 quotes verbatim del SRT).
- **Intento de usar el mood que Andrés prefería visualmente** (librero + candelabro, `MPD-T2E03-validation_00001_.png` de Stage A) **descartado**: tenía el patrón de diana vetado en un vinilo y la cara salía demasiado legible/reconocible. 2 rondas de corrección de prompt no lo resolvieron (empeoró cada vez). Se siguió con la composición simétrica, que cumplía las reglas desde el primer render.
- **2 bugs reales de composición** heredados del script de EP.02, encontrados por inspección visual y corregidos: wordmark superpuesto sobre el marco en 16:9 (`y_center` de crop mal calibrado para esta escena), título cortado en 9:16 (piso del auto-fit de fuente muy alto para un título más largo que el de EP.02). Detalle completo en `pipeline-audit-ep03.md` Stage 3.

**5. Sitio web + deploy:**
- Sección `.case` completa para Expediente 03 agregada a `website/index.html` (patrón de acumulación de MPD, no rotación) — hero, embed de "Sintoniza" y portada web (`ep03-cover.jpg`, 760×760) actualizados.
- Deploy-preflight corrido limpio (proyecto correcto, sin secrets, baseline 200). Deploy prebuilt a producción (`vercel deploy --prebuilt --prod` + `vercel alias set`) — verificado en vivo: `curl` 200, contenido nuevo confirmado.
- **Consultado con Andrés antes de deployar** (el episodio no está en vivo en Spotify hasta el lunes) — confirmó desplegar igual.

**6. Spotify:** Andrés pegó la URL real: `https://open.spotify.com/episode/4CC5CsJPY75Wyg5Yd5RR6O?si=rWV9VInqRLOh84qBIS4nuQ` — **programado para publicarse el lunes 2026-08-17 a las 00:00, NO está en vivo todavía**. Guardado así explícitamente en `pipeline-state-ep03.md` y `roadmap-mpd.md` para que la próxima sesión no lo trate como ya verificable.

**7. Retrospectiva aplicada** (3 fixes, ver commit de skills):
1. `~/.claude/skills/CLAUDE.md` § Windows — shell: `Start-Job` no sobrevive entre llamadas separadas de la tool; usar `Start-Process -PassThru` + `Wait-Process` en llamada aparte.
2. `~/.claude/skills/CLAUDE.md` § Instrumentos que mienten en silencio: WhisperX alucina boilerplate sobre música/silencio en vez de dejar el SRT vacío — comparar timestamp final del SRT vs `ffprobe` duration, verificar con `volumedetect`.
3. `comfyui/docs/artwork-composition.md`: copiar el compositor de un episodio anterior trae `y_center`/piso de auto-fit calibrados a ESA escena/título — verificar visualmente los 3 formatos, no solo 1:1.

**Auditoría de skills:** limpia — ningún `SKILL.md` tocado esta sesión, solo 2 templates nuevos en `comfyui/templates/` y notas en `docs/` existentes.

---

## Where We Paused

**Last action:** retrospectiva aplicada, handoff en curso.
**Next action:** ninguna acción nuestra pendiente — **esperar al lunes 2026-08-17 00:00** y verificar que el episodio quedó realmente en vivo en Spotify (`curl` o abrir el link), luego confirmar que el sitio (ya desplegado) y el embed de "Sintoniza" cargan bien contra el episodio real.
**Blockers:** ninguno de nuestro lado — depende de que Spotify libere el episodio en la fecha programada.

---

## Files to Read First

- `mrputridsden-production/pipeline-state-ep03.md` — checkpoint actual (`stage_c: in_progress`, spotify_url programado)
- `mrputridsden-production/pipeline-audit-ep03.md` — bitácora completa de Stage B/C, incluye el bug de audio y los 2 bugs de artwork
- `mrputridsden-production/roadmap-mpd.md` — fila de EP.03 actualizada

---

## Notes / Gotchas

- **El máster viejo con la cola de música (`MPD EP 03.wav`/`.mp3` versión de 50:28) fue SOBREESCRITO por el re-export limpio de Andrés** — no existe más en disco, no hay que limpiarlo.
- **ComfyUI local quedó corriendo al final de esta sesión** (no se cerró explícitamente, a diferencia del cierre habitual). Si la próxima sesión necesita generar algo, verificar con `curl 127.0.0.1:8188/system_stats` antes de asumir que hay que levantarlo de nuevo.
- **YouTube metadata de EP.03 está lista pero el canal de MPD todavía no existe** (`status: pendiente` en `podcast-profile.json`) — no accionable todavía, ya anotado en el propio `youtube-ep03.md`.
- **No verificar el embed de Spotify ni el link del sitio como "funcionando" antes del lunes 00:00** — va a fallar/mostrar error hasta esa fecha por diseño, no es un bug a arreglar.

---

## Questions to Answer

Ninguna abierta — todo lo que dependía de una decisión de Andrés (timing del deploy, audio de la cola, composición del artwork) se resolvió en esta sesión.
