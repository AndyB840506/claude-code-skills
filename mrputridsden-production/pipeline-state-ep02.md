EPISODE: EP.02 (MPD, T2·E2) — "Pactos, símbolos y mensajes ocultos: el rock y el diablo"
notas_numeración: corregido 2026-08-06 (Andrés) — T2 reinicia numeración pública en EP.02, no continúa la cuenta EP.001-005 de T1. Archivos y checkpoint renombrados de ep007 a ep02; el handoff histórico del 08-05 sigue archivado como "ep007" porque narra el estado de esa fecha, no se reescribe.
stage_a: complete — 2026-08-05 (guion final reescrito, 5.725 palabras, mrputridsden-production/scripts/EP02-el-rock-y-el-diablo.html; creado retroactivamente 2026-08-06, el episodio venía en curso antes de este checkpoint)
stage_b: complete — 2026-08-06 (transcripción, verificación de fuentes, show notes, YouTube, artwork nuevo y plan social los 3, todo listo — ver pipeline-audit-ep02.md)
stage_c: complete — 2026-08-09. Spotify confirmado en vivo (verificado vía WebFetch al arrancar la sesión, publicado 2026-08-08). El sitio (mrputridsden.com) nunca se había actualizado tras publicar EP.006 el 08-01 — seguía mostrando "Expediente 01 · En producción" y el embed apuntaba a EP.005 (T1). El `workflow 04-grid-rotation.md` describe un markup `.episodes-grid`/`.episode-card` que ya no existe (reemplazado por el rediseño "La Guarida", commit `8b9a4a8`, 2026-07-22) — no aplicaba tal cual, así que el fix real fue: Expediente 01 pasado a publicado (portada propia `ep01-cover.jpg`, link real a Spotify), Expediente 02 agregado como sección nueva (portada `ep02-cover.jpg`), hero actualizado a destacar EP.02, embed de Sintoniza actualizado. Deploy prebuilt + alias verificado HTTP 200 y contenido nuevo en vivo. Detalle completo en `pipeline-audit-ep02.md`.
spotify_url: https://open.spotify.com/episode/46l6NpQVF9np4unotGT4KM — CONFIRMADO EN VIVO 2026-08-09 (verificado dos veces: WebFetch directo al episodio, y listado en la página del show)
notes: Segunda grabación completa hecha 2026-08-06 21:32-21:37 en E:\Podcast\MPD\Temporada 2\EP 02\MPD EP 02.wav/.mp3/.rpp (reemplaza la toma corta del 08-05, 24:40, que fue solo de calibración). Pendiente antes de cerrar Stage B: verificar ~10 marcadores .verificar nuevos del guion (raíz africana del mito del cruce, incendio de Boleskine 1900, símbolos de Led Zeppelin IV, cita de Rob Halford, alcance PMRC/Senado 1985, fama de Tommy Johnson en vida, escultura de Clarksdale, jurado o no en el juicio de Nevada, año de muerte de Kenneth Anger) — lista completa en .agents/handoff/2026-08-05-mpd-ep007-reescritura.md.

## Corrección 2026-08-09 — Stage 3b (quote cards) nunca corrió, ahora sí
Stage A/B/C (guion/assets/deploy) completos y plan social de 3 días publicado (confirmado por
Andrés). El workflow `03b-marketing.md` Paso 2 (quote cards) nunca se ejecutó para EP.02 — la
bitácora salta del plan social a la corrección de numeración sin pasar por ahí. EP.006 sí tuvo
4 quote cards verbatim (ver handoff 07-28/07-30); EP.02 tenía cero. Un "no hace falta" registrado
antes fue una confirmación apurada del usuario sobre una pregunta que empaquetaba dos assets
distintos — corregido al re-preguntar por separado. **Resuelto:** 4 quote cards generadas con
`comfyui/templates/mpd-quote-card-ep02-t2.py` (copiado/adaptado de `mpd-quote-card-t2.py`,
escena/paleta desde `mpd-portada-ep02-t2.py`), verbatim contra el SRT real, verificadas
visualmente. **Clip de audio resuelto también:** extraído del máster con ffmpeg (33:39–34:38,
juicio de Nevada, 59.6s) — ver `episodios/temporada-2/social-ep02.md` para el detalle del bug de `afade` encontrado y
corregido en el proceso. Pipeline de EP.02 completo, sin pendientes conocidos.
