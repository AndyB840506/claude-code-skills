# Práctica de examen Clean Verbatim

## Paso 1 — Obtener texto fuente

- SRT existente: extraer texto plano ordenado por turno (sin timestamps ni speaker IDs en el
  resultado, pero sí usarlos internamente para saber dónde va cada salto de línea):
  ```powershell
  python "C:\Users\andre\.claude\skills\transcribeme-prep\scripts\srt_to_docx.py" "<RUTA_SRT>" --list-speakers
  ```
  (esto solo lista speakers; para extraer el texto plano, leer el SRT directamente y aplicar el
  mismo criterio de "nueva línea por cambio de speaker" al reescribir en el Paso 2 — no hace
  falta un script nuevo para esto, es parte de la reescritura de Claude)
- O texto/audio corto pegado directamente por el usuario — no requiere SRT en este modo.

## Paso 2 — Reescritura (la hace Claude en vivo, no un script)

Leer `docs/clean-verbatim-rules.md` y aplicar sobre el texto:

1. Quitar muletillas/discourse markers ("um", "uh", "you know", "I mean", "like" cuando es
   muletilla).
2. Normalizar los 3 crutchwords confirmados: kinda→kind of, gonna→going to, gotta→got to.
   Cualquier otra normalización se marca inline como "inferida, no verificada".
3. Quitar speaker IDs y timestamps del resultado final.
4. Una línea por turno de speaker (un solo `\n`).
5. Empezar en minúscula (salvo nombre propio/pronombre).
6. Terminar sin puntuación.

## Paso 3 — Auto-chequeo verificable

Antes de presentar como listo, confirmar (no asumir):

- Buscar en el resultado: `um`, `uh`, `you know`, `kinda`, `gonna`, `gotta` → debe dar 0
  coincidencias literales
- Primer carácter en minúscula (o explicar la excepción)
- Último carácter no es signo de puntuación

Si algo falla, corregir y volver a chequear antes de mostrar el resultado.

## Paso 4 — Presentar y opcionalmente guardar

Mostrar el resultado en el chat — es material para practicar y criticar al momento, no un
entregable final. Si el usuario quiere guardarlo para comparar progreso entre intentos:

```powershell
if (Test-Path "E:\Transcriptor") { $base = "E:\Transcriptor" } else { $base = "D:\Transcriptor" }
New-Item -ItemType Directory -Force -Path "$base\transcribeme\clean-verbatim-practice" | Out-Null
```

Guardar como `<base>\transcribeme\clean-verbatim-practice\<fecha>-intento.txt`.
