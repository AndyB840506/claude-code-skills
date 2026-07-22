# Guía de estilo de guion — Behind the Queue (BTQ)

> Consultar SIEMPRE antes de escribir un guion de BTQ (igual que MPD consulta su glosario de tono).
> Nace del feedback de Andy (2026-06-17): los guiones estaban "muy tiesos, les falta chispa".
> Referencia de narrativa con chispa: los guiones de MPD (ej. `mrputridsden-production/scripts/EP005-aterciopelados.html`).

BTQ es **solo host (Andy)**: conecta un referente pop (música, cine, juegos) con una lección de
liderazgo para un supervisor/gerente de BPO de ~40 años. La chispa no viene de banter entre hosts
(no hay co-host) — viene del ritmo hablado, la escena, el dato que sorprende, el humor y la calidez.

---

## Diagnóstico — qué pone "tieso" un guion BTQ (visto en EP.017)

1. **Frases de ensayo escrito, no de habla.** Oraciones largas con subordinadas y cadenas de
   guiones largos que nadie dice en voz alta sin sonar leyendo.
2. **Estructura formulaica.** Casi cada segmento termina en un `REMATE`. Mismo patrón
   hook → explicación → remate, una y otra vez. El oyente lo predice.
3. **Refrán-tesis repetido hasta el cansancio.** En EP.017 "seguir sonando/funcionando cuando ya
   no estés" aparece ~9× casi textual. Mata el impacto.
4. **Mismo conector siempre.** "Llévenlo a su piso", "Tradúzcanlo a su operación", "Piensen en su
   piso" — el puente referente→BPO se hace con la misma frase cada vez.
5. **Tono solemne parejo.** Todo es grave, importante, de TED talk. Cero humor, cero guiño, cero
   autoconciencia, cero sorpresa. Sin contraste, todo suena plano.

---

## Las 9 reglas de chispa (BTQ solo host)

1. **Escribe como Andy habla, no como se escribe.** Frases cortas, declarativas. Rompe las cadenas
   de guiones largos en 2-3 frases. Si una oración no se puede decir de un respiro, pártela.

2. **Varía el ritmo — no todo termina en REMATE.** Máximo ~3-4 remates por episodio, en los
   momentos de verdad. Los demás segmentos pueden cerrar con una pregunta, un dato seco, una
   imagen, o un silencio. La sorpresa vive en romper el patrón.

3. **Una tesis, dicha 2-3 veces máximo — y variada.** Elige el refrán central y ánclalo en 2-3
   momentos clave, cada vez con palabras distintas. Nunca repetir la misma frase textual >3×
   (lint obligatorio, ver abajo).

4. **Varía el puente referente→BPO.** Prohibido repetir "llévenlo a su piso / tradúzcanlo a su
   operación". Alternativas: una pregunta directa, una micro-escena del piso, un "a usted le pasó
   esto el martes", un dato de la operación, un personaje (el supervisor que…). El puente cambia
   cada vez.

5. **Abre con escena, no con anuncio.** En vez de "Hoy quiero arrancar con una pregunta", meter al
   oyente en una imagen: el estadio lleno, el piso a las 6pm un viernes, el chat del cliente
   explotando. Cinematográfico. "Imagínense" se permite, pero con presupuesto (máx 1, igual que MPD).

6. **Carne investigada y verificada — nunca inventada.** El sello es "la tarea hecha": datos
   reales, fechas, cifras, anécdotas poco conocidas pero ciertas. NUNCA inventar fuentes (en una
   versión de EP.017 se había citado un artículo HBR inexistente — se reemplazó por casos reales
   Jobs/Apple y Collins. Investigar en web antes de escribir; marcar lo no confirmado como
   [VERIFICAR]).
   **La verificación cubre también las pasadas de expansión/edición, no solo el primer
   borrador** (casi se cuela una cifra inventada de horas de vuelo del B-17 en una pasada de
   expansión de EP.022 — se detectó y se reemplazó por el dato real verificado antes de
   entregar). Cualquier dato nuevo agregado DESPUÉS del borrador inicial —al alargar,
   ilustrar o rematar un párrafo— se verifica igual que el material original, no se asume
   "de memoria" solo porque el tema ya se investigó antes.
   **Episodios atados a un momento cultural en curso** (un Mundial, unos premios, una serie del
   momento): anclar el guion en hechos históricos ya verificables y tratar el evento vivo solo como
   telón de fondo. NUNCA afirmar resultados del evento en curso si caen más allá del corte de
   conocimiento — marcarlos `[ACTUALIZAR AL GRABAR]` para que el host meta UN dato fresco y real al
   grabar, sin inventar (visto en EP.018 / Mundial 2026: las anécdotas son de 1950/1993/2014/2019;
   nada del torneo en curso se afirma como resultado).

