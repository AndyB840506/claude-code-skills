# Formato real de entregables de TranscribeMe [oficial]

Fuente: transcribeme.com/blog/transcription-formatting-and-editing-styles/ (verificado 2026-09-14).

## Estilos de contenido

- Full Verbatim / Clean Verbatim / Edited Verbatim — ver `clean-verbatim-rules.md` para el detalle
  de Clean Verbatim.

## Identificación de speakers

- Etiquetas `S1`, `S2`, `S3`, etc., o nombres personalizados cuando hay varios participantes.
  Este servicio está incluido en el precio — no es un extra.
- **No** usar las etiquetas crudas `SPEAKER_00`/`SPEAKER_01` que produce WhisperX/Pyannote — hay
  que remapearlas a `S1`/`S2` (o a nombres reales) antes de presentar cualquier muestra.

## Timestamps

- Intervalo por defecto: cada ~2 minutos, o en cada cambio de speaker.
- Intervalos personalizados disponibles según necesidad del cliente — no hay una regla más
  específica verificada sobre exactamente dónde cae el marcador dentro de un monólogo largo.
- **Decisión de diseño de este skill** (no viene de TranscribeMe, es la forma más simple de
  cumplir ambos criterios a la vez sin cortar un marcador a mitad de frase): emitir un marcador
  `[hh:mm:ss]` antes de un turno cuando pasaron ≥120s desde el último marcador emitido, siempre
  en el primer turno.

## Otros formatos que ofrecen (no relevantes para la muestra de portfolio salvo que se pida)

- **SRT:** formato especializado con timestamps precisos, para closed captioning.
- **NVivo:** para transcripciones de entrevistas analizadas en el software NVivo (investigación
  académica).
- **Market Research:** diferencia moderador de participantes de focus group; sin timestamps,
  incompatible con NVivo.
