# Handoff: Lucca Tune — overclock, voltaje y luces (0.4.2 a 0.8.1)
**Date:** 2026-10-01 (jueves), cierre 11:56
**Machine:** desktop (E:\) — RTX 3080 Ti XC3; todo lo instalado y medido vive solo en esta máquina
**Status:** In progress — 0.8.1 instalada y subida; falta que Andrés la vea con sus ojos
---
## What We Accomplished This Session

Repo `C:\Users\andre\repos\gpu-tuner` → `github.com/Lucca-Tech/gpu-tuner` (privado), rama `main`,
HEAD `e805c3d`, limpio e igual al remoto (leído con `ls-remote` a las 11:56). 105 pruebas pasan.
12 commits hoy.

- **Pruebas de Andrés sobre la 0.4.2:** curva y sliders, bandeja, arrastre y reinicio, cerradas.
- **EA AntiCheat bloqueó Battlefield 6** por `EVGA\Kernel\driver-x64.sys`, el driver de kernel de
  Precision X1 (no de Lucca Tune). Se deshabilitó; Andrés desinstaló X1 y LED Sync; restos borrados.
- **0.4.3** — el overlay sacaba del juego al mostrarse (tomaba el primer plano 6 ms) y quedaba
  tapado. Andrés confirmó en el juego que quedó bien.
- **Prueba de carga real** (38 min a 334 W): la curva sigue el **hotspot** de fábrica (**0.4.4**).
- **0.5.0** — preajustes medidos con carga constante de 348 W, tope del 90 % (regla de Andrés para
  alargar la vida de los ventiladores), emergencia a 100 % si el hotspot llega a 88 °C; el motor
  rechaza peticiones dirigidas a otro nombre de equipo.
- **0.6.0 → 0.6.2** — overclock sin voltaje (potencia, temperatura objetivo, reloj de núcleo y de
  memoria) con prueba de 20 s que se revierte sola, y sin reaplicar tras un cierre brusco. Pasarse
  del rango recomendado exige aceptar una advertencia y permiso de administrador. Potencia en %
  enlazada con la temperatura, como en X1.
- **0.7.0** — lectura de voltaje siempre; refuerzo de voltaje solo con el rango completo abierto.
- **0.8.0 → 0.8.1** — luces propias de la EVGA: modos, color, brillo, velocidad, zonas enlazables,
  color que sigue una temperatura con tres puntos editables, y luces en los perfiles.
- **Recuadro gris de las gafas (volvió):** el Explorador crea una ventana con nuestro mismo título
  y el programa buscaba la suya por título. Corregido en la 0.8.1.
- **Memoria:** el índice llevaba 71 entradas sin cargar; se acortó (18 KB, 199 entradas). La
  bitácora de Lucca Tune se movió de la memoria al repo.
- **Kit (retrospectiva):** `memory-audit` ahora mide el índice; dos reglas nuevas de instrumentos y
  una de la herramienta PowerShell en `CLAUDE.md`; sección 10 en `docs/estandar-de-entregables.md`;
  `audit-triggers.py` ya no cuenta las skills sincronizadas.

## Where We Paused
**Last action:** 0.8.1 instalada, comprobada sobre la tarjeta y subida; se repuso la elección de
luces de Andrés que una prueba mía había borrado.
**Next action:** preguntar a Andrés qué vio en la 0.8.1 (y en la 0.6.2 y 0.7.0) antes de proponer
nada. La vez anterior encontró tres cosas que las pruebas por programa no vieron.
**Blockers:** todo lo que sigue necesita los ojos de Andrés frente al escritorio.

### Lo que Andrés debe mirar (escritorio; nada de esto se puede hacer desde el portátil)
1. **Luces (0.8.1):** velocidad en un modo animado, botón "Zones linked", y "Follows temperature"
   con sus tres puntos y el selector núcleo / hotspot / memoria. ¿Los leds hacen lo que dice la pantalla?
2. **Gafas:** que el recuadro gris no vuelva tras un reinicio del PC (solo se probó reiniciando la app).
3. **Overclock (0.6.2):** dejar vencer una prueba y ver el aviso "Not kept in time"; potencia en %.
4. **Voltaje (0.7.0):** la quinta fila debe decir algo como "0.762 V · LOCKED".

## Files to Read First
- `C:\Users\andre\repos\gpu-tuner\docs\estado.md` — **el estado vigente**: etapas, evidencia de
  cada una, lo no verificado, pendientes diferidos con su razón, límites que no se cruzan.
- `C:\Users\andre\repos\gpu-tuner\docs\bitacora.md` — historia con horas, causas y mediciones.
- Memoria `project_gpu_tuner_lucca.md` — decisiones de producto de Andrés y trampas ya pagadas.
- Memoria `reference_pywebview_shaped_window.md` — receta de la ventana con forma, con la trampa nueva.
- `gpu_tuner/tuning.py` (overclock y su red de seguridad), `gpu_tuner/lights.py`, `gpu_tuner/icx3.py`.

## Notes / Gotchas
- **Estado real al cerrar (leído 11:56):** servicio `LuccaTune` Running; curva de Andrés
  (35→50, 50→65, 66→80, 80→90), sigue hotspot; overclock en fábrica (350 W, 83 °C, 0, 0, 0 %), rango
  completo cerrado, nada guardado; luces: zonas 1 y 3 en "temperature", siguen el hotspot; overlay
  apagado; gafas en (1599, 563).
- **Cada cambio obliga a reconstruir e instalar** (`python build.py`, `python build.py installer`),
  instalar pide administrador, y hay que reabrir la app después (el instalador silencioso no la abre).
- **Un guion de prueba que toca la tarjeta guarda primero lo que Andrés tenía y restaura eso.**
  Hoy uno terminó "devolviendo las luces de fábrica" y le borró su elección.
- **Nunca buscar una ventana propia con `FindWindowW` por título** (ver la memoria de pywebview).
- **Las pruebas de overlay ponen la pantalla en magenta**, y las de luces cambian los leds: avisar antes.
- **Voltaje:** solo se escribió 1 % a la tarjeta, nunca más. El tope de 100 % no lo declara el driver.
- **La advertencia de responsabilidad no es texto legal revisado.** Antes de publicar: licencia en
  el instalador vista por un abogado.
- **OpenRGB NO se instala en este PC sin preguntar:** trae un controlador de kernel (PawnIO) y fue
  un controlador de kernel el que bloqueó Battlefield.
- **Anomalía sin explicar:** una comprobación del panel de luces dio 1 de 10 en su primera corrida
  y no se repitió en cuatro más. Anotada en `estado.md`, sin causa atribuida.
- **Límites del clasificador (de ayer, siguen):** no desensamblar Precision X1 ni crear tareas
  programadas con privilegios máximos sin que Andrés lo autorice.
- **Índice de memoria en el tope:** `MEMORY.md` tiene 200 líneas justas. La próxima memoria nueva
  lo cruza; bajar de ahí exige fusionar entradas, que es una sesión aparte con aprobación por grupo.

## Questions to Answer
- ¿Qué encontró Andrés al mirar la 0.8.1, la 0.6.2 y la 0.7.0?
- ¿Sesión de fusión de memorias para bajar el índice de 200 líneas? (duplicados, contradicciones
  y obsoletas siguen sin revisar; tres archivos de HireSignal y MPD están pasados de tamaño.)
- Puente con OpenRGB: ¿se instala OpenRGB en este PC, o se prueba en otra máquina?
- Diferido en luces: ciclo y pila de colores. Diferido en general: firma de código, tema claro y
  escalas distintas de 100 %, AMD, Linux, FPS en el overlay (detalle en `estado.md`).
