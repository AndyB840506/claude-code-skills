# Handoff: EP.018 BTQ (El Mundial) — guion con chispa + calibración de wpm

**Date:** 2026-06-19
**Status:** In progress — guion EP.018 escrito, calibrado (143 wpm) y expandido con carne verificada; lint pasa. Andy lo está LEYENDO para dar veredicto de chispa. Reglas de wpm + veracidad aplicadas a las guías; ediciones de ESTILO de la guía BTQ pendientes de su lectura.

---

## NEXT STEP principal (dirección de Andy)

**Esperar el veredicto de chispa de Andy sobre el guion EP.018.** Él dijo "ya lo leo". Cuando responda:
1. Si aprueba la chispa → iterar `guion-style-btq.md` con las ediciones de ESTILO que faltan (quedaron en pausa a propósito).
2. Si pide ajustes al guion → aplicarlos sobre `EP018-mundial-guion.html`.
3. Confirmar el título final (propuesto: "El Mundial: liderazgo cuando no puedes tocar el balón").

---

## What We Accomplished This Session

- **EP.018 BTQ "El Mundial" — guion escrito desde cero** (`btq-production/launch-assets/EP018-mundial-guion.html`). Un solo episodio (no 2 partes, por ser adquisición + ventana cultural). Ángulo: *el técnico no puede tocar el balón* = el supervisor que no atiende la llamada. Columna vertebral = 4 palancas (preparar · elegir · ajustar · confiar).
- **Carne 100% verificada vía web:** Bielsa (Spygate 2019 + ~1.800 cintas), Van Gaal/Krul 2014 (cambio de arquero solo para penaltis), Obdulio/Maracanazo 1950 (200 mil, periódicos pre-impresos, discurso de Rimet ensayado), Pékerman/Colombia 2014 (3 victorias históricas → 4 seguidas; gol Puskás de James), Maturana 5-0 del 93 (con el matiz de "perder es ganar un poco"). Segmento nuevo de Referencias Cruzadas: **Benjamin Zander** (el director de orquesta que no produce sonido) + **Ferguson** (26 años).
- **Calibración de tiempos (el gran fix):** medido contra el SRT real del EP.17 → **ritmo de Andy ≈ 143 wpm** (6.062 palabras / 42,3 min). El marcado por minutos a ojo venía inflado (~90 wpm) → por eso terminaba 15 min antes y estiraba. EP.18 v1 tenía 4.213 palabras (~29 min). **Reescrito a 7.033 palabras = ~49 min puros / ~57 con su expansión natural en vivo (~15%).**
- **Lint BTQ pasa:** 4 remates, 0 puentes prohibidos, 0 meta-anuncios, 0 muletillas, 0 cadenas de guiones largos, refrán textual 3/3, 4 momentos de humor, datos verificados.
- **Retrospective aplicada (2 reglas, aprobadas por Andy):**
  - `guion-style-btq.md`: nueva sección "Calibración de duración" (143 wpm, tabla palabras→min, ajuste por expansión, cómo medir, recalibrar) + bullet de lint + **regla 6 extendida** (episodios atados a momento cultural: anclar en histórico, marcar el evento vivo `[ACTUALIZAR AL GRABAR]`, no inventar resultados más allá del corte de conocimiento).
  - `podcast-creator/workflows/01-episodio.md`: el `word_count_target` ahora exige wpm MEDIDO contra SRT real (no adivinado) + verificación post-grabación.
- **Audit de skills:** limpio (todos los SKILL.md ≤50 líneas, sin archivos sueltos, sin corrupción).

## Where We Paused

**Last action:** session-close (retrospective aplicada → audit limpio → este handoff).
**Next action:** esperar el veredicto de chispa de Andy y, según eso, iterar el estilo de la guía o ajustar el guion (ver NEXT STEP).
**Blockers:** ninguno técnico. Solo se espera la lectura/veredicto de Andy.

## Files to Read First

- `btq-production/launch-assets/EP018-mundial-guion.html` — el guion entregado (lo que Andy está leyendo)
- `btq-production/guion-style-btq.md` — la guía; ya tiene Calibración de duración + regla 6 extendida; faltan ediciones de estilo si aprueba
- `btq-production/roadmap-btq.md` — EP.018 sigue "en roadmap" (actualizar a "guion listo" cuando se confirme)
- `.claude/skills/podcast-creator/workflows/01-episodio.md` — Paso 2 ahora con regla de wpm medido

## Notes / Gotchas

- **143 wpm es el número de oro para BTQ (Andy solo host).** Dimensionar SIEMPRE en palabras, no en minutos a ojo. Recalibrar contra SRTs futuros. NO asumir que MPD usa el mismo (es co-host; medir aparte).
- **Marcadores intencionales en el guion EP.018** (para Andy al grabar, NO son TODOs de código): 3× `[ACTUALIZAR AL GRABAR]` (dato fresco del Mundial 2026 en curso, sin inventar resultados — Andy está más allá del corte de conocimiento del modelo) y 1× `[VERIFICAR]` (título en español del libro de Ferguson "Leading" 2015; fallback = "Good to Great" de Collins).
- **EP.018 = 1 solo episodio** (decisión deliberada): adquisición de oyentes nuevos vía social + ventana del Mundial = compartible de una sentada, no 2-partes.
- **Commit incluye un cambio ajeno a esta sesión:** `docs/roadmap-future-proofing.md` (re-confirmación de "graphify ligero/visual", fechado 19-jun) estaba sin commitear; se incluyó para no perderlo.
- EP.005 MPD sigue sin grabar (del handoff anterior). EP.017 grabado, pendiente de verificar si ya salió en Spotify.

## Questions to Answer (al retomar)

- ¿Alguno de los next steps ya se hizo? (preguntar antes de asumir)
- ¿Veredicto de chispa de Andy sobre EP.018? ¿Qué ediciones de estilo entran a la guía?
- ¿Se confirma el título "El Mundial: liderazgo cuando no puedes tocar el balón"?
- ¿EP.018 pasa a "guion listo" en el roadmap-btq?
- ¿Andy grabó algo de EP.005 / EP.017 ya está en Spotify?
