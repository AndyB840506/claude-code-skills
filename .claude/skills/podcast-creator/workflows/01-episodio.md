# Workflow 01 — Guion Completo del Episodio

Genera un script completo, palabra por palabra, para un episodio específico. Se adapta al formato del podcast (solo, entrevista, co-host, silla_putrida).

**Regla fundamental: Lee `podcast-profile.json` primero. Si no existe, lanza `00-setup.md` antes de continuar.**
**Regla de lenguaje: Consulta `glosario-cachaco.md` antes de escribir cualquier guión (contiene guía de tono actualizada — español colombiano casual).**
**Regla de eventos: Consulta `eventos.json` para el Segmento de Promoción.**
**Regla de rotación de género: Revisar el género del episodio anterior antes de proponer el tema. No repetir el mismo género back-to-back. Si el EP anterior fue metal → el siguiente no puede ser metal. Géneros contiguos válidos: rock clásico, blues, jazz, soul, reggae, punk, alternativo, electrónico, folclore, salsa/afro-latino, etc.**
**Regla del conector de género (EP.003 en adelante): Durante la investigación del episodio, identificar un dato real dentro del material — un artista, una influencia, un cruce histórico — que conecte orgánicamente con el género del siguiente episodio. Ese dato se convierte en el puente del cierre: el host lo nombra como anticipo del próximo capítulo. El conector NO se inventa — se descubre en la investigación. Si no existe un conector natural, revisar el orden del roadmap antes de forzarlo. Ejemplo: EP.002 (metal) → Iommi se inspiró en Django Reinhardt (jazz) → ese dato es el puente hacia un episodio de jazz. EP.003 (rock roots) → el árbol africano tiene dos ramas, una fue al Caribe → ese dato es el puente hacia EP.004 (salsa).**
**Regla de investigación y verificación (OBLIGATORIA, antes de escribir): investigar el tema en la web y reunir datos verificables (fechas, cifras, anécdotas reales, evolución del sonido, álbumes emblemáticos Y los menos conocidos, canciones). NUNCA inventar fuentes, fechas, productores ni quotes — marcar lo no confirmado como `[VERIFICAR]` para chequear antes de grabar. Igualar la profundidad de los episodios fuertes (Black Sabbath / Kraken): dato duro + escena de la época + anécdota cierta poco conocida. Lección EP.005 (Aterciopelados): el primer borrador acreditó mal al productor de "El Dorado" (era Federico López, no Manzanera) — el error solo salió al investigar.**
**Regla de 2 partes (default para episodios con investigación profunda): si la data con chispa pasa de ~60 min, estructurar el guion en 2 partes DESDE EL INICIO — corte natural, cada parte con su apertura/cierre corto, recap de ~20 seg al abrir la Parte 2. Metadata compartida; solo cambia el título "(Parte 1)"/"(Parte 2)". Ver memoria `project-mpd-episodes-two-parts`.**

> **⚠️ Alcance de este workflow — qué es genérico y qué es específico de MPD/BTQ:**
> Este archivo se usa para cualquier show creado con `podcast-creator`, pero acumuló
> reglas específicas de Mr. Putrid's Den y BTQ que NO aplican a un show nuevo salvo que
> comparta ese perfil. Específicamente son **solo MPD/BTQ** (sáltalos para otros shows,
> a menos que el `podcast-profile.json` del show diga lo contrario):
> - Todo Paso -1 y Paso 0-SP (Silla Pútrida — formato de invitado de MPD)
> - Las reglas de lenguaje/`glosario-cachaco.md`, rotación de género, y conector de
>   género de arriba (específicas del formato musical de MPD)
> - El tratamiento "usted/ustedes, nunca tú" y las palabras prohibidas del Paso 3
>   (español colombiano — no aplica a shows en otro idioma)
> - Las tablas de segmentos "co-host" y el Segmento de Promoción (Andrés/Juan de MPD)
>
> Lo genérico y aplicable a cualquier show: Paso 0 (cargar perfil), Paso 0.5 (formato
> del episodio), Paso 1 (datos del episodio), Paso 1.5 (cuestionario si es interview),
> Paso 2 (arquitectura + word count), la disciplina de investigación/verificación de
> arriba (aplica a cualquier género, no solo música), y el formato de entrega del Paso 3.

