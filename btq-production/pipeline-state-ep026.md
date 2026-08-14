EPISODE: EP.026 (BTQ) — «Llevo cuatro meses sin llenar esa vacante»: por qué el perfil que pidió no existe por ese salario

stage_a: **grabado 2026-08-13**, transcripción en curso. Tema fijado 2026-08-01 (idea de Andy,
de foros de LinkedIn), casos investigados y verificados en fuente primaria el 2026-08-13. Guion
completo en `launch-assets/EP026-vacante-guion.artifact.html` — 5.331 palabras escritas, 40:43
medidos programáticamente (148 wpm +13%, esqueleto D sin precedente medido). Lints corridos y en
PASS: `lint_guion_repeticion.py` (2 hallazgos corregidos, PASS final), grep de español neutro y
de cifras en letras (limpio).

**Grabación confirmada por Andy 2026-08-13** en `E:\Podcast\BTQ\EP26\` (`BTQ EP 26.wav` /
`.mp3` / `.rpp`). **Duración real medida con ffprobe (wav y mp3 coinciden): 2205,27 s = 36:45.**
Esto es **~4 minutos por debajo del piso del estándar editorial de 40-45 min** (el guion escrito
estimaba 40:43). No se preguntó ni se asumió la causa — pendiente de comparar contra la
transcripción real (en curso) para ver qué se cortó o si Andy simplemente habló más rápido que
el ritmo calibrado de 148 wpm. **Confirmado por Andy 2026-08-13: se grabó tal cual estaba escrito.** Ninguno de los dos
pendientes se ejecutó como paso separado antes de grabar:
- **Re-verificación de fuentes justo antes del micrófono** — no se hizo como segunda pasada.
  Mitiga el riesgo: las fuentes primarias ya se habían abierto y verificado directamente durante
  la escritura (no de memoria ni de reportería sola) el mismo día. El caso 3 (UK) sigue con la
  advertencia de fuente débil (Wikipedia, no gobierno primario) — eso no cambió.
- **Visto bueno explícito sobre nombrar a Irina Lara** — no se dio como decisión aparte, pero
  Andy grabó leyendo el guion completo (incluida esa sección) y no la cortó ni la cambió. Se
  interpreta como aprobación por acción, no como pendiente abierto. Si al revisar la
  transcripción o al armar los assets públicos Andy quiere suavizarla o quitarla, todavía se
  puede editar el audio o ajustar solo lo escrito (Spotify, artículo, redes) antes de publicar.
stage_b: no iniciado. **Transcripción lista** —
`E:\Transcriptor\transcripciones\BTQ EP 26.srt` (WhisperX large-v2 + diarización, 2026-08-14).

## Por qué salió 36:45 en vez de los 40:43 escritos — explicado, no es contenido cortado

**Corrección 2026-08-14, misma sesión:** el mensaje que le mandé a Andy diciendo "nada se
saltó" fue una primera lectura demasiado rápida del transcript — no era falso a propósito, pero
tampoco estaba verificado con grep. Al cruzar cada bloque `.dato` del guion contra el SRT con
grep (no a ojo), aparecieron **3 bloques de dato completos que Andy NO leyó al aire**, aunque sí
leyó los casos y el resto de los datos alrededor. Corregido abajo — ver § Hallazgos.

La causa del gap de tiempo en sí sigue siendo de calibración, no de este contenido saltado (el
gap era ~4 min y el contenido saltado son ~3 frases cortas, no alcanza a explicar los 4 min por
sí solo):

- **Palabras realmente habladas (contadas sobre el SRT): 5.512**, contra 5.331 escritas. Eso es
  una expansión real de solo **+3,4%**, no el +13% que se usó para dimensionar el guion (la
  regla de `guion-style-btq.md` dice usar +13% para "esqueleto nuevo sin precedente medido" —
  en este caso fue optimista).
- **Ritmo real: ~150 wpm** (5.512 palabras / 36,75 min) — está prácticamente en el número
  calibrado (148 wpm), así que el problema NO es que Andy hablara más rápido de lo esperado.
- **Conclusión:** para el esqueleto D (trenzado), el factor de expansión real medido es
  **+3,4%, no +13%**. Aplicado a la fórmula: 5.331 escritas × 1,034 / 148 = 37,3 min esperados
  — más cerca de los 36:45 reales que la estimación original de 40:43. **Pendiente:** anotar
  este dato en `guion-style-btq.md` § Calibración de duración la próxima vez que se toque esa
  sección (regla propia del documento: "recalibrar cada pocos episodios contra el SRT más
  reciente").

## Hallazgos reales al comparar transcripción vs. guion (no inventados, verificados en el SRT)

0. **⚠️⚠️ 3 bloques `.dato` completos NO se leyeron al aire — verificado con grep sobre el SRT,
   no a ojo.** Los casos y remates alrededor de cada uno sí se leyeron completos; lo que falta
   es exactamente el recuadro de cifras:
   - **Segmento 1 — ManpowerGroup Colombia (el dato duro "del mundo del oyente", ADN 3).** Andy
     dice "hay un dato bastante interesante que realizó Manpower Colombia... sobre escasez de
     talento" pero **nunca dice el 66%, ni el desglose por sector (TI 75%, energía 71%, etc.)**.
     El argumento retórico de después ("escasez, ¿a qué precio?") sigue funcionando sin el
     número, pero el episodio se queda sin la cifra que lo ancla — este era, en el guion, el
     dato duro exigido por el ADN de la sección, y tal como quedó grabado, no se dijo.
   - **Segmento 3 — riesgo financiero de hospitales rurales (37,3% en 2024 vs. 16,8% en 2022).**
     No se mencionan estos dos números en ningún punto del segmento.
   - **Segmento 4 — pérdida de conductores UK (12.500 conductores europeos perdidos antes de la
     pandemia, 25.000 exámenes de conducción menos 2019-2020).** Salta directo de "70.000
     conductores" a "manejar un camión... no es un oficio de baja exigencia", sin esas dos
     cifras intermedias.
   **Para los assets públicos (show notes, Spotify, artículo):** no citar estos 3 números como
   "dicho en el episodio" — si se usan, aclarar que son contexto adicional del guion/investigación,
   no algo que el oyente escuchó.
1. ~~El disclaimer de conflicto de interés salió incompleto~~ — **RESUELTO 2026-08-14, no era
   un problema real.** Se había marcado como hallazgo porque el guion decía "HireSignal y Kuma
   Talent" y la grabación solo nombró Kuma Talent. Andy aclaró: **HireSignal no es una empresa
   aparte, es un producto de Kuma Talent** (consistente con `reference_kuma_infra.md` en
   memoria, que ya tenía `app.kumatalent.com=HireSignal` — no se cruzó contra esa memoria antes
   de reportar el "hallazgo"). Nombrar solo Kuma Talent en la grabación fue una declaración
   completa, no parcial. Queda "Hugo Lancheros" como socio mencionado que no estaba en el
   guion — sin importancia para el disclaimer, mencionado aquí solo por completitud del registro
   transcripción-vs-guion.
2. **"Imagínense" se usó 12 veces**, contra el presupuesto de la guía de estilo (máx. 1). Es
   ad-lib de Andy, no estaba en el guion escrito (ahí quedó en 0). No es corregible ya grabado;
   se anota como patrón a vigilar en la próxima sesión de escritura o como feedback de entrega
   si Andy quiere ajustar en vivo.
3. **"Su merced" se usó 2 veces** (min. ~17:59 y ~27:38) — no estaba en el guion. Es un
   colombianismo más marcado que los ya catalogados en `guion-style-btq.md` § Español neutro
   (más cercano al registro rural cundiboyacense que a "plata" o "chévere"); no pasaría la
   prueba de "¿lo entiende alguien en México sin que se lo expliquen?". Candidato a agregar a la
   lista de palabras ancladas a país si vuelve a aparecer.
4. **Transcripción, no errores al aire** (patrón ya documentado en `guion-style-btq.md` — cotejar
   contra el guion antes de reportar): "Agdecta"/"Adecta" por ACDECTA, "Bichada" por Vichada,
   "Buck" por Bock, "HGB" por HGV, "Behind the Cue" por Behind the Queue, "la mina aerocivil"
   probablemente por "la misma Aerocivil". El guion tiene todos estos términos bien escritos —
   es WhisperX confundiendo nombres propios, no un error de Andy.

**Corrección de ruta de artwork, misma sesión (Andy la cazó):** las portadas y quote cards se
generaron primero en `E:\AI\outputs\BTQ-EP026\` (carpeta de assets de MARCA). La regla fijada
2026-07-31 en `brand-constants.md` manda que van en `E:\Podcast\BTQ\EP NN\BTQ Artwork EP NN\`,
junto al audio. Copiado a `E:\Podcast\BTQ\EP26\BTQ Artwork EP26\` y el gate mecánico se re-corrió
ahí — PASS. Ver `EP026-vacante-launch.md` § D para el detalle completo, incluida la nota de que
EP.023 y EP.025 tienen el mismo problema sin corregir.

stage_c: no iniciado.
spotify_url: https://open.spotify.com/episode/683PSkr20tY9Jy57M8vPBa?si=ULDQW49kSyqC5ZfXZ3S_Fw
(confirmada por Andy 2026-08-14). **Fecha de publicación: domingo 16 de agosto de 2026, 8:00 PM
Colombia** (confirmada por Andy 2026-08-14). Ambas propagadas a artículo/social/YouTube — falta
solo desplegar (`website/episodios/index.html` + sitemap + `vercel --prod`).

**Carril:** Oficio de Jefe #3. **Esqueleto:** D (trenzado) — los dos casos colombianos
(controladores aéreos + médicos rurales) trenzados en los segmentos 2-3, Reino Unido como giro
al ~58% que amplía la tesis fuera del sector público. A quedó descartado por uso consecutivo en
EP.025.

## Título y ángulo

**Título:** `Por qué no llena esa vacante hace cuatro meses: el candidato unicornio` (70
caracteres · ancla de 9 palabras — al tope del techo fijado 2026-08-03).

**Las dos banderas del roadmap, resueltas al escribir:**
- **Evergreen:** el episodio no ancla en "ahora más que nunca los reclutadores ghostean". El eje
  es el mecanismo de precio/perfil (pedir sin invertir en producir), con la pandemia y el Brexit
  como ejemplo dentro de un caso (Reino Unido), no como tesis del episodio.
- **Conflicto de interés (HireSignal/Kuma Talent):** declarado explícito en el Segmento 0, en un
  bloque aparte del disclaimer de encuadre, antes del ritual "Buenas y santas". No se disimula,
  por instrucción del roadmap.

## Dato duro del mundo del oyente

ManpowerGroup Colombia, Estudio de Escasez de Talento 2024 (vía Semana, cita a Lina Correa,
directora de Talent Solutions): 66% de escasez reportada por empleadores en 2024 (+2 puntos vs.
2023). Por sector: TI 75%, energía y servicios públicos 71%, comunicaciones 68%, salud 64%. El
guion incluye una lectura crítica del propio dato: es una encuesta a empleadores, con incentivo
a no admitir que el precio ofrecido es el problema.

## Casos — estado de verificación

### 1. Colombia — controladores aéreos (2023) + seguimiento Aerocivil/Procuraduría (2026) — ✅ VERIFICADO en fuente primaria abierta esta sesión

**Ángulo primario:** el Estado pidió el perfil más exigente de aviación civil y congeló la
formación 5 años.

Fuente: Infobae, 22-23 de noviembre de 2023 (leída completa vía WebFetch). Déficit según
ACDECTA: 400 controladores; según Aerocivil: 48. Colombia opera con 704 controladores activos.
Cita directa de Irina Lara, presidenta de ACDECTA: «Desde este año le estamos diciendo al
Gobierno que necesitamos 1.200 controladores.» Causa: 5 años sin abrir cursos de formación.
Consecuencia documentada: Avianca canceló 66 vuelos y retrasó 400 en una sola jornada; 9.400
pasajeros afectados. Meta de Aerocivil de 10 millones de pasajeros a 2030, en riesgo según
ACDECTA.

**Seguimiento 2026 — usado en el guion, con cuidado explícito por ser denuncias en investigación:**
Infobae, 16 de mayo de 2026 (leída completa vía WebFetch) — investigación de la Procuraduría
sobre Aerocivil. Estudio interno de 2018 recomendaba 799 controladores; en 2025 la planta seguía
en 715 (84 vacantes), mientras el tráfico de El Dorado pasó de 30 a más de 50 millones de
pasajeros anuales (2018-2025). Decreto 0315 (marzo 2026): bono de 154% para controladores en
Bogotá; un controlador grado 21 llega a ~20 millones COP/mes con bonos. Documentos internos
señalan pagos a controladores que no cumplieron su carga operativa (acuerdos sindicales por
antigüedad) y al menos 70 controladores con vínculos familiares directos en cargos clave
(apellidos citados: Córdoba, Araújo, Díaz, Torres). El artículo nombra el caso de **Irina Lara**
—la misma fuente citada en 2023— con salario cercano a 18 millones/mes, sin certificación
médica vigente, y solo 30 de las 1.200 horas anuales de vuelo requeridas.

**⚠️ Decisión editorial que necesita el sí explícito de Andy antes de grabar:** el guion nombra a
Irina Lara en las dos mitades del caso — como voz de alarma en 2023 y como sujeto de denuncia en
2026 — enmarcado explícitamente como "denuncias bajo investigación de la Procuraduría, no hechos
probados". Es información real y publicada, pero nombrar a una persona identificable en medio de
una investigación en curso es una decisión de peso editorial, no solo de verificación de fuente.
Si Andy prefiere no nombrarla o suavizar esa parte, el resto del caso (déficit, bonos, nepotismo
sin nombre propio) sostiene el argumento igual.

### 2. Colombia — médicos rurales — ✅ VERIFICADO en fuente primaria abierta esta sesión

**Ángulo primario:** trenzado con el caso 1 — mismo mecanismo (Estado pide perfil exigente, no
invierte en producirlo), techo más alto (vidas, no vuelos).

Fuente: Índice de Salud Rural 2024, Centro de Pensamiento Así Vamos en Salud, publicado el 17 de
febrero de 2025 (vía Infobae, leída completa vía WebFetch — el sitio propio de Así Vamos en
Salud dio error de certificado y no se pudo abrir directo). Solo 3 municipios con +100
médicos/10.000 hab. (Santafé de Antioquia, Abejorral, Córdoba-Bolívar). 116 municipios con 1
solo médico, concentrados en Cundinamarca, Santander y Norte de Santander. 37,3% de ESE rurales
en riesgo financiero en 2024 (vs. 16,8% en 2022). Cobertura de control prenatal: Vaupés 26,4%,
Guainía 34,3%, Vichada 37,6%. En 60 municipios, <1% de mujeres accede a mamografía (171 sin
dato). Papunaua (Vaupés): cobertura de depresión ~4% (la más alta del país) y la tasa de
suicidio más alta de Colombia. Infraestructura: 41,1% con alcantarillado, 39% de municipios con
agua potable <50%, 37,4% con internet <1% (de 520 municipios analizados).

### 3. Reino Unido — crisis de combustible 2021 (déficit de conductores HGV) — ✅ VERIFICADO, con una fuente débil marcada

**Ángulo primario:** giro — el mismo mecanismo sin Estado de por medio, resuelto (mal) por el
mercado libre.

Fuente: Wikipedia, artículo "2021 United Kingdom fuel supply crisis" (leído completo vía
WebFetch), con cifras que el propio artículo cruza contra BBC y Reuters. Déficit de 70.000
conductores HGV. Pérdida de 12.500 conductores europeos pre-pandemia. 25.000 exámenes de
conducción menos aprobados 2019-2020 (cierre de centros por COVID). Pánico de compra a fines de
septiembre 2021: 50-90% de gasolineras secas en algunas regiones (27 sept.), 22% en Londres/
sureste sin combustible (3 oct.). Respuesta del Gobierno: ejército en alerta, flota de reserva
de 80 vehículos, 300 conductores extranjeros autorizados de emergencia, exención parcial de la
ley de competencia.

**[VERIFICAR SI HAY TIEMPO]** Wikipedia es agregador, no fuente primaria — no se abrió un
informe del gobierno británico (DfT/ONS) directamente en esta sesión. Las cifras cruzan contra
BBC/Reuters dentro del propio artículo, lo que da confianza razonable, pero no es el estándar
de "fuente primaria abierta" que sí se cumplió en los dos casos colombianos.

## Recomendaciones tejidas (3, medios mixtos, verificadas)

1. Peter Cappelli (2012), *Why Good People Can't Get Jobs: The Skills Gap and What Companies Can
   Do About It*, Wharton Digital Press — libro. Verificado vía múltiples reseñas/Wharton
   Executive Education, no leído completo (es un libro, no un artículo corto).
2. Laszlo Bock (2015), *Work Rules!*, Twelve — libro/dato. Dato de Google (correlación cero
   entrevista-desempeño, GPA sin predictividad tras 2 años, 14% del equipo sin título
   universitario) verificado vía múltiples fuentes de prensa y del propio Bock citado en Wikipedia.
3. Regina Hartley, TED Talk *Why the Best Hire Might Not Have the Perfect Resume* — charla.
   Verificada como charla real de TED; el contenido específico atribuido en el guion (preferir
   candidatos con adversidad real) es la tesis conocida de la charla, no una cita textual.

## Referencias cruzadas (fuera de los 3 casos)

- "Purple squirrel" — jerga de reclutamiento en EE. UU., termino documentado (Wikipedia), sin
  origen único verificable ni fecha exacta — usado como término genérico, no como caso con
  consecuencias.
- Caso ilustrativo: Sebastián Ramírez / FastAPI (2020) — oferta real que pedía "más de 4 años de
  experiencia" en un framework de 18 meses de existencia. Verificado vía múltiples fuentes de
  prensa tech, consistente entre sí.
- Training Within Industry (TWI) / War Manpower Commission, Departamento de Guerra de EE. UU.,
  1940-1945 — verificado vía Wikipedia + fuentes .gov citadas en la búsqueda (NPS, BLS). Déficit
  estimado de casi 7 millones de trabajadores para 1942.

## Dichos torcidos (3 de 5 disponibles)

1. "El que mucho abarca, poco aprieta" (segmento 1, extendido).
2. "Cuentas claras conservan amistades" → "cuentas claras conservan candidatos" (segmento 3,
   invertido).
3. "Más vale pájaro en mano que ciento volando" (segmento 4, extendido).

Ninguno repetido contra `launch-assets/*.html` (verificado por lectura, no solo grep — los
dichos de EP.024 y EP.025 ya catalogados en sus propios pipeline-state no se repiten aquí).

## Compuerta de aplicabilidad — medida, no cumple el número exacto

Segmento 6 ("Qué hace usted el lunes"): 1.133 palabras = **21,2%** del total (regla:
≥25%). Arranca en el minuto 30:26 de 40:43 = **74,8%** del episodio (regla: antes del 60%).

Se reforzó el segmento 6 en varias rondas de edición con contenido real atado a los 3 casos
(no relleno genérico) antes de aceptar el número final. **Dato de contexto, no excusa:** el
mismo cálculo aplicado a la arquitectura publicada de `EP025-camiseta-guion.artifact.html`
(segmento 6 en 34:16 de 40:00) da un arranque todavía más tardío — 85,6%. La compuerta no se
está cumpliendo en la práctica reciente del show; esto no es un problema aislado de este guion.
Queda para que Andy decida si vale la pena reestructurar EP.026 antes de grabar, o si la regla
de `guion-style-btq.md` § ADN 3b necesita recalibrarse contra lo que el formato real permite.

## Pendientes antes de grabar

- [ ] Re-verificar TODAS las fuentes justo antes del micrófono (regla de Andy 2026-07-31) — este
      guion se escribió y verificó en una sola sesión el 2026-08-13, no ha pasado por una
      segunda sesión de re-chequeo.
- [ ] Visto bueno explícito de Andy sobre nombrar a Irina Lara en el caso Aerocivil/Procuraduría
      (denuncias en investigación, no hechos probados — ver arriba).
- [ ] Si hay tiempo: buscar una fuente primaria de gobierno UK (DfT/ONS) para el caso 3, en vez
      de depender de Wikipedia como agregador.
- [ ] Decidir si se reestructura el segmento 6 por la compuerta de aplicabilidad, o se acepta
      como está (ver nota arriba).
- [ ] Confirmar teaser hacia EP.027 — está escrito deliberadamente evergreen porque ese episodio
      sigue "GUION A REDISEÑAR" en `roadmap-btq.md`; si para cuando se grabe EP.026 ya hay más
      claridad sobre EP.027, se puede hacer el teaser más específico.
