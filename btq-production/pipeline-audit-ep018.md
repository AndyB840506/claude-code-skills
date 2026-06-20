# Pipeline audit — EP.018 (BTQ — El Mundial)

## Stage 0 — Intake
- Que se hizo: episode brief construido (show BTQ, audio confirmado, datos extraidos del guion EP018-mundial-guion.html)
- Audio: E:\Podcast\BTQ\EP 18\BTQ EP 18.wav (923.7 MB, 2026-06-19 21:02)
- Resultado: OK

## Stage 1 — Transcripcion
- Que se hizo: transcripcion con diarizacion (large-v2, es, srt)
- Archivos generados: E:\Transcriptor\transcripciones\BTQ EP 18.srt (70.2 KB)
- Notas: sin alucinaciones en bordes; un solo speaker (Andy); marcadores [ACTUALIZAR AL GRABAR] del Mundial resueltos al grabar (3-1, 48 selecciones, 3 paises)
- Resultado: OK

## Stage 2 — Generacion de assets
- Que se hizo: episode-launch invocado (ruta BTQ)
- Archivos generados: btq-production/launch-assets/EP018-mundial-launch.md
- Contenido: Spotify SEO (titulo EP.18, preview, desc HTML+texto, tags), plan social 4 dias (intriga vie 19/sab 20, launch dom 21 8PM, pico lun 22, refuerzo mar 23), YouTube (titulo+desc 5 bloques+17 capitulos con timestamps reales del SRT+20 tags+thumbnail), 3 prompts cover-art (1:1/9:16/16:9, sujeto DT en la raya)
- Gate heredado: aprobado por Andy
- Checkpoint Spotify: pendiente — Andy publica dom 21-jun 8PM y trae URL en vivo
- Resultado: OK — 3 prompts de cover-art listos para Stage 3

## Stage 3 — Validacion de imagenes
- Que se hizo: validacion directa (Read de imagenes) contra reglas estandar (rondas: 1)
- Imagenes en E:\Podcast\BTQ\EP 18\BTQ EP 18 Artwork\

### Ronda 1
- Imagen 1:1 (2048x2048)   -> 1 figura/cero caras: PASS · texto "EL MUNDIAL"/"LIDERAZGO SIN TOCAR EL BALON" letra por letra sin tildes: PASS · footer EP.018: PASS · regla de margen: PASS -> PASS
- Imagen 9:16 (1536x2752)  -> 1 figura/cero caras: PASS · mismo titulo letra por letra: PASS · footer: PASS · margen: PASS -> PASS
- Imagen 16:9 (2752x1536)  -> 1 figura/cero caras: PASS · texto "EL BALON"/"NO ES TUYO" letra por letra sin tildes: PASS · footer: PASS · margen (texto izq/sujeto der): PASS -> PASS

- Resultado: OK — 3/3 imagenes PASS en 1 ronda (incluye fix del titulo del episodio en 1:1 y 9:16 pedido por Andy)

## Stage 3b — Material de marketing
- Que se hizo: plan social confirmado (ya venia del Stage 2 §B, no se regenero); 4 quote cards generadas (Andy pidio las 4) siguiendo specs documentadas + patron validado EP.017 (btq-project/workflows/quote-cards.md no existe en disco)
- Archivos generados: seccion E de btq-production/launch-assets/EP018-mundial-launch.md (Q1 preparar/Bielsa, Q2 Obdulio/pulso, Q3 Zander/ojos, Q4 cierre/tesis) — 16:9 split-scene, derivables a 1:1/9:16
- Pendiente: Andy genera las 4 en Flow y pasa rutas (revision visual rapida, no requiere subagent de Stage 3)
- Resultado: OK