---

## Paso -1 — ¿Hay Silla Pútrida esta semana? [MPD-específico — ver nota de alcance arriba]

**SIEMPRE pregunta esto antes de cualquier otra cosa:**

> ¿Esta semana hay Silla Pútrida? (¿Tienen invitado especial en el show?)

- **SÍ** → `formato_episodio = "silla_putrida"`. Ir a **Paso 0-SP** antes de continuar.
- **NO** → `formato_episodio = "co-host"`. Continuar con **Paso 0** normalmente.

---

## Paso 0-SP — Flujo especial Silla Pútrida (solo si hay invitado)

### A. Recopilar datos básicos

Pregunta:

> **¿Quién viene a La Silla Pútrida?**
> 1. Nombre del invitado
> 2. ¿Qué hace? (músico, promotor, luthier, dueño de bar, productor, otro)
> 3. ¿Tienen algún link, red social o referencia donde pueda investigarlo?
> 4. Número del episodio

### B. Modo Narval — Investigar al invitado

Con el nombre y perfil, **investiga al invitado en la web** antes de generar nada:
- Busca su trabajo, proyectos, trayectoria
- Encuentra 3-5 datos curiosos o poco conocidos
- Identifica momentos clave de su carrera
- Busca entrevistas previas para no repetir preguntas ya hechas

Con esa investigación, genera el **documento de prep para hosts** usando `mrputridsden-production/templates/silla-putrida-prep-hosts.md`:
- Bio real investigada (no la que el invitado escribe — la que encontraste)
- Los datos curiosos
- 5-7 preguntas únicas basadas en su trayectoria real
- Selecciona el set de preguntas base del perfil correspondiente en `mrputridsden-production/templates/preguntas-por-perfil.md`

Presenta el documento de prep al usuario y di:
> "Acá está la investigación del invitado. Revise si falta algo antes de enviarle la carta."

### C. Generar carta al invitado

Usando `mrputridsden-production/templates/silla-putrida-invitacion.md`, genera la carta personalizada con:
- Referencia específica al trabajo del invitado (de lo investigado)
- Los 3 temas propuestos para la conversación

Genera también el documento de prep corto para el invitado usando `mrputridsden-production/templates/silla-putrida-cuestionario.md` — solo pide bio libre, confirmación de temas y NO-list.

Di al usuario:
> "Acá está la carta de invitación y el doc de preparación para enviarle al invitado. Cuando confirme y devuelva su NO-list, regrese y generamos el guión."

### D. Guardar ficha del invitado

Crea `mrputridsden-production/fichas-invitados/[nombre-invitado].md` con:
```
# Ficha: [Nombre del invitado]
Episodio: EP.[NNN]
Fecha: [fecha]
Perfil: [artista / promotor / luthier / venue / productor]
Bio investigada: [resumen]
Datos curiosos: [lista]
Temas cubiertos: [lista — llenar después de grabar]
NO-list: [lo que pidió que no se toque]
Redes: [links]
```

### E. Generar guión (solo después de confirmación del invitado)

**No generar el guión hasta que el usuario confirme que el invitado respondió.**

Cuando el usuario diga que el invitado confirmó:
- Integrar la NO-list del invitado
- Usar las preguntas investigadas + las aprobadas por el invitado
- Recordar: grabación **presencial** — los 3 en el mismo cuarto, ambos hosts pueden preguntar
- Marcar los intercambios como `[ANDRÉS/JUAN — cualquiera de los dos puede preguntar esto]`

---

## Paso 0 — Cargar identidad del podcast

Lee `podcast-profile.json`. Extrae y ten disponible:
- Nombre del podcast, host(s), formato
- Tono y reglas de escritura (`reglas_tono`)
- Intro y outro templates
- Convención de numeración
- Duración promedio (`duracion_min`)
- Estilo de narración y word count target (`estilo_narración`, `word_count_target`)

