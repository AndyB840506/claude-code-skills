# Handoff: MPD EP.04 "Paul is Dead" — guion y artwork listos, pendiente grabar

**Date:** 2026-08-20 (jueves)
**Machine:** desktop (E:\ existe, RTX 3080 Ti usada para el artwork)
**Status:** Stage A completo — pausa natural, esperando grabación.

---

## What We Accomplished This Session

- **Guion completo de EP.04** (Expediente 04, "Paul is Dead"): ~35 min, 4.452
  palabras `host-text`, verificado programáticamente. Aprobado as-is por Andrés
  pese a quedar bajo el piso editorial de 43 min (mismo precedente que EP.005 y
  EP.03). Ángulo: Fred LaBour/*Michigan Daily* 1969, con una comparativa de
  "dobles" modernos agregada a pedido de Andrés (Avril Lavigne/Melissa Vandella,
  teoría reptiliana, video viral de Justin Bieber). Cierre NO anuncia próximo
  expediente (el candidato disponible del banco ya estaba usado, ver abajo).
  - Archivo: `mrputridsden-production/scripts/EP04-paul-is-dead.html`
  - Artifact publicado: https://claude.ai/code/artifact/c0253208-3bc3-4117-b274-008d1fb483ce
- **Artwork final** (1:1/16:9/9:16) en `E:\Podcast\MPD\Temporada 2\EP 04\artwork\`
  — concepto: periódico envejecido enmarcado en el óvalo de "La Guarida" (nexo
  con el artículo real de LaBour). 4 rondas de iteración documentadas en
  `episodios/temporada-2/artwork-ep04.md`, incluyendo un pedido de Andrés de
  retrato real de Paul McCartney que se rechazó dos veces (derechos de imagen +
  ironía temática) — ver `feedback_no_real_person_likeness_override` en memoria.
- **Corrección propia antes de comprometerla:** casi se propone "Crowley" (ya
  usado en EP.03) y "pánico satánico ampliado" (ya cubierto entero en EP.02)
  como próximo expediente disponible — detectado abriendo los scripts reales,
  no la memoria ni el roadmap.
- **Retrospective aplicado (5 cambios):** lecciones de ComfyUI (regenerar a
  mayor resolución con el mismo seed ≠ escalar la aprobada; el telón fijo puede
  no leerse distinto entre episodios; texto "borroso" en un objeto sigue
  produciendo pseudo-texto) en `comfyui/docs/`, y `banco-expedientes.md` items
  1-4 marcados como USADO para que no se vuelvan a proponer.
- **Skill audit:** 0 colisiones de triggers en las 28 skills, todos los
  `SKILL.md` bajo 50 líneas. Sin correcciones necesarias.

---

## Where We Paused

**Last action:** session-close (retrospectiva + auditoría + este handoff).
**Next action:** Andrés graba el episodio. Cuando el audio exista, retomar el
pipeline ("corre el pipeline para EP.04") — sigue directo con la transcripción.
**Blockers:** ninguno. La transcripción (WhisperX) necesita el desktop
específicamente — no correr esa etapa desde el portátil.

---

## Files to Read First

- `mrputridsden-production/pipeline-state-ep04.md` — `stage_a: complete`, resto pendiente
- `mrputridsden-production/scripts/EP04-paul-is-dead.html` — guion aprobado
- `mrputridsden-production/episodios/temporada-2/artwork-ep04.md` — artwork final + iteración completa
- `mrputridsden-production/roadmap-mpd.md` — fila de EP.04 marcada "guion listo"

---

## Notes / Gotchas

- El servidor de ComfyUI local (desktop, puerto 8188) quedó **corriendo** al
  cierre de esta sesión — no se apagó explícitamente. Si la próxima sesión
  necesita generar más artwork, verificar con `curl http://127.0.0.1:8188/system_stats`
  antes de intentar relanzarlo.
- `comfyui/templates/mpd-portada-ep04-t2.py` apunta a
  `E:\AI\outputs\MPD-T2E04-escenario-v4-3000-graded.png` como escena final — los
  archivos `v1`/`v2`/`v3` en esa misma carpeta son descartes de la iteración,
  no borrar (quedan de referencia en `artwork-ep04.md`).

---

## Questions to Answer

Ninguna abierta — todas las decisiones de Stage A quedaron cerradas con Andrés
en la sesión (word count, concepto de artwork, cierre sin anuncio).
