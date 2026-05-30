---
name: btq-guion
description: >
  Crea guiones completos para episodios de Behind the Queue (BTQ) en formato anchor points.
  Solo para ESCRIBIR GUIONES — para artwork, redes, registro o checklist usar btq-project.
  Triggers: guión BTQ, script episodio BTQ, guion para grabar, escribir guión BTQ,
  guión de Frieren, guión Bohemian Rhapsody, guión God of War, quiero escribir el guión,
  ayúdame con el guión, estructura del episodio, write BTQ script, create episode script BTQ,
  script for recording, new BTQ episode script, anchor points BTQ, BTQ script format.
---

# BTQ Guion Creator — Guiones para Behind the Queue

Crea el guión completo de un episodio de BTQ en formato anchor points, aplicando
automáticamente todas las reglas de tono, estructura y marca. Andy habla; tú estructuras.

**Regla fundamental: el guión no reemplaza a Andy — le da los bloques. Andy decide cómo conectarlos.**

> **Nota:** Las reglas de Tone Master (TM) y el roadmap completo de la temporada están en
> `btq-project/SKILL.md` (secciones 4 y 7). Leer ese archivo antes de escribir cualquier guión.

---

## Paso 1 — Leer contexto y confirmar datos del episodio

**Primero:** Leer `btq-project/SKILL.md` sección 7 (Roadmap) para obtener el número de episodio siguiente, referencia cultural y tema — si el usuario no los especificó. Solo preguntar lo que no aparece en el roadmap.

Antes de escribir, reúne esta información. Si ya fue compartida en la conversación, úsala directamente sin preguntar de nuevo.

### Datos necesarios:

**Obligatorios:**
- Número de episodio (EP.0XX)
- Referencia cultural (personaje, canción, película, videojuego, anime)
- Título tentativo del episodio
- Tema central (el concepto de experiencia/liderazgo que se va a explorar)
- Frase de cierre del personaje (la que Andy usa en el TM final)

**Opcionales pero valiosos:**
- Fuentes de datos preferidas (si no se especifican, usar: Gallup, McKinsey, Deloitte, HBR, SHRM)
- Segmento variable deseado (Minuto de Acción, roles, consecuencias — ver Paso 3)
- Duración objetivo (si Andy tiene preferencia; de lo contrario ignorar)
- Notas específicas del episodio

### Si falta información:

Pregunta en UN solo bloque conversacional, no en interrogatorio:

> "Para armar el guión necesito confirmar algunos datos. ¿Me confirmas el número de episodio, la referencia cultural y la frase de cierre del personaje que vas a usar?"

Si el usuario dice "usa el roadmap" o menciona el personaje sin más datos, busca en `btq-project/SKILL.md`
sección 7 (Roadmap) y completa con lo que corresponde.

### Fuentes de investigación obligatorias (antes de escribir Seg 2):

No limitarse a Wikipedia o redes sociales. Para cualquier referencia cultural, buscar activamente en:
- Blogs especializados del fandom (ej. anmosugoi.com para anime)
- Reddit — subreddits específicos de la obra
- Baidu — para obras con origen chino o japonés
- Facebook — comunidades de fans (tienen datos que fuentes formales no publican)
- Entrevistas en medios especializados (no solo mainstream)

**Por qué:** Andy encontró en Reddit y blogs la historia real del origen de Diarios de la Boticaria que ninguna fuente formal traía completa.

---

## Paso 2 — Diseñar la arquitectura del episodio

Antes de escribir el guión completo, presenta la arquitectura para validación:

```
EP.0XX — [TÍTULO]
Referencia cultural: [personaje/obra]
Tema central: [concepto]

ARQUITECTURA — 7 SEGMENTOS:

1. HOOK            — [idea del gancho sin revelar el personaje]
2. EL PUENTE       — [cómo se conecta con operaciones/experiencia]
3. LOS DATOS       — [fuentes y estadísticas a usar, máx. 1 por bloque]
4. MITO O REALIDAD — [3 rondas propuestas]
5. [SEGMENTO VAR.] — [Minuto de Acción / Roles / Consecuencias / lo que pida el episodio]
6. CIERRE          — [2 audiencias: líderes (3 preguntas) → agentes/supervisores]
7. TEASER          — [episodio siguiente] + TM de cierre
```

