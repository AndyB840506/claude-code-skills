# Handoff: QR → form con rastro en Sheet + dashboard kumatalent49

**Date:** 2026-07-09
**Status:** Complete — flujo live en producción y dashboard creado (verificado por Andres)

---

## What We Accomplished This Session

**Flujo QR → formulario con rastro (el pendiente "Sheets" del handoff 2026-07-08):**
- `kuma-talent-web` commit `c9f2e85`: soporte `?job=KT-00X` en kumatalent.com —
  fuerza modo candidato, preselecciona la vacante cuando cargan de `jobs.php` y
  hace scroll al form; código desconocido cae a "General application" (fail-soft).
  **Live verificado** (marker `PRESELECT_JOB` en producción).
- `hiresignal` commit `9c6cce3`: el botón QR del admin ahora codifica
  `SITE_URL/?job=CODE` (form con rastro Sheet/Drive); **"Copy link" conserva la
  entrevista directa** — ambas opciones disponibles. Pusheado, app 200 OK.
- QR viejos ya impresos siguen apuntando a entrevista directa — re-descargar.

**Descubrimiento de hosting:** kumatalent.com **ya migró de Vercel a DO App
Platform** (header `x-do-app-origin`; deploy-on-push desde GitHub, ~20s). El
runbook `docs/migracion-do.md` estaba stale — actualizado (commit `1265705`).
Nada de vercel CLI para este sitio.

**Dashboard del Sheet "Kuma Talent Database" (cuenta kumatalent49):**
- Sheet ID `18Q4_asLlyBO0c752nVfErHxgRKuRXDn8-LbWkJruin0`, columnas A–J
  (Date…Interview Link). doPost del apply-flow confirmado funcionando (filas
  KT-004/KT-005 con vacancy+code+link).
- Script `setupDashboard()` en `hiresignal/docs/sheet-dashboard.gs` (usa
  openById): tab Dashboard con 5 KPIs, pivot por vacante, pivot por día
  (solo candidatos) y 2 gráficas. **Andres lo ejecutó y la tab apareció.**
  Re-correrlo reconstruye la tab; nunca toca la raw.
- El web app del form quedó con 2 deployments activos (AKfycbxut… viejo = el
  que usa el sitio; AKfycbzUB… nuevo innecesario) — no borrar el viejo.

**Retrospective + audit aplicados:**
- `deploy-preflight`: Paso 4 ahora identifica el host real por headers (no
  confiar en docs del repo) y SKILL.md ampliado a deploys no-Vercel.
- Memoria `feedback_confirm_ids_before_deploy`: al pedir IDs de Google, mostrar
  la forma de la URL con el pedazo resaltado; Apps Script Run ≠ Deploy.
- Memorias nuevas: `kumatalent_sheet_dashboard`, `kumatalent_web_hosting_do`;
  actualizada `project_hiresignal_jd_conventions` (QR vs Copy link).
- Re-saves de las 4 vacantes en admin: **Andres los hizo** (2026-07-08 noche).

## Where We Paused

**Last action:** Session close (retrospective → audit → este handoff).
**Next action:** Nada técnico pendiente. Del lado de Andres: limpiar las filas
de prueba del Sheet raw (dijo que lo hace él) y, opcional, una entrevista de
prueba para ver el assessment FR + badges en el PDF.
**Blockers:** Ninguno.

## Files to Read First

- `C:\Users\andre\repos\hiresignal\docs\sheet-dashboard.gs` — script del
  dashboard (fuente de verdad si hay que ajustar métricas/gráficas).
- Memoria `kumatalent_sheet_dashboard` — ID del Sheet, columnas, deployments.
- Memoria `kumatalent_web_hosting_do` — cómo se deploya el sitio ahora (push).

## Notes / Gotchas

- **kumatalent.com = DO deploy-on-push** — `git push origin master` publica en
  ~20s. El flujo Vercel prebuilt del runbook quedó obsoleto.
- **hiresignal sigue auto-deployando con push a master** — push solo con OK.
- El Sheet NO está compartido con berandre2 → no accesible vía MCP de Drive;
  cambios al Sheet van por Apps Script que corre Andres.
- Si se ajusta el dashboard: editar el .gs local, pasarle el código completo a
  Andres para pegar y re-correr `setupDashboard` (idempotente).

## Questions to Answer

- ¿Hard-reject por francés "basic" en roles que lo requieren? (hoy solo inglés
  tiene hard-reject; arrastrado del handoff 2026-07-08).
- Paso 6 del runbook DO: ¿ya se removieron los dominios del proyecto Vercel
  viejo? (limpieza opcional, solo tras estabilidad).
