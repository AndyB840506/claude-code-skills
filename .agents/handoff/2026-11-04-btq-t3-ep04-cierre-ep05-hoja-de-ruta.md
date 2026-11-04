# Handoff: BTQ T3 — EP.04 cerrado y en vivo, hoja de ruta del EP.05 (IA) aprobada
**Date:** 2026-11-04 (miércoles)
**Machine:** desktop (E:\)
**Status:** EP.04 cerrado. EP.05 en preproducción: hoja de ruta lista, falta fecha e invitado.
---
## What We Accomplished This Session
- Verificado: EP.04 público en Spotify (oEmbed devuelve el título), https://open.spotify.com/episode/4toaNIfokVoTlUInTLSdbt
- Web renderizada en local (Playwright, 1440 y 390 px: 6/6 imágenes, sin scroll horizontal) y
  **desplegada a producción** (`dpl_pozpfxfy9fQcH8h9XSbDeV5KmRAz`). `curl -L` del sitio + diff contra
  el local: 0 líneas. `ep04-cita-paula.jpg` 200; `ep03-cita-alejo.jpg` 404 (borrada a propósito).
- Cierre del EP.04 según Andy: Paula no confirmó el aviso de la anécdota del perro; la lámina del
  reel se quedó firmada con Paula; Adriana y Paula dijeron que NO al episodio de IA.
- Hoja de ruta EP.05 (IA en el BPO) escrita y aprobada: `btq-production/hoja-de-ruta-T3-EP05-ia.md`,
  Artifact https://claude.ai/artifact/9yz7J6mxoYn7SzVTqp6Z4x. Tronco para Andy y Alejo + bloque
  "Si hay invitado". Única cifra externa: Klarna (700 agentes en 2024, marcha atrás en 2025).
- Workflow nuevo `episode-launch/workflows/t3-hoja-de-ruta.md` (enlazado desde SKILL.md).

## Where We Paused
**Last action:** session-close.
**Next action:** cuando Andy fije fecha de grabación del EP.05 y confirme (o no) invitado, ajustar
el bloque "Si hay invitado" al perfil real y republicar el Artifact sobre la misma URL.
**Blockers:** ninguno.

## Files to Read First
- `btq-production/hoja-de-ruta-T3-EP05-ia.md`
- `.claude/skills/episode-launch/workflows/t3-hoja-de-ruta.md`

## Notes / Gotchas
- `publish_files` rechazó dos veces el `.artifact.html` escrito por python ("only files this session
  is allowed to read"), incluso después de leerlo con Read; `publish_version` con el contenido sí
  funcionó. Causa no aislada.
- Si Paula pide quitar la anécdota del perro: se edita solo la descripción en Spotify for Creators
  (la tarjeta web no la menciona).
- `t3-conversacional.md` mide 66 líneas (>50); ya estaba así, sin dividir.
- Klarna en la hoja de ruta: leída solo vía notas de prensa, no el anuncio original de 2024.

## Questions to Answer
- ¿Fecha de grabación del EP.05?
- ¿Quién es el posible invitado y qué perfil tiene (operaciones, tecnología, HR, agente)?