Pregunta si la arquitectura está bien o si quiere ajustar algo antes de desarrollar.

> **Nota de estructura:** Esta es la arquitectura mínima de 7 segmentos. Para episodios completos (EP.012+), agregar según corresponda: Las Lecciones (ancladas en momentos específicos), Referencias Cruzadas (mín. 2 de negocios), Aplicable Hoy (3 acciones, 1 permanente), Recomendaciones de Andy. Ver btq-project sección 5 para la estructura completa de 10 segmentos.

---

## Paso 3 — Escribir el guión en formato anchor points

### Reglas de formato anchor points (EP.008+):

Cada segmento tiene:
- **Titular de entrada** en negrita (lo que arranca el bloque)
- Bullets de datos/ideas cortos — Andy los desarrolla en su propia voz
- Recordatorios de anécdota como notas internas `[NOTA: Andy cuenta...]` — nunca el texto completo
- `[REMATE]` al cierre de cada bloque — entregado completo, sin suavizar
- Sin transiciones entre bloques — Andy decide cómo conectar

### Marcadores de script:

| Marcador | Duración | Uso |
|---|---|---|
| `[PAUSA]` | 1–2 seg | Después de una idea importante |
| `[PAUSA LARGA]` | 3–4 seg | Que la idea aterrice |
| `[REMATE]` | — | Última línea de cada bloque, dicha completa |
| `[NOTA]` | — | Recordatorio para Andy, no se lee en voz alta |
| *cursiva* | — | Énfasis de voz |

### Reglas de datos:

Ver reglas completas en `btq-project/SKILL.md` sección 4 (Tone Master → Data rules). Resumen: máximo 1 dato por bloque, nunca estadísticas consecutivas.

**Reglas adicionales (aprendidas en auditoría EP.014):**
- El límite "sin estadísticas consecutivas" aplica también entre segmentos — si Seg 3 cierra con dato, Seg 4 NO puede abrir con dato
- Todo dato de HBR u otra fuente académica requiere: título del estudio + año + existencia verificada. Dato sin año o sin título = dato sospechoso, eliminarlo
- Aplicar las 7 reglas de veracidad del CLAUDE.md antes de incluir cualquier dato. Si no hay fuente verificable, no incluirlo

**Audit retroactivo obligatorio** — Si en esta sesión se agrega o modifica una regla de calidad (datos, tono, estructura) porque un guión existente la viola, revisar y corregir ese guión en el mismo turno antes de entregar. No basta con actualizar la regla — el artefacto debe quedar corregido también.

### Reglas de contenido:

- Anécdotas SIEMPRE en tercera persona: "conozco un caso", "conocí una operación" — nunca con nombres identificables
- Andy nunca es referenciado en segunda persona dentro de su propio guión
- No back-to-back statistics — punto duro

### Marcadores [VERIFICAR] — durante el borrador

Marcar con `[VERIFICAR: descripción]` cualquier dato no confirmado por fuente específica:

```
[VERIFICAR: año exacto de lanzamiento del primer álbum]
[VERIFICAR: nombre de la editorial que rechazó el manuscrito original]
[VERIFICAR: número exacto de copias vendidas en la primera semana]
[VERIFICAR: cita textual atribuida al autor]
```

Datos que siempre requieren marcador si no están verificados: fechas exactas, números (ventas, presupuesto, duración), nombres propios, citas textuales de personas reales, detalles físicos o geográficos específicos.

**Antes de entregar:** Resolver TODOS los marcadores con web search. El guión final no puede tener ningún [VERIFICAR] sin resolver.

