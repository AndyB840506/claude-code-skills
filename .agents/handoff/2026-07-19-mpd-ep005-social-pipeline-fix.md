# Handoff: MPD EP.005 — Plan social generado + gap del pipeline corregido
**Date:** 2026-07-19
**Status:** Complete

---

## What We Accomplished This Session

**Plan social de EP.005 generado (faltaba):**
- `mrputridsden-production/episodios/social-ep005.md` — el episodio (Aterciopelados) ya estaba
  publicado desde la noche del sábado 18 julio, así que el plan no pudo usar el ciclo estándar
  Intriga/Contenido/Lanzamiento (sin ventana previa al lanzamiento). Se armó como
  Lanzamiento (domingo 19, hoy) / Contenido (martes 21) / Recordatorio (jueves 23), firmado
  100% Andrés (formato solo desde EP.005, sin mencionar la salida de Juan — decisión ya tomada).
- Quote del Día 2: *"Una canción secreta, escrita para Cerati — nadie lo supo hasta que él
  murió"* — calza con el quote card Q3 ya generado (`artwork-ep005.md`).
- TikTok marcado explícitamente "EN PAUSA — no publicar por ahora" a pedido de Andrés
  (2026-07-19), el copy queda escrito por si se reactiva.

**Causa raíz encontrada y corregida (retrospectiva):** la ruta MPD de `episode-pipeline`
(Stage B, `02-assets.md`) invocaba show-notes, YouTube y artwork, pero **nunca** el workflow de
social media — por eso el plan de EP.005 no se generó hasta que Andrés preguntó por él, 2 días
después de publicado. Tres fixes aplicados:

1. `episode-pipeline/workflows/02-assets.md` — agregado paso 4 a la ruta MPD: invocar
   `podcast-creator/workflows/04-social-media.md` en la misma etapa que los otros tres, sin
   esperar a que el episodio esté en vivo.
2. `.claude/skills/podcast-creator/workflows/04-social-media.md` — agregado fallback: si el
   link de Spotify ya es real (episodio ya publicado), el plan pasa a
   Lanzamiento/Contenido/Recordatorio arrancando el día que se corre el workflow, en vez de
   contar hacia atrás desde una fecha de publicación que ya pasó. También ahora lee
   `status: "pausado"/"pendiente"` en `links` de `podcast-profile.json` y salta esas
   plataformas automáticamente (en vez de generarlas y marcarlas "no publicar" a mano).
3. `.claude/skills/mrputridsden/podcast-profile.json` — agregado `links.tiktok` con
   `status: "pausado"` y la nota de la decisión de Andrés, para que el punto 2 aplique sin
   intervención manual en el próximo episodio.

**Memoria guardada:** `feedback_social_media_generate_at_recording.md` (tipo feedback) — regla
general de "generar social al grabar, no al publicar", indexada en `MEMORY.md`. El fix #1 de
arriba es lo que la hace efectiva en la práctica.

**Auditoría de skill kit:** revisados los 3 routers tocados (`podcast-creator/SKILL.md` 41
líneas, `mrputridsden/SKILL.md` 31 líneas, `episode-pipeline/SKILL.md` 49 líneas) — todos bajo
el límite de 50, sin archivos `.md` sueltos junto a carpetas de skills. Sin issues.

## Where We Paused

**Last action:** Commit + push de los 3 fixes de pipeline + `social-ep005.md`, luego este
handoff.
**Next action:** Ninguna acción inmediata pendiente sobre EP.005 — el plan social ya está
listo para ejecutar según el calendario (Día 2 martes 21, Día 3 jueves 23). El próximo episodio
que pase por Stage B de `episode-pipeline` debería generar su plan social automáticamente sin
que Andrés tenga que pedirlo — vale la pena confirmar que el fix funciona en la práctica la
próxima vez que se corra el pipeline para MPD.
**Blockers:** Ninguno.

## Files to Read First

- `mrputridsden-production/episodios/social-ep005.md` — el plan social recién generado.
- `episode-pipeline/workflows/02-assets.md` — ruta MPD ahora incluye el paso de social media.
- `.claude/skills/podcast-creator/workflows/04-social-media.md` — fallback para episodios ya
  publicados + lectura de plataformas pausadas/pendientes.

## Notes / Gotchas

- El clip de audio de 30-60 seg y la confirmación del wording exacto de la quote del Día 2
  contra el audio grabado siguen pendientes (marcados en el resumen de assets de
  `social-ep005.md`) — no bloquean publicar los posts de texto/imagen.
- El fallback nuevo en `04-social-media.md` es la primera vez que se usa — si en un próximo
  episodio el plan sale raro (fechas mal calculadas, día equivocado), revisar esa sección
  primero antes de asumir que es un problema nuevo.

## Questions to Answer

- (Heredadas del handoff anterior, `2026-07-17-mpd-solo-format-ep005.md`, aún sin resolver):
  reemplazo para el segmento de eventos underground / booking de invitados de EP.008 — sin
  fuente definida (Juan cubría esto como promotor); y qué tema toma EP.009 ahora que su pillar
  original ("Spotlight: eventos underground") fue retirado.
