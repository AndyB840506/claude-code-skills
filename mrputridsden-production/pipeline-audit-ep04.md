# Bitácora — EP.04 (MPD) "Paul is Dead"

## Stage A — Roadmap y pre-producción (2026-08-20)

- **Qué se hizo:** episodio confirmado desde el compromiso anunciado al aire en el
  cierre de EP.03 (banco-expedientes.md #3, ángulo Fred LaBour/Michigan Daily 1969
  ya verificado). Guion completo escrito (3 rondas de investigación: Wikipedia "Paul
  is dead" completo, comparativa de "dobles" moderna pedida por Andrés — Avril
  Lavigne/Melissa Vandella, teoría reptiliana, video viral de Justin Bieber).
  Word count verificado programáticamente: 4.452 palabras host-text (~35 min
  estimados), aprobado as-is por Andrés pese a quedar bajo el piso editorial de 40 min.
  Prompts de artwork generados y validados en ComfyUI local (1024×1024, Z-Image
  Turbo) — 4 rondas de iteración (ver `episodios/temporada-2/artwork-ep04.md`),
  escalado a producción final (3000×3000 1:1, 1920×1080 16:9, 1080×1920 9:16).
- **Corrección durante la sesión (roadmap):** se detectó y corrigió un error propio
  antes de comprometerlo — se propuso inicialmente anunciar "Crowley" como próximo
  expediente sin verificar que ya se había usado en EP.03; y luego se propuso
  "pánico satánico ampliado" sin verificar que ya se cubrió entero en EP.02
  (confirmado abriendo el script real, no de memoria). Decisión final: el cierre de
  EP.04 NO anuncia próximo expediente.
- **Corrección durante la sesión (artwork):** el primer concepto aprobado (espejo
  antiguo) se descartó después por feedback de Andrés — se parecía demasiado a
  EP.03 a primera vista. Andrés pidió luego un retrato fotorrealista de Paul
  McCartney en primer plano y, al bloquearlo, pidió explícitamente "hacer override"
  de la restricción vía el prompt de ComfyUI — se rechazó: nombrar a una persona
  real y viva en el prompt no reduce el riesgo de derechos de imagen, lo aumenta, y
  el bloqueo no es una restricción técnica de Claude que se pueda esquivar
  redactando distinto. Se ofreció y ejecutó una alternativa (foto genérica dañada,
  no un retrato reconocible) que también falló técnicamente — el modelo devolvió un
  rostro completo y nítido, repitiendo un patrón de fallo ya documentado en EP.03.
  Concepto final: periódico enmarcado (sin ningún rostro), 2 rondas hasta reducir el
  pseudo-texto del titular a un nivel invisible a tamaño real (150px, verificado).
- **Archivos generados:**
  - `scripts/EP04-paul-is-dead.html` + `.artifact.html` (Artifact publicado)
  - `episodios/temporada-2/artwork-ep04.md`
  - `E:\Podcast\MPD\Temporada 2\EP 04\artwork\MPD-T2E04-PORTADA-3000.jpg` (+16x9, +9x16)
  - `pipeline-state-ep04.md` (este archivo lo acompaña)
- **Resultado:** OK — pausa natural, esperando grabación. Commiteado y pusheado.

## Stage 0 — Intake (2026-08-23)

- **Qué se hizo:** episode brief armado desde artefactos de Stage A ya aprobados
  (guion, artwork-ep04.md, roadmap-mpd.md fila EP.04) — sin re-preguntar datos ya
  cerrados. Audio confirmado en disco: `E:\Podcast\MPD\Temporada 2\EP 04\MPD EP 04.mp3`,
  31:53 real (ffprobe), consistente con el guion (~35 min estimados). Numeración
  verificada contra `roadmap-mpd.md` (regla del número único desde EP.02): público =
  interno = "EP.04".
- **Resultado:** OK — brief completo, arranca transcripción.

## Stage 1 — Transcripción (2026-08-23)

- **Qué se hizo:** transcripción con diarización (large-v2, es, srt) vía WhisperX
  en background (detached process, PID 2720). Warning de `torchcodec` presente
  en el log — documentado como inofensivo en `transcriptor/docs/environment.md`.
  Última línea real termina en 00:31:35 contra 31:53 de audio total (brecha de
  18s, consistente con outro/silencio — no hay señal de alucinación de boilerplate).
