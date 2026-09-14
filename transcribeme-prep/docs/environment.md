# Notas de entorno

## Detección de unidad — no hardcodear

Este skill corre tanto en el escritorio (`E:` disponible) como en el portátil (sin `E:`, solo
`C:`/`D:`). Detectar la unidad de producción con `Test-Path E:\Transcriptor` primero; si no
existe, usar `D:\Transcriptor`. Si ninguna existe, crearla en el primer uso bajo `D:\Transcriptor`
(portátil) — nunca escribir output de producción en `C:` ni dentro de `.claude\`.

## Rutas de salida

- `<unidad>\Transcriptor\transcribeme\portfolio-samples\` — los `.docx` generados
- `<unidad>\Transcriptor\transcribeme\clean-verbatim-practice\` — los `.txt` de práctica (opcional, solo si el usuario pide guardar el intento)

Estas carpetas son nuevas y separadas de `<unidad>\Transcriptor\transcripciones\`
(la carpeta de SRTs de producción de `transcriptor` — nunca escribir ahí).

## Dependencia: python-docx

No viene instalado por defecto. Antes de correr `workflows/portfolio-sample.md`:

```powershell
pip show python-docx
```

Si no está instalado:

```powershell
python -m pip install --user python-docx
```

Reportar este comando al usuario antes de correrlo (instala un paquete nuevo). No se necesita un
venv dedicado — a diferencia de WhisperX (cuya aislación existe por fragilidad de versiones de
CUDA/torch), `python-docx` es una librería liviana sin conflictos de versión conocidos en este
entorno.

## Integración con transcriptor

Este skill puede invocar `/transcriptor` para producir un SRT nuevo a partir de audio, pero lo
trata como caja negra — nunca lee ni modifica los archivos internos de esa skill. Ver
`transcriptor/docs/environment.md` para sus propias rutas (`<unidad>\Transcriptor\audios\`,
`<unidad>\Transcriptor\transcripciones\`).
