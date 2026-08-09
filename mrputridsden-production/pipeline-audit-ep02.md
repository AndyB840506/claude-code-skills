## Stage 0 — Intake
- Qué se hizo: episode brief construido (show, audio, datos de episodio); pipeline-state-ep02.md creado retroactivamente (stage_a: complete)
- Resultado: OK

EPISODE BRIEF
  show:            MPD
  ep_number:       EP.02 (T2·E2)
  title:           Pactos, símbolos y mensajes ocultos: el rock y el diablo
  cultural_ref:    Robert Johnson / encrucijada → Led Zeppelin - Crowley / Boleskine → backmasking - PMRC / juicio Nevada 1990
  guest:           none (formato solo)
  sources:         mrputridsden-production/banco-expedientes.md; mrputridsden-production/scripts/EP02-el-rock-y-el-diablo.html
  closing_tm:      n/a (solo BTQ)
  spotify_url:     pending
  audio_path:      E:\Podcast\MPD\Temporada 2\EP 02\MPD EP 02.wav (grabación completa 2026-08-06)
  language:        es
  speakers:        solo (MPD T2 = formato solo, no co-host)

## Stage 1 — Transcripción
- Qué se hizo: re-transcripción con diarización (large-v2, es, srt) sobre la grabación completa nueva (la toma corta del 08-05 se respaldó como "MPD EP 02 (pre-fix backup).srt" antes de sobrescribir)
- Archivos generados: E:\Transcriptor\transcripciones\MPD EP 02.srt (39:23, 51.799 bytes)
- Resultado: OK

## Stage 1b — Verificación de fuentes (16 marcadores .verificar, deuda de la sesión 08-05)
- Qué se hizo: WebSearch dirigido sobre cada marcador, cruzado contra el SRT nuevo para ver qué quedó grabado
- Resultado: 15/16 CONFIRMADOS o ya cubiertos por el hedge existente; 1 ALERTA — incendio de Boleskine "1900" (min 18:17 del audio) sin fuente encontrada (los incendios documentados son 2015 y 2019). Andrés decidió (2026-08-06) dejarlo tal cual, sin regrabar ni cortar — "no siempre tiene que ser 100% verificable".
- Detalle completo en el mensaje al usuario de esta sesión (no se generó archivo aparte)

## Stage 2a — Show notes + YouTube
- Qué se hizo: workflows 05-show-notes.md y 07-youtube.md de podcast-creator, con timestamps verificados contra el SRT real (no los estimados del guion)
- Archivos generados: mrputridsden-production/episodios/temporada-2/ep02-metadata.md, mrputridsden-production/episodios/temporada-2/ep02-youtube.md (movidos y renombrados desde shownotes-ep02.md/youtube-ep02.md el 2026-08-09, ver nota abajo)
- Resultado: OK — título Spotify 64 chars, descripción corta 128 chars, 6 capítulos YouTube verificados (mínimo 105s, regla de los 10s)

## Stage 2b — Artwork (composición nueva, no el formato numeral de EP.006)
- Qué se hizo: el workflow 03-artwork.md de podcast-creator estaba desactualizado (dirección T1); se verificó el artwork vigente (EP.006) y se acordó con Andrés una escena fotorrealista propia que integra las 3 historias (cruce de caminos + disco de vinilo + casona/Boleskine al fondo), en vez de reusar el formato "numeral gigante". Generada en ComfyUI local (Z-Image Turbo, 1536² → RealESRGAN 4x → 3000×3000), grading azul de marca (night_grade variante E) por pedido explícito de Andrés, compuesta con `comfyui/templates/mpd-portada-ep02-t2.py` (basado en mpd-portada-ep-t2.py pero sin draw_numeral). Aprobado por Andrés en escena base y en los 3 formatos finales.
- Archivos generados: E:\Podcast\MPD\Temporada 2\EP 02\artwork\MPD-T2E02-PORTADA-3000.jpg (1:1), MPD-T2E02-16x9-FINAL.png, MPD-T2E02-9x16-FINAL.png
- Verificado: piso de negro ≥11 en esquina, footer (21,17,16) ≈ FOOTER_DARK (20,17,16) — invariante de marca respetada; legible a 150px
- Resultado: OK

## Stage 2c — Plan social (3 días)
- Qué se hizo: workflow 04-social-media.md de podcast-creator. Fecha de publicación confirmada con Andrés: sábado 2026-08-08 00:00 (tras corregir un primer dato ambiguo de "mañana a medianoche" que no dejaba ventana para el plan de 3 días). Solo Instagram/Facebook — TikTok pausado, YouTube sin canal, MPD no tiene LinkedIn/X.
- Archivos generados: mrputridsden-production/episodios/temporada-2/social-ep02.md (movido desde social-ep02.md el 2026-08-09)
- Resultado: OK — plan completo generado ANTES de publicar en Spotify, no después (regla del pipeline, aprendida en MPD EP.005)

