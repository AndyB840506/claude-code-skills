# Handoff: Router Mitrastar — puertos para Destiny 2 (sin Tampermonkey)

**Date:** 2026-10-12 (lunes, verificado con `Get-Date`)
**Machine:** desktop (E:\) — DESKTOP-UMEGKH1
**Status:** Complete — puertos abiertos y confirmados por Andy; queda un tema abierto con ExitLag

---

## What We Accomplished This Session

- **Pedido inicial "tampermonkey" → la meta real era abrir un puerto para Destiny 2.** Se
  resolvió sin userscript: tras el login normal del router, la página
  `https://192.168.1.1:8000/cgi-bin/applications.cgi` ("Puertos") carga aunque el menú de
  Colombia no la muestre.
- **Dos reglas agregadas en el router** y releídas en su tabla después de guardar:
  `Destiny2-3074 | UDP | 192.168.1.6 | 3074→3074 | Yes` y
  `Destiny2-3097 | UDP | 192.168.1.6 | 3097→3097 | Yes`. Las 9 reglas previas quedaron
  intactas. Lista de puertos tomada del artículo de ayuda de Bungie (PC: solo UDP 3074 y 3097).
- **Andy confirmó en el juego que funcionó** (el NAT ya no sale moderado sin ExitLag).
- **Sin CGNAT ese día:** IP WAN del router = IP pública (comparadas).
- **Memoria del router corregida** (`reference_router_movistar_mitrastar.md`): el modelo leído
  hoy es `GPT-2841GX2X2v10`, firmware `GL_g0.0_100AVR0b7`, no el GPT-2741GNAC anotado en julio.
- **Retrospectiva aplicada (3 cambios):** viñeta nueva en `CLAUDE.md` § Windows — shell (Git
  Bash convierte argumentos que empiezan con `/`; `MSYS_NO_PATHCONV=1`), memoria nueva
  `feedback_ask_goal_behind_tool_request.md`, y línea nueva en
  `feedback_always_backup_github.md` (carpeta nueva en `repos\` se sube en el mismo cierre).

## Where We Paused

**Last action:** explicarle a Andy por qué ExitLag le da NAT estricto, y cerrar sesión.
**Next action:** ninguna obligatoria. Si Andy vuelve con el tema: ver "Questions to Answer".
**Blockers:** ninguno.

## Files to Read First

- `~/.claude/projects/c--Users-andre--claude-skills/memory/reference_router_movistar_mitrastar.md`
  — modelo real, URL de puertos, reglas agregadas, riesgo de la IP por DHCP.

## Notes / Gotchas

- **`C:\Users\andre\repos\userscripts\` NO existe en el escritorio.** Se creó en el portátil
  el 2026-07-26, nunca fue repo git. Si sigue en el portátil — NO VERIFICADO — conviene
  `git init` + push desde allá (machine-bound: portátil). No hizo falta para el objetivo de hoy.
- **El PC recibe `192.168.1.6` por DHCP, sin reserva.** Si el router le da otra IP, las dos
  reglas apuntan a otro equipo y el NAT vuelve a moderado sin aviso. La interfaz básica no
  tiene reserva de IP; no se buscó en la avanzada.
- **UPnP quedó encendido** junto con las reglas manuales. Bungie no recomienda las dos cosas
  a la vez; funcionó así, no se tocó.
- **`logIn_soporte.cgi` es otro login** (no acepta la contraseña normal) y no hace falta: con
  el login normal (`logIn_mhs.cgi`) también abre la interfaz avanzada (`indexmain.cgi`).
- **Mecánica del router, por si hay que volver a leerlo por script:** el login manda
  `md5(contraseña + ":" + sid)` con el `sid` que viene en la propia página; los archivos
  estáticos devuelven 403 "You must supply a local referer" sin cabecera Referer; la tabla de
  reglas viene en la variable `parsePortMapping` de `applications.cgi`.
- **La contraseña del router NO se guardó** en este handoff ni en memoria. Los scripts de la
  sesión vivían en el scratchpad temporal y la leían de una variable de entorno.

## Questions to Answer

- **ExitLag + Destiny 2 = NAT estricto.** Explicación dada (no medida en el equipo): ExitLag
  saca el tráfico por sus servidores, así que el NAT lo define ese servidor y los puertos del
  router quedan fuera del camino. Opciones propuestas: jugar Destiny sin ExitLag, probar otra
  ruta/región en ExitLag, o preguntar a su soporte. Falta saber por qué Andy usa ExitLag
  (qué síntoma ve sin el programa).
- **¿Reservar la IP del PC?** Ofrecido dos veces, sin respuesta.
- **¿Cambiaron el router o la nota de julio estaba mal?** No determinado.
