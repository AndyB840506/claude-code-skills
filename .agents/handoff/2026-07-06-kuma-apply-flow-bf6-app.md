# Handoff: Kuma Apply Flow (live) + BF6 Meta Ops App
**Date:** 2026-07-06 (tarde — segunda sesión del día; la de la mañana cerró en
`2026-07-06-memory-corruption-hardening.md`)
**Status:** Complete
---
## What We Accomplished This Session

### Kuma Talent — pipeline aplicación → entrevista, LIVE y verificado E2E
- Sociedad con Hugo **reactivada** (la memoria decía radio-silent/LuccaTech — ya no).
  Kuma Flow sigue solo-concepto, en stand-by por costos (GoHighLevel ~$407/mes).
- **Flujo completo live:** kumatalent.com → selector de vacantes (leído en vivo de
  `api/jobs.php`) → `api/apply.php` genera invite único de 7 días → entrevista
  instantánea + email de respaldo enviado por el Apps Script (kumatalent49).
  Verificado de punta a punta incluyendo el email real en Gmail.
- Nuevos endpoints en `hiresignal`: `api/jobs.php`, `api/apply.php`,
  `api/site-cors.php` (CORS origin-locked). Docs en `hiresignal/docs/apply-flow.md`.
  Commits `11ef3a6` (endpoints) — deploy automático DO al pushear master.
- `kuma-talent-web/index.html`: selector de vacante + flujo de 2 llamadas fail-soft
  (si HireSignal cae, el lead va igual al Apps Script). Commits `ffb4a1c`+`16feda9`.
  **Deploy Vercel = flujo PREBUILT obligatorio** (`ignoreCommand: exit 0` → un
  `vercel --prod` normal da 404): `vercel pull` → `vercel build --prod` →
  `vercel deploy --prebuilt --prod` (auto-aliasea al apex).
- **Gotcha Apps Script:** el usuario creó un deployment NUEVO (URL cambió) en vez de
  versionar el existente — la web quedó apuntando al URL nuevo (`AKfycbxutVyb…`).
  Si el form deja de loggear, revisar URL vs deployment activo primero.
- Decisiones: LinkedIn scraping descartado (ToS/ban risk — X-ray search manual para
  perfiles senior); piloto de scraping FB Groups parqueado (publicar EN los grupos
  gratis > scrapearlos); validez de invites del web-apply = **7 días** (juicio mío,
  usuario no objetó; es un número en `api/apply.php`).

### BF6 Meta Ops — de skill borrada a app interactiva (3 iteraciones de feedback)
- `bf6-meta-configurator` estaba **borrada desde el 7 de junio** (purga de huérfanas,
  commit `ed5ed3b`) — restaurada de git y reconstruida completa.
- **Modelo final = APP, no reporte:** `E:\Claude Output\bf6\bf6-meta-app.html`
  (path estable, inglés siempre). Mode MP/REDSEC, playstyle, class filter y platform
  se eligen EN la app (localStorage); cards clickeables abren builds con nombres
  propios de attachments; settings por plataforma (PC/PS5/Xbox distintos de verdad)
  + bloque override REDSEC; chip de edad de datos que se auto-marca STALE a los 60
  días. La skill quedó como **refresher**: `bf6` = re-fetch + regenerar mismo archivo.
- Receta de datos codificada en `workflows/run-report.md`: bfhub.gg/meta/mp+br
  obligatorios (única fuente con nombres exactos de attachments en bulk), pase de
  búsqueda POR ARMA (los summaries de búsqueda traen builds completos), pase
  comunitario Reddit/social obligatorio, guías de settings por plataforma.
  Commits `0b6ea03` → `f989fd7` → `0bd6084`.

### Memoria + reglas
- Memoria actualizada y committeada: `reference_kuma_infra` (apply flow + gotcha),
  `reference_deploy_mechanisms` (prebuilt kumatalent), nueva
  `user_communication_register` (chistes/referencias = sabor, NO órdenes — pedido
  explícito del usuario para los "hermanos mensos").
- Retrospective aplicada a `CLAUDE.md` del workspace: excepción de escrituras
  byte-exactas (BOM de `Set-Content -Encoding UTF8` en PS 5.1) y footgun de
  `curl -L -X POST` (411 tras redirect).

## Where We Paused
**Last action:** Session-close — retrospective y audit aplicados; escribiendo handoff.
**Next action:** Pasos 4-5 del cierre (continuity sync + baseline check — el conteo
de skills subió a 26, va a disparar memory-audit).
**Blockers:** Ninguno.

## Files to Read First
- `hiresignal/docs/apply-flow.md` — el contrato del flujo apply (endpoints, Apps
  Script, fail-soft).
- `bf6-meta-configurator/SKILL.md` + `workflows/run-report.md` — modelo app +
  receta de datos con los 3 pases.
- `memory/user_communication_register.md` — cómo leer al usuario (sabor vs orden).

## Notes / Gotchas
- **Sheet de Kuma:** quedan filas de prueba por borrar (una del deployment viejo sin
  columnas nuevas + "Andres Bermudez (PRUEBA E2E)"); 2 invites de prueba en admin →
  Invites (expiran solos el 13-jul); el deployment viejo del Apps Script
  (`AKfycbzj2R2…`) conviene archivarlo.
- El guard del sandbox bloquea comandos PowerShell compuestos que mezclan rutas de
  `E:\` con espacios y `Remove-Item` — separar en llamadas simples.
- bfhub builds tienen fechas individuales oct-nov 2025 (página mantenida, updated
  hoy) — tras el rework de recoil del 1.3.3.0, verificar feel; Match Grade ammo
  ahora +100% drag (⚠ en los builds de snipers).

## Questions to Answer
- Siguiente paso natural de Kuma: aviso gratis en Computrabajo (Asistente Virtual,
  calibrado con el benchmark) apuntando al form — pendiente de que el usuario quiera.
- ¿Los 7 días de validez del invite web-apply se quedan? (default mío, fácil cambiar.)
