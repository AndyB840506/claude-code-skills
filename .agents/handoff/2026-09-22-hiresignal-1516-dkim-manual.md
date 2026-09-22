# Handoff: HireSignal 1.5.15–1.5.16, DKIM de kumatalent.com y manual white-label
**Date:** 2026-09-22 (martes)
**Machine:** laptop (C y D, sin E:) — HireSignal en `C:\Users\andre\repos\hiresignal`
**Status:** In progress — Sprint 5 con todo construido; esperan fechas (jue 24, vie 25) y DKIM de GoDaddy
---
## What We Accomplished This Session

- **Handoff del 09-18 verificado** contra el estado real (repo en `26a87e0`, prod en 1.5.14, fechas).
- **Manual de usuario white-label del admin** (inglés, 14 secciones, sin HireSignal/Kuma/KT):
  Artifact https://claude.ai/artifact/FWNN2ix7Usmqk8mAB6o4dJ (versión 5, compartido "Anyone with the
  link") + `D:\Downloads\Screening-Dashboard-Handbook.pdf` y `.html` (solo en el portátil).
  Escrito desde el código; revisado contra 6 pantallas reales (menú, plantillas de Outreach, Analytics,
  Edit job, Candidate campaign, Pool) → 6 frases corregidas. Lleva sello "Draft — pending screen review".
  El PDF se genera con Edge headless (imprimir desde el visor de claude.ai rompe la paginación).
- **1.5.15 en prod** (`844ffec`): enlaces clicables en Outreach a empleadores (`outreachLinkify()`
  compartido), `admin/edit.php` ya no pierde preguntas propias ni modo al dar error, página de baja FR+EN
  para el correo bilingüe (`l=fr-en`). ✅ Enlace verificado en correo real (Send test 14:29 UTC,
  "Mostrar original"); ✅ página de baja verificada en prod con token falso.
- **1.5.16 en prod** (`f06bf26`): la vista previa del editor de plantillas de Outreach muestra el HTML
  real (era texto plano y confundió a Andrés). Test de escape con `<script>`. Suite **1109/0**.
- **KT-004:** la vacante sigue ACTIVA a propósito (pruebas); la campaña está "Draft – inactive".
  Rui ×2 + Juliet ARCHIVED en el Pool (verificado en captura).
- **DKIM de kumatalent.com:** faltaba. Agregados en DigitalOcean DNS los CNAME
  `secureserver1._domainkey` → `s1.dkim.kumatalent_com.a07.onsecureserver.net.` y `secureserver2` → `s2…`
  (TTL 3600). Verificados en 4 resolvers públicos + DoH (clave `v=DKIM1` real); GoDaddy dice
  "configuración correcta". **Send test de 15:36 UTC aún SIN `DKIM-Signature`.**
- **Roadmap:** "Track paralelo — Campañas en redes sociales para promover HireSignal" en el checkpoint
  (commit `17a5f57`, pusheado con OK de Andrés; redeploy de la misma 1.5.16).
- Retrospectiva: `docs/estandar-de-entregables.md` §9 (documentos para compartir / PDF), 2 reglas en
  `CLAUDE.md` (`python -c` con barras; test de escape debe afirmar la versión escapada), memoria nueva
  `feedback_verify_screen_before_asking_user`.

## Where We Paused
**Last action:** retrospectiva aplicada y commiteada en el kit (`01d3b64`); roadmap commiteado en local.
**Next action:** preguntarle a Andrés si ya pasó el jueves/viernes y qué salió de las pruebas de abajo.
**Blockers:**
- **Jueves 24-sep:** Send follow-ups de Outreach (TEST A debe recibir `Re:`, C suprimido).
- **Viernes 25-sep:** (1) follow-up a candidatos en KT-004 — vence **20:58 UTC (15:58 Colombia)**;
  hay que **activar** la campaña, pulsar SOLO *Send follow-ups* y volver a pausarla: activarla habilita
  "Send to 3" a postulantes REALES (Akshay, Alexander, Santiago). Revisar en `berandre2+test1@gmail.com`:
  mismo hilo con `Re:`, fecha nueva, enlace abre. (2) **DKIM** (pasadas 48 h): Send test + un correo
  desde el webmail de `hello@` → si sigue sin `DKIM-Signature`, soporte de GoDaddy. Si el webmail firma
  y HireSignal no, el fallback es que HireSignal firme con PHPMailer DKIM y selector propio
  (`hs1._domainkey`) — sin construir, necesita OK de Andrés.
- **El viernes corre en el ESCRITORIO** (decisión de Andrés): antes de empezar, correr `install.ps1`
  de `claude-continuity` para restaurar la memoria de hoy (el sync es de una sola vía). Los 4 repos
  quedaron limpios y pusheados al cierre (kit `ee0de86`+, skills, hiresignal `17a5f57`, continuity).

## Files to Read First
- `hiresignal/.agents/build-state/integraciones-pool.md` — checkpoint vivo; 1.5.15 y 1.5.16 al final de
  la sección del Sprint 5; el track de redes después del Sprint 9.
- `hiresignal/CHANGELOG.md` — 1.5.15 y 1.5.16 con su evidencia.
- Memoria `project_hiresignal_outreach.md` — DNS, DKIM, KT-004, fechas, inconsistencias.

## Notes / Gotchas
- **Fuente del manual:** el scratchpad de esta sesión es temporal. Para editarlo: leer el Artifact
  (`Artifact read` con la URL) o `D:\Downloads\Screening-Dashboard-Handbook.html` (esa copia trae el
  envoltorio `<!doctype><html><head>` para imprimir; el Artifact publica sin él). Republicar con `url`.
- Desde el portátil, consultar directo a `ns1-3.digitalocean.com` devolvió el valor DKIM viejo un buen
  rato (TTL fijo, también por TCP) mientras los resolvers públicos veían el nuevo: nodo atrasado de DO,
  hipótesis no confirmada. Lo que ven los receptores se mide con 8.8.8.8/1.1.1.1/9.9.9.9 + DoH.
- **No aplicar el `_dmarc p=reject`** que propone la pantalla de GoDaddy: los reportes de HireSignal
  salen por Gmail (`SMTP_*`) y podrían rebotar.
- Producto de correo: "Correo Profesional Pro Light" de GoDaddy; su ayuda lo titula "powered by Titan";
  MX = `secureserver.net`.
- La vista previa de la **campaña a candidatos** sigue en texto plano y sin pie (no tocada).
- `andy@behind-thequeue.com` está en la misma cuenta de GoDaddy: probable mismo problema de DKIM.

## Questions to Answer
- **Inconsistencias del checkpoint (no resueltas):** el plan del 09-18 dice "usuarios → Sprint 6" pero
  la secuencia dice Sprint 6 = localización y 7 = usuarios; la tabla "Dónde arrancar" sigue en
  "Sprint 4 CERRADO ← aquí estamos"; "Sprint 8 — manual (Canva)" vs el manual hecho hoy como Artifact.
- Manual: ¿las 7 pantallas que faltan (lista de Jobs, Invites, Ranking, History, Outreach,
  Integrations, Settings) o se da por bueno y se quita el sello?
- Campañas en redes: las 5 preguntas del track (qué se promueve, canales, cuenta/marca, producción,
  métrica) → sesión de estrategia.
- ¿Trusted sources de la base de datos en DO (restringir a la app)? Sin revisar.
- Pendientes de antes: borrador de reclutamiento con Hugo; francés por hablante de Quebec; cierre del
  Sprint 5 tras el 25.
