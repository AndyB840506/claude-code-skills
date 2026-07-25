# Handoff: BTQ — rebrand v4 en vivo, reglas anti-fórmula y EP.023 listo para grabar

**Date:** 2026-07-25 (sábado)
**Machine:** desktop (E:\)
**Status:** In progress — todo lo que se podía hacer sin micrófono está hecho y verificado. Falta que Andy grabe.

---

## What We Accomplished This Session

**Rebrand v4 — cerrado.**
- `behind-thequeue.com` **en vivo** con el sistema v4 tipográfico. Verificado contra el dominio real con cache-busting: 7 marcadores nuevos presentes, 7 residuos viejos limpios, og-image 21 KB (antes 2 MB con typo), cabeceras de seguridad intactas.
- Se encontraron y corrigieron 3 residuos que el reskin había dejado vivos: la bio del host todavía traía la tesis de cultura pop («los personajes que más amamos»), «B-Side» (metáfora de vinilo retirada) y oro en el CSS del guion.

**Reglas nuevas — todas verificables por máquina, no por memoria.**
- **Español neutro** (`guion-style-btq.md`): estándar de **léxico, no de voz**. Incluye por qué `cola` es peligrosa y por qué el nombre del show nunca se traduce. Lint corrido sobre todo `btq-production`: la deuda era mínima y toda ya publicada.
- **Rotación de esqueleto:** ningún esqueleto dos episodios seguidos; menú de 5; el canónico queda **en pausa** tras usarse 4 veces (EP.020–023). Segmentos nombrados por contenido — `Cuerpo N` y `Re-enganche` prohibidos.
- **Nunca dos veces el mismo pozo:** ningún dato ni caso ancla puede repetirse en 5 episodios. (EP.020 y EP.022 compartían el mismo Cuerpo 2, «el dato SQM».)
- **Frases-molde:** `scripts/lint_guion_repeticion.py` (nuevo) mide solapamiento de 6-gramas contra los guiones anteriores, excluyendo el ritual.
- **Recomendaciones tejidas, sin bloque** — el bloque con encabezado era la peor señal de cierre falso. Confirmado con Andy antes de tocar `brand-constants.md`, que está congelada.

**EP.023 — reescrito entero con esqueleto INVERTIDO.**
- Abre con el desmentido de Levitt & List (2011), que antes estaba enterrado como «re-enganche».
- **Eliminada la escena de apertura compuesta** (Julián): contradecía en el primer minuto la promesa del show («casos documentados, cifras verificables»).
- Recomendaciones repartidas: Cuddy en el seg. 1 (misma crisis de replicación), Mayo en el 3, The Truman Show en el 5.
- Título fijado: `EP.23 — Efecto Hawthorne: por qué su equipo rinde distinto cuando lo miran` (73 car.).
- Portadas en tipografía pura, 3 aspect ratios, gate PASS.

**Audio:** se retira la música de intro/outro; va un jingle corto (mismo al abrir y cerrar).

---

## Where We Paused

**Last action:** retrospectiva + audit del kit aplicados y commiteados (`74e71f5`).

**Next action:** **Andy graba EP.023** (dijo que lo intentaría hoy en la tarde). Con el audio, retomar en **Stage B**: transcripción → assets.

> ⚠️ **Las quote cards son Stage B y se validan contra la TRANSCRIPCIÓN real, nunca contra el guion** — Andy se expande al grabar. `verify_assets.py` fallará por cards faltantes hasta que exista el audio; en Stage A hay que correrlo con `--stage-a`. El propio mensaje de error lo explica ahora.

**Blockers:** ninguno técnico. Todo lo pendiente depende de Andy.

---

## Files to Read First

