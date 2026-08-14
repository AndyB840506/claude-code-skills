# Roadmap — Mr. Putrid's Den (MPD)

Fuente de verdad de "qué episodio sigue". `episode-pipeline` la lee al arrancar
Stage A (`00-roadmap.md`) y la actualiza al cerrar cada macro-stage.

Estados posibles: `en roadmap` → `guion listo` → `grabado` → `en Spotify` → `publicado`

| EP | Título | Estado |
|---|---|---|
| EP.001 | Bienvenidos a la Guarida | publicado |
| EP.002 | Black Sabbath: El Génesis del Heavy Metal | publicado |
| EP.003 | Las raices del rock: Sister Rosetta Tharpe | publicado - rendimiento bajo vs EP.002 (ver nota de audiencia) |
| EP.004 P1 | Kraken: el Titan del Rock colombiano (Parte 1) | publicado - https://open.spotify.com/episode/0Zf7egfYOQFP3E8Af9b4fr - salio 2026-06-14 (no el 19 como decia el plan), 1h45min. Verificado contra Spotify 2026-07-28. |
| EP.004 P2 | Kraken: el Titan del Rock colombiano (Parte 2) | publicado - https://open.spotify.com/episode/1QRXaL85TszCpwo2pfmEPw - salio 2026-06-20, 1h16min. Verificado contra Spotify 2026-07-28. ⚠️ **NO esta en el archivo de la web** (ver nota abajo). |
| EP.005 | Aterciopelados: De un bar de Bogotá al continente. | en Spotify - https://open.spotify.com/episode/2D129VK9H4sn7itPKjgz3W - primer episodio solo, duracion real ~35.8 min habla / ~36.8 min total |
| EP.006 (T2·E1) | El Club de los 27: la maldición que los números desmienten | **publicado** - https://open.spotify.com/episode/3KW68cHhHpkMCLbgZkiov7 - salió **2026-08-01** (no el 07-31 que decía la memoria), **41 min**. Título, show, fecha y duración verificados contra Spotify el 2026-08-03. Regrabado el 2026-07-28. Checkpoint de plays: ~2026-08-14. Guion: `scripts/EP006-club-de-los-27.html`, ~5.208 palabras narracion (~40.5 min estimados, calibracion MPD 159 wpm/+23.5%), formato solo. ESTRENO DE LA TEMPORADA 2. Publico = T2·E1; interno = 6º producido. Faltan: SRT, metadata/show-notes, quote cards, plan de lanzamiento. |
| EP.02 (T2·E2) | Pactos, símbolos y mensajes ocultos: el rock y el diablo | **publicado** - https://open.spotify.com/episode/46l6NpQVF9np4unotGT4KM - salió 2026-08-08, 39:23. Guion: `scripts/EP02-el-rock-y-el-diablo.html`. Renombrado de "EP.007" a "EP.02" el 2026-08-06 (Andrés) — ver nota de numeración abajo. Sitio (mrputridsden.com) actualizado y verificado 2026-08-09: Expediente 01 pasado a publicado + Expediente 02 agregado — ver `pipeline-audit-ep02.md`. |
| EP.03 (T2·E3) | La Bestia que el rock volvió inmortal | guion listo - Stage A cerrado 2026-08-14. Guion en `scripts/EP03-la-bestia-que-el-rock-volvio-inmortal.html` (4.408 palabras), concepto de artwork aprobado (`episodios/temporada-2/artwork-ep03.md`). Experimento de estilo Tales from the Crypt, solo este episodio. Próximo paso: grabar. |

**Cadencia de carriles (Andrés, 2026-08-03):** principal (alta rotación) por defecto; **uno de
nicho cada 3 o 4 episodios**. Con esta cuenta, el primer slot de nicho cae en **T2·E4 o T2·E5**.
Ver `banco-expedientes.md` § Carril de nicho.

---

## Estructura de temporadas (decision de Andres 2026-07-21)

El show pivota **100% a misterios y leyendas**, anclado en el rock. *(Alcance afinado el 2026-07-24
a HIBRIDO ANCLADO EN ROCK: el rock es la columna e identidad, pero hay valvula para otras leyendas
e invitados. Sigue siendo 100% misterios — nada de episodios de analisis de banda.)*
En vez de renombrar/migrar plataformas
(riesgo legal + dominio ya registrado), se parte en temporadas:

- **Temporada 1 = EP.001–EP.005.** El show viejo (rock/metal/jazz variado), incluida la era co-host
  con Juan. Queda como ARCHIVO — no se borra nada, conserva historia y suscriptores. Asi se
  encapsula el "rastro de Juan" sin destruir nada.
