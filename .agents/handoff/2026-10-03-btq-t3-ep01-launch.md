# Handoff: BTQ T3 EP.01 "De escampadero a carrera", listo para salir
**Date:** 2026-10-03 (sábado)
**Machine:** escritorio (E:\)
**Status:** In progress. Todo el kit de lanzamiento está listo y el episodio está programado en Spotify; falta desplegar la web cuando el episodio esté en línea.

---

## What We Accomplished This Session

- **El EP.01 de T3 se grabó hoy** (Zoom, 19:03) con Alejandro de co-host. El máster es `E:\Podcast\BTQ\T3\EP 01.mp3` y `.wav`, de **85:47**. Andy lo dio por definitivo, así que se publica completo.
- **Transcripción:** WhisperX con diarización → `E:\Transcriptor\transcripciones\BTQ-T3-EP01.srt`. `SPEAKER_01` = Andy (77 %, 55,9 min) y `SPEAKER_02` = Alejo (22 %, 15,7 min).
- **Título** (elegido por Andy): `EP.01 — De escampadero a carrera: lo que nadie cuenta de trabajar en un call center`.
- **Portadas compuestas** (3 formatos) en `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP01-portada-v2-*.png`. El script es nuevo: `comfyui/templates/btq-portada-t3.py`.
- **Descripción de Spotify:** 268 palabras, en HTML y en texto plano; tags y fuente de cada afirmación con su timestamp del SRT.
- **Clip de audio:** "No siempre el top performer tiene madera de líder" → `E:\Podcast\BTQ\T3\clip\BTQ-T3-EP01-CLIP-01.{wav,mp3}`, 48,05 s. Los bordes se comprobaron re-transcribiendo el clip.
- **Plan social** de domingo a martes: 12 posts en bloques listos para pegar.
- **Imágenes de redes** en `E:\Podcast\BTQ\T3\redes\EP01\`: teaser, 3 stories, 2 citas 4:5, lámina y MP4 del reel. El generador es nuevo: `comfyui/templates/btq-social-t3.py`.
- **Lista "fuera de todo texto escrito"** en el launch file: lo sensible del audio que no entra en ningún texto publicado (la empresa "lavada en activos", críticas a personas con nombre, drogas).
- **Web preparada, SIN desplegar** (commit `05774f9`): la tarjeta del EP.01 enlaza al episodio y vuelve el embed del show. Pasa la matriz de 7 anchos (360 a 1440): sin desborde, sin errores, con la tarjeta y el embed en su sitio.
- **Decisión de Andy:** la metadata de T2 en el RSS **no se corrige** ("ya cerremos T2"). El EP.23 sigue como S3E1, junto al EP.01. Quedó tachado en el roadmap y anotado en la memoria.
- **Retrospectiva aplicada:**
  - nuevo `episode-launch/workflows/t3-conversacional.md`, enlazado desde `SKILL.md`;
  - §E con la comprobación de los bordes del clip y `-t` en vez de `-shortest`;
  - `web-page-kit` con la receta de Playwright y el falso "revelado atascado" del hero fijo;
  - `CLAUDE.md` con `sed -i` añadido a la regla de las barras invertidas.

## Where We Paused

**Last action:** cierre de sesión (retrospectiva, auditoría y handoff).
**Next action:** cuando Andy avise que el EP.01 ya está en línea (**domingo 4 de octubre, 11 PM Colombia**):
1. Confirmar que el oEmbed responde: `curl -sL "https://open.spotify.com/oembed?url=https://open.spotify.com/episode/6Mssd4RGqkzrvrcLTwdr8b"`. Hoy devuelve vacío porque el episodio está programado.
2. `vercel deploy --prod --yes --cwd "C:\Users\andre\.claude\skills\btq-production\website"`
3. Verificar en behind-thequeue.com con `curl -L` que no quede ningún `class="player"` y que aparezca `6Mssd4RGqkzrvrcLTwdr8b`, y capturar el embed para confirmar que muestra el EP.01 y no el EP.27.

**Blockers:** solo la hora de salida del episodio. El despliegue funciona desde cualquier máquina, porque la web está en git. Las imágenes y el audio, en cambio, viven en `E:\` del **escritorio** y no están en el portátil.

## Files to Read First

- `btq-production/launch-assets/T3-EP01-escampadero-launch.md`: todo el kit, con qué imagen va en cada post y los pendientes con casillas.
- `.claude/skills/episode-launch/workflows/t3-conversacional.md`: lo que cambia en T3 frente al flujo de T2.
- `btq-production/roadmap-btq.md` § Temporada 3.

## Notes / Gotchas

- **El embed del show muestra el último episodio publicado.** Si se despliega antes del domingo a las 11 PM, la web muestra el EP.27 en rojo, que es justo lo que se quería evitar. La web en vivo todavía tiene la tarjeta propia (`class="player"`).
- **El push a GitHub no despliega BTQ.** Hace falta `vercel --prod`.
- **Verificar la web en local:** las capturas de Edge headless por ancla salen vacías y las de viewport alto deforman el hero fijo. Usar Playwright con `channel="msedge"`, como explica `web-page-kit` Rule 10.
- **Bajo `file://` sale un error falso del favicon** (`/btq-t3-logo.png`). En vivo responde 200.
- **El índice `MEMORY.md` está en 200 líneas**, el límite de lectura del hook. Para bajarlo hay que fusionar unas 60 memorias con `/memory-audit`, que propone antes de aplicar. No lo hice sin preguntar.
- En el audio del EP.01 la apertura todavía dice **"Buenas y santas"**. Eso queda para el EP.02.

## Questions to Answer

- ¿El subtítulo de Spotify ("lo que nadie cuenta de trabajar en un call center") está bien? Se cambió del "20 años dentro de un call center" que propuse, porque Andy dice "más de 15 años".
- ¿Andy está cómodo con dos posts en primera persona que usan sus anécdotas: lo de aplicar a team leader y los casi ocho años para terminar la carrera?
- ¿Las "pulgas" del primer edificio están bien entendidas por Whisper? Nadie escuchó ese tramo.
- EP.02: el saludo nuevo y la fecha de grabación. El tema ya está anunciado al aire: la otra cara de Alejo, que subió sin terminar la carrera.
- Sin comprobar desde el 27-sep: logo a 3000×3000 o vector, roadmap de 8 temas, transcripts a Drive para Alejo.