| ❌ Genérico (script blando) | ✅ Específico (script que se ve) |
|---|---|
| "pasó un tiempo difícil en su juventud" | "fue arrestado en 1966, tenía 17 años — pasó varios meses en Winson Green Prison" |
| "grabaron el álbum muy rápido" | "una sola sesión de 12 horas, el 16 de octubre de 1969, en Regent Sounds Studios, Londres. Costo total: £500." |
| "el video se viralizó mucho" | "2.9 millones de likes en Instagram en menos de 48 horas" |
| "la autora publicó en internet" | "Natsu Hyuuga lo publicó de forma anónima en una plataforma gratuita en 2011, con un concepto completamente diferente al que llegó a publicarse." |

---

## Paso 3.5 — Estilo narrativo: el habla cinemática para host solo

BTQ es un show de un solo host. El estilo narrativo debe hacer que la historia se VEA, no solo se escuche.

### Especificidad visual obligatoria

La regla de oro: si puedes ver la escena en tu cabeza mientras escribes, el nivel de detalle es el correcto.

- ❌ "sufrió un accidente y no pudo seguir"
- ✅ "una máquina se cerró sobre su mano. Le amputó las puntas de los dedos medio e índice — la mano con la que pisaba los trastes"

- ❌ "vivió en condiciones muy humildes"
- ✅ "vivía en un cuarto de 12 metros cuadrados en Tokio, comiendo arroz con salsa de soya, escribiendo desde las 11 de la noche hasta las 4 de la mañana después de su turno en la cafetería"

### El beat de reacción — versión solo

En un show de dos hosts, uno reacciona al dato del otro y eso le da tiempo al oyente para procesar. En BTQ ese espacio se crea así:

**Con [PAUSA] + confirmación propia:**
```
[dato sorprendente]
[PAUSA]
Sí. Exactamente lo que están pensando.
[repite con más detalle y contexto]
```

**Con pregunta retórica directa:**
```
¿Y saben cuánto tiempo duró esa sesión de grabación?
[PAUSA]
Doce horas. Una sola tarde.
```

**Con eco inmediato:**
```
Su papá se negó a pagar la fianza.
[PAUSA]
Su propio padre. Se negó.
```

### La inversión de expectativa

Instalar la expectativa obvia → destruirla:

- "La crítica dijo que era ruido para gente sin criterio. [PAUSA] El público lo llevó al top 10 en su primera semana."
- "Esa canción de emergencia, ese relleno de último minuto... [PAUSA] fue el primer sencillo del álbum. La canción más conocida de la banda."
- "Perdió las puntas de sus dedos. Y con eso, sin querer, inventó el sonido que definiría todo el metal que vino después."

### La conexión improbable

Conectar dos elementos que parecen no tener relación para revelar el patrón central del episodio:

- Django Reinhardt (jazz belga, 1930s) → Tony Iommi (metal británico, 1970s) → mismo patrón: restricción que se convierte en identidad
- Para BTQ: buscar activamente la conexión entre la obra de referencia y el mundo de operaciones/liderazgo/CX. Esa conexión que nadie vería venir ES el valor del episodio.

### El ancla de lugar y tiempo

Los hechos sueltos no tienen peso. Los hechos con coordenadas sí:

- ❌ "grabaron rápido con poco presupuesto"
- ✅ "16 de octubre de 1969. Regent Sounds Studios, Londres. Una tarde. £500."

- ❌ "lo publicó en internet sin mucha expectativa"
- ✅ "2011. Plataforma Shōsetsuka ni Narō. Sin nombre real. Sin editorial. Con un concepto completamente diferente al que llegó a publicarse."

---

## Paso 4 — Aplicar el Tone Master (TM)

El TM completo está en `btq-project/SKILL.md` sección 4. Resumen de los puntos críticos:

