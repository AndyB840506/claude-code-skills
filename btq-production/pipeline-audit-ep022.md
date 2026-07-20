# Pipeline Audit — BTQ EP.022

## Stage A — Roadmap y pre-producción

### Paso 1 — Confirmar episodio
- Andy confirmó el pilar SEO como dirección general en conversación (retomando el
  handoff de cierre de EP.021, que dejó el tema de EP.022 como pregunta abierta), y
  luego el ángulo P&L específico. Se presentaron 3 candidatos de métrica + teoría real
  citable (costo de rotación/Capital Humano de Becker, cost-to-serve/Service-Profit
  Chain de Heskett, costo de mala calidad/"Quality Is Free" de Crosby) vía
  AskUserQuestion — Andy eligió Crosby.
- Roadmap actualizado: fila EP.022 agregada a `roadmap-btq.md` con el tema confirmado,
  estado `en roadmap` → `guion listo` tras aprobación.

### Paso 2 — Guion
- Qué se hizo: `/btq-guion` no existe (confirmado, ver nota en `episode-pipeline`
  routing) — guion escrito directamente siguiendo `btq-production/guion-style-btq.md`.
  Investigación web previa para verificar todos los datos antes de escribir (regla 6):
  Philip Crosby / "Quality Is Free" (1979, ITT, costo de no conformidad ~20-25% de
  ventas), Samsung Galaxy Note 7 (2016, $5.300M, presión de cronograma vs. iPhone 7),
  SQM Group (costo de llamada repetida, ahorro por punto de FCR), PwC "Experience Is
  Everything" (2018, 32% abandona tras una mala experiencia, ~49% en LatAm), Peter
  Pronovost / Keystone Initiative Michigan (NEJM 2006, checklist de vía central),
  Boeing Model 299 / origen del checklist de vuelo (1935).
- Corrección durante la escritura: una primera versión incluía una cifra de horas de
  vuelo del B-17 en la Segunda Guerra Mundial sin verificar — se detectó antes de
  entregar y se reemplazó por el dato real y verificado (12.731 unidades construidas,
  tercer bombardero más producido de la historia).
- Publicado como Artifact (copia sin `<!DOCTYPE>/<html>/<head>/<body>`, mismo `<style>`
  + `<div class="container">`) para revisión de Andy — aprobado sin cambios.
- Lint aplicado: 4.674 palabras contadas (p.line + remate + dato + sub) → ~42.2 min a
  150 wpm + expansión 35.5%, dentro de 40-45 min. 3 REMATE (máx 3-4). Refrán central
  ("la calidad es gratis") 3 veces en el guion hablado, cada una con función narrativa
  distinta (tease en el Hook, cita del título del libro, cierre canónico) — dentro del
  máx 3. 0 "imagínense", 0 "me vuela la cabeza". Sin bloque "Mito o Realidad" aparte.
  Sin meta-anuncios de estructura.
- Archivos generados: `btq-production/launch-assets/EP022-costo-calidad-guion.html`
- Resultado: OK — aprobado por Andy 2026-07-14

