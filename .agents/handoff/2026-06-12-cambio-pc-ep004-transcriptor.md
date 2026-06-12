# Handoff: Cambio de máquina (portátil → escritorio) — EP.004 assets listos + transcriptor

**Date:** 2026-06-12
**Status:** In progress — assets EP.004 completos; transcriptor pendiente de verificar EN EL ESCRITORIO; grabación es HOY

---

## ⚠️ Contexto de máquinas (leer primero)

Andres trabaja en **DOS PCs**:
- **Portátil** (donde se escribió este handoff): discos C: y D: solamente. SIN E:, sin Python real, sin WhisperX. RTX 3060 Laptop 6GB.
- **PC de escritorio** (donde se retoma): discos C:, D: y E:. Ahí debería vivir `E:\Transcriptor\` (venv WhisperX, audios, transcripciones) tal como lo describe la skill `transcriptor`.

La conclusión previa "E: no existe — máquina anterior" era INCOMPLETA: E: no existe en el portátil, pero sí en el escritorio. Memoria corregida (`two-pcs-laptop-vs-desktop`). NO reinstalar nada hasta verificar qué hay en el escritorio.

## What We Accomplished This Session

- **EP.004 guion v4** (commit 284467f, sesión anterior del mismo día): expansión a 2,717 palabras habladas (~19.4 min a 140 ppm), balance 70/30 exacto (Andrés 1,902 / Juan 815). Densidad EP.002–003. Contenido nuevo: ultrametal paisa + cartas de Euronymous, Batalla de las Bandas 1985 (la cuenta Juan), herencia latina/estigma, segmento "La Voz y las Tripulaciones", legado.
- **Quote cards EP.004** (commit fb8b8a8): 5 prompts Flow completos 16:9 en `artwork-ep004.md` — Q1 Cartas de Noruega, Q2 La Macarena split 1985/1987, Q3 El Idioma, Q4 La Voz, Q5 El Titán. + 2 alternates en banca (Teatro Lux, Vestido de Cristal).
- **Plan social / teasers EP.004** (commit e570530): `social-ep004.md` nuevo — 3 días (Jue 12 intriga cartas-Noruega / Vie 13 quote materia prima / Sáb 14 lanzamiento), copy para IG/FB, Stories, X, TikTok. + Teaser cards T1 y T2 en 9:16 agregados a `artwork-ep004.md`.
- **Diagnóstico transcriptor en el PORTÁTIL:** roto ahí (sin E:, sin Python, sin WhisperX). Se propuso reinstalar en D:\ del portátil — **PLAN DESCARTADO** al aclararse que existe el escritorio con E:. No se instaló nada.
- Memoria `two-pcs-laptop-vs-desktop` actualizada (reemplaza `e-drive-absent-post-wipe`).

## Where We Paused

**Last action:** Commit + push de teasers (e570530), corrección de memoria de las dos máquinas, y este handoff.
**Next action (en el escritorio):**
1. `git pull origin main` en ambos clones (repo kit-skill-creator y ~/.claude/skills).
2. Verificar el transcriptor donde sí debería estar: `Test-Path E:\Transcriptor\venv-whisperx` + `nvidia-smi` + probar activación del venv. Si está sano, no hay nada que instalar — solo confirmar que está listo para el audio de hoy.
3. Preguntar a Andres qué next steps ya completó (regla del handoff — no asumir).

**Blockers:**
- Eventos reales de Juan para `eventos.json` — el segmento de Promoción del guion está como placeholder (ver markers abajo). Debe resolverse ANTES o DURANTE la grabación de hoy.
- HF token: lo provee Andres al correr el transcriptor (no se guarda en disco).

## Files to Read First

- `mrputridsden-production/episodios/artwork-ep004.md` — paquete completo: 3 portadas + 5 quote cards + 2 teaser cards (todo listo para Google Flow)
- `mrputridsden-production/episodios/social-ep004.md` — plan teasers 3 días con copy por plataforma
- `mrputridsden-production/scripts/EP004-kraken-el-titan-del-rock-colombiano.html` — guion v4 final para la grabación de hoy
- `~/.claude/skills/transcriptor/` (SKILL.md, docs/environment.md, workflows/transcribe.md) — rutas E:\Transcriptor a verificar en el escritorio
- `mrputridsden-production/pipeline-state-ep004.md` — estado del pipeline del episodio

## Pending Markers (proyecto)

- `pipeline-state-ep004.md:6` — PENDIENTE: Juan debe pasar eventos reales (eventos.json solo tiene ejemplos). **Actúa: Juan/Andres.**
- `EP004-kraken...html:295` y `:638` — Promoción como placeholder; opción B documentada: grabar el segmento como recomendación general de apoyar la escena local. **Actúa: Juan/Andres al grabar hoy.**

## Notes / Gotchas

- **Quote cards y teaser T2:** el wording sale del guion v4 — confirmar contra el AUDIO grabado antes de publicar (si la frase salió distinta al aire, ajustar el card).
- **Fechas del plan social:** asumen publicación sábado 14 junio (espejo de EP.002: grabación jueves → live sábado). Si la publicación se mueve, correr la secuencia completa, no saltarse días.
- **Transcriptor en 6GB VRAM (si tocara correrlo en el portátil):** large-v2 + diarización puede quedar justo — fallback `--compute_type int8`. En el escritorio verificar la GPU con `nvidia-smi` antes de asumir.
- Teatro Lux: dos cifras en fuentes (980 El Colombiano vs 1,200 La Carne) — el guion usa 980 y la discrepancia está documentada en la sección Fuentes.
- Seguridad pendiente de sesiones previas (lado Andres): borrar repo GitHub `AndyB840506/estimador` (`gh auth refresh -h github.com -s delete_repo` y luego `gh repo delete AndyB840506/estimador --yes`) + revocar el Gmail App Password expuesto (Google Account → Security → App Passwords).

## Questions to Answer

- ¿El escritorio tiene `E:\Transcriptor\` intacto con el venv funcional, o también requiere setup?
- ¿Dónde va a quedar el audio crudo de la grabación de hoy (escritorio E:\Transcriptor\audios\ presumiblemente)?
- ¿Juan pasó los eventos reales, o el segmento de Promoción se graba como recomendación general?
