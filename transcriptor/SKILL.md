---
name: transcriptor
description: "Transcribe podcast audio to SRT using WhisperX (large-v2, Spanish, speaker diarization). Triggers: transcribir, transcripción, transcribe audio, procesar audio, pasar a texto, transcribe, process audio, run whisperx."
---

# Transcriptor — WhisperX con diarización

Transcribe audios de podcast a SRT usando WhisperX (large-v2, español, diarización por speakers).

Funciona en dos modos:
- **Standalone:** el usuario pide transcribir un audio
- **Pipeline:** llamado desde episode-pipeline (BTQ o MPD) con ruta de audio como argumento

## Workflow

Sigue `workflows/transcribe.md` — determina modo y ruta del audio, verifica el HF
token, corre WhisperX, confirma el output.

## Reference

- `docs/environment.md` — rutas de venv/audios/transcripciones, modelo, idioma, e
  integración con pipelines
