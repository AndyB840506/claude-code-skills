# Handoff: BTQ EP.021 — quote cards regeneradas en portátil + cierre de sesión

**Date:** 2026-07-13 (lunes)
**Status:** Complete — EP.021 100% cerrado (incluye qué set de cards se publica);
auditoría del kit aplicada; retrospectiva aplicada.

---

## What We Accomplished This Session

- **Corrección de arranque:** la sesión empezó respondiendo sobre EP.021 con el repo
  14 commits atrás (sin correr el `git pull` de inicio que manda el CLAUDE.md del
  proyecto) — dijo que el episodio no estaba grabado cuando ya estaba publicado. Se
  corrigió con `git pull` y se guardó memoria `feedback_verify_startup_sync_before_answering`
  para no repetirlo, incluso cuando el mensaje del usuario "parece" una pregunta simple.
- **Quote cards de EP.021 regeneradas en el portátil** (Andy las había generado en el
  PC, pero está trabajando desde el portátil): ComfyUI local (D:\AI, Z-Image Turbo,
  RTX 3060 6GB) + texto compuesto con PIL (Segoe UI, tildes correctas). 3 escenas
  (micrófono/estudio, CRT en estática/sofá, vela+standby rojo) — 2 de 3 necesitaron
  una segunda pasada: CARD1 salió con fondo rojo en vez de negro puro (bleed de color
  de la luz), CARD3 alucinó una figurita junto a la vela sin que se pidiera. Ambos
  corregidos y verificados visualmente antes de componer el texto.
- **Andy decidió publicar el set del portátil**, no el del PC — ya programadas en Meta
  Business Suite con las fechas/horas del calendario original (§B2). Archivos en
  `D:\Podcast\BTQ\EP 21\BTQ Artwork EP 21\BTQ-EP021-CARD{1,2,3}-16x9.png`.
  `EP021-simpsons-launch.md` actualizado con nota explícita de cuál set es el vigente
  y cuál queda sin usar (el del PC, no borrado).
- **Feedback editorial para EP.022:** Andy prefirió el tono/enfoque de EP.020 (pilar
  SEO, más "profesional", temas operacionales) sobre EP.021 (pop-culture). Registrado
  en `roadmap-btq.md` como señal para inclinar EP.022 hacia otro pilar SEO en vez del
  siguiente candidato pop-culture de la lista — tema exacto aún sin decidir.
- **Retrospectiva (2/2 aplicados):** (1) plantilla reutilizable
  `comfyui/templates/quote-card-compose.py` para no reinventar la composición PIL cada
  vez (split 50/50, fuente, tamaño dinámico), referenciada desde `03b-marketing.md` y
  `brand-constants.md`. (2) nota "Implementación PIL" con fuente/tamaño en
  `brand-constants.md`.
- **Lecciones de Z-Image Turbo** (de las 2 regeneraciones): un adjetivo de color cerca
  de la luz tiñe TODO el fondo aunque se pida "void black" aparte; escenas de un solo
  objeto en vacío pueden alucinar un objeto extra sin pedirlo. Documentadas en
  `comfyui/docs/prompting.md` + `imagen-a-prompt/docs/prompt-formats.md` (copia
  standalone, sincronizada). De paso se corrigió la nota vieja "Z-Image untested en el
  portátil" — quedó verificado OK (~40s/imagen, sin OOM, RTX 3060 6GB).
- **Auditoría del kit de skills (6/6 aplicados):**
  1. Ruta falsa de `podcast-creator` anidada dentro de `mrputridsden` corregida en
     `mrputridsden/CLAUDE.md` (era `.../mrputridsden/.claude/skills/podcast-creator`,
     es `.claude/skills/podcast-creator` en la raíz) + 2 filas heredadas en
     `test-harness/results.md`.
  2. `imagen-a-prompt/SKILL.md` tenía 99 líneas con toda la lógica embebida — extraída
     a `workflows/analizar-imagen.md`, el router quedó en 40 líneas.
  3. Triggers superpuestos `mrputridsden`/`podcast-creator` — los genéricos de
     mrputridsden ahora llevan calificador ("de la guarida", "de mr putrid").
  4. Desambiguación cruzada `web-page-kit` (Rule 8 = autoridad de tono a nivel de
     sitio) vs `ui-ux-pro-max`/`frontend-design` (componentes sueltos, no rediseñar
     el tono completo si web-page-kit ya está corriendo).
  5. Referencia rota a `/prompt-reviewer` (español, no existe) quitada de
     `prompt-reviewer-en/SKILL.md`.
  6. 4 `SKILL.md` que medían exactamente 50 líneas recortados a <50
     (`apify-scraper`, `episode-pipeline`, `memory-audit`, `session-close`).
- **Commit `f79c932`** con los 21 archivos de esta sesión (push pendiente — ver
  Blockers).

## Where We Paused

**Last action:** commit del trabajo sustantivo de la sesión; escribiendo este handoff.
**Next action:** nada de agente para EP.021 — Andy publica las 3 quote cards del
portátil según el calendario ya programado en Meta Business Suite. Próximo trabajo de
pipeline: EP.022 — decidir tema exacto (pilar SEO/operacional, ver roadmap-btq.md).
**Blockers:** ninguno de agente. Falta correr Step 4 (continuity sync) y Step 5
(memory+skill-kit audit check) de `/session-close` — siguen después de este handoff.

## Files to Read First

- `btq-production/launch-assets/EP021-simpsons-launch.md` §B2 — calendario + nota de
  cuál set de cards es el vigente (portátil, no PC).
- `btq-production/roadmap-btq.md` — feedback de Andy sobre EP.022 antes de proponer tema.
- `comfyui/templates/quote-card-compose.py` — plantilla para la próxima vez que se
  generen quote cards localmente (cualquier show).
- `.claude/skills/episode-launch/docs/brand-constants.md` §Quote Cards — spec completa
  (colores, fuente, split 50/50) ya con la implementación PIL documentada.

## Notes / Gotchas

- El set de cards del PC (`E:\Podcast\BTQ\EP 21\...`) sigue existiendo, no se borró —
  simplemente no es el que se publica esta vez.
- Z-Image Turbo SÍ funciona bien en el portátil (6GB VRAM) — la nota vieja que decía
  "untested, expect slow/OOM" ya no aplica, quedó corregida en `stack-reference.md`.
- Convención nueva: `D:\Podcast\<Show>\EP NN\...` en el portátil espeja
  `E:\Podcast\<Show>\EP NN\...` en el desktop — mismo nombre de carpeta, solo cambia la
  letra de unidad (igual que `D:\AI` ↔ `E:\AI`).
- El PIL renderiza tildes/ñ perfectas de forma determinista — ya no hace falta la
  regla vieja de "mayúsculas SIN tildes" que existía para compensar a Flow.

## Questions to Answer

- ¿Tema exacto de EP.022? Andy señaló que prefiere el enfoque tipo EP.020 (pilar SEO,
  operacional) sobre pop-culture — falta el tema concreto (no es Metallica/Matrix/Star
  Wars de la lista vieja, esos siguen como candidatos pop-culture para más adelante).
