# Handoff: BTQ T3 EP.02 — transcript, kit de lanzamiento y web en modo teaser
**Date:** 2026-10-17
**Machine:** desktop (E:\)
**Status:** In progress — kit y web listos; falta cambiar el botón de la web cuando el episodio salga
---
## What We Accomplished This Session
- EP.02 de T3 grabado hoy (2026-10-17, Zoom; no el 10 como decía la memoria). Máster `E:\Podcast\BTQ\T3\EP 02.mp3`, 64:25.
- Transcrito con WhisperX: `E:\Transcriptor\transcripciones\BTQ-T3-EP02.srt` (587 bloques; `SPEAKER_02` = Andy, `SPEAKER_01` = Alejo).
- Título elegido por Andy: "EP.02 — La gente no renuncia al trabajo, renuncia al jefe (y a veces el problema es el top performer)" (101 car.).
- Kit completo: `btq-production/launch-assets/T3-EP02-renuncia-al-jefe-launch.md` (descripción 256 palabras, tags, plan social dom-mar con link de Spotify, fuentes por timestamp, lista "fuera de texto").
- Portada opción A (frase completa) en `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP02-portada-{1x1,9x16,16x9}.png`.
- Redes en `E:\Podcast\BTQ\T3\redes\EP02\`: teaser, 3 stories, 3 quote cards, reel MP4 de 55,0 s (clip 45:37.80–46:32.80, manzana podrida). Citas re-verificadas contra el SRT con script (con prueba de mutación).
- `comfyui/templates/btq-social-t3.py`: config por episodio en `EPS` + 2º argumento `EP.NN`; quote cards alineadas por línea base. Regresión EP.01: 0 px de diferencia (antes del arreglo de línea base).
- Spotify: programado por Andy para el **domingo 2026-10-18, 9:30 PM**; link `https://open.spotify.com/episode/6wAsgLBFQmDPcEf9vX5DdU`.
- Web en producción (`dpl_2QgreA5ddq6rvch45uWHPv2EotpU`): tarjeta EP.02 en modo teaser (fecha + quote card de Alejo + botón "Domingo 9:30 PM" al show) y EP.01 en fila "Temporada 3". Verificado: HTML en vivo == local, imagen 200, captura 1440/390 sin desborde.
- Retrospectiva aplicada: `episode-launch/workflows/t3-conversacional.md` (keyword en títulos, inglés sin traducir, oración completa en portada/teaser, generador EPS + regresión, teaser web, Vercel Auth); puntero al workflow en los dos kits T3; memorias `feedback_btq_english_terms_untranslated`, `project_btq_t3_alejandro`, `btq_website`.

## Where We Paused
**Last action:** session-close (retrospectiva + auditoría del kit sin hallazgos nuevos).
**Next action:** cuando Andy diga que el EP.02 está al aire (domingo 18 después de las 9:30 PM): en `btq-production/website/index.html` cambiar el botón de `.next` a "Escuchar" con href al episodio (hay nota en el HTML encima del botón), quitar la fecha de la etiqueta `.k`, verificar que el link abre el EP.02 (oEmbed con título), `vercel --prod` desde `btq-production/website`, y verificar con `curl -L` + diff. Marcar el checklist del kit.
**Blockers:** esperar a que el episodio esté en línea.

## Files to Read First
- `btq-production/launch-assets/T3-EP02-renuncia-al-jefe-launch.md` — kit y checklist de publicación.
- `.claude/skills/episode-launch/workflows/t3-conversacional.md` — reglas del launch T3 (no se leyó en esta sesión hasta la retro).

## Notes / Gotchas
- Las piezas de E:\ solo existen en el desktop.
- Preview de Vercel: `curl` da 200 con la página de login (no 401); el MCP de Vercel no tiene acceso a `mrputridsden`. Producción sí se verifica con `curl -L`.
- PIL `Errno 22` al guardar sobre un archivo abierto en el visor de Andy: generar en temporal y copiar.
- Andy decidió dejar la descripción del EP.01 con la promesa "la otra cara de Alejo" aunque el EP.02 no la cumple.
- Extra sin post asignado: `BTQ-T3-EP02-cita-alejo-pregunta-4x5.png` (Andy no respondió si se borra).

## Questions to Answer
- NO CONFIRMADO: ¿las anécdotas personales de Andy en los posts de LinkedIn del domingo (equipos pulidos que le quitaban) y del lunes (top performer que llegaba tarde) están OK para publicar? El workflow T3 pide avisar antes.
- NO CONFIRMADO: el título no lleva keyword call center/BPO (el formato T3 la pide); avisado a Andy en la retro, sin respuesta explícita.
- ¿Se borra la tarjeta extra `cita-alejo-pregunta-4x5.png`?
