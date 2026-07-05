# Handoff: BTQ EP.020 — Lanzamiento cerrado (Stage C completa, pipeline publicado)
**Date:** 2026-07-05
**Status:** Complete — episodio publicado y verificado en vivo. Un solo detalle cosmético pendiente (Q4 overlay de texto).
---

## What We Accomplished This Session

- **Spotify URL recibida y checkpoint resuelto:** Andy publicó EP.020 y pasó la URL
  (`https://open.spotify.com/episode/6gRVIWVI3jBUAJarLJ7AsQ`). `pipeline-state-ep020.md`
  actualizado, pipeline avanzó de Stage B a Stage C (`00-intake.md` checkpoint).
- **Cambio de dirección de arte para quote cards (retroactivo desde EP.020):** Andy
  comparó las quote cards generadas contra la portada y calificó el estilo antiguo
  ("graphic editorial poster — NOT photorealistic 3D", usado EP.017–EP.019) de
  "boring/sketchy". Las 4 quote cards de EP.020 se reescribieron completas para usar el
  MISMO render cinematográfico/con volumen real que la portada. Documentado como regla
  nueva en `episode-launch/docs/brand-constants.md` §Quote Cards para EP.021+.
- **Regla de fondo variado:** al quitar el anillo dorado genérico de fondo (motivo
  reservado para la portada), se agregó a cada card un elemento de fondo distinto y
  desenfocado, relevante al tema de esa cita específica — evita que las 4 cards se
  sientan repetitivas entre sí. También documentado en brand-constants.md.
- **5 rondas de validación de imágenes** hasta llegar a 4/4 con escena aprobada:
  - Patrón recurrente descubierto: Flow reinsertaba el anillo dorado genérico en Q1, Q3
    y Q4 pese a pedir otro fondo — se resolvió agregando una línea explícita "DO NOT
    render any concentric ring/circle/target pattern" a cada prompt.
  - Patrón recurrente #2: Flow autocorrigió "NUMERO" → "NÚMERO" (con tilde) en Q4 tres
    veces seguidas (prompt original + 2 ediciones dirigidas) pese a instrucción
    explícita de no usar tilde. Se decidió parar de reintentar en Flow y corregir esa
    palabra puntual por fuera (overlay/recorte en editor simple) — la escena de Q4 ya
    está aprobada, solo falta ese overlay cosmético.
  - Resultado final: **Q1, Q2, Q3 completamente aprobadas. Q4 aprobada en escena,
    pendiente overlay manual de una palabra.**
- **Grid del sitio BTQ rotado y desplegado:** `btq-production/website/index.html` — hero
  "latest" pasó de EP.019 a EP.020; EP.019 entró al tracklist de 4 (era el episodio en
  circulación); EP.015 salió por ser el más antiguo. Grid resultante: `019,018,017,016`.
  **Descubrimiento importante:** la convención visual de BTQ es descendente (más
  reciente de los 4 primero), NO ascendente como decía `04-grid-rotation.md` — MPD sí es
  ascendente (verificado). El doc del workflow se corrigió con esta distinción precisa
  por show.
- **Deploy a producción:** preflight PASS → gate de aprobación (Andy aprobó) →
  `vercel --prod` desde `btq-production/website/` → `https://behind-thequeue.com`→
  HTTP 200 confirmado con el contenido nuevo → Spotify confirmado (EP.20 visible en la
  página pública del show). Pipeline completo, `pipeline-state-ep020.md` →
  `stage_c: complete`.
- **Commit + push:** `44f5657` — launch-assets, pipeline-audit, pipeline-state,
  brand-constants.md, index.html.
- **Retrospectiva aplicada (4 fixes):**
  1. `brand-constants.md` — sección nueva "Patrones de fallo conocidos de Flow"
     (anillo genérico + autocorrección de tildes) para aplicar preventivamente en
     futuros episodios, no reactivamente.
  2. Memoria `feedback_flow_quotecard_text_validation.md` — regla de corte agregada
     (2 intentos de edición fallidos → corregir fuera de Flow).
  3. `episode-pipeline/workflows/04-grid-rotation.md` — corregido con la distinción
     real por show (BTQ descendente, MPD ascendente) y ejemplos separados verificados.
  4. `episode-pipeline/workflows/05-deploy-verify.md` — referencia a `roadmap-[show].md`
     (que no existe para ningún show) hecha condicional.
  - Auditoría de skills (episode-launch, episode-pipeline): sin hallazgos — ambos
    `SKILL.md` bajo 50 líneas, sin archivos sueltos.

## Where We Paused

**Last action:** cierre de sesión (retrospective → skill audit → este handoff → sigue
continuity sync).
**Next action:** Andy hace el overlay manual de texto en la quote card Q4 (cambiar
"NÚMERO" por "NUMERO" sin tilde, línea 1) en un editor simple (Canva u otro) sobre el
archivo `E:\Podcast\BTQ\EP 20\BTQ Artwork EP 20\Empty_contact_center_desk_scene_202607050839.jpeg`
— la escena ya está aprobada, es solo ese overlay puntual. Luego las 4 quote cards
quedan listas para subir a redes según el plan social de `EP020-metricas-launch.md` §B.
**Blockers:** ninguno de nuestro lado. Tema de EP.021 sigue sin definir (heredado de
sesiones anteriores, no resuelto hoy).

## Files to Read First

- `btq-production/pipeline-state-ep020.md` — estado final: Stage C completa, pipeline
  publicado.
- `btq-production/pipeline-audit-ep020.md` — bitácora completa de las 5 rondas de
  validación de imágenes + Stage 4/5, útil para entender por qué las quote cards de
  EP.020 se ven distintas a las de EP.017–019.
- `.claude/skills/episode-launch/docs/brand-constants.md` §Quote Cards — nueva
  dirección de arte cinematográfica + patrones de fallo conocidos de Flow, aplica a
  EP.021 en adelante.
- `episode-pipeline/workflows/04-grid-rotation.md` — corregido con el orden real por
  show (BTQ descendente / MPD ascendente).

## Notes / Gotchas

- **El orden visual del grid NO es igual entre shows** — verificar siempre el archivo
  real antes de rotar, no asumir del ejemplo del workflow doc (ya corregido, pero
  seguir verificando en vivo por si el markup cambia).
- **Flow tiene 2 patrones de fallo conocidos y documentados ahora**: reinserta el
  anillo dorado genérico si no se banea explícitamente, y autocorrige palabras
  deliberadamente sin tilde de vuelta a la ortografía estándar. Ambos ahora tienen
  mitigación escrita en brand-constants.md — aplicarla desde el primer prompt en
  EP.021, no esperar a que falle.
- No existe `roadmap-btq.md` ni `roadmap-mpd.md` en el repo — `pipeline-state-ep[NNN].md`
  es la única fuente de verdad de estado por ahora.

## Questions to Answer

- ¿Tema de EP.021? Sigue sin definir — necesario antes de escribir el teaser real.
- ¿Confirma Andy que el overlay de Q4 ya se hizo, o sigue pendiente en la próxima sesión?
