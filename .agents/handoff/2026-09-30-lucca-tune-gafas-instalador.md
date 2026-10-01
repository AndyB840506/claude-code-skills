# Handoff: Lucca Tune — instalador, perfiles y ventana con forma de gafas
**Date:** 2026-09-30 (miércoles), cierre 23:30
**Machine:** desktop (E:\) — RTX 3080 Ti XC3; todo lo instalado vive solo en esta máquina
**Status:** In progress — versión 0.4.2 instalada y funcionando; faltan las pruebas que Andrés hará el jueves 2026-10-01
---
## What We Accomplished This Session

Producto: reemplazo propio de EVGA Precision X1 / MSI Afterburner, marca Lucca Tech.
Repo `C:\Users\andre\repos\gpu-tuner` → `github.com/Lucca-Tech/gpu-tuner` (privado), rama `main`,
HEAD `edda10a`, limpio y al día con el remoto. 57 pruebas pasan.

- **Nombre decidido por Andrés: Lucca Tune.** El paquete Python y el repo siguen llamándose
  `gpu_tuner` / `gpu-tuner`.
- **Ícono:** el logo de la página de Lucca Tech (`repos/lucca-tech-web/logo.png`), pedido por Andrés.
- **Instalador real** (`installer.iss`, Inno Setup 6.7.3): `python build.py installer` →
  `dist\LuccaTune-Setup-<versión>.exe`. Instala en `C:\Program Files\Lucca Tune`, registra el
  servicio `LuccaTune` (LocalSystem, arranque automático), accesos en escritorio / menú Inicio /
  inicio de sesión. Probado: instalar encima, desinstalar, reinstalar.
- **0.1.1** — el motor perdía los ajustes del modo que no estaba activo al reiniciarse.
- **0.2.0 → 0.3.0** — perfiles; Andrés pidió que fueran **numerados 0–9 como en el X1**, sin
  nombres. SAVE y luego un número guarda; un número solo carga.
- **0.3.0** — el overlay se podía cerrar para siempre (tomaba el foco y un Alt+F4 lo destruía).
- **0.4.0** — ventana principal **con forma de las gafas del logo**; la interfaz completa pasó a
  ser la ventana "Lucca Tune Settings".
- **0.4.1** — quitado el fondo gris alrededor de las gafas (era la capa Mica de Windows).
- **0.4.2** — quitado el recuadro oscuro que salía un instante al abrir. **Andrés confirmó a ojo
  que quedó limpio.**
- Firma de código: explicada y **aplazada**. Lucca Tech no está constituida como empresa.

## Where We Paused
**Last action:** Andrés confirmó que las gafas se ven limpias en la 0.4.2 y pidió cerrar la sesión.
**Next action:** las pruebas que Andrés hará el jueves 2026-10-01 (ver abajo). Empezar preguntando
cuáles ya hizo.
**Blockers:** todas las pruebas pendientes necesitan a Andrés frente al escritorio.

### Pruebas pendientes (todas en el escritorio; nada de esto se puede hacer desde el portátil)
1. **Carga real** — jugar ~15 min mientras se graba. Dos grabaciones previas NO tuvieron carga
   (promedio 28–29 %, pico 128–151 W). Decide si la curva sigue el hotspot o el peor entre hotspot
   y memoria. El grabador (`record_load.py`) estaba en el scratchpad temporal de la sesión: hay que
   reescribirlo; lee `http://127.0.0.1:8377/api/state` cada 2 s y escribe un CSV.
2. **Curva y sliders** — confirmar que ya no hay que reajustarlos al abrir (arreglo de la 0.1.1 sin
   confirmación de Andrés).
3. **Menú de la bandeja** — clic real en Open / Settings / Profiles; nunca se pudo probar desde aquí.
4. **Reinicio del PC** — ver que el servicio y las gafas arrancan solos.
5. **Arrastre de las gafas con el ratón real** — solo se probó con mensajes de ratón enviados.

## Files to Read First
- Memoria `project_gpu_tuner_lucca.md` — bitácora completa con horas, causas y lo no probado.
  **Ojo:** su línea en `MEMORY.md` quedó en la zona que el índice ya no carga (el archivo pasa del
  límite), así que hay que abrirla a mano.
- Memoria `reference_pywebview_shaped_window.md` — receta de la ventana con forma y lo que no sirve.
- `repos/gpu-tuner/gpu_tuner/desktop.py` — app de escritorio: gafas, panel, overlay, bandeja.
- `repos/gpu-tuner/gpu_tuner/ui/goggles.html` — la ventana de gafas.
- `repos/gpu-tuner/gpu_tuner/server.py` — motor: modos, perfiles, API.
- `repos/gpu-tuner/README.md`

## Notes / Gotchas
- **Estado real del escritorio al cerrar (verificado 23:26):** instalada 0.4.2; servicio `LuccaTune`
  Running/Auto; app corriendo; modo curva siguiendo hotspot cada 300 ms; perfil 0 con algo guardado
  por Andrés; overlay apagado (vuelve con Ctrl+Alt+F9); gafas en (1111, 373).
- **Cada cambio de interfaz obliga a reconstruir e instalar:** el servicio sirve las páginas desde
  su propio paquete. Instalar pide permiso de administrador (aviso de Windows) y reinicia la app.
- **Probar desde el código sin instalar:** arrancar `gpu_tuner.desktop.main(port=<otro>, demo=True)`
  con `GPU_TUNER_DATA` apuntando a una carpeta temporal; así usa su propio motor simulado.
- **Las pruebas de transparencia ponen una ventana magenta en pantalla ~10 s.** Avisar a Andrés.
- **El clasificador de la sesión negó dos cosas; no reintentar por otra vía sin que Andrés lo
  autorice:** seguir desensamblando el código interno de Precision X1, y crear una tarea programada
  con privilegios máximos.
- Carpetas viejas sin uso que no se borraron: `C:\ProgramData\GPU Tuner`, `C:\Users\andre\.gpu-tuner`.
- La API local (127.0.0.1:8377) no tiene autenticación; pendiente de endurecer antes de vender.
- Sin probar: tema claro de Windows, pantallas con escala distinta de 100 %.
- No hay forma de vaciar un perfil numerado, solo de guardar encima.

## Questions to Answer
- ¿La curva por defecto debe seguir el hotspot o el peor entre hotspot y memoria? (sale de la prueba de carga)
- ¿Firma de código: certificado individual a nombre de Andrés, o constituir Lucca Tech primero?
  (aplazado hasta acercarse a publicar)
- Hoja de ruta sin empezar: luces de la tarjeta con color por temperatura, FPS en el overlay,
  overclock, AMD, Linux, teclas rápidas por perfil.
