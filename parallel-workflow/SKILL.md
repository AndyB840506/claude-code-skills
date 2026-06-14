---
name: parallel-workflow
description: "Breaks a large task into independent subtasks and runs them in parallel using multiple subagents. Synthesizes results into a single final output. Triggers: /parallel-workflow, /pw, run in parallel, parallelize this, break into subtasks, run simultaneously."
---

# Parallel Workflow — Multi-Agent Task Executor

Splits any large task into independent subtasks and runs them simultaneously using
parallel subagents. Results are collected and synthesized into one final output.

## When to Use

- Auditing multiple files or repos at once
- Generating assets for multiple items (episodes, pages, products)
- Running the same analysis across different inputs
- Any task with N independent units of work

## Workflow

Sigue `workflows/execute.md` — decompón la tarea en subtasks independientes, lanza N
agentes en paralelo (un solo mensaje, `run_in_background: true` en cada uno), recolecta
y sintetiza en una respuesta unificada.

## Reglas críticas

- Nunca correr agentes en secuencia cuando pueden ir en paralelo.
- Máximo recomendado: 10 agentes en paralelo (más → dividir en batches).
- Confirmar el plan de decomposición con el usuario antes de lanzar.
