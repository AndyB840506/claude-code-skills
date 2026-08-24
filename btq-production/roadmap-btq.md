# Roadmap — Behind The Queue (BTQ)

Fuente de verdad de "qué episodio sigue". `episode-pipeline` la lee al arrancar
Stage A (`00-roadmap.md`) y la actualiza al cerrar cada macro-stage.

**Esta tabla es un resumen y se desactualiza** — se escribe una vez y no siempre se toca de
nuevo cuando el episodio avanza. Para el estado real de un episodio en producción, abrir
`pipeline-state-epXX.md`; si contradice esta fila, gana el pipeline-state y esta fila se corrige
en el momento (mordió el 2026-08-10 con EP.024: la fila decía "falta expandir" una semana
después de publicado).

Estados posibles: `en roadmap` → `guion listo` → `grabado` → `en Spotify` → `publicado`

| EP | Título | Estado |
|---|---|---|
| EP.011 | Frieren | publicado |
| EP.012 | Bohemian Rhapsody | publicado |
| EP.013 | Back to the Future | publicado |
| EP.014 | Maomao | publicado |
| EP.015 | Solid Snake (Metal Gear Solid) | publicado — https://open.spotify.com/episode/6fpGqMqaLozmWB4ABOlO3S |
| EP.016 | Pink Floyd / The Wall | publicado — https://open.spotify.com/episode/3CNyTkA6OCLoCrmNEh0LVR |
| EP.017 | Soda Stereo / Cerati | publicado — https://open.spotify.com/episode/0LJ22lLMgfWh3wLbbgNhxC |
| EP.018 | El Mundial — liderazgo bajo presión (adquisición de oyentes vía reach social) | publicado — https://open.spotify.com/episode/6PC4QIDiAwmVZJ1BV5PYcx |
| EP.019 | Gladiator / Máximo — "la huella que deja un líder" | publicado — https://open.spotify.com/episode/0nNg2ngSzEVxKk7awLe5AK |
| EP.020 | Pilar SEO — Métricas / KPIs de call center (evergreen, keyword-first, sin referente pop) | publicado — https://open.spotify.com/episode/6gRVIWVI3jBUAJarLJ7AsQ |
| EP.021 | Los Simpson — 30 años en el aire: cómo evitar el burnout de un equipo a largo plazo | publicado — https://open.spotify.com/episode/0VH2eMppsNMBl3JqTEq4T0 |
| EP.022 | Pilar SEO — Costo de mala calidad en call center (Philip Crosby, "Quality Is Free", 1979) — ángulo P&L: cuánto cuesta NO invertir en calidad | publicado — https://open.spotify.com/episode/6ewMTUO0FGNxfIMS0u55Yu |
| EP.023 | Pilar SEO — el Efecto Hawthorne en medición del desempeño (Elton Mayo, estudios Western Electric, 1920s; reanálisis de Levitt & List 2011) | publicado — https://open.spotify.com/episode/3FQOeIT8bNTakHNGgBhMMR |
| EP.024 | **Oficio de Jefe #1** — `Por qué su equipo no le cuenta los problemas: seguridad psicológica` | **publicado** — https://open.spotify.com/episode/25xgYzaTZmxEXqTNIu7yQp. Artículo, redes y YouTube cerrados 2026-08-10 (ver `pipeline-state-ep024.md`; esta fila estaba desactualizada, la tabla decía "guion v2 escrito" de una versión anterior a la publicación) |
| EP.025 | **Oficio de Jefe #2** — «ponerse la camiseta»: el discurso de lealtad como herramienta tóxica | **grabado, transcrito, assets listos, publica domingo 9 de agosto 8PM Colombia** — https://open.spotify.com/episode/5AgkBZ1F1M9WPU4MxxqESq. Casos: WeWork · Uber/Fowler · Wells Fargo. **Renumerado de EP.026 a EP.025 el 2026-08-07** — ver nota abajo |
| EP.026 | **Oficio de Jefe #3** — `Por qué no llena esa vacante hace cuatro meses: el candidato unicornio` | **grabado, transcrito, publica domingo 16 de agosto 8PM Colombia** — https://open.spotify.com/episode/683PSkr20tY9Jy57M8vPBa?si=ULDQW49kSyqC5ZfXZ3S_Fw. Assets de lanzamiento listos, artículo del sitio desplegado (commit `b0fcd56`). Pendiente manual de Andy: artículo nativo de LinkedIn (sugerido 19 de agosto) + calendario social + YouTube metadata. Ver `pipeline-state-ep026.md`. **Renumerado de EP.025 a EP.026 el 2026-08-07** para que el episodio ya producido (camiseta) ocupe el próximo cupo real. Ver nota abajo |
| EP.027 | **Pilar SEO** — `Por qué su mejor empleado se vuelve un mal jefe: el Principio de Peter` (Peter y Hull, 1969 + Benson/Li/Shue, QJE 2019) | **PUBLICADO** — https://open.spotify.com/episode/5GEHeLhfee0NmFYalIU1YW?si=NyN-FjRTR56ciSDEDc-dQg, domingo 23 de agosto 2026 8PM Colombia. Artículo del sitio desplegado, kit de lanzamiento completo. Ver `pipeline-state-ep027-peter.md`. ~~GUION A REDISEÑAR — decisión de Andy 2026-08-03~~: **SUPERADA 2026-08-20** — Andy confirmó que la grabación del 07-31 es válida tal cual, la nota de rediseño quedó vieja. |
| EP.028 | **Pilar SEO** — Ley de Little (John D. C. Little, 1961; teoría de colas). El show le debe este tema a su propio nombre | en roadmap — **adelantada de EP.031 a EP.028 el 2026-08-23**: EP.027 ya está en vivo con el teaser grabado («la próxima vez les traigo la Ley de Little»), y esa promesa quedó pública. Rompe a propósito la rotación 3+1 (ver nota abajo). Título por definir con la fórmula invertida |
| EP.029 | Oficio de Jefe #4 — carga cognitiva, aparcada (candidato disponible) | **aparcada 2026-08-07**, no descartada — casos y fuente de Sweller ya verificados en `pipeline-state-carga-cognitiva-parked.md`. Retomar con un esqueleto distinto a E y sin referencias cruzadas a EP.024. **Corrida de EP.028 a EP.029 el 2026-08-23** para darle el cupo a Little |
| EP.030 | Oficio de Jefe #5 — tema por definir | en roadmap. **Corrida de EP.029 a EP.030 el 2026-08-23** |
| EP.031 | Oficio de Jefe #6 — tema por definir | en roadmap. **Corrida de EP.030 a EP.031 el 2026-08-23** |

