# Workflow 01 — Guion Completo del Episodio

Genera un script completo, palabra por palabra, para un episodio específico. Se adapta al formato del podcast (solo, interview, co-host, episodio con invitado especial).

**Regla fundamental: Lee `podcast-profile.json` primero. Si no existe, lanza `00-setup.md` antes de continuar.**

---

## Paso -1 — ¿Hay episodio con invitado especial esta semana?

**Solo si el perfil tiene `segmento_invitado.activo = true`**, pregunta primero:

> ¿Esta semana hay [nombre del segmento_invitado]? ¿Tienen invitado especial?

- **SÍ** → `formato_episodio = "invitado_especial"`. Ir a **Paso 0-IE** antes de continuar.
- **NO** → `formato_episodio` según el perfil. Continuar con **Paso 0** normalmente.

Si el perfil NO tiene `segmento_invitado` → saltar este paso.

---

## Paso 0-IE — Flujo episodio con invitado especial

### A. Recopilar datos básicos

Pregunta:

> **¿Quién viene al [nombre del segmento_invitado]?**
> 1. Nombre del invitado
> 2. ¿Qué hace? (tipo según los perfiles definidos en el podcast)
> 3. ¿Tienen algún link, red social o referencia donde pueda investigarlo?
> 4. Número del episodio

### B. Modo Narval — Investigar al invitado

Con el nombre y perfil, **investiga al invitado en la web** antes de generar nada:
- Busca su trabajo, proyectos, trayectoria
- Encuentra 3-5 datos curiosos o poco conocidos
- Identifica momentos clave de su carrera
- Busca entrevistas previas para no repetir preguntas ya hechas

Con esa investigación, genera el **documento de prep para hosts** usando `templates/episodio-invitado-prep-hosts.md`:
- Bio real investigada (la que encontraste, no la que el invitado escribe)
- Los datos curiosos
- 5-7 preguntas únicas basadas en su trayectoria real
- Selecciona el set de preguntas base del perfil correspondiente en `templates/preguntas-por-perfil.md` si existe

Presenta el documento de prep al usuario y di:
> "Acá está la investigación del invitado. Revisá si falta algo antes de enviarle la carta."

### C. Generar carta al invitado

Usando `templates/episodio-invitado-invitacion.md`, genera la carta personalizada con:
- Referencia específica al trabajo del invitado (de lo investigado)
- Los 3 temas propuestos para la conversación

Genera también el documento simple para el invitado usando `templates/episodio-invitado-cuestionario.md` — solo pide bio libre, confirmación de temas y lo que NO quiere que se toque.

Di al usuario:
> "Acá está la carta de invitación y el doc para enviarle al invitado. Cuando confirme y devuelva su NO-list, regresá y generamos el guion."

### D. Guardar ficha del invitado

Crea `fichas-invitados/[nombre-invitado].md` con:
```
# Ficha: [Nombre del invitado]
Episodio: EP.[NNN]
Fecha: [fecha]
Perfil: [tipo según el podcast]
Bio investigada: [resumen]
Datos curiosos: [lista]
Temas cubiertos: [lista — llenar después de grabar]
NO-list: [lo que pidió que no se toque]
Redes: [links]
```

### E. Generar guion (solo después de confirmación del invitado)

**No generar el guion hasta que el usuario confirme que el invitado respondió.**

Cuando el usuario diga que el invitado confirmó:
- Integrar la NO-list del invitado
- Usar las preguntas investigadas + las aprobadas por el invitado
- Si la grabación es presencial — indicar `[cualquiera de los hosts puede preguntar esto]`
- Si es remoto — indicar qué host conduce cada pregunta

---

## Paso 0 — Cargar identidad del podcast

Lee `podcast-profile.json`. Extrae y ten disponible:
- Nombre del podcast, host(s), formato
- Tono y reglas de escritura (`reglas_tono`)
- Lenguaje: región, estilo, palabras frecuentes, palabras prohibidas, tratamiento al oyente (`lenguaje`)
- Intro y outro templates
- Convención de numeración
- Duración promedio (`duracion_min`)
- Estilo de narración y word count target (`estilo_narración`, `word_count_target`)
- Segmentos activos: `segmento_invitado`, `segmento_promo`

Si existe `glosario-[slug].md` (slug = nombre del podcast en minúsculas con guiones) → cargarlo y usar sus términos en el guion.
Si existe `eventos.json` → cargarlo para el segmento de promo.

---

## Paso 0.5 — Detectar formato de ESTE episodio

El perfil tiene un formato default, pero cada episodio puede ser diferente.

Pregunta:

> El perfil de tu podcast es **[formato del perfil]**, pero cada episodio puede variar.
> ¿Cómo es **este episodio específico**?
> 1. **Solo** — solo tú hablas
> 2. **Con co-host** — [mostrar nombres de co-hosts del perfil si existen]
> 3. **Entrevista** — tienes un invitado especial

Espera la respuesta. Guarda `formato_episodio: "solo" | "interview" | "co-host"` como override del formato del perfil.

---

## Paso 1 — Datos del episodio

