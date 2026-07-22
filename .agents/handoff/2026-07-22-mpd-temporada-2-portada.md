# Handoff: MPD Temporada 2 — pivote a misterios, guion T2·E1 y portada
**Date:** 2026-07-22
**Status:** Complete — el siguiente paso es la WEB (a propósito, en sesión nueva)

---

## What We Accomplished This Session

**Decisión estratégica: el show pivota 100% a misterios y leyendas del rock.**
- **Nombre público SIGUE siendo Mr. Putrid's Den.** Se descartó renombrar/migrar (riesgo legal +
  dominio ya registrado). **"The Crossroads" queda como codename interno**, no público.
- **Temporada 1 = EP.001–EP.005** (archivo, incluye la era co-host con Juan → así se encapsula ese
  "rastro" sin borrar historia ni suscriptores). **Temporada 2 arranca con el Club de los 27.**
- Numeración pública **reinicia por temporada**: Club de los 27 = **T2 · E1** (interno sigue EP.006).
  En Spotify se usan los campos nativos Season=2 / Episode=1 — se setean al publicar, NO requiere
  dominio nuevo.
- Límite firme de Andrés: **NADA de simbología ocultista** (cree en las energías). El misterio se
  logra con atmósfera. Ver memoria `feedback_mpd_no_occult_symbols`.

**Guion T2·E1 "El Club de los 27" — listo y verificado.**
- `mrputridsden-production/scripts/EP006-club-de-los-27.html` + `*.artifact.html`.
- **5.208 palabras de narración (~40,5 min)** — contado programáticamente, dentro del rango
  editorial 40-45. Lint de muletillas limpio (0 usos de todas las prohibidas).
- Eje del episodio: el desmentido con el estudio real **BMJ 2011 (Barnett, QUT)** — no hay pico de
  muertes a los 27, pero los músicos jóvenes mueren 2-3x más. Datos no confirmados al 100% marcados
  `[VERIFICAR]` dentro del guion para chequear antes de grabar.
- Conector al próximo expediente: Robert Johnson y el cruce de caminos.

**Portada de la Temporada 2 — terminada.**
- `E:\Podcast\MPD\Temporada 2\artwork\MPD-T2-PORTADA-CONTEXTO-3000.jpg` (con tipografía).
  También la escena sola (`MPD-T2-PORTADA-FINAL-3000.jpg`), la versión sin filtro y la base 1536.
  Las 6 descartadas están en `alternativas\` (no se borró nada).
- Escena: estudio victoriano gótico, chimenea encendida, butaca vacía, whisky y puro apagado.
  Foto realista + filtro de foto antigua determinista (`comfyui/templates/vintage_grade.py`,
  strength 0.6, aplicado DESPUÉS del upscale para que el grano quede a escala).
- Tipografía compuesta con PIL sobre la plantilla existente (`mpd-portada-compose.py`) + íconos
  reales de plataforma reusados de EP.005. **Nunca texto generado por IA.**

## Where We Paused

**Last action:** `/session-close` — retrospectiva aplicada, audit de skills limpio, este handoff.
**Next action:** **Los cambios de la página web** con el sistema de la Temporada 2. Andrés pidió
explícitamente hacerlo en sesión NUEVA (esta se alargó y entró en redundancia).
**Blockers:** Ninguno.

## Files to Read First

- `mrputridsden-production/roadmap-mpd.md` — estructura de temporadas y estado de T2·E1.
- Memoria `project_mpd_rebrand_cruce_de_caminos` — todas las decisiones del pivote.
- Memoria `feedback_mpd_no_occult_symbols` — el límite firme, antes de tocar cualquier visual.
- `mrputridsden-production/rebrand/identidad-cruce-de-caminos.html` — specimen de identidad.

## Notes / Gotchas

- **CABO SUELTO IMPORTANTE:** el specimen de identidad propone paleta ámbar/carretera y estética de
  póster ilustrado, pero la portada elegida es una foto de estudio victoriano. **No concuerdan.**
  Antes de rediseñar la web hay que decidir cuál manda, o el sistema visual queda partido.
- La portada elegida (v18) tiene **dos calaveras decorativas en la repisa y el vaso SIN calavera
  moldeada** — Andrés la aceptó así sabiéndolo. Existe una v19 con el vaso-calavera y la repisa
  despejada si se quiere cambiar (prompt en scratchpad de la sesión, regenerable).
- Cambié el tagline de la portada a **"Donde la música se encuentra con el mito"** (el del perfil
  sigue siendo "Donde los riffs encuentran el whisky"). Es una línea del script si se quiere revertir.
- **Deploy de la web: SOLO por el flujo prebuilt** y verificando `.vercel/project.json`
  (`projectName` debe ser `mr-putrids-den-web`). Ver `deploy-preflight` Paso 1b.

## Questions to Answer

- **Pendiente de la sesión, explícitamente diferido por Andrés:** convertir las reglas críticas de
  memoria en **hooks de `settings.json`** que el harness haga cumplir. Su observación —correcta— es
  que las reglas escritas se ignoran en la práctica: esta sesión violé
  `feedback_teoria_de_la_faja` (declaré el artwork cerrado con un defecto conocido sin arreglar) y
  diseñé una identidad sin mirar el artwork vigente, pese a que el `CLAUDE.md` del proyecto tiene una
  "Regla de transición de modelo" que predice exactamente esa falla. La memoria es contexto asesor;
  los hooks los ejecuta el harness. **Atacar esto al inicio de la próxima sesión.**
- ¿Se alinea el specimen de identidad con la portada fotográfica, o se rehace la portada en el
  lenguaje ilustrado del specimen?