> **EP.025 — «ponerse la camiseta» (2026-08-07, reasignado desde EP.028, y renumerado de
> EP.026 a EP.025 el mismo día).** Origen: un video que un amigo de Andy le compartió sobre el
> mensaje tóxico que ese discurso trae dentro de las organizaciones. Reemplaza a carga
> cognitiva, que Andy grabó y descartó por sonar a reencauche de EP.024 — ver
> `pipeline-state-carga-cognitiva-parked.md`. Andy confirmó que quiere **las tres capas
> juntas**, no una sola:
> 1. **Extraer lealtad sin retribución** — la camiseta como excusa para pedir horas extra,
>    sacrificio personal o silencio ante malas condiciones, a cambio de nada concreto.
> 2. **Confundir identidad con obediencia** — el discurso de pertenencia hace que cuestionar
>    una decisión se sienta como traición al equipo, no como parte normal del trabajo.
> 3. **Culpar al individuo por fallas estructurales** — si algo sale mal, es que "no se puso la
>    camiseta", lo que desvía la responsabilidad de decisiones que tomó la organización.
>
> **Guion completo, 2026-08-07:** 5.239 palabras habladas, 40:00 medidos programáticamente,
> esqueleto A (canónico), sin referencia a EP.024. Tres casos con fuente primaria: WeWork
> (comunicados de SoftBank), Uber/Susan Fowler (su propio blog + video del tablero de Kalanick),
> Wells Fargo (consent order CFPB + LA Times 2013 + caso nombrado de Claudia Ponce de Leon).
> Ver `pipeline-state-ep025.md` para las citas literales completas y los pendientes que quedan
> (lints, atribución de "Eight is Great", teasers de EP.024 y EP.026).
> **Por qué se renumeró:** EP.025 original (vacante) nunca tuvo guion ni grabación — el slot
> estaba vacío en la práctica. El episodio que sí está listo pasa a ocupar el próximo cupo real.

> **EP.026 — el ángulo y por qué se giró (2026-08-01, renumerado de EP.025 a EP.026 el
> 2026-08-07).** La idea nació de foros de LinkedIn y
> Andy la traía en tres piezas: (a) contratar en LatAm por costo termina pidiendo requisitos
> altos por un salario irrisorio; (b) qué le pasa a la oferta laboral cuando la gente acepta
> esos puestos por necesidad; (c) por qué los reclutadores hoy son más exigentes y hacen
> ghosting sin entrevistar, al revés que en la pandemia, cuando le rogaban al candidato.
>
> **Se giró el punto de vista, no el material.** Las tres piezas están escritas desde el
> **candidato**, y la audiencia verificada de BTQ es el que **contrata** (gerente/supervisor
> de ~40). El ángulo aprobado —«llevo cuatro meses sin llenar esa vacante»— conserva (a) y (b)
> completas con el oyente como protagonista.
>
> **Dos banderas señaladas y pendientes de resolver al escribir:**
> - **Evergreen:** «ahora más que nunca los reclutadores ghostean, al revés que en la pandemia»
>   es coyuntural y el roadmap exige evergreen. La versión que aguanta es el **ciclo de poder
>   del mercado laboral**, con la pandemia como ejemplo y no como eje. La pieza (c) entra así o
>   no entra.
> - **Conflicto de interés:** Andy tiene HireSignal y Kuma Talent. Un episodio sobre
>   reclutamiento puede leerse como publicidad. **Se declara en el disclaimer de encuadre del
>   segmento 0**, no se disimula. Decidido antes de escribir, no después.
>
> **Sourcing pendiente:** aplica el mismo estándar del carril — 2-3 casos nombrados con
> consecuencias verificables. Un episodio sobre el mercado laboral sin casos duros se vuelve
> opinión, que es peor que teórico.

