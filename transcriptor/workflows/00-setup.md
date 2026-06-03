# Setup — Verificar e instalar dependencias

Ejecutar este workflow la primera vez antes de transcribir, o si `whisper` no responde.

---

## Paso 1 — Verificar Python

```powershell
python --version
```

- Si retorna `Python 3.8.x` o superior: continuar.
- Si retorna error o versión menor a 3.8: pedir al usuario que instale Python desde https://python.org (versión 3.11 recomendada). Detener aquí hasta que esté instalado.

---

## Paso 2 — Verificar Whisper

```powershell
whisper --help
```

- Si retorna el menú de ayuda: Whisper ya está instalado. Saltar al Paso 4.
- Si retorna error `'whisper' is not recognized`: continuar al Paso 3.

---

## Paso 3 — Instalar Whisper

```powershell
pip install openai-whisper
```

Esto instala el paquete `openai-whisper` (no confundir con la API de OpenAI — este es el modelo local, sin API key).

Después de instalar, verificar nuevamente:
```powershell
whisper --help
```

Si sigue sin funcionar, intentar con:
```powershell
python -m whisper --help
```

Si el segundo comando funciona pero el primero no, usar `python -m whisper` en lugar de `whisper` en todos los comandos del workflow `01-transcribir.md`.

---

## Paso 4 — Verificar ffmpeg

```powershell
ffmpeg -version
```

- Si retorna la versión de ffmpeg: todo listo. Saltar al Paso 6.
- Si retorna error: continuar al Paso 5.

---

## Paso 5 — Instalar ffmpeg

Opción A (recomendada, via winget):
```powershell
winget install --id Gyan.FFmpeg --source winget --silent
```

Opción B (manual):
1. Ir a https://ffmpeg.org/download.html → Windows builds
2. Descargar el ZIP de la versión "essentials"
3. Extraer a `C:\ffmpeg\`
4. Agregar `C:\ffmpeg\bin` al PATH del sistema:
   - Buscar "Variables de entorno" en el menú inicio
   - Editar la variable `Path` del sistema
   - Agregar `C:\ffmpeg\bin`
5. Reiniciar la terminal y verificar con `ffmpeg -version`

---

## Paso 6 — Crear carpetas de trabajo

Crear la estructura de carpetas en `E:\`:

```powershell
New-Item -ItemType Directory -Force -Path "E:\Transcriptor\audios"
New-Item -ItemType Directory -Force -Path "E:\Transcriptor\transcripciones"
```

`-Force` evita error si las carpetas ya existen.

---

## Paso 6.5 — Solución si el modelo no descarga (SSL / Avast)

Si al correr la primera transcripción aparece este error:

```
ssl.SSLCertVerificationError: certificate verify failed: Basic Constraints of CA cert not marked critical
```

Causa: Avast (u otro antivirus) inyecta su propio certificado CA que Python 3.14 rechaza. La descarga del modelo se bloquea.

Solución — descargar el modelo manualmente con `requests` (que acepta `verify=False`):

```powershell
$env:PYTHONUTF8 = "1"
& python -c @'
import requests, os, pathlib
url = "https://openaipublic.azureedge.net/main/whisper/models/345ae4da62f9b3d59415adc60127b97c714f32e89e936602e85993674d08dcb1/medium.pt"
dest = pathlib.Path.home() / ".cache" / "whisper" / "medium.pt"
dest.parent.mkdir(parents=True, exist_ok=True)
print(f"Descargando a {dest}...")
r = requests.get(url, verify=False, stream=True)
total = int(r.headers.get("content-length", 0))
downloaded = 0
with open(dest, "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)
        downloaded += len(chunk)
        if total:
            print(f"{downloaded//1024//1024} MB / {total//1024//1024} MB", end=chr(13))
print("Listo.")
'@
```

El modelo `medium` (769 MB) quedará en `C:\Users\andre\.cache\whisper\medium.pt` y Whisper lo usará automáticamente.

---

## Paso 7 — Confirmar instalación

Mostrar al usuario:

```
✓ Python: [versión detectada]
✓ Whisper: instalado
✓ ffmpeg: instalado
✓ Carpetas listas:
    E:\Transcriptor\audios\           ← aquí subes los archivos de audio
    E:\Transcriptor\transcripciones\  ← aquí aparecen las transcripciones

Setup completo. Ya puedes transcribir archivos de cualquier duración.

NOTA: La primera vez que uses un modelo (ej. medium), Whisper lo descarga
automáticamente (~769 MB). Esa descarga ocurre una sola vez.

Para transcribir: copia tu audio en E:\Transcriptor\audios\ y escribe
"transcribir [nombre del archivo]" o simplemente la ruta completa.
```

---

## Paso 8 (opcional) — Instalar whisperx para diarización de hablantes

Solo necesario si el audio tiene **más de un interlocutor** y quieres que el transcriptor identifique quién habla.

**Requisito importante:** whisperx NO es compatible con Python 3.14. Requiere un entorno separado con Python 3.12.

### 8a — Instalar Python 3.12 (si no está instalado)

```powershell
py --list
```

Si no aparece `-V:3.12`: instalar con winget:

```powershell
winget install --id Python.Python.3.12 --source winget --silent
```

### 8b — Crear venv Python 3.12 para whisperx

```powershell
py -3.12 -m venv "E:\Transcriptor\venv-whisperx"
```

### 8c — Instalar whisperx en el venv

**Pausar Avast temporalmente** antes de este paso (click derecho → Avast shields control → Disable for 10 minutes). Los modelos se descargan de huggingface.co y Avast bloquea la conexión SSL.

```powershell
& "E:\Transcriptor\venv-whisperx\Scripts\pip.exe" install whisperx
```

### 8d — Reemplazar PyTorch con versión CUDA

El paso anterior instala PyTorch CPU. Reemplazarlo con la versión CUDA correcta.

Verificar versión de CUDA instalada:
```powershell
nvidia-smi
```
Buscar "CUDA Version" en la esquina superior derecha de la salida (ej. `12.8`).

Instalar con la versión correspondiente (ejemplo para CUDA 12.8):
```powershell
& "E:\Transcriptor\venv-whisperx\Scripts\pip.exe" install --force-reinstall torch torchaudio --index-url https://download.pytorch.org/whl/cu128
& "E:\Transcriptor\venv-whisperx\Scripts\pip.exe" install --force-reinstall "torchvision==0.26.0+cu128" --index-url https://download.pytorch.org/whl/cu128
```

> Si tu CUDA es diferente (ej. 12.1 o 12.4), reemplaza `cu128` por `cu121` o `cu124` en las URLs.

Ignorar los warnings de `pip's dependency resolver` — son esperados y no afectan el funcionamiento.

### 8e — Obtener token de Hugging Face

1. Crear cuenta en huggingface.co
2. Ir a huggingface.co/settings/tokens → New token (tipo: **Read**)
3. Aceptar términos en **dos** modelos (ambos obligatorios):
   - huggingface.co/pyannote/speaker-diarization-community-1
   - huggingface.co/pyannote/speaker-diarization-3.1
4. Guardar el token — se usa con `--hf_token TU_TOKEN` al transcribir

> **Seguridad:** El token `hf_...` nunca debe pegarse en el chat de Claude. Pasarlo siempre directo al comando en la terminal o guardarlo en una variable de entorno.

### 8f — Verificar

```powershell
& "E:\Transcriptor\venv-whisperx\Scripts\whisperx.exe" --help
```

Si retorna el menú de ayuda: whisperx listo.
