# Pipeline Audit — EP.021 (Los Simpson)

## Stage A — Roadmap y pre-producción (2026-07-06)

- **Qué se hizo:** episodio confirmado desde roadmap (dry-run de Sesión 3 del roadmap de
  future-proofing — ver `docs/roadmap-future-proofing.md`). Tema decidido con Andy: Los Simpson,
  ángulo "cómo mantener un equipo motivado a largo plazo sin caer en burnout/rutina". Investigación
  real vía WebSearch (disputa salarial 1998, tenencia de Al Jean 2001-2024/25, "Zombie Simpsons"/
  Dead Homer Society, SNL/Lorne Michaels, Toyota heijunka/jinji-ido). Guion escrito completo
  siguiendo `guion-style-btq.md`, con lint aplicado (remates, muletillas, oraciones largas,
  estructura canónica). Prompts de artwork preparados. Archivo de estado creado.
- **Hallazgo real durante la escritura:** el primer borrador declaró una duración sin medirla
  programáticamente (~48 min "a ojo"), midió en realidad ~19 min. Se corrigió expandiendo el
  contenido y, más importante, se recalibró el wpm/expansión de BTQ contra el SRT real de EP.020
  (150 wpm real / +35.5% expansión, no los 143 wpm / +15% asumidos) — ver `guion-style-btq.md`.
  De esa recalibración salieron 2 reglas nuevas aplicadas a los 3 shows (BTQ/CCC/MPD vía
  `podcast-creator/workflows/01-episodio.md`): medir siempre contra el SRT real antes de escribir,
  y el estándar editorial de 40-45 min (BTQ y CCC) fijado por Andy en esta sesión.
- **Segundo hallazgo:** Andy pidió una regla nueva de estructura — ningún segmento antes del Cierre
  canónico debe sonar a que el episodio terminó ahí (riesgo de abandono según data de retención de
  Spotify). Se agregó como sección dedicada en `guion-style-btq.md` y se aplicó a este guion (hook
  de "todavía les debo la pregunta" antes de Aplicable Hoy).
- **Archivos generados:**
  - `btq-production/launch-assets/EP021-simpsons-guion.html` (guion completo, ~4.584 palabras
    escritas, ~41.4 min medido)
  - `btq-production/launch-assets/EP021-simpsons-artwork.md` (prompts 1:1/9:16/16:9)
  - `btq-production/pipeline-state-ep021.md`
  - `btq-production/roadmap-btq.md` actualizado (EP.020 → publicado + URL real, EP.021 agregado)
- **Resultado:** OK — pausa natural, esperando grabación.

## Stage 0 — Intake (2026-07-10)

- Qué se hizo: episode brief construido. Audio confirmado por Andy:
  `E:\Podcast\BTQ\EP 21\BTQ EP 21.mp3` (39.5 MB, grabado 2026-07-10). Closing TM y fuentes
  extraídos del guion aprobado (no se repreguntaron). `spotify_url: pending`.
- Resultado: OK — sigue Stage 1 (transcripción)

## Stage 1 — Transcripción (2026-07-10)

- Qué se hizo: transcripción con diarización (large-v2, es, srt) vía WhisperX en background,
  exit 0. Encoding UTF-8 verificado leyendo el archivo (el mojibake del log era solo el
  console encoding de PS). Tags [SPEAKER_00]/[SPEAKER_01] presentes.
- Archivos generados: E:\Transcriptor\transcripciones\BTQ EP 21.srt (46 KB, ~41:10 de contenido + outro musical)
- Resultado: OK — sigue Stage 2 (assets via episode-launch)

## Stage 2 — Generación de assets (2026-07-10)

- Qué se hizo: episode-launch invocado en modo pipeline. Fact-check de entidades reales del
  SRT vs fuentes del guion: sin errores. Descripción Spotify 310 palabras (contada
  programáticamente). Capítulos de YouTube con timestamps reales del SRT.
- Corrección de Andy en el gate: los aros/círculos concéntricos de fondo NO van — se
  retiraron de los 3 prompts de portada, y la regla se hizo permanente en
  brand-constants.md (vetados en TODAS las imágenes BTQ, portadas y quote cards; antes
  el motivo estaba "reservado para la portada") + memoria actualizada.
- Archivos generados: btq-production/launch-assets/EP021-simpsons-launch.md;
  EP021-simpsons-artwork.md actualizado (sin aros); brand-constants.md §Reglas #3,
  checklist #6, §Quote Cards y §Patrones de Flow actualizados.
- Gate heredado: aprobado por Andy (con la corrección de aros aplicada antes).
- Checkpoint Spotify: pendiente — Andy va a publicar con la metadata del §A.
- Resultado: OK — 3 prompts de cover-art listos para Stage 3