> **Ley de Little — decidida como pilar SEO (2026-08-01).** Era EP.025 bajo el roadmap
> anterior. Se evaluó reencuadrarla como episodio de Oficio de Jefe («Póngale más gente»:
> por qué la cola no baja) y **Andy escogió mantenerla en el carril teórico**. El teaser que
> la anunciaba se grabó dentro del EP.024 de Peter, así que la promesa **no está publicada**
> y no obliga a ninguna fecha.
>
> ⚠️ **SUPERADO 2026-08-23:** esa última frase dejó de ser cierta el día que EP.027 (el
> episodio de Peter, renumerado) salió al aire con el teaser intacto — la promesa **sí es
> pública** ahora. Andy decidió adelantar Little de EP.031 a EP.028 para honrarla. Ver la
> fila de EP.028 en la tabla y la nota de rotación 3+1 más abajo.

> **EP.024 — por qué este tema** (decisión de Andy, 2026-07-25). Continúa directamente el cierre
> de EP.023, que preguntó literalmente «¿a quién ascendió? ¿a quién no le renovó?», y cumple el
> teaser grabado: «una idea que todo el mundo repite en las reuniones». Es el primer episodio con
> el **disclaimer de encuadre** nuevo (ver `guion-style-btq.md`) y el primero dimensionado con la
> tabla recalibrada — con esqueleto fusionado son **~5.565 palabras escritas** para el centro del
> estándar, no las ~4.700 de la tabla vieja.
> **Fuente primaria por verificar al escribir:** el roadmap exige confirmar la fuente antes de
> redactar. Peter/Hull 1969 es la referencia que tengo, pero no la he abierto en esta sesión.

---

## Estrategia editorial (analytics Spotify 2026-06-12; giros 2026-07-21 y 2026-07-25)

**Audiencia núcleo (verificada):** hombre 35–44 (43% del total; 56% sumando todo el rango),
Colombia 70% + EE.UU. 20%, escucha en Android y ~15% en desktop Windows (en el trabajo).
Perfil: gerente/supervisor de ~40 años.

### Rotación 3+1 y carril «Oficio de Jefe» (2026-08-01) — SUPERA el giro del 2026-07-21

**Decisión de Andy**, tomada después de grabar el EP.024 de Peter y sentirlo «demasiado
teórico, como una reseña y un análisis, sin nada memorable que rescatar».

**Lo medido que respalda la decisión** (sobre el guion grabado, 5.427 palabras habladas):

| Tramo | Palabras | % |
|---|---|---|
| Montaje: historia del libro + metodología del paper (segmentos 0-3) | 2.072 | 38% |
| **Contenido aplicable** (único tramo accionable, arranca en el minuto ~38 de 45) | **753** | **13,9%** |

Los tres casos nombrados eran Barings (1995), Antietam (1862) y *The Office* (ficción):
ninguno es una operación contemporánea. El formato «teórico nombrado + su paper» llevaba
cuatro episodios seguidos (Crosby, Hawthorne, Peter, y Little iba de quinto).

**Regla nueva — rotación 3+1.** Reinstaura la cadencia de «un pilar SEO al mes» que el giro
del 2026-07-21 había reemplazado, pero el carril acompañante ya **no es pop-culture**:

1. **Tres episodios de Oficio de Jefe**, luego **uno de pilar SEO**. Se cuenta desde EP.024.
   **El cupo de un carril se cuenta contra la tabla de arriba, no se deriva de «3+1» de
   memoria.** El 2026-08-03 se afirmó dos veces que el siguiente pilar libre era EP.032
   —es EP.035— teniendo la tabla a la vista. Es §Procedencia: una aritmética sobre el estado
   del roadmap es una afirmación sobre el roadmap, y se comprueba abriéndolo.
   **Excepción puntual, 2026-08-23:** EP.028 rompe el patrón a propósito — Pilar SEO
   (Little) justo después de otro Pilar SEO (EP.027), sin los 3 de Oficio de Jefe entre
   medio — para honrar el teaser que EP.027 ya sacó al aire en vivo. Los Oficio de Jefe
   #4-6 no se cancelan, se corren un puesto (EP.029-031). La cadencia 3+1 se retoma después
   de EP.028, no se abandona.
