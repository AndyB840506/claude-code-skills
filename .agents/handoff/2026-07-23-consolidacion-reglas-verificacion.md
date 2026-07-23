# Handoff: Consolidación de reglas de verificación + skill `verify` global
**Date:** 2026-07-23 (jueves — par fecha/día verificado contra el calendario)
**Machine:** desktop (E:\)
**Status:** Complete en la parte de reglas · 3 builds planeados con decisiones cerradas, **ninguno construido**

> Cuarto handoff del 2026-07-23. Los otros tres: `mpd-t1-cierre-y-auditoria-triggers`,
> `procedencia-causa-raiz`, `hiresignal-outreach-pendiente-fulfillment`.

---

## 1 · Qué pasó

Andrés pegó **12 bloques** (reglas, una skill, y 3 pedidos de construcción) de forma
secuencial. Resultado real, auditado contra los archivos al cierre:

| Estado | Cuántos |
|---|---|
| Aplicados en disco | 9 |
| Rechazados a propósito | 1 (el hook de settings.json) |
| Planeados, sin construir | 3 |

**4 de los 9 quedaron con texto materialmente distinto al pegado**, cada uno con
aprobación explícita en el momento. Los cambios que importan:

- **Círculos concéntricos: veto revertido.** El bloque pegado los prohibía; `btq-production/artwork-general-v3.md` los **EXIGE** (surcos de vinilo, oro #C9A84C). Los vetos ahora son por tipo de asset.
- **`#0A0A0A` dejó de redeclararse** → apunta a la fuente canónica.
- **`## Verify Before Claiming` perdió su contenido** → quedó como puntero. Era la 4ª copia de la misma regla.
- **Cadencia de progreso de 60s → fronteras de etapa.** El harness no tiene timer propio durante una tarea.
- **"cada tarea" → solo no triviales**, para no chocar con el preámbulo Karpathy.

## 2 · Hallazgo principal: `skill-kit-auditor` roto 45 días

La skill **no existe**. Se renombró a `skill-management` el **2026-06-08**, pero el fix
solo tocó los archivos de `session-close` — y el handoff de ese día declaró *"verified
across all 11 AndyB840506 repos"*. Las referencias en los dos `CLAUDE.md` y en
`roadmap-future-proofing.md` quedaron rotas hasta hoy. Se "arregló" otra vez el 06-10,
con el mismo alcance parcial.

Es el caso más limpio del modo de fallo que Andrés quiere eliminar: **una afirmación de
completitud con alcance menor al declarado, que nadie re-verificó.** Arreglado hoy en los
4 sitios vivos; las apariciones en `test-harness/` y handoffs viejos se dejaron como
registro histórico.

## 3 · Reglas nuevas (globales)

- **`~/.claude/CLAUDE.md` regla 14** — ante cualquier "constrúyeme X", grep del kit y de `docs/` ANTES de planear. Motivo: **4 de 4** pedidos de construcción de hoy ya existían (`episode-pipeline` era el orquestador pedido; `03-image-validation.md` media compuerta; `insight` la auditoría de fricción; `memory-audit` el drift auditor).
- **§ Procedencia** — nueva instancia: escribir una regla sobre un dominio sin abrir antes la fuente de ese dominio.
- **§ Procedencia, métrica** — el 07-23 dio 4 reprocesos en la primera sesión y **5 en esta**. La tasa NO bajó. Lo único que mejoró: los de esta sesión los detecté yo antes de entregar, no Andrés.
- **`session-close` paso 1** — reconciliar `lo pegado | dónde quedó | en qué difiere` antes del handoff.

## 4 · Skill `verify` (nueva, global)

`verify/SKILL.md` en la **raíz** del repo (no en `.claude/skills/` — ahí sería
project-scoped y no cargaría en hiresignal, kumatalent ni MPD). 8 reglas: tabla de
evidencia, `Get-Date` real, git status por repo, lectura directa de imágenes con tope de
**2 regeneraciones**, `.Length` en strings con límite, veredicto INCOMPLETE, cierre en dos
secciones (solo tareas no triviales) y una sola lista de palabras prohibidas.

## Where We Paused

**Last action:** `/session-close` en curso — paso 3 (este handoff).
**Next action:** construir los hooks de recibo (`PreToolUse`), que es el único de los 3
pendientes que Andrés aprobó explícitamente como el siguiente.
**Blockers:** ninguno técnico. Ver la advertencia del watcher abajo.

## Files to Read First

- `CLAUDE.md` — todas las secciones nuevas; empezar por `## Artwork` y `## Límites de lo publicable`.
- `verify/SKILL.md` — las 8 reglas, ahora global.
- `.claude/skills/episode-launch/docs/brand-constants.md` § "Dirección de artwork" (**CONGELADA v3**) — **fuente canónica** de artwork BTQ. **NO fue leído completo esta sesión**, solo sus encabezados.
- `episode-pipeline/workflows/03-image-validation.md` — ya contiene media compuerta de assets; leer antes de escribir `verify_assets.py`.

## Notes / Gotchas

- **`PostToolUse` corre DESPUÉS de la herramienta: no puede bloquear nada.** Para impedir un deploy va `PreToolUse` con `permissionDecision: "deny"`. El hook que Andrés pegó además leía `$env:CLAUDE_TOOL_FILE_PATH`, que no existe — el contrato es JSON por stdin. Habría sido un no-op silencioso.
- **Un hook nuevo no se puede probar en la sesión que lo crea** si no había `.claude/settings.json` al arrancar: el watcher no lo carga hasta abrir `/hooks` o reiniciar. Planear la prueba para la sesión siguiente.
- **Control negativo real para la compuerta de assets:** `E:\Podcast\BTQ\EP 22\BTQ Artwork EP 22\BTQ-EP022-COVER-1x1-approved-3000 (pre-pcb-fix backup).png` — es la portada con el patrón PCB que violaba marca. Si la compuerta no la marca, la compuerta no sirve. **Machine-bound: solo existe en el desktop (E:\).**
- **Los píxeles de esquina de EP.022 NO son (10,10,10) exactos** — COVER-16x9 da (14,14,15) y COVER-1x1 da (7,6,6), ambos aprobados y publicados. Una aserción de igualdad estricta reprueba trabajo bueno: usar banda de tolerancia y detectar el (0,0,0) puro.
- **La carpeta de EP 22 tiene backups** (`pre-pcb-fix backup`, `scene-only`). Un glob ingenuo los valida como si fueran entregables: hace falta manifiesto o convención de nombres.
- **Las reglas de artwork viven en 5 sitios** + 1 fantasma (`btq-project/workflows/artwork.md`, no existe). Canónica = `brand-constants.md`.
- **EP.023 no tiene artwork generado** — `E:\Podcast\BTQ` llega hasta EP 22. El guion está listo; no hay grabación, así que no hay transcripción.
- Los transcripts de sesión de este workspace empiezan el **2026-06-25** (117 `.jsonl`): una auditoría de historial no puede llegar más atrás.

## Questions to Answer

- **NEEDS USER INPUT (Andrés + Hugo) — heredado:** plan de fulfillment de HireSignal. Sigue siendo el bloqueo que manda; detalle en `2026-07-23-hiresignal-outreach-pendiente-fulfillment.md`.
- **¿Qué se hace con `frontend-design`?** Es un stub de 1 archivo, declara `license: Complete terms in LICENSE.txt` con ese archivo inexistente, duplica el nombre de un skill bundled de Anthropic, y su territorio ya lo cubren `ui-ux-pro-max` (32 archivos) y `web-page-kit`. Es el único skill sin zona `Triggers:` (1 de 29) y **a propósito**: dársela crearía una colisión a tres bandas. Opciones: borrarlo, o dejarlo documentado como deliberadamente sin triggers.

### Cerradas después de escribir este handoff (2026-07-23, misma sesión)

- ✅ **Slug bug: resuelto, ya estaba arreglado.** `claude-continuity/sync.ps1` líneas 29-31 lo documentan: *"Do NOT recompute Claude's project slug -- the derivation differs from Claude Code's (case + dash handling), so a computed slug silently misses the real folder."* El script enumera las carpetas reales en vez de calcular el slug. Por eso no se podía reproducir.
- ✅ **`docs §4` renombrado** a "prompts de generación **y renders**", con nota de qué ítem es exclusivo del prompt.
- ✅ **`verify` regla 6** ahora tiene la categoría **NO VERIFICABLE** (por construcción), que no fuerza INCOMPLETE pero obliga a listarla en la sección 2.
- ✅ **Zonas `Triggers:`** agregadas a `retrospective` y `ui-ux-pro-max`. Efecto colateral: las colisiones reales del kit pasaron de **2 a 0** (el solapamiento `landing page` ⊂ `create landing page` desapareció al dejar de parsear la lista larga de keywords).

## Next Steps

1. **Construir los hooks de recibo** (`PreToolUse`, aprobado como el siguiente). Diseño: receipts por `session_id`, filtro `if` sobre comandos de deploy/push, `permissionDecision: "deny"` si falta el recibo. **No debe bloquear** deploys de andyfreelancer / kumatalent / MPD, que usan mecanismos distintos.
   ⚠️ **Resolver esta tensión ANTES de construir:** [[feedback_hooks_reactivos]] dice explícitamente que los hooks solo hacen cumplir reglas **mecánicas** y que las de criterio "no son mecanizables — no prometer que un hook va a hacer cumplir una regla de juicio". El hook puede comprobar que *exista* un recibo; no puede comprobar que de verdad verifiqué algo. Enforza el ritual, no la sustancia. Decidir con Andrés si eso igual vale la pena (un recibo falso al menos es un acto deliberado y auditable) o si el esfuerzo va a otro lado.
2. **Compuerta de assets** — `verify_assets.py` + `banned-patterns.json` con alcance por tipo de asset, backfill desde los 9 `pipeline-audit-*.md`. Probar contra EP.022 (debe PASAR) y contra el backup pre-pcb-fix (debe FALLAR).
3. **Capa de wave paralela dentro de `episode-pipeline`** — NO un orquestador nuevo. A/B/E en paralelo; C y D secuenciales porque comparten una sola GPU. Dry-run sobre EP.022 sin escrituras.
4. **Decidir sobre `frontend-design`** (borrar vs documentar) — ver Questions. Es el único cabo suelto de higiene que queda en el kit.
5. **Producción parada, no es meta-trabajo:** BTQ **EP.023** tiene guion desde el 07-21 pero sin artwork generado y sin grabar (`E:\Podcast\BTQ` llega hasta EP 22). MPD **EP.006** (Club de los 27) tiene guion pero sin artwork, sin metadata y sin social — los `artwork-ep0XX.md` solo llegan a EP.005.
