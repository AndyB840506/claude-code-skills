---
name: crear-skill
description: "Crea skills de Claude Code personalizadas para este workspace. Usar cuando el usuario trabaja directamente en este kit. Triggers ES: quiero una skill nueva, diseñar una skill, hacer una skill aquí, crear skill en este proyecto, skill desde cero, construir una skill, nueva skill para el kit, convertir esto en skill, hacer esto automático, quiero automatizar un proceso. Triggers EN: create skill for this project, skill from scratch, build a skill here, new skill for this workspace, add skill to kit, make this into a skill."
---

# Crear Skill — Crea tus propias skills

Le describes un proceso que quieres automatizar y Claude genera una skill completa lista para usar. Es la herramienta que crea herramientas.

Las skills de Claude Code son archivos `.md` que le enseñan a Claude a hacer tareas específicas. Cualquier proceso que hagas de forma repetitiva puede convertirse en una skill.

---

## EXECUTION

## Paso 1 — Entender qué necesita el usuario

Pregunta de forma conversacional (no como formulario). Si el usuario ya describió lo que quiere, procede directamente al Paso 2.

**Preguntas clave (en un solo bloque):**
- **¿En qué idioma?** — Español, English, o bilingüe
- **¿Qué quieres automatizar?** — Describe el proceso o resultado esperado
- **¿Es de propósito general o específico para un tipo?** — Evita asumir scope
- **¿Qué información necesita?** — URL, texto, carpeta, archivo, API...
- **¿Qué debe generar?** — HTML, código, informe, archivo, dashboard...
- **¿Quién la usa?** — Solo tú, tu equipo, o la compartes públicamente
- **¿Cómo se publica/despliega el output?** — Especialmente si genera HTML o apps

**Si el usuario menciona un kit similar:** leer ese kit primero antes de diseñar. Ver [workflows/understand.md](workflows/understand.md) para el procedimiento.

Si no sabe qué crear, propón ideas por industria: ver [workflows/understand.md](workflows/understand.md).

**Output:** Entender el proceso a automatizar. Con eso, ir al Paso 2.

---

## Pasos 2–7 (ver workflows)

- [Paso 2: Diseñar](workflows/design.md) — Planifica input, proceso, output
- [Pasos 3–5: Crear e Instalar](workflows/create-install.md) — Genero el `.md`, confirmo, instalo
- [Pasos 6–7: Test y Presentación](workflows/test-present.md) — Verifico y presento resultado
- [Principios de Diseño](docs/design-principles.md) — 10+ principios de buenas skills

---

## Ejemplo

```
/crear-skill

"Quiero una skill que lea un CSV de productos 
y genere fichas de producto en HTML"

↓ 

Creo la skill completa → Te pido confirmación → 
La instalo → Listo para usar
```

---

## Idioma

Puedes crear skills en:
- **Español** — para uso personal o equipo hispanohablante
- **English** — para compartir globalmente

---

## Dónde se Guardan

Todas las skills van en:
```
.claude/skills/nombre-skill/SKILL.md
```

Si es muy grande, se organiza con carpetas:
```
.claude/skills/nombre-skill/
├── SKILL.md (router)
├── workflows/ (procedimientos)
└── docs/ (referencias)
```

---

## Distinción con skill-creator

- **`/crear-skill`** — Esta skill. Para uso dentro de este workspace. Instrucciones en español.
- **`/skill-creator`** — Versión en inglés, para crear skills genéricas o compartibles globalmente.

---

## Secciones de EJECUCIÓN

Toda skill necesita una sección `## EXECUTION` con instrucciones explícitas para que realmente funcione. Ver [Guía de EXECUTION](docs/execution-guide-es.md) para plantillas y ejemplos detallados.

**Incluye secciones EXECUTION en toda skill que generes.** Esto es lo que hace que las skills realmente funcionen.
