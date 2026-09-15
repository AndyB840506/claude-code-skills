# Estilo — español neutro latinoamericano

**El estándar de este proyecto es el ESPAÑOL NEUTRO**, el registro del doblaje
latinoamericano. Su objetivo entero es que **ningún jugador pueda ubicar de qué país es
la traducción**.

**La regla, en una línea: léxico neutro siempre; carácter regional nunca.**

La industria construye ese neutro sobre una base mexicana, pero eso se refiere solo al
sustrato invisible —gramática, tratamiento `tú` / `ustedes`, léxico general como `carro`,
`celular`, `computadora`, `departamento`—, **no a darle sabor mexicano al texto**. La
jerga local queda fuera venga de donde venga:

| Origen | Fuera por defecto |
|---|---|
| México | `chingar`, `chingada`, `pinche`, `güey`, `no mames`, `órale`, `chido`, `neta`, `morro`, `carnal`, `panocha` |
| España | `vosotros`, `gilipollas`, `hostia`, `joder`, `follar`, `polla`, `tío`, `vale`, `guay` |
| Cono Sur | `vos`, `sos`, `che`, `boludo`, `pija`, `concha`, `huevón` |
| Colombia / Caribe | `malparido`, `parcero`, `pinga` |

> `<i>Ah, chingada madre, ¿cuánto más...</i>` ← **mal**: suena a un país concreto.
> `<i>Maldita sea, ¿cuánto más...</i>` ← **bien**: se entiende en todo el continente.

**La prueba, al releer cada línea:** si podés decir de qué país es el traductor, hay que
reescribirla. Aplica igual a un mexicanismo, un españolismo o un argentinismo — ninguno
tiene prioridad sobre otro, todos rompen el neutro.

**Única excepción:** la jerga local sirve **para caracterizar a un personaje concreto**
que en el original también habla marcado. Nunca como voz por defecto del juego, y
siempre declarada como adaptación.

---

## Qué evitar de España

Estos son los que más delatan una traducción hecha para el mercado español:

| España | Latino neutro |
|---|---|
| vosotros, vuestro, sabéis, venid | ustedes, su, saben, vengan |
| **coger** (= agarrar un objeto) | tomar, agarrar, recoger |
| vale | está bien, de acuerdo, listo, ok |
| tío / tía (como "amigo") | amigo, hermano — o reformular |
| chaval | chico, muchacho, joven |
| ordenador | computadora |
| móvil | celular |
| gilipollas | idiota, imbécil, estúpido |
| hostia | según el caso — ver groserías abajo |
| guay / molar / flipar | genial, buenísimo, alucinar |
| zumo | jugo |
| piso (vivienda) | departamento |
| aparcar | estacionar |

**`coger` es el caso crítico.** En buena parte de Latinoamérica es el verbo sexual, así
que una línea inocente como "coge la llave" cambia de sentido por completo. En neutro
**no se usa para tomar un objeto**: siempre `agarrar` o `tomar`. El validador lo marca
siempre para forzar esa revisión.

---

## Qué evitar del voseo

El voseo rioplatense (`vos`, `sos`, `tenés`, `querés`, `mirá`, `che`) es un marcador
regional tan fuerte como el `vosotros` español, solo que del otro lado. **Usar `tú`**:
`eres`, `tienes`, `quieres`, `mira`.

El script marca formas voseantes como aviso.

*(Esto coincide con una preferencia ya establecida del usuario: español neutro con
`tú`, sin jerga argentina.)*

---

## Groserías — traducir fiel, sin censurar

**Esta es una regla dura, no una preferencia.** Una grosería del original se traduce
con una grosería equivalente en español. No se suaviza, no se omite, no se reemplaza
por un eufemismo y **nunca se escribe con asteriscos ni se autocensura**. Si el
personaje dice `fuck`, el jugador hispanohablante tiene que leer algo igual de fuerte.

Bajar el registro es un error de traducción con consecuencias reales: rompe la
caracterización, aplana el tono del juego y hace que el doblaje o los subtítulos no
cuadren con la actuación. Un soldado furioso que dice "cielos" es un personaje
distinto al que escribió el guionista.

Esto no es una licencia para agregar groserías donde no las hay: **la fidelidad corre
en las dos direcciones**. Una línea limpia en inglés se traduce limpia.

### Mapa de intensidad

Todas las opciones de esta tabla son **pan-hispanoamericanas**: se entienden en todo el
continente y ninguna delata un país. Es referencia de trabajo, no reemplazo automático —
la elección final depende del personaje y del ritmo de la frase.

