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

## Flujo de ejecución

| Paso | Tarea | Dónde |
|---|---|---|
| 0 | **Leer** `btq-project/SKILL.md` §4 (Tone Master) y §7 (Roadmap) — obligatorio antes de cualquier paso | `Read` tool |
| 1 | Confirmar datos del episodio | inline — ver abajo |
| 2 | Diseñar arquitectura | inline — ver abajo |
| 3a | Escribir anchor points | [workflows/03-escribir.md](workflows/03-escribir.md) |
| 3b | Aplicar estilo narrativo | [workflows/03-escribir.md](workflows/03-escribir.md) |
| 4 | Aplicar Tone Master (cargado en Paso 0) | btq-project/SKILL.md §4 |
| 5 | Desarrollar 7 segmentos en detalle | [workflows/04-segmentos.md](workflows/04-segmentos.md) |
| 6 | Revisión de calidad + entrega | [workflows/05-revision.md](workflows/05-revision.md) |

---

## Paso 1 — Leer contexto y confirmar datos del episodio

**Primero:** Leer `btq-project/SKILL.md` sección 7 (Roadmap) para obtener el número de episodio siguiente, referencia cultural y tema — si el usuario no los especificó. Solo preguntar lo que no aparece en el roadmap.

### Datos necesarios

**Obligatorios:** Número EP · Referencia cultural · Título tentativo · Tema central · Frase de cierre TM

**Opcionales:** Fuentes preferidas · Segmento variable · Duración objetivo · Notas específicas

Si falta información, preguntar en **UN solo bloque conversacional**:

> "Para armar el guión necesito confirmar algunos datos. ¿Me confirmas el número de episodio, la referencia cultural y la frase de cierre del personaje que vas a usar?"

### Fuentes de investigación obligatorias (antes de escribir Seg 2)

No limitarse a Wikipedia o redes sociales. Buscar en: blogs especializados del fandom, Reddit (subreddits específicos), Baidu (obras con origen asiático), Facebook communities de fans, entrevistas en medios especializados.

**Por qué:** Andy encontró en Reddit y blogs la historia real del origen de Diarios de la Boticaria que ninguna fuente formal traía completa.

---

## Paso 2 — Diseñar la arquitectura del episodio

Antes de escribir el guión completo, presentar la arquitectura para validación:

```
EP.0XX — [TÍTULO]
Referencia cultural: [personaje/obra]
Tema central: [concepto]

ARQUITECTURA — 7 SEGMENTOS:
1. HOOK            — [gancho sin revelar el personaje]
2. EL PUENTE       — [conexión con operaciones/experiencia]
3. LOS DATOS       — [fuentes y estadísticas, máx. 1 por bloque]
4. MITO O REALIDAD — [3 rondas propuestas]
5. [SEGMENTO VAR.] — [Minuto de Acción / Roles / Consecuencias]
6. CIERRE          — [2 audiencias: líderes → agentes/supervisores]
7. TEASER          — [episodio siguiente] + TM de cierre
```

> **Nota de estructura:** Esta es la arquitectura mínima de 7 segmentos. Para episodios completos
> (EP.012+), agregar según corresponda: Las Lecciones (ancladas en momentos específicos),
> Referencias Cruzadas (mín. 2 de negocios), Aplicable Hoy (3 acciones, 1 permanente),
> Recomendaciones de Andy. Ver btq-project sección 5 para la estructura completa de 10 segmentos.

Esperar confirmación antes de desarrollar.

---

## Paso 4 — Aplicar el Tone Master (TM)

El TM completo está en `btq-project/SKILL.md` sección 4. Puntos críticos:

- **Apertura:** "Buenas y santas. Feliz día, feliz tarde o feliz noche. Cualquier día que éste sea." — NUNCA abreviada
- **Intro:** "Esto es Behind the Queue, episodio [NÚMERO]." — siempre con número
- **Cierre (EP.010+):** "Esto fue Behind the Queue, episodio [NÚMERO]. Yo soy Andy. Y como diría [personaje]: [frase]."
- **Prohibiciones absolutas:** ❌ "obviamente" ❌ "pero bueno" ❌ muletillas ❌ segunda persona en guión propio ❌ anécdotas con nombres

Si al revisar el guión aparece alguna de estas palabras o estructuras, eliminarla antes de entregar.

---

*BTQ Guion Skill v1.4 · Jun 2026 · Reorganizado a workflows — Pasos 3-7 en workflows/*
