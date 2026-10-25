# Handoff: BTQ T3 EP.03 — transcript, kit de lanzamiento y web en modo teaser
**Date:** 2026-10-24
**Machine:** desktop (E:\)
**Status:** In progress — kit, piezas y web teaser en producción; falta pasar el botón de la web a "Escuchar" cuando el episodio salga
---
## What We Accomplished This Session
- EP.02: publicado el domingo 18 (RSS lo confirma). El título salió "P.02 — …" (sin la E) en RSS y Spotify; **Andy decidió dejarlo así**. Su botón web nunca pasó a "Escuchar" y ya no hace falta (lo reemplazó el teaser del EP.03).
- EP.03 grabado hoy (2026-10-24, Zoom). Máster `E:\Podcast\BTQ\T3\EP 03.mp3`, **46:51** decodificado (la cabecera del mp3 dice 45:13: no usarla).
- Transcrito: `E:\Transcriptor\transcripciones\BTQ-T3-EP03.srt` (411 segmentos; `SPEAKER_00` = Andy, `SPEAKER_01` = Alejo, `SPEAKER_02` = canción). Tema: micromanagement.
- Título elegido por Andy: "EP.03 — El señor Burns y Balú: los dos jefes que hay en todo call center" (72 car., "Balú" con tilde por decisión de Andy).
- Kit completo: `btq-production/launch-assets/T3-EP03-micromanagement-launch.md` (descripción 297 palabras, tags, plan social dom-mar con link, fuentes por timestamp, lista "fuera de texto", promesa de invitadas mujeres líderes del BPO para el EP.04 aprobada por Andy, anécdota del cumpleaños en el post del lunes aprobada).
- Portadas `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP03-portada-{1x1,9x16,16x9}.png`; redes en `E:\Podcast\BTQ\T3\redes\EP03\` (teaser, 3 stories, 2 quote cards, reel Burns/Smithers PNG + MP4 68,4 s); clip `E:\Podcast\BTQ\T3\clip\BTQ-T3-EP03-CLIP-01.{wav,mp3}` (25:23.0–26:31.4, bordes re-transcritos).
- `btq-portada-t3.py`: arreglado — una línea con Ñ/Ú bajaba y se pegaba a la siguiente (tope común de mayúscula). Regresión EP.02: el bloque sube 1-2 px, mismo espaciado.
- `btq-social-t3.py`: entrada EP.03 en `EPS`. Regresión EP.02: 0 px.
- Spotify: programado por Andy para el **domingo 2026-10-25, 9:30 PM**; link `https://open.spotify.com/episode/64SD7d1siRZ6gLYgX6FPll`.
- Web en producción (`website-cazofcqad`, alias behind-thequeue.com): tarjeta EP.03 en teaser (fecha + quote card de Alejo `ep03-cita-alejo.jpg` + botón "Domingo 9:30 PM" al show); EP.02 en la fila "Temporada 3"; `ep02-cita-alejo.jpg` borrada. Verificado: HTML en vivo == local, imagen 200, ep02 da 404, capturas 1440/390 sin desborde.
- Commits `7c75a7e`, `64e63be`. Retro aplicada en `episode-launch/workflows/t3-conversacional.md` (duración decodificada, ortografía de lo renderizado y grafía de personajes, cita del reel que se lea sola, teaser N reemplaza N-1) y memoria `feedback_menus_welcome` (2+ preguntas → menú).

## Where We Paused
**Last action:** session-close (retrospectiva aplicada, auditoría del kit sin hallazgos).
**Next action:** cuando Andy confirme que el EP.03 está al aire (domingo 25 después de las 9:30 PM): comprobar que el oEmbed de `https://open.spotify.com/episode/64SD7d1siRZ6gLYgX6FPll` devuelve el título; en `btq-production/website/index.html` cambiar el botón `.pill` de la tarjeta `.next` a "Escuchar" con href al episodio (nota en el HTML encima del botón) y quitar la fecha de la etiqueta `.k`; `vercel --prod` desde `btq-production/website`; verificar con `curl -L` + diff (sin CR); marcar el checklist del kit.
**Blockers:** esperar a que el episodio esté en línea.

## Files to Read First
- `btq-production/launch-assets/T3-EP03-micromanagement-launch.md` — kit y checklist de publicación.
- `.claude/skills/episode-launch/workflows/t3-conversacional.md` — reglas del launch T3 (actualizadas hoy).

## Notes / Gotchas
- Las piezas de E:\ solo existen en el desktop.
- `vercel` sale con código 255 en PowerShell aunque el deploy quede bien (stderr envuelto): confirmar con `vercel inspect` o `curl`, no con el exit code.
- Preview de Vercel: `curl` da 200 con la página de login; producción sí se verifica con `curl -L`.
- El EP.03 promete en texto invitadas mujeres líderes para el EP.04: si no se cumple, avisar a Andy antes de escribir el kit del EP.04.

## Questions to Answer
- Ninguna abierta.
