# Handoff: BTQ EP.027 cerrado + EP.028 fijado como Ley de Little

**Date:** 2026-08-23
**Machine:** desktop (E:\)
**Status:** Complete — EP.027 verificado en vivo y cerrado; EP.028 replanificado, sin guion
todavía.

---

## What We Accomplished This Session

- **Clip de audio para redes de EP.027**, que había quedado pendiente: extraído del máster
  limpio, momento "el ascenso dejó de ser una asignación de cargo y se volvió una forma de
  pago" (quote card 3, 24:42.8–25:25.0, 42.2s). Verificado con `volumedetect`: audio real,
  no silencio.
  - **Primer intento quedó en la ubicación/nomenclatura equivocada** (`E:\Podcast\BTQ\EP 27\
    BTQ Artwork EP 27\social-clip\..., .mp3` sin `.wav`) — nunca grepeé el propio kit de
    skills (`.claude/skills/episode-launch/workflows/step2-generate-assets.md` §E), que ya
    documentaba el paso completo (verificado en EP.025). Corregido en la retrospectiva:
    reubicado a `E:\AI\outputs\BTQ-EP027\BTQ-EP027-CLIP-Q3.wav/.mp3`.
- **EP.027 verificado en vivo y el ciclo cerrado.** Artículo, og-image, índice de episodios
  y sitemap confirmados con curl (200 / contienen el slug); `vercel inspect` confirma el
  build de producción del 08-20 aliasado a `behind-thequeue.com`. El primer intento de
  verificar el índice dio un falso negativo por no usar `curl -L` sobre un redirect 308 —
  cachado antes de reportarlo, documentado en `CLAUDE.md` § "Instrumentos que mienten en
  silencio".
- **EP.028 pasó a ser la Ley de Little** (John D. C. Little, 1961), adelantada desde EP.031.
  Motivo: EP.027 ya salió en vivo con el teaser grabado ("la próxima vez les traigo la Ley
  de Little"), y esa promesa quedó pública — antes de esta sesión no lo estaba, así que la
  nota que decía "no obliga a ninguna fecha" (2026-08-01) dejó de ser cierta. Rompe a
  propósito la rotación 3+1 (Pilar SEO justo después de otro Pilar SEO); los Oficio de Jefe
  #4-6 se corrieron un puesto (EP.029-031). Confirmado explícitamente por Andrés tras
  presentarle la tensión con 3 opciones.
- **Retrospectiva corrida** — 2 hallazgos aplicados: (1) fix del clip de EP.027 + memoria
  nueva `reference_btq_social_clip_step.md` apuntando al paso ya documentado; (2) nueva
  entrada en `CLAUDE.md` sobre `curl` sin `-L` en redirects.
- Skill Management Audit: 0 hallazgos (triggers, tamaño de SKILL.md, encoding, duplicados).
- Commits: `3e127c9`, `3d0ef89`, `01fd776`, `90746d0` — todos pusheados.

## Where We Paused

**Last action:** commit + push de los fixes de retrospectiva (`90746d0`).
**Next action:** decidir si arrancar Stage A de `episode-pipeline`/`episode-launch` para
EP.028 (guion de la Ley de Little) — **no se empezó**, solo se movió el roadmap.
**Blockers:** ninguno técnico.

## Files to Read First

- `btq-production/roadmap-btq.md` — fila de EP.028 (Little) y la nota de excepción a la
  rotación 3+1, ambas nuevas de hoy.
- `btq-production/launch-assets/EP027-peter-launch.md` §D/F — clip corregido, checklist
  verificado en vivo.
- `.claude/skills/episode-launch/workflows/step2-generate-assets.md` §E — el paso de clip
  de audio, para cualquier episodio futuro (BTQ ya lo tiene, no reinventarlo).

## Notes / Gotchas

- El clip viejo (ubicación equivocada) se borró físicamente de disco (`E:\Podcast\BTQ\EP 27\
  BTQ Artwork EP 27\social-clip\`) — no queda copia ahí, solo en `E:\AI\outputs\BTQ-EP027\`.
- Little's Law como EP.028 **no tiene guion todavía** — solo el teaser de 2 frases grabado
  dentro de EP.027 y la fuente confirmada (Little 1961, *Operations Research* 9(3):383-387).
  Falta todo el trabajo de Stage A (sourcing de casos, guion, verificación de fuentes).
- Pendiente sin urgencia, ya anotado en `EP027-peter-launch.md`: registrar en
  `guion-style-btq.md` § Calibración de duración el factor real del esqueleto TRENZADO
  (+11,4% en EP.027, +3,4% en EP.026).

## Questions to Answer

- ¿Arrancar ya el guion de EP.028 (Ley de Little) o esperar a que Andy publique el resto
  del calendario social/YouTube/LinkedIn de EP.027 primero?
