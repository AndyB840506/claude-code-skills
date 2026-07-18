# Roadmap — Mr. Putrid's Den (MPD)

Fuente de verdad de "qué episodio sigue". `episode-pipeline` la lee al arrancar
Stage A (`00-roadmap.md`) y la actualiza al cerrar cada macro-stage.

Estados posibles: `en roadmap` → `guion listo` → `grabado` → `en Spotify` → `publicado`

| EP | Título | Estado |
|---|---|---|
| EP.001 | Bienvenidos a la Guarida | publicado |
| EP.002 | Black Sabbath: El Génesis del Heavy Metal | publicado |
| EP.003 | Las raices del rock: Sister Rosetta Tharpe | publicado - rendimiento bajo vs EP.002 (ver nota de audiencia) |
| EP.004 P1 | Kraken: el Titan del Rock colombiano (Parte 1) | en Spotify - programado viernes 2026-06-19 (link listo) |
| EP.004 P2 | Kraken: el Titan del Rock colombiano (Parte 2) | grabado - sale ~2026-06-20 |
| EP.005 | Aterciopelados: una gomela, un punkero | grabado 2026-07-17 - `E:\Podcast\MPD\EP 05\MPD EP 05.mp3` (35MB) - primer episodio solo, duracion real ~35.8 min (SRT, por debajo del piso de 40 min - ver guion-style-mpd.md) |

---

**Cambio de formato (2026-07-17):** Juan dejo el proyecto, Andres continua solo desde EP.005 en
adelante. El guion co-host original de EP.005 (Aterciopelados, P1+P2, ~90 min) quedo descartado
(recuperable via git history) y se reescribio el mismo dia como episodio unico solo, 4.616
palabras escritas. Se grabo el mismo dia. El default de 2 partes queda retirado para episodios
nuevos (ver memoria `project_mpd_episodes_two_parts`, RETIRED). El segmento de Promocion (eventos
underground) tambien se retiro del show, no se reasigno.

**Calibracion real (2026-07-17, mismo dia, tras transcribir el SRT):** el guion se escribio con
una formula PRESTADA de BTQ (150 wpm + 35.5% expansion) por no tener datos propios de MPD solo
todavia - estimaba ~42 min. La grabacion real salio en ~35.8 min (SRT via WhisperX, sin
diarizacion - un solo host): Andres habla mas rapido en MPD (159 wpm medido) pero expande menos
en vivo (+23.5%, no +35.5%). Con datos reales ya calibrados en
`mrputridsden-production/guion-style-mpd.md`, el proximo guion debe apuntar a ~5.543 palabras
escritas para el target real de 43 min (antes se apuntaba a ~4.760 con la formula prestada).
`podcast-profile.json` (`word_count_target`) ya actualizado a 5543.

**Decision de Andres (2026-07-17):** EP.005 se publica AS-IS, sin padding ni re-grabacion pese a
salir corto (~35.8 min vs 43 min target). El formula corregida (~5.543 palabras escritas,
`guion-style-mpd.md`) se aplica desde EP.006 en adelante, no retroactivamente a EP.005.

**Pendiente ahora:**
1. Generar/actualizar Show Notes + Metadata (`ep005-metadata.md` no existe aun, crear) con la
   duracion real ~35.8 min.
2. Andres aun no ha decidido si se menciona el paso a formato solo en el episodio o solo en show
   notes - el guion grabado NO lo menciona al aire, a proposito (ver nota de produccion en el script).

Ver memoria `project_mpd_juan_departure` y `podcast-profile.json` (formato_historico,
duracion_nota, word_count_target_nota, roadmap_9_episodes).

**Notas:**
- Seeded desde memoria `mrputridsden_project` (snapshot 2026-06-05).
- Roadmap completo EP.002–EP.011 ya definido con regla de rotación de género y regla
  de conector — agregar filas a esta tabla a medida que cada episodio entra en
  producción activa (no listar los 11 de una vez para no quedar desactualizado).
- Mantener esta tabla actualizada manualmente o vía `episode-pipeline` — es la fuente
  que Stage A consulta para decidir cuál episodio sigue.

---

## Regla de audiencia (aprendida EP.003, 2026-06-11)

EP.003 (Sister Rosetta Tharpe, musicologia/raices) rindio por debajo de EP.002
(Black Sabbath, banda iconica). Leccion aplicada desde EP.004:

- **El ancla de cada episodio es una banda o artista con nombre reconocible
  para la audiencia metalera/rockera.** La musicologia y la genealogia van
  DENTRO del episodio como contexto, no como tema titular.
- Bandas locales/latinas con peso historico (Kraken, etc.) conectan doble:
  identidad + nostalgia.
- Antes de fijar el siguiente episodio del roadmap: revisar plays de Spotify
  del episodio anterior (checkpoint post-launch, ~1-2 semanas despues de
  publicar) y registrar el dato en esta tabla.