2. **Oficio de Jefe** = el sujeto del episodio es un **problema operativo recurrente**, no
   una teoría. Se titula con la frase que el oyente ya usa («Mi puerta siempre está abierta»,
   «Póngale más gente»). La teoría entra solo si sostiene un punto concreto, y puede no tener
   apellido famoso. Sigue siendo evergreen y buscable — la gente busca el problema, no el
   nombre del teórico.
3. **Pilar SEO** = lo que se venía haciendo desde EP.020: teórico nombrado, paper citable,
   fórmula de título invertida. **No se retira nada de su ADN ni de sus reglas**; solo deja de
   ser todos los episodios y pasa a ser uno de cada cuatro.
4. **El ADN de casos es intocable en los DOS carriles:** 2-3 casos reales y nombrados con
   consecuencias severas y verificables. Un episodio de Oficio de Jefe sin casos duros no
   queda «más operativo», queda en opinión — que es peor que teórico.
   **Precisión de Andy, 2026-08-03: el caso puede venir de cualquier industria, pero cada uno
   tiene que aterrizar en la operación del oyente con equivalentes nombrados.** Lo regional
   ayuda y se prefiere, pero **no es obligatorio**; lo obligatorio es la correlación. Un
   reactor nuclear o una sala de urgencias sirven si el guion traduce: «en su operación esto
   se llama…». Es la técnica que hizo aterrizar el edificio Space en EP.024 —«las costuras se
   llaman *ya hablé con él*, *le pusimos un refuerzo esta semana*, *lo estamos monitoreando*»—
   y sin ella el caso queda como una curiosidad de otro mundo.
5. **La columna de fuentes del carril nuevo no es el paper**, porque no lo hay: son
   investigaciones de incidentes, hallazgos de reguladores, expedientes judiciales y
   post-mortems públicos. Se verifican con el mismo estándar.

**El nombre «Oficio de Jefe» y dónde se publica (decidido 2026-08-01).** Se escogió sobre
`Manejo de Personal` (más volumen de búsqueda pero genérico y sin voz), `La Operación`
(buen nombre, mal keyword — compite con cirugía y con operativos policiales) y
`Frases de Reunión` (memorable, no lo busca nadie). Gana porque carga **«jefe»**, que es a la
vez lo que el oyente escribe en el buscador y con lo que se identifica, y porque hace eco del
remate ya grabado en el episodio de Peter: *«el ascenso no es un premio, es un cambio de
oficio»*.

- **NO va como prefijo en el título del episodio.** La fórmula invertida ya usa ese espacio
  para el problema en las palabras del oyente, que es la keyword que hoy funciona; un prefijo
  se la come. El título de un episodio de Oficio de Jefe es solo la frase del problema.
- **Va donde Spotify sí indexa:** como agrupación de serie/temporada y en la descripción del
  show. Un nombre de carril que solo vive en este roadmap no lo ve nadie y no ayuda al
  algoritmo.
- **Esto le da una respuesta posible al pendiente de la línea de abajo** («No existía sistema
  de temporadas — si el corte va a significar algo para el oyente, hay que crearlo»,
  2026-07-25). El corte de temporada del alcance macro y el arranque de este carril caen en el
  mismo punto: EP.024.
  **Propuesta, NO aprobada todavía:** montar la agrupación en Spotify for Podcasters y
  actualizar la descripción del show en `metadata-v4-macro.md`. Es un cambio en una plataforma
  pública y **necesita el sí de Andy antes de tocarlo** — no hay nada urgente empujándolo,
  porque no hay episodio publicado esperando esa agrupación.

⚠️ **HISTÓRICO — SUPERADO 2026-08-20/23.** Lo que sigue describía el estado del 2026-08-01,
cuando el audio de Peter estaba grabado pero no publicado. Ya no es cierto: **el guion se
reusó tal cual, sin regrabar ningún tramo** (decisión de Andy, 2026-08-20 — los dos errores
quedaron aceptados, ver `pipeline-state-ep027-peter.md`), y **el episodio sí está en una
plataforma** — publicado como EP.027 el 2026-08-23, con el teaser de Little en vivo. Se
conserva sin reescribir como registro de la decisión original.

**Sobre la grabación de EP.024 (Peter):** no se descarta. El tema se reubicó a EP.027 como el
pilar SEO de la primera vuelta. **Si se reusa el audio, hay que regrabar dos tramos**: el
segmento 0 dice «episodio 24» y el segmento 7 anuncia la Ley de Little como el episodio
siguiente. Queda abierto si el guion se reusa tal cual (13,9% aplicable) o se reestructura
antes — la queja de Andy fue del contenido, no solo de la frecuencia.

