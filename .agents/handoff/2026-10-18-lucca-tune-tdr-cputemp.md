# Handoff: Lucca Tune — recuperacion tras TDR, selector de imagen, nubes, temperatura de CPU (0.13.1-0.15.0)
**Date:** 2026-10-18 (domingo)
**Machine:** desktop (E:\) — todo lo instalado y medido vive en el escritorio; desde el portatil no se puede probar contra el hardware
**Status:** In progress — 0.15.0 instalada y en GitHub (`Lucca-Tech/gpu-tuner` @ `d25216e`); sprints 2 y 4 pendientes, CPU TEMP sin ver dentro del servicio
---
## What We Accomplished This Session
- 0.13.1 (`233f4fc`): el 17-oct un TDR (9 resets `nvlddmkm` 153) dejo a NVML con access violations 3 h y la curva de ventiladores APAGADA sin aviso. Ahora NVML se reinicia solo (DriverLost, reintento cada 2 s), el modo elegido vuelve solo (decision de Andres) y un error repetido se anota una vez. Probado con `pnputil /restart-device` sobre el servicio instalado: curva de vuelta en ~5 s. El boton de imagen usa `create_file_dialog` de pywebview (el `<input type=file>` no abria; ninguna imagen habia llegado nunca). Andres subio una imagen: llego.
- 0.14.0 (`1f4d618`): las nubes cruzan la pantalla (bucle de 16 s, ~30 px/s). Andres: "quedaron perfectas".
- 0.15.0 (`d25216e`): casilla CPU TEMP por PawnIO (ya cargado por OpenRGB) + modulo AMDFamily17 (LGPL-2.1, en `gpu_tuner/modules/`). Prueba elevada: 43,4-45,5 C contra 42,7-43,4 C de Ryzen Master.
- Clima: Andres comparo con AccuWeather (17 C) contra 14 C de Lucca; el METAR de El Dorado (medido) daba 14 C: se queda Open-Meteo.
- LIMITE AMPLIADO por Andres: a la bomba se permite la consulta de LECTURA 0x82 (MI_00). Responde ~2.800: no es temperatura (consistente con RPM de la bomba, sin confirmar); decision: no mostrarlo.
- TT RGB Plus: desinstalado (verificado: sin proceso, sin tarea, fuera de Programas).
- Docs al dia: `docs/estado.md` (etapas 0.13.1-0.15, pendientes) y `docs/bitacora.md` (3 entradas del 18-oct). Memoria del proyecto y `reference_pywebview_shaped_window` actualizadas.

## Where We Paused
**Last action:** cierre de sesion (retrospectiva, auditoria del kit sin hallazgos reales, este handoff).
**Next action:** pedirle a Andres que ponga la casilla CPU TEMP en el panel y pase la pantalla a Panel; verificar en el servicio real (registro sin "CPU's temperature is not available", vista previa, numero en el AIO). El servicio corre como SYSTEM: la prueba elevada NO lo cubre.
**Blockers:** sprint 2 (retraso de la placa MSI) bloqueado por hardware: el controlador de luces de la placa (USB 0DB0:0076) no aparece desde el 15-oct 14:31 (LastArrivalDate). Andres debe hacer un apagado completo con la fuente DESCONECTADA antes de la proxima sesion.

## Files to Read First
- `C:\Users\andre\repos\gpu-tuner\docs\estado.md` — estado vigente, etapas, pendientes con su razon, limites (incluye 0x82).
- `C:\Users\andre\repos\gpu-tuner\docs\bitacora.md` — ultimas 3 entradas del 2026-10-18.
- `C:\Users\andre\repos\gpu-tuner\gpu_tuner\cputemp.py` — lectura de CPU por PawnIO.
- Memoria `project_gpu_tuner_lucca.md` — decisiones de Andres y trampas pagadas.

## Notes / Gotchas
- Un TDR se reproduce con `pnputil /restart-device` sobre la 3080 Ti (script en un .ps1 elevado; pantalla negra unos s). Win+Ctrl+Shift+B NO lo reproduce.
- La vista previa de Settings (`/api/screen/preview`) dibuja siempre t=0 del clima: no sirve para ver movimiento; dibujar cuadros con `render_weather(now, t)`.
- PawnIO: tomar el mutex `Global\Access_PCI` antes de `ioctl_read_smn`; formula de k10temp (`(reg 0x59800 >> 21) * 0,125`, -49 si bit 19). El modulo trae escritura de MSR: no usarla.
- Las luces de Andres estan APAGADAS con el interruptor general (`scene.on: false`) por eleccion suya.
- Instalar: `python build.py` + `python build.py installer`, luego un .ps1 con `Start-Process ... -Verb RunAs` (la herramienta PowerShell rechaza los argumentos con comas en linea).
- Resets de la tarjeta: causa desconocida (sin overclock de Lucca activo). Lucca ya se recupera; no los evita.

## Questions to Answer
- ¿Hizo Andres el apagado completo con la fuente desconectada? ¿Aparecio la placa (0DB0:0076) y los leds de la caja?
- Sprint 4 (tema claro / escala != 100 %): necesita aprobacion para cambiar su pantalla temporalmente y restaurar su configuracion exacta.
- Hipotesis sin comprobar: deshabilitar Mystic_Light_Service / MSI_Case_Service el 15-oct pudo hacer que la placa no se inicialice al arrancar.
