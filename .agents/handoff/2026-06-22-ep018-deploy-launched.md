# Handoff: EP.018 BTQ (El Mundial) — deploy + lanzamiento completo (pipeline cerrado)

**Date:** 2026-06-22
**Status:** Complete — EP.018 publicado en Spotify y en vivo en behind-thequeue.com (HTTP 200 verificado). Pipeline de punta a punta cerrado (`stage_c: complete`). Quedan pendientes NO bloqueantes de hilos previos (ver Next Steps).

---

## What We Accomplished This Session

Se retomó el handoff del 2026-06-19 (EP.018 bloqueado esperando publicación en Spotify del dom 21). Andy confirmó publicado y se corrió el tramo final del pipeline:

- **Stage 4 — Grid rotado** en `btq-production/website/index.html`: de `013, 014, 015, 016` a **`014, 015, 016, 017`**. Entra EP.017 (Soda Stereo/Cerati), sale EP.013 (Back to the Future). EP.018 NO va al grid (su embed lo cubre).
- **URL Spotify EP.017 rescatada:** nunca se había registrado (figuraba `pending` desde su lanzamiento el 14-jun). Andy la pasó desde el browser → `https://open.spotify.com/episode/0LJ22lLMgfWh3wLbbgNhxC`. Propagada a su launch file (línea 5 + 3 CTAs) + roadmap.
- **URL Spotify EP.018:** `https://open.spotify.com/episode/6PC4QIDiAwmVZJ1BV5PYcx`. Propagada a su launch file + roadmap + checkpoint.
- **Setup de deploy en el PORTÁTIL (PC nuevo, sin entorno):** instalé Vercel CLI 54.15.0, Andy hizo `vercel login` (team `mrputridsden`), y recreé el link a mano en `btq-production/website/.vercel/project.json` (projectId `prj_SIXnUYNlwet3DbAVlKpDrV353f3U`, orgId `team_hF19vFjfS0vMqSqSM4W8YQCy`) — SIN `vercel link` (corrompe el repo.json del monorepo). projectId vía `vercel project inspect`, orgId vía API `/v2/teams`.
- **Stage 5 — Deploy + verificación:** preflight PASS → gate aprobado por Andy → `vercel --prod --yes --cwd btq-production/website` (NODE_OPTIONS=--use-system-ca) → aliased a behind-thequeue.com → **HTTP 200** + grid en vivo confirma EP.017 presente / EP.013 fuera. Spotify PASS (informativa, confirmado por Andy).
- **Bitácora** `pipeline-audit-ep018.md` con Stage 4 + Stage 5; checkpoint `stage_c: complete`.
- **Commit + push:** `5d7fd46` (6 archivos: index.html, roadmap, 2 launch files, state, audit).
- **Retrospective aplicada (2 reglas, aprobadas por Andy):**
  - `deploy-preflight/workflows/checks.md` Paso 2: ruta de recuperación "máquina nueva / sin link" (instalar CLI, login, sacar IDs, escribir project.json a mano).
  - `episode-pipeline/workflows/04-grid-rotation.md` Paso 0: validar también la URL del episodio que ENTRA al grid (el anterior), no solo el que se lanza — puede estar `pending` aunque el nuevo esté en vivo (caso EP.017).
- **Audit de skills:** limpio (todos los SKILL.md ≤50 líneas; sin loose files; sin corrupción).
- **Memoria nueva:** `reference_btq_vercel_deploy_laptop` (setup de deploy BTQ en el portátil + IDs).

## Where We Paused

**Last action:** retrospective aplicada + audit limpio + este handoff (las 2 ediciones de skills NO están commiteadas todavía — el handoff las incluirá en su commit).
**Next action:** nada bloqueante. EP.018 está 100% lanzado. Lo siguiente del roadmap BTQ es EP.019 (Gladiator/Máximo).
**Blockers:** ninguno.

## Files to Read First

- `btq-production/roadmap-btq.md` — EP.017 y EP.018 = `publicado` con URLs; siguiente = EP.019 Gladiator
- `btq-production/pipeline-audit-ep018.md` — bitácora completa (Stage 0→5)
- `~/.claude/projects/.../memory/reference_btq_vercel_deploy_laptop.md` — cómo deployar BTQ en el portátil

## Notes / Gotchas

- **El portátil NO tiene E:** (audio/artwork viven en E: en el escritorio). Para deploy de webs no importa (los sitios están en el repo en C:). Para procesar audio/imágenes de un episodio nuevo hay que estar en el escritorio o tener E:.
- **El `.vercel/` se pierde con cada cambio de PC** (gitignored). Recrear con la receta de `reference_btq_vercel_deploy_laptop`. No usar `vercel link` desde subdir.
- **Reincidencia PS 5.1:** volví a usar inline-`if` en PowerShell y falló (ya está en memoria `feedback_ps51_syntax`). Recordar: nada de inline-if, usar bloques `if {} else {}`.
- **EP.016 launch file** todavía dice `spotify_url: pending` (stale) aunque EP.016 está publicado — housekeeping menor, no crítico.

## Questions to Answer (al retomar)

- ¿Alguno de los next steps ya se hizo? (preguntar antes de asumir)
- **EP.018 quote cards (4):** ¿Andy ya las generó en Flow? (prompts en §E de `EP018-mundial-launch.md` — pendiente NO bloqueante de hilos previos; requiere Flow + revisión visual rápida).
- **andyfreelancer.com** (handoff 2026-06-19, otra sesión): ¿llegó el correo de prueba a `hello@`? ¿se pidió indexación de `/` en Search Console?
- **MPD EP.005:** sigue sin grabar (de handoffs anteriores).
- ¿Arrancamos EP.019 (Gladiator/Máximo)?
