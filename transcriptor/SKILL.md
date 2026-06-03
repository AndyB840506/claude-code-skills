---
name: transcriptor
description: "Transcribe audio a texto usando Whisper local (offline, gratis, sin límite de duración). Ideal para audios de más de 30 minutos. Soporta múltiples idiomas: español, inglés, portugués, francés, alemán, italiano, japonés, chino y más — o detección automática. Soporta MP3, MP4, M4A, WAV, OGG, FLAC, WEBM, MKV. Genera TXT, SRT, VTT o todos los formatos. Triggers: transcribir, transcriptor, transcripción, audio a texto, pasar audio a texto, convertir audio a texto, transcribe audio, audio to text, transcribe this, transcribir reunión, transcribir podcast, transcribir entrevista, transcribir clase, transcribir video, transcribir en español, transcribir en inglés, transcribe in english, transcribe in spanish."
---

# Transcriptor — Audio a texto con Whisper local

Convierte cualquier archivo de audio a texto sin límite de duración, sin costo, sin conexión a internet.

**Regla fundamental: Antes de transcribir, verificar que `whisper` esté instalado. Si no está, ejecutar `00-setup.md` primero.**

---

## Routing

| Si el usuario dice... | Ejecutar |
|---|---|
| "setup", "instalar", "dependencias", "primer uso", "install", "configurar", "no tengo whisper" | `workflows/00-setup.md` |
| ruta de audio, "transcribir [archivo]", "pasar a texto", cualquier otra solicitud | `workflows/01-transcribir.md` |

---

## Formatos soportados

`.mp3` · `.mp4` · `.m4a` · `.wav` · `.ogg` · `.flac` · `.webm` · `.mkv`

No se necesita conversión previa. Whisper usa ffmpeg internamente.

---

## Formatos de salida

| Opción | Descripción |
|--------|-------------|
| `srt` | Con timestamps cada 3-5 seg — **default recomendado** |
| `vtt` | WebVTT para reproductores web |
| `all` | Genera todos los formatos a la vez |

> `txt` no se ofrece — whisper genera una frase por línea, resultado ilegible.

---

## Modelos disponibles

Ver comparativa completa en `docs/modelos.md`. Default recomendado: **`medium`**.

---

## Flujo de uso

```
Primera vez → 00-setup.md → 01-transcribir.md
Usos posteriores → 01-transcribir.md directamente
```
