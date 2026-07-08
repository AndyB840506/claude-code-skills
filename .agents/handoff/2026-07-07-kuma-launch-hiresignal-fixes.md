# Handoff: Kuma landing v3 launch (DO migration) + HireSignal reskin & fixes

**Date:** 2026-07-07
**Status:** Complete — todo deployado y verificado; quedan 2 pruebas del lado de Andy/Hugo

---

## What We Accomplished This Session

**Landing kumatalent.com (repo `C:\Users\andre\repos\kuma-talent-web`):**
- Diseño v3 de Hugo lanzado como **producción oficial** con foto de Andres Y de
  Hugo (encuadre `object-position` por retrato), transiciones smooth entre modos,
  y fixes móviles (forms apilados, nav CTA solapando el wordmark — cazado con
  captura real a 375px).
- **Migrado de Vercel a DO App Platform** con el token que dio Andy: app estática
  `kuma-talent-landing` (push a master = deploy), dominios apex+www con cert,
  records MX/TXT de email intactos (snapshot previo). Vercel queda dormant como
  rollback. Token de DO queda activo ~30 días como llave de emergencia.
- Runbook de la migración en `kuma-talent-web/docs/migracion-do.md` (ya ejecutado).

**HireSignal (repo `C:\Users\andre\repos\hiresignal`, commits `93aaf0e`→`6031c0a`):**
- **Reskin completo a la marca Kuma** (ink/brown/cream, oso como logo default,
  wordmark bicolor Hire+Signal) en chat, form, admin (6 páginas), PDF y emails.
- **Reportes durables**: PDF/transcript en Postgres `kv_store` (`report:<file>`) —
  el disco del contenedor DO se borra en cada deploy (causa raíz del "PDF not
  found" en History; los PDFs viejos solo existen como adjuntos de email).
- **QR codes** por invite en admin/invites.php (lib vendorizada, render local —
  los links son secretos de un solo uso). Verificado E2E: QR descargado →
  decodificado → invite vivo en servidor.
- **Bug de entrevista arreglado** (Hugo lo pisó en el retest móvil): UTF-8
  inválido del texto del CV rompía `json_encode` → request vacío → API 400.
  Fix: `JSON_INVALID_UTF8_SUBSTITUTE` en `_luccaPost`. Root-cause vía runtime
  logs de DO.
- **Settings que "no guardaban"**: el botón test-email era el primer submit del
  form y el Enter lo disparaba descartando ediciones — ahora es link; guard
  contra POST wipe por `post_max_size`. El "HireSignal ✓DB" salió con migración
  automática en config.php (removible cuando se confirme).
- **CV any-format** (regla de producto de Andy: cero errores por formato):
  sniffing por magic bytes (pdf/docx/odt/rtf), fallback strings-style para
  binarios, y extracción fallida arranca la entrevista sin contexto de CV.

**Retrospectiva aplicada:** doc nuevo `web-page-kit/docs/mobile-qa-headless.md`
(receta QA móvil headless en Windows), memoria nueva `reference_do_app_platform_api`,
actualizadas `reference_kuma_infra` + `reference_deploy_mechanisms` (¡Vercel prebuilt
para kumatalent quedó OBSOLETO!) + `project_hiresignal_testing` + security baseline
(QRs locales), y gotcha JSON/UTF-8 en CLAUDE.md § Debugging.

## Where We Paused

**Last action:** Session close (retrospectiva aplicada, audit limpio, este handoff).
**Next action:** Esperar los 2 retests de Hugo/Andy (abajo). Nada técnico pendiente.
**Blockers:** Ninguno del lado del agente. Del lado humano:
1. **Retest de entrevista móvil**: generar invite nuevo → QR → Hugo la corre
   completa (el invite anterior se quemó al fallar). Idealmente con el mismo CV
   que rompió. Valida: fix UTF-8, UX móvil del chat, y genera el primer PDF durable.
2. **Prueba de fuego de durabilidad**: tras esa entrevista, el próximo deploy NO
   debe romper la descarga del PDF en History (antes era exactamente lo que fallaba).
3. Confirmar que Settings ya guarda nombre/logo (el fix del Enter-trap).

## Files to Read First

- `C:\Users\andre\repos\hiresignal\config.php` — `_luccaPost` (fix UTF-8) y la
  migración one-off del app_name (líneas ~22-29; remover cuando se confirme limpio).
- `C:\Users\andre\repos\kuma-talent-web\docs\migracion-do.md` — runbook DO (ejecutado).
- Memoria `reference_do_app_platform_api` — cómo operar DO por API con el token.

## Notes / Gotchas

- **kumatalent.com ya NO se deploya con Vercel prebuilt** — push a master del repo
  = deploy automático en DO. No "arreglar" producción deployando a Vercel.
- El disco de contenedor de DO es efímero: cualquier feature nueva de HireSignal
  que escriba archivos debe ir a Postgres (patrón `kv_store` / `report:<file>`).
- QA móvil headless en Windows tiene trampas de DPI/min-width — receta completa en
  `web-page-kit/docs/mobile-qa-headless.md` (iframe harness + probe de overflow).
- Token DO (dop_v1, full access) activo hasta ~2026-08-06 — Andy lo revoca en
  panel → API cuando quiera.

## Questions to Answer

- ¿App móvil de HireSignal? Diseño conversado: admin app para reclutadores (falta
  auth por token en backend) + candidato vía QR → web (Universal/App Links cuando
  exista app). Sin arrancar — cuando Hugo avance, generar docs de la API actual.
- EP002 de CCC sigue esperando grabación (handoff anterior `2026-07-07-ccc-ep002-stage-a.md`).
