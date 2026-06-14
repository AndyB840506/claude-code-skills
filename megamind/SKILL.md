---
name: megamind
description: "Master orchestrator skill. Loads project context, detects task complexity, and automatically routes to parallel-workflow for large tasks or handles directly for simple ones. The unified entry point for Claude Megamind. Triggers: /megamind, big task, large task, orchestrate, coordinate agents."
---

# Megamind — Master Orchestrator

The unified entry point for Claude Megamind. Loads workspace context and automatically
routes tasks to the right execution mode.

## What It Does

Carga `project-map` (contexto del workspace) → analiza la complejidad de la tarea →
enruta: tarea simple = la maneja directo; tarea grande = `/parallel-workflow` (multi-agente).

## Workflow

Sigue `workflows/orchestrate.md` — carga `~/.claude/project-map.md` (si no existe,
sugiere `/project-map`), entiende la tarea, evalúa la complejidad y enruta (1 item o
pasos secuenciales = directo; 2+ items independientes = `/parallel-workflow`), luego
ejecuta y sintetiza en un resultado unificado. Incluye la tabla de modos de ejecución.