7. **Mete humor, guiño y autoconciencia.** Andy solo, una hora — necesita contraste. Un chiste
   seco, admitir lo obvio ("sí, ya sé, otro que les habla de Cerati"), una exageración, un aparte.
   El humor no le quita peso a la lección: le da respiro para que la lección pegue más duro.

8. **Conectores de contenido, no meta-anuncios.** Prohibido "Aquí es donde BTQ deja de ser
   teoría", "ahora vamos a la parte aplicable". La última frase de un segmento ya engancha el
   siguiente. El oyente no necesita el índice.

9. **Concreto > abstracto. Una escena vívida vence a una lista.** En vez de enumerar 5 lecciones
   genéricas, elegir UNA y darle un personaje, un día, un detalle. El resto va más corto.

---

## ADN estructural de los episodios pilar SEO (fijado 2026-07-21, tras el giro a 100% pilar SEO)

Comparación EP.020 (Goodhart, "más profesional" según Andy) vs. borrador inicial de EP.023
(Hawthorne, sentía menos peso) confirmó qué es lo que hace que un pilar SEO pegue fuerte.
**No es una plantilla literal a repetir episodio tras episodio** — el tema, los casos y la
ejecución cambian siempre; esto es el ADN que debe estar presente, no el guion mismo:

1. **2-3 casos reales y NOMBRADOS, con consecuencias severas y verificables** (despidos,
   multas, cárcel, muertes) — no solo "la teoría y sus matices". EP.020 tuvo tres: Wells
   Fargo (fraude, 5.300 despedidos, multa), VA Hospital (muertes documentadas, renuncia de
   un secretario), Atlanta Public Schools (condenas penales bajo ley RICO).
2. **Los casos escalan en gravedad** a lo largo del episodio — el primero (negocios/plata),
   el de re-enganche el más grave (vidas humanas), el de Referencias Cruzadas en un mundo
   totalmente distinto a los dos anteriores.
3. **Un segmento con dato duro y verificado, específico de la industria de call center/BPO**
   (no solo de "otro mundo") — en EP.020 fue SQM Group (correlación FCR-CSAT 1:1). Sin esto,
   el episodio se siente teórico en vez de aplicable.
4. **El giro/re-enganche al 60% no tiene que ser siempre un caso más** — puede ser (como en
   EP.023 con el reanálisis de Levitt & List 2011) una vuelta de tuerca sobre el propio
   material ya presentado. Es un diferenciador válido, no una desviación del ADN, siempre que
   los 2-3 casos nombrados con consecuencias severas también estén presentes en el episodio.

**Antes de dar por buena la arquitectura de un pilar SEO nuevo**, verificar contra esta
lista: ¿hay al menos 2 casos reales y nombrados con consecuencias severas? ¿escalan? ¿hay un
dato duro propio de call center? Si falta alguno, buscarlo antes de escribir el guion
completo — no agregarlo después como parche.

---

## Frases de cajón prohibidas (detectadas 2026-07-21, feedback Andy)

EP.020 y EP.022 repitieron casi textual el mismo disclaimer autodesestimativo:
"Y no, tranquilos, [no me volví economista / esto no se convierte en un pódcast de
contabilidad] de un momento a otro — sigo sin [entender un balance general / saber
leer un estado de resultados], así que descuiden". Al aparecer dos veces seguidas ya
suena a fórmula, no a chispa espontánea (contradice la regla 3: "nunca repetir la
misma frase textual >3×" aplica también a frases *casi* idénticas entre episodios
distintos, no solo dentro de uno).

**No usar disclaimers de cajón tipo "tranquilos, esto no es un pódcast de X" para
aligerar un tramo técnico.** Si un segmento se pone denso, alivianarlo con la escena,
el humor específico del caso, o una pregunta directa al oyente — nunca con una
disculpa genérica por hablar de números/teoría. Antes de entregar un guion, releer
contra los guiones anteriores (no solo el propio) buscando este tipo de muletilla
estructural repetida.

