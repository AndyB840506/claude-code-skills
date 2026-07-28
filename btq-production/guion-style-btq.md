# Guía de estilo de guion — Behind the Queue (BTQ)

> Consultar SIEMPRE antes de escribir un guion de BTQ (igual que MPD consulta su glosario de tono).
> Nace del feedback de Andy (2026-06-17): los guiones estaban "muy tiesos, les falta chispa".
> Referencia de narrativa con chispa: los guiones de MPD (ej. `mrputridsden-production/scripts/EP005-aterciopelados.html`).

BTQ es **solo host (Andy)**: le explica a un supervisor/gerente de BPO de ~40 años una ley, teoría
o principio real de gestión, bajado al piso con casos verificados. La chispa no viene de banter
entre hosts (no hay co-host) — viene del ritmo hablado, la escena, el dato que sorprende, el humor
y la calidez.

> **Carril vigente: 100% pilar SEO** (giro del 2026-07-21). El carril **pop-culture** —conectar un
> referente de música, cine o juegos con la lección— está **en pausa**, no retirado: las reglas que
> hablan de «el referente» siguen escritas porque sirven si vuelve, pero **no aplican hoy**. Fuente:
> `roadmap-btq.md` § Reglas retiradas.

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

7. **Mete humor, guiño y autoconciencia.** Andy solo, 40-45 minutos — necesita contraste. Un chiste
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

---

## Español neutro: neutro en el diccionario, Andy en el micrófono (feedback Andy 2026-07-25)

El show se escucha en toda Latinoamérica. Se escribe en **español neutro**, pero neutro en el
sentido del doblaje profesional: **es un estándar de léxico, no de voz.** Regula qué palabras se
usan, no cómo suena Andy.

**Esto NO es licencia para aplanar el guion.** El fallo característico de un guion BTQ es salir
*tieso* (ver el Diagnóstico que abre esta guía), y las reglas 1 y 7 de chispa existen justamente
para evitarlo. Neutro mal entendido suena a locutor de aeropuerto — y eso es peor que un
regionalismo.

| Neutro SÍ regula | Neutro NO toca |
|---|---|
| Palabras ancladas a un país | Frases cortas y declarativas (regla 1) |
| Palabras con segundo sentido regional | El chiste seco, la autoconciencia (regla 7) |
| Voseo y vosotros → `usted` / `ustedes` | El ritmo staccato, la escena en presente |
| Modismos que hay que explicar | Meterse con el oyente, la ironía, el aparte |

**La prueba:** un oyente en México o Argentina, sin contexto colombiano, ¿entiende la frase sola
y sin que se le explique? Si sí, se queda aunque sea coloquial —*"sí, ya sé, otro que les habla
de Cerati"* viaja perfecto—. Si no, se reescribe.

### 1 · Palabras ancladas a un país (cambiar)

`tinto` (en Colombia es café negro; en el resto de la región es vino tinto — el caso ejemplar),
`parcero/parce`, `chino` o `pelado` por niño, `bacano`, `berraco`, `man`, `vaina`, `camello` por
trabajo, `jartera`, `tusa`, `ahorita` (significa cosas distintas según el país). También
`chévere`, que viaja al norte andino pero no al Cono Sur ni a México.

*Borderline, decidir por caso:* `plata` por dinero — se entiende en toda la región aunque México
prefiera `dinero`. Aporta textura; no está prohibida, pero si un párrafo ya va cargado de
colombianismos, esta es la primera que cae.

### 2 · Palabras con segundo sentido regional (cazar siempre)

`coger` (normal en Colombia, vulgar en México, Argentina, Uruguay y Chile — usar *tomar*),
`concha`, `pico`, `pinche`, `chucha`, `papaya`, `verga`, `culo`, `bicho`.

### 3 · El caso `cola` — y el nombre del show

`cola` significa «trasero» en buena parte de la región. En el piso de un contact center nadie lo
oye así: es el término de la industria y se usa veinte veces al día. El problema no es la
palabra, es la **construcción** — cuando se despega del contexto técnico y queda sola con un
adjetivo físico, el segundo sentido se activa solo.

- ✅ *"la cola de llamadas"*, *"la teoría de colas"* — el contexto operativo la ancla.
- ✅ Alternativas limpias: *"la fila de llamadas"*, *"el volumen en espera"*, *"los casos
  represados"*, *"el backlog"*.
- ⚠️ *"la cola en rojo"*, *"ver la cola crecer"* (EP.018, EP.019) — limítrofes; el color y el
  verbo salvan el contexto, pero por poco.
- ❌ `cola` + adjetivo corporal o de tamaño: *"reventada"*, *"apretada"*, *"grande"*.
  Ya salió al aire así: *"La cola está reventada"* (EP.018).

**El nombre del show NUNCA se traduce.** «Behind the Queue» se dice y se escribe en inglés
siempre, incluso a mitad de una frase en español. La traducción literal es impublicable, y por
eso la metáfora de la cola (ver `brand-constants.md`) vive en inglés en la marca y solo baja al
español como *fila / espera / backlog* dentro del guion.

> Las listas de arriba son un punto de partida, no un inventario cerrado. Ante una palabra con
> sabor local que no esté listada, aplicar la prueba del párrafo inicial.

## Título: el PROBLEMA va primero, y el teórico después como autoridad

**Fórmula obligatoria de los episodios pilar SEO — INVERTIDA el 2026-07-28 (decisión de Andy
sobre los analytics del catálogo):**

