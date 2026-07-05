# Pipeline Audit — BTQ EP.020

## Stage 0 — Intake
- Qué se hizo: episode brief construido desde handoff + guion aprobado (show, audio, datos del episodio) — no se repreguntó nada ya resuelto en `pipeline-state-ep020.md` ni en el guion.
- Resultado: OK

## Stage 1 — Transcripción
- Qué se hizo: transcripción con diarización (large-v2, es, srt)
- Archivos generados: E:\Transcriptor\transcripciones\BTQ EP 20.srt
- Resultado: OK

## Stage 1b — Re-transcripción (fix de timing intro/outro)
- Qué se hizo: Andy detectó que el intro/outro musical tenía un problema de timing que
  extendió y corrió todos los números del episodio; reexportó el audio (mismo path,
  tamaño cambió 44.2MB → 42.9MB). SRT anterior respaldado como
  "BTQ EP 20 (pre-fix backup).srt". Re-transcripción con los mismos parámetros (large-v2, es, diarize, srt).
- Impacto: invalida los timestamps de capítulos de YouTube y de las 4 quote cards en
  EP020-metricas-launch.md (generados antes del fix) — el contenido/texto de los assets
  no cambia, solo hay que recalcular los tiempos contra el SRT nuevo.
- Resultado: OK — SRT nuevo generado (`BTQ EP 20.srt`, ~44min38s), timestamps de capítulos
  YouTube y de las 4 quote cards recalculados en EP020-metricas-launch.md contra el SRT
  corregido (shift de ~-37s en la mayoría de marcadores, algunos con variación mayor por
  diferencias naturales de frase exacta elegida como ancla).

## Stage 2 — Generación de assets
- Qué se hizo: `episode-launch` invocado con los 6 inputs desde el episode brief/handoff
  (sin repreguntar); generó Spotify SEO, plan social 4 días, metadata de YouTube y quote
  cards. Cover-art no se regeneró — ya estaba generado y aprobado en Stage A.
- Fact-check: detectado y corregido un lapsus de atribución al aire ("Madeline Statham" /
  "Marilyn Statham" según la transcripción) — el nombre correcto (Marilyn Strathern, 1997)
  se usa en todos los assets públicos.
- Archivos generados: btq-production/launch-assets/EP020-metricas-launch.md
- Gate heredado: aprobado por Andy 2026-07-04
- Checkpoint Spotify: resuelto 2026-07-05 — https://open.spotify.com/episode/6gRVIWVI3jBUAJarLJ7AsQ?si=50f8830a8029439f
- Resultado: OK — 3 prompts de cover-art ya resueltos en Stage A (no quedan pendientes para Stage 3)

## Stage 3 — Validación de imágenes (cover-art)
- Qué se hizo: heredado de Stage A — 3 imágenes (1:1, 16:9, 9:16) ya generadas y aprobadas, checklist completo pasado.
- Resultado: OK — no requiere nueva validación

## Stage 3b — Material de marketing (quote cards)

### Ronda 1
- Andy generó las 4 quote cards en Flow. Revisión visual: Q1 (termómetro) siguió el
  prompt aprobado pero en el estilo antiguo "graphic editorial poster — NOT
  photorealistic 3D"; Q2/Q3/Q4 volvieron como variantes casi idénticas de la escena de
  portada (agente de contact center de espaldas, dashboard, título "MÉTRICAS Y KPIs")
  en vez de sus escenas individuales (diana con anillo deformado, ventanilla bancaria,
  escritorio vacío).
- Veredicto: FAIL — 0/4 coinciden con la dirección visual pedida.
- Acción: Andy pidió el mismo tratamiento cinematográfico/con volumen real que la
  portada para las 4 quote cards, reemplazando el estilo "graphic editorial poster"
  usado desde EP.017. Decisión registrada como regla nueva en
  `episode-launch/docs/brand-constants.md` §Quote Cards (retroactiva desde EP.020).
  Los 4 prompts reescritos completos (nunca fragmento parcial) en
  `EP020-metricas-launch.md` §E con el bloque cinematográfico + checklist actualizado.
- Resultado: prompts corregidos, pendiente de que Andy regenere las 4 en Flow y pase
  las rutas para nueva revisión (Ronda 2).

