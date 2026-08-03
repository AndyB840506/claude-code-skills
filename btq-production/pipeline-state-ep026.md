EPISODE: EP.026 (BTQ) — carga cognitiva · «el procedimiento está escrito y aun así se equivocan»
stage_a: **en curso** — tema fijado 2026-08-03, casos en verificación. Guion no iniciado.
stage_b: no iniciado.
stage_c: no iniciado.

**Carril:** Oficio de Jefe #3. **Publica:** domingo 2026-09-06, 8:00 PM Colombia (cadencia semanal
desde EP.024 del 2026-08-02; verificado con calendario, no estimado).

> Ojo: la fecha de arriba asume que EP.025 sale el 9 de agosto y EP.026 el 16. **Recalcular si
> alguno se corre.**

## Título — recortado 2026-08-03

```
EP.26 — Por qué su equipo no sigue el procedimiento: carga cognitiva
```

**58 caracteres · ancla de 7 palabras.** Dentro del techo nuevo (70 car. / 9 palabras de ancla),
que se midió justamente a raíz de este título — ver `guion-style-btq.md` § Largo máximo.

*Primera propuesta, descartada:* `Por qué su equipo se equivoca aunque el procedimiento esté
escrito: carga cognitiva` — 83 caracteres, el outlier de todo el catálogo post-giro (46-70).

**Por qué esta versión es mejor que la larga, y no solo más corta:** «por qué mi equipo no sigue
el procedimiento» es lo que un jefe teclea en un buscador. El título plantea **el diagnóstico
equivocado** —que no lo siguen— y el episodio lo voltea: no es desobediencia, es que el
procedimiento se diseñó para no poder seguirse bajo carga.

> ⚠️ **Coherencia título ↔ guion (regla vigente).** La promesa del título tiene que responderse
> explícitamente en el cuerpo. Acá eso significa un momento donde se dice, sin rodeos, que la
> gente **sí** está tratando de seguirlo. Si el episodio no desmonta la premisa del título, el
> título queda acusando al equipo, que es lo contrario de la tesis.

## De dónde salió el tema

Del filtro de sugeridor externo (ver `roadmap-btq.md`). Fue la única sobreviviente utilizable
pronto: los cupos de pilar SEO llegan hasta EP.035, así que se reencuadró de «Cognitive Load
Theory: simplifying complex scripts for agents» —título de la era call center— al problema
operativo. La teoría de Sweller entra como columna, no como sujeto.

## Estructura — esqueleto E, el del EP.024

Acción primero: la recomendación cae en el minuto 2 y el resto la justifica. En EP.024 ese
esqueleto dio **29,3% de contenido aplicable** arrancando en el 2,7% del guion (la compuerta
exige ≥25% y arranque <60%).

**Taxonomía de tres, calcada de las «cuatro formas» del EP.024:**

| Caso | Qué falló |
|---|---|
| Three Mile Island, 1979 | **el procedimiento sobraba** — 100 alarmas en minutos, sin forma de priorizar |
| Avianca 052, 1990 | **el procedimiento no llegó a tiempo** — la palabra existía y bajo carga no salió |
| Keystone ICU, Michigan, 2006 | **le quitaron carga en vez de ponerle** — y funcionó, medido |

El tercero es el ancla de «qué hace usted el lunes»: la recomendación no es capacitar más, es
reducir la carga y volver imposible saltarse el paso crítico.

## ⚠️ Instrucción de Andy sobre el caso Avianca (2026-08-03) — ELEMENTO OBLIGATORIO

El caso roza el EP.024 (Nokia: «el mensaje nunca llegó arriba»). **Andy decidió no cambiarlo
sino ponerlo de frente y marcar la diferencia en el aire:**

> «Que no lo vean con los ojos del mensaje no llegó, sino de que fue el diseño el que falló.»

O sea: el guion **nombra explícitamente** la cercanía con el EP.024 y la desmonta. En el 024 el
mecanismo era el **miedo** —hablar tenía un precio—. Acá el mecanismo es **carga y diseño**: la
tripulación sí habló, dijo lo que el procedimiento le permitía decir, y el diseño no cargaba el
significado. Es una referencia cruzada al catálogo, que el show ya usa.

