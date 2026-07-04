# Notas de entorno

- **venv:** `E:\Transcriptor\venv-whisperx\` (Python 3.12, whisperx 3.8.6, torch 2.8.0+cu128)
- **Cache de modelos HF:** `E:\Transcriptor\hf-cache\` (env var de usuario `HF_HOME` — los modelos no van a C:)
- **Cache torch hub:** `E:\Transcriptor\torch-cache\` (env var de usuario `TORCH_HOME` — ahí viven los alineadores wav2vec2: `voxpopuli` para español, `WAV2VEC2_ASR_BASE_960H` para inglés. WhisperX descarga el que falte la primera vez que se usa ese idioma)
- **HF token:** en el escritorio está persistido como env var de usuario `HF_TOKEN` (decisión de Andres, 2026-06-12) — el workflow lo encuentra solo y no hay que pedirlo. En el portátil no está guardado: pedirlo al usuario.
- **ffmpeg:** requerido por whisperx para decodificar audio — instalado vía winget (Gyan.FFmpeg), ya en PATH. Si una sesión vieja no lo ve, recargar PATH o abrir shell nueva.
- **Ojo torch:** si se reinstala whisperx, pip puede pisar torch con la build CPU. Verificar `torch.cuda.is_available()` y, si da False, reinstalar: `pip install --force-reinstall --no-deps torch==2.8.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cu128`
- **Audios entrada:** `E:\Transcriptor\audios\`
- **SRTs salida:** `E:\Transcriptor\transcripciones\`
- **Modelo:** large-v2 (requiere GPU/CUDA — el sistema tiene CUDA configurado)
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
