# Transcribir — Flujo principal

---

## Paso 1 — Verificación rápida de Whisper

Antes de pedir el archivo, verificar que Whisper esté disponible:

```powershell
whisper --help
```

Si falla, informar al usuario y lanzar `00-setup.md`. No continuar hasta que el setup esté completo.

---

## Paso 2 — Obtener ruta del archivo

**Carpeta de entrada fija:** `E:\Transcriptor\audios\`

**Caso A — el usuario dio solo el nombre del archivo** (ej. `reunion.mp3`):
Construir la ruta completa automáticamente: `E:\Transcriptor\audios\reunion.mp3`. No preguntar nada.

**Caso B — el usuario dio la ruta completa:**
Usarla directamente tal como la proporcionó.

**Caso C — el usuario no especificó ningún archivo:**
Leer el contenido de la carpeta:

```powershell
Get-ChildItem "E:\Transcriptor\audios" -File | Select-Object Name, Length, LastWriteTime
```

- **Si hay exactamente 1 archivo:** usarlo directamente sin preguntar nada. Confirmar al usuario: `Usando: [nombre del archivo]`
- **Si hay más de 1 archivo:** listar y pedir elección:

```
Archivos en E:\Transcriptor\audios\:

  1. reunion.mp3        (45 MB)
  2. entrevista.m4a     (120 MB)

¿Cuál quieres transcribir? Escribe el número o el nombre.
```

- **Si la carpeta está vacía:**
```
No hay archivos en E:\Transcriptor\audios\
Copia tu archivo de audio ahí y vuelve a ejecutar /transcriptor
```

**Validar que el archivo exista** después de construir la ruta:

```powershell
Test-Path "E:\Transcriptor\audios\NOMBRE_ARCHIVO"
```

Si retorna `False` y la carpeta no existe: indicar que el setup no se ha corrido todavía (`/transcriptor setup`).

---

## Paso 3 — ¿Hay más de un interlocutor?

Preguntar una sola vez, brevemente:

```
¿El audio tiene más de un interlocutor? (entrevista, podcast con invitado, reunión, etc.)

  no (default) — Un solo hablante
  si           — Varios hablantes (se activará diarización)
```

**Si responde "no" o Enter:** continuar el flujo normal con Whisper.

**Si responde "si":** verificar si whisperx está disponible:

```powershell
$env:PYTHONUTF8 = "1"
& "E:\Transcriptor\venv-whisperx\Scripts\whisperx.exe" --help
```

- Si funciona: activar modo diarización (ver Paso 8 — variante whisperx).
- Si falla (`not recognized`): informar al usuario:

```
whisperx no está instalado. Para identificar interlocutores necesitas instalarlo.

¿Quieres instalarlo ahora? (requiere Python 3.12 y cuenta gratuita en huggingface.co)
  si — instalar whisperx (ver 00-setup.md Paso 8)
  no — continuar sin diarización
```

Si acepta instalar: ejecutar `00-setup.md` Paso 8 completo (pasos 8a–8f).

Después de instalar, pedir el token de Hugging Face:
```
Para la diarización necesitas un token gratuito de Hugging Face:

  1. Ve a huggingface.co → crea cuenta gratuita
  2. Entra a huggingface.co/settings/tokens → New token (tipo: Read)
  3. Acepta términos en: huggingface.co/pyannote/speaker-diarization-community-1
  4. Acepta términos en: huggingface.co/pyannote/speaker-diarization-3.1
  5. Copia el token (hf_...) y pégalo directamente en el comando de la terminal
     — nunca en el chat de Claude.
```

Guardar el token en memoria de sesión como `$hf_token` para usarlo en Paso 8.

---

## Paso 4 — Seleccionar idioma

Preguntar al usuario:

```
¿En qué idioma está el audio?

  auto (default) — Detección automática
  es             — Español
  en             — Inglés
  pt             — Portugués
  fr             — Francés
  de             — Alemán
  it             — Italiano
  ja             — Japonés
  zh             — Chino
  otro           — Escribe cualquier código ISO 639-1

