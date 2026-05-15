# Pasos 3–5: Crear, Confirmar e Instalar

## Paso 3 — Escribir la Skill

Genero el archivo `.md` con estructura clara:

```markdown
---
name: nombre-en-kebab-case
description: "Descripción + triggers variados (5+ frases)"
---

# Nombre de la Skill

Párrafo de bienvenida.

## Paso 1 — [Recoger Datos]

Instrucciones para este paso.

## Paso 2 — [Procesar]

Lógica principal.

## Paso 3 — [Generar Output]

Qué crea y formato.
```

Reglas:
- Frontmatter con `name` (kebab-case) y `description` (5+ triggers)
- Secciones numeradas con pasos claros
- Ejemplos concretos
- Lenguaje imperativo (haz, pregunta, genera)

## Paso 4 — Pedir Confirmación

CRÍTICO: Antes de guardar, pregunto explícitamente:

```
¿Quieres que guarde esta skill?

Skill: [nombre-skill]
Ubicación: .claude/skills/[nombre-skill]/SKILL.md

- "sí" / "yes" — Guardar la skill
- "no" — No guardar, quiero revisar
- "cambiar X" — Cambiar algo antes
```

**Espero respuesta explícita. No guardo sin aprobación.**

## Paso 5 — Instalar

Una vez aprobada, creo la estructura:

```bash
mkdir -p .claude/skills/nombre-skill
# Guardo el contenido en SKILL.md
```

**Regla importante:** Todas las skills van en carpeta, nunca como archivo suelto:

```
.claude/skills/
├── nombre-skill/
│   └── SKILL.md    ← Siempre así
```

Si es grande, uso estructura de carpetas:

```
.claude/skills/nombre-skill/
├── SKILL.md        (router <50 líneas)
├── workflows/      (procedimientos)
└── docs/           (referencias)
```

Resultado: La skill queda lista para usar automáticamente.
