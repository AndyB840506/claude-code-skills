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
| EP.005 | Aterciopelados: De un bar de Bogotá al continente. | en Spotify - https://open.spotify.com/episode/2D129VK9H4sn7itPKjgz3W - primer episodio solo, duracion real ~35.8 min habla / ~36.8 min total |
| EP.006 (T2·E1) | El Club de los 27 | guion listo - 2026-07-21, `scripts/EP006-club-de-los-27.html`, ~5.208 palabras narracion (~40.5 min estimados con calibracion real MPD 159 wpm/+23.5%), formato solo. ESTRENO DE LA TEMPORADA 2. Publico = Temporada 2, Episodio 1; interno = 6º producido (EP.006). |

---

## Estructura de temporadas (decision de Andres 2026-07-21)

El show pivota **100% a misterios y leyendas del rock**. En vez de renombrar/migrar plataformas
(riesgo legal + dominio ya registrado), se parte en temporadas:

- **Temporada 1 = EP.001–EP.005.** El show viejo (rock/metal/jazz variado), incluida la era co-host
  con Juan. Queda como ARCHIVO — no se borra nada, conserva historia y suscriptores. Asi se
  encapsula el "rastro de Juan" sin destruir nada.
- **Temporada 2 = desde el Club de los 27** (misterios/leyendas). Numeracion publica REINICIA por
  temporada: Club de los 27 = **T2 · E1**; los siguientes cuentan 1,2,3… dentro de la T2. En Spotify
  se usan los campos nativos Season=2 / Episode=1 (se setean en el paso de metadata, NO requiere
  dominio nuevo). El numero interno (EP.006, EP.007…) se mantiene en archivos/roadmap para continuidad.

**Nombre:** publico sigue **Mr. Putrid's Den**. "The Crossroads" es codename interno de la etapa
(no publico). Direccion visual T2 "La Guarida" — ver `rebrand/identidad-la-guarida.html` y memoria
`project_mpd_rebrand_cruce_de_caminos`. SIN simbologia ocultista (limite firme de Andres).
(El specimen viejo "whisky & carretera" / `identidad-cruce-de-caminos.html` quedo eliminado el
2026-07-22: construia identidad publica sobre el codename interno.)

**Conector del Club de los 27** (descubierto en investigacion): Robert Johnson y el cruce de caminos
-> puente al proximo expediente (pactos con el diablo / Led Zeppelin-Crowley / backmasking). OJO:
ese tema toca lo ocultista — confirmar con Andres su comodidad y tratarlo desde angulo esceptico
antes de producirlo (ver `feedback_mpd_no_occult_symbols`).

**Plan especulativo previo** de `podcast-profile.json` (`roadmap_9_episodes`, "Beatles vs Zeppelin"
etc.) queda como banco de ideas de banda para mezclar/descartar segun el nuevo enfoque de misterios —
ya no es la fila activa. Esta tabla manda.

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
1. ~~Generar Show Notes + Metadata~~ - hecho 2026-07-17: `episodios/ep005-metadata.md` (titulo,
   descripcion EN/HTML, keywords, capitulos con timestamps reales del SRT, datos del episodio).
2. ~~Artwork del episodio~~ - hecho 2026-07-17: regenerado vía pipeline local (ComfyUI + PIL),
   primera vez que MPD usa este stack (antes solo BTQ/CCC). Portada 1:1/16:9/9:16 + 4 quote
   cards en `E:\Podcast\MPD\EP 05\artwork-local\`. Detalle completo en `artwork-ep005.md`. Las
   imágenes viejas de Flow (2026-06-17, pre-cambio de formato) quedan como referencia histórica,
   no se usan para publicar. Herramientas nuevas reusables: `comfyui/templates/mpd-portada-compose.py`
   y `mpd-quote-card-compose.py`.
3. ~~Decision sobre mencionar el paso a formato solo~~ - decidido 2026-07-19: queda sin
   mencionar, ni en el episodio ni en show notes ni en redes.
4. ~~Al publicar: agregar URL real de Spotify~~ - hecho 2026-07-19: publicado en
   https://open.spotify.com/episode/2D129VK9H4sn7itPKjgz3W, `ep005-metadata.md` y esta tabla
   actualizados.

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