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

## Stage 3 — Generación de imágenes (2026-07-10, en curso)

- Cambio de herramienta: Flow rechazó los prompts por copyright (figura tipo Homero).
  Se generó en el ComfyUI local del desktop (E:\AI, Z-Image Turbo, grafo "Desde Cero"
  convertido a API, 8 steps / CFG 1 / res_multistep).
- Escenas SIN tipografía (el texto/footer va como overlay aparte — modelo local no
  renderiza texto exacto confiable).
- Iteración: 9x16 v1 falló (test-card salió como barras de colores literales + piso
  con paisaje/horizonte) → v2 con prompt corregido (solo scan-lines dorados, piso
  studio void) pasó.
- Candidatas en E:\AI\outputs\: BTQ-EP021-1x1_00001_.png (pasa checklist),
  BTQ-EP021-16x9_00001_.png (pasa), BTQ-EP021-9x16_00002_.png (pasa; v1 descartada).
- Cambio de dirección (Andy): personajes con nombre propio sí, porque local no tiene filtro
  — pero el nombre "Homer Simpson" ancla el render al cartoon (ignora "de espaldas"/"no
  yellow"). Advertido el riesgo IP de publicar un Homero reconocible (decisión editorial
  de Andy). Espectro generado: cartoon puro / híbrido 3D (i2i denoise 0.55) / uncanny
  (0.7). Andy eligió el HÍBRIDO 3D (BTQ-EP021-1x1-i2i_00001_.png).
- Lección (feedback de Andy, "queda super picasso"): NO describir al personaje de memoria
  en prompts — la identidad debe venir de píxeles de referencia (img2img desde el cartoon
  fiel del propio modelo, o desde stills reales). Las conversiones de figuras pequeñas en
  el encuadre degradan identidad (9:16/16:9 fallaron a denoise 0.55 y 0.65).
- Solución final: composición determinista con Pillow (compose_ep021.py) — la ÚNICA figura
  aprobada se recorta y monta en los 3 formatos + tipografía Anton (overlay, tildes
  correctas porque ya no depende de Flow) + franja de íconos Spotify/YouTube reciclada de
  la portada real de EP.019 (que es 2048x2048, no 3000 — bug corregido). Patrón de footer
  real de EP.019 (más simple que el bloque congelado del doc).
- Finales: E:\Podcast\BTQ\EP 21\BTQ Artwork EP 21\BTQ-EP021-FINAL-{1x1,9x16,16x9}.png
  (1:1 a 3000x3000 nativo por composición — sin upscale IA necesario).
- Composiciones Pillow rechazadas por Andy ("super feo" — figura flotando en negro sin
  atmósfera). Lección: la atmósfera nace en el render, no se agrega componiendo.
- Andy generó la portada oficial él mismo en la UI de ComfyUI con el prompt con nombre
  propio (ComfyUI_00042_.png, 3D dorada) y la fijó como OFICIAL. Se exploró una vía 2D
  (4 iteraciones: chibi → proporciones canon → shading Simpsons Movie → "SIMPSÓN" typo →
  limpia) que quedó como alternativa en BTQ-EP021-1x1-2D_00004_.png, no elegida.
- Lecciones de prompting Z-Image documentadas en comfyui/docs/prompting.md: a CFG 1 el
  negative no actúa; "DO NOT render X" evoca X; no pedir conceptos que contienen el
  elemento prohibido (test-card ⊃ círculos); SetLatentNoiseMask para retoques (no
  VAEEncodeForInpaint); destruir estructura con blur antes de re-texturizar.
- Resultado: portada 1:1 oficial = la de Andy. 9:16/16:9 pendientes de definir sobre esa
  base (además del typo "Queee" y el upscale si Andy los quiere de mi lado).

## Stage 3b — Material de marketing (2026-07-11)

- Plan social: ya generado en Stage 2 (EP021-simpsons-launch.md §B) — no se regeneró.
- Quote cards: 3 remates extraídos del guion, los 3 validados contra el SRT real
  (~05:09, ~24:10, ~39:20 — dichos casi verbatim). Cards compuestas con split 50/50
  (escena ComfyUI con volumen real + texto determinista PIL, tildes correctas, cero
  riesgo de typo del modelo): CARD1 micrófono/estudio, CARD2 CRT en estática/sofá,
  CARD3 vela/standby rojo. Card 2 corregida a cita verbatim antes de entregar.
- Archivos: E:\Podcast\BTQ\EP 21\BTQ Artwork EP 21\BTQ-EP021-CARD{1,2,3}.png (1080x1080).
- Resultado: OK — pendiente visto bueno de Andy; siguen grid (04) y deploy (05), ambos
  bloqueados por la URL de Spotify (aún pending).
