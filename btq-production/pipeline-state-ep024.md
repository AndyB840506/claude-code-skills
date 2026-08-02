EPISODE: EP.024 (BTQ) — «Por qué su equipo no le cuenta los problemas»
stage_a: **cerrado** 2026-08-01 — guion v2 escrito, artwork cerrado, episodio grabado.
stage_b: **en curso** — grabación, transcripción, MP3 y carpeta de artwork listos; falta metadata.
stage_c: no iniciado.

## Estado de producción (2026-08-01, medido)

| Entregable | Ruta | Verificado |
|---|---|---|
| Audio máster | `E:\Podcast\BTQ\EP 24\BTQ EP 24 oficial.wav` | 41:26 · tomas `260801_1832`/`_1836` |
| MP3 publicación | `E:\Podcast\BTQ\EP 24\BTQ EP 24 oficial.mp3` | 128 kbps · −21,0 LUFS · TP −0,8 dBFS |
| Transcripción | `E:\Transcriptor\transcripciones\BTQ EP 24 oficial.srt` | 451 cues · último 41:08 · 1 hablante |
| Artwork | `E:\Podcast\BTQ\EP 24\BTQ Artwork EP 24\` | 1:1 3000² · 9:16 · 16:9 + JPEG q92 |

## URL de Spotify — PROVISIONAL, NO propagar

```
https://open.spotify.com/episode/25xgYzaTZmxEXqTNIu7yQp
```

Entregada por Spotify el 2026-08-01, antes del lanzamiento. **Sin verificar.** Al consultarla
ese día devolvió **HTTP 404**, que es lo esperable en un episodio no público pero que **no
distingue** entre «todavía no propaga», «el ID va a cambiar» y «el ID está mal».

El token `?si=…` de la URL compartida se descartó: es rastreo de compartir, no parte del
identificador. Nunca entra en el artículo ni en el JSON-LD.

**No está en ningún asset todavía.** El artículo sigue con `PENDIENTE-SPOTIFY-URL` en 2 sitios
(el CTA del cuerpo y el del riel) a propósito.

**Al lanzar el domingo, antes de propagarla:** abrir la página del episodio en el navegador y
copiar la URL de ahí, no de aquí. Si el ID cambió, este archivo queda obsoleto — es el caso
confirmado en EP.016, donde `pipeline-state-ep016.md` guardaba `episode/6GoODy…` como
«confirmada» y la URL real tras la re-subida era `episode/3CNyTkA6…`.

**Decisiones de Andy sobre el audio grabado (2026-08-01, no se regraba nada):**
- Nokia dice «4 de cada 10» en `10:04`, no «casi cuatro de cada diez» como el guion corregido.
  Fue improvisación deliberada para no sonar a guion. **Queda así**; el 37,8% real va en las
  fuentes, no en el audio.
- El dato de la cuadrilla reforzando la columna en Space (10 de los 12 muertos eran esos
  trabajadores) **no se dijo** y se deja fuera. Sigue disponible para show notes.
- «Grenfell» sonaba a «Greenfield» para WhisperX por pronunciación; corregido en el SRT
  (5 ocurrencias), el audio no se toca. También se corrigió «12 heridas» → «2 heridas» en `24:54`.
  El ASR crudo quedó en `BTQ EP 24 oficial-ASR-CRUDO.srt`.

**Pendientes de artwork, no bloquean:** la portada tiene 0,18% de píxeles `#000000` (el void es
`#0E1113` y `brand-constants.md` prohíbe el negro puro — sospecha: el degradado inferior), y las
contrapruebas de 300/96 px de 9:16 y 16:9 están en cuadrado, o sea deformadas.