Presiona Enter para detección automática, o escribe el código del idioma.
```

Si el usuario presiona Enter o no especifica: usar detección automática (no se pasa `--language`).

Si elige un idioma específico: agregar `--language CODIGO` al comando final. Ej: `--language es`

> Nota para uso freelance: forzar el idioma mejora la precisión y velocidad cuando el idioma es conocido.

---

## Paso 5 — Seleccionar modelo

**Si el modo es diarización (whisperx):** default recomendado es `large-v2`.
**Si el modo es un solo interlocutor (Whisper):** default recomendado es `medium`.

Preguntar al usuario (o usar el default según modo):

```
¿Qué modelo quieres usar?

  [default]  — medium (un interlocutor) / large-v2 (diarización)
  small      — Más rápido, buena precisión, ~30 seg por hora de audio
  medium     — Muy buena precisión, ~2-5 min por hora de audio
  large-v2   — Mejor precisión, recomendado para diarización

Presiona Enter para usar el default, o escribe el nombre del modelo.
```

Si el usuario presiona Enter o no especifica: usar el default según modo activo.

Referencia completa de modelos en `docs/modelos.md`.

---

## Paso 6 — Seleccionar formato de salida

Preguntar:

```
¿Formato de salida?

  srt (default) — Con timestamps cada 3-5 seg, texto organizado y fácil de leer
  vtt           — Para reproductores web
  all           — Genera todos los formatos a la vez

Presiona Enter para srt, o escribe: vtt / all
```

Si el usuario presiona Enter o no especifica: usar `srt`.

> `txt` no se ofrece — whisper genera una frase por línea en ese formato, el resultado queda fragmentado e ilegible.
> `srt` es siempre la opción correcta para leer o editar la transcripción.

---

## Paso 7 — Verificar carpeta de salida

**Carpeta de salida fija:** `E:\Transcriptor\transcripciones\`

Siempre usar esta carpeta como destino, independientemente de dónde esté el archivo de audio.

Verificar que exista antes de ejecutar:

```powershell
if (-not (Test-Path "E:\Transcriptor\transcripciones")) {
    New-Item -ItemType Directory -Force -Path "E:\Transcriptor\transcripciones"
}
```

---

## Paso 8 — Ejecutar transcripción

Informar al usuario antes de ejecutar:

```
Iniciando transcripción...
Archivo: [nombre del archivo]
Idioma: [auto-detect / código seleccionado]
Modelo: [modelo seleccionado]
Formato: [formato seleccionado]
Salida: E:\Transcriptor\transcripciones\

