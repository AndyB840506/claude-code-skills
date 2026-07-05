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
- Checkpoint Spotify: pendiente — Andy va a publicar y avisar la URL
- Resultado: OK — 3 prompts de cover-art ya resueltos en Stage A (no quedan pendientes para Stage 3)
