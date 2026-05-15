---
name: crear-skill
description: "Asiste al usuario para crear sus propias skills de Claude Code personalizadas en español o inglés, automatizar flujos de trabajo, crear comandos o convertir procesos manuales en automáticos. Triggers: 'crea una skill', 'quiero una skill', 'skill personalizada', 'automatizar esto como skill', 'crear comando Claude Code', 'convertir en skill', 'hacer esto automático'."
---

# Crear Skill — Crea tus propias skills

Le describes un proceso que quieres automatizar y Claude genera una skill completa lista para usar. Es la herramienta que crea herramientas.

Las skills de Claude Code son archivos `.md` que le enseñan a Claude a hacer tareas específicas. Cualquier proceso que hagas de forma repetitiva puede convertirse en una skill.

---

## Flujo de Creación

1. **Entender** — ¿Qué quieres automatizar?
2. **Diseñar** — Planifica input, proceso, output
3. **Escribir** — Genero la skill en `.md`
4. **Confirmar** — ¿Quieres que la guarde?
5. **Instalar** — La skill queda lista en `.claude/skills/`
6. **Testear** — Verificamos que funciona
7. **Presentar** — Resumen de lo generado

---

## Quick Links

- [Paso 1: Entender](workflows/understand.md) — Qué necesitas
- [Paso 2: Diseñar](workflows/design.md) — Estructura de la skill
- [Paso 3-5: Crear e Instalar](workflows/create-install.md) — Genero y guardo
- [Paso 6-7: Test y Presentación](workflows/test-present.md) — Verifico y presento
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