**Si existe un archivo `guion-style-[show].md` en la carpeta de producción del show**
(ej. `btq-production/guion-style-btq.md`, `corporate-crime-confidential-production/guion-style-ccc.md`),
consúltalo antes de escribir — ahí vive el wpm real medido del show (no adivinado) y
cualquier regla de atribución/formato específica de ese show (ej. la distinción cita-real
vs narración-dramatizada de CCC). Si no existe todavía y este es el episodio piloto, no
hay wpm medido aún — usar el estimado del perfil y crear el archivo de calibración
después de la primera grabación real (ver Paso 4).

Calcula el word count target para este episodio basado en la duración que el usuario confirme en Paso 1.

---

## Paso 0.5 — Detectar formato de ESTE episodio (nuevo)

El perfil del podcast tiene un formato default, pero cada episodio puede ser diferente.

Pregunta:

> El perfil de tu podcast es **[formato del perfil]**, pero cada episodio puede variar.
> ¿Cómo es **este episodio específico**?
> 1. **Solo** — solo tú hablas
> 2. **Con co-host** — [mostrar nombres de co-hosts del perfil si existen]
> 3. **Entrevista** — tienes un invitado especial

Espera la respuesta. Guarda `formato_episodio: "solo" | "interview" | "co-host"` como override del formato del perfil para este episodio solamente.

---

## Paso 1 — Datos del episodio

Pregunta en un solo mensaje adaptado al formato del perfil:

> **Para este episodio:**
> 1. ¿Cuál es el número de episodio? (ej: 001, 014...)
> 2. ¿Cuál es el tema o título tentativo?
> 3. ¿Cuál es el ángulo único — qué perspectiva o enfoque vas a tomar que no hace todo el mundo?
> 4. ¿Hay alguna referencia cultural, historia, persona o evento que sirva como hilo conductor?
> 5. ¿Cuál es el takeaway principal — qué debe llevarse el oyente al terminar?

**Si formato = `interview`**, agrega al mismo mensaje:
> 6. Nombre del invitado y cargo o descripción en una línea
> 7. ¿De qué 3 temas quieres hablar con el invitado?
> 8. ¿Hay algún tema tabú o pregunta que NO debes hacer?

**Si formato = `co-host`**, agrega:
> 6. ¿Quién abre el episodio hoy?
> 7. ¿Hay dinámicas especiales entre los hosts para este episodio?

---

## Paso 1.5 — Generar cuestionario de entrevista y briefing (si es interview)

**Solo si `formato_episodio = "interview"`:**

### A. Cuestionario de entrevista (10-15 preguntas escaladas)

Genera un documento con estructura clara:

```
CUESTIONARIO DE ENTREVISTA — EP.[NNN]
═════════════════════════════════════════════════════════
  Invitado: [nombre]
  Tema principal: [tema]
  Duración estimada: ~[X] minutos
═════════════════════════════════════════════════════════

BLOQUE DE BIENVENIDA (2-3 preguntas — fáciles, warm-up)
──────────────────────────────────────────────────────
1. ¿Quién eres y qué haces? [OBLIGATORIA]
2. ¿Cómo llegaste a esto? [OBLIGATORIA]
3. ¿Cómo te describes en 3 palabras? [OPCIONAL]

BLOQUE CENTRAL — TEMA PRINCIPAL (5-7 preguntas — escaladas)
──────────────────────────────────────────────────────
4. [Primera pregunta exploradora sobre tema 1]
5. [Pregunta de profundidad sobre tema 1 — "¿por qué crees que...?"]
6. [Pregun­ta sobre tema 2 — cambio de enfoque]
7. [Pregunta provocadora — desafiar creencia o perspectiva]
8. [Pregunta sobre tema 3 — síntesis]
[notas de escucha activa: si el invitado menciona X, profundizar con "¿y cómo afectó eso...?"]

BLOQUE DE CIERRE (2-3 preguntas)
──────────────────────────────────────────────────────
N-2. ¿Qué consejo le darías a alguien que está empezando en...? [OBLIGATORIA]
N-1. ¿Cuál es tu visión para el futuro de...? [OBLIGATORIA]
N. ¿Dónde nos pueden encontrar tus oyentes? [redes, web, email] [OBLIGATORIA]

PREGUNTAS DE RESERVA (si queda tiempo o necesitas reemplazar respuestas cortas)
──────────────────────────────────────────────────────
R1. [Pregunta alternativa profunda]
R2. [Pregunta sobre dato sorprendente que el invitado mencionó]
```

