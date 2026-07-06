---
name: memory-audit
description: "Periodic memory hygiene — finds duplicate, contradicting, orphaned, or stale entries in the auto-memory system (MEMORY.md + individual files) and proposes consolidation before applying. Distinct from /insight (cross-session friction → new rules) and /retrospective (single session). Auto-triggered by session-close when memory grows +15 files since the last run; also invocable manually. Triggers: memory audit, clean up memory, memoria contradictoria, memoria desactualizada, revisar memoria, consolidar memoria, teoria de los 3 chiflados, memory hygiene, prune memory, memory cleanup."
---

# Memory Audit — Higiene de la Memoria

Sin limpieza periódica, la memoria acumula redundancia y termina auto-contradiciéndose
("teoría de los 3 chiflados": cada memoria pisando a la otra sin que nadie note el
choque hasta que ya es un enredo). Esta skill hace la limpieza que ninguna otra hace.

## Qué hace

- Lee `MEMORY.md` + cada archivo de memoria que indexa en
  `C:\Users\andre\.claude\projects\<workspace>\memory\`.
- Encuentra 4 tipos de problema:
  1. **Duplicados/solapados** — dos o más memorias sobre el mismo hecho.
  2. **Contradicciones** — una memoria afirma X, otra afirma lo contrario.
  3. **Obsoletas (stale)** — la memoria hace una afirmación verificable (un archivo,
     un estado "WIP"/"live", un repo, una fecha límite) que ya no es cierta. Verifica
     una muestra contra el estado real (leer el archivo, `git log`, `curl` a un sitio
     live) — prioriza memorias con afirmaciones de estado/fecha, no preferencias
     durables que no decaen con el tiempo.
  4. **Huérfanas** — entrada en `MEMORY.md` sin archivo, o archivo sin entrada en
     `MEMORY.md`.
- Para cada hallazgo: muestra la evidencia y propone UNA resolución concreta (fusionar,
  corregir, archivar, o vincular) — nunca borra nada sin mostrarlo primero.
- Aplica solo lo aprobado, actualiza `MEMORY.md` en el mismo paso, y refresca el
  contador de línea base (`memory/.audit-baseline.json`).

## Cómo se distingue

- `/retrospective` — extrae aprendizajes de **una** sesión.
- `/insight` — busca fricción que se repite **entre** sesiones para proponer reglas
  nuevas. Mira handoffs + memoria, pero no audita la memoria en sí.
- `/session-close` — el ritual de cierre de cada sesión.
- `/memory-audit` — limpieza de lo que YA existe en memoria: duplicados,
  contradicciones, obsolescencia. No extrae aprendizajes nuevos, no propone reglas —
  consolida lo que ya hay.

## Cuándo corre

- **Automático:** `session-close` lo dispara solo (sin preguntar si correrlo o no)
  cuando el conteo de archivos de memoria creció ≥15 desde `memory/.audit-baseline.json`
  — ver `session-close/INSTRUCTIONS.md` Paso 4.5. El disparo es automático; lo que
  sigue pidiendo aprobación explícita es aplicar los cambios (ver Reglas abajo).
- **Manual:** invocable en cualquier momento con `/memory-audit`.

## Workflow

Sigue `workflows/audit.md` — inventario → detectar → verificar muestra → proponer →
aplicar → actualizar línea base.

## Rules

- **El disparo de la auditoría es automático; aplicar cambios NO lo es** — inventariar,
  detectar y verificar corren sin pedir permiso; fusionar/corregir/eliminar un archivo
  de memoria siempre se presenta como propuesta y espera aprobación explícita antes de
  tocar el archivo.
- **Verificar, no asumir obsolescencia** — antes de marcar una memoria como stale,
  comprobar contra el estado real (archivo/repo/sitio), no solo por antigüedad de fecha.
- **Preferir fusionar sobre borrar** — si dos memorias sobre el mismo tema no se
  contradicen, fusiónalas en una sola entrada más completa en vez de eliminar la más
  vieja sin más.
- **Actualizar MEMORY.md en el mismo paso** — cualquier cambio a un archivo de memoria
  debe reflejarse de inmediato en su línea del índice.
