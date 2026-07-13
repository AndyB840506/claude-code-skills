---
name: memory-audit
description: "Periodic memory + skill-kit hygiene — finds duplicate, contradicting, orphaned, or stale memory entries AND corrupted/broken skill files (empty frontmatter, broken workflow/docs references, garbled encoding), proposing fixes before applying. Distinct from /insight (cross-session friction → new rules), /retrospective (single session), and skill-management (structure/maintainability, not corruption). Auto-triggered by session-close when memory grows +15 files OR the skill count changes since the last run; also invocable manually. Triggers: memory audit, clean up memory, memoria contradictoria, memoria desactualizada, revisar memoria, consolidar memoria, teoria de los 3 chiflados, memory hygiene, prune memory, memory cleanup, skill corruption, integridad de skills."
---

# Memory Audit — Higiene de la Memoria y el Skill Kit

Sin limpieza periódica, la memoria acumula redundancia y termina auto-contradiciéndose
("teoría de los 3 chiflados"). Lo mismo aplica a los skills — frontmatter vacío o
referencias rotas a `workflows/` son el mismo patrón de corrupción, con más blast
radius porque algunos skills (`freelance-gig`) tocan producción en vivo. Esta skill
hace ambas limpiezas juntas.

## Qué hace

- Lee `MEMORY.md` + cada archivo de memoria en
  `C:\Users\andre\.claude\projects\<workspace>\memory\`, y busca 5 tipos de problema:
  duplicados/solapados, contradicciones, obsoletas (afirmación verificable que ya no es
  cierta), huérfanas (índice ↔ archivo desalineados), y sobredimensionadas (>60 líneas,
  ver [[feedback_memory_file_discipline]]).
- Escanea también el skill kit completo (`Glob **/SKILL.md`, dinámico) por 3 tipos de
  corrupción: frontmatter vacío/roto, referencias rotas a `workflows/`/`docs/`, y texto
  corrupto. Prioridad de verificación real: skills que tocan producción en vivo
  (`freelance-gig` → `the-freelancer`/andyfreelancer.com).
- Para cada hallazgo: muestra la evidencia y propone UNA resolución concreta — nunca
  borra nada sin mostrarlo primero. Detalle completo de cada paso en `workflows/audit.md`.
- Aplica solo lo aprobado, actualiza `MEMORY.md` en el mismo paso, y refresca el
  contador de línea base (`memory/.audit-baseline.json`).

## Cómo se distingue

`/retrospective` = una sesión. `/insight` = fricción cross-sesión → reglas nuevas.
`skill-management` = estructura/mantenibilidad de un skill (líneas, triggers), no
corrupción. `/memory-audit` = limpieza de lo que YA existe en memoria + corrupción en
el skill kit — no extrae aprendizajes nuevos ni reorganiza estructura.

## Cuándo corre

- **Automático:** `session-close` lo dispara solo cuando memoria creció ≥15 archivos
  desde `memory/.audit-baseline.json` **o** el conteo de `SKILL.md` cambió — ver
  `session-close/INSTRUCTIONS.md` Paso 5. Costo cero fuera de session-close (no es un
  job de fondo). El disparo es automático; aplicar cambios sigue pidiendo aprobación.
- **Manual:** invocable en cualquier momento con `/memory-audit`.

## Workflow

Sigue `workflows/audit.md` — inventario → detectar → verificar muestra → proponer →
aplicar → actualizar línea base. Reglas de aprobación (nunca tocar sin aprobar, preferir
fusionar sobre borrar, verificar antes de marcar obsoleta) viven en el Paso 4 de ese archivo.
