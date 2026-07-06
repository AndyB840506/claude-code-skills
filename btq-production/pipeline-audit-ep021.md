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

## Siguiente paso

Andy graba el guion. Al tener el audio, retomar el pipeline ("corre el pipeline para EP.021") para
seguir con Stage B (transcripción) — el estado queda guardado en `pipeline-state-ep021.md`.
