# Handoff: HireSignal Sprint 5 — primer envío real, EN+FR y follow-up (1.5.14)
**Date:** 2026-09-18 (viernes)
**Machine:** laptop (D:\) — HireSignal en `C:\Users\andre\repos\hiresignal`, `master` = `origin/master` = `26a87e0`
**Status:** In progress — Sprint 5: todos los criterios construidos; falta la prueba real del follow-up (2026-09-25) y el cierre con la guía de usuario
---
## What We Accomplished This Session

Versiones en prod hoy (cada una verificada con `curl -sL https://app.kumatalent.com/api/health.php`):

- **1.5.9** — el primer envío real (KT-004 → 2 entradas de prueba) dio `Sent 0, Failed 2: Class "PHPMailer\PHPMailer\PHPMailer" not found`. `admin/candidate-campaign.php` no cargaba `vendor/autoload.php`. Reproducido en local antes de corregir. Test nuevo en `tests/outreach-mailer.test.php` que deriva de las libs qué funciones llegan a un mailer y exige el autoloader en cada página (5 páginas).
- **1.5.10** — `ccsBodyHtml()`: las URLs del cuerpo salen como `<a href>`.
- **1.5.11** — `ccLinkSpacing()` también en `ccRender()`: línea en blanco antes y después del enlace, aunque el texto guardado no la tenga. ✅ verificado por Andrés en la vista previa de prod.
- **Verificado en prod por Andrés con 1.5.9:** llegaron los 2 correos (Gmail a bandeja, Hotmail a spam); la baja dejó `andresbermudez50@hotmail.com` en la supresión compartida (criterio 7 ✅); tope compartido 2/15 ✅; en Gmail el enlace ya era clicable.
- **1.5.12** — el pie del correo a candidatos llevaba la razón de EMPLEADORES ("because your company is actively hiring"). Ahora: *"You're receiving this because you applied to or interviewed with Kuma Talent."* (aprobado) + borrador FR.
- **1.5.13** — vacantes EN+FR: **un solo correo, FR arriba y EN abajo** (decisión de Andrés, cumplimiento). Asunto `FR / EN`, "English version below.", separador `———`, pie bilingüe; no envía sin las dos plantillas; tarjeta "What the candidate receives" en la campaña. Sin envío real bilingüe todavía.
- **1.5.14** — **criterio 8**: sección "Follow-ups" (botón `Send follow-ups (N)`, lista de vencidos / en espera con fecha / excluidos con motivo). Uno por persona y vacante a los 7 días si el enlace no se usó; **renueva el mismo enlace 7 días** (decisión de Andrés); `Re:` + asunto real; idioma del primer correo. `extendInvite()` en `invites.php`. Probado en local contra Postgres.
- Suite **1081/0**; cada arreglo con mutación que falla su test.
- Decisiones de Andrés: **usuarios con permisos para el dashboard → Sprint 6** (hoy hay una sola sesión compartida `$_SESSION['admin_auth']`); Rui ×2 y Juliet se **archivan** en el Pool + se borran sus entrevistas en History (lo hace Andrés; no borrar del Pool: el import del Sheet los recrearía); guía de usuario paso a paso al cierre del Sprint 5.
- Retrospectiva: 4 memorias actualizadas + `reference_hiresignal_prod_url` nueva. Skills repo: `.gitignore` ignora `.trash/` y `synced/` (copias del harness de los plugins).

## Where We Paused
**Last action:** push de 1.5.14 (`26a87e0`), prod reporta 1.5.14; Postgres y servidor locales apagados.
**Next action:** preguntarle a Andrés si ya archivó Rui ×2 + Juliet y borró sus entrevistas → pedir captura del Pool y confirmar que no aparecen en Recipients de KT-004.
**Blockers:**
- Prueba real del follow-up: **viernes 2026-09-25**, 7 días después del envío a `berandre2+test1@gmail.com` (hora exacta en la sección Follow-ups de KT-004, "From … UTC"). Andrés pulsa Send follow-ups y revisa: mismo hilo con `Re:`, fecha nueva, enlace abre la entrevista. **No archivar esa entrada.**
- KT-004 sigue **Active** con postulantes reales en Recipients: se sugirió a Andrés pausarla. Sin confirmar.

## Files to Read First
- `hiresignal/.agents/build-state/integraciones-pool.md` — checkpoint vivo; líneas nuevas de hoy al final de la sección del Sprint 5 (hallazgos 1-3, plan aprobado, pasos 2 y 3).
- `hiresignal/CHANGELOG.md` — 1.5.9 a 1.5.14 con la evidencia de cada una.
- `hiresignal/api/candidate-send-lib.php` — `ccsLanguage`/`ccsRender` (bilingüe), `ccsFooterWhy`, `ccsFollowupsDue`/`ccsSendFollowups`.

## Notes / Gotchas
- Prod: `https://app.kumatalent.com` (health en `/api/health.php`). Tras cambiar de versión, esperar ~20 s antes de probar.
- Local (portátil): Postgres en `D:\tools\pg16\pgsql\bin\` (no `pg16\bin`); `pg_ctl start` cuelga la tool de PowerShell → lanzarlo en background y pararlo con `pg_ctl -D D:\tools\pgdata-it stop -m fast`. `vendor/` ya está instalado en el clon del portátil (composer.phar temporal con `-d extension=zip`). `config.php` ya incluye `invites.php`. El envío local siempre falla en la guarda CASL (sin dirección postal) — sirve para probar el flujo, pero tapa lo que hay detrás (así se escapó 1.5.9).
- Juicios propios no aprobados como texto (están en el CHANGELOG): formato del correo bilingüe; el follow-up es de un clic (el primer envío pide confirmación); el enlace se renueva aunque el envío del follow-up falle; los enlaces clicables solo en correos a candidatos (Outreach a empleadores arma el cuerpo igual y NO se tocó).
- La página de confirmación de baja sale en inglés también para el correo bilingüe.
- Todos los textos FR (plantillas y pies) siguen siendo borrador: revisión por hablante de Quebec antes de enviar a candidatos reales.

## Questions to Answer
- ¿Andrés pausó KT-004? ¿Archivó Rui ×2 + Juliet?
- ¿Arreglar también los enlaces del correo de Outreach a empleadores (una línea)?
- Microsoft manda el correo a spam: sin investigar (revisar SPF/DKIM/DMARC del dominio o las cabeceras del correo en Hotmail).
- Pendientes que vienen de antes: **jueves 2026-09-24** Send follow-ups de Outreach (TEST A debe recibir `Re:`, C suprimido); revisión del borrador de reclutamiento con Hugo; francés por hablante de Quebec.
- Cierre del Sprint 5 tras la prueba del 25: guía de usuario paso a paso (formato por decidir; los documentos para compartir van a Artifact/Drive) y abrir el Sprint 6 con los usuarios con permisos.
