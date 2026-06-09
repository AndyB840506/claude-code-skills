# Workflow 01 — Transcripción (headless)

Invoca `transcriptor/workflows/01-transcribir.md` pero **sin hacer sus 4 preguntas** —
todas las respuestas salen del episode brief y de las reglas globales del usuario.

---

## Respuestas pre-cargadas (no preguntar nada de esto)

| Pregunta de `transcriptor` | Respuesta pre-cargada | Por qué |
|---|---|---|
| ¿Uno o varios hablantes? | **Varios — activar diarización (whisperx)** | Ambos shows (`speakers: multi` en el brief) son co-host |
| ¿Idioma? | **es** | `language: es` en el brief |
| ¿Tamaño de modelo? | **large-v2** | La diarización lo requiere |
| ¿Formato de salida? | **srt** | Regla global del usuario — nunca generar txt (ver `feedback_transcripcion` / sección Transcription del CLAUDE.md global) |

---

## Ejecución

1. Toma `audio_path` del episode brief — ya viene auto-descubierto y confirmado por
   el usuario en `00-intake.md` (carpeta fija por show + match por número de episodio),
   no es necesario volver a preguntarlo ni validarlo aquí.
2. Si el archivo no está ya en `E:\Transcriptor\audios\`, cópialo ahí primero (es la
   carpeta de entrada fija que `transcriptor` espera) — usa PowerShell `Copy-Item`,
   nunca `xcopy`.
3. Ejecuta la transcripción con los 4 parámetros de la tabla — sin preguntar nada de
   eso al usuario.
4. El resultado se guarda en `E:\Transcriptor\transcripciones\[nombre-audio].srt` con
   tags `[SPEAKER_00]`, `[SPEAKER_01]`, etc.

---

## Al terminar

1. Confirma en una línea: "Transcripción lista — SRT con diarización en
   [ruta]." y continúa directo a `02-assets.md`.
2. Agrega a la bitácora:
   ```
   ## Stage 1 — Transcripción
   - Qué se hizo: transcripción con diarización (large-v2, es, srt)
   - Archivos generados: [ruta al .srt]
   - Resultado: OK
   ```

## Si algo falla

Si `transcriptor` no está instalado o whisperx no está disponible, NO intentes
instalarlo a mitad de pipeline sin avisar — reporta el bloqueo al usuario y pregunta si
quiere que lo configures ahora (`transcriptor/workflows/00-setup.md`) o que continúes el
pipeline saltando este stage (usando un script/transcript que el usuario ya tenga).
