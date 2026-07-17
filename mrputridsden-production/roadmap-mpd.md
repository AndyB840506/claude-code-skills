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
| EP.005 | Aterciopelados: una gomela, un punkero | guion co-host (P1+P2, ~90 min) DESCARTADO - reescribir solo, episodio unico ~43 min - sin grabar |

---

**Cambio de formato (2026-07-17):** Juan dejo el proyecto, Andres continua solo desde EP.005 en
adelante. El guion co-host de EP.005 (Aterciopelados, P1+P2, ~90 min) ya escrito queda descartado
- se reescribe como episodio unico de ~43 min (nuevo sweet spot de retencion, decision de Andres)
antes de grabacion. El default de 2 partes queda retirado para episodios nuevos (ver memoria
`project_mpd_episodes_two_parts`, RETIRED). Ver memoria `project_mpd_juan_departure` y
`podcast-profile.json` (formato_historico, duracion_nota, word_count_target_nota,
roadmap_9_episodes).

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