## Casos — estado de verificación

### 1. Three Mile Island — ✅ VERIFICADO en fuente primaria (2026-08-03)

Informe de la Comisión Presidencial (Kemeny), PDF con capa de texto. Citas literales:

- «Frederick and Faust were in the control room when the first alarm sounded, followed by a
  **cascade of alarms that numbered 100 within minutes**.» (p. 22)
- Testimonio de Craig Faust ante la Comisión, nota 17: **«I would have liked to have thrown away
  the alarm panel. It wasn't giving us any useful information.»** (pp. 22-24)
- Estado normal de la sala, antes del accidente: «panel upon panel of red, green, amber, and
  white lights; and **alarms that sound or flash warnings many times each hour**.» (p. 22)
- **La línea que sostiene la tesis:** «each was a product of his training — training that did not
  adequately prepare them to cope with the accident at TMI-2. Indeed, **their training was partly
  responsible for escalating what should have been a minor event into a potentially devastating
  accident**.» (p. 22)

Esa última frase es la que convierte el caso en «falló el diseño», no «fallaron los operadores»
— dicho por la comisión presidencial, no por el podcast.

### 2. Avianca 052 — ✅ VERIFICADO en fuente primaria (2026-08-03)

**NTSB/AAR-91/04**, adoptado el 30 de abril de 1991. PDF escaneado de 293 páginas, sin capa de
texto: se rasterizó con PyMuPDF y se leyó como imagen (ver § Herramienta, abajo).

- Boeing 707-321B, matrícula colombiana **HK 2016**, Cove Neck, Nueva York, **25 de enero de 1990**.
- **158 personas a bordo, 73 con heridas mortales.**
- «the flightcrew was placed in holding **three times** by air traffic control for a total of about
  **1 hour and 17 minutes**.»
- En la tercera espera la tripulación reportó que no podía esperar más de 5 minutos, que se estaba
  quedando sin combustible y que no alcanzaba su alterno, Boston-Logan.
- Pérdida de potencia en los cuatro motores; cayó a unas 16 millas del aeropuerto.
- **Causa probable, literal:** «the failure of the flightcrew to adequately manage the airplane's
  fuel load, and their failure to communicate an emergency fuel situation to air traffic control
  before fuel exhaustion occurred.»
- **Factores contribuyentes, literal:** «the flightcrew's failure to use an airline operational
  control dispatch system… Also contributing to the accident was inadequate traffic flow
  management by the Federal Aviation Administration and **the lack of standardized understandable
  terminology for pilots and controllers for minimum and emergency fuel states**.»
- **Y el enlace directo con la carga:** «windshear, **crew fatigue and stress** were factors that
  led to the unsuccessful completion of the first approach and thus contributed to the accident.»
- Uno de los cuatro temas de seguridad del informe: «Flightcrew coordination and **English
  language proficiency of foreign crews**.»

> ⚠️ **Discrepancia dentro del propio informe, resuelta.** El sumario ejecutivo abre con «On
> **July 19, 1989**». La portada, el abstract y el resto del informe dicen **25 de enero de 1990**,
> que es la fecha correcta. Es un error de tipeo del documento. **No usarlo como dato**; si se
> menciona al aire como ironía —un informe sobre una falla de comunicación que se equivoca en su
> propia primera página— tiene que ir explicado, o parece que el error es nuestro.

### 3. Keystone ICU (Pronovost, NEJM 2006) — ✅ VERIFICADO (2026-08-03)

NEJM y AJIC devuelven **403** y PubMed bloquea con captcha. El abstract publicado sí está en el
repositorio institucional de Johns Hopkins, y de ahí salen las cifras.

Cita: Pronovost, P., Needham, D., Berenholtz, S., Sinopoli, D., Chu, H., Cosgrove, S., Sexton,
B., Hyzy, R., Welsh, R., Roth, G., Bander, J., Kepros, J., & Goeschel, C. (2006). *An
intervention to decrease catheter-related bloodstream infections in the ICU.* **New England
Journal of Medicine, 355(26), 2725-2732.**