```
EP.NN — [El problema, dicho como lo diría el oyente]: [el teórico o la ley que lo explica]
```

**Por qué se invirtió — está medido, no es gusto.** Cruzando impresiones contra tiempo de consumo
de los episodios publicados después del 28-abr-2026 (misma ventana en ambas métricas):

| Episodio | Impresiones | Min escuchados por impresión | % desde búsqueda |
|---|---|---|---|
| EP.20 `Ley de Goodhart` | 143 | **4,57** | 25,2% |
| EP.18 `El Mundial` | 124 | 3,15 | 4,8% |
| EP.16 `The Wall` | 153 | 2,59 | 32,0% |
| EP.12 `Bohemian Rhapsody` | 286 | 2,18 | 44,8% |
| EP.14 `MAOMAO` | 227 | 1,69 | 52,9% |
| EP.17 `Soda Stereo` | 341 | **0,98** | 61,3% |

Tres cosas salen de ahí:

1. **Mientras más impresiones vienen de búsqueda, PEOR convierten** — la relación es casi monótona.
   Quien busca «Soda Stereo» quiere a Soda Stereo; le sale un pódcast de gestión y se va en menos
   de un minuto. Y ojo: **EP.17 sí entregaba Soda Stereo.** No falló por engañar, falló porque esa
   gente nunca iba a ser la audiencia. La puerta de cultura pop no sirve ni cumpliendo la promesa.
2. **Los nombres de teorías dan intención sin alcance.** Nadie busca «Principio de Peter».
3. Lo único que tiene alcance **y** intención es **el problema en las palabras del oyente** — que
   además es literalmente cómo se le pregunta a una IA, así que la misma decisión sirve para
   posicionarse en búsqueda y en respuestas de modelos.

> **Corrección a una creencia del roadmap.** Está escrito que EP.020 «probablemente rankeó por la
> keyword call center», y sobre eso se aceptó el costo del giro macro del 2026-07-25. Los datos
> dicen otra cosa: EP.020 recibió **36 impresiones de búsqueda** en 22 días (EP.017 recibió 209) y
> **102 de sus 143 impresiones vinieron del Home** de Spotify. EP.020 no ganó por SEO — ganó por
> **conversión**. Lo que hay que replicar de EP.020 no es su keyword: es que su tema le importó a
> la audiencia que ya existe.

**Ejemplo del cambio, con EP.024:**

```
Antes:  EP.24 — Principio de Peter: por qué su mejor empleado se vuelve un mal jefe
Ahora:  EP.24 — Por qué su mejor empleado se vuelve un mal jefe: el Principio de Peter
```

La autoridad no se pierde: se mueve tres palabras a la derecha. Y el título deja de prometer un
referente que después hay que honrar — promete la tesis, que es lo que el episodio ya entrega.

### Registro histórico — la fórmula anterior (2026-07-25 → 2026-07-28)

*Esto describe lo que se hacía antes, no lo que se hace ahora.* La fórmula pedía
`[Teórico o ley que lleva su nombre]: [qué es, en llano, en usted]`, con el nombre propio «al
frente y solo» por efecto de autoridad. Bajo esa regla se titularon EP.020, EP.022 y EP.023.
Lo que **sigue vigente** de esa etapa está abajo: el veto al título-eslogan, el caso Hawthorne y
la regla de que portada y metadata comparten string.

**Alcance del aterrizaje (giro macro, 2026-07-25; reubicado al invertir la fórmula el 2026-07-28):**
el aterrizaje en «su equipo», «su operación» o «su empresa» ahora vive en el **primer** tramo —es
el problema mismo, dicho en segunda persona— y ya **no** en «su call center». La teoría puede venir de donde
sea (manufactura, aviación, software, economía); lo que se mantiene es que baje al piso.
Única excepción deliberada: **EP.020 no se retitula** aunque diga «call center» — pero
**no por la keyword**. La corrección de arriba lo mide: EP.020 recibió 36 impresiones de búsqueda
y 102 de sus 143 vinieron del Home; no ganó por SEO. Se deja quieto porque es el **único episodio
con desempeño medido**, y cambiarle el título destruye la única línea base que existe para
comparar. Ver `btq-production/metadata-v4-macro.md`.

Lo que va antes de los dos puntos es **el problema, en las palabras del oyente** — la frase que
esa persona escribiría en un buscador o le preguntaría a una IA. Después de los dos puntos, el
teórico o la ley, que aporta la autoridad y el término técnico.

- **Bien — EP.24:** `Por qué su mejor empleado se vuelve un mal jefe: el Principio de Peter`.
  El problema al frente en lenguaje de persona; la teoría detrás, sosteniéndolo.
- **Mal — la fórmula vieja:** `Principio de Peter: por qué su mejor empleado se vuelve un mal jefe`.
  Arranca con un término que nadie busca. El contenido es idéntico; el descubrimiento no.
- **Mal — EP.22 publicado:** `La Calidad Es Gratis: el costo real de la mala calidad…`.
  "La Calidad Es Gratis" es el título del libro de Crosby y **suena a eslogan de
  marketing**, no a fuente consultable. Este veto sigue vigente: **el ancla nunca es el título
  de un libro ni una frase con sabor a publicidad**, vaya donde vaya en el título.
- **Mal — puerta de cultura pop:** `Soda Stereo: el liderazgo que sigue sonando…`. Trae mucha
  impresión y casi ningún oyente (0,98 min por impresión, el peor del catálogo), **incluso
  cumpliendo la promesa**. No usar un referente pop como ancla de descubrimiento.

