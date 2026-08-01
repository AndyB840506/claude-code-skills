EPISODE: EP.024 (BTQ) — «Por qué su equipo no le cuenta los problemas»
stage_a: **en curso** — guion v2 escrito 2026-08-01, artwork en selección.
stage_b: no iniciado (grabación, transcripción, assets).
stage_c: no iniciado.

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
- **5.162 palabras escritas ≈ 39,4 min** a 148 wpm con el factor +13% del esqueleto nuevo.
  ⚠️ **Sigue ~250 palabras corto** del piso de 40 min del estándar.
- **Compuertas medidas** con el script de conteo, no estimadas: aplicable **27,5%** (exige ≥25%)
  arrancando en el **2,9%** del guion (exige <60%).
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

- [ ] **Expandir ~250 palabras** para cruzar el piso de 40 min.
- [ ] **Abrir las fuentes primarias.** Ninguna se ha abierto; todo está corroborado entre
      secundarias. Faltan: informes de la Contraloría (Reficar e Hidroituango), informe técnico
      del colapso de Space, fallo del Tribunal Administrativo de Antioquia, post original del
      Grenfell Action Group (la URL que se intentó dio 404) y el paper de Edmondson.
- [ ] **Conciliar las cifras de Reficar.** Circulan ~USD 997 millones (~$2,9 billones), USD 2.879
      millones (~$8,5 billones) y USD 6.080 millones, y **son cosas distintas** — fallo de
      detrimento vs. daño detectado vs. monto del proceso. El guion **no dice ninguna**, a
      propósito. Ojo: $2,9 billones aparece también en Hidroituango por otro concepto.
- [ ] **Lo de Echeverry golpeando la mesa va ATRIBUIDO** («él mismo contó que…»). Es un relato
      del exministro de 2024, no un hallazgo de auditoría.
- [ ] Correr `scripts/lint_guion_repeticion.py` contra EP.023 y contra el guion de Peter.
- [ ] Definir el teaser del segmento 8 — hoy está genérico. EP.025 ya tiene tema.

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
