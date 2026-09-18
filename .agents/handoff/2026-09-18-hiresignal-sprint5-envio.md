# Handoff: HireSignal Sprint 5 — 1.5.8 en prod, envío a candidatos sin prueba real
**Date:** 2026-09-18 (viernes)
**Machine:** laptop (D:\) — HireSignal en `C:\Users\andre\repos\hiresignal`
**Status:** In progress — Sprint 5 abierto; criterios 1-4 verificados en prod, 5/6/7/9 construidos y desplegados sin envío real, 8 sin construir
---
## What We Accomplished This Session

Versiones empujadas a prod hoy (todas verificadas con `GET /api/health.php`):

- **1.5.3** "Draft with AI" (criterio 4). El primer push NO desplegó (health quedó en 1.5.2 >15 min); un commit vacío `435ed7f` lo desplegó. Causa no determinada.
- **1.5.4** enlace de invitación en su propia línea (pedido de Andrés) + chequeo de paga exacta.
- **1.5.5** panel "Rejected AI draft: what the AI wrote" (texto crudo del modelo al rechazar).
- **1.5.6** el modelo ya no escribe ubicación/modalidad/paga: deja `[JOB DETAILS]` y el código las inserta; `ccAiRepair` devuelve `\u2013`/`\ndash`/llaves escapadas a su carácter. Motivo: 3 llamadas reales salieron con caracteres escritos como código.
- **Criterio 4 ✅ en prod** (captura de Andrés sobre 1.5.6, borrador limpio).
- **1.5.7** decisión de Andrés: el correo a candidatos **no nombra a la empresa** (se comparte tras la preselección; en el panel de un cliente el remitente ya lo dice). Se quitó "Kuma Talent" fijo del borrador y del prompt → `{sender_name}` / `OUTREACH_FROM_NAME`. Runbook: `OUTREACH_FROM_NAME` faltaba. Andrés renombró KT-004 sin "HGS".
- **1.5.8** criterios 5, 6, 7 y 9: sección **Recipients** en la campaña de cada vacante (`api/candidate-send-lib.php`, `admin/candidate-campaign.php`). Filtro por etapa, excluidos con motivo, política de consentimiento como dato, envío en dos pasos, enlace propio de 7 días, tope diario **compartido** con Outreach (15/día), registro `candidate_sends`, nota en el Pool sin cambiar la etapa. Suite 1027/0; mutaciones de cada exclusión fallan sus tests.
- Retrospectiva aplicada: kit `CLAUDE.md` (`da6ae31`: heredoc con barras → Write; `git checkout` devuelve CRLF) + 5 memorias.

## Where We Paused
**Last action:** push de 1.5.8 (`132d148`), prod reporta 1.5.8. Andrés pidió cerrar y dejar el resto para la próxima sesión.
**Next action:** prueba real del envío (pasos de Andrés, abajo). Nada se ha mandado a un candidato real todavía.
**Blockers:** la prueba la hace Andrés en el admin de prod; requiere el CSV que está SOLO en el portátil.

### Pasos de la prueba real (Andrés)
1. **Pool → Import applications**: subir `D:\Downloads\pool-test-entries.csv` (**solo en el portátil**; 2 filas: `berandre2+test1@gmail.com`, `andresbermudez50@hotmail.com`). Desde otra máquina, recrear un CSV con `name,email,applied_at` y esas 2 filas.
2. En el Pool, pasar las 2 a **Submitted** (los postulantes reales están en New; así no reciben nada).
3. **KT-004 → Candidate campaign**: revisar el texto guardado, **Activate**, en Recipients dejar **solo Submitted** → Filter.
4. **Confirmar que la lista muestra SOLO esas 2 direcciones** → Send to 2 → Confirm send → captura del resultado.
5. Revisar las 2 bandejas (incluido spam de Hotmail): dónde cayó, si el enlace abre la entrevista, si la baja funciona.

## Files to Read First
- `hiresignal/.agents/build-state/integraciones-pool.md` — checkpoint vivo del sprint; tabla de 10 criterios + evidencia por versión.
- `hiresignal/api/candidate-send-lib.php` — destinatarios, política, envío (dependencias inyectables).
- `hiresignal/admin/candidate-campaign.php` — la pantalla (IA, plantillas, Recipients).
- `hiresignal/docs/provisionar-instancia-cliente.md` — runbook de clientes (agregados hoy: `OUTREACH_FROM_NAME`, `OUTREACH_DAILY_CAP`).

## Notes / Gotchas
- **Deploy que no llega:** si health no cambia en ~3 min, commit vacío y mirar DO **Activity** (no Runtime Logs).
- **Local:** Postgres portable `D:\tools\pg16`, cluster `D:\tools\pgdata-it`, puerto 5433, DB `hs_outreach_it`; server `php -S 127.0.0.1:8765 ... tests/browser/router.php`; Edge CDP 9333. Sin `ANTHROPIC_API_KEY` en el portátil: para la IA local se apunta `llm_report_url` (doc `settings` de la base local) a un stub; **borrar esa fila al terminar** (hoy quedó borrada).
- Local tiene 3 filas `failed` borradas de `candidate_sends`; las invitaciones de prueba "Campaign:" de KT-001 siguen en el kv_store local (inofensivas, base de pruebas).
- Scripts de reemplazo: escribirlos con Write (no heredoc) y normalizar fin de línea; varios archivos de hiresignal están en CRLF tras `git checkout`.
- El envío usa el texto **guardado**, no el de los formularios; la pantalla avisa si hay ediciones sin guardar.

## Questions to Answer
- **Vacantes "auto" (EN+FR):** hoy mandan en **inglés** a todos (el Pool no sabe el idioma de cada candidato). **Nunca se le dijo a Andrés** — decidir.
- **"Una forma de crear usuarios"** (Andrés): entendido como alta manual de candidatos CON base de consentimiento, para que califiquen. Sin confirmar; si era "usuarios admin" es otro proyecto.
- **Criterio 8** (un follow-up a 7 días si el enlace no se usó y sigue vigente): sin construir. Es lo último del sprint.
- Pendientes que vienen de antes: 2026-09-24 Send follow-ups de Outreach (TEST A debe recibir `Re:`, C suprimido); revisión del borrador de reclutamiento con Hugo; francés por hablante de Quebec.