### Ajuste previo a Ronda 2 — variedad de fondo
- Andy notó que, sin el anillo dorado, Q1 y Q2 quedaban como un objeto flotando en
  negro puro sin contexto — arriesgaba verse repetitivo entre las 4 cards. Se agregó a
  cada prompt un elemento de fondo distinto y desenfocado (profundidad de campo),
  relevante al tema de esa cita específica, sin volver al anillo genérico:
  Q1 bullpen de contact center desenfocado, Q2 pared de medidores analógicos, Q3
  display de turnos visible tras el vidrio, Q4 fila de escritorios igualmente vacíos.
  Regla documentada en `episode-launch/docs/brand-constants.md` §Quote Cards para
  futuros episodios.

### Ronda 2
- Andy generó 3 de las 4 (falta Q1 termómetro). Revisión visual directa:
  - Q2 (Arrow_hitting_archery_target...) → PASS. Cinematic, textura de metal
    real/grietas, texto correcto, atribución correcta a Strathern. Fondo se resolvió
    como polvo/luz radiante en vez de "pared de medidores" — cumple el objetivo
    (profundidad, no vacío plano) aunque no literal al prompt; aprobado igual.
  - Q3 (Bank_teller_counter_window_empty...) → FAIL. El fondo tras el vidrio muestra
    un anillo concéntrico dorado grande — exactamente el motivo genérico que se
    decidió retirar de todas las cards salvo Q2. Debía mostrar un display de turnos.
  - Q4 (Empty_desk_with_target_rings...) → FAIL, dos fallas: (a) mismo problema de
    anillo concéntrico de fondo en vez de la fila de escritorios vacíos pedida (el
    propio nombre de archivo lo delata: "target_rings"); (b) texto renderizó
    "NÚMERO" con tilde, viola la regla sin-tildes (spec pedía "NUMERO").
  - Q1 (termómetro): no generada en este batch — pendiente.
- Acción: prompts de Q3 y Q4 reescritos completos (nunca fragmento parcial) con (1)
  instrucción explícita "DO NOT render any concentric ring/circle/target pattern —
  reserved exclusively for [Q2]" y (2) para Q4, nota de ortografía reforzada
  aclarando que "NUMERO"/"TERMOMETRO" sin tilde es estilización deliberada, no error
  a autocorregir.
- Resultado: pendiente Ronda 3 — Andy debe regenerar Q3 y Q4 con los prompts
  corregidos, y generar Q1 (nunca producida). Q2 queda aprobada.

- Q1 (Thermometer_heating_signal_gold...) generada y revisada → FAIL. Mismo patrón
  que Q3/Q4: en vez del bullpen desenfocado pedido, el fondo muestra un anillo
  concéntrico dorado — tercera card consecutiva (de 4) donde Flow reemplaza el fondo
  pedido por el motivo genérico de diana. Resto de la card correcta (render
  fotorrealista, texto exacto sin tildes, mitad negra limpia).
- Patrón identificado: el motivo de anillo parece estar fuertemente asociado a BTQ en
  el modelo (por las portadas previas) y se cuela incluso cuando se pide otro fondo
  explícitamente. Se aplicó a Q1 el mismo bloque "DO NOT render any concentric
  ring/circle/target pattern" ya agregado a Q3/Q4.
- Resultado: Ronda 3 pendiente para las 3 (Q1, Q3, Q4) con el ban explícito de
  anillos. Q2 sigue aprobada (es la única donde el anillo es el sujeto correcto).

### Ronda 3
- Q1 (Thermometer_heating_in_black...) regenerada → PASS. El ban explícito de
  anillos funcionó: fondo ahora muestra el bullpen de contact center desenfocado
  pedido, sin anillo. Render fotorrealista correcto, texto exacto sin tildes, mitad
  negra limpia. **Q1 aprobada.**
- Q3 y Q4: Andy aún no las ha regenerado (archivos con timestamp sin cambios desde
  Ronda 2) — pendientes con los prompts ya corregidos (ban de anillos + nota de
  ortografía en Q4).
- Resultado: 2/4 aprobadas (Q1, Q2). Pendiente Q3 y Q4.