### Paso 3 — Prompts de artwork
- Qué se hizo: mismo desafío que EP.020 (pilar SEO sin referente pop) — se buscó un
  símbolo literal del propio contenido del episodio en vez de un patrón decorativo
  desconectado, siguiendo el precedente documentado en
  `EP020-metricas-artwork-v3.md`. Elegido: un patrón de checklist/checkboxes dorados
  (el episodio gira en torno a checklists — Pronovost, Boeing, Aplicable Hoy #2), con
  un checkbox final deliberadamente sin marcar como el gancho visual. Figura: la
  supervisora de QA de la escena de apertura del guion (Ana), de espaldas, hombro con
  el monitor de revisión de llamadas. Se mantiene el veto de círculos/anillos/diana
  vigente desde EP.021 (brand-constants.md §3).
- Archivos generados: `btq-production/launch-assets/EP022-costo-calidad-artwork-v3.md`
  (prompts 1:1 y 16:9 completos; 9:16 queda para derivar del 1:1 aprobado, mismo patrón
  de adaptación de episodios previos — no generado en este documento)
- Resultado: OK — prompts listos, pendiente generación real en Flow por Andy (no
  bloqueante para cerrar Stage A, igual que el patrón de episodios anteriores)

### Paso 4 — Archivo de estado
- Qué se hizo: `pipeline-state-ep022.md` creado, `roadmap-btq.md` actualizado a
  `guion listo`.
- Resultado: OK — pausa natural, esperando grabación

### Extra — pruebas de artwork local (ComfyUI, adelantadas antes de la grabación)
- Qué se hizo: a pedido de Andy, se probó generar la portada 1:1 localmente (D:\AI,
  Z-Image Turbo) en vez de Flow, para validar la dirección visual antes de grabar.
  - v1 (escena completa con prompt customizado): quedó con tono cálido tipo "foto de
    oficina", lejos del void-black + rim light dorado que pide la marca. FAIL parcial.
  - v2 (prompt ajustado: cuarto en negro total, monitor en dark-mode con glow dorado,
    un checkbox final claramente vacío entre 4 marcados): PASS — validó la dirección
    conceptual (checklist como símbolo literal, mismo criterio que la diana de EP.020).
  - Prueba de tipografía completa en un solo prompt (bloque congelado con nombres de
    íconos, a pedido de Andy citando su experiencia en EP.21): los íconos de la fila 1
    (Facebook/Instagram/TikTok) salieron reconocibles y a color, pero TODO el texto
    horneado por el modelo salió con typos ("BEHIND THE QEQUE", "Behind the Queve",
    "Mada Calidad") y faltó la fila 2 de íconos. Confirmado y corregido según feedback
    de Andy.
  - Solución híbrida: íconos de plataforma generados en una imagen aparte (fondo negro
    puro, sin texto/escena) — 4/4 variantes del batch salieron limpias, ambas filas
    completas. Compuestos con PIL sobre la escena v2 junto con todo el texto (wordmark,
    BTQ, título, EP.22) vía plantilla nueva `comfyui/templates/portada-compose.py`
    (recorte automático por bounding-box del strip de íconos).
  - 2 rondas de ajuste de tamaño de tipografía dorada (BTQ/EP.22) a pedido de Andy —
    de ~0.022×H a ~0.040×H (BTQ) y ~0.050×H (EP.22).
  - Técnica documentada en memoria `btq_local_portada_hybrid_typography` para
    reutilizar en futuras portadas BTQ locales.
- Archivos finales copiados a `D:\Podcast\BTQ\EP 22\BTQ Artwork EP 22\`:
  `BTQ-EP022-COVER-1x1-approved.png` (aprobada por Andy), `BTQ-EP022-COVER-1x1-scene-only.png`
  (escena sin tipografía, por si se necesita recomponer), `BTQ-icon-strip-source.png`
  (fuente de íconos recortable para reutilizar en 16:9/9:16 y futuras portadas).
- Pendiente: escalar a 3000×3000 real (test corrió a 1024×1024); derivar 16:9 y 9:16
  con el mismo criterio cuando se necesiten.
- Resultado: OK — Andy aprobó el resultado final ("Asi quedo perfecto")

### Extra 2 — escalado a producción + 16:9 + 9:16 (escritorio, 2026-07-15)
- Los archivos de prueba aprobados vivían solo en D:\ (portátil); el escritorio (E:\AI,
  RTX 3080 Ti) no tenía acceso a ellos. A pedido de Andy, se regeneró todo desde cero en
  vez de transferir archivos manualmente.
- 1:1: escena nativa 1536×1536 (2 iteraciones — v1 salió con figura masculina y último
  checkbox como cuadro sólido en vez de vacío; v2 corrigió género y contraste del
  checkbox; v3 redujo un patrón de fondo tipo circuito que competía con el texto) →
  RealESRGAN_x4plus → resize a 3000×3000 exacto (verificado con PIL). Tira de íconos
  generada en batch de 4, las 4 limpias, se usó la variante #3 (fondos más consistentes).
  Compuesto con `portada-compose.py`. Aprobado por Andy.
- 16:9: escena nueva nativa 1920×1080 (2 iteraciones — v1 salió con checklist en dos
  columnas y varios casilleros vacíos dispersos, diluyendo el chiste visual; v2 forzó
  una sola columna de 7 casillas con solo la última vacía). Tipografía compuesta con
  plantilla nueva `comfyui/templates/cover-16x9-compose.py` (título+subtítulo alineados
  a la izquierda, sin footer, fuente dinámica). Aprobado.
- 9:16: 2 intentos de generar la escena de cero fallaron en controlar la composición
  extrema (figura ocupando la mitad/base del frame en vez del tercio superior, con negro
  abajo). Se cambió de estrategia: derivar del recorte superior de la escena 1:1 YA
  aprobada + relleno de negro de marca exacto (10,10,10) por PIL, sin generar de nuevo —
  0 riesgo de reintroducir errores ya corregidos (género, checkbox, íconos extra).
  Primer intento de composición dejó el wordmark superpuesto sobre la cabeza/monitor
  porque el recorte no dejaba suficiente margen negro arriba; corregido con un offset
  vertical antes de pegar la escena. Aprobado en la segunda versión.
- **Bug encontrado y corregido en `portada-compose.py`**: la tira de íconos se pegaba de
  forma opaca sobre el footer; su propio fondo (0,0,0) no coincidía con el negro del
  footer (10,10,10), dejando una caja rectangular visible (detectado por Andy en la
  entrega del 1:1). Fix: máscara de alfa derivada de `ImageChops.difference` contra
  negro puro, así solo los píxeles de ícono se componen y el footer se ve continuo.
  Verificado con muestreo de píxeles (footer y huecos entre íconos leen exactamente
  10,10,10 tras el fix). Aplica retroactivamente a cualquier portada futura que use la
  plantilla.
- Archivos finales en `E:\Podcast\BTQ\EP 22\BTQ Artwork EP 22\`: `BTQ-EP022-COVER-1x1-approved-3000.png`,
  `BTQ-EP022-COVER-16x9.png`, `BTQ-EP022-COVER-9x16.png`, más `-scene-only-3000.png` y
  `BTQ-icon-strip-source.png` de respaldo.
- Resultado: OK — 3 variantes aprobadas por Andy.

## Stage B — Post-grabación

### Stage 0 — Intake
- Qué se hizo: Andy reportó grabación lista en `E:\Podcast\BTQ\EP 22\BTQ EP 22.mp3`
  (viernes 2026-07-17, según lo planeado). Episode brief armado sin repreguntar —
  título, cultural_ref, closing TM y fuentes ya estaban resueltos en el guion
  aprobado (`EP022-costo-calidad-guion.html`) y en `pipeline-state-ep022.md`.
- Resultado: OK — brief completo, arranca transcripción.

### Stage 1 — Transcripción
- Qué se hizo: audio copiado a `E:\Transcriptor\audios\BTQ EP 22.mp3` (41.1MB),
  WhisperX large-v2 + diarización (es), corrido en background (proceso completó
  exit 0, log revisado línea por línea — contenido del transcript coincide con el
  guion aprobado, duración real ~42.5 min consistente con el estimado de 42.2 min).
- Archivos generados: `E:\Transcriptor\transcripciones\BTQ EP 22.srt` (49.173 bytes)
- Resultado: OK

### Stage 2 — Generación de assets
- Qué se hizo: `episode-launch` invocado con los 6 inputs resueltos desde el episode
  brief (sin repreguntar) — SEO Spotify, plan social 4 días, metadata YouTube (11
  capítulos con timestamps reales del SRT), y checklist de verificación del cover-art
  (ya generado y aprobado en Stage A local, no se re-generaron prompts ni se pasó por
  Stage 3 estándar de Flow). Fact-check de entidades reales dichas al aire vs. fuentes
  del guion — sin errores. Chequeo de consistencia título/tagline entre guion, metadata
  y artwork — documentado, sin conflicto real (artwork recorta "en Call Center" por
  espacio, campo SEO lo mantiene para búsqueda).
- Archivos generados: `btq-production/launch-assets/EP022-costo-calidad-launch.md`
- Gate heredado: aprobado por Andy sin ajustes
- Checkpoint Spotify: confirmado 2026-07-20 — https://open.spotify.com/episode/6ewMTUO0FGNxfIMS0u55Yu
- Resultado: OK — commit + push hechos (e6f8171)

### Stage 3 (parcial) — Verificación de cover-art ya existente
- Qué se hizo: al cerrar sesión, releídas las 3 imágenes finales con `Read` (no solo
  confiar en la aprobación previa de Stage A) — detectado un patrón de circuito/PCB
  dorado en la esquina superior derecha de 1:1 y 9:16, ausente en 16:9. Viola
  `brand-constants.md` §Reglas #3 ("PCB/circuits: ONLY for AI/tech episodes — NEVER on
  general covers") — EP.022 no es un episodio de tecnología. No fue detectado en las
  rondas de aprobación de Stage A.
- Resultado: FAIL parcial (1:1, 9:16) / PASS (16:9) — Andy eligió "corregir con parche
  PIL" (AskUserQuestion). Corregido: relleno de negro de marca con grano sutil sobre la
  zona del circuito (esquina superior derecha), narrow left-seam blend para evitar
  costura visible; figura, checklist en pantalla, texto y footer sin tocar. Originales
  respaldados como `BTQ-EP022-COVER-1x1-approved-3000 (pre-pcb-fix backup).png` y
  `BTQ-EP022-COVER-9x16 (pre-pcb-fix backup).png`. Re-verificado visualmente con `Read`
  tras el parche — PASS en las 3 imágenes.

## Stage 3 — Validación de imágenes (formal, 2026-07-20)
- Qué se hizo: Spotify confirmado por Andy (episode/6ewMTUO0FGNxfIMS0u55Yu), checkpoint
  cerrado. Set ya existente (generado en Stage A, corregido en el hallazgo de arriba) —
  releídas las 3 imágenes con `Read` y aplicado el checklist formal de
  `episode-launch/docs/brand-constants.md` (no existe `btq-project/workflows/artwork.md`).

### Ronda 1 (única — el fix del PCB ya se hizo antes de este stage formal)
- Imagen 1:1   → Regla de margen: PASS (tipografía en tercio superior/inferior, sujeto+monitor en tercio central) · Split-scene: N-A · Referencia oficial: N-A (personaje original) → PASS
- Imagen 16:9  → Regla de margen: PASS (título en tercio izquierdo negro, figura en el resto) · Split-scene: N-A · Referencia: N-A → PASS
- Imagen 9:16  → Regla de margen: PASS (escena en tercio superior, título+footer en tercio inferior) · Split-scene: N-A · Referencia: N-A → PASS
- Resultado: OK — 3/3 imágenes con veredicto PASS

## Stage 3b — Material de marketing
- Qué se hizo: plan social ya venía de Stage 2 (episode-launch), sin regenerar — solo
  confirmado. Quote cards: Andy eligió "generar ahora (local)" (AskUserQuestion) — 3
  REMATE del guion (Hook/Ana, Samsung, hospital+avión). Escenas vía ComfyUI local
  (Z-Image Turbo, 960×1080, void black + rim light dorado, formato 16:9 desde EP.021).
  **2 rondas de fallos de patrón vetado antes de aprobar:** ronda 1 (CARD1/CARD2)
  reinsertó el anillo/diana concéntrico vetado (mismo patrón de falla que Flow, ahora
  confirmado también en generación local) — CARD3 salió con texto ilegible/mal escrito
  en el clipboard ("Pre Filelt"). Ronda 2 con prohibición reforzada: CARD2 quedó limpio,
  CARD1 mejoró pero la tela del cubículo tenía una textura de mini-círculos repetidos
  (detectado con zoom, no a simple vista) — ronda 3 forzó un divisor de metal liso sin
  textura, PASS. CARD3 ronda 2 ya salió limpio (líneas en blanco, sin texto legible).
  Citas verificadas verbatim contra la transcripción real (Stage 1) antes de componer —
  las 3 coinciden con lo dicho al aire (con limpieza aprobada de muletillas/conectores).
  Texto compuesto con PIL (`quote-card-compose.py`, invocado vía script Python con
  strings literales para no perder tildes por escaping de shell) — verificado letra por
  letra y seam de composición muestreado a nivel de píxel (10,10,10 exacto en los 3).
- Archivos generados: `E:\Podcast\BTQ\EP 22\BTQ Artwork EP 22\BTQ-EP022-CARD1-16x9.png`,
  `BTQ-EP022-CARD2-16x9.png`, `BTQ-EP022-CARD3-16x9.png`
- Resultado: OK — 3/3 quote cards aprobadas

## Stage 4 — Rotación de grid
- Qué se hizo: grid BTQ rotado de `020,019,018,017` a `021,020,019,018` — EP.021 (en
  circulación antes de este lanzamiento) entra al grid al principio (orden descendente
  BTQ), EP.017 sale. URL de EP.021 ya estaba registrada (badge "última pista"), reusada
  tal cual. Badge "última pista"/hero actualizado a EP.022 (lt-n, lt-k, lt-t, href).
- Episodio que entra: EP.021 | Episodio que sale: EP.017
- Archivo modificado: `btq-production/website/index.html`
- Resultado: OK

## Stage 5 — Deploy + verificación
- Qué se hizo (Paso 1, preflight): proyecto Vercel `website` confirmado (projectId/orgId
  en `btq-production/website/.vercel/project.json`, sin colisión con MPD), directorio +
  `vercel.json` válidos (sin `ignoreCommand` — flujo estándar), sin secrets expuestos,
  baseline de producción HTTP 200 (host confirmado Vercel).
- Resultado preflight: PASS
- Qué se hizo (Paso 2, gate): resumen pre-deploy presentado a Andy — aprobado ("Si
  hagamos deploy"). Andy confirmó que el plan social ya quedó programado en Meta por
  fuera del pipeline.
- Qué se hizo (Paso 3, deploy): `vercel --prod` desde `btq-production/website/` →
  aliased a `https://behind-thequeue.com` (deployment `dpl_EWJ7oXedxm3rUHmWBCFtMoV5yw6E`).
- Qué se hizo (Paso 4, verificación HTTP): `curl` con cache-bust → HTTP 200, contenido
  confirmado en vivo (no caché viejo): badge `lt-n">022<`, grid `t-num">021<`, URL de
  Spotify de EP.022 presentes en el HTML servido.
- Qué se hizo (Paso 5, verificación Spotify): WebFetch contra la página pública del show
  → EP.22 aparece primero en el listado, título coincide exacto con la metadata generada.
- URL verificada: https://behind-thequeue.com → HTTP 200
- Verificación Spotify: PASS — episodio encontrado en la página del show
- Resultado: OK — episodio publicado y verificado en vivo