- «A total of **108 ICUs** agreed to participate in the study, and **103 reported data**.»
- **1.981 meses-UCI** y **375.757 días-catéter** en el análisis.
- Línea base: **mediana 2,7** · **media 7,7** infecciones por 1.000 días-catéter.
- **0-3 meses: mediana 0.** · **16-18 meses: media 1,4.**
- Razones de tasa de incidencia: **0,62 (IC 95%: 0,47-0,81)** a los 0-3 meses y
  **0,34 (IC 95%: 0,23-0,50)** a los 16-18 meses.

> ⚠️ **Los resúmenes de búsqueda traían la cifra mal atribuida en el tiempo, y por poco entra
> así.** Decían «la tasa cayó 66% en los primeros tres meses». Falso: a los 0-3 meses la razón
> es 0,62, o sea **38%** de reducción. El **66% es 1 − 0,34, y eso es a los 16-18 meses**. La
> mediana sí llegó a 0 en los primeros 3 meses, y ahí está el origen de la confusión: se mezcló
> la mediana temprana con el porcentaje tardío.
>
> **Al aire, la forma correcta es la de dos tiempos** — y además es mejor historia: bajó rápido,
> y lo difícil (y lo que se sostuvo 18 meses) fue que no volviera a subir.

⚠️ **NO verificado, no usar todavía:** la cifra de «más de 1.500 vidas y ~USD 175 millones»
circula asociada al proyecto pero **no está en este abstract**. Si se quiere decir al aire, hay
que buscar de dónde sale.

## Herramienta — lectura de PDF escaneados

`pymupdf`, instalado el 2026-08-03 para abrir el informe de la NTSB. **La receta y el porqué
viven en `skills/CLAUDE.md` § instrumentos que mienten en silencio** — no se repiten acá.

## Pendientes antes de escribir

- [x] ~~Cerrar el caso 3~~ — **cerrado 2026-08-03** vía el repositorio de Johns Hopkins, y de
      paso se atrapó una cifra mal atribuida en el tiempo.
- [x] ~~Confirmar el título~~ — recortado a 58 caracteres el 2026-08-03.
- [x] ~~Decidir si el tercer caso se cambia por uno de la región~~ — **Andy: los tres se quedan.**
      Lo regional no es obligatorio; lo obligatorio es la correlación con el oyente (abajo).
- [ ] Sweller: abrir la fuente de la teoría de carga cognitiva, no citarla de memoria.

## ⚠️ Correlación con el oyente — instrucción de Andy (2026-08-03)

Los tres casos se quedan como están. Pero vienen de un reactor nuclear, una cabina y una UCI, y
el oyente dirige una operación. **Cada caso tiene que aterrizar con equivalentes nombrados en su
mundo, o queda como curiosidad de otro planeta.** Regla general en `roadmap-btq.md` § rotación,
punto 4.

Aterrizajes obligatorios, uno por caso:

| Caso | Cómo se llama eso en la operación del oyente |
|---|---|
| TMI — 100 alarmas sin jerarquía | el tablero donde todo está en rojo, las alertas que ya nadie abre, el chat con 40 notificaciones por hora |
| Avianca — la palabra que no cargaba el significado | «urgente» en el asunto de un correo que ya todos escriben, el «prioridad alta» del ticket que perdió sentido, escalar sin una palabra que obligue |
| Keystone — quitar carga, no ponerla | de 14 pasos a los 5 que importan, y volver imposible saltarse el crítico |

La técnica de referencia es la del EP.024 con el edificio Space: «en su operación las costuras se
llaman *ya hablé con él*, *le pusimos un refuerzo esta semana*, *lo estamos monitoreando*». Sin
ese puente, Space habría sido una tragedia ajena; con él, el oyente se reconoce.

**El caso de Avianca tiene doble deber:** ese aterrizaje, y además la distinción explícita con el
EP.024 (ver arriba).
