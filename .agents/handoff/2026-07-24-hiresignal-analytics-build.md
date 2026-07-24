# Handoff — HireSignal: análisis costos/whitelabel + build de analytics

**Fecha:** 2026-07-24
**Sesión:** revisión estratégica de HireSignal + arranque del módulo de analítica.

## Qué se hizo esta sesión

1. **PDF para Hugo (entregado):** `hiresignal/docs/HireSignal-costos-whitelabel-vs-RecruitX-2026-07-24.pdf` (7 pp) — refresco de costos reconciliado (ambos flujos en Opus 4.8 `config.php:55,60` → ~$0.40/candidato, no los ~$0.30 que subestimaba la propuesta de junio), 3 modelos whitelabel con precio, y comparación vs RecruitX (TalentNow, ATS completo a $35/usuario/mes, verificado en SoftwareSuggest). También publicado como Artifact. **Nota:** ese PDF está untracked en hiresignal (no commiteado), trae estructura de costos interna — ok para Hugo (socio), no para cliente final.

2. **Dirección de producto fijada (y revertida a media sesión):** HireSignal **NO** se vuelve ATS ni se construye un ATS separado — el usuario lo descartó explícito. Se queda como capa de screening con IA; crece por **integraciones** (APIs con token, webhooks, Slack, Zapier, push a ATS) y **analítica profunda**. Ver memoria `project_kuma_ats_complementary.md`.

3. **Build de analytics — Etapa A + B core (CONSTRUIDO Y VERIFICADO):** en la rama **`feat/analytics-dashboard`** de hiresignal (commit `772c9e1`, **pusheado**, NO en master porque hace deploy_on_push).
   - `admin/analytics-lib.php` — agregaciones puras. **41/41 unit tests** (`tests/analytics-lib.test.php`).
   - `admin/analytics.php` — dashboard dark-first, filtros (fecha/job/verdict/idioma), 6 vistas, charts SVG/CSS hechos a mano. KPIs cross-checked a mano (5, 71%, 63.4, 40%, 40%). Screenshot premium confirmado.
   - `admin/analytics-export.php` — CSV verificado.
   - `admin/_shell.php` + `admin/admin.css` — design system dark-first compartido, sin Google Fonts CDN, marca por APP_NAME/logo.
   - Instalé **PHP 8.3 vía winget** en esta máquina para poder verificar (ver `reference_php_local_verification.md`).

## Plan completo
`~/.claude/plans/ayudame-a-revisar-hiresignal-floofy-lobster.md` (aprobado). Etapas A→D + phasing.

## Next Steps (pendientes, en orden)

1. **DECISIÓN DEL USUARIO PENDIENTE:** al cerrar la sesión quedó sin responder si prefiere **(a)** que siga construyendo (PDF de analytics + Etapa C + D) o **(b)** levantar primero el dashboard en su Laragon y verlo en vivo antes de continuar. Preguntar al retomar.
2. **`admin/analytics-pdf.php`** (reporte PDF descargable) — falta. Reusa Dompdf de `api/report.php`. El botón "PDF report" en analytics.php ya apunta ahí (hoy 404).
3. **Etapa C — reporte por entrevista** (`api/report.php` + `api/intelligence-engine.php`):
   - **2 pasadas Opus**: mantener la estructurada (scores deterministas) + agregar una **pasada narrativa SIN schema** (evita el límite de grammar, subir el cap de 4096 tokens) para análisis en prosa profundo. El usuario insistió: "usamos Opus 4.8 y lo tenemos sacando cosas básicas".
   - **Exponer datos ya computados** que el PDF descarta: texto `analysis` por dimensión, contradicciones critical/warning, `follow_up_topics`, `bluff_probability`, resumen ejecutivo.
   - **Rediseño PDF premium LIGHT** (el usuario confirmó: "el pdf no puede ser dark"). NO dark. Limpiar strings "HireSignal" hardcodeados en emails (~`api/report.php` 656-707).
4. **Etapa D — reskin del resto del admin:** adoptar `_shell.php` + `admin.css` en index/history/ranking/settings/outreach/invites; quitar "HireSignal" hardcodeado (ranking.php:88 email).
5. **Deploy:** solo tras OK explícito + `deploy-preflight`. Mergear a master dispara deploy_on_push a app.kumatalent.com (LIVE).

## Verificación pendiente (límite honesto)
El PDF (Dompdf) y las 2 pasadas de LLM del reporte **no se pueden correr en esta máquina** (sin `vendor/` ni API key). Verificar en Laragon del usuario o deploy de staging. La lógica pura y el render de páginas sí se verificaron local (ver `reference_php_local_verification.md`).

## Estado de datos de prueba
`data/interviews.json` + `data/invites.json` tienen fixtures de muestra (gitignored, NO commiteados) para correr los runners locales. Borrarlos si se conecta la DB real local.