- **Apertura:** "Buenas y santas. Feliz día, feliz tarde o feliz noche. Cualquier día que éste sea." — NUNCA abreviada
- **Intro:** "Esto es Behind the Queue, episodio [NÚMERO]." — siempre con número
- **Cierre (EP.010+):** "Esto fue Behind the Queue, episodio [NÚMERO]. Yo soy Andy. Y como diría [personaje]: [frase]."
- **Prohibiciones absolutas:** ❌ "obviamente" ❌ "pero bueno" ❌ muletillas ❌ segunda persona en guión propio ❌ anécdotas con nombres

Si al revisar el guión aparece alguna de estas palabras o estructuras, elimínala antes de entregar.

---

## Paso 5 — Estructura detallada de los 7 segmentos

### Segmento 1 — Hook

- Gancho emocional SIN revelar el personaje todavía
- Pregunta o situación que conecta con la experiencia del oyente
- Revelar el nombre del personaje/obra
- "Para el que no lo conoce..." → 3–4 líneas accesibles sobre la serie/juego/película
- `[REMATE]` de apertura

### Segmento 2 — El Puente

- Transición natural de la referencia cultural a la operación real
- Identifica el paralelo central (qué tiene en común el personaje con un líder/supervisor/agente)
- `[REMATE]` que ancle la conexión

**"Detrás de" como columna vertebral (aprendido EP.014):**
No solo analizar la obra o el personaje — investigar la historia del CREADOR antes de crear lo que creó. Esa historia muchas veces es más poderosa que cualquier análisis del personaje.
- Música: ¿qué pasó en la vida del artista ANTES y DURANTE la creación de esa obra?
- Anime/Manga: ¿cuál fue el origen de la obra, quién la escribió, qué tuvo que superar?
- Videojuegos: ¿qué enfrentó el equipo/director para crear ese juego?
- Películas: ¿por qué se hizo esa película, qué rechazos tuvo, qué sacrificios?

**Por qué:** EP.012 (Freddie/Queen) y EP.014 (Natsu Hyuuga/Maomao) son los mejores ejemplos — la historia del creador da la dimensión humana que conecta el tema del episodio con la audiencia. Natsu Hyuuga vivió exactamente lo que Maomao predica.

### Segmento 3 — Los Datos

- Evidencia con fuentes (1 dato por bloque, máximo)
- Andy desarrolla la implicación del dato en sus propias palabras
- `[NOTA]` para recordar de dónde viene cada fuente
- Si hay más de 1 dato importante, distribuirlos en sub-bloques separados
- `[REMATE]` que conecte el dato con la realidad operativa

### Segmento 4 — Mito o Realidad

Mínimo 3 rondas. Formato:

```
MITO: "[Afirmación común que se va a cuestionar]"
[PAUSA]
[Andy responde con evidencia o perspectiva]
[REMATE]: La realidad es [afirmación directa].
```

Diseñar mitos relevantes al tema del episodio, no genéricos.

### Segmento 5 — Segmento Variable

Elige según lo que necesita el episodio (preguntar si no se especifica):

**Minuto de Acción** — 1 cosa concreta que el oyente puede hacer esta semana:
```
[NOTA: Andy presenta como reto específico y alcanzable]
[REMATE]: No mañana. Esta semana.
```

> **Regla EP.014+:** Si el episodio tiene "Aplicable Hoy" con 3 acciones, al menos UNA debe ser una **herramienta mental permanente** — algo que el oyente pueda usar en cualquier reunión por el resto de su carrera, no solo esta semana. Acciones solo semanales son correctas pero olvidables al miércoles.
> 
> **Anti-repetición:** Antes de finalizar Aplicable Hoy, verificar que ninguna de las 3 acciones haya aparecido igual en un episodio anterior. Si repite una acción de EP.012+ es una señal de que la lección no está anclada en este episodio específico.

**Roles** — cómo aplica el tema según el rol del oyente:
```
Si eres agente: [comportamiento específico]
Si eres supervisor: [acción específica]
Si eres líder: [decisión específica]
```

**Consecuencias** — qué pasa si no se aplica lo del episodio:
```
[Consecuencia a corto plazo]
[Consecuencia a largo plazo]
[REMATE] duro
```

### Segmento 6 — Cierre