La primera vez que uses el modelo [X], se descargará automáticamente (~769 MB para medium).
Esto ocurre una sola vez.
```

Construir y ejecutar el comando. Siempre usar la ruta completa del ejecutable y `PYTHONUTF8=1` para evitar errores de encoding en Windows.

**Variante A — Un solo interlocutor (Whisper estándar):**

Con idioma específico:
```powershell
$env:PYTHONUTF8 = "1"
& "C:\Users\andre\AppData\Local\Python\pythoncore-3.14-64\Scripts\whisper.exe" "E:\Transcriptor\audios\ARCHIVO" --model MODELO --language CODIGO --output_format FORMATO --output_dir "E:\Transcriptor\transcripciones" --device cuda
```

Con detección automática:
```powershell
$env:PYTHONUTF8 = "1"
& "C:\Users\andre\AppData\Local\Python\pythoncore-3.14-64\Scripts\whisper.exe" "E:\Transcriptor\audios\ARCHIVO" --model MODELO --output_format FORMATO --output_dir "E:\Transcriptor\transcripciones" --device cuda
```

**Variante B — Múltiples interlocutores (WhisperX con diarización):**

Ejecutable: `E:\Transcriptor\venv-whisperx\Scripts\whisperx.exe` (venv Python 3.12 — NO usar el de Python 3.14)

> Modelo recomendado para diarización: **`large-v2`** (no `medium`). La mayor capacidad mejora significativamente la separación de hablantes.

Con idioma específico:
```powershell
$env:PYTHONUTF8 = "1"
& "E:\Transcriptor\venv-whisperx\Scripts\whisperx.exe" "E:\Transcriptor\audios\ARCHIVO" --model MODELO --language CODIGO --output_format FORMATO --output_dir "E:\Transcriptor\transcripciones" --diarize --hf_token TOKEN --device cuda
```

Con detección automática:
```powershell
$env:PYTHONUTF8 = "1"
& "E:\Transcriptor\venv-whisperx\Scripts\whisperx.exe" "E:\Transcriptor\audios\ARCHIVO" --model MODELO --output_format FORMATO --output_dir "E:\Transcriptor\transcripciones" --diarize --hf_token TOKEN --device cuda
```

La salida de whisperx incluye etiquetas como `[SPEAKER_00]`, `[SPEAKER_01]`, etc. Nombres reales no se asignan automáticamente — el usuario puede renombrarlos manualmente.

Ejemplos concretos:
```powershell
$env:PYTHONUTF8 = "1"
# Un interlocutor, español
& "C:\Users\andre\AppData\Local\Python\pythoncore-3.14-64\Scripts\whisper.exe" "E:\Transcriptor\audios\reunion.mp3" --model medium --language es --output_format srt --output_dir "E:\Transcriptor\transcripciones" --device cuda

# Múltiples interlocutores, español
& "E:\Transcriptor\venv-whisperx\Scripts\whisperx.exe" "E:\Transcriptor\audios\entrevista.mp3" --model large-v2 --language es --output_format srt --output_dir "E:\Transcriptor\transcripciones" --diarize --hf_token hf_xxxx --device cuda
```

---

## Paso 9 — Reportar resultado

Una vez completada la transcripción, mostrar:

```
✓ Transcripción completada

Archivo generado: E:\Transcriptor\transcripciones\[nombre].srt
Idioma detectado: [idioma que reportó Whisper]

¿Quieres abrir el archivo ahora?
```

Si el usuario dice sí, abrir con:
```powershell
Invoke-Item "E:\Transcriptor\transcripciones\NOMBRE_ARCHIVO"
```

---

## Manejo de errores comunes

| Error | Causa probable | Solución |
|-------|---------------|----------|
| `CUDA out of memory` | Modelo muy grande para la GPU | Cambiar a modelo `small` o `medium` |
| `ffmpeg not found` | ffmpeg no instalado | Lanzar `00-setup.md` Paso 5 |
| `No such file or directory` | Ruta incorrecta o archivo no movido a audios\ | Verificar que el archivo esté en `E:\Transcriptor\audios\` |
| Proceso muy lento | `--device cuda` no activo o CPU | Verificar que CUDA está disponible; reintentar con `--device cuda` |
| Texto en idioma incorrecto | Audio con mucho ruido o música | Especificar idioma explícitamente en Paso 3 |
| `whisperx not found` | whisperx no instalado o venv no creado | Ir a `00-setup.md` Paso 8 completo |
| `Torch not compiled with CUDA enabled` | PyTorch instalado en versión CPU en el venv | Re-correr 00-setup.md Paso 8d para reemplazar con versión cu128 |
| `GatedRepoError 403` | No se aceptaron los términos del modelo pyannote | Aceptar términos en huggingface.co/pyannote/speaker-diarization-community-1 |
| `SSLCertVerificationError` al descargar modelo | Avast bloqueando huggingface.co | Pausar Avast 10 min, volver a correr |
| `[SPEAKER_00]` solo un hablante | Audio sin pausas claras entre speakers | Normal — whisperx necesita pausas para separar hablantes |

---

## Anti-patrones

**No post-procesar output `txt`.**
Si el resultado en txt queda fragmentado (una frase por línea), no intentar limpiarlo con scripts. La solución correcta es re-correr whisper con `--output_format srt`. El SRT tiene los timestamps y el texto completo — no hay nada que limpiar.
