# Handoff: HireSignal — competencia micro1, marca blanca y sesiones en Postgres
**Date:** 2026-07-24 (viernes)
**Machine:** portátil (C/D, sin E:)
**Status:** In progress — pausa deliberada; Andrés revisa pendientes con Hugo antes de seguir

---

## What We Accomplished This Session

Repo `hiresignal` (Lucca-Tech), **16 commits en master**, todo pusheado. Producción
verificada en `app.kumatalent.com` después del último deploy.

**Competencia vs. micro1 (HGS está comparando)**
- `docs/battlecard-micro1.md` — posicionamiento, 3 pilares, manejo de las 4 objeciones previsibles.
- `docs/roadmap-competitivo.md` — P0/P1/P2 por impacto/esfuerzo, con sección explícita de lo que NO haremos.
- `docs/pitch-hgs.html` — 11 slides 16:9. **No nombra al competidor en ninguna.** La slide 10 lista honestamente lo que no podemos hacer (voz, ATS, SOC 2).
- `docs/modelo-servicio-vs-licencia.html` — memo INTERNO, marcado "no compartir con el cliente".

**Cumplimiento Ontario**
- Disclosure de IA EN + FR en `index.php` (ESA / Working for Workers Four Act, obligatorio desde 2026-01-01 para empleadores de 25+).
- `docs/ai-disclosure-ontario.md` — párrafo listo para las ofertas de HGS, más las 5 obligaciones hermanas.

**Marca blanca — dos pasadas, y la segunda encontró lo grave**
La primera pasada arregló lo evidente. La segunda encontró 5 fugas más:
- `config.php` — el **saludo bilingüe** decía *"I'm [name] from HireSignal / je suis [name] de HireSignal"*. Es la primera frase que lee el candidato, y **solo aparece en la rama EN/FR — la de HGS**.
- `api/report.php` — correo de confirmación al candidato (encabezado, cuerpo, firma). El asunto ya usaba `APP_NAME`, así que llegaba con marca del cliente y firmado por nosotros.
- `api/report.php` — correo del reporte al equipo contratante.
- `api/message.php` — mensaje al alcanzar el tope de la entrevista.
- `admin/ranking.php` — título y topbar.
- `tests/whitelabel.test.php` = **23/23**. Usa el tokenizer de PHP (ignora comentarios, mira solo cadenas visibles), recorre todos los archivos de cara al candidato/cliente, y construye el prompt en **los 3 modos de idioma**.

**Costo por candidato — medido, no estimado**
- Contado contra `/v1/messages/count_tokens`: **$0.27 (8 turnos) a $0.395 (20, el tope)**.
- ⚠️ **Corrección de una afirmación previa mía:** dije que faltaba cachear la conversación y que era condición previa para cotizar. **Era falso** — `api/message.php` ya lo hacía; yo había leído solo `config.php`. Sin caché serían $0.70.
- **$3.50/candidato = 89% de margen HOY, sin tocar código.** micro1 Growth = $3.99/entrevista efectivo.
- **Opus 5 cuesta lo mismo que Opus 4.8** ($5/$25 por MTok). Migrar es gratis y es cambio de setting en la DB, no deploy.
- Modelo vivo en `tests/cost-model.py`.

**Sesiones en Postgres** (el hallazgo no planeado)
Una prueba real de HGS no apareció en el admin. No era un problema de visualización:
la entrevista **nunca se guardó**. Las sesiones PHP vivían en el disco del contenedor y
6 deploys en 56 minutos lo reemplazaron; la entrevista murió con `"Session expired"`, y
como `logInterview()` solo corre al generar el reporte, no quedó ni un registro parcial.
- `session-store.php` + `tests/session-store.test.php` = **16/16** (contra SQLite, sin necesidad de Postgres).
- TTL de 4 horas — el default de PHP son 24 minutos, más corto que una entrevista real.
- IDs de sesión ahora validados contra el store (session fixation).
- `api/health.php` reporta `{"storage":"postgres","sessions":"postgres"}`.

**Hardening para instancias por cliente**
- `data/jobs.json` estaba **versionado** y `dbBootstrap()` lo sembraba en el primer arranque: una instancia nueva nacía con **las vacantes reales de Kuma Talent** en la DB del prospecto. Sacado del repo y gitignoreado.
- `APP_NAME` / `SENDER_NAME` / `PUBLIC_BASE_URL` **no se leían del entorno**. Ahora sí, como **semillas** (lo que el cliente guarde en admin manda).
- Sin logo subido, el candidato veía el oso de Kuma. Ahora cae a monograma neutro.
- `docs/provisionar-instancia-cliente.md` — runbook interno.

