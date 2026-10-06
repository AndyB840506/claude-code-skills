# Handoff: BTQ T3, EP.01 con la web en vivo y EP.02 con fecha
**Date:** 2026-10-06 (martes)
**Machine:** portátil (D:\)
**Status:** In progress. El ciclo del EP.01 de T3 quedó cerrado en la web; el EP.02 tiene fecha y falta su hoja de ruta, que se trabaja en el escritorio.

---

## What We Accomplished This Session

- **Se verificó el handoff del 03-oct antes de actuar.** El EP.01 ya estaba en línea: el oEmbed de Spotify respondía con su título, el RSS lo listaba primero y el embed del show mostraba el EP.01. La web en vivo seguía en la versión del 1 de octubre ("próximamente").
- **behind-thequeue.com desplegada a producción** con el OK de Andy (deployment `dpl_DuDUcEXL6umGaQT7MajKj5wfLpNT`, contenido del commit `05774f9`).
  - El HTML en vivo es idéntico byte a byte a `btq-production/website/index.html` (59.182 bytes tras normalizar fines de línea).
  - Captura con Playwright/Edge a 1440 px: el embed muestra el EP.01 con el arte de T3 sobre azul, 1:25:47; sin errores de JavaScript; el botón "Escuchar" de la tarjeta 01 apunta al episodio.
- **Decisiones de Andy para el EP.02 (2026-10-06):**
  - **Grabación: sábado 10 de octubre de 2026.**
  - **"Buenas y santas" queda retirado, sin reemplazo.** No hay saludo fijo; abren directo con la conversación, como en MPD. Descartó el guion telefónico y "Línea abierta".
- **Registrado:** casilla del despliegue marcada en el launch file del EP.01 (`45d9778`); roadmap § Temporada 3 con la fecha, el retiro del saludo y la línea vieja de "web sin desplegar" corregida (`5e35f61`); memoria `project_btq_t3_alejandro` al día.
- **Retrospectiva aplicada:** viñeta nueva en `CLAUDE.md` § Instrumentos que mienten (buscar `class="x"` exacto no ve elementos con varias clases) y memoria `reference_btq_vercel_deploy_laptop` actualizada.

## Where We Paused

**Last action:** cierre de sesión.
**Next action:** **en el escritorio**, preparar la hoja de ruta del EP.02 con la transcripción completa del EP.01 (`E:\Transcriptor\transcripciones\BTQ-T3-EP01.srt`, que solo existe en `E:\` del escritorio). Andy pidió esperar al escritorio para esto.
**Blockers:** saber quién arma la hoja de ruta. La minuta del 26-sep dice que Alejandro manda el esquema y que hay checkpoint el miércoles antes de grabar (sería el miércoles 7 de octubre). No se confirmó si eso sigue en pie.

## Files to Read First

- `btq-production/roadmap-btq.md` § Temporada 3: las decisiones de T3, incluidas las dos de hoy.
- `btq-production/launch-assets/T3-EP01-escampadero-launch.md`: el kit del EP.01 y cómo quedó anunciado el EP.02.
- `.claude/skills/episode-launch/workflows/t3-conversacional.md`: el flujo de T3 frente al de T2.

## Notes / Gotchas

- **La T3 va sin guion.** Lo que se prepara es tema y hoja de ruta (puntos, anécdotas, referencias). No aplicar `guion-style-btq.md` ni sus lints.
- **Tema del EP.02, anunciado al aire:** la otra cara de Alejo, que subió sin terminar la carrera. La cita exacta del anuncio está en el SRT del EP.01; no se abrió en esta sesión.
- **El chequeo `class="player"` del handoff anterior daba un cero falso:** la página vieja tenía `class="player rv"`. Para confirmar un despliegue, hacer diff del HTML en vivo contra el local.
- **En el portátil** se recreó `btq-production/website/.vercel/project.json` (ignorado por git) y se instaló `playwright` de Python. En el escritorio no cambió nada.
- **Vista móvil en vivo sin repetir:** la matriz de 7 anchos se pasó el 03-oct sobre este mismo HTML, pero no contra producción.
- `start.ps1` sigue avisando que la memoria está repartida en 3 slugs. No es nuevo.

## Questions to Answer

- ¿Alejandro manda el esquema del EP.02, o lo prepara Claude como borrador para el checkpoint?
- Sin comprobar: cuáles posts del plan social (domingo 4 a martes 6 de octubre) se publicaron.
- Sin comprobar desde el 27-sep: logo a 3000×3000 o vector, roadmap de 8 temas, transcripts a Drive para Alejandro.
- `MEMORY.md` mide 140 líneas (contadas con `wc -l` el 2026-10-06): el aviso de "200 líneas" del handoff del 03-oct ya no aplica. Memoria: 202 archivos, +8 desde la última auditoría; no alcanza el umbral de `/memory-audit`.