## Título con nombre del creador cuando el episodio ancla en una ley/teoría específica

**Feedback Andy (2026-07-21):** cuando el episodio gira alrededor de una ley o teoría
con autor identificable (ej. Ley de Goodhart, Philip Crosby / Cost of Poor Quality),
el título debe nombrar a ese creador — no solo describir el concepto en abstracto.
EP.020 y EP.022 no lo hicieron (títulos genéricos: "Métricas y KPIs...", "El Costo de
la Mala Calidad...") y quedó como oportunidad perdida de anclar autoridad y
searchability real. Aplica principalmente a episodios **pilar SEO** (sin referente
pop) — los pop-culture siguen la fórmula `EP.XX — [Referente]: [frase con keyword]`
de abajo, que ya trae su propio ancla de búsqueda.

---

## Estructura canónica del episodio (pop-culture) — seguir desde el primer borrador

Derivado de comparar EP.018 (completo) vs. un primer borrador de EP.019 que se quedó corto
(feedback Andy 2026-06-26: "se encasilló en el referente, le faltó el cierre"). Un episodio
BTQ pop-culture lleva, en orden, estos bloques. No omitir ninguno al escribir el borrador:

1. **Apertura** (ritual: "Buenas y santas…") + **Hook** en escena.
2. **El Puente** referente → supervisor BPO (a veces enlaza con el episodio anterior).
3. **Cuerpo** (2-4 segmentos): la tesis desarrollada con el referente. Dentro de estos
   segmentos, meter **datos de interés** puntuales — verificados, poco conocidos, con ángulo
   de "esto no te lo esperabas, cuéntaselo a alguien" (incluye separar mito de realidad del
   referente cuando aplique, ej. qué inventó Hollywood vs. qué pasó de verdad). Van pegados al
   momento de la anécdota, no en un bloque aparte. No forzar uno por segmento — solo donde el
   dato realmente sorprenda (evitar volverlo fórmula, ver regla 2).
   [Cambio 2026-07-04: antes vivía como bloque final "Mito o Realidad"; la curva de retención
   de EP.012 y EP.018 mostraba que ahí es exactamente donde el oyente abandona — se movió al
   cuerpo y se reencuadró de corrección académica a dato compartible.]
4. **Re-enganche al ~60%**: el dato/giro más fuerte va en la segunda mitad, no en el primer
   tercio (completion rates 50-67%).
5. **Referencias Cruzadas — FUERA del referente.** Traer 2 ejemplos reales y verificados del
   MISMO tema pero de otro mundo (otra época, otro oficio, otro país). NO quedarse solo dentro
   de la película/banda del episodio. Ej. EP.018: Zander (director de orquesta) + Ferguson.
   EP.019: Sócrates + John Wooden. Es lo que hace el episodio universal y no un resumen del
   referente.
6. **Aplicable Hoy**: 3 cosas concretas para esta semana.
7. **Recomendaciones de Andy — diversificadas.** Máximo UNA atada al referente (la peli/disco
   del episodio); las otras saltan fuera (un libro de otro mundo, una charla, otra peli). NO
   las tres dentro del mismo tema/época. Mezclar medios: película + libro + charla.
   **Nunca repetir la misma recomendación (ni la misma referencia cruzada) entre episodios**
   (feedback Andy 2026-07-21). Antes de cerrar las 3 recomendaciones o las referencias cruzadas
   de un guion nuevo, grepear `btq-production/launch-assets/*.html` por el título candidato — si
   ya apareció en otro episodio, descartarlo y buscar otro. Precedente: EP.023 (Matrix) descartó
   "Moneyball" (ya en EP.020) y "Sully" (ya en EP.022) por esta regla, y confirmó por grep que
   Baudrillard / Kathryn Schulz / The Big Short no se habían usado antes.
8. **Cierre canónico** (NO omitir nada de esto — es la firma de BTQ):
   - **Pregunta comentable** que interpela al oyente sobre SU situación.
   - **CTA de comentarios:** "escríbanlo en los comentarios del episodio, en Spotify, los leo
     todos" (+ guiño a los comentarios del episodio anterior).
   - **CTA de compartir** ("si esto les hizo pensar en alguien, compártanlo").
   - **Redes:** LinkedIn — "estoy en LinkedIn como Andrés Bermúdez Rodríguez".
   - **Teaser** del próximo episodio (bien armado, no una nota suelta).
   - **Firma + TM canónico:** "Yo soy Andy. Y recuerden: [tesis del episodio en una frase
     memorable]" + nota OUTRO MUSICAL.

