# Handoff: Lucca Tune — offline tras actualizacion del driver NVIDIA (0.15.1)
**Date:** 2026-10-21 (miercoles)
**Machine:** desktop (E:\) — todo lo instalado y medido vive en el escritorio; desde el portatil no se puede probar contra el hardware
**Status:** In progress — 0.15.1 instalada y en GitHub (`Lucca-Tech/gpu-tuner` @ `25993ee`); siguiente: apagado en frio de Andres para la placa MSI
---
## What We Accomplished This Session
- Diagnostico: a las 10:09:28 Windows instalo el driver NVIDIA 621.01 (UserPnp 20003, SIN evento nvlddmkm 153: no fue TDR); 1 s despues NVML dio access violation y el servicio quedo colgado (API en timeout, ~100 % de un nucleo, 33 CLOSE_WAIT). Mismo patron el 2026-10-07 07:50 (instalacion + ~6 min de errores). El 17-oct si fueron TDR, sin instalacion.
- Pila con py-spy elevado (antes de reiniciar): hilo del ticker en `_reconnect -> nvmlShutdown`, nativo `nvmlShutdown -> SwitchToThread` girando para siempre con el candado de NvmlBackend tomado.
- 0.15.1 (`25993ee`): `NvmlBackend.stuck()` sin candado (perdido 30 s sin una llamada que funcione), vigilante en el servicio que hace `os._exit(1)`, recuperacion del servicio en el instalador (`sc failure` 5/10/30 s, cuenta a cero al dia), `open_when_ready` para arrancar a mitad de una instalacion; prueba en vivo vs nvidia-smi lee "28.00" (621.01). 188 pruebas (182 + 6), 4/4 mutaciones cazadas.
- Servicio real: proceso matado -> Windows lo relanzo en ~5 s con la curva; `pnputil /restart-device` -> el vigilante salto a los 32 s, curva de vuelta a los ~43 s.
- Docs: `docs/estado.md` (fila 0.15 + 2 pendientes nuevos) y `docs/bitacora.md` (entrada 2026-10-21). Memoria: trampa "actualizacion != TDR" en `project_gpu_tuner_lucca.md`; nueva `reference_pyspy_hung_service.md`; CLAUDE.md del kit: viñeta UTF-16 de un powershell.exe aparte.

## Where We Paused
**Last action:** Andres eligio la opcion 3 (placa MSI) y se le dieron los pasos del apagado en frio; cierre de sesion.
**Next action:** cuando Andres vuelva tras el apagado con la fuente DESCONECTADA: comprobar USB `0DB0:0076` presente (`Get-PnpDevice -PresentOnly`, LastArrivalDate), que OpenRGB lo vea (puerto 6742), que `/api/state` traiga `others` no nulo, y que Andres CONFIRME a ojo los leds de la caja. Si pasa, sprint 2 (retraso de ~1 s de la placa en las animaciones).
**Blockers:** el apagado en frio lo hace Andres (no hecho al cerrar: "No todavia").

## Files to Read First
- `C:\Users\andre\repos\gpu-tuner\docs\estado.md` — etapas, pendientes con su razon (incluye TDR ~43 s con 621.01 y la anomalia de las 10:18), limites.
- `C:\Users\andre\repos\gpu-tuner\docs\bitacora.md` — entrada 2026-10-21 con todas las mediciones.
- `C:\Users\andre\repos\gpu-tuner\gpu_tuner\nvml.py` y `gpu_tuner_service.py` — vigilante y `stuck()`.
- Memoria `project_gpu_tuner_lucca.md`.

## Notes / Gotchas
- Una actualizacion del driver NO se reproduce con `pnputil /restart-device` (no cambia nvml.dll). La 0.15.1 solo se confirma de verdad en la proxima actualizacion real de NVIDIA.
- Con el driver 621.01 un TDR ya no se recupera dentro del proceso (el 18-oct, con 617.14, en ~5 s). Sospecha sin medir: `nvmlShutdown` colgado otra vez. Para medirlo: py-spy elevado durante un `pnputil /restart-device` (pantalla negra unos s).
- Contador de fallos del servicio: hoy ya van 2 (pruebas 10:33 y 10:34); el 3.º y siguientes esperan 30 s. Se pone a cero a las 24 h sin fallos.
- Anomalia sin causa: el servicio relanzado a mano a las 10:18 anoto "restored: True" con la curva pero la API daba `mode off` con valores de fabrica, ventiladores fijos 67/67/53 %. No se repitio en 3 arranques posteriores.
- Hipotesis sin comprobar para la placa: deshabilitar `Mystic_Light_Service` / `MSI_Case_Service` el 15-oct (ultima llegada del USB ese dia). No tocarlos sin preguntar: `MSI_Case_Service` reescribia la placa.
- Pruebas elevadas: `.ps1` con `Start-Process powershell.exe -Verb RunAs -Wait`; su salida redirigida sale UTF-16LE.

## Questions to Answer
- ¿Aparecio la placa (0DB0:0076) y los leds de la caja tras el apagado en frio?
- ¿Medir ya por que el TDR no vuelve dentro del proceso con el 621.01 (opcion 1), o esperar?
- Pendiente del handoff 2026-10-18 aun abierto: CPU TEMP dentro del servicio (Andres pone la casilla en el panel).
- Sprint 4 (tema claro / escala != 100 %): necesita aprobacion para cambiar su pantalla temporalmente.
