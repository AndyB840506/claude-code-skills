---
name: transcribeme-prep
description: "Prepara materiales para aplicar a plataformas de transcripción profesional (TranscribeMe y similares): muestra de portfolio en .docx a partir de un SRT existente, o práctica de reescritura Clean Verbatim para su examen de ingreso. Triggers: transcribeme, muestra de transcripción, portfolio transcripción, examen clean verbatim, transcribeme practice, exam prep, transcript sample, práctica examen transcripción."
---

# TranscribeMe Prep — muestras y práctica de examen

Este skill **nunca toca `transcriptor` ni su formato de salida**. Solo lee un SRT que ya existe,
o invoca `/transcriptor` como caja negra para producir uno nuevo. El SRT original queda intacto
siempre — esto genera un artefacto nuevo y separado, no un reemplazo. No viola la regla de
"nunca post-procesar SRT a TXT" del pipeline de podcasts (esa regla protege el entregable de
producción; este skill no es ese entregable).

Dos modos, comparten el mismo insumo:

1. **Muestra de portfolio** (`workflows/portfolio-sample.md`) — genera un `.docx` presentable
   con speaker labels `S1`/`S2`, timestamps cada ~2 min o en cambio de speaker, para mostrar
   calidad de trabajo en una aplicación.
2. **Práctica de examen Clean Verbatim** (`workflows/clean-verbatim-practice.md`) — reescribe un
   fragmento quitando muletillas y normalizando crutchwords, sin speakers ni timestamps, siguiendo
   las reglas documentadas en `docs/clean-verbatim-rules.md`.

## Paso 0 — Determinar insumo y modo

1. **¿Hay audio o SRT?**
   - Si el usuario da un audio y esta máquina tiene `transcriptor` disponible (existe
     `E:\Transcriptor\venv-whisperx\` o `D:\Transcriptor\venv-whisperx\` — chequear con
     `Test-Path`, no asumir una unidad fija): ofrecer invocar `/transcriptor` primero y usar el
     SRT resultante.
   - Si no hay audio ni transcriptor disponible en esta máquina: pedir la ruta de un SRT
     existente, o — solo para el modo de práctica de examen — aceptar texto pegado directamente
     (no requiere SRT en ese modo).
2. **¿Qué modo?** Preguntar directamente si no es obvio por el pedido del usuario — no asumir:
   - "muestra de portfolio" → `workflows/portfolio-sample.md`
   - "práctica de examen" / "clean verbatim" → `workflows/clean-verbatim-practice.md`

## Reference

- `docs/environment.md` — rutas de salida por máquina, chequeo/instalación de `python-docx`
- `docs/clean-verbatim-rules.md` — reglas del examen de TranscribeMe, cada una con su fuente
- `docs/transcribeme-format-reference.md` — formato de entregable real de TranscribeMe (S1/S2, timestamps)
