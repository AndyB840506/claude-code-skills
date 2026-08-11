# Handoff: AI Visibility Audit — rediseño visual + muestra pública + plan de LinkedIn
**Date:** 2026-08-11
**Machine:** laptop (D:\)
**Status:** Complete — todo verificado, nada bloqueado; pendiente decidir si se commitea/pushea

---

## What We Accomplished This Session

**kit-ai-lead-generator-app (laptop setup + email drafts):**
- Configuró PHP 8.4 en el portátil (php.ini con extensiones curl/mbstring/openssl/pdo_sqlite/sqlite3), resuelto el bind IPv6 (`localhost` no funciona en este portátil, usar `127.0.0.1` explícito).
- `ANTHROPIC_API_KEY` seteada solo en la sesión de terminal del usuario (nunca pegada a herramientas de Claude) — patrón confirmado: `$env:ANTHROPIC_API_KEY = "..."` manual, sin `Read-Host`.
- Extendido `api/generate.php` + `config.php` para generar un draft de email personalizado (`email_asunto`/`email_cuerpo`) por cada lead, con las 8 líneas de servicio de The Freelancer (incluye AI Visibility Audit, agregado recientemente). 7 leads reales generados para The Freelancer, incluido Rappi.

**the-freelancer — motor de AI Visibility Audit (refactor completo):**
- Rehecho el motor de una sola llamada (que le fallaba a Sonnet 5 devolviendo texto libre en vez de HTML) a un **pipeline de 4 etapas**: investigación libre con herramientas (Opus 5) → estructuración con JSON Schema (sin herramientas, son mutuamente excluyentes en la API) → score determinista en código (pesos fijos + gate duro: robots.txt bloqueando crawlers de IA principales topa el score en 30) → render HTML puro en código.
- Archivos nuevos: `freelancer/ai-visibility-precheck.js`, `ai-visibility-schema.js`, `ai-visibility-scoring.js`, `ai-visibility-report-template.js`, `freelancer/prompts/ai_visibility_audit_research.md`. Wireado en `freelancer/deliverable.js`.
- Verificado de punta a punta con caso real pagado (Rappi): score 30/100 (gate activado, GPTBot bloqueado en robots.txt), 8 categorías, 3 honestamente "No verificado" en vez de forzar un número.
- **Rediseño visual completo** tras feedback del usuario ("demasiado denso" → luego "demasiado IA"): reemplazó fuentes de sistema + tarjetas planas por la tipografía real de marca (Cabinet Grotesk/Supreme/Martian Mono vía Fontshare) y un gauge circular SVG por categoría — reusando el componente y los tokens que ya existían sin usar en `one-pager/samples/seo-audit-tesla.html`. Ver `docs/estandar-de-entregables.md`... (no existe ese doc en este repo — nota aparte, no crear referencia falsa).
- **Muestra pública** para marketing: `renderAiVisibilityHtml()` ahora acepta `sample: true` → agrega watermark diagonal "MUESTRA", banner de honestidad (no es cliente real, datos públicos), y difumina (`filter: blur`) los puntajes por categoría, el "próximo paso" y la tabla de acciones prioritarias — el diagnóstico (observado + por qué importa) queda visible como gancho. Generada en `one-pager/samples/ai-visibility-audit-rappi.html`.
- Archivos de prueba (`test-ai-visibility*.js/.json/.html`) limpiados al terminar — no quedan en el repo.

**Integración con marketing:**
- Localizado el plan existente: `marketing/social-media-plan.md` (IG+LinkedIn general) y `marketing/linkedin-plan.md` (específico de AI Visibility Audit, ya tenía 4 posts + 7 imágenes PNG en `marketing/linkedin-assets/output/`, todo confirmado presente y sincronizado con `origin/master`, 0 commits de diferencia).
- Agregado **Post 5** a `linkedin-plan.md`: caption listo para pegar sobre la auditoría real de Rappi (ángulo: marca fuerte pero score bajo por robots.txt bloqueando GPTBot), pensado para subir como documento/PDF nativo de LinkedIn (el usuario ya guardó el HTML como PDF manualmente desde el navegador).
- Checklist de lanzamiento actualizado con el ítem del Post 5.

## Where We Paused

**Last action:** Cerrado con `/session-close` — retrospectiva aplicada (3 memorias nuevas), auditoría del kit de skills limpia (0 issues), escribiendo este handoff.
**Next action:** Publicar el Post 5 en LinkedIn (texto + PDF ya listos, ver `marketing/linkedin-plan.md` sección "Post 5"). Después, decidir si commitear/pushear los cambios de esta sesión en ambos repos (ver Blockers).
**Blockers:**
- **Nada commiteado todavía.** `the-freelancer` tiene 3 archivos modificados + 6 nuevos sin stagear (motor completo + plan de LinkedIn). `kit-ai-lead-generator-app` tiene `api/generate.php`/`config.php` modificados + `db/leads.sqlite`/`leads/the-freelancer/` sin trackear (datos reales de leads — evaluar si deben ir a git o quedarse locales/gitignored). No se commiteó porque el usuario no lo pidió explícitamente esta sesión — preguntar al retomar.
- El PDF del reporte de Rappi lo guardó el usuario manualmente desde el navegador (no vive en el repo) — confirmar dónde quedó antes de publicar el Post 5.

## Files to Read First
- `the-freelancer/marketing/linkedin-plan.md` — Post 5 (sección 4), listo para publicar hoy.
- `the-freelancer/freelancer/ai-visibility-report-template.js` — motor de render, incluye el modo `sample` (watermark + difuminado) y el sistema de gauges. Cualquier cambio visual futuro al AI Visibility Audit pasa por acá.
- `the-freelancer/one-pager/samples/ai-visibility-audit-rappi.html` — la muestra pública ya generada, para revisar antes de compartir el link.
- `the-freelancer/one-pager/samples/seo-audit-tesla.html` — referencia del sistema de marca real (fuentes, gauge, paleta) — consultar ANTES de diseñar cualquier deliverable nuevo de The Freelancer, ver memoria `feedback_check_sibling_design_before_building`.

## Notes / Gotchas
- `output_config.format` (salida JSON estructurada) es mutuamente excluyente con `web_search`/`web_fetch` en la misma llamada de la API de Anthropic — de ahí las 4 etapas. Ver memoria `reference_anthropic_api_gotchas`.
- `client.messages.create()` es rechazado por el SDK una vez `max_tokens` es alto (~32000) — usar `.stream().finalMessage()`.
- Este portátil no resuelve `localhost` por IPv6 — `php -S` debe bindear a `127.0.0.1` explícito.
- El JSON estructurado de cada corrida se puede cachear (`SKIP_STAGE1`/`SKIP_STAGE2`) para iterar el render sin re-pagar la API — patrón guardado en memoria (`feedback_cache_llm_pipeline_stages`), pero el archivo de cache mismo se borró en la limpieza final (no persiste entre sesiones a propósito).

## Questions to Answer
- ¿Se commitea y pushea el trabajo de esta sesión en `the-freelancer` y `kit-ai-lead-generator-app`, o se deja local por ahora?
- ¿`db/leads.sqlite` y `leads/the-freelancer/` (datos reales de leads generados) deberían ir a git o quedar gitignored/solo locales?
- ¿Se agrega también una versión del sample de Rappi al plan de Instagram (`social-media-plan.md`), o el AI Visibility Audit se queda solo en LinkedIn por ahora?
