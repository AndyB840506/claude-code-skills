# Handoff: HireSignal sprint 3, español y portugués (lado candidato)
**Date:** 2026-10-21 (miércoles)
**Machine:** desktop (E:\)
**Status:** In progress. Pasos 1-3 construidos y verificados en local; el paso 4 (entrevistas reales) no completó. **Nada commiteado.**

---

## What We Accomplished This Session
- **Revisión de ai-job-search** (MadsLorentzen) → ideas para HireSignal y copia privada para Andrés (`repos/ai-job-search`, push bloqueado por falta del scope `workflow`: Andrés debe correr `gh auth refresh -h github.com -s workflow`).
- **HireSignal 1.5.26-1.5.27 en producción** (antes de la compactación): alerta de CV con texto dirigido a la IA (`247d9e7`, `bffa7c1`) y Dompdf 3.1.6 (`3380804`); health confirmó 1.5.27.
- **Pivote del negocio (Andrés):** solo vender HireSignal, cero candidatos, mercado global EN/FR/ES/PT. Memoria: `project_kuma_pivot_hiresignal_only`.
- **kumatalent.com rediseñado HireSignal-first**, rama `redesign-hiresignal` de kuma-talent-web @ `71421f3` (**pusheada**, master intacto). Build multi-idioma (`site/build.py` + `site/copy/en.json`), landing + página `/try`. Preview privado: https://claude.ai/artifact/LHLWGb517L4JYYANiM1HQd
- **CSV de Analytics de HGS:** 2 entrevistas, ambas pruebas internas de personal de HGS (REJECT 0/100). No sirven como resultados; la sección II de la página se queda cualitativa.
- **Sprint 3 (rama `feat/languages-es-pt` de hiresignal, SIN commitear, 24 entradas en `git status`):**
  - Idiomas de entrevista EN/FR/ES/PT + auto entre los 4 (`config.php`: `INTERVIEW_LANGUAGES`, registro ES usted / PT você, saludo de auto en el idioma de pantalla).
  - PT en motor, esquema, PDF (insignias que no se parten), admin (Edit job, Jobs, Ranking), Analytics, CSV y API v1. "Basic" = requisito no cumplido en los 4.
  - Pantallas del candidato en 4 idiomas: `i18n.php` nuevo, `index.php` reescrito con selector EN·FR·ES·PT, `chat.php`, `assets/js/app.js` (`tx()`), errores de `api/start.php` y `api/message.php`.
  - Tests nuevos `tests/languages.test.php` (63) y `tests/candidate-screens.test.php` (185). Suite **1507/0**. **28 mutaciones atrapadas**. Pantallas EN con texto visible idéntico a master. Navegador real 23/23.
  - `CHANGELOG.md` [1.6.0] y `.agents/build-state/sprint3-idiomas.md` (DoD) escritos. `APP_VERSION` **sigue en 1.5.27**: subirla al cerrar.

## Where We Paused
**Last action:** /session-close; retrospectiva aplicada (CSS text-transform en `CLAUDE.md`, memoria PHP local con PHPRC).
**Next action:** decidir con Andrés si se commitea y pushea la rama `feat/languages-es-pt` **como respaldo** (no despliega: solo master despliega). Después, repetir el paso 4.
**Blockers:**
- **Paso 4.** Las 3 entrevistas reales fallaron por entorno/instrumento:
  - ES: timeout de 90 s del modelo en el primer turno.
  - PT y auto: Haiku cortado a `max_tokens` 400 y una respuesta vacía.
  - La copia E2E no tiene `smalot/pdfparser`, así que no se leyó ningún CV.
  - Arreglos: `max_tokens` ≥ 1000, reintento si la respuesta sale vacía, instalar pdfparser en la copia (o usar `scratchpad/tools/pdfdeps`), reintento ante timeout.
  - Señal: en auto el entrevistador siguió en español con usted.
- **Deploy:** requiere decisión explícita de Andrés (push a master = producción).

## Files to Read First
- `repos/hiresignal/.agents/build-state/sprint3-idiomas.md`: DoD, decisiones y lo que queda fuera.
- `repos/hiresignal/i18n.php`: textos del candidato y precedencia de idioma.
- `repos/hiresignal/CHANGELOG.md` [1.6.0].
- Memorias `project_hiresignal_sprint3_idiomas`, `project_kuma_pivot_hiresignal_only`, `reference_php_local_verification`.

## Notes / Gotchas
- **Machine-bound:** todo lo del sprint 3 vive **solo en el working tree del escritorio** hasta que se commitee. También son machine-bound los scripts de verificación en el scratchpad de la sesión (`run_suite.sh`, `mutate_lang.py`, `screens_browser.py`, `lang_sim.py`, `make_e2e3.py`, `phpini/php.ini`). Se pierden si se limpia `%TEMP%`. Si se quieren conservar, moverlos a `hiresignal/tests/tools/` antes de que se pierdan.
- La suite local necesita `PHPRC` → php.ini con extensiones. Sin él, 37 fallos falsos.
- `index.php` y `chat.php` escapan con `ENT_COMPAT`: los apóstrofes quedan crudos, como antes, para que el guard de marca blanca siga encontrando "l'intelligence".
- La pastilla PT en Ranking aparece solo si se evaluó (decisión mía, para no llenar las filas viejas de "Not assessed").
- El FR y el PT de `i18n.php` los escribí yo y esperan revisión nativa: Quebec y Brasil.
- El servidor E2E (puerto 8099) está apagado.

## Questions to Answer
- ¿Commit + push de `feat/languages-es-pt` como respaldo ahora, antes de terminar el paso 4?
- 3b: los correos de campaña a candidatos solo existen en-CA/fr-CA. Una vacante ES/PT hoy enviaría el correo EN/FR. ¿Se bloquea el envío para esas vacantes mientras tanto?
- ¿Quién revisa el FR (Quebec) y el PT (Brasil)?