## No dar señales de cierre falso antes del Cierre real (retención Spotify, fijado 2026-07-06)

Según la data de permanencia/completion de Spotify, cualquier momento del episodio que **suene**
a final —una frase que cierra un círculo, un tono de aplauso, un remate demasiado conclusivo, un
segmento que "resuelve" del todo— le da al oyente el permiso mental de dejar de escuchar ahí,
aunque el episodio siga. El oyente no abandona solo por aburrimiento; abandona en el momento exacto
en que algo *suena* a que ya terminó.

**Los puntos de mayor riesgo, por diseño de la estructura canónica, son los REMATES de segmentos
intermedios y el tramo Aplicable Hoy → Recomendaciones** (posiciones 6-7 de 8) — ambos, en casi
cualquier pódcast, funcionan culturalmente como "señal de que ya casi se acaba".

**Mitigación obligatoria — condición → acción → verificación:**
- Cuando un REMATE de un segmento que NO es el cierre final quede redactado con tono de conclusión
  total (una frase que "amarra" el tema sin dejar nada abierto), reescribirlo para que tire hacia
  adelante — una pregunta sin responder, un hilo que se retoma después, nunca un punto final
  emocional. Verificar releyendo cada REMATE fuera del Cierre y preguntando: "¿esto suena a que el
  episodio podría terminar aquí?" Si la respuesta es sí, reescribirlo.
- Antes de entrar a Aplicable Hoy o a Recomendaciones, meter una línea corta de enganche que le
  diga al oyente, sin sonar a anuncio de índice (regla 8, sin meta-anuncios), que todavía viene algo
  que vale la pena — ej. una referencia a la pregunta del cierre, un "todavía no les he dicho la
  parte que más le tocó a X" — nunca un simple "y ahora, unas recomendaciones" que suena a que el
  contenido real ya se acabó.
- Verificar en la lectura final: ningún bloque antes del Cierre canónico debe poder funcionar,
  por sí solo, como final satisfactorio del episodio si se cortara ahí.

## Voz narrativa — "MPD meets TED", no documental BBC (feedback Andy 2026-06-26)