| Inglés | Equivalentes neutros, de menor a mayor fuerza |
|---|---|
| damn / damn it | rayos, maldición, maldita sea |
| hell (What the hell) | diablos, demonios, qué demonios, qué carajos |
| crap | porquería, basura, mierda |
| shit | mierda |
| fuck (exclamación) | mierda, carajo, maldita sea |
| fucking (intensificador) | maldito, puto/puta, jodido |
| motherfucker | desgraciado, hijo de perra, hijo de puta |
| asshole | idiota, imbécil, hijo de puta |
| bastard | maldito, desgraciado, bastardo |
| bitch | maldita, zorra, perra |
| dick / prick | idiota, imbécil, cretino |
| piss off / screw you | lárgate, púdrete, vete al carajo, vete a la mierda |
| bullshit | tonterías, estupideces, pura mierda |

Notar lo que **no** está: `chingados`, `pinche` y `pendejo` (México), `gilipollas`,
`hostia` y `joder` como interjección (España), `malparido` (Colombia), `boludo`
(Argentina), `huevón` (Chile). Todos tienen equivalente neutro en la tabla.

**El intensificador `fucking` no se pierde.** `Get the fucking door` no es "abre la
puerta": es "abre la maldita puerta" o "abre la puta puerta". Si desaparece el
intensificador, desapareció información del original.

### Sobre el ejemplo del cliente

El brief trae este par:

```
God fucking damn it, how much more...      (EN)
Putain de merde, encore combien...         (FR)
Maldita sea, ¿cuánto más...                (ES)
```

Vale la pena notarlo con honestidad: el francés (`putain de merde`) conserva toda la
carga del original, y el español del ejemplo (`maldita sea`) queda **por debajo**. Se
puede subir sin regionalizar: `Mierda, ¿cuánto más...` o `Carajo, ¿cuánto más...`.

Lo que **no** resuelve el problema es irse a `chingada madre`: sube la fuerza pero
rompe el neutro, que es peor. **Subir el registro nunca justifica marcar el texto.**

El ejemplo del cliente sirve como referencia de **forma** — sintaxis, tags, signos,
puntuación final — no como calibración del registro de groserías. Para eso manda la
regla de fidelidad de arriba.

### La tensión real: fuerza contra neutralidad

Las groserías son el punto donde el neutro más cuesta, porque **lo más fuerte suele ser
lo más local**. Cuando choquen, el orden es:

1. Buscar la opción **fuerte y neutra** — casi siempre existe, y la tabla de arriba la
   tiene. `Mierda`, `carajo`, `hijo de puta`, `vete a la mierda` no le deben nada a
   ninguna jerga local.
2. Si la neutra pierde fuerza, **redistribuirla en la frase** en vez de cambiar de
   palabra: `¡Mierda, otra vez no!` golpea más que `¡Mierda!` sola, sin marcar nada.
3. Recién si nada de eso alcanza, va al bloque de Consultas. **Nunca se resuelve
   metiendo un regionalismo en silencio.**

### Si algo genuinamente no se puede traducir

Si una línea tiene una grosería cuyo equivalente cambiaría el sentido (juego de
palabras obsceno, insulto con referencia cultural), **no se resuelve bajando el tono**:
se traduce con la mejor opción fuerte disponible y se anota en el bloque de Consultas
para que anna decida. La opción suave nunca es el default silencioso.

---

## Contenido adulto (18+) — traducir completo y explícito

Estos títulos son **juegos para adultos** con contenido sexual explícito. Traducir esas
líneas es parte del trabajo, igual que cualquier otra. Aplica lo mismo que con las
groserías, y con más razón:

- **No se omite ninguna línea.** Una celda vacía rompe el build; una línea "saltada por
  incómoda" es un entregable defectuoso.
- **No se suaviza a lenguaje clínico ni poético.** Si el original usa vocabulario
  explícito y vulgar, el español usa vocabulario explícito y vulgar. Cambiar una
  palabra cruda por un término médico o un eufemismo altera el tono de la escena y la
  voz del personaje.
- **Tampoco se escala.** Si el original es sugerente y elíptico, el español es
  sugerente y elíptico. La fidelidad de registro corre en las dos direcciones.

### Los tres registros, y por qué importa acertar

El inglés distingue claramente tres niveles y el español también. El error más común
es cruzarlos.

| Registro | Inglés típico | Español equivalente |
|---|---|---|
| Clínico / neutro | intercourse, genitals, breasts, buttocks | relación sexual, genitales, senos, glúteos |
| Coloquial / eufemístico | sleep with, private parts, chest, behind | acostarse con, partes íntimas, pecho, trasero |
| Explícito / vulgar | fuck, cock, tits, ass, cum | ver la tabla de abajo |

Una escena explícita escrita con vocabulario de la fila 3 **no se traduce con
vocabulario de la fila 1**. Ese cruce es el fallo típico y se nota de inmediato.

### El vocabulario sexual también va en neutro

Aquí es donde el neutro más cuesta, y hay que decirlo con honestidad: **la jerga sexual
es el área más regionalizada del español, y para algunas categorías no existe un término
vulgar realmente neutro.** Fingir que sí lo hay produciría justo el error que estamos
corrigiendo.

Lo que sí se puede hacer es ordenar las opciones por alcance:

