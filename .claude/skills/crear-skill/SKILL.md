---
name: crear-skill
description: "Crea skills de Claude Code personalizadas para este workspace. Usar cuando el usuario trabaja directamente en este kit. Triggers ES: quiero una skill nueva, diseñar una skill, hacer una skill aquí, crear skill en este proyecto, skill desde cero, construir una skill, nueva skill para el kit, convertir esto en skill, hacer esto automático, quiero automatizar un proceso. Triggers EN: create skill for this project, skill from scratch, build a skill here, new skill for this workspace, add skill to kit, make this into a skill."
---

# Crear Skill — Crea tus propias skills

Le describes un proceso que quieres automatizar y Claude genera una skill completa
lista para usar. Es la herramienta que crea herramientas.

Las skills de Claude Code son archivos `.md` que le enseñan a Claude a hacer tareas
específicas. Cualquier proceso que hagas de forma repetitiva puede convertirse en
una skill.

## EXECUTION — Pasos 1–7

- [Paso 1: Entender](workflows/understand.md) — preguntas clave, ideas por industria, kits similares
- [Paso 2: Diseñar](workflows/design.md) — Planifica input, proceso, output
- [Pasos 3–5: Crear e Instalar](workflows/create-install.md) — Genero el `.md`, confirmo, instalo
- [Pasos 6–7: Test y Presentación](workflows/test-present.md) — Verifico y presento resultado

Si el usuario ya describió lo que quiere, procede directamente al Paso 2.

## Reference

- `docs/design-principles.md` — 10+ principios de buenas skills
- `docs/execution-guide-es.md` — plantillas para secciones `## EXECUTION`
- `docs/conventions.md` — idioma, dónde se guardan las skills, distinción con
  skill-creator, regla de entrega mínima, ejemplo de uso
