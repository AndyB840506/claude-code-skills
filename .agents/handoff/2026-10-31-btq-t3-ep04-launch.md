# Handoff: BTQ T3 EP.04 — kit de lanzamiento listo, falta salir al aire y desplegar la web
**Date:** 2026-10-31
**Machine:** desktop (E:\)
**Status:** In progress — kit y piezas listos, episodio subido a Spotify; falta confirmar la hora, desplegar la web y avisar a Paula
---
## What We Accomplished This Session
- EP.04 grabado hoy por Zoom con Adriana Simbaqueba y Paula Cantor. Máster `E:\Podcast\BTQ\T3\EP 04.mp3`, 74:45. SRT `E:\Transcriptor\transcripciones\BTQ-T3-EP04.srt` (800 segmentos; separa bien las 4 voces aunque Alejo y Paula compartan micrófono).
- Título elegido por Andy: `EP.04 — "Esta niña": lo que le toca a una mujer para liderar en un call center`.
- Kit completo: `btq-production/launch-assets/T3-EP04-mujeres-lideres-launch.md`. Descripción de 349 palabras, plan social de domingo 1 a miércoles 4 nov, primeros comentarios con el link.
- Portadas con los 4 (`btq-portada-t3.py`, modo `INVITADAS`) y piezas de redes (`btq-social-t3.py`, `gente`, `HOST`, `RECORTE`). Regresión: EP.03 0 px en portadas; redes EP.01 y EP.03, 7 de 7 idénticas.
- Citas de Paula tras dos cambios de Andy: tarjeta "sí se puede" (64:37), tarjeta nueva "quería irse a los 10 minutos" (30:52, post del miércoles), reel "Es que esta niña me está diciendo tal cosa" (27:24).
- Reel `E:\Podcast\BTQ\T3\redes\EP04\BTQ-T3-EP04-reel-paula-nina-9x16.mp4`, 64,8 s (clip 26:49,65 a 27:54,45).
- Andy subió el episodio: https://open.spotify.com/episode/4toaNIfokVoTlUInTLSdbt
- Web en local: tarjeta `.next` del EP.04 con `ep04-cita-paula.jpg`, EP.03 en la fila "Temporada 3", `ep03-cita-alejo.jpg` borrada. **Sin desplegar y sin ver renderizada.**
- 3 aprendizajes en `episode-launch/workflows/t3-conversacional.md`.

## Where We Paused
**Last action:** session-close.
**Next action:** confirmar con Andy la hora de salida. Cuando el episodio esté al aire: oEmbed devuelve el título, revisar la web, `vercel --prod` desde `btq-production/website`, y `curl -L` + `tr -d '\r'` + diff contra el local.
**Blockers:** el episodio no aparecía público el 2026-10-31: oEmbed vacío, página 403, RSS con el EP.03 como último. Puede estar programado; no confirmado (el 403 podría ser un bloqueo a curl).

## Files to Read First
- `btq-production/launch-assets/T3-EP04-mujeres-lideres-launch.md` — checklist de Publicación al final; lista de lo que queda fuera de todo texto.
- `.claude/skills/episode-launch/workflows/t3-conversacional.md` — reglas del launch T3.

## Notes / Gotchas
- **Andy debe avisar a Paula** antes de publicar: anécdota del perro en la descripción (autorizada sin nombrar a KM2 ni al jefe) y sus citas. La descripción ya se le entregó a Andy para Spotify.
- **La lámina del reel incumple la regla nueva:** firma con Paula una frase del agente. Se le avisó a Andy y no decidió. Alternativa del mismo clip: "Y yo decía, cómo no, o sea, yo no soy una niña, me respetas".
- Teaser y stories dicen "HOY 9:30 PM": si la hora cambia, hay que regenerarlos (`btq-social-t3.py <out> EP.04`). Solo escritorio: fotos y piezas viven en E:\.
- En el segundo 0:45 del clip, Whisper oyó "No, dale, dale" en una pasada y el SRT del episodio no lo registra. Sin oír.
- La foto de Adriana mide 400×400 y se ve algo blanda en la 1:1.
- El lunes 2 nov debería ser festivo en Colombia (sin comprobar en calendario oficial).
- El clasificador de permisos bloqueó un commit + push por Bash con 3 archivos el 2026-10-31.

## Questions to Answer
- ¿Quedó programado para el domingo 1 nov, 9:30 PM?
- ¿La lámina del reel se queda, va sin firma o cambia de frase?
- ¿Adriana y Paula aceptaron volver para el episodio de IA? Se les invitó al aire y no respondieron. La IA no se prometió en ningún texto.
