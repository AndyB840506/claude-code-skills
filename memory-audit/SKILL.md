---
name: memory-audit
description: "Periodic memory + skill-kit hygiene — finds duplicate, contradicting, orphaned, or stale memory entries AND corrupted/broken skill files (empty frontmatter, broken workflow/docs references, garbled encoding), proposing fixes before applying. Distinct from /insight (cross-session friction → new rules), /retrospective (single session), and skill-management (structure/maintainability, not corruption). Auto-triggered by session-close when memory grows +15 files OR the skill count changes since the last run; also invocable manually. Triggers: memory audit, clean up memory, memoria contradictoria, memoria desactualizada, revisar memoria, consolidar memoria, teoria de los 3 chiflados, memory hygiene, prune memory, memory cleanup, skill corruption, integridad de skills."
---

# Memory Audit — Higiene de la Memoria y el Skill Kit

Sin limpieza periódica, la memoria acumula redundancia y termina auto-contradiciéndose
("teoría de los 3 chiflados": cada memoria pisando a la otra sin que nadie note el
choque hasta que ya es un enredo). Lo mismo aplica a los archivos de skills — un
`SKILL.md` con frontmatter vacío o una referencia rota a `workflows/` es el mismo
patrón de corrupción, con más blast radius porque algunos skills (`freelance-gig`)
tocan sitios de producción en vivo. Esta skill hace ambas limpiezas juntas.

## Qué hace

- Lee `MEMORY.md` + cada archivo de memoria que indexa en
  `C:\Users\andre\.claude\projects\<workspace>\memory\`.
- Encuentra 5 tipos de problema:
  1. **Duplicados/solapados** — dos o más memorias sobre el mismo hecho.
  2. **Contradicciones** — una memoria afirma X, otra afirma lo contrario.
  3. **Obsoletas (stale)** — la memoria hace una afirmación verificable (un archivo,
     un estado "WIP"/"live", un repo, una fecha límite) que ya no es cierta. Verifica
     una muestra contra el estado real (leer el archivo, `git log`, `curl` a un sitio
     live) — prioriza memorias con afirmaciones de estado/fecha, no preferencias
     durables que no decaen con el tiempo.
  4. **Huérfanas** — entrada en `MEMORY.md` sin archivo, o archivo sin entrada en
     `MEMORY.md`.
  5. **Sobredimensionadas** — archivo de memoria por encima de ~60 líneas
     (ver [[feedback_memory_file_discipline]]). Señal de que se está dejando crecer
     una sola entrada en vez de dividirla en memorias enlazadas.
- Además, escanea el skill kit completo (`Glob **/SKILL.md` — dinámico, cualquier
  skill nuevo entra solo, sin lista fija que mantener) por 3 tipos de corrupción:
  1. **Frontmatter vacío/roto** — `name`/`description` faltantes o vacíos en un
     `SKILL.md`.
  2. **Referencias rotas** — un `workflows/X.md` o `docs/Y.md` que el `SKILL.md`
     menciona pero no existe en disco.
  3. **Texto corrupto** — codificación mangled (ej. "Ã©" en vez de "é") o cortes de
     palabra a mitad. Verificado 2026-07-06: confirmar con `Read`, no con un dump de
     PowerShell — PowerShell puede mostrar mojibake que no existe en el archivo real.
  Prioridad de verificación: skills que tocan producción en vivo (`freelance-gig` →
  `the-freelancer` repo / andyfreelancer.com) — si su contenido no coincide con el
  estado real del repo, es un hallazgo, no solo una nota.
- Para cada hallazgo: muestra la evidencia y propone UNA resolución concreta (fusionar,
  corregir, archivar, o vincular) — nunca borra nada sin mostrarlo primero.
- Aplica solo lo aprobado, actualiza `MEMORY.md` en el mismo paso, y refresca el
  contador de línea base (`memory/.audit-baseline.json`).

## Cómo se distingue

- `/retrospective` — extrae aprendizajes de **una** sesión.
- `/insight` — busca fricción que se repite **entre** sesiones para proponer reglas
  nuevas. Mira handoffs + memoria, pero no audita la memoria en sí.
- `/session-close` — el ritual de cierre de cada sesión.
- `skill-management` — checklist de **estructura/mantenibilidad** de un skill (líneas,
  triggers, organización de carpetas). No busca corrupción — eso es este skill.
- `/memory-audit` — limpieza de lo que YA existe en memoria Y corrupción en el skill
  kit: duplicados, contradicciones, obsolescencia, frontmatter roto, referencias
  rotas. No extrae aprendizajes nuevos, no propone reglas ni reorganiza estructura —
  consolida y repara lo que ya hay.

## Cuándo corre

- **Automático:** `session-close` lo dispara solo (sin preguntar si correrlo o no)
  cuando el conteo de archivos de memoria creció ≥15 desde `memory/.audit-baseline.json`,
  **o** cuando el conteo de `SKILL.md` en el kit cambió desde la última corrida —
  ver `session-close/INSTRUCTIONS.md` Paso 5. Costo cero mientras no cierres sesión:
  el umbral vive dentro de session-close, no es un job de fondo independiente. El
  disparo es automático; lo que sigue pidiendo aprobación explícita es aplicar los
  cambios (ver Reglas abajo).
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
