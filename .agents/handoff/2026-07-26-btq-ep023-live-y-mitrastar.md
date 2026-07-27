# Handoff: BTQ EP.023 en vivo + userscript Mitrastar

**Date:** 2026-07-26 (la sesión cerró 2026-07-27 00:09, lunes — verificado contra el calendario)
**Machine:** laptop (D:\) — sin unidad E:
**Status:** EP.023 publicado y web desplegada · pendientes manuales de Andy desde el escritorio

---

## What We Accomplished This Session

- **EP.023 EN VIVO** en Spotify (`https://open.spotify.com/episode/3FQOeIT8bNTakHNGgBhMMR`),
  verificado por og:title. URL sustituida en los 3 marcadores, web desplegada con
  `vercel --prod` (`dpl_Gv3PxhntkCxjxyfFnZGBbfoadMEX` → `behind-thequeue.com`) y verificada
  en vivo con cache-busting. roadmap → publicado. **Commit `3dd5d7d`.**
- **Decisiones de Andy, aplicadas en TODOS los productores (no solo en notas):**
  - **YouTube: NO se retira.** Se retiró por error (leí «YouTube confirmó con el RSS» como
    «no queda trabajo manual»); Andy edita la metadata a mano en Studio, el RSS solo crea el
    ítem. Revertido en la misma sesión: `48b7898` retiró → `f6015be` revirtió. §C de step2 viva.
  - **SafeCreative: RETIRADO** para BTQ (la recomendación genérica de `podcast-creator` se queda).
  - **Jingle: varía por episodio** manteniendo el formato de EP.023 (invierte la regla vieja
    de «asset permanente que se reusa»). Regla nueva en `jingle-brief.md`.
- **Assets regenerados EN EL PORTÁTIL** (`D:\AI\outputs\BTQ-brand` y `D:\AI\outputs\BTQ-EP023`):
  portadas 3 formatos, 4 quote cards, avatar y banner de YouTube. Faltaban Pillow + las 3
  fuentes (Cabinet Grotesk, Supreme, Martian Mono) — instaladas y documentadas en
  `brand-constants.md` § Fuentes. COVER-q92.jpg = **235 KB** (contraprueba de no-deriva). **`298ff90`.**
- **Residuo v3 en el bloque D de quote cards** corregido: «split 50/50», «objeto de escena» y
  «texto sin tildes» (esta última casi hace que salieran sin acentos). **Commit `1100e40`.**
- **Userscript Mitrastar** (menú avanzado del router Movistar GPT-2741GNAC) reescrito a **v1.3**:
  5 bugs corregidos, `@include` para el puerto 8000 (único abierto, verificado con
  `Test-NetConnection`), `test-mitrastar.js` con jsdom (11 checks en verde). **Andy confirmó
  que YA tiene acceso al menú avanzado.** Vive en `C:\Users\andre\repos\userscripts\`.
- Router guardado en memoria (`reference_router_movistar_mitrastar.md`) y aprendizaje nuevo
  `feedback_automation_not_equals_no_manual_work.md`.

## Where We Paused

**Last action:** corregir marcador stale «PENDIENTE DE DEPLOY» en `pipeline-state-ep023.md`
(la web ya estaba desplegada) y cerrar sesión.
**Next action:** desde el ESCRITORIO, subir avatar+banner a YouTube y pegar la metadata §C.
**Blockers:** todo lo pendiente es manual de Andy y **machine-bound al escritorio** (assets en
`E:\`, sesión de YouTube Studio).

## Files to Read First

- `btq-production/pipeline-state-ep023.md` — checkpoint; manda sobre este handoff si chocan
- `btq-production/launch-assets/EP023-hawthorne-launch.md` — assets; §C YouTube ES aplicable
- `.claude/skills/episode-launch/workflows/step2-generate-assets.md` — §C YouTube revivida
- `C:\Users\andre\repos\userscripts\mitrastar-unlocker.user.js` — v1.3 + `test-mitrastar.js`

## Notes / Gotchas

- **Sesión en el PORTÁTIL** (C y D, sin E). Los assets se REGENERAN por máquina, no se copian:
  son PIL determinista. `brand-constants.md` § Fuentes tiene el aprovisionamiento completo.
- **`verify_assets.py` nunca ha validado una quote card de BTQ:** busca `-CARDn-16x9.png` pero
  el generador las nombra `BTQ-EP023-QUOTE-N.png`. El gate de cards está muerto para BTQ.
- **Atribución de las quote cards** usada: `BEHIND THE QUEUE · EP.023` — sin confirmar contra
  las del escritorio.
- `userscripts\` **no es repo git** y tiene `node_modules` de jsdom dentro.

## Questions to Answer

- **Offset de los 23 capítulos de YouTube:** se calcularon contra el SRT PREVIO al jingle. Si al
  montar se agregó stinger + silencio en cabeza (había 0,59 s, el checklist pide 3 s), los
  timestamps están corridos ese delta. Comprobar en qué segundo entra la primera palabra del
  audio publicado ANTES de pegar los capítulos.
- **Nombre canónico de las quote cards** (`-QUOTE-N` vs `-CARDn-16x9`) para arreglar el regex
  de `verify_assets.py` (1 línea) sin romper el pipeline social ya programado.
- **Documentar el jingle de EP.023** (dirección de las 3, duración, archivo) — es la referencia
  de formato para EP.024 en adelante y no está escrito en ningún lado.
- **Hora de lanzamiento 20:00 vs 21:00** — decisión heredada, se resuelve con analytics de EP.023.
- **`git init` de `userscripts\`** con `.gitignore` (para el userscript + tests) — opcional.
- **EP.024 = Principio de Peter:** abrir la fuente primaria antes de redactar; primer guion
  dimensionado a ~5.565 palabras con la tabla nueva.