Marca explícitamente qué preguntas son OBLIGATORIAS vs OPCIONALES. Esto permite al host adaptar según el ritmo de la conversación.

### B. Documento de briefing para el invitado

Genera un documento listo para enviar al invitado 3-5 días antes de la grabación:

```
──────────────────────────────────────────
  INVITACIÓN A [NOMBRE PODCAST]
──────────────────────────────────────────
  Episodio:  EP.[NNN] — [Título del episodio]
  Host:      [nombre del host]
  Duración:  ~[X] minutos
  Fecha:     [fecha tentativa si la hay]
──────────────────────────────────────────

DE QUÉ VAMOS A HABLAR

[Descripción de 3-4 párrafos del episodio y los 3 temas principales]

SOBRE [NOMBRE PODCAST]

[Nombre] — [tagline]. 
Audiencia: [descripción del oyente ideal].
Escúchalo en: [links de plataformas del perfil]

REQUISITOS TÉCNICOS

✓ Micrófono USB o auriculares con micrófono (NO bocinas)
✓ Cuarto silencioso, puertas cerradas (apaga AC/calefacción si es ruidosa)
✓ Auriculares puestos durante TODA la grabación
✓ Conexión a internet estable (wifi o cable, no datos móviles)
✓ Plataforma: [Riverside.fm / Zoom / la que uses]
✓ Link de sesión: [PENDIENTE — se enviará 24h antes]

TEMAS QUE CUBRIREMOS (en orden aproximado)

· [Tema 1] — contexto breve
· [Tema 2] — contexto breve
· [Tema 3] — contexto breve

NOTA IMPORTANTE

La grabación se usará para el podcast [Nombre Podcast]. Si hay algún tema que prefieras omitir o no abordar, avísame al menos 24h antes de la grabación.

──────────────────────────────────────────
```

Presenta ambos documentos al usuario antes de Paso 2, con la pregunta: "¿Revisas el cuestionario y el briefing antes de que empecemos con la arquitectura?"

---

## Paso 1.6 — Generar documento de sincronía pre-grabación (si es co-host)

**Solo si `formato_episodio = "co-host"`:**

Genera un documento breve para que los co-hosts se sincronicen antes de grabar:

```
SYNC PRE-GRABACIÓN — EP.[NNN]
─────────────────────────────────────────
  Tema del episodio: [tema]
  Ángulo: [ángulo único]
─────────────────────────────────────────

ASIGNACIÓN DE SEGMENTOS

· [Host1] abre con: [hook específico — primera frase que dice]
· [Host2] cubre: [segmento específico — ej: "Bloque principal A"]
· [Host1] cubre: [segmento específico — ej: "Bloque principal B"]
· Cierre a cargo de: [Host que cierra]

PUNTOS DE DEBATE PLANIFICADOS

· [Tema donde los hosts pueden tener opiniones diferentes — dejar espacio para intercambio natural]
· [Otro tema si aplica]

DINÁMICA ESPECIAL PARA ESTE EPISODIO

[Si hay algo único: un formato especial, un segmento donde intercambian mucho, un juego, etc.]

COSAS A EVITAR EN ESTE EPISODIO

[Si hay temas sensibles, errores de episodios anteriores, o cosas que no cuadran con el contenido, listarlas]

─────────────────────────────────────────
TIEMPO ESTIMADO DE HABLA POR HOST
  [Host1]: ~[X]% del episodio
  [Host2]: ~[X]% del episodio
─────────────────────────────────────────
```

Presenta el documento con la pregunta: "¿Revisas la asignación de segmentos? ¿Cambias algo antes de empezar?"

---

## Paso 2 — Presentar arquitectura para aprobación

