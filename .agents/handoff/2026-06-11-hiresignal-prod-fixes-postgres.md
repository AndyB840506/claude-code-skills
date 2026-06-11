# Handoff — 2026-06-11 — HireSignal: fixes de producción + persistencia Postgres

## Estado: HireSignal 100% funcional en producción, Fase 1 de persistencia LIVE

Repo: `C:\Users\andre\repos\hiresignal` · Remote: `Lucca-Tech/hiresignal` (master)
Live: `https://hiresignal-pqsee.ondigitalocean.app` · Health: `/api/health.php` → `{"storage":"postgres"}`

## Qué se hizo (en orden)

1. **Fix página en blanco en chat** (`7f4e768`) — `chat.php` usaba `LOGO_MARK` sin incluir `config.php`. Bug venía del deploy del 9 de junio (commit `911428e`), no del refactor. Fatal en producción para todo candidato.
2. **Fix reportes nunca generados** (`1787f0a`) — La API rechazaba el schema del Intelligence Engine: HTTP 400 "The compiled grammar is too large". Schema adelgazado (5.4KB/4 $defs anidados → 2.9KB/1 $def plano) + fallback automático sin schema si la llamada estructurada falla. **Pipeline completo verificado en producción**: form → chat → engine (Opus 4.8) → PDF → ambos emails entregados (usuario confirmó recepción y abrió el PDF).
3. **3 JDs de prueba committeados al repo** (`c61685b`) — KT-004 (Bilingual CX Agent, agent), KT-005 (Systems Engineer, professional), KT-006 (CEO, executive), cada uno con 3 custom questions. Links listos para compartir con el socio.
4. **Fase 1 persistencia PostgreSQL** (`0369cfe`) — Usuario creó dev database en DO ($7/mes, PG, co-ubicada; `DATABASE_URL` auto-inyectada). Nuevo `db.php`: jobs/settings como documentos JSONB en `kv_store`, historial en `interview_log`, todo con `business_id` (negocio default id=1 "Kuma Talent"). Auto-seed desde JSON en primer boot; fallback transparente a archivos sin BD. Dockerfile + `pdo_pgsql`. Verificado live.

## Decisiones de negocio/arquitectura

- **PostgreSQL reemplaza la decisión anterior de MySQL** (dev DBs de DO son solo PG; JSONB superior; PDO hace el cambio gratis)
- **Leracom: cuenta/recurso muerto** — la key expuesta en git history es moot (solo verificar que la cuenta esté cerrada). **Se construirá versión propia de voz**: adaptador de canal (telefonía/STT/TTS) sobre el conversation core compartido
- **Workflow de jobs cambió**: ahora se administran desde el admin panel (durables en BD). `data/jobs.json` del repo es solo seed del primer arranque — editarlo ya NO actualiza producción
- Graphify evaluado y descartado por ahora (herramienta dev, escala incorrecta, quema tokens)

## Próximos pasos

1. **Socio prueba los links KT-004/005/006** — recopilar feedback de las entrevistas reales
2. **Fase 2 — conversation core**: estado de entrevista fuera de sesiones PHP → tablas relacionales `interviews`/`messages` (candidato puede retomar; admin ve entrevistas en curso; prerequisito de voz y Kuma Flow). PDFs a BD o Spaces en esta fase.
3. **Después**: adaptador de voz propio (stack por decidir: Twilio vs WebRTC) y modo lead-qualification para Kuma Flow

## Gotchas para la próxima sesión

- `git pull` SIEMPRE antes de trabajar hiresignal (lección del clone desactualizado)
- Filesystem de DO es efímero — solo la BD persiste; PDFs solo por email por ahora
- Schemas de structured outputs: planos, sin $defs anidados, probar contra la API real (memoria: structured-outputs-grammar-limit)
- PS 5.1: `git commit -m` con comillas dobles internas falla → temp file + `git commit -F`
- El historial de entrevistas arrancó vacío hoy (las pruebas previas estaban en el archivo que el deploy borró); desde ahora todo persiste
