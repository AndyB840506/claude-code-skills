EPISODE: **EP.027** (BTQ) — el Principio de Peter
stage_a: **complete** — guion aprobado 2026-07-28, **grabado la noche del 2026-07-31**.
stage_b: **completa (2026-08-20)**. Publicado en Spotify:
  https://open.spotify.com/episode/5GEHeLhfee0NmFYalIU1YW?si=NyN-FjRTR56ciSDEDc-dQg — domingo
  23 de agosto 2026, 8PM Colombia. Artículo del sitio desplegado y verificado en vivo (curl
  200 en artículo, og-image, índice y sitemap). Kit completo en
  `launch-assets/EP027-peter-launch.md`.
stage_c: no iniciado (redes/YouTube — assets escritos en el kit, publicación manual de Andy).

**Contradicción resuelta 2026-08-20:** `roadmap-btq.md` traía una fila del 2026-08-03 diciendo
"GUION A REDISEÑAR... la grabación queda obsoleta", nunca reflejada en este archivo. Andy
confirmó explícitamente que esa nota quedó vieja y que la grabación del 07-31 es válida — la
fila del roadmap se corrigió en la misma sesión.

## Sesión 2026-08-20 — destrabar stage_b

- **Audio confirmado como válido**, no obsoleto — el nombre en disco
  (`BTQ EP 27-PETER-OBSOLETO.mp3/.wav/.rpp`, en `E:\Podcast\BTQ\EP 27\`) arrastra el sufijo del
  rename viejo del 2026-08-01, pero el contenido grabado el 31 de julio se usa tal cual
  (confirmado por Andy, ignorando los 2 errores hablados conocidos abajo).
- **Duración real medida con ffprobe: 41:00** (2460,27 s) — dentro del estándar 40-45 min.
- **Transcrito por primera vez** con WhisperX large-v2 + diarización:
  `E:\Transcriptor\transcripciones\BTQ EP 27-PETER-OBSOLETO.srt`. Confirmados por grep, no a
  ojo, los 2 errores ya conocidos por el roadmap: el segmento 0 dice literalmente "episodio 24"
  (min. 0:43) y el segmento 7 anuncia la Ley de Little como episodio siguiente (min. 40:00) —
  ambos aceptados por Andy, no se regraba.
  - **"Imagínense" se usó 10 veces al aire** (presupuesto de la guía: máx. 1), ad-lib de Andy,
    no estaba en el guion. Mismo patrón que EP.026 (12 usos) — candidato a vigilar en la próxima
    sesión de escritura.
  - **Expansión real medida: +11,4%** (6.156 palabras habladas / 5.525 escritas), muy cerca del
    +13% asumido al escribir. Dato nuevo para la tabla de calibración del esqueleto TRENZADO
    (`guion-style-btq.md` § Calibración de duración) — el otro dato medido de ese esqueleto
    (EP.026) dio solo +3,4%, así que la muestra sigue siendo de 2 episodios con resultados
    dispares.
- **Portadas regeneradas desde cero** en la carpeta correcta desde el primer intento
  (`E:\Podcast\BTQ\EP 27\BTQ Artwork EP 27\`) — las 6 viejas con el título de EP.24 horneado se
  eliminaron. Dirección: tipografía pura v4, sin la excepción de escena renderizada (esa era
  para el EP.024 real, "puerta abierta", no para este episodio — confirmado leyendo
  `brand-constants.md` antes de generar). Gate mecánico y verificación visual: **PASS**.
- **4 quote cards generadas** desde citas verbatim del SRT real (no del guion), verificadas
  contra el audio con grep.
- **Kit completo escrito**: artículo del sitio (no desplegado), Spotify SEO, plan social de 4
  días, YouTube metadata con capítulos reales del SRT, artículo nativo de LinkedIn (+ versión
  renderizada en Artifact). Todo con placeholders `PENDIENTE-URL-SPOTIFY` explícitos donde
  falta la URL real — ver `launch-assets/EP027-peter-launch.md` para el detalle y §F para los
  pendientes que bloquean el deploy.
- **Hallazgo de proceso, sin resolver:** `step2-generate-assets.md` dice que la regla de "sin
  rayas ni comillas angulares" aplica también al artículo del sitio, pero el último artículo
  publicado (EP.026, 2026-08-16) tiene 26 rayas como conector y 10 comillas angulares — el
  documento y el entregable real se contradicen. Esta sesión siguió el entregable real para el
  artículo del sitio (rayas permitidas, consistente con EP.023-026) y la regla escrita para
  LinkedIn/Spotify/social/YouTube (texto que se pega a mano en un editor de terceros). Sin
  resolver cuál de las dos gana oficialmente — reportado, no decidido en silencio.

> ⚠️ **ESTE EPISODIO ERA EL EP.024 HASTA EL 2026-08-01.** Andy lo grabó, lo sintió
> «demasiado teórico, como una reseña», y decidió cambiar el tema y regrabar. Peter no se
> descartó: se reubicó a **EP.027**, como el pilar SEO de la primera vuelta de la rotación 3+1.
> El archivo se renombró de `pipeline-state-ep024.md` el 2026-08-01.
>
> **Todo lo que dice «EP.024» / «EP.24» más abajo es histórico** y se refiere a este episodio
> bajo su numeración vieja. No se reescribió: falsificaría el registro de cómo se produjo.
> El EP.024 real es otro episodio — ver `pipeline-state-ep024.md`.
>
> **⚠️ LAS PORTADAS HAY QUE REGENERARLAS, NO RECICLARLAS.** Los ~54 archivos quedaron en
> `E:\AI\outputs\BTQ-EP024-PETER-OBSOLETO\` (renombrada el 2026-08-01 desde `BTQ-EP024\`).
> Están rotos por los dos lados: llevan el título de Peter —inservibles para el EP.024 real— y
> tienen **`EP.24` horneado dentro de la imagen**, así que tampoco sirven para EP.027. El
> `titulo.txt` de esa carpeta se renombró a `titulo-PETER-VIEJO.txt` para que ningún script
> vuelva a hornear desde él.
>
> Peligro específico: esas portadas **no se ven viejas**. Están en el sistema visual vigente
> —tipografía pura, void, cream, señal— y solo tienen el título equivocado. Un asset roto que
> se ve roto lo caza cualquiera; uno impecable con el título de otro episodio, no.

## Guion — ESCRITO 2026-07-28

Archivo: `launch-assets/EP024-peter-guion.html` · Artifact:
https://claude.ai/code/artifact/b84b68c3-97d0-49e2-ae28-184e8e333740

**Título — RETITULADO 2026-07-28 con la fórmula invertida:**

```
EP.24 — Por qué su mejor empleado se vuelve un mal jefe: el Principio de Peter
```

78 caracteres (límite de YouTube: 100). Va idéntico en portada, Spotify y YouTube.
**Primer episodio con la fórmula nueva**: el problema al frente en las palabras del oyente, el
teórico detrás como autoridad. Ver `guion-style-btq.md` § Título para la evidencia que la motivó.

**Coherencia título ↔ guion (regla nueva, verificada):** la promesa se responde en el bloque DATO
del segmento 4 — «mientras más vendía la persona antes del ascenso, PEOR jefe resultó ser», con la
caída de 0,061 y el tercio de trabajador.

*Título anterior, descartado:* `EP.24 — Principio de Peter: por qué su mejor empleado se vuelve un
mal jefe` (71 car.). Mismo contenido, arrancando por un término que nadie busca.

**Esqueleto TRENZADO** (el D del menú de rotación) — primera vez que se usa. Dos hilos alternados
que no se resuelven hasta el segmento 5: A = la sátira de 1969, B = el paper de 2019. El invertido
se usó en EP.023 y el canónico sigue en pausa tras 4 usos seguidos.

**Tesis:** el ascenso no es un premio, es un cambio de oficio — y la empresa lo está usando como
sistema de pago.

| Lint | Resultado |
|---|---|
| `lint_guion_repeticion.py` vs 7 guiones | **PASS** — cero 6-gramas compartidos (primera pasada dio FAIL con 5; reescritas) |
| Duración | 5.525 palabras escritas → **42,2 min** con factor +13% (centro del estándar 40-45) |
| Muletillas | `imagínense` 0 · disclaimer de cajón 0 · puente-molde 0 |
| Moldes retirados en EP.023 | los 3 ausentes |
| Alcance | call center 0 · contact center 0 · BPO 0 |
| Tuteo | 0 |
| Remates | 3 (máximo 4) |
| Cierre canónico | las 7 piezas presentes + jingle de salida |
| Disclaimer de encuadre | 54 palabras (rango 35-55), con la mitad de «qué NO va a oír» |

**Primer episodio con disclaimer de encuadre.** Va en el segmento 0, entre el hook en frío y el
«Buenas y santas», después del jingle de entrada.

## Pasada de relleno y argumentos débiles 2026-07-31 (decisión de Andrés: opción 2)

Andrés detectó el incentivo estructural: **si el estándar de duración se mide en palabras
escritas, todo lo que alarga el texto sin alargar el audio empuja hacia la meta gratis** —
escribir las cifras en letras es la forma más barata, y el relleno argumental la siguiente.
Encargo: cortar relleno **y sustituirlo por sustancia verificada**, no solo recortar.

**Cortado (~355 palabras de relleno puro):** el mecanismo del Principio enunciado 5 veces
seguidas en el seg. 1 (quedan 2); la recepción del libro dicha 4 veces (quedan 2); el cierre
del seg. 2 que repetía la línea anterior con anáfora; la invisibilidad del daño dicha 3 veces
en el seg. 4 (queda solo el REMATE, que era el bueno); y las muletillas de tribuna
—«deténgase un segundo…», «la frase que a mí me dejó pensando varios días» y **«ahora, seamos
rigurosos, porque este pódcast promete evidencia»**, que anunciaba rigor en lugar de ejercerlo,
a tres líneas de las cifras de Barings sin verificar.

**Añadido (~270 palabras, todo verbatim del paper publicado):**

- **Robustez del equipo distinto** — «slightly stronger for managers assigned to a different
  team… unlikely to be driven by team-specific factors». Mata la objeción obvia («¿y si el
  equipo ya venía flojo?»), que el guion no respondía.
- **El 32% exacto** en vez de «alrededor de un tercio», y «duplicar no es raro: equivale a
  pasar del percentil 50 al 67» — dimensiona una premisa que se afirmaba sin dimensionar.
- **El hallazgo del ranking:** descontadas las ventas, **ser el nº 1 del equipo** sigue
  prediciendo el ascenso. No estaba en el guion. «Está premiando el podio.»

**Sobre-alcance corregido:** el guion explicaba *por qué* la colaboración predice un buen jefe.
El paper dice literalmente «**we cannot pinpoint the exact channel**». Ahora el guion lo dice:
«la correlación está medida; la explicación es de uno».

**Argumentos débiles reformulados (7):** «está llena de frases perfectas que resultaron falsas»
(generalización sin un solo ejemplo) · «cualquier manual de cualquier época» → «segregación de
funciones, lo primero que revisa cualquier auditoría» · doble apelación a consenso anónimo sobre
McClellan → una sola y atribuida · «al doble de su tamaño real» (cifra sin fuente) → retirada ·
«miles de personas pensando lo mismo» → retirada · «cada vez que lo mandan a vender» sobre 9
temporadas → acotado · «la que hizo que el libro se vendiera como pan caliente» → retirada.

**Duración: 5.577 → 5.492 palabras habladas = 42,6 → 41,9 min.** Dentro del estándar 40-45 sin
depender del relleno, que era el punto.

⚠️ **El diagnóstico de fondo sigue abierto:** los segmentos 1 y 3 son **1.382 palabras (25% del
episodio) sobre un libro que nunca se abrió en edición completa.** Ahí el relleno y la falta de
verificación son la misma cosa. Se recortó, no se resolvió.

## Cifras en numeral, no en letras (regla de Andrés, 2026-07-31)

19 cifras-dato pasadas a numeral. **Dos instrumentos míos sub-reportaron en cadena:** el
extractor de afirmaciones filtraba por dígitos (no vio las 16 cifras escritas en palabras) y el
segundo exigía que la cifra fuera seguida de `años|millones|mil|por ciento|libras`, así que no
vio «veintidós mil setecientas diecisiete **bajas**» ni «cinco **personas**». Dentro de lo que
no veían había un error real: «cincuenta y seis años» sobre un libro de 1969 — son **57**.

⚠️ **Efecto colateral no resuelto:** el modelo de duración cuenta palabras **escritas** y asume
que equivalen a palabras habladas. Un numeral rompe esa equivalencia (`827` se escribe como 1
palabra y se dice como 3), así que el modelo ahora **subestima**, y el sesgo crece con cuántas
cifras tenga el episodio. Medir el desfase contra el SRT real de EP.024 al transcribir.

## Re-verificación de fuentes 2026-07-31 — ANTES de grabar (2 errores corregidos)

Instrucción de Andrés: *«siempre revisa las fuentes porque después de que grabe te das cuenta que
no era como estaba en el guion»*. Se re-abrieron las fuentes primarias en vez de confiar en la
nota de la sesión del 07-28. **Dos afirmaciones estaban mal y se corrigieron en el guion:**

1. **Luisiana no es «un tercio del territorio».** 828.000 mi² sobre ~3,8 M ⇒ **~23%**.
   Corregido a «casi una cuarta parte».
2. **«La única cifra que aparece igual en el borrador de 2018 y en el estudio publicado»: falso.**
   Se bajaron las dos versiones y se compararon: además del 30% coinciden los **cinco
   subordinados por jefe**, **«casi un tercio de un trabajador»** y el periodo **2005-2011**.
   Corregido a «una de las pocas cifras que sobrevivió igual».

Otras dos, por precisión: la frase «the slows» es **atribuida** a Lincoln, no una cita
documentada (pasó a «se dice que le diagnosticó»); y Leeson, liberado el 3 jul 1999, cumplió
**3 a 7 m** desde la condena o **4 a 4 m** desde el arresto — «cuatro y medio» pasaba de los dos,
quedó en «poco más de cuatro». El QJE se publicó en **nov 2019**, así que «siete años» pasó a
«casi siete años».

**Se dejó SIN cambiar «dos canadienses»** (primera línea del episodio): Raymond Hull nació en
Inglaterra en 1919 **pero era un dramaturgo canadiense**, así que la frase es defendible. Se
señala por si alguien la cuestiona.

⚠️ **Trampa del PDF:** el que baja primero de NBER es el **borrador de 2018** — 214 empresas,
53.035 trabajadores, 1.531 ascendidos. Usarlo habría puesto TODAS las cifras del segmento 4
mal. La versión publicada está en la copia de la autora:
`http://danielle.li/assets/docs/PromotionsAndThePeterPrinciple.pdf`
(guardada en `E:\AI\outputs\BTQ-EP024\qje2019-publicado.pdf`).

**Confirmado textualmente en el paper publicado:** `131 different U.S.-based client firms` ·
`38,843 workers` · `1,553 of whom were promoted` · `5,956 managers` · `from 2005 to 2011` ·
`a 0.061 point decline in manager value added` (Tabla III col. 2) · `30% higher under this
counterfactual policy` · `almost one-third of one worker` sobre `five subordinates`.

**NO verificado en fuente primaria:** los £827 millones exactos (Britannica dice «roughly £830
million») y el «más del doble del capital del banco». El libro de Peter sigue sin abrirse en
edición completa.

## Fuentes — verificadas 2026-07-28, re-verificadas 2026-07-31 (ver arriba)

- **Peter & Hull 1969.** La formulación exacta está corroborada por la cita del paper de QJE y
  por fuentes enciclopédicas. **El libro NO se abrió en su edición completa**: la única copia
  íntegra en línea es un escaneo sin autorización y se descartó. Jerarquiología, incompetencia
  creativa y la autoría de Hull vienen de fuentes secundarias legítimas. No hay cita textual
  larga del capítulo 1 en el guion, a propósito.
- **Benson, Li & Shue (QJE 2019).** PDF abierto y leído directamente (Open Access CC BY-NC).
  Cifras usadas: 131 empresas · 38.843 trabajadores · 1.553 ascendidos · 5.956 jefes · 2005-2011
  (Tabla I) · +0,074 pp por duplicar ventas sobre una tasa mensual de 0,0023 (Tabla II col. 2) ·
  −0,061 de valor agregado y «casi un tercio de un trabajador» sobre un equipo de 5 (Tabla III
  col. 2) · +30% de calidad gerencial en el contrafactual.
- ⚠️ **No mezclar con el working paper de 2018** (NBER w24343): otra muestra —214 empresas,
  ~53.000 trabajadores, «14% más probable»— y es la versión que repite la prensa. El «15%» que
  circula sale de ahí. El guion usa SOLO las cifras publicadas.
- **Barings/Leeson 1995** (Britannica; National Library Board de Singapur) y **McClellan/Antietam
  1862, 22.717 bajas** (American Battlefield Trust, Britannica, Encyclopedia Virginia).
- **Little 1961**, *Operations Research* 9(3):383-387 — solo para el teaser de EP.025.

## Recomendaciones tejidas (grep: ninguna usada antes)

| Medio | Cuál | Segmento |
|---|---|---|
| Libro (referente) | *The Peter Principle*, 1969 | 3 |
| Serie | *The Office* — Michael Scott | 5 |
| Charla/video | «Why Is My Boss Incompetent?», Yale Insights 2018, con video de Kelly Shue | 6 |

## Métrica de seguimiento — minutos por reproducción

Spotify **no** entrega retención dentro del episodio (confirmado con Andy 2026-07-28: el único
archivo de retención es el semana-a-semana, y es ilegible con 1-3 oyentes por semana). El proxy
que sí sale de los exports normales, y que se anota en el `pipeline-state` de CADA episodio:

```
minutos por reproducción = horas de consumo x 60 / reproducciones
```

| Episodio | Min/reproducción | Nota |
|---|---|---|
| EP.022 | ~23-28 | ventanas aproximadas, n=9 |
| EP.023 | ~20,5 | 3,41 h / 10 reproducciones, ~60% de 33,77 min |
| EP.024 | *(pendiente)* | |

Es un proxy débil con estos volúmenes — sirve por tendencia a lo largo de 4-5 episodios, no por
el valor de un episodio suelto. **Alternativa mejor si hay vistas suficientes: YouTube Studio sí
da la curva de retención minuto a minuto** del mismo audio. Revisar cuántas vistas tiene el ítem
de EP.023 antes de sacar conclusiones de ahí.

## Corrección post-aprobación (2026-07-28, auditoría de la guía de estilo)

Una línea se reescribió **después** de aprobado, con visto bueno de Andy: traía
`todavía no les he mostrado`, el mismo andamiaje de EP.022 y EP.023 — tercero seguido. El lint
de 6-gramas lo dejó pasar porque difería en la última palabra; ahora hay un grep nominal en el
checklist. El guion sigue en PASS y dentro del estándar.

**Duración: 5.612 palabras escritas → 42,8 min**, contando `line + remate + dato +
mito/realidad + sub` y usando el factor y el wpm **medidos del SRT real de EP.023**
(×1,134 · 148,6 wpm), no heredados de ninguna nota.

Dos conteos malos aparecieron en el camino, ambos por el instrumento y no por el guion:

- regex con `(.*?)</` → 5.213 (39,8 min). Corta en el primer `</`, así que trunca toda línea
  con un `<strong>` adentro.
- extractor que solo miraba `line` y `sub` → 5.536 (42,3 min). Se saltaba los bloques `remate`
  y `dato`, que **sí se hablan**. Con las cinco clases, EP.023 da exactamente los 4.425 que
  registra la guía — o sea que el método correcto reproduce la cifra histórica.

**Riesgo abierto: el esqueleto D (trenzado) no tiene precedente medido.** El ×1,134 sale de
EP.023, que es esqueleto B con segmentos fusionados. Si D expande como los de segmentos
separados, EP.024 se va a 47,6 min (×1,26) o 52,9 (×1,40) — fuera del estándar por arriba.
Es el error recuperable (se corta), al revés que EP.023, que se quedó corto y eso no se
arregla en post. Al transcribir, **medir el factor real de D y anotarlo en la tabla de
esqueletos** de `guion-style-btq.md`.

## Artwork — PORTADAS LISTAS 2026-07-31

`E:\Podcast\BTQ\EP 24\BTQ Artwork EP 24\` — 1:1 (3000²) · 16:9 (1920×1080) · 9:16 (1080×1920),
más el JPG q92 y los reescalados de 300 y 96 px. Compuerta: `verify_assets.py --stage-a` **PASS**
(3 imágenes, negro de marca `#0E1113`, cero negro puro). Stage 2 leído a ojo en las tres.

**Al generarlas se destapó que el generador y la fórmula de título estaban en conflicto.**
`portada-ep-compose.py` se escribió el 2026-07-25 esperando un ancla de nombre propio
(`EFECTO HAWTHORNE`) y la dibujaba **una palabra por línea**. La fórmula invertida adoptada el
2026-07-28 —EP.024 es el primer episodio que la usa— hace que el ancla sea la frase del problema,
10 palabras. Resultado medido antes del arreglo:

| | ancla 1:1 | ancla 16:9 | legible a 96 px |
|---|---|---|---|
| EP.023 (fórmula corta) | 420 px | 216 px | sí |
| EP.024 sin arreglar | 232 px | **84 px** | no |
| EP.024 arreglado | 348 px | 168 px | sí |

Dos cambios en el script: el ancla se **envuelve por ancho** en vez de una palabra por línea, y el
paso de línea se calcula sobre **la tinta real** (con el avance fijo de `asize * 0.86` la tilde de
`QUÉ` chocaba con la pata de la `R`). Con un título de fórmula corta los tamaños vuelven idénticos
(420/216/152 px); el interlineado queda algo más ceñido, así que **no** es idéntico píxel a píxel
—medido con diff— pero ningún asset publicado cambia.

⚠️ **`scripts/banned-patterns.json` quedó viejo**: exige footer con dos filas de íconos y
`EP.0NN` a 3 dígitos, ambos retirados de `brand-constants.md` el 2026-07-25. No se tocó.

## Pendiente

- Quote cards: se componen DESPUÉS de grabar, contra la transcripción real.
- Grabación: dejar **3 s de silencio en cabeza y cola** (en EP.023 quedaron 0,59 s) + 30 s de
  room tone. El jingle varía respecto al de EP.023 manteniendo su formato.
- **Artículo en `/episodios/<slug>` + su `og:image`** — nuevo paso del kit desde 2026-07-28
  (ver `episode-launch/workflows/step2a-episode-article.md`). Se escribe antes del plan
  social, porque los 4 posts de LinkedIn se cortan de él; se **despliega el domingo**, junto
  con el episodio, para que el CTA de escucha tenga a dónde apuntar. Slug propuesto:
  `por-que-su-mejor-empleado-se-vuelve-un-mal-jefe` (derivado del título aprobado).
