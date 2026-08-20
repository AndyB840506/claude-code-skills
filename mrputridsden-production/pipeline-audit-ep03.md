## Stage A — Roadmap y pre-producción

- Qué se hizo: episodio confirmado desde `banco-expedientes.md` (candidato principal
  decidido por Andrés 2026-08-05, "Crowley y su huella en la música"). Verificadas antes
  de escribir: "Mr. Crowley" (Ozzy, 1980), "Quicksand" (Bowie, 1971), rostro de Crowley
  en Sgt. Pepper's (1967) — los 3 leads que estaban SIN VERIFICAR en el banco. Investigación
  adicional durante la escritura: la Abadía de Thelema y la muerte de Raoul Loveday (1923,
  origen real del apodo "el más malvado del mundo"), origen del apodo "La Bestia" (se lo
  puso su madre de adolescente), la Batalla de Blythe Road / expulsión de la Golden Dawn
  (1900, con W.B. Yeats), y el mito FALSO de que Black Sabbath toma su nombre de un texto
  de Crowley (viene de una película de Boris Karloff, 1963) — desmentido con fuente antes
  de escribirlo, evitando que un dato falso entrara al guion.
- **Experimento de estilo (decisión de Andrés, ver memoria `project_mpd_ep03_crypt_experiment`):**
  Tales from the Crypt aplicado SOLO a este episodio — ritmo de suspenso tipo
  horror-anthology, Andrés más cómplice en bienvenida/cierre, dos guiños de cuarta pared,
  y el cierre rompe a propósito la regla de "nunca resolver" con un giro irónico. Si no
  convence al escuchar la grabación, EP.02/EP.006 siguen siendo el molde para EP.04.
- Arquitectura aprobada por Andrés antes de escribir (target ~43 min / ~5.150 palabras,
  pausa 22%).
- Guion escrito: `scripts/EP03-la-bestia-que-el-rock-volvio-inmortal.html`. Word count
  verificado programáticamente (no a ojo): 4.408 palabras en bloques `host-text`, dentro
  del ±15% del target (banda 4.380-5.920) — primer borrador salió corto (2.627), se
  amplió con material adicional VERIFICADO (no relleno retórico): Abadía de Thelema,
  origen del apodo "La Bestia", Batalla de Blythe Road, mito de Black Sabbath.
  Publicado como Artifact para lectura: https://claude.ai/code/artifact/38b0c9d4-fe4e-4889-b149-080bd2948934
  Aprobado por Andrés.
- Artwork: concepto aprobado tras 3 iteraciones en ComfyUI local (Z-Image Turbo). v1
  produjo un patrón de diana/círculos concéntricos vetado en el sleeve de un vinilo
  (corregido describiendo el objeto sin nombrar el concepto prohibido, no negándolo). v2
  corrigió el patrón pero perdió la identidad de "vinilo" (quedaron como tarjetas en
  blanco) y agregó un segundo marco de sobra. v3 recuperó los vinilos como discos reales
  (surcos/etiqueta, textura física esperada, no el motivo decorativo vetado) sin
  reintroducir el patrón. Grading azul variante E aplicado y aprobado. Detalle completo
  y prompt final en `episodios/temporada-2/artwork-ep03.md`. Producción final (upscale,
  tipografía, quote cards) diferida a más cerca del lanzamiento — no bloqueante para
  Stage A.
- **Corrección post-retrospectiva:** el primer borrador del cierre dejaba el conector al
  próximo expediente SIN anunciar, decidido unilateralmente por el asistente — esa
  decisión es de Andrés por regla explícita (`mrputridsden/CLAUDE.md`). Corregido:
  Andrés eligió anunciar "Paul is Dead" como Expediente 04. Guion, `banco-expedientes.md`
  y este archivo actualizados; word count re-verificado (4.482, sigue dentro de banda).
- Archivo de estado creado: `pipeline-state-ep03.md`.
- Roadmap actualizado: fila de EP.03 pasa a `guion listo`.
- Resultado: OK — pausa natural, esperando grabación.

