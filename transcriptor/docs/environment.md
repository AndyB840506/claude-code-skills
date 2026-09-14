# Notas de entorno

Dos máquinas, misma estructura, distinta unidad — detectar con `Test-Path "E:\Transcriptor"`
(ver Paso 0 de `workflows/transcribe.md`), nunca hardcodear la letra.

| | Escritorio | Portátil |
|---|---|---|
| Unidad | `E:\Transcriptor\` | `D:\Transcriptor\` (desde 2026-09-14 — no hay `E:` en esta máquina) |
| GPU | RTX 3080 Ti 12GB | RTX 3060 Laptop 6GB |
| HF_TOKEN persistido | Sí (2026-06-12) | Sí (2026-09-14) |

- **venv:** `<unidad>\Transcriptor\venv-whisperx\` (Python 3.12, whisperx 3.8.6, torch 2.8.0+cu128) — mismas versiones en ambas máquinas, verificado con smoke test end-to-end en el portátil el 2026-09-14 (SRT idéntico en formato al del escritorio: `[SPEAKER_00]:`, timestamps, diarización).
- **Cache de modelos HF:** `<unidad>\Transcriptor\hf-cache\` (env var de usuario `HF_HOME` — los modelos no van a C:)
- **Cache torch hub:** `<unidad>\Transcriptor\torch-cache\` (env var de usuario `TORCH_HOME` — ahí viven los alineadores wav2vec2: `voxpopuli` para español, `WAV2VEC2_ASR_BASE_960H` para inglés. WhisperX descarga el que falte la primera vez que se usa ese idioma)
- **HF token:** persistido como env var de usuario `HF_TOKEN` en ambas máquinas — el workflow lo encuentra solo y no hay que pedirlo.
- **ffmpeg:** requerido por whisperx para decodificar audio — instalado vía winget. En el portátil, `Gyan.FFmpeg` (build completa) dio timeout de descarga (504 Gateway, reproducido 2 veces) — funcionó `Gyan.FFmpeg.Essentials` (build más liviana). Si la build completa falla por timeout, probar la Essentials antes de asumir un bloqueo de red/antivirus.
- **Ojo torch:** si se reinstala whisperx, pip puede pisar torch con la build CPU. Verificar `torch.cuda.is_available()` y, si da False, reinstalar: `pip install --force-reinstall --no-deps torch==2.8.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cu128`
- **Ojo variables de entorno recién configuradas en la MISMA sesión de Claude Code:** `[System.Environment]::SetEnvironmentVariable(..., "User")` escribe el registro correctamente (verificable con `GetEnvironmentVariable(..., "User")`), pero un proceso ya en marcha (incluida toda una sesión de Claude Code, y cada llamada de herramienta dentro de ella) no ve el cambio — seguirá leyendo el valor viejo (o vacío) hasta que se abra un proceso genuinamente nuevo después de reiniciar la sesión/terminal. Mordió el 2026-09-14 configurando `HF_HOME`/`TORCH_HOME` en el portátil: WhisperX igual descargó ~3.3GB a `C:\Users\andre\.cache\` (la ubicación default) porque la sesión no vio las variables nuevas, a pesar de que el registro ya las tenía bien. **Si hay que usar la variable en la misma sesión donde se configuró, pasarla inline en esa llamada** (`$env:HF_HOME = "..."` antes del comando), no confiar en que ya quedó persistida. Mismo patrón con el PATH tras instalar algo por winget.
- **Cache de HuggingFace es compartido entre skills** — `C:\Users\andre\.cache\huggingface\hub\` puede tener modelos de otras herramientas (ej. `models--1038lab--llama-joycaption-beta-one` de ComfyUI/imagen-a-prompt). Si algo queda cacheado ahí por error (ver punto anterior), mover solo las carpetas `models--*` específicas de whisperx/pyannote — nunca la carpeta `hub\` completa.
- **Audios entrada:** `<unidad>\Transcriptor\audios\`
- **SRTs salida:** `<unidad>\Transcriptor\transcripciones\`
- **Modelo:** large-v2 (requiere GPU/CUDA — ambas máquinas tienen CUDA configurado)
- **Idiomas soportados:** español (`--language es`, default) e inglés (`--language en`) —
  se pregunta en modo standalone; en modo pipeline se puede pasar como segundo argumento,
  si no se pasa usa español (BTQ y MPD son ambos en español)
- **Speakers:** diarización automática (Pyannote detecta cambios de speaker sin número fijo)
- El warning de `torchcodec` en el log es inofensivo — la transcripción funciona igual

# Integración con pipelines

Cuando episode-pipeline (BTQ o MPD) llama esta skill, pasa la ruta del audio como argumento
(y opcionalmente el idioma, si el show no es en español):

```
/transcriptor E:\Transcriptor\audios\BTQ-EP017.mp3
/transcriptor E:\Transcriptor\audios\SHOW-EP001.mp3 en
```

La skill corre en modo silencioso y devuelve el path del SRT al pipeline para el siguiente paso (show notes, guión, etc.).
