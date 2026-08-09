# Handoff: MPD EP.02 (T2·E2) — pipeline cerrado por completo, retrospectiva aplicada

**Date:** 2026-08-09 (domingo)
**Machine:** desktop (E:\ existe, verificado; audio máster y artwork en E:\)
**Status:** Complete — no queda ningún pendiente conocido para EP.02

---

## What We Accomplished This Session

**Retomado desde el handoff del 08-06** (que había quedado parado en `stage_c: blocked_on_live`,
esperando el sábado 2026-08-08). Verificado con WebFetch (dos veces, episodio directo + página
del show) que EP.02 sí está en vivo en Spotify desde el 08-08.

**Sitio de MPD reparado (hallazgo real, no solo retomar el handoff):**
- `mrputridsden.com` nunca se había actualizado tras publicar EP.006 el 08-01 — seguía en
  "Expediente 01 · En producción" con el embed apuntando a EP.005 (T1).
- El workflow `episode-pipeline/workflows/04-grid-rotation.md` asume un markup
  `.episodes-grid`/`.episode-card` que el rediseño "La Guarida" (commit `8b9a4a8`, 2026-07-22) ya
  había reemplazado — no aplicaba tal cual, así que el fix real fue manual: Expediente 01 pasado a
  publicado (portada propia `ep01-cover.jpg`, link real a Spotify), Expediente 02 agregado como
  sección nueva (portada `ep02-cover.jpg`), hero destacando el más reciente, embed de Sintoniza
  actualizado.
- Deploy vía flujo prebuilt de Vercel (`ignoreCommand: exit 0`) + `vercel alias set` (obligatorio,
  `--prod` no realiasa el dominio custom) → verificado HTTP 200 + contenido nuevo en vivo.

**Quote cards generadas (Stage 3b había quedado sin correr):**
- El workflow `03b-marketing.md` Paso 2 nunca se ejecutó para EP.02 en la sesión del 08-06 — saltó
  directo del plan social a la corrección de numeración. EP.006 sí tuvo 4 quote cards verbatim;
  EP.02 tenía cero.
- Nuevo compositor `comfyui/templates/mpd-quote-card-ep02-t2.py` (copiado/adaptado de
  `mpd-quote-card-t2.py`, escena y paleta desde `mpd-portada-ep02-t2.py`).
- 4 cards generadas, verbatim contra el SRT real, verificadas visualmente (legibles, tildes OK,
  sin motivos vetados).

**Clip de audio extraído (con un bug de ffmpeg real encontrado y corregido):**
- 59.6s del juicio de Nevada (33:39–34:38), extraído directo del máster `.wav` con ffmpeg.
- El primer intento exportó **silencio total** pese a duración y bitrate correctos — el filtro
  `afade` medía su tiempo contra la línea de la línea de tiempo del archivo COMPLETO (39 min), no
  del clip recortado, porque `-ss`/`-to` estaban DESPUÉS de `-i`. Detectado con
  `ffmpeg -af volumedetect`, no por inspección de metadata. Documentado en
  `~/.claude/CLAUDE.md` § "Instrumentos que mienten en silencio" para no repetirlo en BTQ/CCC.

**Reorganización de archivos (a pedido explícito del usuario):**
- `episodios/` mezclaba T1 (EP.001-005) con archivos sueltos de T2 fuera de convención.
- Creado `episodios/temporada-2/` — movidos ahí `ep02-metadata.md`, `youtube-ep02.md`,
  `social-ep02.md` (renombrados desde `shownotes-ep02.md`/`youtube-ep02.md`/`social-ep02.md` en
  la raíz) y también `ep006-metadata.md`, `social-ep006.md`, `youtube-ep006.md` (que ya seguían el
  patrón pero vivían sueltos en `episodios/`, mezclados con T1).
- Handoffs históricos que citan las rutas viejas de EP.006 **NO se reescribieron** — narran el
  estado a esa fecha.

**Retrospectiva aplicada (3 fixes, ver commit `6cd89b0`):**
1. `feedback_short_approval_asks.md` — corolario: una pregunta = una decisión independiente. No
   empaquetar dos assets distintos en un solo sí/no.
2. `feedback_always_show_image_paths.md` — corolario: con 2+ assets en un mismo cierre, cada ruta
   en su propia línea, no enterrada en prosa.
3. `podcast-creator/workflows/04-social-media.md`, `05-show-notes.md`, `07-youtube.md`,
   `06-html-export.md` — especifican `episodios/` como destino explícito (antes decían "el
   directorio actual", causa raíz de por qué EP.02 quedó desordenado). De paso se corrigió que el
   commit anterior de reorganización no había completado el borrado de los archivos viejos en la
   raíz (quedaban eliminados solo localmente, no commiteados).

**Auditoría de skills:** limpia — 28 skills, 0 colisiones de triggers, 0 `SKILL.md` sobre 50
líneas, sin archivos sueltos.

---

## Where We Paused

**Last action:** retrospectiva aplicada y pusheada (commit `6cd89b0`).
**Next action:** ninguna acción pendiente conocida sobre EP.02. Próximo trabajo natural de MPD:
Expediente 03 (Crowley y su huella musical más allá de Zeppelin, ver `banco-expedientes.md`).
**Blockers:** ninguno.

---

## Files to Read First

- `mrputridsden-production/pipeline-state-ep02.md` — checkpoint completo, todo `complete`
- `mrputridsden-production/pipeline-audit-ep02.md` — bitácora detallada de Stage 0 a Stage 5 + la
  reorganización de archivos
- `mrputridsden-production/episodios/temporada-2/` — metadata/youtube/social de EP.006 y EP.02, ya
  reorganizados

---

## Notes / Gotchas

- **El workflow `episode-pipeline/workflows/04-grid-rotation.md` sigue desactualizado para MPD.**
  Describe un markup que ya no existe. Falta una decisión de Andrés antes de reescribirlo: cuando
  llegue el Expediente 03, ¿las secciones de expedientes se acumulan indefinidamente en el sitio,
  o en algún punto se archivan/resumen? Sin esa decisión no se puede fijar el patrón de rotación
  nuevo. Registrado también en memoria `project_mpd_archivos_secretos_pillar`.
- **`ffmpeg -af afade` + `-ss`/`-to` DESPUÉS de `-i` silencia el clip sin error visible** — ver la
  regla nueva en `~/.claude/CLAUDE.md`. Aplica a cualquier corte de audio futuro (BTQ, CCC
  incluidos), no solo a MPD.
- **`episodios/temporada-2/` es el patrón nuevo para shows que separan numeración por temporada.**
  Si BTQ o CCC alguna vez lo necesitan, replicar la misma estructura (`episodios/temporada-N/`).

---

## Questions to Answer

1. ¿Cuándo se arranca la investigación del Expediente 03 (Crowley)?
2. ¿Qué pasa con el sitio cuando llegue el Expediente 03 — se acumulan las secciones o se
   archivan las viejas? (bloquea reescribir `04-grid-rotation.md` para MPD)
