# Handoff: Lucca Tune — la placa MSI anima sola (0.16.0, sin ver por Andres)
**Date:** 2026-10-21 (miercoles)
**Machine:** desktop (E:\) — todo lo instalado y medido vive en el escritorio; desde el portatil no se puede probar contra la placa
**Status:** In progress — 0.16.0 instalada y en GitHub (`Lucca-Tech/gpu-tuner` @ `5ddb526`); falta que Andres mire las animaciones
---
## What We Accomplished This Session
- Placa MSI (USB 0DB0:0076) de vuelta: un arranque fallo con "Device Descriptor Request Failed" en Port_#0015 (pnputil no lo arreglo); volvio tras reasentar el cable al header USB 2.0 interno con la fuente desconectada.
- Sprint 2 (retraso de la placa) diagnosticado: la placa se para 5,0 s cada ~190 informes HID (error 121 = limite de Windows), a 2-20 por segundo, sin LEDs (JARGB 3 a 0), con MSI Center parado, con lecturas 0x50/0x51 intercaladas. Es el firmware, no el hub ARGB (SATA, sin controles; todo menos la grafica cuelga de el).
- 0.15.2 (`46ae372`): con OpenRGB 1.0 (protocolo 6, ACK) un cuadro a la vez, gana el mas nuevo, sin cola tras las paradas. Andres: la animacion corre, se congela, sigue; cambios de color bien.
- Efecto propio de la placa por informe 0x50 (formato del issue #5955 de OpenRGB): fila JARGB 3 en respiracion -> Andres: continua, todos los ventiladores, AIO incluido. Restaurado al original (3 lecturas iguales).
- 0.16.0 (`5ddb526`): `gpu_tuner/msi_board.py` + OpenRGB.run_effect/end_effects + Lights.effect/end_effect + Scene.apply. breathing -> respiracion; rainbow/wave -> onda arcoiris; cycle -> onda con la paleta; guardar = 0. Al parar: modo directo y colores reenviados. 204 pruebas, 7/7 mutaciones. Instalada 18:46. Herramientas de medicion en `tools/`.
- Retro: `CLAUDE.md` del kit (estado que cambia a mitad de prueba puede ser el usuario) y memoria `project_gpu_tuner_lucca.md` (paradas de la placa, ACK de OpenRGB, cable del header).

## Where We Paused
**Last action:** 0.16.0 instalada; se le pidio a Andres probar desde el panel (All lights): encender, breathing / rainbow / wave / cycle ~30 s cada una, luego none. No contesto antes del cierre.
**Next action:** cuando Andres pruebe: por cada efecto, ¿continuo o se congela? Luego verificar con `python tools/msi_read_config.py` (solo lectura) que tras "none" JARGB 3 vuelve a `09 ff 00 00 00 ff 00 00 00 ff ff ff ff 03 15 78`, y mirar el registro `C:\ProgramData\Lucca Tune\lucca-tune.log` por "own effect could not be set". Si todo bien: docs/estado.md fila 0.16 -> Cerrada con su cita.
**Blockers:** la observacion a ojo es de Andres.

## Files to Read First
- `C:\Users\andre\repos\gpu-tuner\docs\estado.md` — filas 0.15/0.16 y el pendiente "Retraso de la placa MSI".
- `C:\Users\andre\repos\gpu-tuner\docs\bitacora.md` — entradas del 2026-10-21 17:00-18:50 con todas las mediciones.
- `C:\Users\andre\repos\gpu-tuner\gpu_tuner\msi_board.py` — formato 0x50 y por que.

## Notes / Gotchas
- Al cerrar, las luces estan APAGADAS por eleccion de Andres (17:59 "all lights on False"); la placa en modo directo igual al original. No encenderlas sin que el lo pida.
- `tools/msi_hid_timing.py` manda negro por HID: solo con las luces apagadas.
- Nunca poner el byte "guardar" (offset 289) en 1: no probado.
- La lectura de 0x50 justo despues de mandar 0x51 salio desplazada ~8 bytes una vez (sin aclarar); a los segundos leia bien.
- Scripts con rutas `\\?\HID#...` siempre en archivo, nunca por heredoc (rompe las barras, error 123).
- Sin explicar: el "~1 s" visto a ojo el 15-oct (el lado del PC tarda 23 ms).
- La sincronia con la grafica es aproximada (la placa usa su reloj): decision aceptada por Andres.

## Questions to Answer
- ¿Los cuatro efectos son continuos en la caja y "none" devuelve su color?
- ¿Las velocidades de la placa (3) se sienten parecidas a las de la grafica, o hay que ajustar el reparto 0-33/34-66/67-100?
- Pendientes previos aun abiertos: CPU TEMP dentro del servicio; TDR ~43 s con el driver 621.01 (pila sin sacar); sprint 4 (tema claro / escala) necesita aprobacion para cambiar su pantalla.
