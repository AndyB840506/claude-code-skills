# Handoff: HireSignal multi-frente + kumatalent bilingüe (sesión con delegación)

**Date:** 2026-07-10
**Status:** Complete — todo deployado y verificado live; 1 env var pendiente del lado de Andres

---

## What We Accomplished This Session

Primera sesión con el **modelo delegado** (Fable orquesta, ejecutores Sonnet en
background — ver memoria `user_delegation_model`). Todo en producción:

**HireSignal (`C:\Users\andre\repos\hiresignal`, commits `f02c03b`..`0ef4e6d`):**
- **Admin responsive móvil** (7 páginas, solo CSS): tablas con scroll horizontal en
  vez de recorte, stat-bar con wrap, login fluido, edit a 1 columna, @media 640px
  por página. Verificado live (CSS nuevo servido).
- **Hard-reject francés**: `assess_french` + `french_level==='basic'` → REJECT
  forzado (espejo del inglés, prompt + override determinístico). Smoke test 6/6.
  OJO: checkbox "Assess French" ahora implica requisito duro. Los ports JS de
  `tests/` NO se actualizaron (paridad pendiente si se corren evals).
- **`analysis_summary` persistido** por entrevista (8 dimensiones, niveles EN/FR/ES,
  strengths/concerns/quotes) — antes se descartaba tras el PDF. Contrato compartido
  con el ranking. Entrevistas pre-07-10 no lo tienen.
- **History**: filtro por vacante + **Delete backup-first** (borra solo si ≥1 canal
  de backup responde OK; canales: Drive vía Apps Script `docs/backup-webapp.gs` +
  email con adjuntos a kumatalent49@gmail.com con CC al recruiter). Filas por
  `_dbid` (serial de Postgres expuesto en lectura). **E2E verificado por Andres**:
  fila vieja borrada, correo llegó.
- **Ranking**: fila expandible con badges de idioma, barras de dimensiones,
  strengths/concerns/quotes inline (solo entrevistas nuevas).
- **Barrido de salud del stack**: 10 checks GET, todo sano.

**kumatalent.com (`C:\Users\andre\repos\kuma-talent-web`, commit `9a391e8`):**
- Bio de Andres reescrita con datos reales de su CV (arco agente→regional manager,
  100+ FTEs, $50M portfolios, "built HireSignal") + copy de HireSignal vendiendo los
  diferenciadores reales (adaptativo, detecta libreto, EN/FR en vivo).
- **`fr.html`**: versión FR-CA nativa completa + toggle EN/FR + hreflang. Ver
  memoria `reference_kumatalent_bilingual` — **TODO cambio a index.html debe
  replicarse en fr.html**.

**Infra:** dominio kumatalent.com removido del Vercel viejo (DNS verificado en DO
antes y después; rollback Vercel ya NO existe — memoria actualizada).

## Where We Paused

**Last action:** Session close (retrospectiva aplicada, audit sin hallazgos, este handoff).
**Next action (Andres):** poner env var `BACKUP_WEBAPP_URL` en DO → app hiresignal →
Settings → App-Level Env Vars, valor:
`https://script.google.com/macros/s/AKfycby-hhrnDr02Cqk924uZl0K0u7-1iZ4wsIxLyAhjcS-BjhH7UfuGj2WhHSK2tgwyWMUsJA/exec`
(el Apps Script ya está deployado y verificado con ping). Sin la var, el canal Drive
reporta "unavailable" y el backup viaja solo por email (funciona igual).
**Blockers:** Ninguno.

## Files to Read First

- Memoria `user_delegation_model` + `feedback_delegation_verify_artifacts` — cómo
  trabajar el modo delegado sin comerse claims falsos de ejecutores.
- Memoria `reference_kumatalent_bilingual` — la trampa de sincronía index/fr.html.
- `C:\Users\andre\repos\hiresignal\api\backup-lib.php` — flujo completo del
  backup-before-delete (canales, gate, gotcha del 302 de Apps Script).

## Notes / Gotchas

- **Exploradores/executors: pull del repo ANTES de lanzarlos** (regla ampliada en
  CLAUDE.md — hoy un explorador mapeó el árbol stale y reportó un feature existente
  como inexistente).
- Un ejecutor reportó "17/17 PASS" de un test que no existía — verificación de
  ejecutores SIEMPRE re-corrida por el orquestador.
- Este desktop no tiene PHP ni Docker: PHP portable descargado al scratchpad para
  `php -l` y smoke tests (windows.php.net, zip NTS x64).
- Los PDFs de entrevistas pre-2026-07-07 son irrecuperables; el delete respalda solo
  metadata.json en esos casos (el confirm lo avisa).
- Los correos de backup salen a kumatalent49@gmail.com (cuenta archivo) con CC al
  recruiter email de Settings.
- Chequeo de "PDF perdido" en History = 1 query por fila con PDF; ok a escala
  actual, optimizar si el historial llega a cientos.

## Questions to Answer

- ¿Actualizar los ports JS de `tests/` con la regla FR (paridad de evals)?
- ¿Títulos de vacantes bilingües en el dropdown del apply form? (hoy llegan en EN
  desde `api/jobs.php`).
- Validación visual pendiente de Andres: admin responsive en celular + repaso final
  del francés de fr.html.
