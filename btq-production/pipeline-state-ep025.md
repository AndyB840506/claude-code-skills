EPISODE: EP.025 (BTQ) — «ponerse la camiseta»: el discurso de lealtad como herramienta tóxica

**⚠️ RENUMERADO 2026-08-07 (segunda vez el mismo día): era EP.026, ahora es EP.025.** EP.025
("cuatro meses sin llenar la vacante") nunca tuvo guion ni grabación — el slot 25 estaba vacío
en la práctica, así que el episodio que sí está listo para producirse pasa a ocupar ese lugar.
"Cuatro meses sin llenar la vacante" se corre a EP.026. Ver `roadmap-btq.md` para el detalle del
swap — no hubo cascada, solo estos dos números intercambiaron contenido.

stage_a: **en curso** — tema y los tres casos fijados 2026-08-07 (reasignado desde carga
cognitiva, ver `pipeline-state-carga-cognitiva-parked.md`). Casos verificados en fuente primaria
o directamente en la fuente original. Guion completo y medido — ver
`launch-assets/EP025-camiseta-guion.artifact.html`.
stage_b: no iniciado.
stage_c: no iniciado.

**Carril:** Oficio de Jefe #2. **Origen:** video que un amigo de Andy le compartió sobre el
mensaje tóxico de "ponerse la camiseta" en el entorno laboral (el video en sí no se abrió en
esta sesión — no es la fuente de los casos, solo el disparador de la idea).

## Título y ángulo — ajustado 2026-08-07 (segunda pasada, tras ver el borrador de aterrizajes)

**Título:** `Ponerse la camiseta: la explotación laboral disfrazada de slogan` (64 caracteres, ancla
de 9 palabras).

**Corrección de Andy sobre el enfoque:** no son tres mecanismos paralelos e independientes. Es
**una mentira corporativa con tres caras**: el slogan de "familia"/"misión"/"lealtad" es la
máscara, y la explotación laboral es lo que hay debajo. Los tres casos no ilustran tres
problemas distintos — ilustran tres MOMENTOS de la misma mentira: se vende (WeWork), se
defiende cuando alguien la señala (Uber), y se limpia cuando revienta (Wells Fargo). El giro
del episodio tiene que nombrar esto explícitamente: no es que estas empresas hayan fallado en
vivir su cultura — la cultura ERA el mecanismo de extracción, funcionando exactamente como se
diseñó.

**Orden reconsiderado para esqueleto A:** WeWork primero (la mentira en su forma más pura y
literal — "somos familia" con la asimetría de dólares más flagrante) → Uber (cómo se blinda la
mentira cuando alguien la nombra) → Wells Fargo (qué pasa cuando la mentira revienta: se culpa
a quien más se la creyó, no a quien la vendió) → giro nombrando el mecanismo completo →
aplicación.

## Las tres capas — instrucción de Andy (2026-08-07), las tres juntas

1. **Extraer lealtad sin retribución** — la camiseta como excusa para pedir sacrificio sin nada
   concreto a cambio.
2. **Confundir identidad con obediencia** — cuestionar se siente como traición al equipo.
3. **Culpar al individuo por fallas estructurales** — "no se puso la camiseta" desvía la
   responsabilidad de decisiones que tomó la organización.

## Estructura — esqueleto A (canónico), decisión 2026-08-07

**No esqueleto E** (ya usado en EP.024 y en el intento descartado de este mismo cupo — fue
justo lo que hizo sonar ese intento a reencauche). **Sin referencias cruzadas explícitas a
EP.024.** Esqueleto A está en pausa desde EP.023, así que además cumple la rotación.

## Casos — estado de verificación

### 1. Wells Fargo — «Eight is Great» (2016) — ✅ VERIFICADO en fuente primaria (2026-08-07)

**Ángulo primario: culpar al individuo por fallas estructurales.**

Fuente primaria: **Consent Order, CFPB, 2016-CFPB-0015** (09/08/2016), leído completo vía
pymupdf (mismo caso que los PDF de la NTSB — sin capa de texto extraíble por WebFetch directo,
sí extraíble con pymupdf).

- **1.534.280** cuentas de depósito potencialmente no autorizadas, de las cuales ~85.000
  incurrieron en ~USD 2 millones en comisiones (§16).
- Mecanismo, textual: «Respondent's employees engaged in "simulated funding." To qualify for
  incentives that rewarded bankers for opening new accounts that were funded shortly after
  opening, Respondent's employees opened deposit accounts without consumers' knowledge or
  consent and then transferred funds from consumers' authorized accounts to temporarily fund
  the unauthorized accounts» (§10).
- **Roughly 5.300 empleados despedidos** por "Improper Sales Practices" durante el período
  relevante (§9) — el consent order lo dice explícito: fueron los empleados de base los
  sancionados, no la estructura de incentivos que fijó la meta.
- **Multa civil de la CFPB: USD 100 millones** (§57) — **ojo, cifra compuesta:** el titular de
  prensa "USD 185 millones" es la SUMA de tres acciones regulatorias distintas (CFPB 100M + OCC
  35M + Fiscalía de LA 50M). Al aire, si se usa el total hay que decir que son tres
  organismos, no inventar que los 185M son de un solo ente.