**La promesa del título tiene que poder señalarse en una línea concreta del guion** (fijado
2026-07-28, a raíz de una pregunta de Andy: «si menciono algo en el título y no lo desarrollo, la
gente siente que le metieron gato por liebre»). Antes de aprobar el título, ubicar **la frase
exacta del guion que lo responde**. Si no se puede señalar con el dedo, el título está mintiendo
aunque sea sin querer. La fórmula problema-primero hace esto casi automático —el título promete la
tesis, no un referente— pero se verifica igual, porque el riesgo aparece cuando el título se
escribe antes que el cuerpo.

**Caso especial — resuelto 2026-07-25 (EP.023), sigue vigente para la SEGUNDA mitad.** Cuando el
efecto se conoce por un nombre que NO es el del teórico (*efecto Hawthorne*, por la fábrica; el
investigador fue Elton Mayo), **gana el término reconocible**, siempre que sea un nombre propio y
no un eslogan: el modelo es *[tipo] de [nombre propio]* — `Ley de Goodhart`, `Efecto Hawthorne`,
`Principio de Peter`. `Elton Mayo` a secas sería el equivalente a poner «Goodhart» solo. Con la
fórmula invertida esta decisión ya no afecta el descubrimiento —para eso está el problema al
frente— pero sí la autoridad, así que se mantiene. Sigue siendo consulta con Andy si un caso
futuro no encaja.

**El título de la portada y el título publicado son el MISMO string.** La incongruencia
entre artwork y metadata nace de aplicar criterios distintos en cada uno; se evita
resolviendo el título una sola vez, antes de generar la imagen.

Los episodios **pop-culture** (carril en pausa desde el giro del 2026-07-21) siguen la
fórmula `EP.XX — [Referente]: [frase con keyword]` de abajo, que trae su propio ancla.

---

## Estructura canónica del episodio — seguir desde el primer borrador

> **Aplica a TODOS los episodios, incluidos los pilares SEO** (aclarado 2026-07-28). Esta sección
> llevaba el rótulo «(pop-culture)» heredado de cuando se escribió, y el cierre canónico —la firma
> del show, exigida por el lint en todos los episodios— vive aquí adentro. Con el carril
> pop-culture en pausa, ese rótulo hacía que la sección entera pareciera archivada.
> **Lo único condicional son los puntos que nombran «el referente»** (2 y 5): si el episodio no
> tiene referente pop, el puente y las Referencias Cruzadas salen del tema mismo, no de una
> película o una banda. El resto es obligatorio siempre.
> El §ADN de los pilares SEO (arriba) no reemplaza esto: dice qué material tiene que haber,
> no en qué orden va ni cómo cierra.

Derivado de comparar EP.018 (completo) vs. un primer borrador de EP.019 que se quedó corto
(feedback Andy 2026-06-26: "se encasilló en el referente, le faltó el cierre"). Un episodio
BTQ lleva, en orden, estos bloques. No omitir ninguno al escribir el borrador:

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
7. **Recomendaciones de Andy — TEJIDAS, no en bloque** (cambio 2026-07-25, confirmado por Andy;
   precisado también en `brand-constants.md`). Ya **no** existe un segmento titulado
   «Recomendaciones de Andy». Las tres se reparten por el cuerpo y entran **como cita que
   respalda lo que se acaba de decir**: «esto lo cuenta Mayo en su libro», «lo van a ver
   retratado en tal película», «y lo confirma tal en su charla». Cada una cae donde el
   contenido se la gana — si no hay un punto del guion que la justifique, esa recomendación
   está mal elegida.
   *Por qué:* un bloque con encabezado antes del cierre suena a créditos finales y le da al
   oyente permiso para abandonar (ver § No dar señales de cierre falso). La regla vieja mitigaba
   eso con "una línea de enganche" antes del bloque — maquillaje, el bloque seguía ahí.
   Se conserva la diversificación: máximo UNA atada al referente, mezclar medios
   (película + libro + charla), nunca las tres del mismo tema o época.
   **Nunca repetir la misma recomendación (ni la misma referencia cruzada) entre episodios**
   (feedback Andy 2026-07-21). Antes de cerrar las 3 recomendaciones o las referencias cruzadas
   de un guion nuevo, grepear `btq-production/launch-assets/*.html` por el título candidato — si
   ya apareció en otro episodio, descartarlo y buscar otro. Precedente: EP.023 (Matrix) descartó
   "Moneyball" (ya en EP.020) y "Sully" (ya en EP.022) por esta regla, y confirmó por grep que
   Baudrillard / Kathryn Schulz / The Big Short no se habían usado antes.
8. **Cierre canónico** (NO omitir nada de esto — es la firma de BTQ):
   - **Pregunta comentable** que interpela al oyente sobre SU situación.
   - **CTA de comentarios:** "escríbanlo en los comentarios del episodio, en Spotify, los leo
     todos". El **guiño a los comentarios del episodio anterior es CONDICIONAL** (fijado
     2026-07-28): solo va si el episodio anterior tiene comentarios reales, y hay que
     **mirarlos antes de escribirlo** — no basta con suponer que llegaron. Si no hay ninguno,
     el reemplazo es el reconocimiento honesto de que la sección está vacía, que además
     funciona mejor como CTA ("si usted escribe algo, va a ser el único").
     *Por qué:* la redacción vieja daba la pieza por obligatoria y empujaba a inventarla. En el
     borrador de EP.024 se coló "varios me contaron cosas de sus propias mediciones" cuando
     EP.023 tenía **cero** comentarios — se detectó solo porque Andy compartió los analytics.
     Una pieza obligatoria que depende de un hecho externo es una fábrica de datos inventados.
   - **CTA de compartir** ("si esto les hizo pensar en alguien, compártanlo").
   - **Redes:** LinkedIn — "estoy en LinkedIn como Andrés Bermúdez Rodríguez".
   - **Teaser** del próximo episodio (bien armado, no una nota suelta).
   - **Firma + TM canónico:** "Yo soy Andy. Y recuerden: [tesis del episodio en una frase
     memorable]" + nota JINGLE DE SALIDA (ver § Jingle, abajo).

