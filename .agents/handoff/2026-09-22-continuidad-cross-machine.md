# Handoff: Continuidad cross-machine — memoria unificada y arranque automático
**Date:** 2026-09-22 (martes)
**Machine:** desktop (E:\)
**Status:** Complete — scripts arreglados y pusheados; queda UNA comprobación en el portátil

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

## Files to Read First

- `claude-continuity/start.ps1` — el script nuevo; su cabecera explica la regla ASCII
- `claude-continuity/sync.ps1` y `install.ps1` — los comentarios dicen qué cambió y por qué
- `~/.claude/skills/CLAUDE.md` § «Comportamiento al iniciar» — el paso 0
- `.agents/handoff/2026-09-22-hiresignal-1516-dkim-manual.md` — el handoff del portátil, con
  el trabajo de HireSignal que vence esta semana (abajo)

## Notes / Gotchas

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