**Antes de escribir el script**, calcula y muestra el word count target basado en:
- Duración del episodio confirmada en Paso 1
- Formato del episodio (`formato_episodio`)
- Estilo de narración (`estilo_narración`) del perfil

```
WORD COUNT TARGET PARA ESTE EPISODIO
════════════════════════════════════════
Duración: [X] minutos
Formato: [formato_episodio]
Estilo: [estilo_narración]
→ Word count target: ~[N] palabras

Esto es el tamaño esperado del script para evitar quedarse corto 
o demasiado largo.
════════════════════════════════════════
```

**Regla obligatoria, antes de escribir CUALQUIER guion (BTQ, CCC, MPD, o show nuevo) — condición →
acción → verificación:** cuando vaya a calcular el word count target, medir el wpm y el % de
expansión en vivo contra el SRT real más reciente de ESE show (`E:\Transcriptor\transcripciones\`),
NO asumir un número de una guía vieja ni reusar el de otro show. Verificar comparando el resultado
contra la duración real reportada de ese episodio (si el usuario la menciona) antes de aceptar la
cifra como correcta — esto nace de un caso real (BTQ EP.021, 2026-07-06) donde se asumió 143 wpm /
+15% de expansión de una guía desactualizada, y el SRT real de EP.020 mostró **150 wpm / +35.5%** —
casi el doble de expansión asumida. No repetir ese error en ningún show.

**Cómo calcular el word count target (NO adivinar minutos):** usa un **wpm MEDIDO** contra el
SRT real del show, no una suposición. El supuesto típico de ~100-110 wpm está muy por debajo de
la realidad: un host leyendo en voz alta corre mucho más rápido (BTQ/Andy solo host = **~150 wpm**
+ **~35.5% de expansión en vivo**, recalibrado 2026-07-06 contra el SRT de EP.20 — ver
`btq-production/guion-style-btq.md` → "Calibración de duración" para la cifra vigente de cada show,
nunca copiar la de otro). Fórmula: `palabras_escritas ≈ (minutos objetivo × wpm_medido) / (1 + expansión_medida)`.
Deja colchón para CORTAR, no para estirar.

**Verificar después de grabar:** comparar la duración real del SRT contra la marcada en el guion.
Si difieren, recalibrar el wpm Y el % de expansión del show con `palabras_habladas_del_SRT /
minutos_de_audio` (wpm) y `palabras_habladas_del_SRT / palabras_escritas_del_guion` (expansión), y
actualizar ambos números en la guía de estilo del show. Los SRT viven en `E:\Transcriptor\transcripciones\`.

**Después de mostrar el word count**, presenta la arquitectura adaptada a ESTE episodio y espera aprobación explícita.

Calcula los tiempos según `duracion_min` del perfil:

| Duración total | Bloques principales | Tiempo por bloque |
|---|---|---|
| 15 min | 1 bloque | 6-7 min |
| 30 min | 2 bloques | 5-7 min c/u |
| 45 min | 3 bloques | 6-8 min c/u |
| 60 min | 3-4 bloques | 8-10 min c/u |

**Estructura base según tipo de episodio:**

**Episodio normal (co-host):**

| # | Segmento | Duración | Contenido para ESTE episodio |
|---|----------|----------|------------------------------|
| 1 | Intro music | 30 seg | [música de apertura] |
| 2 | Bienvenida | 1-2 min | [Andrés y Juan abren el episodio] |
| 3 | Contexto del tema | 3-4 min | [por qué este tema ahora] |
| 4 | Bloque principal A | [X min] | [primer desarrollo] |
| 5 | [INTERCAMBIO] | — | diálogo libre entre hosts |
| 6 | Bloque principal B | [X min] | [segundo desarrollo / giro] |
| 7 | **Segmento de Promoción** | 3-5 min | [Juan presenta eventos de `eventos.json`] |
| 8 | Reflexión / Takeaway | 3-4 min | [conclusión accionable] |
| 9 | Outro + CTA | 1-2 min | [cierre + call to action] |
| 10 | Outro music | 30 seg | [música de cierre] |

**Episodio Silla Pútrida (con invitado):**

| # | Segmento | Duración | Contenido para ESTE episodio |
|---|----------|----------|------------------------------|
| 1 | Intro especial Silla Pútrida | 30 seg | [música + anuncio de invitado] |
| 2 | Bienvenida + presentación | 2-3 min | [Andrés presenta al invitado, Juan da contexto] |
| 3 | Bloque preguntas A | [X min] | [preguntas aprobadas — Bloque 1 y 2] |
| 4 | [INTERCAMBIO natural] | — | conversación fluye libre |
| 5 | Bloque preguntas B | [X min] | [preguntas aprobadas — Bloque 3] |
| 6 | Cierre con invitado | 2-3 min | [dónde encontrarlo, redes, proyectos] |
| 7 | **Segmento de Promoción** | 3-5 min | [Juan AL FINAL — eventos de `eventos.json`] |
| 8 | Outro + CTA | 1-2 min | [cierre + agradecimiento al invitado] |
| 9 | Outro music | 30 seg | [música de cierre] |

**Nota sobre el Segmento de Promoción:**
- Consultar `eventos.json` para usar eventos reales — si está vacío, marcar `[PENDIENTE — Juan agrega eventos]`
- Juan lo conduce siempre
- Tono: entusiasta, conversacional, sin leer como publicidad

Presenta esto con los temas reales del episodio en cada fila. **Espera "ok", "adelante", "perfecto" o similar antes de escribir el script.**

---

## Paso 3 — Escribir el script completo

Una vez aprobada la arquitectura, escribe el script palabra por palabra.

### Marcadores de producción

- `[PAUSA]` — silencio intencional de 0.5-1 segundo
- `[ÉNFASIS]` — palabra o frase que recibe énfasis vocal
- `[SFX: descripción]` — efecto de sonido o música sugerida
- `[TRANSICIÓN]` — cambio de segmento con música de fondo
- `[NOTA: texto]` — nota para el host, no se lee en voz alta

### Reglas de escritura

- Aplica las `reglas_tono` del `podcast-profile.json`
- **Consulta `glosario-cachaco.md` y usa español colombiano casual — bogotano moderno, sin arcaísmos**
- Palabras prohibidas: "sumerce", "ala", "chirriado", "cachifo", "caray", "carachas" (arcaísmos 40's) + "parcero", "bacano" (muy coloquiales) + "vosotros", "vos", "ché", "tío" (otros regionalismos)
- Tratamiento al oyente: "usted" o "ustedes" — NUNCA "tú" ni "sumerce"
- Usa el `intro_template` del perfil como base (puede adaptarlo pero no cambiarlo radicalmente)
- Usa el `outro_template` del perfil
- Escribe como se habla, no como se escribe: contracciones, frases cortas, pausas naturales
- Cada segmento debe tener una frase de transición clara al siguiente
- **Conectores conversacionales entre hosts** — el guion de co-host no es Host A habla / Host B reacciona / Host A habla. Los bloques deben conectarse con puentes que suenen como conversación real, no como turnos de debate:
  - ✅ "Y ese dato es clave, porque lo que viene después..." (retoma el hilo del otro)
  - ✅ "Mirá, yo añadiría algo a eso..." (suma sin interrumpir)
  - ✅ "Que es una locura, porque..." (reacción emocional + continuación)
  - ✅ "Claro — y si a eso le sumás que..." (construye sobre lo anterior)
  - ❌ [Host A: bloque de hechos] / [Host B: "¿Cómo?"] / [Host A: otro bloque] — mecánico, suena a interrogatorio
  - La regla: cada vez que cambia el host, la primera línea del nuevo bloque debe recoger algo de lo que dijo el anterior
  - **Calibrar los conectores contra la transcripción REAL del episodio anterior** (ej. el SRT en `E:\Transcriptor\transcripciones\`): los pases deben sonar a como los hosts hablan de verdad — name-checks ("¿sí o no, Juanito?", "como bien dijiste"), recoger lo anterior, callbacks ("¿se acuerdan de X? ahora sí") — no a turnos escritos de debate

**Audit retroactivo obligatorio** — Si en esta sesión se agrega o modifica una regla de calidad (conectores, tono, estructura) porque un guion existente la viola, revisar y corregir ese guion en el mismo turno antes de entregar. No basta con actualizar la regla — el artefacto existente debe quedar corregido también.

**Confirmación de entrega obligatoria** — Al terminar de escribir cualquier archivo (script, metadata, checklist), confirmar al usuario la ruta exacta donde quedó guardado: "Guardado en: C:\Users\andre\repos\kit-skill-creator\mrputridsden-production\scripts\EP00X-titulo.html". Nunca asumir que el usuario sabe dónde está el archivo.

**Si formato_episodio = `interview`:**
- Escribe las preguntas del host en orden de escalada: bienvenida → preguntas fáciles → profundas → cierre
- Usa el cuestionario generado en Paso 1.5 como estructura, pero adapta las palabras exactas para sonar natural
- Incluye notas de escucha activa: `[NOTA: si el invitado menciona X, profundiza con "¿y cómo afectó eso a...?"]`
- No escribas las respuestas del invitado — son improvisadas
- Incluye una pregunta de cierre: "¿qué le dirías a alguien que...?"
- Ejemplo de pregunta con nota:
```
[HOST: Tu nombre] ¿Qué aprendiste durante ese primer año?

[NOTA: Escucha atentamente. Si menciona un fracaso específico, pregunta:
"Cuéntame más de eso — ¿cómo lo superaste?"]
```

**Si formato_episodio = `co-host`:**
- Indica quién habla cada segmento: `[HOST: Nombre]`
- Usa el documento de sincronía (Paso 1.6) como guía para asignar segmentos
- Incluye momentos de intercambio marcados con `[INTERCAMBIO]` donde los hosts pueden comentar entre sí sin guion
- Equilibra el tiempo de habla entre los hosts (±20%)
- **Asigna ownership de segmentos por expertise del host, no solo por porcentaje de palabras.** Para Mr. Putrid's Den: Juan lidera segmentos de shows en vivo, mitología de artistas y genealogía musical (su expertise como promotor). Andrés lidera historia musicológica, hilo narrativo e hilo entre episodios.
  > ⚠️ **Desactualizado para MPD — ver `.claude/skills/mrputridsden/CLAUDE.md` §Regla de
  > balance co-host (la fuente vigente, no este archivo):** la proporción real es
  > **~70/30 a favor de Andrés** (no 50/50 — decisión de Andrés en EP.004), y la frase
  > "Yo quiero contar esta historia porque..." está **prohibida** para Juan (feedback
  > EP.004, 2026-06-11: lo hace sonar leyendo). Juan abre con el hecho directo, sin
  > fórmula declarativa — ver ejemplos concretos en `mrputridsden/CLAUDE.md`. Este bullet
  > queda como ejemplo genérico de "ownership por expertise, no por %" para shows NUEVOS
  > sin reglas propias — para MPD, siempre gana el archivo de CLAUDE.md citado arriba.
- Ejemplo de segmento con intercambio:
```
[HOST: Nombre1] [lee segmento del script...]

[INTERCAMBIO]
[HOST: Nombre2] ¿Y tú qué opinás de eso?
[HOST: Nombre1] Yo creo que...

[ambos pueden dialogar naturalmente — el script solo marca dónde ocurre]
```

### Formato de entrega del script

```
══════════════════════════════════════════════════════
  [NOMBRE PODCAST] — [EP.NNN]: [TÍTULO DEL EPISODIO]
  Duración estimada: ~[X] minutos | Formato: [formato]
══════════════════════════════════════════════════════

─── SEGMENTO 1: INTRO + HOOK ─────────────────────────

[SFX: música de apertura, fade out a los 5 segundos]

[Texto del script aquí — primera frase que engancha al oyente antes de que pueda cambiar el episodio]

[PAUSA]

─── SEGMENTO 2: BIENVENIDA ───────────────────────────

[Texto del script — máximo 30 segundos, breve presentación]

─── SEGMENTO 3: CONTEXTO ─────────────────────────────

[Texto del script]

[... continúa para cada segmento aprobado ...]

─── SEGMENTO FINAL: OUTRO + CTA ──────────────────────

[Outro template adaptado]

[SFX: música de cierre, fade in]

══════════════════════════════════════════════════════
  FIN DEL SCRIPT — EP.[NNN]
══════════════════════════════════════════════════════
```

---

## Paso 4 — Checklist de calidad

Antes de entregar, verifica internamente cada punto:

- [ ] El hook de apertura genera intriga o sorpresa en los primeros 30 segundos
- [ ] El tono es consistente con las `reglas_tono` del perfil en todos los segmentos
- [ ] Los `[PAUSA]` están colocados en momentos de impacto emocional o reflexión
- [ ] El CTA del outro es claro, específico y accionable
- [ ] La duración estimada está dentro del rango del perfil (±15%)
- [ ] Intro y outro usan los templates del perfil como base
- [ ] El takeaway está explicitado claramente antes del outro
- [ ] No hay segmentos que superen el doble de la duración estimada de otro
- [ ] [Si interview] Las preguntas escalan de fácil a profundo
- [ ] [Si co-host] Los hosts tienen tiempos de habla equilibrados (±20%)
- [ ] **Word count real verificado programáticamente** (NO estimado a ojo): contar las
      palabras habladas del script terminado — excluyendo `[marcadores]`, headers y la
      sección de fuentes — y confirmar que cae dentro de ±15% del target calculado en
      Paso 2. Lección de Corporate Crime Confidential EP.001 (2026-07-04): un script
      declaró ~6.700 palabras en su propio footer sin verificarlo nunca; el conteo real
      era ~3.000, la mitad del target de 45 min — el guion quedó "completo" con la mitad
      del contenido necesario y esto solo se detectó después de grabar. No confiar en un
      conteo autoreportado — contar de verdad antes de guardar como completo.
      Gotcha PS 5.1 (mordió en CCC EP002, 2026-07-07): al leer el guion para contar,
      usar `Get-Content -Raw -Encoding UTF8` — sin el flag, PS 5.1 lee ANSI y corrompe
      los headers Unicode (──/══) del guion, y el conteo falla o incluye basura.
- [ ] **Si este fue el episodio piloto (primer wpm real medido del show):** crear
      `guion-style-[show].md` en la carpeta de producción del show con el wpm medido
      (`palabras_habladas_del_SRT / minutos_de_audio`) y la tabla de dimensionamiento,
      siguiendo el patrón de `btq-production/guion-style-btq.md` o
      `corporate-crime-confidential-production/guion-style-ccc.md`. Si el show ya tiene
      ese archivo, actualízalo solo si el wpm medido de este episodio difiere
      significativamente del ya registrado.

---

## Paso 5 — Guardar y transición

1. Guarda el script como `episodio-[NNN]-[slug-del-titulo].md` en el directorio actual.
   (slug = título en minúsculas con guiones, sin tildes: "inteligencia-artificial")

2. Muestra resumen:

```
══════════════════════════════════════════
  Script generado ✓
══════════════════════════════════════════
  Episodio:   [EP.NNN] — [Título]
  Formato:    [formato]
  Duración:   ~[X] minutos estimados
  Segmentos:  [número]
  Archivo:    episodio-[NNN]-[slug].md
══════════════════════════════════════════
```

3. Pregunta: "¿Continuamos con el plan de grabación, el artwork, o prefieres exportar el HTML ahora?"

---

## Nota — Flujo completo post-grabación (EP.002+)

El guion es el primer paso. Después de grabar, el flujo continúa en este orden:

```
Show Notes / Metadata  →  workflows/05-show-notes.md
Artwork del episodio   →  workflows/03-artwork.md   (Spotify 1:1 + Stories 9:16 + YouTube 16:9)
Arte para redes        →  workflows/04-social-media.md  (cuando redes estén activas)
Social Media           →  workflows/04-social-media.md  (plan lanzamiento 3 días)
HTML Export            →  workflows/06-html-export.md
```

Usar `mrputridsden-production/templates/checklist-produccion-episodio.md` para trackear cada entregable.