**Checklist de onboarding al cliente** — ES / EN / FR-CA, 3 archivos autónomos.
Estructura verificada **por conteo**, no leyendo: las tres tienen 6 páginas, 5 secciones,
17 campos, 8 requeridos, 3 con antelación, 7 opcionales. Corregido un bug de fondo: las
hojas no pintaban su propio blanco y el texto salía sobre gris al embeberse.

---

## Where We Paused

**Last action:** retrospectiva aplicada (regla 9 en `verify`, Paso 4b en `deploy-preflight`), commit `ae4f7df` en el repo de skills, pulled en el clon global.

**Next action:** esperar la revisión de Andrés con Hugo. **No arrancar la migración del admin sin aprobación explícita** — está propuesta, no aprobada.

**Blockers:**
- P0.1 y P0.2 son de Andrés/Hugo, no técnicos.
- P0.4 necesita la API key de prueba, que **Andrés guarda en su propio gestor** (no está en el repo ni en env var).

---

## Files to Read First

- `docs/roadmap-competitivo.md` — tiene una sección "Estado al 2026-07-24" arriba con lo cerrado y lo desbloqueado.
- `docs/modelo-servicio-vs-licencia.html` — las cifras de precio; incluye una nota de corrección de la versión anterior.
- `tests/cost-model.py` — el modelo de costo vigente, corre solo.
- `docs/provisionar-instancia-cliente.md` — antes de montar cualquier instancia de cliente.

---

## Notes / Gotchas

- **Cada push a `master` redespliega TODAS las instancias que apunten a esa rama.** Ya no mata entrevistas (sesiones en DB), pero un cambio para un cliente sale para todos. Cliente que necesite congelarse: rama propia y quitarle `deploy_on_push`.
- **Atajo de diagnóstico:** si faltan entrevistas de hoy pero las viejas sí aparecen, el admin y la DB están bien — la entrevista murió antes de terminar. `logInterview()` solo escribe al generar el reporte.
- Si las vacantes siguen respondiendo tras un deploy, la DB está viva: el fallback JSON es efímero y el deploy lo borra.
- El SMTP es la fuga de marca blanca que queda. Vive en la cabecera del correo; ningún cambio de HTML la tapa. Cada instancia necesita el SMTP del cliente.
- La rama `feat/analytics-dashboard` **mergea limpio** (15 commits atrás pero todos sus archivos son nuevos), 41/41 tests, sin fugas de marca. Pero `analytics.php` **está huérfano**: no está enlazado desde ninguna página del admin.

---

## Questions to Answer

- **P0.1 — Andrés (5 min, BLOQUEA el battlecard):** confirmar en el browser que micro1 pivoteó a data labeling y que Zara ya no figura como producto. El hallazgo viene de fetches automatizados sobre un sitio SPA.
- **P0.2 — Andrés + Hugo:** decisión de modelo comercial. El memo recomienda C ($3.50/candidato) con datos medidos. Falta el volumen mensual real de HGS y saber si pidieron licencia o solo compararon precios.
- **P0.4 — desbloqueado, necesita la key:** correr una entrevista real contra KT-005 (FR-CA) y generar el PDF. Es la pieza de venta más fuerte que no existe. Aprovechar la misma corrida para verificar la marca blanca **por comportamiento** (poner un `APP_NAME` ficticio y confirmar que el modelo nunca dice "HireSignal" en voz alta) — hoy está verificada por el texto del prompt, no por lo que el modelo responde.
- **PROPUESTO Y NO APROBADO — migrar 5 páginas del admin a `_shell.php`.** Resuelve cuatro cosas de una: cierra **20 ocurrencias de marca hardcodeada en 7 páginas** (incluida `login.php`, lo primero que ve el cliente, y `settings.php:33-34`, cuyos defaults escriben `'HireSignal'` en la DB **del cliente**), desbloquea analytics, entrega la Etapa D que P0.2 opción B/C requiere, y elimina 383 líneas de CSS duplicado. Estimado medio día. Orden propuesto de menor a mayor riesgo: `login` → `index` → `history` → `invites` → `outreach` → `edit` → `settings` (este último de última, porque además hay que corregirle los defaults).
- Opcional, no urgente: chat en Sonnet 5 (−29% de costo), migrar a Opus 5 (gratis).