| Categoría | Neutro (default) | Vulgar de alcance amplio | Marcado — NO usar |
|---|---|---|---|
| Acto sexual | tener sexo, acostarse con, hacerlo | metérsela, hacérselo | coger (MX/AR), follar (ES), culear (Cono Sur), chingar (MX) |
| Pene | pene, miembro, entrepierna | verga | pija (AR), polla (ES), pinga (Caribe) |
| Vagina | vagina, sexo, entrepierna | *(sin opción neutra — ver abajo)* | panocha (MX), concha (Cono Sur), coño (ES/Caribe) |
| Senos | senos, pechos | tetas | chichis (MX) |
| Nalgas | nalgas, trasero | culo | — |
| Orgasmo | terminar | acabar, venirse | correrse (ES) |

`Tetas`, `culo`, `verga`, `acabar` y `venirse` son vulgares **y** pan-hispanoamericanos:
esos cargan la escena sin marcarla, y son la herramienta principal.

**Las dos categorías sin salida limpia son el acto sexual y la vagina.** Ahí ninguna
opción es a la vez vulgar y neutra. Dos caminos, en este orden:

1. **Reformular para esquivar el término**: el español erótico se apoya mucho más en el
   verbo y en la descripción física que en el sustantivo. `Métemela`, `hazlo ya`,
   `entre las piernas`, `ahí` resuelven la mayoría de las líneas sin nombrar nada
   marcado, y suenan más naturales que cualquier sustantivo forzado.
2. **Si la línea exige el término**, va al bloque de Consultas **una sola vez**: anna
   puede tener un mercado objetivo definido que lo resuelve para todo el juego. Fijada
   la decisión, se mantiene idéntica en todo el lote.

Lo que no se hace es elegir un regionalismo en silencio porque "suena más fuerte".

### Consistencia — crítica en este género

Fijar el vocabulario en la primera aparición y **mantenerlo en todo el lote**. Si un
personaje dice `verga` en la fila 40, no dice `pene` en la fila 95 salvo que el
cambio de registro sea intencional en el original. La inconsistencia léxica en escenas
íntimas rompe la inmersión más que en cualquier otro tipo de línea.

Esto pesa el doble en las dos categorías sin opción neutra: una vez elegido el camino
(reformular, o el término que anna confirme), **no se alterna**.

Conviene armar un mini-glosario del lote (término inglés → término español fijado) y
entregarlo junto con la traducción: le sirve a anna y al siguiente lote.

### No traducir el inglés palabra por palabra

La fraseología sexual inglesa traducida literal suena a doblaje malo. El español tiene
sus propias fórmulas y son las que hay que usar.

| Literal (suena mal) | Natural en español |
|---|---|
| "más duro, más duro" | "más fuerte", "así", "no pares" |
| "me voy a venir" ← *I'm gonna cum* | "ya voy a acabar", "ya casi", "me vengo" |
| "tómame" ← *take me* | "hazlo", "ven", "métemela" |

Los gemidos e interjecciones también se localizan: `mmph`, `nngh`, `ahn` tienen
convenciones propias en español (`mmm`, `ngh`, `ah`). No copiarlos tal cual del inglés
si no se leen naturales.

### El único límite real

Contenido sexual entre adultos: se traduce completo, sin filtro.

Si una línea del original sugiere que un personaje sexualizado es menor de edad —o el
texto lo insinúa aunque el juego afirme lo contrario— **eso no se traduce y no se
resuelve en silencio**: se detiene esa fila y se escribe a anna.b_th. Es el mismo
mecanismo del bloque de Consultas, aplicado a lo único que no es cuestión de estilo.

---

## Longitud

El español se expande ~15–25% sobre el inglés. En un juego eso puede desbordar
bocadillos, botones y HUD.

- **Strings de UI** (botones, menús, etiquetas cortas): buscar activamente la opción
  más corta. Si el inglés tiene ≤ 12 caracteres, tratar el largo como restricción
  real, no como preferencia.
- **Diálogo largo:** la expansión es normal, no forzar recortes.
- Si una línea de UI no cabe en un equivalente razonablemente corto, va al bloque de
  Consultas — puede necesitar decisión de diseño, no de traducción.

El script reporta la expansión de cada fila y marca las que superan +40%, para revisar
a ojo si son UI.

---

## Consistencia dentro del lote

- Un término del juego se traduce **igual en todas las filas** del lote. Si el lote
  menciona un objeto, habilidad o lugar más de una vez, fijar la forma en la primera
  aparición y mantenerla.
- Mantener el **tratamiento** (`tú` vs `usted`) constante por personaje y relación.
  Cambiar de `tú` a `usted` a media conversación sin motivo narrativo es un error.
- Género gramatical: si el string tiene un placeholder que puede ser un personaje de
  cualquier género (`{player}`, `(GG)`), evitar adjetivos con género marcado. Preferir
  formulaciones neutras ("te ves cansado/a" → reformular a "se te nota el cansancio").
  Si no hay salida neutra, va a Consultas.