**Los archivos de la era Peter se movieron a `E:\Podcast\BTQ\EP 27\`** el 2026-08-01. Sus
portadas **no sirven ahí**: llevan `EP.24` horneado dentro de la imagen.

> **Este episodio REEMPLAZÓ al del Principio de Peter el 2026-08-01.** Peter estaba grabado y
> se sintió «demasiado teórico, como una reseña»; se reubicó a EP.027 sin descartarse. Todo lo
> de Peter vive ahora en `pipeline-state-ep027-peter.md` — **no mezclar los dos**.

## Título

```
EP.24 — Por qué su equipo no le cuenta los problemas: seguridad psicológica
```

75 caracteres (límite de YouTube: 100). Va idéntico en portada, Spotify y YouTube.

Carril **Oficio de Jefe #1**. Andy escogió que el término buscable ganara sobre el gancho, igual
que en EP.023 con «Efecto Hawthorne». El string ofrecido primero —`Seguridad psicológica: por
qué…`— se corrigió porque invertía la fórmula fijada el 2026-07-28: **el problema va primero,
escrito como lo BUSCARÍA el oyente; el término técnico va detrás**.

La frase `mi puerta siempre está abierta` **no se botó**: es el hook hablado del segmento 0, que
es donde trabaja. No sirve como título porque es algo que un jefe *dice* en una reunión, no algo
que teclea en un buscador (regla nueva en `guion-style-btq.md` § Lo que el oyente DICE).

## Guion

Archivo: `launch-assets/EP024-puerta-abierta-guion.html`
Artifact: https://claude.ai/code/artifact/9a5078a8-3388-4582-97b9-48a71bc7851c

- **Esqueleto E — acción primero**, nunca usado antes. La recomendación cae en el minuto 2 y el
  resto del episodio la justifica. 9 segmentos.
- **Registro: ejecutivo relajado** (decisión de Andy 2026-08-01) — frases cortas, cero floritura
  literaria, el golpe lo da el dato.
- **5.405 palabras escritas ≈ 41,3 min** a 148 wpm con el factor +13% del esqueleto nuevo.
  ✅ **Cruzó el piso de 40 min** el 2026-08-01.
- **Compuertas medidas** con el script de conteo, no estimadas: aplicable **29,3%** (exige ≥25%)
  arrancando en el **2,7%** del guion (exige <60%).
- **5 dichos, uno por segmento, todos torcidos** (§ Dichos): leche/vaca · panadero · tapar el sol
  · el sordo negado · ojos que no ven. Segmentos 5 y 8 sin dicho, a propósito.

### Los cuatro casos y la taxonomía

Idea de Andy: no son cuatro ejemplos, son **cuatro formas distintas de que una mala noticia no
sirva**. El segmento 5 cierra recorriéndolas.

| Caso | Qué falló | Costo |
|---|---|---|
| Nokia 2007-2013 | el mensaje **nunca llegó** — filtrado en el camino | un mercado entero |
| Reficar + Hidroituango | **llegó y no importó** | plata pública · 17.000 evacuados |
| Edificio Space, Medellín 2013 | **llegó y lo parchearon** — «un amarre o una costura» | 12 muertos |
| Grenfell 2017 | era público y **castigaron al mensajero** | 72 muertos |

Dos de cuatro son colombianos y van de primeros — decisión de Andy: menos EE.UU., más
regionalidad. **Boeing descartado** (usado en EP.022, dentro de la ventana de 5 episodios).
**Columbia/CAIB parqueado**, no descartado.

Dato duro del mundo del oyente: **Edmondson 1999** — los mejores equipos reportaban MÁS errores.

## ⚠️ Pendientes antes de grabar

- [x] ~~Expandir ~250 palabras~~ — **hecho 2026-08-01**, 5.405 palabras = 41,3 min. Lo que
      expandió no fue relleno: fueron los dos hallazgos de la pasada de verificación.
- [x] ~~Verificar Edmondson y Nokia~~ — **hecho, y los dos traían error**:
      · **Nokia:** el guion decía «cuatro de cada diez teléfonos del planeta» en 2007. Gartner da
      **37,8% en el año completo**; el 40% se cruzó solo en el **cuarto trimestre**. Corregido.
      · **Edmondson:** el hallazgo de los errores es de **1996** (*Journal of Applied Behavioral
      Science*), no del paper de 1999 en ASQ, que es donde nombra la seguridad psicológica.
      Estaba mal atribuido. Corregido, y de paso el guion ganó el mecanismo real: las unidades
      que reportaban más eran aquellas donde las enfermeras confiaban entre sí.
- [x] ~~Space~~ — **hecho, y apareció el mejor dato del episodio**: la torre cayó **mientras una
      cuadrilla reforzaba una columna**, y **10 de los 12 muertos eran esos trabajadores**. La
      organización sí respondió a la advertencia; la respuesta misma mató gente. Añadido al
      segmento 4. Sentencia de 2022 del Tribunal Administrativo de Antioquia: >40.000 millones
      de pesos contra municipio, Lérida CDO, aseguradora y curadores urbanos.
- [x] ~~URL del post de Grenfell~~ — confirmada:
      `grenfellactiongroup.wordpress.com/2016/11/20/kctmo-playing-with-fire/`
- [x] ~~**FALTAN por abrir:** los informes de la Contraloría sobre Reficar e Hidroituango~~ —
      **abiertos el 2026-08-01**, ya no dependen de secundarias. Se bajó y leyó el **comunicado
      de prensa n.º 165 de la CGR (26 nov 2021)**: fallo en firme de Hidroituango por
      **$4.330.831.615.227,34** contra **26 personas naturales y jurídicas**, compuesto por
      $3.157.419.881.218,97 de destrucción del valor presente neto y $1.173.411.734.008,37 de
      lucro cesante. ⚠️ **El audio dice «1,1 y 2,9 billones», que son las cifras del informe
      especial ANTERIOR, no las del fallo.** No se corrige el audio (decisión de Andy); el
      artículo publica las dos en orden.
- [x] ~~**Conciliar las cifras de Reficar**~~ — **conciliadas el 2026-08-01**. Las tres cifras que
      circulaban son cosas distintas y la que aplica es la primera: **USD 997 millones =
      $2,9 billones** es el *fallo de responsabilidad fiscal* del **26 de abril de 2021**
      (ratificado en octubre de 2021) por mayores inversiones que no agregaron valor, contra
      2 presidentes, 3 vicepresidentes, 7 miembros de junta y 4 contratistas — que es exactamente
      la composición que el episodio nombra al aire. Confirmado además el incremento del
      presupuesto de **USD 3.993 a 4.854 millones el 7 de mayo de 2012** en la renegociación con
      CB&I, con análisis interno que advertía en contra. Sigue en pie el aviso: $2,9 billones
      aparece también en Hidroituango por otro concepto — no son la misma plata.
- [x] ~~**Lo de Echeverry golpeando la mesa va ATRIBUIDO**~~ — se cumplió: el audio lo dice como
      «él mismo contó años después que…». Es un relato del exministro, no un hallazgo de
      auditoría, y así queda también en el artículo.
- [ ] Correr `scripts/lint_guion_repeticion.py` contra EP.023 y contra el guion de Peter.
- [ ] ~~Definir el teaser del segmento 8~~ — **quedó genérico en la grabación** («estoy entre dos
      y las dos me gustan»). Ya no es accionable para EP.024; se cierra sin hacer.

## Artwork — EXCEPCIÓN, escena renderizada solo en este episodio

Decisión de Andy 2026-08-01: la portada vuelve a llevar ilustración, **solo para EP.024**. Del
EP.025 en adelante sigue la tipografía pura. Detalle y justificación en
`episode-launch/docs/brand-constants.md` § Excepción puntual.

**Concepto:** los tres monos —no ver, no oír, no hablar— **torcidos**: las manos que los tapan
entran desde fuera del cuadro, así que la imagen dice la tesis del episodio (alguien puso el
precio de hablar) en vez de la que el episodio demuele (ignorancia voluntaria).

**Seleccionada:** `E:\AI\outputs\BTQ-EP024-monos-r6\QUANT-crema.png` — cuantizada a las tres
tintas exactas de marca. Fuente sin cuantizar: `r6s2404_00001_.png`. Alterna: `r6s2202`.

- **Crema sobre void, medido:** contraste figura/fondo **16,55:1** contra **1,87:1** de la
  variante gunmetal, que a 96 px hacía desaparecer a los monos y dejaba solo brazos flotando.
- **Señal solo en los brazos** — verificado: 0,000% de naranja en el tercio inferior del cuadro.
- Seis rondas. Lo que las movió fue de Andy: pasar de render realista a dibujo, y señalar que la
  temática de maquinaria chocaba con la identidad. Eso último destapó que el cuerpo de
  `brand-constants.md` llevaba una semana desactualizado.

**Artwork CERRADO 2026-08-01.** Andy confirmó que va de portada, no a redes.

**Entregables:** `E:\AI\outputs\BTQ-EP024\` — `EP024-COVER-1x1.png` (3000x3000),
`-9x16.png` (1620x2880), `-16x9.png` (2560x1440), más contrapruebas de 300 y 96 px, la
ilustración base y la fuente sin cuantizar. `titulo.txt` con el string horneado.

- **Composición:** la ilustración NO llena el cuadro. Se recorta al contenido, se le quita el
  14% superior (solo brazos entrando) y se encaja entre el 25,5% y el 73,5% de la altura. Sin
  eso, el kicker `GESTIÓN · CALIDAD · LIDERAZGO` caía sobre la cabeza del primer mono y el
  degradado inferior griseaba las patas. Las tres proporciones se recomponen, no se recortan.
- **Legibilidad a 96 px verificada:** el wordmark se lee y el concepto —tres figuras con manos
  naranja tapándolas— se entiende. El título no se lee a ese tamaño; es el intercambio aceptado
  al ir con ilustración en vez de tipografía pura.
- **Bug encontrado y corregido:** `portada-compose.py` dimensiona el wordmark como fracción de
  la ALTURA, así que en 9:16 «THE QUEUE» se salía del cuadro. Se creó
  `comfyui/templates/portada-compose-ratios.py` — derivado, con el wordmark achicado hasta caber
  en el ANCHO. El original marcado `MUERTO` no se tocó.

## ⚠️ Assets obsoletos que NO se pueden reciclar

`E:\AI\outputs\BTQ-EP024-PETER-OBSOLETO\` (renombrada el 2026-08-01 desde `BTQ-EP024\`) tiene 54
archivos de la era Peter, incluidas **portadas terminadas y en el sistema visual vigente** que
solo tienen el título equivocado. No se ven viejas: se ven perfectas. Su `titulo.txt` se renombró
a `titulo-PETER-VIEJO.txt` para que ningún script vuelva a hornear desde él.

Tampoco sirven para EP.027, donde Peter vive ahora: llevan **`EP.24` horneado dentro de la
imagen**. Hay que regenerarlas.
