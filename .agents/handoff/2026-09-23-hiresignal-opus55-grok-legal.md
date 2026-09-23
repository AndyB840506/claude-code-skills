# Handoff: HireSignal — Opus 5.5, Grok medido, informe razón-primero, revisión legal
**Date:** 2026-09-23 (miércoles)
**Machine:** laptop (D:\) — DESKTOP-M86UNRS, sin E:
**Status:** Complete — 1.5.20 → 1.5.25 en producción (health 14:55 COT); fallback a Grok planeado, no construido
---
## What We Accomplished This Session
- **1.5.20** chat e informe en `claude-opus-5-5`, thinking adaptive, effort `low` (medido 3 brazos vs Opus 5: informe 12/12 vs 9/12, 18 s vs 37 s, $0.059 vs $0.093; entrevista mismo costo, +2 s/turno aceptado por Andrés). Topes: entrevista 4000, JD 4000, campaña 8000. Health expone `llm` (modelo efectivo). Rollback por env.
- **1.5.21** Grok/xAI medible por env (`LLM_{CHAT,REPORT}_{PROVIDER,URL,KEY}`, `reasoning_effort`, esquema JSON para `xai`); prod sin cambio. Grok 4.7 low: ~½ costo entrevista, ~⅓ informe, 12/12, pero 7.7 s/turno y 40 s/informe; `high` inviable.
- **1.5.22** informe "la razón primero, la cita como prueba" (decisión de Andrés tras revisión a ciegas: https://claude.ai/artifact/TcwcFMowqT5b9LwfqtEXJk). Contradicciones siguen citando ambos lados.
- **1.5.23** reglas en la base común: "no reconciliar por el candidato" (Opus `solo` ~9/13 → 8/8) y "lo disputado no suma" (Grok dejó de premiar lo contradicho). 0 FP en `clean_tricky`.
- **1.5.24** menú lateral del admin entero en capturas de página completa (era artefacto de captura; `body.has-sidebar::before`).
- **1.5.25** correo de Ranking: candidatos marcados en sección propia con motivo; se envía aunque todos estén marcados. Verificado con correo real vía SMTP sink local.
- xAI: ZDR **activo** en "Andrés's team" (captura). `LLM_FALLBACK_KEY` agregada en DO por Andrés (sin efecto aún; no verificable hasta que el fallback la lea).
- Revisión legal: Anthropic Usage Policy = hiring tools "High-Risk" (humano revisa + aviso); xAI AUP prohíbe "high-stakes automated decisions" de empleo; Ley 25 Quebec 12.1. Doc de 26 preguntas para abogado canadiense (inglés), **compartido con Hugo por Andrés**: https://claude.ai/code/artifact/939783ca-d22d-42f7-a8c2-85b32abee766
- Seguridad: dos keys de Anthropic quedaron como NOMBRE de variable y se expusieron al listar; Andrés las revocó y creó keys nuevas (workspace-scoped). Regla nueva en CLAUDE.md § Debugging.

## Where We Paused
**Last action:** session-close (retrospectiva aplicada: 2 reglas en CLAUDE.md + 2 memorias).
**Next action:** jueves 24 — Outreach "Send follow-ups" (TEST A debe recibir `Re:`, C suprimido).
**Blockers:** respuesta legal de Hugo/abogado antes de encender el fallback en prod.

## Pendientes, en orden
1. **Jue 24-sep:** Outreach follow-ups (TEST A / C).
2. **Vie 25-sep, ESCRITORIO, antes de 20:58 UTC (15:58 COT):** follow-up de candidatos KT-004 — activar campaña, pulsar SOLO "Send follow-ups", re-pausar. **Nunca "Send to 3"** (postulantes reales).
3. **Vie 25-sep:** DKIM — Send test + correo desde webmail; si sigue sin `DKIM-Signature`, soporte GoDaddy.
4. **Fallback Anthropic→Grok** (ítem aparte, no Sprint 5), apagado en prod hasta lo legal: chequeo con la lectura de JD en `start.php`, proveedor fijo por entrevista, circuit breaker compartido, cambio solo ante 5xx/529/429/timeout (nunca 400 ni rechazo), proveedor registrado en el informe, **nombre del entrevistador persistente al cambiar**, health "fallback configured: sí/no" (verifica `LLM_FALLBACK_KEY`).
5. Completar en el doc legal: región de la base en DO y proveedor de correo ("to be confirmed by us"); adjuntar términos comerciales/DPA de Anthropic (pregunta 18).
6. Opcional: borrar Gamma doc 5a9hcsu6htqbddo; actualizar sección Invites del doc wsfvzlss36nwdk6; verificar a mano en prod que Revoke conserva filtros de Invites.

## Files to Read First
- `repos/hiresignal/CHANGELOG.md` — 1.5.20–1.5.25 con tablas de medición y hallazgos.
- memoria `project_hiresignal_outreach.md` — estado y plan del fallback.
- memoria `reference_hiresignal_browser_check.md` — kit de verificación local (CA bundle, SMTP sink, full-page, sandbox de proveedor).

## Notes / Gotchas
- PHP del portátil sin CA bundle: `-d curl.cainfo=".../Git/mingw64/etc/ssl/certs/ca-bundle.crt"` por corrida.
- Keys: `ANTHROPIC_API_KEY` y `XAI_API_KEY` son variables de USUARIO en el portátil; la sesión no las hereda → leerlas del registro por comando. En el escritorio NO verificadas.
- Opus devuelve el thinking vacío por defecto; `LLM_REPORT_THINKING_DISPLAY=summarized` para diagnóstico.
- Sandbox apagado al cierre (Postgres 5433, 8765/8766, SMTP 2525, Edge 9333). Relanzar: `grok-sandbox.sh` estaba en el scratchpad de la sesión (temporal) — reconstruir desde la memoria si hace falta.
- Hallazgos abiertos: nombre del candidato no llega al chat sin CV (prompt dice "Hi [candidate name]"); `OUTREACH_FROM_NAME` default "Kuma Talent"; DB prod "Dev Database" $7 sin backups verificados; xAI Chat Completions marcado "Legacy".

## Questions to Answer
- ¿El auto-flag "requirements not met" necesita confirmación humana antes de pesar? (pregunta 2 del doc legal)
- ¿Quién da el aviso de la Ley 25 12.1 a candidatos de Quebec: HireSignal o el empleador?
