---
name: megamind
description: "Fallback orchestrator for ad-hoc tasks with no dedicated skill, or tasks spanning 2+ independent repos/projects. Loads project-map context, assesses complexity, and routes to parallel-workflow for independent multi-item work or handles directly otherwise. Do NOT use when a named domain skill already covers the task (e.g. episode-launch, freelance-gig, web-page-kit, episode-pipeline) — invoke that skill directly instead. Triggers: /megamind, audit all repos, multi-repo task, orchestrate across projects, no skill fits this, coordinate agents."
---

# Megamind — Master Orchestrator

Fallback entry point for tasks that don't already have a dedicated skill, or that
span 2+ independent repos/projects. Loads workspace context and routes to the right
execution mode. Named skills always take priority — megamind is the catch-all, not
the default front door.

## What It Does

Chequea si hay un skill nombrado que ya cubre la tarea (si lo hay, usarlo directo) →
carga `project-map` (contexto del workspace) → analiza la complejidad → enruta: tarea
simple = la maneja directo; tarea grande = `/parallel-workflow` (multi-agente).

## Workflow

Sigue `workflows/orchestrate.md` — primero chequea si un skill nombrado ya cubre la
tarea (si sí, usarlo directo y parar ahí); si no, carga `~/.claude/project-map.md`
(con chequeo de antigüedad — si tiene más de 14 días, avisar antes de confiar en
él), entiende la tarea, evalúa la complejidad y enruta (1 item o pasos secuenciales
= directo; 2+ items independientes = `/parallel-workflow`), luego ejecuta y
sintetiza en un resultado unificado. Incluye la tabla de modos de ejecución.
