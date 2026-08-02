# Handoff: BTQ EP.024 grabado, transcrito y con toda la metadata lista

**Date:** 2026-08-01 (sábado)
**Machine:** desktop (E:\) — todo el audio y el artwork viven ahí; desde el portátil no existen
**Status:** In progress — el episodio está listo para subir; falta la URL real de Spotify y el deploy del sitio

---

## What We Accomplished This Session

Andy grabó el EP.024 nuevo (seguridad psicológica) y esta sesión lo llevó de WAV a paquete de
publicación completo. **Publica mañana domingo 2026-08-02 a las 8:00 PM Colombia** (verificado
contra el calendario: el 2 de agosto de 2026 sí cae domingo).

**Audio y transcripción**
- `BTQ EP 24 oficial.wav` — 41:26, tomas `260801_1832` y `_1836`. La identidad se verificó por
  las tomas que cita el `.rpp`, no por la duración: el WAV de Peter dura 41:00, a solo 26 s.
- MP3 de publicación medido contra EP.023: −21,0 vs −21,2 LUFS, LRA 5,4 vs 5,5, formato idéntico.
  El único delta es el true peak, −0,8 dBFS contra −2,3. Andy lo dejó así.
- SRT con WhisperX: 451 cues, un solo hablante, último cue en 41:08. Se corrigieron 5 «Greenfield»
  → «Grenfell» y «12 heridas» → «2 heridas»; el ASR crudo quedó en `-ASR-CRUDO.srt`.

**Se abrieron las fuentes primarias que llevaban dos sesiones pendientes** — era el pendiente
marcado como «de más riesgo» en el pipeline-state:
- **Hidroituango:** se bajó y leyó el comunicado de prensa n.º 165 de la CGR (26 nov 2021). Fallo
  en firme de **$4.330.831.615.227,34** contra **26 personas naturales y jurídicas**
  ($3.157.419.881.218,97 de destrucción de VPN + $1.173.411.734.008,37 de lucro cesante).
  **El audio dice «1,1 y 2,9 billones», que son las cifras del informe especial ANTERIOR.**
- **Reficar conciliado:** USD 997 millones = $2,9 billones es el *fallo* del 26 abr 2021, contra
  2 presidentes, 3 vicepresidentes, 7 miembros de junta y 4 contratistas — exactamente la
  composición que el episodio nombra al aire. Confirmado también el salto de presupuesto de
  USD 3.993 a 4.854 millones el 7 de mayo de 2012.

**Entregables producidos**
- **Artículo** `/episodios/por-que-su-equipo-no-le-cuenta-los-problemas` — 3.437 palabras,
  5 bloques, 6 fuentes. JSON-LD parsea, sitemap regenerado, índice enlazado, og:image propia
  1920×1080. Verificado con script, no a ojo.
- **Assets de lanzamiento** en `launch-assets/EP024-puerta-abierta-launch.md`: Spotify (388
  palabras medidas, versión HTML copy-safe), plan social de 4 días, YouTube con 16 capítulos
  sacados del SRT alineado.
- **4 quote cards** 1920×1080, citas validadas verbatim contra el SRT con el diff de limpieza
  impreso (solo dos muletillas: «simplemente», «pues»).
- **Compuerta de assets en PASS**, stage 1 y stage 2: se leyeron las 7 imágenes contra
  `banned-patterns.json` (cero anillos incluso en zoom nativo, título cotejado letra por letra,
  tildes correctas en las cards).

**Retrospectiva aplicada** (commit `12cd371`): el SRT no es el audio; el composer de portadas
ahora emite tamaños canónicos; barrer la carpeta del EPISODIO al reasignar; y reproducir un
fallo antes de sumar un instrumento a la lista de los que «mienten en silencio».

---

## Where We Paused

**Last action:** commit `12cd371` con los cuatro cambios de la retrospectiva, pusheado.

**Next action:** **el domingo, cuando el episodio esté publicado en Spotify**, copiar la URL real
desde la página del episodio en el navegador y pasármela.

**Blockers:** ninguno para subir el episodio. La URL de Spotify es lo único que bloquea el
deploy del sitio.

---

## Files to Read First

- `btq-production/pipeline-state-ep024.md` — estado real, con la URL provisional y las
  decisiones de Andy sobre el audio. **Empezar por aquí.**
- `btq-production/launch-assets/EP024-puerta-abierta-launch.md` — todo lo que se copia y pega.
- `btq-production/website/episodios/por-que-su-equipo-no-le-cuenta-los-problemas.html` — el
  artículo, con sus 2 placeholders.

---

## Notes / Gotchas

- **⚠️ La URL de Spotify que hay guardada es PROVISIONAL y devolvió 404.**
  `https://open.spotify.com/episode/25xgYzaTZmxEXqTNIu7yQp`. Un 404 no distingue entre «no
  propagada», «ID equivocado» e «ID que va a cambiar». En EP.016 el ID cambió tras la re-subida.
  **Copiarla del navegador, no de este archivo.** El token `?si=…` es rastreo, no va nunca.
- **Tres discrepancias entre el audio y las fuentes, decididas por Andy y SIN corregir en el
  audio:** Nokia dice «4 de cada 10» en `10:04` (la fuente da 37,8%); el dato de la cuadrilla de
  Space no se dijo y se deja fuera; «Grenfell» suena a «Greenfield» solo para el ASR. Los assets
  públicos llevan la cifra verificada. **No reabrir esto como si fuera un pendiente.**
- **Los archivos de Peter se movieron a `E:\Podcast\BTQ\EP 27\`.** Sus portadas **no sirven
  ahí**: llevan `EP.24` horneado dentro de la imagen y hay que regenerarlas.
- Las portadas 16:9 y 9:16 se reescalaron a los tamaños canónicos; los originales grandes
  quedaron como `-2560x1440.png` y `-1620x2880.png` en las dos carpetas.
- **Rutas de `E:\` = solo desktop.** El audio, el SRT, las portadas y las cards no existen desde
  el portátil. Lo único que viaja en el repo es el artículo, el og:image y el .md de assets.
- Pendiente de artwork que no bloquea: la portada tiene 0,18% de píxeles `#000000` (el void es
  `#0E1113`, sospecha del degradado inferior), y las contrapruebas de 300/96 px de 9:16 y 16:9
  se generan en cuadrado, o sea deformadas — el `canvas.resize((px, px))` del composer.

---

## Questions to Answer

- Las portadas dicen `EP.24` (dos dígitos) y la atribución de las quote cards dice `EP.024`
  (tres). Las dos formas conviven en el mismo set. EP.023 hizo lo mismo, así que se dejó igual.
- ¿Se arregla la contraprueba cuadrada del composer? Es una línea
  (`canvas.resize((px, px))` en `portada-compose-ratios.py`), pero no estaba en el alcance
  aprobado hoy.
- `guion-style-btq.md` sigue en **1.012 líneas**. Señalado en dos audits seguidos, aplazado a
  propósito: partirlo merece su propia sesión.
- Sigue abierto de antes: correr `scripts/lint_guion_repeticion.py` contra EP.023 y contra el
  guion de Peter.