- **Temporada 2 = desde el Club de los 27** (misterios/leyendas). Numeracion publica REINICIA por
  temporada: Club de los 27 = **T2 · E1**; los siguientes cuentan 1,2,3… dentro de la T2. En Spotify
  se usan los campos nativos Season=2 / Episode=1 (se setean en el paso de metadata, NO requiere
  dominio nuevo).
  **SUPERADO 2026-08-06 (Andrés):** la idea de mantener un "numero interno" separado (EP.006,
  EP.007…) para archivos/roadmap, distinto del numero publico de temporada, quedo retirada —
  generaba confusion (un titulo de Spotify salio escrito "EP.007" por error, mezclando los dos
  esquemas). **Regla nueva: un solo numero.** Desde este episodio, archivos, roadmap y texto
  publico usan el mismo numero de temporada: **EP.02** (= T2·E2), **EP.03** (= T2·E3), etc. La fila
  de EP.006 arriba NO se renombra — ya esta publicada bajo el esquema viejo y renumerarla
  falsificaria un registro en vivo; el corte aplica desde EP.02 en adelante.

**Nombre:** **Mr. Putrid's Den** full, sin sub-nombres. *("The Crossroads" fue un codename interno
del pivote y quedo RETIRADO el 2026-07-24 — nunca fue publico y ya no se usa ni internamente.)*
Direccion visual T2 "La Guarida" — ver `rebrand/identidad-la-guarida.html` y memoria
`project_mpd_rebrand_cruce_de_caminos`. SIN simbologia ocultista (limite firme de Andres).
(El specimen viejo "whisky & carretera" / `identidad-cruce-de-caminos.html` quedo eliminado el
2026-07-22: construia identidad publica sobre el codename interno.)

**Conector del Club de los 27** (descubierto en investigacion): Robert Johnson y el cruce de caminos
-> puente al proximo expediente (pactos con el diablo / Led Zeppelin-Crowley / backmasking). OJO:
ese tema toca lo ocultista — tratarlo desde angulo esceptico y sin simbologia en el artwork
(ver `feedback_mpd_no_occult_symbols`).

