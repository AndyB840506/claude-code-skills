# Pipeline audit — EP.019 (BTQ — Gladiator)

## Stage A — Roadmap y pre-producción (2026-06-26)
- **Qué se hizo:** episodio confirmado desde roadmap (con swap EP.019↔020 corregido: Gladiator
  se graba ahora = EP.019; pilar SEO de métricas = EP.020, semana siguiente). Guion generado,
  reescrito a voz narrativa "MPD meets TED" y aprobado por Andy. Limpieza de lenguaje
  (palabras poco comunes → habla natural). Segmento Referencias Cruzadas añadido (Sócrates +
  Wooden, fuera de Roma). Recomendaciones diversificadas. Cierre canónico completo (redes +
  teaser + TM). Prompts de artwork preparados (no generados — eso es Stage C).
- **Archivos generados:**
  - btq-production/launch-assets/EP019-gladiator-guion.html (guion, ~58 min)
  - btq-production/launch-assets/EP019-gladiator-artwork.md (prompts portada/teaser/thumbnail)
  - btq-production/pipeline-state-ep019.md (checkpoint)
  - roadmap-btq.md actualizado (EP.019 → guion listo)
- **Verificación:** lint guion-style-btq.md en verde (4 remates, 1 "imagínense", 0 "me vuela",
  cita exacta 3x, sin palabras raras, duración MEDIDA por palabras/143 no a ojo). Datos
  históricos verificados por web (Goodhart/SQM se guardaron para EP.020; Cómodo, Marco Aurelio,
  Sócrates, Wooden, Collins para EP.019). Marcados [VERIFICAR] antes de grabar: detalle exacto
  de la muerte de Cómodo (Narciso/192) y título en español de "Good to Great".
- **Resultado:** OK — pausa natural, esperando grabación del episodio completo (teaser ya grabado).

## Stage B.0/B.1 — Intake + Transcripción (2026-06-29)
- **Qué se hizo:** episodio completo grabado por Andy. Episode brief armado (closing TM
  confirmado tal cual del guion; fuentes tomadas de la sección Fuentes del guion). Audio
  localizado en E:\Podcast\BTQ\EP 19\BTQ EP 19.wav (1.07 GB) — confirmado con Andy tras
  discrepancia inicial (archivo apareció primero suelto en la raíz E:\Podcast\, luego
  confirmado ya movido a la subcarpeta correcta). Transcripción corrida con WhisperX
  large-v2 + diarización, español.
- **Archivos generados:**
  - E:\Transcriptor\transcripciones\BTQ EP 19.srt (78 KB)
  - btq-production/pipeline-state-ep019.md actualizado (stage_b: in_progress)
- **Verificación:** SRT generado sin errores (exit code 0), tamaño consistente con ~58 min de audio.
- **Resultado:** OK — sigue a Stage B.2 (assets vía episode-launch).

## Stage B.2 — Generación de assets + checkpoint Spotify (2026-06-29)
- **Qué se hizo:** episode-launch invocado con los 6 inputs del brief. Generados Spotify SEO
  (título/preview/descripción HTML+texto/tags), plan social 4 días (fechas asumidas, a
  confirmar), YouTube metadata (capítulos con timestamps reales del SRT), y 4 quote cards
  revalidadas contra el audio real (no contra el guion escrito — hubo variación natural:
  "su merced" en vez de "usted", "Tim Collins" corregido a "Jim Collins" tras confirmar con
  Andy). Cover-art prompts reusados de Stage A (EP019-gladiator-artwork.md), no regenerados.
  Andy confirmó la URL de Spotify en vivo — propagada a todos los CTAs de §B/§C.
- **Archivos generados:**
  - btq-production/launch-assets/EP019-gladiator-launch.md
  - btq-production/pipeline-state-ep019.md actualizado (stage_b: complete, spotify_url resuelto)
- **Verificación:** quote cards cruzadas línea por línea contra el SRT (timestamps citados).
  Dato corregido (Jim Collins) confirmado explícitamente por Andy antes de publicar en assets.
- **Resultado:** OK — pendiente aprobación de Andy para commit + push; sigue a Stage C
  (validación de imágenes en Flow) tras la aprobación.
