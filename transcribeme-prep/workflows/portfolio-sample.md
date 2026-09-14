# Muestra de portfolio (.docx)

## Paso 0 — Verificar python-docx

```powershell
pip show python-docx
```

Si no está instalado, avisar al usuario y correr:

```powershell
python -m pip install --user python-docx
```

## Paso 1 — Obtener el SRT

Según `SKILL.md` Paso 0: ruta directa, o invocar `/transcriptor` primero si hay audio y la
máquina lo tiene disponible. Confirmar que el archivo existe antes de seguir.

## Paso 2 — Detectar speakers y preguntar mapeo

```powershell
python "C:\Users\andre\.claude\skills\transcribeme-prep\scripts\srt_to_docx.py" "<RUTA_SRT>" --list-speakers
```

Mostrar al usuario el resultado (cuántos speakers, línea de ejemplo de cada uno) y preguntar:

> ¿Asigno `S1`/`S2` genérico, o pones nombres reales (ej. "Andrés", "Invitado")?

Esto es una decisión del usuario — no asumir. Si pide nombres reales, construir el argumento
`--speakers SPEAKER_00=Andrés,SPEAKER_01=Invitado` con el mapeo que confirme.

## Paso 3 — Determinar título y ruta de salida

Preguntar (o inferir del nombre del archivo SRT si es obvio, confirmando con el usuario) el
nombre del show/episodio para el encabezado del documento.

Ruta de salida — detectar unidad disponible (ver `docs/environment.md`):

```powershell
if (Test-Path "E:\Transcriptor") { $base = "E:\Transcriptor" } else { $base = "D:\Transcriptor" }
New-Item -ItemType Directory -Force -Path "$base\transcribeme\portfolio-samples" | Out-Null
```

## Paso 4 — Generar el .docx

```powershell
python "C:\Users\andre\.claude\skills\transcribeme-prep\scripts\srt_to_docx.py" "<RUTA_SRT>" "<RUTA_SALIDA>.docx" --title "<TITULO>" --speakers "SPEAKER_00=S1,SPEAKER_01=S2"
```

El script:
- Fusiona segmentos consecutivos del mismo speaker en turnos
- Inserta un marcador `[hh:mm:ss]` antes de un turno cuando pasaron ≥120s desde el último
  marcador emitido (siempre en el primer turno) — cubre a la vez las dos convenciones
  documentadas de TranscribeMe (cada ~2 min / en cambio de speaker) sin cortar un marcador a
  mitad de frase
- Da formato Calibri 11pt, con el label de speaker en negrita

## Paso 5 — Confirmar

Reportar la ruta completa del `.docx` generado al usuario. Sugerir abrirlo y revisar visualmente
antes de usarlo en la aplicación — el script no valida legibilidad ni corrige errores de
transcripción del SRT original.
