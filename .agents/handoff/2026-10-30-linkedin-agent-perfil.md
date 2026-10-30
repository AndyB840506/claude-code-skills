# Handoff: linkedin-agent, plugin li-* y limpieza del perfil de LinkedIn
**Date:** 2026-10-30
**Machine:** laptop (D:\)
**Status:** In progress — perfil actualizado y verificado en vivo; quedan las recomendaciones y la exportación

---

## What We Accomplished This Session

- **`repos\linkedin-agent`:** app Python instalada y cambiada: sin CrewAI, login manual con sesión en `.chrome-profile`, Selenium Manager y `LLM_PROVIDER` (`ollama` por defecto con `gemma3:4b`, o `anthropic`). Corrida real OK: 5 conversaciones y 5 sugerencias.
- **Ollama:** 0.40.13 instalado en el portátil; modelos en `D:\AI\ollama\models`.
- **Plugin `linkedin-agent@linkedin-agent-skill`:** 11 skills `li-*` instaladas desde `repos\linkedin-agent-skill`, con ajustes locales: `slop-es.json`, detector con tildes, emojis ZWJ protegidos y datos en `repos\linkedin-content`.
- **`repos\linkedin-content\voice.md`:** perfil de voz con muestras reales de Andy.
- **Perfil de LinkedIn:** titular, Acerca de, URL `andres-bermudez84`, foto, Destacados en 4 tarjetas, Services, 17 experiencias, duplicados fuera y MBAs falsos borrados. Última medición completa: 76/100; estimado tras los cambios finales: 78.
- **Recomendaciones:** pedidas por mensaje directo a Hugo Lancheros, Santiago Sanchez (`santiagosanchez-rrhh-tech`) y Jose Ramirez (`joseramirezprofile`, Oliver Wyman).
- **Retrospectiva:** 3 entradas nuevas en `CLAUDE.md` y `feedback_linkedin_own_account.md`.

## Where We Paused

**Last action:** cierre de sesión después de actualizar Services.
**Next action:** preguntar a Andy si llegó la exportación de LinkedIn y si Hugo, Santiago o José respondieron.
**Blockers:** el correo de exportación (pedida el 2026-10-30 a las 8:20 PM según LinkedIn; el enlace dura 72 horas) y las respuestas de los tres contactos.

## Files to Read First

- `C:\Users\andre\repos\linkedin-content\voice.md` — perfil de voz que leen las skills `li-*`.
- `C:\Users\andre\repos\linkedin-content\perfil\` — respaldos y textos aplicados; `respaldo-completo-2026-10-30.json` tiene todas las descripciones previas a la limpieza.
- Memoria `project_linkedin_agent.md` y `feedback_linkedin_own_account.md`.

## Notes / Gotchas

- **Máquina:** todo esto vive solo en el portátil. `linkedin-agent`, `linkedin-agent-skill` y `linkedin-content` no están en GitHub con estos cambios, y `.chrome-profile` tampoco viaja.
- **Copias con cambios sin commit:** los dos repos son clones de terceros; no hay remoto propio donde subirlos.
- **Plugin:** el CLI está en `%USERPROFILE%\.vscode\extensions\anthropic.claude-code-*\resources\native-binary\claude.exe`, no en el PATH. Tras editar el repo hay que reinstalar el plugin.
- **Permisos:** el clasificador bloqueó algunas escrituras externas y dejó pasar otras. Si bloquea, no rodearlo: pasar el comando a Andy.
- **Scripts de esta sesión:** estaban en el scratchpad y son temporales. Sirven como referencia los patrones de memoria y `CLAUDE.md`, no esas rutas.
- **NO VERIFICADO:** si Andy borró `LINKEDIN_EMAIL` y `LINKEDIN_PASSWORD` de `repos\linkedin-agent\.env`. A las 3:02 PM seguían ahí.
- **NO VERIFICADO:** si el CV menciona un MBA. `repos\cv` no existe en el portátil. Andy no tiene MBA: sus títulos son pregrados.

## Questions to Answer

- ¿Llegó la exportación? Dejar en `repos\linkedin-content\export` y filtrar solo los textos de Andy para afinar `voice.md`. No subirla a GitHub.
- ¿Andy quiere fork privado de `linkedin-agent` y `linkedin-agent-skill` para respaldar los cambios?
- Pendiente de `start.ps1`, no relacionado: `kit-ai-lead-generator` tiene trabajo sin commit o sin push.