## Corrección de numeración (2026-08-06)
- Andrés corrigió: la Temporada 2 reinicia numeración pública en EP.02 — no continúa la cuenta EP.001-005 de T1. Todos los archivos de este episodio (antes nombrados "ep007") y sus referencias internas ("EP.007") se renombraron a "ep02"/"EP.02". El handoff histórico `2026-08-05-mpd-ep007-reescritura.md` NO se renombra — narra el estado a esa fecha, se queda como registro.

## Reorganización 2026-08-09 — episodios/temporada-2/
`shownotes-ep02.md`, `youtube-ep02.md` y `social-ep02.md` vivían sueltos en la raíz de
`mrputridsden-production/`, distinto del patrón de EP.001-005 (`episodios/ep0XX-metadata.md`).
Movidos y renombrados a `episodios/temporada-2/ep02-metadata.md` / `ep02-youtube.md` /
`social-ep02.md`. De paso, `episodios/ep006-metadata.md`, `social-ep006.md` y `youtube-ep006.md`
(que sí seguían el patrón pero vivían sueltos en `episodios/`, mezclados con los de T1) se
movieron también a `episodios/temporada-2/` para que la carpeta separe T1 de T2 consistentemente.
**Los handoffs históricos que citan las rutas viejas de EP.006 NO se reescribieron** (narran el
estado a esa fecha) — si se abren, la ruta que dan ya no es la vigente; la vigente es esta.

## Cierre de Macro-Stage B
- stage_b: complete, spotify_url: https://open.spotify.com/episode/46l6NpQVF9np4unotGT4KM?si=dscl0PsHSoWMLsIURGBNGQ — recibida 2026-08-06, pero Andrés aclaró que NO está en vivo todavía (programada sábado 2026-08-08 00:00). No se verificó con HTTP porque el usuario ya avisó que fallaría — no es una comprobación pendiente, es el estado esperado.

## Stage C — Retomado 2026-08-09 (sesión nueva, handoff del 08-06 quedó parado en sábado)
- Spotify confirmado en vivo con WebFetch directo al episodio Y a la página del show (dos verificaciones independientes) antes de tocar el sitio.
- **Hallazgo:** el sitio (mrputridsden.com) nunca se actualizó tras publicar EP.006 el 08-01 — "Expediente 01" seguía en "En producción" y el embed de Sintoniza apuntaba a EP.005 (T1). El `workflow 04-grid-rotation.md` de `episode-pipeline` describe un markup `.episodes-grid`/`.episode-card` que ya no existe en el sitio real — el rediseño "La Guarida" (commit `8b9a4a8`, 2026-07-22) lo reemplazó por completo. Ese workflow quedó desactualizado para MPD; no se siguió tal cual.
- Confirmado con Andrés (AskUserQuestion) el alcance del fix: Expediente 01 pasado a publicado + Expediente 02 agregado como sección nueva.

## Stage 4 — "Rotación" (adaptada — no aplica el grid de 4 cards del workflow)
- Qué se hizo: portadas 1:1 de EP.006 y EP.02 copiadas desde `E:\Podcast\MPD\Temporada 2\EP 01\artwork\MPD-T2E01-PORTADA-3000.jpg` y `...\EP 02\artwork\MPD-T2E02-PORTADA-3000.jpg`, redimensionadas a 760×760 (convención de `t2-cover.jpg`) y guardadas como `ep01-cover.jpg` (56 KB) / `ep02-cover.jpg` (108 KB) en `website/`.
- `index.html`: nav "Expediente 01"→"Expedientes"; hero pasa a destacar Expediente 02 (el más reciente); Expediente 01 actualizado a estado publicado con link real a Spotify (`3KW68cHhHpkMCLbgZkiov7`) y portada propia; sección nueva `#expediente02` con sinopsis (Robert Johnson / Boleskine House / juicio de Judas Priest) y link a Spotify (`46l6NpQVF9np4unotGT4KM`); embed de Sintoniza actualizado al episodio de EP.02. "El Archivo" (T1) sin tocar.
- Verificación de integridad: conteo de comillas por línea (0 líneas con número impar), imágenes con width/height explícitos.
- Resultado: OK

## Stage 5 — Deploy + verificación
- Qué se hizo: `deploy-preflight` (PASS: project.json correcto `mr-putrids-den-web`, sin secrets, baseline 200, `ignoreCommand: exit 0` confirmado → flujo prebuilt) → gate de aprobación (aprobado por Andrés) → copia a `.vercel/output/static/` → `vercel deploy --prebuilt --prod` → `vercel alias set <deployment> www.mrputridsden.com` (obligatorio, `--prod` no realiasa el dominio custom) → verificación HTTP → verificación Spotify.
- URL verificada: `https://www.mrputridsden.com/?cb=...` → 200, con `cache-buster` para evitar cache de WebFetch/CDN. Marcadores nuevos confirmados en el HTML servido: "Expediente 02", "ep02-cover.jpg", URL de Spotify de EP.02.
- Verificación Spotify: PASS — episodio encontrado en la página del show.
- Resultado: OK — episodio publicado y sitio verificado en vivo.