## Jingle en vez de música de intro/outro (decisión de Andy, 2026-07-25)

**Se retira la música de intro y de outro.** En su lugar va un **stinger corto (2-4 s)**,
el mismo al abrir y al cerrar — el patrón de *Leyendas Legendarias*: una firma sonora que
se reconoce en dos segundos, no una cama que hay que cuadrar contra la voz.

- **No es cama musical.** No corre por debajo del habla, no hace fade largo. Andy entra
  sobre el **silencio**, no sobre la música; y al cerrar, el jingle entra *después* de que
  la firma termina, no encima de ella.
- **El mismo stinger en los dos extremos.** Es una firma sonora, no dos piezas distintas.
- **En el guion:** nota `JINGLE DE ENTRADA` en el Segmento 0, antes de «Buenas y santas»;
  nota `JINGLE DE SALIDA` después del TM canónico. Ya **no** se escribe `OUTRO MUSICAL`.

**Por qué, además del gusto:** en EP.020 el timing de la música de intro/outro obligó a
re-transcribir el episodio (ver `launch-assets/EP020-metricas-launch.md`). Un stinger seco
elimina esa clase de problema: no hay solape que sincronizar.

El estándar de duración de 40-45 min sigue midiendo **solo el habla** — el jingle no cuenta,
igual que antes no contaba la música.

## Disclaimer de encuadre — el puente al ritual (decisión de Andy, 2026-07-25)

**El problema que resuelve.** En EP.023 el Segmento 0 quedó así: hook en frío → «Bienvenidos a
Behind the Queue, episodio 23» → **18 segundos de nada** → «Buenas y santas». El salto del hook
al ritual no tenía puente: el jingle solo tapa el hueco, no lo resuelve. Andy pidió un
**disclaimer de encuadre** que haga esa transición.

**Qué es.** Entre el hook en frío y el «Buenas y santas», un bloque corto que le dice al oyente
qué va a oír en el episodio **y qué no**. Se escribe **nuevo en cada episodio** — es encuadre del
tema, no una fórmula recitada. Lo que se fija acá es su forma, no su texto.

| Restricción | Valor |
|---|---|
| Largo | **35-55 palabras** (≈15-22 s a 148 wpm) |
| Posición | Segmento 0, después del hook y del `JINGLE DE ENTRADA`, antes de «Buenas y santas» |
| Obligatorio | La mitad de «qué **no** va a oír» — es la que sostiene la promesa de evidencia |

**Lo que NO puede ser:**

- **Un índice.** «Hoy vamos a ver tres cosas: primero…» convierte el episodio en una agenda y le
  da al oyente permiso para saltar. Misma patología que el bloque de recomendaciones con
  encabezado (ver § No dar señales de cierre falso).
- **El remate adelantado.** El giro y el dato del ~60% no se tocan acá. El disclaimer encuadra
  la pregunta; no entrega la respuesta.
- **Una fórmula recitada.** Si dos episodios seguidos lo abren con la misma construcción, deja de
  ser encuadre y pasa a ser ritual — y el ritual ya existe dos líneas más abajo. Aplica la misma
  lógica que la rotación de esqueleto: **verificarlo contra el episodio anterior** con
  `scripts/lint_guion_repeticion.py`.
- **Un descargo legal.** No es «esto no constituye asesoría profesional». Andy descartó
  explícitamente esa lectura: el encuadre es del **tema**, no de la responsabilidad.

**Efecto en la duración:** suma ~45 palabras habladas al Segmento 0. Es marginal, pero cuenta
dentro del estándar — el disclaimer es habla, no jingle. Incluirlo al dimensionar (ver
§ Calibración de duración).

## Rotación de esqueleto — la fórmula no se repite (fijado 2026-07-25)

**El problema, medido.** EP.020, EP.021, EP.022 y EP.023 salieron con el MISMO esqueleto de 9
segmentos, en el mismo orden, con los mismos nombres de ranura (`Cuerpo 1`, `Cuerpo 2`,
`Re-enganche`). Cuatro episodios seguidos. El oyente que llegó por EP.020 ya sabe, en EP.023,
que después del segundo caso viene el giro.

**Lo intocable son las piezas, no su orden** (precisado en `brand-constants.md` § esencia):
teórico nombrado · casos reales con consecuencias que escalan · un dato duro · un giro que
reencuadra · aplicación real · cierre canónico. Cómo se ordenan lo decide el material.

**Regla: ningún esqueleto dos episodios seguidos.** Menú de arranque —se puede inventar otro,
lo que no se puede es repetir el anterior:

| | Esqueleto | Cuándo sirve |
|---|---|---|
| **A** | *Canónico* — escena → nombrar → caso → caso → giro → cruzadas → aplicación | El default histórico. Ya se usó 4 veces seguidas: **en pausa**. |
| **B** | *Invertido* — abrir con el desmentido y reconstruir hacia atrás | Cuando la teoría misma está en disputa (EP.023). |
| **C** | *Un solo caso a fondo* — un caso largo por capas, sin segundo cuerpo | Cuando el caso da para sostener 40 min solo (más cerca de MPD). |
| **D** | *Trenzado* — dos casos en paralelo, alternando, no en secuencia | Cuando hay dos historias que se iluminan mutuamente. |
| **E** | *Acción primero* — dar el consejo en el minuto 2 y usar el episodio para justificarlo | Cuando la aplicación es contraintuitiva y el "por qué" es el suspenso. |

**Los segmentos se nombran por su CONTENIDO, no por su función.** `Cuerpo 1` y `Re-enganche` son
ranuras de producción y no deben aparecer en un guion. EP.018 lo hacía bien: «La preparación ·
Bielsa», «La decisión · Van Gaal y Obdulio».

## Nunca dos veces el mismo pozo (fijado 2026-07-25)

**Hallazgo:** EP.020 y EP.022 usan literalmente el mismo Cuerpo 2 — «el dato SQM». Mismo dato
duro, dos episodios. La regla de no repetir recomendaciones ni referencias cruzadas ya existía
(punto 7 de § Estructura canónica) pero **no cubría los datos ni los casos**, que son lo que
sostiene el episodio.

- **Ninguna fuente de dato o caso ancla puede repetirse en 5 episodios.** Antes de cerrar el
  dato duro o los casos, grepear `btq-production/launch-assets/*.html` por la fuente candidata.
- Si la única cifra disponible ya se usó, **buscar otra fuente para el mismo punto**, no
  reciclarla con otras palabras.

## Frases-molde: la voz no es una plantilla (fijado 2026-07-25)

**Medido con solapamiento de 6-gramas entre guiones, excluyendo el ritual canónico** (que SÍ debe
repetirse). Lo que apareció:

| Frase | Episodios |
|---|---|
| «Tres cosas concretas, esta semana, sin…» + «ninguna de las tres cuesta un peso» | **EP.020, 022, 023** |
| «Y aquí va el dato que me guardé todo el episodio para este momento exacto» | EP.017, 018 |
| «¿Cuándo fue la última vez que…?» | EP.017, 018, 019, 021 |
| `tres cosas concretas` — **1 vez en 6 de 7 episodios** · `y aquí está` — 12 veces · `esa es la` — 10 veces | |

Una frase que aparece exactamente una vez por episodio, en seis episodios, no es muletilla: es
un molde. **Prohibidas de aquí en adelante** las tres de la tabla, y prohibido abrir el tramo de
aplicación con una fórmula fija de conteo («tres cosas concretas / tres herramientas / tres
cosas que puede hacer»). La aplicación entra distinto cada vez.

**Una cita atribuida no se reescribe si no se puede verificar su origen** (2026-07-25). En la
web había un *pull quote* atribuido a EP.011 —«Lo que tienes hoy no va a estar para siempre»—
en tuteo, chocando con el usted del sistema nuevo. **No se tocó**: no apareció en ningún guion
del repo, solo en versiones viejas del sitio, así que no hay forma de saber si es textual del
audio o una paráfrasis escrita para la web. Reescribir una cita atribuida sin conocer su origen
es inventar lo que alguien dijo. Ante el choque de registro, se pregunta; no se corrige.

**La mitigación de una regla se volvió molde.** El § No dar señales de cierre falso **pedía** meter
«una línea de enganche» antes de la aplicación, y la ejemplificaba con *"todavía no les he dicho la
parte que más le tocó a X"* (**mitigación retirada el 2026-07-28**, justamente por esto). El lint
encontró esa línea **casi textual en EP.022 y EP.023**:
`todavía no les he contado la parte que`. Una mitigación redactada como ejemplo se copia como
plantilla. **Los ejemplos de esta guía son ilustraciones, no texto para pegar** — cuando una
regla dé un ejemplo de redacción, escribir uno nuevo, no reusar el de la guía.

**Cómo verificar:** `python scripts/lint_guion_repeticion.py <guion.html>` — solapamiento de
6-gramas contra los guiones anteriores, **excluyendo apertura, cierre y recomendaciones** (esos
repiten por diseño; sin excluirlos, 25 de 25 hallazgos eran ritual). Cualquier 6-grama compartido
en el cuerpo se reescribe. Mide repetición **literal, no humor**: si el chiste cambia pero el
andamiaje es idéntico, igual suena a fórmula.

## No dar señales de cierre falso antes del Cierre real (retención Spotify, fijado 2026-07-06)

Según la data de permanencia/completion de Spotify, cualquier momento del episodio que **suene**
a final —una frase que cierra un círculo, un tono de aplauso, un remate demasiado conclusivo, un
segmento que "resuelve" del todo— le da al oyente el permiso mental de dejar de escuchar ahí,
aunque el episodio siga. El oyente no abandona solo por aburrimiento; abandona en el momento exacto
en que algo *suena* a que ya terminó.

**Los puntos de mayor riesgo son los REMATES de segmentos intermedios y el tramo de aplicación**
— en casi cualquier pódcast funcionan culturalmente como "señal de que ya casi se acaba".