Pregunta en un solo mensaje adaptado al formato del perfil:

> **Para este episodio:**
> 1. ¿Cuál es el número de episodio? (ej: 001, 014...)
> 2. ¿Cuál es el tema o título tentativo?
> 3. ¿Cuál es el ángulo único — qué perspectiva o enfoque vas a tomar que no hace todo el mundo?
> 4. ¿Hay alguna referencia cultural, historia, persona o evento que sirva como hilo conductor?
> 5. ¿Cuál es el takeaway principal — qué debe llevarse el oyente al terminar?

**Si formato = `interview`**, agrega:
> 6. Nombre del invitado y cargo o descripción en una línea
> 7. ¿De qué 3 temas quieres hablar con el invitado?
> 8. ¿Hay algún tema tabú o pregunta que NO debes hacer?

**Si formato = `co-host`**, agrega:
> 6. ¿Quién abre el episodio hoy?
> 7. ¿Hay dinámicas especiales entre los hosts para este episodio?

---

## Paso 1.5 — Cuestionario de entrevista y briefing (si es interview)

**Solo si `formato_episodio = "interview"`:**

Genera:

```
CUESTIONARIO DE ENTREVISTA — EP.[NNN]
═════════════════════════════════════════════════════════
  Invitado: [nombre]
  Tema principal: [tema]
  Duración estimada: ~[X] minutos
═════════════════════════════════════════════════════════

BLOQUE DE BIENVENIDA (warm-up)
──────────────────────────────────────────────────────
1. ¿Quién sos y qué hacés? [OBLIGATORIA]
2. ¿Cómo llegaste a esto? [OBLIGATORIA]

BLOQUE CENTRAL — TEMA PRINCIPAL (escaladas)
──────────────────────────────────────────────────────
3. [Pregunta exploradora — tema 1]
4. [Pregunta de profundidad — "¿por qué creés que...?"]
5. [Pregunta sobre tema 2]
6. [Pregunta provocadora — desafiar perspectiva]
7. [Pregunta sobre tema 3 — síntesis]

BLOQUE DE CIERRE
──────────────────────────────────────────────────────
N-1. ¿Qué consejo le darías a alguien que está empezando? [OBLIGATORIA]
N. ¿Dónde nos pueden encontrar? [redes, web] [OBLIGATORIA]

PREGUNTAS DE RESERVA (si queda tiempo)
──────────────────────────────────────────────────────
R1. [Pregunta alternativa]
R2. [Pregunta sobre dato sorprendente]
```

---

## Paso 1.6 — Documento de sincronía pre-grabación (si es co-host)

**Solo si `formato_episodio = "co-host"`:**

```
SYNC PRE-GRABACIÓN — EP.[NNN]
─────────────────────────────────────────
  Tema del episodio: [tema]
  Ángulo: [ángulo único]
─────────────────────────────────────────

ASIGNACIÓN DE SEGMENTOS
· [Host1] abre con: [hook — primera frase]
· [Host2] cubre: [Bloque A]
· [Host1] cubre: [Bloque B]
· Cierre a cargo de: [host que cierra]

PUNTOS DE DEBATE PLANIFICADOS
· [Donde los hosts pueden tener perspectivas distintas]

─────────────────────────────────────────
TIEMPO ESTIMADO DE HABLA POR HOST
  [Host1]: ~[X]%
  [Host2]: ~[X]%
─────────────────────────────────────────
```

---

## Paso 2 — Presentar arquitectura para aprobación

Muestra el word count target:

```
WORD COUNT TARGET PARA ESTE EPISODIO
════════════════════════════════════════
Duración: [X] minutos
Formato: [formato_episodio]
Estilo: [estilo_narración]
→ Word count target: ~[N] palabras
════════════════════════════════════════
```

Presenta la arquitectura del episodio adaptada al formato. **Espera aprobación antes de escribir el script.**

**Estructura base — episodio normal (co-host / solo):**

| # | Segmento | Duración | Contenido |
|---|----------|----------|-----------|
| 1 | Intro music | 30 seg | música de apertura |
| 2 | Bienvenida | 1-2 min | hosts abren el episodio |
| 3 | Contexto del tema | 3-4 min | por qué este tema ahora |
| 4 | Bloque principal A | [X min] | primer desarrollo |
| 5 | [INTERCAMBIO] | — | diálogo libre entre hosts |
| 6 | Bloque principal B | [X min] | segundo desarrollo |
| 7 | Segmento de Promoción *(si activo)* | 3-5 min | eventos de `eventos.json` |
| 8 | Reflexión / Takeaway | 3-4 min | conclusión |
| 9 | Outro + CTA | 1-2 min | cierre + call to action |
| 10 | Outro music | 30 seg | música de cierre |

**Estructura — episodio con invitado especial:**