Los tramos históricos/expositivos son los que más fácil caen en modo informe ("esto pasó,
luego esto, esto significa X"). Reescribirlos en voz narrativa de escena:

- **Presente, no pasado.** "Roma. 31 de diciembre del 192. El hombre más poderoso del mundo
  se está alistando…" mete al oyente AHÍ; "el último día del 192 lo mataron" solo lo reporta.
- **Ritmo staccato emocional** en los beats clave: frases cortas, declarativas, encadenadas.
- **"Ubíquense / Métanse en esto"** para poner al oyente en la escena (sin gastar el
  presupuesto de "imagínense").
- **El giro descubierto** ("Y aquí está lo que casi nadie ve…") en vez de explicar la lección.
- Referencia de técnica: los guiones de MPD (`mrputridsden-production/scripts/`).

## Regla de 2 partes (igual que MPD)

Si la data y las anécdotas dan para más de ~50 min de contenido con chispa (sin relleno) — es decir,
si no caben cómodos dentro del estándar de 40-45 min sin recortar material real — **partir en 2
episodios** desde el guion, en vez de forzar el recorte o pasarse del estándar. Razón: la
investigación profunda + anécdotas ciertas poco conocidas suelen pasarse del rango objetivo (ver
memoria `project-mpd-episodes-two-parts`). Estructurar
el corte natural desde el inicio; cada parte con su propia apertura/cierre y un recap de ~20 seg al
abrir la Parte 2. Ojo: BTQ tiene cadencia semanal estricta (≥7 días entre episodios) — 2 partes =
2 semanas, encaja con el roadmap.

---

## Calibración de duración — dimensionar en PALABRAS, no en minutos adivinados

Regla medida (no de gusto). El guion se dimensiona contando **palabras habladas** y dividiendo por
el ritmo real de Andy, **no** estimando minutos "a ojo" por segmento. Las marcas de minutos por ojo
salen infladas y hacen que Andy termine ~15 min antes de lo marcado y tenga que estirar.

**Estándar editorial de duración (BTQ y CCC, fijado 2026-07-06):** el episodio debe caer **entre 40
y 45 minutos de contenido hablado**, sin contar intro ni outro musical. No es un mínimo sugerido ni
un techo aspiracional — es el rango objetivo. Si el guion mide por debajo de 40 o por encima de 45
(con la fórmula de abajo), expandir o cortar antes de aprobar el guion para grabación, no dejarlo
para la edición.

**Ritmo real de Andy ≈ 150 palabras/min** (recalibrado 2026-07-06 contra el SRT del EP.20:
`E:\Transcriptor\transcripciones\BTQ EP 20.srt` — 6.192 palabras habladas por el host / 41,28 min de
habla efectiva, sin contar intro/outro musical. Cifra anterior de 143 wpm venía del SRT del EP.17,
sigue siendo la referencia correcta si el ritmo de Andy vuelve a bajar). Ese número **ya incluye sus
pausas** — es ritmo de entrega, no de lectura en seco. Diagnóstico EP.17: estaba marcado a "57 min"
(≈90 wpm imaginario) y cayó en ~42-45. EP.18 v1 tenía 4.213 palabras = ~29 min reales aunque estaba
marcado a 52.

**Expansión real en vivo recalibrada:** el EP.20 tenía un guion escrito de 4.570 palabras y terminó
en 6.192 palabras habladas — una expansión real de **+35.5%**, no el +15% que se asumía antes (ver
"Ajuste por expansión" abajo, cifra vieja basada solo en EP.17). Usar +35.5% como referencia actual;
recalibrar de nuevo si el patrón cambia en 2-3 episodios más.

**Tabla de dimensionamiento (palabras habladas → minutos a 150 wpm, recalibrado 2026-07-06):**

| Objetivo real | Palabras habladas | Palabras ESCRITAS (con +35.5% expansión) |
|---|---|---|
| 40 min (piso del estándar) | ~6.000 | ~4.430 |
| 42.5 min (centro del estándar) | ~6.375 | ~4.705 |
| 45 min (techo del estándar) | ~6.750 | ~4.980 |
| >50 min (fuera del estándar → evaluar 2 partes) | ~7.500+ | ~5.535+ |

**Ajuste por expansión en vivo (recalibrado 2026-07-06):** el dato de EP.17 (guion 5.265 → habló
6.062, +15%) resultó ser un piso, no el promedio — el SRT real de EP.20 mostró **+35.5%** (guion 4.570
→ habló 6.192). Usar +35.5% como referencia actual hasta la próxima recalibración. Por eso conviene
escribir el guion para que **en seco** caiga bien por debajo del objetivo hablado, y dejar que la
expansión natural de Andy lo lleve al número real — ver tabla arriba para la conversión ya aplicada.
**Siempre dejar colchón para CORTAR, no para estirar.**

**Cómo medir** (excluir lo que no se lee: bloques `NOTA`, chips `PAUSA`, encabezados de segmento,
tabla de arquitectura): contar palabras de `p.line` + `remate` + `dato` + `mito/realidad` + `sub`,
multiplicar por 1.355 (expansión verificada) y dividir por 150 (wpm verificado) — no dividir
directo por 143 sin aplicar la expansión, ese método subestima la duración real. Marcar los tiempos
de la arquitectura en consecuencia.

**Recalibrar** el 150 wpm y el +35.5% cada pocos episodios contra el SRT más reciente (los SRT viven en
`E:\Transcriptor\transcripciones\`); si su ritmo cambia, actualizar este número y la tabla.

---

## Antes / Después (ejemplo real, estilo BTQ)

**ANTES (tieso — estilo EP.017):**
> "Hay un momento — y la mayoría de los líderes de operaciones lo viven sin darse cuenta — en el
> que un guion de atención, un flujo de escalación, una forma de medir desempeño, deja de estar
> resolviendo el problema para el que se diseñó, y empieza simplemente a funcionar por inercia.
> Nadie lo cuestiona, porque 'así se ha hecho siempre' y los números siguen saliendo en verde."

**DESPUÉS (con chispa):**
> "Piensen en ese guion de atención que llevan tres años usando. El que nadie toca porque 'convierte
> bien'.
> [PAUSA]
> Déjenme adivinar: nadie se acuerda quién lo escribió. Y el día que alguien preguntó por qué se
> hace así, la respuesta fue 'porque siempre se ha hecho así'.
> [PAUSA]
> Eso no está funcionando. Eso está sobreviviendo. Y hay una diferencia enorme."

Qué cambió: frases cortas decibles · un guiño ("déjenme adivinar") · una imagen concreta · un remate
seco por contraste, no por fórmula · cero cadena de guiones largos.

---

## Lint antes de entregar un guion BTQ

- [ ] Refrán-tesis: contar ocurrencias casi textuales del refrán central → **máx 3**.
- [ ] Remates: contar bloques `REMATE` → **máx ~3-4 por episodio**, no uno por segmento.
- [ ] Puente referente→BPO: que NO se repita la misma frase ("llévenlo a su piso") — variar cada vez.
- [ ] Muletillas: máx 1 "imagínense", 0 "me vuela la cabeza" (igual que MPD).
- [ ] **Sin disclaimers de cajón** tipo "tranquilos, esto no es un pódcast de X" para
      aligerar un tramo técnico (repetido casi textual en EP.020/EP.022 — ver sección
      dedicada arriba). Si el título ancla en una ley/teoría con autor, confirmar que
      el nombre del creador está en el título.
- [ ] **Sin "Andy" en tercera persona dentro del guion hablado** (detectado 2026-07-21,
      EP.023 borrador Hawthorne: "del tipo que Andy, personalmente, desconfía..." — debía
      ser "yo, personalmente, desconfío"). BTQ es solo host narrando en primera persona
      todo el episodio; "Andy" en tercera persona solo es válido como etiqueta de sección
      ("Recomendaciones de Andy") o en la firma canónica del cierre ("Yo soy Andy").
- [ ] Frase larga: ninguna oración que no se pueda decir de un respiro; partir las cadenas de guiones.
- [ ] Al menos 2-3 momentos de humor/guiño/autoconciencia repartidos.
- [ ] Datos verificados (fuentes reales, nada inventado); lo dudoso marcado [VERIFICAR].
- [ ] **Vocabulario accesible:** cero palabras que el host/audiencia no usen al hablar
      (regionalismos raros, cultismos, tecnicismos). Cazar y reemplazar por habla natural —
      ej. rechazados: "galones", "desperdigado", "embestida", "factura final", "telón de
      fondo". Si dudas si una palabra "se entiende", cámbiala.
- [ ] **Estructura canónica completa** (ver sección arriba): ¿están Referencias Cruzadas
      FUERA del referente, recomendaciones diversificadas, y el cierre canónico entero
      (comentarios Spotify · compartir · LinkedIn · teaser · firma + TM · outro)? No omitir.
- [ ] **Sin bloque "Mito o Realidad" al final:** los datos de interés / mito-vs-realidad van
      distribuidos dentro del Cuerpo, no como segmento aparte antes del cierre.
- [ ] **Sin señales de cierre falso antes del Cierre real** (ver sección dedicada arriba): releer
      cada REMATE que no sea el del Cierre y confirmar que tira hacia adelante, no que suena a
      final. Confirmar que hay una línea de enganche antes de Aplicable Hoy o Recomendaciones,
      no un salto directo que suene a que el contenido real ya terminó.
- [ ] **Voz narrativa, no documental:** los tramos históricos en presente/escena, no en
      modo informe.
- [ ] Aperturas y conectores de contenido (sin meta-anuncios tipo "ahora vamos a…").
- [ ] Duración: contar **palabras escritas × 1.355 (expansión) / 150 (wpm)** (ver "Calibración de duración", recalibrado 2026-07-06 contra SRT real de EP.20) — NO estimar minutos a ojo, NO usar 143 wpm / +15% (cifras viejas, basadas solo en EP.17). El resultado debe caer **entre 40 y 45 minutos** (estándar editorial, sin contar intro/outro musical) — si queda fuera de ese rango, expandir o cortar antes de grabar, no dejarlo para después.
