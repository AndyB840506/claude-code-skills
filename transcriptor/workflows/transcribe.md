# Execution

## Paso 1 — Determinar modo y ruta del audio

**Si fue llamado desde el pipeline** (el mensaje incluye una ruta de audio explícita como argumento):
- Tomar esa ruta directamente
- Saltar al Paso 2 sin hacer preguntas

**Si fue invocado standalone:**
- Revisar si hay archivos en `E:\Transcriptor\audios\`:
  ```powershell
  Get-ChildItem "E:\Transcriptor\audios" -Include "*.mp3","*.wav","*.m4a","*.mp4" -Recurse | Sort-Object LastWriteTime -Descending | Select-Object -First 5
  ```
- Si hay archivos: mostrar la lista y preguntar cuál transcribir (o confirmar el más reciente)
- Si la carpeta está vacía: pedir al usuario que pegue la ruta completa del audio

## Paso 2 — Verificar HF token

Revisar si el token está disponible:
```powershell
$env:HF_TOKEN
```

- Si tiene valor: usarlo silenciosamente
- Si está vacío o no existe: pedir al usuario:
  > Para diarización necesito tu HuggingFace token. Pégalo aquí (no se guarda en disco):

  Guardar en `$env:HF_TOKEN` solo para esta sesión.

## Paso 3 — Correr WhisperX

Ejecutar con PowerShell:

```powershell
$env:PYTHONUTF8 = "1"
& "E:\Transcriptor\venv-whisperx\Scripts\Activate.ps1"
whisperx "<RUTA_AUDIO>" `
  --language es `
  --model large-v2 `
  --diarize `
  --hf_token $env:HF_TOKEN `
  --output_dir "E:\Transcriptor\transcripciones" `
  --output_format srt
```

Reemplazar `<RUTA_AUDIO>` con la ruta real del archivo.

Esperar a que termine (puede tardar varios minutos dependiendo del largo del audio).

## Paso 4 — Confirmar output

Una vez terminado:
1. Buscar el SRT generado en `E:\Transcriptor\transcripciones\`:
   ```powershell
   Get-ChildItem "E:\Transcriptor\transcripciones" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
   ```
2. Confirmar al usuario con el path completo del SRT generado

**Modo pipeline:** devolver solo el path del SRT para que el pipeline continúe.

**Modo standalone:** mostrar mensaje de éxito con el path y el nombre del archivo.
