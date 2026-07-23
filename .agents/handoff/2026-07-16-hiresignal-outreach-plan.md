# Handoff: HireSignal Ontario Outreach — plan aprobado, build diferido
**Date:** 2026-07-16 (jueves)
**Status:** Plan cerrado y aprobado — implementación pendiente en sesión futura (diferida por rush hour / tokens)
**SUPERSEDIDO:** el plan se construyó el 2026-07-17. Estado actual en `2026-07-23-hiresignal-outreach-pendiente-fulfillment.md`.

---

## What We Accomplished This Session

**Sesión corta, solo planificación (decisión explícita del usuario por rush hour):**

- **Plan aprobado:** pipeline CASL-compliant de cold email para conseguir prospectos de HireSignal en Ontario (expandible a Canadá). Plan file completo en `~/.claude/plans/morning-i-wnated-to-sunny-flame.md`.
- **Decisiones tomadas (vía AskUserQuestion):** fuentes de prospectos = Job Bank Canada + LinkedIn HR + Google Maps (las 3); envío = PHPMailer/SMTP self-built dentro del stack de hiresignal (no SaaS); target inicial = SMBs de Ontario contratando directo.
- **Marco legal:** CASL es la restricción de diseño — consentimiento implícito por publicación conspicua, logging de base de consentimiento por contacto, unsubscribe, footer con dirección física. Sin blasts masivos; piloto de 10–20 Tier 1 con sign-off de Hugo.
- **Reuso descubierto:** `jobbank_canada_scraper.py` (repo kuma-talent-sourcing, parqueado 2026-06-29 como "señal equivocada" para Argentina) es EXACTAMENTE la señal correcta aquí; hiresignal ya tiene PHPMailer funcionando (`admin/test-email.php`). v1 = $0 en tooling nuevo.
- **Retrospective aplicado:** regla plan-mode staleness check (`git ls-remote`) agregada a CLAUDE.md; memoria nueva `feedback_rush_hour_scope_now_build_later`.
- **Memoria de proyecto guardada:** `project_hiresignal_outreach.md` (indexada en MEMORY.md).

## Where We Paused

**Last action:** `/session-close` (retrospective aplicado, audit de skills limpio — 10 skills, sin corrupción).
**Next action:** Sesión de build del outreach pipeline — empezar por Phase 0 del plan.
**Blockers:** Ninguno técnico. El build espera ventana de uso más liviana.

## Next Steps (build session)

1. **Phase 0 del plan:** sync de los 2 clones de skills + `git -C C:\Users\andre\repos\hiresignal pull` (⚠️ estaba STALE el 2026-07-16: local `7ddb895` ≠ remote `0ef4e6d`) + clonar `Lucca-Tech/kuma-talent-sourcing` (NO existe en el desktop).
2. Leer `hiresignal/admin/test-email.php`, `config.php` y el handoff 2026-06-09 de Gmail SMTP para confirmar transporte.
3. Seguir el plan: scraper Job Bank (Ontario) → tablas PostgreSQL + sender throttled + unsubscribe → templates EN → verificación (mail-tester ≥9, unsubscribe E2E) → piloto 10–20 con Hugo.
4. **NEEDS USER INPUT (Andres, antes/durante el build):** creds SMTP (pegadas, no retipeadas), decisión de identidad de envío (recomendado: subdominio, no kumatalent.com principal), dirección física de Kuma para el footer CASL (pedir a Hugo), cap diario aprobado, `APIFY_TOKEN` (solo para fases LinkedIn/Maps, no v1).

## Files to Read First

- `~/.claude/plans/morning-i-wnated-to-sunny-flame.md` — el plan completo (contexto, 4 fases, open items, orden de build).
- Memoria: `project_hiresignal_outreach.md`, `feedback_rush_hour_scope_now_build_later.md`.
- Handoff previo relacionado: `.agents/handoff/2026-06-29-kuma-talent-sourcing.md` (origen del scraper de Job Bank).

## Notes / Gotchas

- Regla al retomar: preguntar qué next steps ya se completaron antes de proponer acciones.
- El plan recomienda arrancar SOLO con Job Bank (señal más fuerte, $0 Apify) y dejar LinkedIn/Maps para después del piloto.
- Nada se construyó ni se envió: cero código nuevo, cero emails, cero pulls a hiresignal.