> **Ya no es una opcion: quedo ANUNCIADO AL AIRE.** El cierre de EP.006 lo nombra textual —
> *"Pactos, simbolos y mensajes ocultos: el rock y el diablo"* — y ahi mismo abre el alcance mas
> alla de Johnson ("no es solo Robert Johnson... Led Zeppelin, bandas de metal enteras, canciones
> que supuestamente esconden mensajes si uno las pone al reves"). Verificado contra
> `scripts/EP006-club-de-los-27.html`, bloque 8, el 2026-08-03. Robert Johnson es la PUERTA del
> expediente, no el tema — y su material biografico ya se gasto en el bloque C de EP.006.
> Angulos investigados en `banco-expedientes.md`.

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
   > ⚠️ **Esas dos quedaron para T1 solamente (2026-07-30).** Son Impact + crimson + dorado,
   > paleta retirada. Para Temporada 2 los compositores son `mpd-portada-ep-t2.py` (los tres
   > formatos del episodio) y `mpd-quote-card-t2.py`. La línea de arriba se conserva porque
   > narra lo que se construyó el 07-17, no porque siga mandando.
3. ~~Decision sobre mencionar el paso a formato solo~~ - decidido 2026-07-19: queda sin
   mencionar, ni en el episodio ni en show notes ni en redes.
4. ~~Al publicar: agregar URL real de Spotify~~ - hecho 2026-07-19: publicado en
   https://open.spotify.com/episode/2D129VK9H4sn7itPKjgz3W, `ep005-metadata.md` y esta tabla
   actualizados.

Ver memoria `project_mpd_juan_departure` y `podcast-profile.json` (formato_historico,
duracion_nota, word_count_target_nota, roadmap_9_episodes).

**Notas:**
- Seeded desde un snapshot de memoria del 2026-06-05 (esa entrada ya no existe).
- El roadmap EP.002–EP.011 de la era T1 se armó con la **regla de rotación de género**, hoy
  RETIRADA (T2 es 100% misterios: no hay género musical que rotar). Lo que sigue vigente es la
  **regla del conector**, ahora hacia el próximo *expediente*, no hacia el próximo género.
  Agregar filas a esta tabla a medida que cada episodio entra en producción activa.
- Mantener esta tabla actualizada manualmente o vía `episode-pipeline` — es la fuente
  que Stage A consulta para decidir cuál episodio sigue.

---

## Hueco abierto en el archivo de la web (detectado 2026-07-28)

`#archivo` de mrputridsden.com dice ser "la primera temporada del show, episodio por episodio" y
tiene **5 filas** (T1·01 a T1·05). Pero T1 publico **6 items**: EP.004 salio en dos partes. La fila
T1·04 apunta solo a la Parte 1 (`0Zf7egfYOQFP3E8Af9b4fr`); la **Parte 2**
(`1QRXaL85TszCpwo2pfmEPw`, 2026-06-20, 1h16min) **no tiene fila**.

**Decidido por Andres el 2026-07-28: NO se renumera nada.** T1 queda sellada en T1·01–T1·05 con
Aterciopelados cerrando el ciclo, y T2 cuenta aparte desde E1. La opcion de correr Aterciopelados a
T1·06 para abrirle campo a la Parte 2 queda **descartada** — tocar la numeracion de una temporada ya
cerrada es justo lo que se queria evitar.

Lo unico que sigue abierto es cosmetico y de bajo impacto: la fila T1·04 enlaza solo la Parte 1 y
declara "92 min" cuando lo real son 105 min (P1) + 76 min (P2). Si algun dia se toca el sitio por
otra razon, arreglar de paso; **no vale un deploy propio**. Ojo con el deploy: `vercel --prod`
normal da 404, hay que usar el flujo prebuilt (ver CLAUDE.md § Sitio web).

---

## Ideas y contactos del feedback del piloto (2026-07-25) — rescatados de WhatsApp 2026-07-28

Salieron en la misma conversacion del feedback y NO estaban en ningun archivo. No son decisiones
tomadas: son pendientes de decidir con Andres.

- **"Martes de misterio"** — idea de cadencia/franja propuesta por Andres en el chat; la persona
  del feedback la respaldo ("uy re si!"). Encaja con que el show no tiene deadline fijo y con que
  ella misma senalo que un capitulo semanal es mucha inversion de tiempo. **Sin decidir.**
- **Episodio de leyendas venezolanas de terror** — ella y una amiga quieren hacer uno; Andres
  ofrecio invitarlas ("te puedo invitar y nos cuentas") y ella acepto con pena pero acepto.
  Encaja con el alcance hibrido (rock como columna, abierto a otras leyendas) y con que La Silla
  Putrida sigue abierta. **Contacto tibio, sin fecha.**
- **Ofrecimiento de ayuda con la edicion** — "yo te puedo ayudar con la edicion", dicho en firme.
  Si la edicion es cuello de botella para la cadencia, esto ya esta ofrecido. **Sin usar.**

Referencia de genero que ella misma mando como norte: **Relatos de la Noche** (Sonoro). Ojo, esa
tutea al oyente y MPD usa usted — se toma la atmosfera, no el registro.

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
  > ⚠️ **Esta columna lleva vacia desde el EP.003.** "Rendimiento bajo vs EP.002"
  > se anoto sin numero. Mientras no haya plays reales anotados aca, cualquier
  > afirmacion sobre que tema "pega mas" es estimacion, no medicion — incluida
  > la seleccion de temas del banco de expedientes.

### Segunda capa — demanda primero, diferenciacion en el detalle (Andres, 2026-08-03)

La regla de arriba dice QUE ancla usar. Esta dice COMO elegir el tema, y corrige un
sesgo que tenia el analisis previo: se estaba tratando la saturacion como defecto.

- **La alta rotacion es senal de demanda probada, no un motivo para descartar.**
  Un tema muy contado lo es porque la gente lo consume. Con audiencia todavia en
  construccion, ir al nicho primero hace la captacion mucho mas dificil.
- **El diferenciador NO es la originalidad del tema: es el detalle subexpuesto.**
  Titular de alta rotacion + el angulo del que casi nadie habla, siempre que sea
  relevante para la tesis. Ejemplo verificado 2026-08-03: la leyenda de la
  encrucijada era de **Tommy Johnson** (sin parentesco), contada por su hermano
  LeDell al folclorista David Evans; salto a Robert Johnson porque los dos vivieron
  en Hazlehurst, Mississippi.
- **Esto NO contradice el filtro de canon de CLAUDE.md** ("si tu revelacion es MAS
  PEQUENA que el mito, no la reveles"). Un detalle poco contado es mas pequeno en
  TAMANO y mas grande en SIGNIFICADO — es justo el destape que reencuadra. Si el
  detalle solo desinfla, no sirve.
- **Cadencia de nicho: uno cada 3 o 4 episodios.** Los temas densos, oscuros o de
  baja rotacion (black metal noruego, muertes en conciertos, EVP, Jim Sullivan)
  **no se descartan** — se aplazan a esos slots. Asi el show construye audiencia con
  los temas de alcance y la premia con profundidad, sin quemarse en el nicho antes
  de tener base.

Banco de temas ya filtrado contra estas dos capas: `banco-expedientes.md`.