### Ronda 4
- Andy regeneró las 4 (incluida Q2, ya aprobada). Revisión visual:
  - Q2 (Arrow_in_archery_target...) → PASS, mejor que Ronda 1: ahora sí muestra la
    pared de medidores/gauges de fondo tal como pedía el prompt (antes era polvo/luz
    radiante). Reaprobada.
  - Q3 (Bank_teller_counter_window_empty..., nuevo archivo) → PASS. Fondo ahora
    muestra el display de turnos con "8" iluminado entre dígitos tenues, sin anillo.
    Texto exacto sin tildes, ventanilla vacía, placa "8" legible.
  - Q4 (Empty_contact_center_desk_scene...) → escena corregida (fila de escritorios
    vacíos de fondo, sin anillo) pero texto FAIL parcial: Línea 1 "NÚMERO" volvió a
    renderizar con tilde pese a la nota de ortografía reforzada. Resto de líneas y
    escena correctas.
  - Q1 no se regeneró en esta ronda (mismo archivo aprobado en Ronda 3, sigue
    vigente).
- Acción: como solo falla el texto de Q4 (no la escena completa), se aplica la regla
  de `feedback_flow_quotecard_text_validation` — NO regenerar la imagen completa,
  edición dirigida sobre la misma imagen ("keep everything identical, only fix
  'NÚMERO' → 'NUMERO' sin tilde en línea 1").
- Resultado: 3/4 aprobadas (Q1, Q2, Q3). Q4 pendiente de una edición de texto puntual
  (no regeneración completa).

### Ronda 5
- Q4 (Empty_contact_center_desk_scene..., nuevo archivo 08:39) → edición de texto
  intentada, sigue FAIL: Línea 1 sigue renderizando "NÚMERO" con tilde — tercer
  intento fallido sobre la misma palabra. Escena sigue correcta (fila de escritorios
  vacíos, headsets, sin anillo, sin personas).
- Patrón: Flow autocorrige "NUMERO" → "NÚMERO" de forma consistente, probablemente
  porque es la ortografía estándar del español y el modelo la prioriza sobre la
  instrucción literal. No ha respondido ni al prompt original ni a dos rondas de
  edición dirigida.
- Resultado: Q4 sigue pendiente — se recomienda a Andy corregir esa palabra por fuera
  de Flow (recorte/overlay de texto en un editor simple) en vez de seguir
  reintentando la generación, ya que el patrón de fallo es consistente y específico
  de esa palabra.
- Decisión de Andy: corregir "NÚMERO" → "NUMERO" fuera de Flow (Canva/editor simple,
  overlay del texto de la línea 1 sobre la imagen ya aprobada). Escena de Q4 queda
  aprobada; solo falta ese overlay puntual antes de considerar la card terminada.

## Stage 4 — Rotación de grid (BTQ)
- Qué se hizo: grid de `btq-production/website/index.html` rotado. Hero "latest"
  actualizado de EP.019 (Gladiator) a EP.020 (Ley de Goodhart) con la URL de Spotify
  ya resuelta. EP.019 entra al tracklist de 4 (era el episodio "en circulación" antes
  de este lanzamiento); EP.015 (Metal Gear Solid) sale por ser el más antiguo.
- Grid anterior: 018, 017, 016, 015 (orden del archivo, más reciente primero)
- Grid nuevo: 019, 018, 017, 016
- Nota: la convención real del archivo es "más reciente de los 4 primero" (orden
  descendente), distinto de lo que describe `04-grid-rotation.md` ("oldest→newest") —
  se siguió el orden real observado en el archivo, no el ejemplo del workflow doc.
- Archivo modificado: btq-production/website/index.html
- Pendiente: NO se hizo deploy todavía (`vercel --prod` es manual, ver Stage 5).
- Resultado: OK

## Stage 5 — Deploy + verificación
- Qué se hizo: preflight (PASS — project.json correcto, vercel.json sin
  ignoreCommand, baseline 200 OK) → gate de aprobación (aprobado por Andy) →
  `vercel --prod` desde `btq-production/website/` → verificación HTTP → verificación
  Spotify.
- URL verificada: https://behind-thequeue.com → HTTP 200 (contenido nuevo confirmado:
  "Ley de Goodhart" y hero "020" presentes en el HTML servido)
- Verificación Spotify: PASS — EP.20 "Ley de Goodhart" confirmado en
  https://open.spotify.com/show/5figtqa6zJxW1pE1sWJeEP
- Pendiente fuera del deploy: overlay manual de texto en Q4 (quote card, "NUMERO" sin
  tilde) — no bloqueante para el sitio, es un asset de redes separado.
- Resultado: OK — episodio publicado y verificado en vivo
