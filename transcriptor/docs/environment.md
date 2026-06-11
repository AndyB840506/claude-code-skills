# Notas de entorno

- **venv:** `E:\Transcriptor\venv-whisperx\`
- **Audios entrada:** `E:\Transcriptor\audios\`
- **SRTs salida:** `E:\Transcriptor\transcripciones\`
- **Modelo:** large-v2 (requiere GPU/CUDA — el sistema tiene CUDA configurado)
- **Idioma:** español (`--language es`) — cambiar solo si el audio es en otro idioma
- **Speakers:** diarización automática (Pyannote detecta cambios de speaker sin número fijo)
- El warning de `torchcodec` en el log es inofensivo — la transcripción funciona igual

# Integración con pipelines

Cuando episode-pipeline (BTQ o MPD) llama esta skill, pasa la ruta del audio como argumento:

```
/transcriptor E:\Transcriptor\audios\BTQ-EP017.mp3
```

La skill corre en modo silencioso y devuelve el path del SRT al pipeline para el siguiente paso (show notes, guión, etc.).
