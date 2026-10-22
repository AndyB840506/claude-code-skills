# Handoff: HireSignal — 1.6.0 → 1.8.0 en producción, 3b-2a (1.9.0) listo sin desplegar
**Date:** 2026-10-22 (jueves)
**Machine:** desktop (E:\)
**Status:** In progress. 3b-2a construido y verificado en la rama `feat/3b2a-report-language` @ `5c54ffb` (pusheada), **sin desplegar**: falta el OK de Andrés.

---

## What We Accomplished This Session
- **1.6.0 en producción** (sprint 3, ES/PT del lado candidato). Paso 4 cerrado con 3 entrevistas reales (ES/PT/auto, ADVANCE 77/80/84).
- **1.7.0 en producción** (3b-1): campañas a candidatos en es-419 y pt-BR, idioma elegido por campaña en vacantes auto (`candidate_campaigns.email_language`), **moneda de la paga** como campo de la vacante, baja y "demasiadas solicitudes" en ES/PT. Migración confirmada por Andrés en prod.
- **1.8.0 en producción**: re-skin con la paleta oscura del sitio (`redesign-hiresignal`), Geist alojada en `assets/fonts` (OFL), logo claro, logo de cliente sobre placa hueso. Andrés revisó las páginas con Postgres: OK.
- **3b-2a construido (sería 1.9.0)**: Settings → Report language; PDF + análisis del modelo + correos del reporte y del ranking en el idioma de la cuenta (`recruiter-i18n.php`, `rt()`); citas del candidato nunca traducidas; copia al candidato en el idioma de sus pantallas (antes siempre inglés). Inglés idéntico a 1.8.0 (prompt con huella sha256 fija en `tests/report-language.test.php`; PDF/correos/transcripción diffeados con `tests/tools/report_render.php`). Suite 1632/0, 12/12 mutaciones, prueba real con Opus en ES/PT/FR.
- Scripts de verificación ahora en `hiresignal/tests/tools/` (README ahí).
- 2 reglas nuevas en `CLAUDE.md` del kit (tests que buscan frases en el código; contar la entrada antes de una corrida pagada).

## Where We Paused
**Last action:** `/session-close` (Andrés pidió cerrar por límite de sesión).
**Next action:** preguntar a Andrés si despliega la **1.9.0** (rama `feat/3b2a-report-language`): subir `APP_VERSION` a 1.9.0 en `config.php`, fast-forward a master, push, health estable, captura en vivo. Después, planear **3b-2b** (páginas del admin).
**Blockers:** el deploy necesita OK explícito de Andrés.

## Files to Read First
- `hiresignal/.agents/build-state/sprint3b-idiomas.md` — decisiones, planes y DoD de 3b-1 y 3b-2a.
- `hiresignal/CHANGELOG.md` — [1.9.0] (sin desplegar), [1.8.0], [1.7.0].
- `hiresignal/recruiter-i18n.php` — catálogo del lado reclutador (3b-2b lo extiende).
- Memorias `project_hiresignal_sprint3_idiomas`, `project_kuma_pivot_hiresignal_only`.

## Notes / Gotchas
- **Decisiones de Andrés para 3b-2b:** idioma = ajuste por cuenta (ya existe, `ACCOUNT_LANGUAGE`); **Outreach no se traduce**; ~825 textos medidos en el admin. La consola sigue en inglés (`verdictDisplay()` en `_shell.php`; `rtVerdict()` traduce sus etiquetas para el correo del ranking).
- Tamaños del PDF: etiquetas de dimensión ≤ 22 caracteres (tarjetas), veredictos ≤ 26 (insignia); el test lo hace cumplir. El inglés ya truncaba y se dejó igual para no romper la identidad con 1.8.0.
- Francés: `recruiterText()` mete U+00A0 antes de `: ; ! ?`.
- Los tests que extraen funciones de `report.php`/`ranking.php` necesitan `require_once recruiter-i18n.php`.
- Timeout de 90 s del chat (`_luccaPost`, `config.php`) disparó una vez el 10-21; no se repitió. Anotado, sin cambio.
- Machine-bound: copias E2E y capturas en el scratchpad de esta sesión (se pierden si se limpia `%TEMP%`; se regeneran con `tests/tools/make_e2e.py`). Siguen sin trackear 3 archivos en `hiresignal/docs/` (FAQ PDF/HTML y costos whitelabel vs RecruitX): no son del sprint, no tocados.
- Orden de producto (Andrés): terminar la base → luego publicar kumatalent.com (`redesign-hiresignal`); `/try` depende de la demo (sprint 4).

## Questions to Answer
- ¿Deploy de 1.9.0?
- ¿Quién revisa los textos FR (Quebec), ES y PT (candidato, campañas y reporte)?
- 3b-2b: ¿alcance final (Pool, Campaign, Analytics + PDF/CSV, Integrations)?