| # | Segmento | Duración | Contenido |
|---|----------|----------|-----------|
| 1 | Intro especial | 30 seg | música + anuncio del invitado |
| 2 | Bienvenida + presentación | 2-3 min | presentar al invitado |
| 3 | Bloque preguntas A | [X min] | preguntas aprobadas |
| 4 | [INTERCAMBIO natural] | — | conversación fluye libre |
| 5 | Bloque preguntas B | [X min] | preguntas aprobadas |
| 6 | Cierre con invitado | 2-3 min | dónde encontrarlo, proyectos |
| 7 | Segmento de Promoción *(si activo)* | 3-5 min | AL FINAL — `eventos.json` |
| 8 | Outro + CTA | 1-2 min | cierre + agradecimiento |
| 9 | Outro music | 30 seg | música de cierre |

**Segmento de Promoción:**
- Solo incluir si `segmento_promo.activo = true` en el perfil
- Conductor: el host designado en el perfil
- Consultar `eventos.json` — si está vacío, marcar `[PENDIENTE]`

---

## Paso 3 — Escribir el script completo

### Marcadores de producción

- `[PAUSA]` — silencio intencional de 0.5-1 segundo
- `[ÉNFASIS]` — palabra o frase que recibe énfasis vocal
- `[SFX: descripción]` — efecto de sonido o música sugerida
- `[TRANSICIÓN]` — cambio de segmento con música de fondo
- `[NOTA: texto]` — nota para el host, no se lee en voz alta

### Reglas de escritura

- Aplica las `reglas_tono` del `podcast-profile.json`
- **Aplica el lenguaje del perfil** — si el perfil tiene campo `lenguaje`: usar su estilo, palabras frecuentes, palabras prohibidas; si no existe el campo → usar lenguaje neutro en español
- Si existe glosario → usar los términos definidos ahí
- Trata al oyente según `lenguaje.tratamiento_oyente` del perfil — si no está definido → usar "tú"
- Usa el `intro_template` del perfil como base
- Usa el `outro_template` del perfil
- Escribe como se habla, no como se escribe: contracciones, frases cortas, pausas naturales
- Cada segmento debe tener una frase de transición clara al siguiente

**Si formato_episodio = `interview`:**
- Escribe las preguntas del host en orden de escalada
- No escribas las respuestas del invitado — son improvisadas
- Incluye notas de escucha activa: `[NOTA: si el invitado menciona X, preguntá "¿y cómo afectó eso a...?"]`

**Si formato_episodio = `co-host`:**
- Indica quién habla cada segmento: `[HOST: Nombre]`
- Equilibra el tiempo de habla entre los hosts (±20%)
- Incluye momentos `[INTERCAMBIO]` donde los hosts dialogan sin guion fijo

### Formato de entrega

```
══════════════════════════════════════════════════════
  [NOMBRE PODCAST] — [EP.NNN]: [TÍTULO DEL EPISODIO]
  Duración estimada: ~[X] minutos | Formato: [formato]
══════════════════════════════════════════════════════

─── SEGMENTO 1: INTRO + HOOK ─────────────────────────

[SFX: música de apertura]

[Primera frase que engancha al oyente]

[PAUSA]

─── SEGMENTO 2: BIENVENIDA ───────────────────────────

[Texto del script]

[... continúa por cada segmento aprobado ...]

─── SEGMENTO FINAL: OUTRO + CTA ──────────────────────

[Outro template adaptado]

[SFX: música de cierre]

══════════════════════════════════════════════════════
  FIN DEL SCRIPT — EP.[NNN]
══════════════════════════════════════════════════════
```

---

## Paso 4 — Checklist de calidad

Verifica antes de entregar:

- [ ] Hook de apertura genera intriga en los primeros 30 segundos
- [ ] Tono consistente con `reglas_tono` del perfil en todos los segmentos
- [ ] Lenguaje regional correcto — palabras del glosario, sin palabras prohibidas
- [ ] Los `[PAUSA]` están en momentos de impacto o reflexión
- [ ] CTA del outro es claro y accionable
- [ ] Duración estimada dentro del rango del perfil (±15%)
- [ ] Takeaway explicitado antes del outro
- [ ] [Si interview] Preguntas escalan de fácil a profundo
- [ ] [Si co-host] Hosts tienen tiempos de habla equilibrados (±20%)
- [ ] [Si segmento_promo activo] Aparece en la posición correcta según el tipo de episodio

---

## Paso 5 — Guardar y transición

1. Guarda el script como HTML en `scripts/EP[NNN]-[slug-del-titulo].html`
   (slug = título en minúsculas con guiones, sin tildes)

2. Ejecuta backup automático:
   ```
   git add scripts/EP[NNN]-[slug].html
   git commit -m "EP.[NNN] — [título] — [fecha]"
   git push origin main
   ```
   Si G: está montado → copiar también allá.

3. Muestra resumen:

```
══════════════════════════════════════════
  Script generado ✓
══════════════════════════════════════════
  Episodio:   [EP.NNN] — [Título]
  Formato:    [formato]
  Duración:   ~[X] minutos estimados
  Segmentos:  [número]
  Archivo:    scripts/EP[NNN]-[slug].html
  Git:        ✓ commit + push
══════════════════════════════════════════
```

4. Pregunta: "¿Continuamos con el plan de grabación, el artwork, o exportar el HTML ahora?"
