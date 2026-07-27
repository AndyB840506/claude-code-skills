# Workflow 01 — Transcripción (headless)

Invoca la skill `/transcriptor` en modo pipeline — pasa el `audio_path` directamente,
sin hacer preguntas al usuario. Los parámetros están fijos: large-v2, español, diarización, SRT.

---

## Ejecución

1. Toma `audio_path` del episode brief — ya viene auto-descubierto y confirmado por
   el usuario en `00-intake.md` (carpeta fija por show + match por número de episodio),
   no es necesario volver a preguntarlo ni validarlo aquí.
2. Si el archivo no está ya en `E:\Transcriptor\audios\`, cópialo ahí primero —
   usa PowerShell `Copy-Item`, nunca `xcopy`.
3. Invoca la skill con la ruta del audio:
   ```
   /transcriptor <audio_path>
   ```
   La skill corre en modo silencioso (sin preguntas interactivas) y devuelve el path del SRT.
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

## Si el audio cambia después de transcribir

Puede pasar que Andy reexporte el audio ya transcrito (ej. arregló un bug de timing en la
música de intro/outro que corrió todos los números) — confirmado en BTQ EP.020. Señales:
mismo `audio_path` pero tamaño de archivo distinto, o el usuario dice explícitamente que
hubo que re-grabar/re-exportar algo.

1. Sobrescribe el audio en `E:\Transcriptor\audios\` con `Copy-Item -Force` y respalda el
   SRT viejo (`[nombre] (pre-fix backup).srt`) antes de que WhisperX lo sobrescriba.
2. Repite la ejecución completa del Paso 3 sobre el archivo nuevo.
3. Si ya se habían generado capítulos de YouTube o quote cards con timestamps del SRT
   viejo (Stage 2), **no los descartes ni los regeneres desde cero** — solo recalcula los
   timestamps contra el SRT nuevo. El contenido/copy no cambia, solo dónde ancla cada cita.
4. Anota el re-run en la bitácora como sub-paso (ej. "Stage 1b — Re-transcripción") en vez
   de sobreescribir la entrada original de Stage 1.

## Si algo falla

Si `transcriptor` no está instalado o whisperx no está disponible, NO intentes
instalarlo a mitad de pipeline sin avisar — reporta el bloqueo al usuario y pregunta si
quiere que lo configures ahora (`transcriptor/workflows/00-setup.md`) o que continúes el
pipeline saltando este stage (usando un script/transcript que el usuario ya tenga).