> **NADA DE ESTO TOCA NINGUNA PLATAFORMA** (confirmado por Andy, 2026-08-01). El episodio se
> grabó pero **nunca se subió ni se programó**: no hay publicación que retirar, ni fecha que
> mover, ni metadata que corregir en Spotify o YouTube. Toda esta reorganización vive en el
> roadmap y en disco. **Lo único ya público que sí restringe el contenido** es el teaser
> grabado dentro de EP.023, que prometió «una idea que todo el mundo repite en las reuniones»
> y verificar «si de verdad aguanta» — eso es una restricción de guion, no una acción de
> plataforma.

### Vetas en exploración — el cliente y la región (2026-08-03)

**No son un carril nuevo y no tocan la rotación 3+1.** Decisión de Andy: se espera a que la
rotación dé una vuelta completa antes de evaluar si esto merece carril propio. Mientras tanto
son **temas dentro de Oficio de Jefe**, y esta sección existe para que cuando llegue el momento
no se re-derive desde cero.

**De dónde salió.** Andy señaló el 2026-08-03 que el show lleva 24 episodios hablando del que
atiende y ninguno del que espera — y que la cola del nombre es, literalmente, gente esperando.
Ver `brand-constants.md` § esencia, punto 5.

**La disciplina que separa esto de contenido de CX:** el cliente es el **sujeto**; el jefe sigue
siendo el **protagonista**. El episodio no es «cómo piensa su cliente» —eso le habla a alguien
que hace publicidad— sino **una decisión que el oyente toma y que el cliente siente**. Si el
oyente no puede hacer nada distinto el lunes, el tema se cayó del carril.

#### Veta A — el proceso mal diseñado desde el principio

Nadie lo cambió: nació así. El procedimiento se ejecuta correctamente y aun así produce el mal
resultado, porque optimiza la variable equivocada. El culpable no es quien lo ejecuta.

#### Veta B — la política que se cambió para ahorrar y la pagó el cliente

Tesis: **la política se diseñó para ahorrar, la pagó el cliente, y después la pagó la empresa
multiplicada.** Alguien la aprobó en una reunión, con buenas intenciones y un ahorro proyectado.

> **Separadas a pedido de Andy (2026-08-03).** Son dos cosas: A nació torcido, B se torció al
> cambiarlo. B tiene fecha, acta y responsable; A no tiene a nadie a quien señalar, y esa
> diferencia cambia el episodio entero.

**Frontera obligatoria con EP.022 (Crosby).** El 022 midió el costo **hacia adentro** —
retrabajo, reprocesos, no prevenir. Estas vetas son el costo **hacia afuera y de vuelta**: la
política funcionó como se diseñó, nadie se equivocó ejecutándola, y la cuenta llegó igual. Sin
esa frontera explícita, quien escuchó el 022 siente que se lo repitieron.

#### Prioridad regional (Andy, 2026-08-03)

Casos de **marcas y empresas latinoamericanas**, no todo mercado norteamericano o europeo.
Continúa la decisión del EP.024, donde 2 de 4 casos fueron colombianos y fueron primero.

**La jugada de fuentes — es el movimiento del EP.024 generalizado.** Lo que le dio peso a ese
episodio fue abrir el comunicado n.º 165 de la CGR, no la prensa. El equivalente regional para
políticas de cara al consumidor son los reguladores de protección al consumidor, que publican
resoluciones con hallazgo y multa cuantificada:

| País | Entidad |
|---|---|
| Colombia | SIC — Superintendencia de Industria y Comercio |
| Chile | SERNAC |
| México | PROFECO |
| Brasil | Procon / Senacon |

#### Banco inicial de casos — TODOS SIN FUENTE PRIMARIA ABIERTA

Son pistas para investigar, **no hechos citables**. Ninguno entra a un guion sin abrir el
documento primario primero.

*Región (prioritarios):*
- **La Polar (Chile, ~2011).** Repactación unilateral de deudas de clientes sin su
  consentimiento, a gran escala; terminó en procesos penales y casi acaba con la compañía. Es
  el caso insignia de la veta B: una política aplicada al cliente para proteger ingresos que
  destruyó a la empresa. **Verificar con SERNAC y con el expediente judicial.**
- **Viva Air y Ultra Air (Colombia, 2023).** Colapso abrupto de dos aerolíneas de bajo costo
  con pasajeros varados. Decisión de estructura de costos que terminó de cara al cliente.
- **Avianca — huelga de pilotos ACDAC (2017).** Miles de vuelos cancelados.
- **Rappi (Colombia).** Investigaciones de la SIC en materia de protección al consumidor.

*Fuera de la región, como contraste y solo si la región no da:*
- **Netflix / Qwikster (2011).** Reestructuración de precio y separación del servicio; pérdida
  fuerte de suscriptores y desplome de la acción, con disculpa pública del CEO.
- **United 3411 (2017).** Lo que lo hace BTQ no es el video: la política **se ejecutó al pie de
  la letra** y dejó al empleado de primera línea sin ninguna salida decente.