- **"Eight is Great"** (la meta de 8 productos por cliente) y su atribución a John Stumpf
  circulan ampliamente en prensa pero **NO están en el consent order** — es lenguaje interno /
  reportería, no el documento legal. **[VERIFICAR]** antes de citarlo como cita textual de
  Stumpf; se puede usar como "el mote que le pusieron en la empresa" sin atribuírselo
  palabra-por-palabra a él sin más chequeo.

### 2. Uber — Susan Fowler (2017) — ✅ VERIFICADO en fuente primaria (2026-08-07)

**Ángulo primario: confundir identidad con obediencia.**

Fuente primaria: el propio blog post de Susan Fowler, *Reflecting On One Very, Very Strange Year
At Uber* (susanjfowler.com, 2017-02-19), leído directo.

- El manager la propuso sexualmente el primer día; RRHH la disuadió de escalar: «this was
  clearly sexual harassment and he was propositioning me, it was this man's first offense» y lo
  justificaron porque «he "was a high performer" (i.e. had stellar performance reviews from his
  superiors)».
- Un manager distinto le cambió la evaluación de desempeño después de calibrada, para bloquear
  su traslado a otro equipo: «my performance review and score had been changed after the
  official reviews had been calibrated», con la razón dada: «I didn't show any signs of an
  upward career trajectory».
- **La cita ancla, sobre el mecanismo de "cuestionar = amenaza":** cuando reportó la amenaza de
  represalia de un manager, la respuesta que recibió fue: «California is an at-will employment
  state, he said, which means we can fire you if you ever do this again» — y de RRHH: «they both
  admitted that this was illegal, but none of them did anything».
- Consecuencia verificable: el post detonó la salida de Travis Kalanick como CEO y la
  investigación externa liderada por Eric Holder.

### 3. WeWork — Adam Neumann (2019-2021) — ✅ VERIFICADO en fuente primaria (2026-08-07)

**Ángulo primario: extraer lealtad sin retribución.**

Fuentes primarias: comunicados oficiales de **group.softbank** (SoftBank Group Corp.), leídos
directo — no reportería de terceros para las cifras centrales.

- **Noviembre 2019:** WeWork despide **2.400 empleados** (~19% de la plantilla). El paquete de
  salida reportado: tres meses de "garden leave" con beneficios completos + un mes de
  indemnización, condicionado a firmar renuncia al derecho a demandar y una cláusula de
  no-competencia de 6 a 12 meses.
- **Octubre 2019, Master Transaction Agreement (fuente primaria SoftBank):** SoftBank confirma
  en comunicado oficial un **fee de asesoría de USD 185 millones** a Neumann y una **línea de
  crédito de USD 500 millones** para que pagara sus préstamos — ambas cifras confirmadas
  directamente en el sitio de prensa de SoftBank, no solo en reportería.
- El titular de "~USD 1.700 millones" en total (sumando la recompra de acciones ~970M) es la
  cifra ampliamente reportada en prensa (CNBC, NYT) para el paquete de 2019 completo; **no
  verifiqué un desglose oficial de los 970M en la fuente primaria** — queda [VERIFICAR] antes de
  citarlo como cifra exacta al aire.
- **Marzo 2021, comunicado oficial de SoftBank (settlement):** tras un litigio porque SoftBank
  intentó cancelar la compra de acciones en 2020, el acuerdo final confirmado en fuente primaria
  fue de **"approximately USD 1.6 billion"** — un número distinto y posterior al de 2019, y
  ambos son reales pero corresponden a momentos distintos de la misma historia. Al aire, contar
  la secuencia (oferta 2019 → SoftBank intenta cancelar 2020 → settlement 2021 ~1.6B), no fundir
  las dos cifras en una sola.
- **Encuesta interna:** 85% de empleados encuestados consideró injusto el paquete de salida de
  Neumann frente al severance de los despedidos (fuente secundaria — sin verificar la encuesta
  original).

## Estado del guion — actualizado 2026-08-07

- [x] ~~Título del episodio~~ — fijado: `Ponerse la camiseta: la explotación laboral disfrazada
      de slogan` (64 car., ancla de 9 palabras).
- [x] ~~Aterrizajes obligatorios~~ — escritos, uno por caso, dentro del segmento 6 (qué hace
      usted el lunes).
- [x] ~~Duración objetivo~~ — guion completo, **5.239 palabras habladas, medidas
      programáticamente, 40:00 a 148wpm+13%.** No repitió el error del intento anterior de este
      cupo (tabla de tiempos fabricada sin correr el conteo) — esta vez el orden fue texto
      primero, conteo real después, tabla rellenada al final con los números medidos.
- [ ] Verificar "Eight is Great" en una fuente más primaria que reportería (testimonio ante el
      Senado de Stumpf, sept. 2016, sería la candidata) o usarlo sin atribución textual directa
      — el guion ya lo trata así, pendiente solo si se quiere citarlo como frase textual.
- [ ] Verificar el desglose de los ~USD 970M en acciones del paquete Neumann 2019 en fuente
      primaria — el guion ya evita esa cifra, usa solo las confirmadas (185M + 500M + 1.6B).
- [ ] Correr `python scripts/lint_guion_repeticion.py` y grep de español neutro antes de aprobar.
- [ ] Confirmar teaser de EP.024 hacia este episodio (no se abrió el cierre de EP.024 en esta
      sesión) y el teaser hacia **EP.026** (vacante, no Peter/Little — ese quedó en EP.027 tras
      el swap) para el cierre de este episodio. El guion todavía dice "Teaser EP.027" en la caja
      pendiente del segmento 7 — corregir antes de grabar.