Siempre dos audiencias, en este orden:

**Líderes primero — 3 preguntas de reflexión:**
```
¿Cuándo fue la última vez que [acción relacionada al tema]?
¿Qué pasaría si [situación del episodio] ocurriera en tu operación mañana?
¿Qué va a cambiar en tu equipo después de escuchar esto?
[PAUSA LARGA]
```

**Agentes y supervisores — mensaje directo:**
```
[Validación del rol] + [acción concreta que está en sus manos]
[REMATE] de cierre
```

### Segmento 7 — Teaser + TM final

**Conector orgánico al siguiente EP (EP.012+):** Durante la investigación del episodio actual, identificar un dato real — una influencia, un artista citado, una fecha histórica compartida — que conecte orgánicamente con el tema o referencia del episodio siguiente. Ese dato se convierte en el puente del teaser. NO se inventa — se descubre en la investigación. Si no existe conector natural, el teaser puede ser solo de intriga sin dato inventado.

```
[NOTA: Andy menciona el próximo episodio con intriga, sin spoilear]
[Frase que conecta el episodio actual con el siguiente]

[PAUSA LARGA]

Esto fue Behind the Queue, episodio [NÚMERO].
Yo soy Andy. Y como diría [personaje]: [frase de cierre del personaje].
```

---

## Paso 6 — Revisión de calidad antes de entregar

Antes de presentar el guión final, verifica:

Cargar y aplicar el checklist completo desde `workflows/quality-checklist.md`.

Resumen de los 4 bloques:
- **Checklist TM** — 10 ítems: apertura, número EP, prohibiciones, REMATE, audiencias, frase TM
- **Checklist de calidad EP.014+** — 7 ítems: cross-segment stats, HBR verification, truth rules, herramienta permanente, anti-repetición, business refs, "detrás de"
- **Checklist de formato** — 5 ítems: negritas, REMATE, NOTA, PAUSA, cursiva
- **Checklist de estilo narrativo (EP.015+):**
  - [ ] Cero marcadores [VERIFICAR] sin resolver
  - [ ] Cada bloque largo tiene al menos un beat de especificidad visual
  - [ ] Cada dato sorprendente tiene su [PAUSA] o equivalente retórico
  - [ ] Al menos una inversión de expectativa en el Seg 2 o Seg 5
  - [ ] La conexión improbable con el mundo de negocios/ops está explícita (no implícita)

---

## Paso 7 — Entrega

**Confirmación de entrega obligatoria** — Al presentar el guión final, confirmar explícitamente cómo fue entregado: "Guión completo arriba en el chat" o, si se exportó a Google Doc, confirmar el link exacto. Nunca asumir que Andy sabe dónde está.

### Formato de entrega:

Presenta el guión completo en texto con toda la marca tipográfica de BTQ
(negritas, marcadores, notas). Indica claramente:

```
GUIÓN LISTO — EP.0XX — [TÍTULO]

Segmentos: 7
Referencia cultural: [obra]
Fuentes incluidas: [lista]
Frase TM: "[frase del personaje]"

[GUIÓN COMPLETO]

---
PENDIENTES DE COMPLETAR:
- [cualquier sección que necesite input de Andy]
- [datos que Andy debe validar antes de grabar]
```

### Si Andy pide el .docx:

Indica los colores BTQ para aplicar manualmente en Word/Google Docs:
- Fondo de headers: `#0A0A0A` (void black)
- Texto de REMATE: `#C9A84C` (signal gold)
- Cuerpo: `#F5F2EC` (off-white)
- Marcadores [NOTA]: gris claro, texto más pequeño

### Al finalizar:

Pregunta:
- ¿Quieres ajustar algún bloque?
- ¿Arrancamos con los prompts de artwork para este episodio?
- ¿Generamos el plan de lanzamiento en redes (3 días)?

---

*BTQ Guion Skill v1.3 · Mayo 2026 · Audit retroactivo + Confirmación de entrega + Conector orgánico teaser añadidos*
