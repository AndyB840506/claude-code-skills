# Reglas de Clean Verbatim — examen de ingreso TranscribeMe

Cada regla lleva su fuente. Las marcadas **[oficial]** vienen del blog de transcribeme.com
(verificado 2026-09-14). Las marcadas **[terceros]** vienen de una guía externa
(gotranscript.com) sobre el examen de ingreso, no de TranscribeMe directamente — tratar como
probable, no como hecho confirmado al 100%. Antes de tomar el examen real, confirmar estas reglas
contra la guía de estilo de 23 diapositivas que TranscribeMe entrega en el propio proceso de
aplicación.

## Estilos de TranscribeMe [oficial]

- **Full Verbatim:** captura el habla exactamente como se dijo, incluyendo repeticiones y errores.
- **Clean Verbatim:** quita muletillas ("hmm", "you know", "like") y corrige tartamudeos.
  Ejemplo oficial: "It was, like, you know, a pretty boring experience" → "It was a pretty boring
  experience."
- **Edited Verbatim:** texto preparado para publicación, con gramática y tiempos verbales
  corregidos.

El examen de ingreso prueba específicamente **Clean Verbatim** [terceros].

## Reglas aplicadas en este skill

1. **Quitar muletillas y discourse markers** [oficial, con ejemplos confirmados]: "um", "uh",
   "you know", "I mean", "like" (cuando es muletilla, no verbo/comparación real).
2. **Normalizar crutchwords a su forma formal** [terceros, 3 ejemplos confirmados]:
   - "kinda" → "kind of"
   - "gonna" → "going to"
   - "gotta" → "got to"
   Cualquier otra normalización más allá de estas tres (ej. "wanna" → "want to") se aplica por
   analogía y se marca inline como **inferida, no verificada** — no se presenta como regla
   confirmada de TranscribeMe.
3. **Sin speaker IDs ni timestamps** [terceros] — el examen no los pide.
4. **Nueva línea por cambio de speaker** [oficial, para el formato general de entregables] — un
   solo salto de línea (`\n`), no doble.
5. **Empieza en minúscula** [terceros] — salvo que la primera palabra sea siempre-mayúscula
   (nombre propio, "I").
6. **Termina sin puntuación** [terceros].

## Auto-chequeo antes de presentar como listo

Antes de mostrar el resultado, verificar (no asumir):
- grep de sobrevivientes literales: `um`, `uh`, `you know`, `kinda`, `gonna`, `gotta` → debe dar 0
- primer carácter del texto es minúscula (o se explica por qué no: nombre propio/pronombre)
- último carácter no es un signo de puntuación

Si algo falla, corregir y re-chequear — no presentar como terminado sin este paso.