## Stage 0 (Macro-Stage B) — Intake
- Qué se hizo: episode brief construido. Audio auto-descubierto en `E:\Podcast\MPD\Temporada 2\EP 03\` (carpeta nueva por episodio, distinta del patrón viejo `E:\Podcast\Mr.Putrid\` documentado en `00-intake.md` — actualizar esa tabla). Confirmado con Andrés: usar `MPD EP 03.wav` (máster) para transcripción. Sin fuentes/links adicionales más allá de lo ya investigado en Stage A.
- Resultado: OK — brief listo, arranca transcripción.

## Stage 1 — Transcripción
- Qué se hizo: transcripción con diarización (large-v2, es, srt) vía WhisperX, corrida como proceso detached (Start-Process, no PowerShell background job — los jobs mueren con el proceso host del tool call). Warning de torchcodec presente pero inofensivo (ya documentado en `transcriptor/docs/environment.md`).
- Archivos generados: `E:\Transcriptor\transcripciones\MPD EP 03.srt` (39 KB). Verificado: apertura coincide con el guion (Hastings, muerte de Crowley 1947), tag `[SPEAKER_00]`.
- Resultado: OK

## Stage 1b — Hallazgo post-transcripción: cola de 18 min sin recortar
- Qué se hizo: el SRT mostraba contenido hablado real hasta 32:45 ("...la última palabra es suya") y después solo texto alucinado por WhisperX sobre audio no vocal ("Subtítulos por la comunidad de Amara.org", patrón conocido de WhisperX ante música/ruido no hablado) hasta el final del archivo en 50:28. Antes de asumir que esa cola de 17.7 min era silencio, se verificó con `ffmpeg -af volumedetect`: -25.2 dB mean / -0.5 dB max — no era silencio. **Causa real, confirmada por Andrés:** música de fondo de Reaper que no se recortó al exportar. Andrés ya la eliminó en el proyecto de Reaper y va a regenerar el export.
- Acción tomada (ahora superada): se había creado `MPD EP 03 - FINAL.wav`/`.mp3` con un corte manual a 32:45 (`ffmpeg -to 00:32:45 -c copy`) como estimación rápida. **Estos archivos quedan obsoletos** — Andrés va a entregar un nuevo export ya limpio desde Reaper; no usarlos para el resto del pipeline. Los originales (`MPD EP 03.wav`/`.mp3`, con la música de cola) tampoco se tocaron.
- Resultado: OK — Andrés eliminó la música de fondo en Reaper y regeneró el export.

## Stage 1c — Re-transcripción sobre el export limpio
- Qué se hizo: nuevo `MPD EP 03.wav`/`.mp3` (Reaper, música de cola eliminada) verificado — duración 33:01.8 (antes 50:28.5), volumedetect al final (-23.3 dB mean / -0.5 dB max, consistente con outro, no con la anomalía anterior). Copiado a `E:\Transcriptor\audios\`, SRT viejo respaldado como `MPD EP 03 (pre-fix backup).srt`, re-transcrito completo (large-v2, es, diarize).
- Archivo generado: `E:\Transcriptor\transcripciones\MPD EP 03.srt` (38.6 KB). Verificado: cierra limpio en 32:42 ("...la última palabra es suya"), sin la alucinación de "Subtítulos de Amara.org" que aparecía en la versión vieja — confirma que la cola de música ya no está.
- audio_path del brief actualizado a la versión limpia (mismo nombre de archivo, contenido regenerado).
- Resultado: OK — listo para Stage 2 (assets), duración real del episodio ~32:45.

## Stage 2 — Generación de assets (ruta MPD)
- Qué se hizo: invocados `podcast-creator/workflows/05-show-notes.md`, `07-youtube.md`, `04-social-media.md`. Los 3 blocks `.verificar` del guion sobre datos de Crowley (Sgt. Pepper's +70 figuras, Batalla de Blythe Road, Bowie LA 1975-76) se cerraron con fuente antes de escribir la metadata pública — ver ediciones en el guion mismo (2026-08-15). Capítulos de YouTube y timestamps de show notes verificados contra el SRT real (no contra las estimaciones del guion, que sobreestimaban ~10 min en los actos finales). Andrés confirmó fecha de publicación: lunes 2026-08-17, 00:00 — plan social armado con esas fechas.
- Archivos generados:
  - `episodios/temporada-2/ep03-metadata.md` (Spotify título 44 chars, descripción corta 124 chars, ambos OK)
  - `episodios/temporada-2/youtube-ep03.md` (título 45 chars, 18 tags, 7 capítulos — las 3 reglas duras de YouTube verificadas programáticamente, todas OK, más corto 98s)
  - `episodios/temporada-2/social-ep03.md` (plan 3 días, Instagram/Facebook — Día 1 sábado 2026-08-15, Día 2 domingo 2026-08-16, Día 3 lanzamiento lunes 2026-08-17)
- Artwork: sigue en estado "concepto aprobado, producción final pendiente" (`artwork-ep03.md`) — no bloqueante para cerrar Stage B, es insumo de Stage 3.
- Chequeo de consistencia título/tagline: guion, show notes y artwork usan el mismo título ("La Bestia que el rock volvió inmortal") — sin discrepancia.
- Checkpoint Spotify: URL sigue `pending` — Andrés va a publicar el lunes 2026-08-17. Metadata de Spotify lista para copiar/pegar en `ep03-metadata.md` §C.
- Resultado: OK — 4 archivos listos, esperando URL de Spotify para cerrar Stage B por completo. Continúa en paralelo a Stage 3 (validación de imágenes / producción final de artwork).

## Stage 3 — Producción final de artwork + quote cards
- Qué se hizo: usuario pidió adelantar Stage 3 porque publica esta noche (programado para el lunes). ComfyUI local levantado (estaba caído). Escena base regenerada a 1536×1536 con el prompt/seed aprobados en Stage A (3082026) — la composición salió simétrica en vez de la asimétrica de v3 original; confirmado con Andrés que sirve así.
- **Intento de usar el mood de v1** (`MPD-T2E03-validation_00001_.png`, que Andrés prefería visualmente): rechazado — tenía el patrón de diana/círculos concéntricos VETADO en el sleeve de un vinilo (regla firme sin excepciones) y el rostro salió demasiado legible/reconocible contra el requisito de "ilegible". 2 rondas de corrección de prompt (mover la instrucción de disolución de rostro al frente, intensificarla) NO lograron resolver la legibilidad de la cara — cada intento salió peor (más nítido, incluso apareció un segundo cuadro de fondo no pedido). Se descartó el mood de v1 y se siguió con la escena simétrica, que cumplía las reglas desde el primer render.
- Upscale 3000×3000 vía ComfyUI API (UpscaleModelLoader + ImageUpscaleWithModel RealESRGAN_x4plus + ImageScale lanczos) — verificado 3000×3000 exacto con PIL.
- `night_grade` variante E aplicado (misma que EP.006/EP.02).
- Composición: `comfyui/templates/mpd-portada-ep03-t2.py` (nuevo, copiado de `mpd-portada-ep02-t2.py`) para 1:1/16:9/9:16, `mpd-quote-card-ep03-t2.py` (nuevo, copiado de `mpd-quote-card-ep02-t2.py`) para 4 quote cards.
- **2 bugs reales encontrados al inspeccionar visualmente cada imagen (no solo confiar en "el script corrió sin error"):**
  1. 16:9 — wordmark "MR. PUTRID'S DEN" quedaba superpuesto sobre el marco ovalado (el crop `y_center=0.55` heredado de EP02 no aplicaba a esta escena, cuyo marco está más arriba en el encuadre). Probé 4 valores de `y_center` (0.30/0.38/0.45/0.55) comparando visualmente; `0.30` dejó headroom limpio sobre el marco. Corregido y re-renderizado.
  2. 9:16 — el título (38 caracteres, más largo que el de EP02, "El rock y el diablo") se cortaba a la derecha ("...volvió inmorta" sin la "l") porque el piso del auto-fit de fuente heredado (`int(H*0.030)`) no dejaba bajar lo suficiente el tamaño. Confirmado con un test aislado en Python que el título nunca cabía en 908px de ancho disponible hasta bajar a 47px (`title_frac` ≈0.0245). Piso bajado a `0.018`. Corregido y re-renderizado.
- Ambos fixes verificados releyendo las imágenes corregidas antes de dar por bueno — títulos completos, sin superposición.
- Verificación de contenido prohibido: las 7 imágenes finales (3 portadas + 4 quote cards) inspeccionadas una por una — sin patrón de diana/círculos concéntricos, rostro consistentemente ilegible/disuelto en las 3 portadas.
- Quote cards: 4, verbatim contra `E:\Transcriptor\transcripciones\MPD EP 03.srt` (no del guion — timestamps y texto exacto de lo hablado): Q1 07:30 (el apodo se lo puso su madre), Q2 13:45 (Sgt. Pepper's), Q3 20:43 (Bowie), Q4 27:48 (fama).
- Archivos: `E:\Podcast\MPD\Temporada 2\EP 03\artwork\MPD-T2E03-PORTADA-3000.jpg`, `-16x9-FINAL.png`, `-9x16-FINAL.png`, `-Q1..Q4-1920x1080.png`.
- Resultado: OK — 7/7 imágenes con veredicto PASS tras corregir 2 rondas de bugs de composición. `artwork-ep03.md` actualizado a "producción final completa".

## Cierre de Macro-Stage B — checkpoint de Spotify resuelto
- Qué se hizo: Andrés entregó la URL de Spotify (pegada directo desde el navegador): https://open.spotify.com/episode/4CC5CsJPY75Wyg5Yd5RR6O?si=rWV9VInqRLOh84qBIS4nuQ. **Programado para publicarse el lunes 2026-08-17 a las 00:00 — NO está en vivo todavía** (hoy es 2026-08-15). `pipeline-state-ep03.md` y `roadmap-mpd.md` actualizados con la URL, marcada explícitamente como "programado, no verificar como live hasta esa fecha" para no repetir el patrón de declarar algo publicado sin comprobarlo.
- Resultado: OK — Stage B cerrado. Sigue Stage C: rotación del sitio (acumulación, ver `episode-pipeline/workflows/04-grid-rotation.md` § MPD) y deploy — este último NO se verifica contra Spotify hasta el lunes.

## Stage 4 — Sitio web (acumulación de Expedientes) + deploy
- Qué se hizo: agregada sección `.case` completa para Expediente 03 en `website/index.html` (siguiendo el patrón de acumulación de MPD, no rotación) — hero actualizado para apuntar a Expediente 03, embed de "Sintoniza" actualizado a la URL de Spotify de EP.03. Portada web optimizada generada (`ep03-cover.jpg`, 760×760, 75 KB, redimensionada desde la portada 3000×3000 final).
- **Timing consultado con Andrés antes de deployar:** el episodio está programado para el lunes 2026-08-17 00:00, no en vivo todavía — confirmó desplegar igual (el botón del show sigue funcionando aunque el episodio individual/embed no cargue hasta el lunes).
- Deploy-preflight corrido: proyecto verificado contra el host real (`vercel inspect` → `mr-putrids-den-web`, coincide con `project.json`), sin secrets, baseline 200 antes de deployar. `.vercel/output/static/` (index.html + ep03-cover.jpg) sincronizado a mano — proyecto usa `ignoreCommand: exit 0`, requiere flujo prebuilt.
- Deploy: `vercel deploy --prebuilt --prod` + `vercel alias set` a `www.mrputridsden.com` (el `--prod` solo no re-apunta el dominio custom).
- Verificado en producción: `curl` da 200, el HTML contiene "Expediente 03", el título del episodio y el ID de Spotify; `ep03-cover.jpg` sirve 200. **No verificado (a propósito):** que el embed/link de Spotify cargue — no va a funcionar hasta el lunes 00:00 por diseño, no es un bug.
- Commit + push a GitHub: `b32b63e`.
- Resultado: OK — EP.03 completo en el sitio y desplegado. Pendiente real: nada de mi lado — falta solo que Spotify libere el episodio el lunes.

## Stage 3b — Clip de audio para redes
- Qué se hizo: extraído del máster limpio (`MPD EP 03.wav`, 33:01.8) el momento "Mr. Crowley" — Don Airey grabando el órgano a solas + la cita de Ozzy "te acabas de conectar directo a mi cabeza, hermano" (24:47.9–25:29.9, verbatim del SRT real). `ffmpeg` con `-ss`/`-to` ANTES de `-i` (seek de entrada) para que el `afade` quedara relativo al clip, no al archivo completo — evita el bug documentado en `~/.claude/CLAUDE.md` § Instrumentos que mienten en silencio (EP.02, 2026-08-09). Fade in/out 0.5s.
- Verificado: 42.0s exactos, `volumedetect` -23.5 dB mean / -4.7 dB max (audio real, no silencio).
- Archivo: `E:\Podcast\MPD\Temporada 2\EP 03\artwork\social-clip\MPD-EP03-clip-mr-crowley.mp3`. `social-ep03.md` actualizado — checklist de assets ahora 4/4 completo.
- Resultado: OK

## Cierre — verificación en vivo (2026-08-20)
- Qué se hizo: retomada la sesión 3 días después del lanzamiento programado. Verificado con dos métodos independientes antes de declarar publicado: (1) WebFetch a la URL de Spotify confirmó título exacto "EP.03: La Bestia que el rock volvió inmortal", show "Mr. Putrid's Den", ~33 min, publicado lunes; (2) `curl -I` a la URL de Spotify dio 200.
- Encontrado: el sitio seguía mostrando "Disponible el lunes" en el hero (`file-status` del Expediente 03) — quedó stale desde el deploy del 2026-08-15. Corregido a "Ya disponible", sincronizado a `.vercel/output/static/`, redesplegado a producción (`vercel deploy --prebuilt --prod` + `vercel alias set`), verificado en vivo con `curl` que el texto nuevo está publicado.
- `pipeline-state-ep03.md` y `roadmap-mpd.md` actualizados — episodio marcado como publicado y verificado, stage_c: complete.
- Resultado: OK — EPISODIO CERRADO.