- **Ryanair (2017).** Miles de vuelos cancelados por cómo se programaron las vacaciones de los
  pilotos.
- **Comcast (2014).** La llamada de retención grabada: un incentivo mal diseñado dejó al agente
  sin permiso para hacer lo único razonable.

**Hilo común de los cuatro de afuera:** la primera línea quedó atrapada entre el cliente y una
política que alguien firmó arriba. Esa es la conexión con la audiencia — el oyente no es el
cliente furioso, es quien aprobó la política o quien tiene que defenderla.

#### Casos QUEMADOS — no reusar

| Caso | Dónde se usó |
|---|---|
| Boeing | EP.022 |
| Volkswagen | artículo del EP.023 |
| Nokia, Reficar, Hidroituango, edificio Space, Grenfell | EP.024 |
| Wells Fargo | **EP.001 de Corporate Crime Confidential** — otro show de Andy; reusarlo se nota |

#### Choque de calendario a vigilar

La **Ley de Little es el EP.028** (adelantada de EP.031 el 2026-08-23) y también es sobre
colas. Son distintos —Little es la matemática del flujo; la veta del cliente es percepción y
política— pero no van pegados.

### Temas que llegan de un sugeridor externo — cómo se filtran (2026-08-03)

Andy trajo dos tandas (~21 temas) de una herramienta de sugerencia. Sirven, pero **como materia
prima del carril pilar SEO, no como lista de episodios.** Por construcción sugieren sobre
conceptos indexados: efecto con nombre propio + su explicación. Un problema operativo sin
apellido famoso no está indexado, así que **la herramienta no puede producir candidatos de
Oficio de Jefe** — que es donde están los cupos abiertos.

> **Corrección 2026-08-03:** en la primera versión de esta sección se escribió que el siguiente
> cupo de pilar era EP.032. **Es EP.035.** La rotación se cuenta desde EP.024: 024-026 Oficio →
> 027 pilar; 028-030 Oficio → 031 pilar; 032-034 Oficio → 035 pilar.

> ⚠️ **Pendiente de aclarar con Andy:** no está confirmado si la herramienta usa datos de
> búsqueda o si genera con un modelo a partir de un prompt (la captura muestra una caja «Try a
> topic, theme or a question», que sugiere lo segundo). **Si genera, no trae señal de demanda**
> y el argumento SEO para adoptar sus temas se cae. No dar por hecho el mecanismo.

**Lo que la lista sí reveló, y es un dato:** 8 de los primeros 15 venían enmarcados en call
center (*tickets, agents, frontline, scripts, sales calls, CX*). El clasificador todavía tiene a
BTQ en el carril que el show dejó el 2026-07-25 — el costo de SEO que se aceptó a sabiendas.

**Las cinco compuertas, en orden. La primera que falle descarta:**

1. **Carril.** ¿Es pilar SEO u Oficio de Jefe? Casi todos son pilar. Los cupos de pilar están
   tomados hasta EP.031; el siguiente real es **EP.035**.
2. **Quemado o comprometido.** Contra la tabla del roadmap y la de casos quemados. En la tanda
   del 2026-08-03 venía el **Principio de Peter, que ya estaba grabado** como EP.027.
3. **¿La fuente aguanta?** Muchos efectos famosos están cuestionados y este show no puede
   pararse en uno sin decirlo. Marcados en esa tanda: **Dunning-Kruger** (el patrón aparece
   incluso en datos aleatorios por autocorrelación), **efecto Cobra** (la anécdota de Delhi no
   tiene respaldo documental; se popularizó en 2001), **bystander/Kitty Genovese** (los 38
   testigos son una distorsión del reportaje original), **Broken Windows** (contestada y
   políticamente cargada), **Dunbar 150** y **Zeigarnik** (réplicas en duda). *Todos por
   verificar contra fuente primaria antes de comprometerse — ninguno se descarta de memoria.*
   Y ojo: desmontar un estudio famoso **ya se hizo en EP.023** con Hawthorne. Repetir el
   movimiento dentro de la ventana de 5 episodios se nota.
4. **¿El protagonista es el jefe?** Descarta lo que le habla a quien hace publicidad (IKEA,
   Loss Aversion, anchoring en ventas, Pavlov) salvo que se reencuadre como **una decisión que
   el oyente toma**. Ver la disciplina de la veta del cliente, arriba.
5. **¿Hay 2-3 casos nombrados con consecuencias verificables, y de la región?** Sin eso el
   episodio queda en opinión, que es peor que teórico.

**El título sugerido no se adopta nunca.** Viene en inglés y con la fórmula de otro show. Se
toma el concepto; el título se reescribe con la fórmula vigente.

**Sesgo a vigilar:** el sugeridor empuja hacia lo saturado (Dunning-Kruger, survivorship bias,
Parkinson son clichés de contenido de LinkedIn). Rankear en una keyword saturada es más difícil
que en una frase de problema específica — el mismo argumento que sostiene la titulación de
Oficio de Jefe.

