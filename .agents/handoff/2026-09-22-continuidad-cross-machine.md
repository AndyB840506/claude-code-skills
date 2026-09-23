# Handoff: Continuidad cross-machine — memoria unificada y arranque automático
**Date:** 2026-09-22 (martes)
**Machine:** desktop (E:\)
**Status:** Complete — scripts arreglados y pusheados; queda UNA comprobación en el portátil

---

## ACTUALIZACIÓN 2026-09-23 (portátil, 09:21 COT)

Verificado en el portátil (sin `E:\`), sesión abierta todavía en `repos\kit-skill-creator`:

| pendiente del 09-22 | estado 09-23 | evidencia |
|---|---|---|
| `Test-Path C:\Users\andre\.claude\skills\.git` | **True** — clon existe, remoto `claude-code-skills`, en `60f2654` | salida del comando |
| `start.ps1` nunca corrido en el portátil | **Corrido.** Continuity estaba 8 atrás → pull a `6650d45`. Memoria: 102 nuevos, 4 actualizados, 0 conservados | salida de `start.ps1` |
| ¿memoria del portátil que el repo no tenga? | **Ninguna.** Slug `repos-kit-skill-creator`: 105 local = 105 repo, 0 solo-local. Slug unificado: 194 local | comparación de nombres |
| Cambiar de ruta a `~/.claude/skills` | **PENDIENTE (Andrés)** — cerrar VS Code y reabrir en `C:\Users\andre\.claude\skills` | — |
| Borrar slugs `C--Users-andre-repos-kit-skill-creator` y `C--Users-andre` del repo de continuity | **PENDIENTE** — desbloqueado en cuanto la primera sesión abra en la ruta nueva y `start.ps1` muestre el slug unificado cargado. Borrar en repo **y** en `~/.claude/projects/` local del portátil, o `sync.ps1` los re-sube | — |
| `install.ps1` sin re-correr entero | **Ya no bloquea**: `start.ps1` cubrió el caso del portátil. Solo importa en una máquina nueva | — |
| `repos\skills` legacy, 3 memorias huérfanas heredadas | Sin decidir | — |

**Next action:** abrir `C:\Users\andre\.claude\skills`, correr `start.ps1` (paso 0), y ahí limpiar los 2 slugs viejos.

### Cierre del mismo día (Andrés: «continúa con todo»)

- **Slugs viejos LIMPIADOS** (continuity `d3c1d4b`). Antes de sacarlos se diffeó contra el
  unificado: 60 de 64 diferencias eran solo CRLF; las 4 reales tenían la versión unificada
  más nueva; `e_drive_absent_post_wipe.md` ya estaba cubierto por `project_two_pcs.md`.
  **2 memorias de `C--Users-andre` no existían en ningún otro slug** —
  `ai-image-gen-exploration`, `feedback-permission-classifier-boundaries`— y se rescataron
  al unificado e indexaron (git las registró como rename 100%). Las carpetas `memory` locales
  se MOVIERON (no borraron) a `~/.claude/projects/_backup-old-slugs-2026-09-23/`.
  `start.ps1` re-corrido: **1 slug, 195 archivos, sin avisos.**
- `btq_production_state` marcada **SUPERADA** (congelada en EP.016; fuente real `roadmap-btq.md`).
- `project_hiresignal_do_deploy` ya estaba marcada HISTÓRICA desde el 09-22.
- **`repos\skills` no existe en el portátil** — vive en el escritorio. Archivarlo queda para allá.
- **Sigue pendiente:** reabrir VS Code en `C:\Users\andre\.claude\skills` (si se sigue abriendo
  `repos\kit-skill-creator`, el harness recrea el slug viejo y `start.ps1` volverá a avisar).
- **`skill_reviewer_integration` → CABLEADA** (Andrés: «agrega a los skills»). Ninguna de las
  dos skills lo tenía. Ahora: `retrospective/workflows/extract-and-apply.md` Step 5 y
  `handoff/workflows/file-handoff.md` paso 7 (este solo si el handoff va suelto, no dentro de
  `/session-close`). Memoria corregida: el skill real es `prompt-reviewer-en` y su modo es
  `quick` ~5 min, no `/prompt-reviewer` «RÁPIDO».

---

## ⚠️ SI ESTA SESIÓN CORRE EN EL PORTÁTIL: HAZ ESTO PRIMERO

La memoria estaba partida en dos slugs y se fusionó hoy en el del escritorio. Para que el
portátil use esa memoria unificada (y deje de crear una paralela), corre:

```powershell
Test-Path C:\Users\andre\.claude\skills\.git
```

| resultado | qué significa | qué hacer |
|---|---|---|
| **True** | el clon ya existe (lo pone `install.ps1` en su paso 4) | Cierra VS Code y **vuelve a abrirlo en `C:\Users\andre\.claude\skills`**. Nada más. A partir de ahí las dos máquinas comparten slug y memoria. |
| **False** | ese clon no se creó nunca en esta máquina | `git clone https://github.com/AndyB840506/claude-code-skills.git C:\Users\andre\.claude\skills` y luego abre esa carpeta. |

Y la primera vez, antes de nada (huevo y gallina: `start.ps1` todavía no está en el portátil):

```powershell
cd C:\Users\andre\repos\claude-continuity
git pull origin master
.\start.ps1
```

De ahí en adelante no hay que invocar nada: el paso 0 del `CLAUDE.md` del kit hace que
Claude corra `start.ps1` solo al arrancar.

**Por qué importa:** Claude Code deriva el slug de memoria de la RUTA del workspace. El
portátil venía abriendo `C:\Users\andre\repos\kit-skill-creator` (nombre elegido en el
bootstrap de junio: *«clone claude-code-skills as the kit-skill-creator workspace»*) y el
escritorio `C:\Users\andre\.claude\skills`. Mismo repo, mismo remoto, **dos memorias que
nunca convergían**. No es diferencia de máquina ni de discos (E:\ vs D:\ es real pero no
tiene que ver): es solo el nombre de la carpeta destino.

**Evidencia:** hoy 15:53 UTC el portátil creó `feedback_verify_screen_before_asking_user.md`
y 15:55 UTC actualizó `project_hiresignal_outreach.md`, ambos bajo
`~/.claude/projects/C--Users-andre-repos-kit-skill-creator/memory/`.

---

## What We Accomplished This Session

- **Corrido `install.ps1`** (era el pedido original, y el handoff del portátil lo exigía
  antes de trabajar el viernes). Antes hubo que hacer `git pull`: el clon local estaba
  **13 commits atrás** y habría restaurado config del 09-10.
- **Detectado y evitado un rollback:** el paso 3 de `install.ps1` iba a pisar el
  `settings.json` del escritorio con el del portátil, que apunta a
  `~/.claude/deploy-preflight-gate.ps1` — archivo que **no existe acá** y que `sync.ps1`
  nunca sube (solo copia `config\hooks\*`). Habría dejado un hook roto en cada llamada de
  Bash y desreferenciado los 4 hooks que sí funcionan. Backup en
  `~/.claude/settings.json.pre-install-2026-09-22.bak`.
- **Memoria fusionada:** 93 archivos del escritorio + 99 del portátil = **192**, índice
  regenerado (192 entradas, 0 huérfanas, 0 duplicados). Los conjuntos eran casi disjuntos:
  solo 4 nombres en común, resueltos por fecha (2 ganó el portátil, 2 el escritorio).
  Backup completo en `~/.claude/projects/_backup-memory-pre-merge-2026-09-22/`.
- **`start.ps1` (NUEVO)** — la mitad que faltaba. `session-close` (paso 5) ya subía memoria
  y config a git, pero **nada las bajaba**: el arranque solo pulleaba el repo de skills. Por
  eso el handoff del portátil tuvo que escribir «corre install.ps1» a mano — el sistema
  compensando con prosa un paso que debía ser automático.
- **`sync.ps1`** — `git pull --rebase --autostash` antes del push (antes pushear sin pull
  hacía que la segunda máquina en cerrar sesión fuera rechazada por non-fast-forward), y
  **dejó de subir `settings.json`**, que es per-máquina.
- **`install.ps1`** — ya no pisa a ciegas: respalda `CLAUDE.md` si difiere y avisa; ya no
  instala `settings.json`. Es el ÚNICO punto del sistema donde algo viejo puede ganarle a
  algo nuevo sin aviso, porque es `Copy-Item -Force` y no git (git da fast-forward o
  conflicto, nunca pisa en silencio).
- **Bug de encoding arreglado:** `install.ps1` **no parseaba en PS 5.1** desde julio. Tenía
  `—` (em dash) dentro de strings en L48/L62; PS 5.1 lee un `.ps1` UTF-8-sin-BOM como cp1252
  y el em dash decodifica a `â€"`, cuya comilla curva PowerShell acepta como **delimitador de
  string**, partiendo la línea. Los 3 scripts quedaron **ASCII puro**, con la razón escrita
  en la cabecera de `start.ps1`. No se había notado porque `sync.ps1` usa `--` y se corre
  siempre; `install.ps1` casi nunca.
- **`CLAUDE.md` del kit:** paso 0 de arranque + regla de abrir siempre la misma ruta.
- **Cierre de sesión (retrospectiva aplicada):** 2 reglas nuevas en el `CLAUDE.md` del kit
  — «git NO preserva mtimes» (§ Instrumentos que mienten) y «un `.ps1` se escribe en ASCII
  puro» (§ Windows — shell) — más la memoria `feedback_go_find_it_dont_reask`. Auditoría del
  kit limpia: 0 colisiones de triggers sobre 31 skills, 0 `SKILL.md` >50 líneas, 0 referencias
  rotas, 31/31 con frontmatter válido.
  **Métricas del cierre:** reproceso por procedencia **2** (los dos detectados antes de
  entregar, ninguno por Andrés); reproceso por iteración ciega **1** — `install.ps1` se
  modificó y **no se volvió a correr**, solo se verificó que parsea.
- **El memory-audit destapó 3 memorias envenenadas por la memoria partida**, todas corregidas:
  una mandaba «editar skills siempre en `kit-skill-creator`» (habría revertido el fix de hoy);
  dos archivos declaraban el mismo `name:` y se contradecían sobre si el portátil tiene
  WhisperX (sí, desde el 2026-09-14, verificado); y una afirmaba que HireSignal «no está
  desplegado» y es de LuccaTech. Esta última llevaba **huérfana del índice desde junio**, así
  que no se cargaba — al indexarla hoy se volvió visible junto con su dato falso.
- **2 bugs del propio kit, arreglados y probados:**
  - `sync.ps1` copiaba sin espejar, así que **ningún borrado se propagaba**: cada
    `memory-audit` que borrara algo lo veía volver en el siguiente `start.ps1`. Ahora espeja,
    pero **sólo si `start.ps1` corrió en las últimas 24 h** (marcador `.config/last-start.txt`,
    gitignored). Sin esa compuerta, una sesión que se saltara `start.ps1` tendría el árbol
    local por detrás del repo y borraría la memoria de la OTRA máquina en vez de la suya.
    Ambas ramas probadas con un archivo señuelo.
  - `session-close` paso 4: `git pull --rebase` sin `--autostash`. Fallo garantizado — ese
    paso corre justo después de editar skills, así que el árbol está sucio por definición.

## Where We Paused

**Last action:** todo pusheado y verificado contra el remoto — continuity `6d4681d`
(194 archivos de memoria, `config/settings.json` retirado, `start.ps1` presente),
kit de skills `e673573`.

**Next action:** correr el `Test-Path` de arriba en el portátil y reportar el resultado.

**Blockers:**
- **`~/.claude/skills` en el portátil: NO VERIFICADO.** No es inspeccionable desde el
  escritorio. Es lo único que falta para cerrar el fix.
- **No borrar todavía `memory/C--Users-andre-repos-kit-skill-creator/`** del repo de
  continuity. Mientras exista, cada `install.ps1` lo replanta y `start.ps1` avisará
  «memoria repartida en 3 slugs» — pero borrarlo **antes** de que el portátil cambie de
  ruta lo dejaría arrancando sin memoria. Limpiar sólo tras confirmar el cambio, junto con
  `C--Users-andre` (3 archivos, de abrir `C:\Users\andre` directo).
- **`start.ps1` nunca se ha corrido en el portátil.** Mirar su salida la primera vez antes
  de ponerse a trabajar.
- **`install.ps1` quedó modificado y NO se volvió a correr entero** — solo se verificó que
  parsea (0 errores en PS 5.1). Los cambios sin ejecutar son los del paso 3: respaldar
  `CLAUDE.md` si difiere y no instalar `settings.json`. Importa porque el portátil es quien
  lo va a correr: si algo falla ahí, es en ese bloque. `start.ps1` cubre el caso normal del
  día a día, así que `install.ps1` sólo hace falta en una máquina nueva.

## Files to Read First

- `claude-continuity/start.ps1` — el script nuevo; su cabecera explica la regla ASCII
- `claude-continuity/sync.ps1` y `install.ps1` — los comentarios dicen qué cambió y por qué
- `~/.claude/skills/CLAUDE.md` § «Comportamiento al iniciar» — el paso 0
- `.agents/handoff/2026-09-22-hiresignal-1516-dkim-manual.md` — el handoff del portátil, con
  el trabajo de HireSignal que vence esta semana (abajo)

## Notes / Gotchas

- **El orden importa: `start.ps1` al inicio, trabajar, `sync.ps1` al cierre.** Los dos se
  neutralizan si se invierten — `start.ps1` restaura a local lo que esté en el repo y no en
  local, así que correrlo DESPUÉS de borrar una memoria la resucita, y el sync posterior no
  tiene nada que espejar. En el flujo normal no pasa, porque el borrado ocurre entre los dos.
  Se descubrió porque la primera prueba del espejado estaba mal diseñada (el señuelo sólo
  vivía en el repo, que es indistinguible de «archivo que subió la otra máquina»): el código
  estaba bien, la prueba no.
- **Git no preserva mtimes.** `start.ps1` NO compara fechas de archivo: un pull estampa
  «ahora» en todo lo que toca y le ganaría a trabajo local genuinamente más nuevo. Compara
  contra la **fecha de commit** del contenido, que es machine-independent, y sólo para
  archivos cuyo hash difiere. Verificado: en su primera corrida conservó los 3 archivos de
  la fusión en vez de pisarlos con la copia del repo.
- **`C:\Users\andre\repos\skills` NO es el segundo clon del kit.** Es otro repo
  (`AndyB840506/skills`), un solo commit de junio: *«Initial commit: handoff, retrospective,
  on-call-handoff-patterns»*. Legacy — conviene archivarlo para que nadie lo confunda.
- En el **escritorio**, el workspace del proyecto y el clon global son la MISMA carpeta, así
  que los dos `git pull` que manda el paso 1 del `CLAUDE.md` son el mismo comando. En el
  portátil eran dos carpetas distintas: de ahí salía el slug divergente.
- La compuerta del script de fusión abortó sin escribir en el primer intento y destapó **3
  memorias del portátil ya huérfanas** desde 2026-06-09 (`btq_production_state`,
  `project_hiresignal_do_deploy`, `skill_reviewer_integration`): estaban en disco pero sin
  línea en `MEMORY.md`, así que no se cargaban nunca. Quedaron indexadas y marcadas
  `[heredada del portatil, sin verificar]` — **no se verificó su contenido**, y
  `project_hiresignal_do_deploy` puede solaparse con `reference_do_app_platform_api`.

## Questions to Answer

- **HireSignal, esta semana** (del handoff del portátil, sin tocar hoy):
  **jueves 24** Send follow-ups de Outreach (TEST A debe recibir `Re:`, C suprimido);
  **viernes 25** follow-up a candidatos de KT-004, vence **20:58 UTC / 15:58 Colombia** —
  hay que activar la campaña, pulsar SÓLO *Send follow-ups* y volver a pausarla (activarla
  habilita «Send to 3» a postulantes REALES: Akshay, Alexander, Santiago). Mismo día,
  recheck de DKIM pasadas las 48 h.
- ¿Archivar/borrar `repos\skills` (el repo legacy)?
- Las 3 memorias huérfanas heredadas: ¿se quedan, se fusionan o se borran? Es trabajo de
  `memory-audit`, no se decidió hoy.
