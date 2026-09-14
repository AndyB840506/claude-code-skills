# Handoff: transcribeme-prep + WhisperX en el portátil

**Date:** 2026-09-14
**Machine:** laptop (D:\) — esta sesión corrió aquí, sin `E:`
**Status:** Complete — falta solo el commit/push automático de session-close (Steps 4-6, en curso ahora mismo)

---

## What We Accomplished This Session

- **Nuevo skill `transcribeme-prep`** (global, `~/.claude/skills/transcribeme-prep` + espejo en
  `kit-skill-creator/transcribeme-prep`) — separado de `transcriptor`, nunca lo toca. Dos modos:
  - `portfolio-sample.md` — SRT → `.docx` presentable (S1/S2, timestamps cada ~2min o en cambio
    de speaker, vía `scripts/srt_to_docx.py` con `python-docx`)
  - `clean-verbatim-practice.md` — reescritura Clean Verbatim para practicar el examen de
    ingreso de TranscribeMe (sin speakers/timestamps, quita muletillas, normaliza crutchwords)
  - Reglas documentadas con su fuente (oficial transcribeme.com vs. terceros) en
    `docs/clean-verbatim-rules.md` — no presentar lo de terceros como confirmado al 100%.
  - Verificado con SRT sintético: remapeo de speakers, fusión de turnos, umbral de 120s para
    timestamps, y auto-chequeo de la práctica (grep de muletillas/crutchwords → 0).

- **WhisperX instalado en el portátil** (`D:\Transcriptor\venv-whisperx\`), mismas versiones que
  el escritorio (Python 3.12, whisperx 3.8.6, torch 2.8.0+cu128). Verificado de punta a punta con
  un smoke test real (audio TTS sintético → SRT con diarización, formato idéntico al del
  escritorio). GPU confirmada en uso (RTX 3060 Laptop, `torch.cuda.is_available() == True`,
  "defaulting to float16 for device cuda" en el log).

- **HF_TOKEN válido persistido** — probé los 4 tokens que Andrés fue pegando contra la API real
  de HuggingFace (`whoami-v2`); los primeros 2 dieron 401 (no eran válidos), el 3º y 4º sí
  funcionan (misma cuenta AndyB840506). Quedó guardado el 3º (`hf_gMlxW...`, display name
  "WhisperX Laptop"). El 4º (`hf_gnffR...`, "Whisper 2 for Laptop") también sirve — Andrés no
  confirmó si prefiere ese en su lugar (funcionalmente da igual, misma cuenta y permisos).

- **Fix real en `transcriptor` y `episode-pipeline`**: ambos tenían `E:\Transcriptor\...` fijo a
  fuego (fallaría tal cual en el portátil). Cambiado a detección dinámica
  (`if (Test-Path "E:\Transcriptor") {...} else { $base = "D:\Transcriptor" }`) en:
  - `transcriptor/workflows/transcribe.md` (Paso 0 nuevo + 3 rutas actualizadas)
  - `transcriptor/docs/environment.md` (tabla comparativa escritorio/portátil)
  - `episode-pipeline/workflows/01-transcription.md` (3 rutas actualizadas)
  - No se tocó el formato de salida del SRT ni el comportamiento del pipeline — solo las rutas.

- **`CLAUDE.md` actualizado** — nuevo bullet en § "Instrumentos que mienten en silencio": un
  `SetEnvironmentVariable(...,"User")` recién corrido en la MISMA sesión no lo ve ningún proceso
  ya en marcha (mismo patrón que el PATH tras `winget install`, generalizado a cualquier env var).
  Mordió hoy mismo: `HF_HOME`/`TORCH_HOME` se configuraron bien en el registro pero WhisperX
  igual descargó ~3.3GB a `C:\Users\andre\.cache\` en la misma sesión — se movieron manualmente a
  `D:\Transcriptor\` (solo las carpetas `models--*` de whisperx/pyannote, sin tocar el cache
  compartido de otras skills como `imagen-a-prompt`/ComfyUI).

- Ambos clones (`~/.claude/skills` y el repo `kit-skill-creator`) verificados idénticos
  (`diff -rq`) después de cada cambio — `transcribeme-prep/`, `transcriptor/`,
  `episode-pipeline/workflows/01-transcription.md`, y `CLAUDE.md`.

## Where We Paused

**Last action:** actualicé `CLAUDE.md` en ambos clones con el bullet de la retrospectiva
(env-var-propagation gotcha), confirmado con `git diff` que no se perdió nada al sincronizar.

**Next action:** este handoff se commitea/pushea ahora (Step 3 de session-close); inmediatamente
después, Step 4 hace el sync real de `~/.claude/skills` (commit+push de `transcribeme-prep`,
`transcriptor`, `episode-pipeline`, `CLAUDE.md`) y Step 5 el continuity sync. Ahora mismo
**nada de esto está commiteado todavía** salvo este propio archivo de handoff.

**Blockers:** ninguno real. Pendiente menor: confirmar con Andrés si prefiere el token
"Whisper 2 for Laptop" en vez del que quedó guardado — no bloquea nada, ambos funcionan igual.

## Files to Read First

- `transcribeme-prep/SKILL.md` — punto de entrada del skill nuevo, router de los 2 modos
- `transcriptor/docs/environment.md` — tabla con el estado real de ambas máquinas (unidad, GPU, HF_TOKEN)
- `CLAUDE.md` línea ~185 — el bullet nuevo sobre env vars, para no repetir el mordisco

## Notes / Gotchas

- **ffmpeg**: la build completa de `Gyan.FFmpeg` vía winget dio timeout de descarga (504 Gateway,
  reproducido 2 veces) en este portátil — funcionó `Gyan.FFmpeg.Essentials` (más liviana). El
  PATH quedó bien en el registro pero no se refleja en esta sesión (mismo patrón de env vars) —
  se resuelve solo abriendo una terminal nueva.
- **Cache de HuggingFace es compartido entre skills** en `C:\Users\andre\.cache\huggingface\hub\`
  — no mover la carpeta completa si algo queda mal cacheado, solo las subcarpetas `models--*`
  específicas del problema.
- **`episode-pipeline/workflows/01-transcription.md` sigue con una referencia rota** a
  `transcriptor/workflows/00-setup.md` (no existe) en su sección "Si algo falla" — encontrado hoy,
  fuera de alcance (no se tocó), Andrés confirmó que puede quedar aparte por ahora.
- El SRT de prueba generado durante el smoke test (`test-smoke.wav`/`.srt`) se borró al terminar
  — no queda nada de prueba en `D:\Transcriptor\audios\` ni `transcripciones\`.

## Questions to Answer

- ¿Cuál de los 2 tokens HF válidos prefiere Andrés dejar activo? (no urgente, ambos sirven)
- ¿Vale la pena crear `transcriptor/workflows/00-setup.md` para cerrar la referencia rota de
  `episode-pipeline`, o se documenta como retirada/no aplicable? — abierto, no se decidió hoy.