**Sobrevivientes de las dos tandas del 2026-08-03**, ya con las compuertas corridas:

| Tema | Veredicto |
|---|---|
| **Cognitive Load (Sweller)** | El mejor. Reencuadrado como Oficio de Jefe: *«el procedimiento está escrito y aun así se equivocan»*. Teoría sólida, sin polémica de replicación, no repite nada del catálogo |
| **Parkinson — Ley de la Trivialidad** | Fuerte. Origen citable (1957, el comité de la planta nuclear contra el cobertizo de bicicletas) sin depender de un paper frágil |
| **Paradoja de Abilene** | Buena, pero **demasiado cerca del EP.024**: los dos son sobre el silencio. Para EP.029-030, no antes |
| **Ley de Parkinson** (las 8 horas) | Pilar SEO para **EP.035**, el siguiente cupo real del carril. Ya está anunciada en la home junto a Goodhart y Crosby |
| **Efecto Pygmalion** | Choca con EP.023 — Hawthorne y Pygmalion son el mismo movimiento de fondo. A favor: los experimentos de campo de Dov Eden en el ejército israelí son material más defendible que el estudio escolar de Rosenthal |
| **Riesgo moral** | Sirve, pero pisa el EP.020 (Goodhart). Distinguible —trasladar el riesgo no es falsear la métrica— pero hay que escribir esa frontera |

### Giro de alcance 2026-07-25 — de call center a gestión empresarial

**Decisión de Andy.** El show sale del techo de BPO/contact center y pasa a **gestión de
equipos y operaciones en cualquier industria**. La teoría puede venir de donde sea; el
aterrizaje es «su equipo / su empresa». Arranca como **corte de temporada**: las portadas de
EP.011–EP.023 se quedan como están, el sistema visual nuevo empieza de EP.024 en adelante.

- **Costo aceptado:** se pierde la cola larga SEO de «call center». Se le señaló que EP.020
  —el único episodio con buen desempeño medido— probablemente rankeó por esa keyword, y
  decidió proceder. Por eso **EP.020 no se retitula**.
- **La esencia no se toca:** mundo Sala de Máquinas, voz de trinchera, formato de teórico
  nombrado, ritual de apertura y cierre, metáfora de la cola. Detalle en
  `episode-launch/docs/brand-constants.md` § Giro de alcance.
- **Metadata nueva** (portada, descripción, categorías, retitulación): `metadata-v4-macro.md`.
- **No existía sistema de temporadas** — «T2» aparecía solo como decoración en la web, no en
  este roadmap ni en la metadata de ningún episodio. Si el corte va a significar algo para el
  oyente, hay que crearlo.

**Repertorio que destraba el giro** (teorías reales, verificar fuente primaria al escribir):
Ley de Little (teoría de colas — el episodio que el show le debe a su propio nombre), Ley de
Parkinson, Principio de Peter, Ley de Brooks, Teoría de Restricciones (Goldratt), Deming,
Herzberg, «Ruido» (Kahneman), efecto Ringelmann.

> **Precisión 2026-08-01:** esta lista es el repertorio del **carril pilar SEO**, o sea 1 de
> cada 4 episodios. No es la lista de temas del show. Leerla como tal fue parte de lo que
> volvió el roadmap enteramente teórico: los 4 episodios previos a EP.024 salieron de aquí.

### Giro estratégico 2026-07-21 — BTQ pasa a 100% pilar SEO

> ⚠️ **SUPERADO el 2026-08-01 por la rotación 3+1** (arriba). Lo que sigue se conserva como
> registro de por qué se tomó y de la evidencia que lo sostuvo. **Lo que sigue vigente:** el
> retiro de la cultura pop y todas las reglas de titulación y de ADN de los episodios pilar
> SEO. **Lo que dejó de mandar:** que TODOS los episodios sean pilar SEO — ahora es 1 de cada 4.

**Decisión de Andy:** retirar la cultura pop del roadmap de forma permanente (no
caso por caso). Lectura de Andy sobre el desempeño reciente: EP.019 (Gladiator) y
EP.021 (Los Simpson) no funcionaron bien, mientras EP.020 (pilar SEO, métricas/KPIs)
sí funcionó muy bien — señal más fuerte y más reciente que la nota de "referentes
80s/90s primero" de la sección original (basada en datos de 2026-06-12, que solo
comparaba EP.012 Queen vs. EP.015 Solid Snake dentro de la era pop-culture, sin
todavía EP.019/EP.021 en la muestra). De aquí en adelante:

- ~~**Todo episodio de BTQ es pilar SEO** — evergreen, keyword-first, sin referente pop.
  Reemplaza la regla anterior de "un pilar SEO al mes" y la rotación con pop-culture.~~
  **RETIRADO 2026-08-01:** vuelve la cadencia de 1 pilar SEO cada 4, con Oficio de Jefe
  —no pop-culture— como carril acompañante. Lo demás de esta lista sigue vigente.