- `btq-production/pipeline-state-ep023.md` — checkpoint del episodio, reescrito entero hoy. Manda sobre este handoff si chocan.
- `btq-production/guion-style-btq.md` — las 4 reglas nuevas viven aquí.
- `.claude/skills/episode-launch/docs/brand-constants.md` — **tabla nueva «qué generador se usa»**. Manda sobre los handoffs viejos.
- `btq-production/metadata-v4-macro.md` — lo que Andy tiene que pegar en Spotify.
- `btq-production/jingle-brief.md` — la dirección sonora está **ABIERTA**, ver abajo.

---

## Notes / Gotchas

- **Generadores muertos con cabecera `MUERTO`:** `portada-compose.py`, `show-cover-compose.py`, `youtube-assets-compose.py`, `EP023-hawthorne-artwork-v3.md`. El vivo para portadas de episodio es **`portada-ep-compose.py`** — que hoy estaba referenciado en **0 documentos** mientras el muerto aparecía en 11. Por eso existe la tabla en `brand-constants.md`.
- `portada-ep-compose.py` recibe el **título publicado completo** y aborta si no cumple la fórmula. Acepta `@archivo.txt` porque PS 5.1 pierde los acentos al pasar por `argv`.
- **Assets en `E:\AI\outputs\` — máquina desktop.** Desde el portátil no existen; habría que regenerarlos (son deterministas, un comando).
- **4 reprocesos por procedencia** esta sesión. Los 3 primeros comparten raíz: buscar una sola representación del dato. Generalizado en `skills/CLAUDE.md` § Instrumentos, con 4 preguntas antes de reportar un «cero hallazgos».
- La línea de ejemplo que la propia guía daba como mitigación anti-abandono («todavía no les he dicho la parte que…») **apareció casi textual en EP.022 y EP.023**. Los ejemplos de la guía son ilustraciones, no texto para pegar.

---

## Questions to Answer

1. **Sonido del jingle — ABIERTO.** Andy: «por el sonido industrial choca un poco, así que voy a experimentar con el sonido». La **forma** está fijada (2-4 s, corte seco, mismo stinger en los dos extremos, entrar sobre el silencio); el **mundo sonoro** no. **Preguntarle qué encontró antes de proponer nada.** Andy lo edita en Reaper; `scripts/cortar_jingle.py` existe como alternativa pero él prefiere su DAW.
2. **Tema de EP.024 — sin definir.** El teaser del cierre de EP.023 quedó genérico a propósito (`[PENDIENTE DEFINIR]` en el guion, 2 sitios). Repertorio disponible en `roadmap-btq.md`: Ley de Little, Parkinson, Peter, Brooks, Goldratt, Deming, Herzberg, Ringelmann.
3. **El 9:16 de la portada se ve vacío.** Es inherente a la tipografía pura en un lienzo tan alto. No se le inventó un elemento decorativo porque contradiría la dirección minimalista. **Pendiente el juicio de Andy.**
4. **Español neutro en MPD — aplazado a la semana del 2026-08-03.** Andy confirmó que aplica igual, se pospuso para cerrar BTQ. Nota puesta en `mrputridsden-production/guion-style-mpd.md`. Al retomarla: **adaptar, no copiar** — MPD tiene otro registro.
5. **Cita de EP.011 en la web** («Lo que tienes hoy no va a estar para siempre») está en tuteo contra el usted del sistema nuevo. **No se tocó**: no aparece en ningún guion del repo, así que no hay cómo saber si es textual del audio. Andy puede confirmarlo.

---

## Pendientes de Andy (ninguno lo puede hacer Claude)

| | |
|---|---|
| Grabar EP.023 | guion listo, artifact publicado |
| Subir 3 imágenes | `E:\AI\outputs\BTQ-brand\` → `BTQ-COVER-q92.jpg` (Spotify), `BTQ-yt-avatar-800.png` y `BTQ-yt-banner-2048x1152.jpg` (YouTube). **Las demás cosas de Spotify —descripción, categorías, retítulos— ya las aplicó.** |
| Experimentar con el sonido del jingle | ver pregunta 1 |