> **Actualización 2026-07-25:** el bloque «Recomendaciones de Andy» **era** el peor de estos
> puntos y ya no existe como segmento — las recomendaciones van tejidas en el cuerpo (ver punto 7
> de § Estructura canónica). La mitigación que estaba escrita aquí ("meter una línea de enganche
> antes de entrar") era maquillaje: el bloque seguía sonando a créditos. Se eliminó la causa, no
> el síntoma — **y con ella se retiró la mitigación**, que se había vuelto molde (ver abajo).

**Mitigación obligatoria — condición → acción → verificación:**
- Cuando un REMATE de un segmento que NO es el cierre final quede redactado con tono de conclusión
  total (una frase que "amarra" el tema sin dejar nada abierto), reescribirlo para que tire hacia
  adelante — una pregunta sin responder, un hilo que se retoma después, nunca un punto final
  emocional. Verificar releyendo cada REMATE fuera del Cierre y preguntando: "¿esto suena a que el
  episodio podría terminar aquí?" Si la respuesta es sí, reescribirlo.
- **RETIRADA la "línea de enganche" antes de la aplicación** (2026-07-28). Era la mitigación
  obligatoria de esta sección y se convirtió exactamente en lo que prohíbe § Frases-molde: el
  ejemplo que traía impreso apareció casi textual en EP.022 **y** EP.023. Una mitigación redactada
  como frase modelo se copia como plantilla, y el checklist la exigía episodio tras episodio.
  **En su lugar:** el remate del segmento anterior a la aplicación es el que tiene que tirar hacia
  adelante — se arregla ahí, con el material del episodio, no con una frase puente reutilizable.
  Y **nunca** abrir la aplicación con una fórmula de conteo fija (ver § Frases-molde).
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

## Datos: verificar ANTES de escribirlos, y qué hacer si el audio los contradice

Regla de Andy (2026-07-25). **Ninguna cifra, fecha, nombre propio ni atribución entra al guion
sin fuente verificada.** No se escribe «como ~X» para verificar después: para cuando el guion
llega al micrófono, el dato ya se grabó. Todo lo verificado va al bloque **Fuentes verificadas
(no leer al aire)** al final del guion, con la publicación concreta — no «un estudio del MIT»
sino la revista y el año.

**Qué hacer cuando lo grabado no coincide con la fuente** (caso EP.023: el guion decía
«sesenta muertes prematuras» y al aire salió «alrededor de setenta»):

1. **Los assets públicos usan la cifra verificada, no la dicha al aire.** Las descripciones
   de Spotify y de YouTube y el copy de redes se escriben contra la fuente.
2. **No se corrige en silencio ni se propaga en silencio.** Se le reporta a Andy la
   discrepancia con el timestamp exacto, y él decide si edita el audio o lo deja.
3. **Distinguir el error de locución del artefacto de transcripción.** WhisperX confunde
   nombres propios: en EP.023 escribió «Freeconomics» por *Freakonomics* y «Elton Mayer» por
   *Elton Mayo*, y el guion tenía ambos bien. Antes de reportar un error al aire, **cotejar
   contra el guion**: si el guion está bien, lo más probable es que sea la transcripción, y
   eso solo lo resuelve el oído de Andy. Precedente: EP.019, «Tim Collins» por Jim Collins.

**El fact-check se corre sobre la TRANSCRIPCIÓN, no sobre el guion** — el guion ya se
verificó al escribirse; lo que falta comprobar es qué salió realmente por el micrófono.

---

## Calibración de duración — dimensionar en PALABRAS, no en minutos adivinados

Regla medida (no de gusto). El guion se dimensiona contando **palabras habladas** y dividiendo por
el ritmo real de Andy, **no** estimando minutos "a ojo" por segmento. Las marcas de minutos por ojo
salen infladas y hacen que Andy termine ~15 min antes de lo marcado y tenga que estirar.

**Estándar editorial de duración (BTQ y CCC, fijado 2026-07-06):** el episodio debe caer **entre 40
y 45 minutos de contenido hablado**, sin contar el jingle de entrada ni el de salida (antes: la
música de intro/outro, retirada el 2026-07-25 — ver § Jingle). No es un mínimo sugerido ni
un techo aspiracional — es el rango objetivo. Si el guion mide por debajo de 40 o por encima de 45
(con la fórmula de abajo), expandir o cortar antes de aprobar el guion para grabación, no dejarlo
para la edición.

**Ritmo real de Andy ≈ 148 palabras/min.** Estable y no es la variable a vigilar: medido sobre los
4 SRT de EP.020-023 con un solo método (palabras de las líneas del speaker / habla efectiva = del
primer al último cue, menos los silencios ≥3 s) da 147,4 · 153,4 · 142,5 · 148,6 — **media 148,0**.
Ese número **ya incluye sus pausas** — es ritmo de entrega, no de lectura en seco. Diagnóstico
EP.17: estaba marcado a "57 min" (≈90 wpm imaginario) y cayó en ~42-45. EP.18 v1 tenía 4.213
palabras = ~29 min reales aunque estaba marcado a 52.

**Expansión real en vivo — RECALIBRADA 2026-07-25. Esta es la variable que rompe la duración.**

| EP | escritas | habladas | expansión | habla efectiva |
|---|---|---|---|---|
| 020 | 4.570 | 6.418 | +40,4% | 43,53 min |
| 021 | 4.584 | 6.134 | +33,8% | 39,99 min |
| 022 | 4.674 | 5.901 | +26,2% | 41,40 min |
| 023 | 4.425 | 5.017 | **+13,4%** | **33,77 min** |

**La causa NO es que Andy se expanda menos con el tiempo — es estructural** (diagnóstico de Andy,
2026-07-25). EP.023 fusionó dentro del cuerpo segmentos que antes iban sueltos (las recomendaciones,
tejidas en vez de en bloque) y se dimensionó **asumiendo que el guion fusionado conservaba las
palabras del original**. No las conserva: **las costuras entre segmentos separados son donde ocurre
la expansión en vivo.** Al disolverlas desaparece el volumen hablado que generaban — de ahí el salto
de -12,8 puntos de EP.022 a EP.023, el mayor de la serie.

**Regla: el factor de expansión depende del ESQUELETO, no de la fecha.**

| Esqueleto | Expansión a usar | Evidencia |
|---|---|---|
| Segmentos separados, con bloques propios (recomendaciones aparte, re-enganche) | **+26% a +40%** | EP.020-022 |
| Segmentos fusionados / recomendaciones tejidas en el cuerpo | **+13%** | EP.023 |

**Al cambiar de esqueleto NO se hereda el factor del esqueleto anterior, y NO se asume que el guion
reescrito conserva el conteo del original — hay que recontarlo.** Fusionar segmentos reduce las
palabras habladas aunque las escritas no bajen. Con esqueleto nuevo sin precedente medido, usar el
factor bajo (+13%): el error caro es quedarse corto, porque estirar en post no se puede y regrabar
sí cuesta.

> ⚠️ Estas cifras salen de medir los SRT directamente, no de las notas de sesiones anteriores. La
> guía registraba 6.192 palabras habladas para EP.20 donde el conteo consistente da 6.418: eran
> métodos distintos de recortar el habla efectiva. Al recalibrar de nuevo, **volver a medir los 4+
> SRT con un solo método** en vez de encadenar cifras heredadas.

**Tabla de dimensionamiento (palabras habladas → minutos a 148 wpm, recalibrado 2026-07-25).**
La columna de escritas usa **+13%** — el factor del esqueleto fusionado. Con un esqueleto de
segmentos separados, usar +26% a +40% y la columna baja proporcionalmente:

| Objetivo real | Palabras habladas | Palabras ESCRITAS (con +13% expansión) |
|---|---|---|
| 40 min (piso del estándar) | ~5.920 | ~5.240 |
| 42.5 min (centro del estándar) | ~6.290 | ~5.565 |
| 45 min (techo del estándar) | ~6.660 | ~5.895 |
| >50 min (fuera del estándar → evaluar 2 partes) | ~7.400+ | ~6.550+ |

Es un salto grande frente a la tabla vieja (~4.700 escritas para el centro): **el guion tiene que
nacer ~18% más largo que los de EP.020-023.**

> ⚠️ **Corregido 2026-07-28.** Hasta esta fecha, aquí abajo seguían vivas las instrucciones de la
> calibración del 2026-07-06 — «usar +35.5%», «multiplicar por 1.355 y dividir por 150»— que
> contradicen la tabla recalibrada de arriba (+13%, 148 wpm) a seis líneas de distancia. Quien
> siguiera este párrafo dimensionaba el guion mal. Lo **histórico** se conserva (así se calibró en
> su momento); lo **normativo** ahora apunta a la tabla vigente.

*Registro histórico, no instrucción:* la calibración del 2026-07-06 tomó el dato de EP.17 (guion
5.265 → habló 6.062, +15%) como piso y el SRT de EP.20 (+35.5%: guion 4.570 → habló 6.192) como
referencia. Esas cifras describen cómo se calibró entonces; **fueron reemplazadas** por la tabla de
esqueleto de arriba tras la remedición del 2026-07-25 con un solo método.

**Cómo medir** (excluir lo que no se lee: bloques `NOTA`, chips `PAUSA`, encabezados de segmento,
tabla de arquitectura): contar palabras de `p.line` + `remate` + `dato` + `mito/realidad` + `sub`,
multiplicar por **el factor de expansión del esqueleto** (tabla de arriba: +13% si los segmentos
van fusionados o si el esqueleto es nuevo y no tiene precedente medido; +26% a +40% si van
separados) y dividir por **148**. Marcar los tiempos de la arquitectura en consecuencia.
Escribir el guion para que **en seco** caiga por debajo del objetivo hablado:
**siempre dejar colchón para CORTAR, no para estirar.**

**Recalibrar** los 148 wpm y el factor de expansión cada pocos episodios contra el SRT más reciente
(los SRT viven en `E:\Transcriptor\transcripciones\`); si su ritmo cambia, actualizar la tabla —y
este párrafo con ella, que es justo lo que no se hizo en julio.

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
      dedicada arriba).
- [ ] **Título (fórmula invertida 2026-07-28):** confirmar que antes de los dos puntos va **el
      problema en las palabras del oyente** —la frase que escribiría en un buscador o le
      preguntaría a una IA— y que el teórico o la ley va **después**. Nunca anclar en el título
      de un libro, en una frase con sabor a eslogan, ni en un referente de cultura pop. El
      aterrizaje va a «su equipo / su operación / su empresa». Confirmar además que el string es
      idéntico al que se hornea en la portada. Ver sección dedicada.
- [ ] **Coherencia título ↔ guion:** señalar **la línea exacta del guion** que responde la promesa
      del título. Si no se puede señalar, se corrige uno de los dos antes de grabar. (Fijado
      2026-07-28: un título que promete algo que el episodio no desarrolla se siente como «gato
      por liebre» y se paga en abandono, no en quejas.)
- [ ] **Sin "Andy" en tercera persona dentro del guion hablado** (detectado 2026-07-21,
      EP.023 borrador Hawthorne: "del tipo que Andy, personalmente, desconfía..." — debía
      ser "yo, personalmente, desconfío"). BTQ es solo host narrando en primera persona
      todo el episodio; "Andy" en tercera persona solo es válido en la firma canónica del cierre
      ("Yo soy Andy"). *(Antes también valía como etiqueta de la sección «Recomendaciones de
      Andy» — esa sección ya no existe, ver punto 7 de § Estructura canónica.)*
- [ ] **Español neutro** (ver sección dedicada — es de léxico, NO aplanar la voz): grep de
      `cola` → ninguna con adjetivo corporal o de tamaño; nombre del show sin traducir; grep de
      anclados a un país (`tinto`, `parce`, `bacano`, `berraco`, `vaina`, `camello`, `chino`,
      `ahorita`) y de doble sentido (`coger`, `concha`, `pico`, `pinche`, `chucha`, `papaya`);
      cero voseo y cero vosotros. Prueba de cada hallazgo: ¿lo entiende un oyente en México sin
      que se lo expliquen? Si sí, se queda aunque sea coloquial.
- [ ] Frase larga: ninguna oración que no se pueda decir de un respiro; partir las cadenas de guiones.
- [ ] Al menos 2-3 momentos de humor/guiño/autoconciencia repartidos.
- [ ] Datos verificados (fuentes reales, nada inventado); lo dudoso marcado [VERIFICAR].
- [ ] **Vocabulario accesible:** cero palabras que el host/audiencia no usen al hablar
      (regionalismos raros, cultismos, tecnicismos). Cazar y reemplazar por habla natural —
      ej. rechazados: "galones", "desperdigado", "embestida", "factura final", "telón de
      fondo". Si dudas si una palabra "se entiende", cámbiala.
- [ ] **Piezas completas** (ver ADN arriba): ¿están Referencias Cruzadas FUERA del referente, las
      3 recomendaciones **tejidas en el cuerpo** (ninguna en bloque, cada una donde el contenido
      se la gana, medios mezclados), y el cierre canónico entero (comentarios Spotify · compartir ·
      LinkedIn · teaser · firma + TM · jingle)? No omitir.
- [ ] **Esqueleto distinto al del episodio anterior** (§ Rotación de esqueleto) y ningún segmento
      llamado `Cuerpo N` ni `Re-enganche` — se nombran por su contenido.
- [ ] **Pozo no repetido** (§ Nunca dos veces el mismo pozo): grepear `launch-assets/*.html` por
      la fuente del dato duro y por cada caso ancla — nada reutilizado en 5 episodios.
- [ ] **Frases-molde** (§ Frases-molde): correr el solapamiento de 6-gramas contra los guiones
      anteriores excluyendo apertura/cierre; cero 6-gramas compartidos en el cuerpo. Prohibido
      abrir la aplicación con fórmula de conteo ("tres cosas concretas").
      **Más un grep nominal, porque el lint de 6-gramas NO caza el andamiaje** si cambia una sola
      palabra: `grep -i "todavía no les he\|aún no les he"` → **cero apariciones**. Precedente
      2026-07-28: EP.022 y EP.023 decían `todavía no les he contado` y EP.024 llegó a guion
      aprobado con `todavía no les he mostrado` — tercero seguido, y el 6-grama pasó porque
      difería en la última palabra. Cuando se detecte un molde nuevo, agregarle su grep aquí:
      el solapamiento literal es el piso, no el techo.
- [ ] **Sin bloque "Mito o Realidad" al final:** los datos de interés / mito-vs-realidad van
      distribuidos dentro del Cuerpo, no como segmento aparte antes del cierre.
- [ ] **Sin señales de cierre falso antes del Cierre real** (ver sección dedicada arriba): releer
      cada REMATE que no sea el del Cierre y confirmar que tira hacia adelante, no que suena a
      final — en especial el que precede a la aplicación. **No** buscar una "línea de enganche":
      esa mitigación se retiró el 2026-07-28 por haberse vuelto molde.
- [ ] **Voz narrativa, no documental:** los tramos históricos en presente/escena, no en
      modo informe.
- [ ] Aperturas y conectores de contenido (sin meta-anuncios tipo "ahora vamos a…").
- [ ] Duración: contar **palabras escritas × factor de expansión del esqueleto / 148 (wpm)** — factor **1.13** si los segmentos van fusionados / las recomendaciones tejidas, **1.26 a 1.40** si van en bloques separados (ver "Calibración de duración", recalibrado 2026-07-25 contra los SRT de EP.020-023). NO estimar minutos a ojo, NO heredar el factor del esqueleto anterior, y si el guion es una reescritura **recontar las palabras** en vez de asumir el conteo del original. El resultado debe caer **entre 40 y 45 minutos** (estándar editorial, contando solo el habla — el jingle no cuenta) — si queda fuera de ese rango, expandir o cortar antes de grabar, no dejarlo para después.
- [ ] **Jingle, no música:** el Segmento 0 abre con nota `JINGLE DE ENTRADA` y el cierre lleva
      `JINGLE DE SALIDA`. Cero apariciones de `OUTRO MUSICAL` o de camas musicales. Ver § Jingle.
- [ ] **Disclaimer de encuadre presente** entre el hook y «Buenas y santas»: 35-55 palabras,
      incluye la mitad de «qué **no** va a oír», no es índice ni descargo legal, y no repite la
      construcción del episodio anterior. Ver § Disclaimer de encuadre.