- **Archivos generados:** `E:\Transcriptor\transcripciones\MPD EP 04.srt`
- **Resultado:** OK

## Stage 2 — Generación de assets (2026-08-23, en curso)

- **Qué se hizo:** show notes (`podcast-creator/05-show-notes.md`) y metadata de YouTube
  (`07-youtube.md`) generadas a partir del guion aprobado + timestamps REALES extraídos
  del SRT (no de los rangos estimados del guion, que apuntaban a 43 min contra los 31:53
  reales — ver nota en cada archivo). Capítulos de YouTube verificados con las 3 reglas
  duras (00:00 inicial, ≥3 capítulos, cada uno ≥10s incluido el último: 28s). Chequeo de
  consistencia título/tagline (guion/metadata/artwork) — los tres usan "Paul is Dead" sin
  discrepancia, a diferencia de lo que pasó en EP.005.
  Artwork: ya cerrado en Stage A (`artwork-ep04.md`), no se regenera.
- **Archivos generados:**
  - `episodios/temporada-2/ep04-metadata.md` (Artifact: https://claude.ai/code/artifact/71ed2f0c-c970-4211-87a9-77cfec74f658)
  - `episodios/temporada-2/youtube-ep04.md` (Artifact: https://claude.ai/code/artifact/d08dba07-0dcc-4084-917b-aad172a68e06)
- **Pendiente:** `04-social-media.md` — falta fecha/hora de publicación (Paso 1, pregunta 3)
  para calcular el plan de 3 días; no es dato derivable de ningún archivo. Nota de
  continuidad: el cierre de EP.03 (ya en vivo) YA anunció el tema de EP.04 al aire —
  cita exacta en `banco-expedientes.md` #3 ("la vez que medio mundo se convenció de que
  Paul McCartney estaba muerto, y armó las pruebas usted mismo, disco por disco"). El
  plan social NO puede abrir el Día 1 con ese mismo gancho (ya quemado, publicado desde
  2026-08-17) — debe abrir con algo que ese cierre NO reveló: el giro (parche/detalle que
  ni Paul explica) o los dobles modernos (Avril/reptilianos/Bieber).
- **Plan social:** generado tras confirmar con Andrés — publicación planeada lunes
  2026-08-24. Verificado que hoy es domingo 2026-08-23 (no asumido) antes de calcular
  fechas — con solo 1 día de antelación real (no 2), el plan estándar de 3 días se
  comprimió a 2 (Intriga+Contenido fusionados en Día 1, Lanzamiento en Día 2).
- **Checkpoint Spotify:** Andrés pegó una URL (episode/6oddT7be7iK4Ikgh0Hwith) que se
  verificó con `curl` — dio 404 real ("Page not found"), confirmado con Andrés que el
  episodio efectivamente NO está publicado todavía. Se descartó la URL y se dejó
  `spotify_url: pending`. Instancia de §Procedencia — nunca grabar una URL de un
  artefacto irreversible sin abrirla primero.
- **Archivos generados (completos):**
  - `episodios/temporada-2/ep04-metadata.md` (Artifact: https://claude.ai/code/artifact/71ed2f0c-c970-4211-87a9-77cfec74f658)
  - `episodios/temporada-2/youtube-ep04.md` (Artifact: https://claude.ai/code/artifact/d08dba07-0dcc-4084-917b-aad172a68e06)
  - `episodios/temporada-2/social-ep04.md` (Artifact: https://claude.ai/code/artifact/bb74917a-17a8-4d64-bb97-9474cd4efa1e)
- **Resultado:** OK — Stage B (Macro-Stage post-grabación) completa. `spotify_url` sigue
  `pending`; la próxima invocación del pipeline se detiene a pedirla (00-intake.md Paso 0)
  antes de avanzar a Stage C.

## Stage 3 — Validación de imágenes (2026-08-23)

- **Qué se hizo:** las 3 imágenes finales de Stage A ya existían — no se regeneraron.
  Leídas directamente con `Read` (no se saltó el paso ni se confió en la aprobación
  previa de Andrés, por la regla de `03-image-validation.md` contra la "faja" de BTQ
  EP.022). Reglas aplicadas: rostros reconocibles (prohibido), simbología ocultista
  (prohibido), paleta "La Guarida", identidad del show legible, texto PIL letra por
  letra, footer de plataformas.
- Imagen 1:1  → Rostros: PASS (ninguno) · Ocultismo: PASS (ninguno) · Paleta: PASS ·
  Texto: PASS (sin typos) → **PASS**
- Imagen 16:9 → mismos chequeos, reflow correcto → **PASS**
- Imagen 9:16 → mismos chequeos, reflow correcto → **PASS**
- Pseudo-texto del periódico (gibberish): presente, pero es un tradeoff ya documentado
  y verificado en Stage A (2 rondas hasta reducirlo a invisible a 150px) — no se
  re-litiga, solo se confirma que sigue así.
- **Resultado:** OK — 3/3 PASS en ronda única, sin necesidad de regenerar.

## Stage 3b — Material de marketing (2026-08-23)

- **Qué se hizo:** plan social ya generado en Stage 2 (`social-ep04.md`), confirmado
  con Andrés (publicación lunes 2026-08-24, plan comprimido a 2 días). Quote cards: no
  existía set previo (verificado listando la carpeta de artwork antes de generar, no
  se preguntó porque la evidencia ya estaba a mano). Generadas 4 cards 1920×1080 vía
  `comfyui/templates/mpd-quote-card-ep04-t2.py` (nuevo, copiado de la plantilla real de
  EP.03 — la nota de la plantilla del pipeline sobre paleta "silver/crimson" está
  desactualizada, T2 usa "La Guarida" navy/brass; se siguió el precedente real de
  EP.03, no la nota stale). Las 4 citas se verificaron verbatim contra el SRT real
  (`MPD EP 04.srt`), con una sola limpieza: "Fred Labor" → "Fred LaBour" (error de
  transcripción ASR del apellido, no edición de contenido). Timestamps: 01:56, 08:01,
  19:07, 24:52 — repartidos a lo largo del episodio, y_center variado (0.30/0.38/0.45/0.52)
  para no repetir encuadre. Las 3 imágenes leídas visualmente tras generar: texto
  correcto, sin rostros ni símbolos prohibidos, paleta correcta.
- **Corrección aplicada:** el plan social (`social-ep04.md` Día 2) citaba una versión de
  3 frases de la Q4; el card renderizado solo usa 2 (el `fit()` automático no truncó
  nada — el texto en `QUOTES` ya era de 2 frases). Se corrigió el copy del plan social
  para que coincida letra por letra con el card, evitando el mismo error de EP.021
  (caption citando el crudo en vez de la imagen final).
- **Archivos generados:**
  - `comfyui/templates/mpd-quote-card-ep04-t2.py`
  - `E:\Podcast\MPD\Temporada 2\EP 04\artwork\MPD-T2E04-Q1..Q4-1920x1080.png`
- **Clip de audio:** generado desde el máster limpio (`MPD EP 04.wav`, no el mp3
  comprimido) — momento "la maquinaria nunca se apagó" (24:38.0–25:26.5, 48.5s),
  arco autocontenido que cierra justo antes del giro hacia Avril Lavigne (gancho
  natural al episodio completo). `-ss`/`-t` puestos ANTES de `-i` (evita el bug de
  timing de `afade` ya documentado — fade relativo al clip, no al archivo completo).
  Verificado con `volumedetect`: -20.6 dB mean, -2.2 dB max — audio real, no silencio
  (consistente con el precedente de EP.03, -23.5 dB).
- **Archivo:** `E:\Podcast\MPD\Temporada 2\EP 04\artwork\social-clip\MPD-EP04-clip-maquinaria.mp3`
- **Resultado:** OK — plan social + 4 quote cards + clip de audio, los 3 assets de
  marketing completos.

## Stage 4 — Sitio web (2026-08-23, BLOQUEADO)

- **Qué se hizo:** se leyó `04-grid-rotation.md` — MPD usa acumulación de expedientes,
  no rotación de grid (decisión 2026-08-14). Paso 0 exige `spotify_url` real ANTES de
  tocar el markup (nunca escribir "pending" en un `href` publicado). `spotify_url`
  sigue `pending` (ver Stage 2 — la URL que pegó Andrés dio 404 real, descartada).
- **Resultado:** BLOQUEADO — no se editó `website/index.html`. Pausa intencional, no
  olvido: retomar cuando Andrés confirme la URL pública de Spotify. En ese momento
  también anotar el `.file-status` del hero ("Disponible el lunes" → "Ya disponible")
  explícitamente, no asumir que confirmar el link cubre ese copy (mordió en EP.03).
