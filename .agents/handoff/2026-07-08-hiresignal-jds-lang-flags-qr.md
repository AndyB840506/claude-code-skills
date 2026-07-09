# Handoff: HireSignal — JDs EN/FR, flags de idioma por vacante, QR público

**Date:** 2026-07-08
**Status:** Complete — todo live en producción y verificado por Andres

---

## What We Accomplished This Session

**Catálogo de vacantes (repo `C:\Users\andre\repos\hiresignal`, jobs.json + admin):**
- 4 JDs nuevas **KT-001..KT-004** (Software Developer, Administrative Assistant,
  Sales Rep B2B/B2C inbound+outbound, CX Rep) — descripciones en inglés, foco
  **EN/FR con español opcional**, remoto LatAm o Canadá, **salarios siempre en CAD**
  (regla nueva, aplicada también a legacy), full-time availability en admin/CX
  (clientes real estate). Legacy KT-001..006 en español removidos del seed local
  (viven en git history y en la DB de producción).
- Andres ya subió/actualizó las vacantes en el admin de producción.

**Feature: evaluación de idiomas por vacante (commits `f7fa4a9` + `86ac473` + merge `f949247`):**
- 3 checkboxes independientes en admin → edit: Assess English / French / Spanish
  (defaults EN ☑ FR ☑ ES ☐). Idioma desmarcado = no se evalúa ni se reporta.
- Stage 3 renombrado `english_assessment` → `language_assessment`; cambia al
  idioma requerido no-primario 3-4 intercambios; se salta si no hay idiomas.
- Engine devuelve `english_level` + `french_level` + `spanish_level` (schema
  enforced); PDF muestra badges EN/FR/ES; ATS `bilingual-fluent` exige EN y FR.
- Dropdown de idioma de entrevista: Auto (EN/FR) / English / French — español
  salió como idioma de conducción (legacy `spanish` cae a auto).
- Verificado: `php -l` en 9 archivos + smoke test CLI de 20 checks (scratchpad).

**Merge con el desktop:** el clon local estaba ~40 commits stale (reskin Kuma,
QR invites, engine hardening, apply-flow). Merge con 4 conflictos resueltos
conservando ambos lados (saludo bilingüe adaptado a EN/FR, grading estricto
extendido a FR/ES, paleta Kuma en PDF).

**QR público por vacante (commit `bd46b9f`):** botón "QR" en admin → Jobs que
renderiza y descarga PNG del link público reutilizable
(`PUBLIC_BASE_URL/index.php?code=KT-00X`). Imprimible/publicable — distinto de
los QR de invites (secretos de un solo uso). Verificado live por Andres.

**Retrospectiva aplicada:** CLAUDE.md (fetch de repos externos antes del primer
edit), memorias nuevas `feedback_kuma_salary_cad`, `feedback_pull_target_repo_first`,
`project_hiresignal_jd_conventions`.

## Where We Paused

**Last action:** Session close (retrospectiva + audit + este handoff).
**Next action:** Nada técnico pendiente en HireSignal. Del lado de Andres:
los 4 re-saves en admin (abrir cada vacante → confirmar checkboxes → Save)
si no los hizo ya, y una entrevista de prueba para ver el assessment FR + badges.
**Blockers:** Ninguno.

## Files to Read First

- `C:\Users\andre\repos\hiresignal\config.php` — `buildLanguageDiagnosticSection`
  + `buildLanguageInstruction` (corazón del feature de idiomas).
- `C:\Users\andre\repos\hiresignal\docs\apply-flow.md` — flujo de aplicación web
  ya construido (base para el QR → formulario, ver Questions).
- Memoria `project_hiresignal_jd_conventions` — las 5 convenciones de producto.

## Notes / Gotchas

- **hiresignal auto-deploya con push a master** — commit local libre, push solo
  con OK de Andres.
- **Fetch de repos externos ANTES del primer edit** — regla nueva en CLAUDE.md;
  esta sesión pagó 4 conflictos por no hacerlo.
- Vacantes guardadas con el schema viejo: el runtime les aplica defaults
  (EN ☑ FR ☑ ES ☐), pero un `requires_english: false` explícito guardado con el
  form viejo SÍ apaga el assessment de inglés — por eso los re-saves.
- Las override rules del desktop rechazan duro si inglés demostrado = "basic"
  en rol que lo requiere; respetan el checkbox. Francés NO tiene hard-reject
  (solo reporta nivel) — decisión pendiente si algún día lo quieren.

## Questions to Answer

- **QR → formulario web con rastro en Sheet/Drive:** el QR actual va directo a
  la entrevista (no deja fila en el Sheet de kumatalent49). Si lo quieren,
  apuntar el QR al form de kumatalent.com con vacante preseleccionada — backend
  ya existe (`apply-flow.md`), falta el param de preselección en kuma-talent-web.
- **Sheet kumatalent49:** Andres lo organiza él mismo — una pestaña raw + pivot
  table con gráficas (acordado; no repartir data en pestañas por fecha/JD).
- ¿Hard-reject por francés "basic" en roles que lo requieren? (hoy solo inglés).