- **Título con el nombre del creador de la ley/teoría** cuando el episodio ancla en
  una con autor identificable (regla ya fijada en `guion-style-btq.md` tras el
  feedback de Andy sobre EP.020/EP.022, que no lo hicieron) — ej. "La Ley de
  Goodhart", "Philip Crosby y el costo de la mala calidad", no solo el concepto
  en abstracto.
- **Reglas retiradas (no borradas, en pausa):** "referentes 80s/90s primero" y la
  "fórmula de título pop-culture" (`EP.XX — [Referente]: [frase con keyword]`) —
  se mantienen documentadas abajo por si el roadmap vuelve a abrir un carril de
  pop-culture más adelante, pero no aplican mientras el giro esté vigente.
- **EP.023 (Matrix)** se descartó por este giro — el guion completo que se había
  escrito se eliminó (2026-07-21), no se archivó, por decisión explícita de Andy.

**Reglas vigentes para elegir y titular episodios (post-giro):**

1. ~~**Pilar SEO siempre**~~ — **ajustado 2026-08-01: keyword-first siempre, pilar SEO 1 de
   cada 4.** Todo episodio sigue siendo evergreen, buscable y sin referente pop; lo que cambia
   es de dónde sale la keyword. En pilar SEO viene de la métrica, ley o teoría citable (mismo
   patrón que EP.020 y EP.022); en Oficio de Jefe viene del **problema tal como el oyente lo
   busca**. La razón de fondo no se toca — el título tiene que ganarse el buscador. Razón
   original que sigue vigente: la adquisición de oyentes nuevos cayó de ~30/mes
   (marzo) a ~4/mes (junio) y EP.01 sigue siendo #1 all-time en consumo gracias a
   Search (193 de 245 impresiones) — los episodios pop-culture ganaban el
   algoritmo pero eran invisibles en el buscador.
2. **Título con nombre del creador** cuando hay uno identificable (ver arriba).
3. **Numeración consistente:** `EP.XX` (dos dígitos, mayúsculas, guion largo). Nunca
   "Ep.11", "EP.015" ni sufijo "| Behind the Queue" en el título de Spotify.
4. **Cadencia semanal estricta — nunca menos de 7 días entre episodios.** Lección
   EP.015: salió 4 días después del EP.014 y quedó como el episodio más flojo del
   catálogo (11 plays).

**Feedback de Andy sobre EP.022 (2026-07-13):** le gustó más el EP.020 (pilar SEO,
métricas/KPIs) que el EP.021 — lo sintió "más profesional", sobre todo por tocar temas
operacionales. Primera señal del giro que se confirmó y se hizo permanente el 2026-07-21.

**Tema EP.022 confirmado (2026-07-14):** costo de mala calidad (Cost of Poor Quality)
en call center, anclado en Philip Crosby ("Quality Is Free", 1979) — mismo patrón que
EP.020 (métrica + teoría real citable), esta vez con ángulo P&L explícito: cuánto le
cuesta a la operación NO invertir en calidad (retrabajo, quejas, reprocesos) vs.
prevención.

---

### Reglas retiradas (pop-culture, en pausa desde 2026-07-21)

Documentadas por si el roadmap reabre este carril más adelante. **Siguen sin aplicar tras la
rotación 3+1 del 2026-08-01:** el carril acompañante del pilar SEO es Oficio de Jefe, no
pop-culture. La cultura pop sigue retirada por la evidencia de EP.019 y EP.021.

1. **Referentes 80s/90s primero** — rock clásico, rock en español, cine de esa era.
   Evidencia parcial (2026-06-12, muestra chica): EP.012 Queen = 40 plays (mejor de
   la era pop-culture) y el algoritmo lo empujaba solo (149 impresiones Home);
   EP.015 Solid Snake = 11 plays (peor del catálogo). Gaming/anime nicho: con
   moderación, no consecutivos.
2. **Fórmula de título pop-culture:** `EP.XX — [Referente]: [frase con keyword BPO /
   liderazgo / call center]`. El gancho emocional se queda, pero el título SIEMPRE
   lleva al menos una keyword buscable.
3. **Candidatos que quedaron sin usar:** Metallica, Matrix, Star Wars — investigados
   y verificados el 2026-07-21 para EP.023 antes del giro; quedan parqueados, no
   descartados como investigación, por si se reabre el carril pop-culture.

---

**Notas:**
- Seeded desde memoria `btq_production_state` (snapshot 2026-06-02) + corrección de
  estado de EP.016 (recording + script confirmados listos por el usuario, pendiente
  publicar en Spotify — 2026-06-07).
- Mantener esta tabla actualizada manualmente o vía `episode-pipeline` — es la fuente
  que Stage A consulta para decidir cuál episodio sigue.
