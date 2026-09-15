# Ejecución — los dos caminos

Hay **dos formas de trabajar**. Elige según cómo llegó el pedido; si no es obvio, pregunta.

**A · En la página** (`page/columna-es.html`, publicada como Artifact). El usuario pega
la columna inglesa ahí y la página traduce sola, con las reglas de esta skill incrustadas
en su prompt. Es el camino normal para un lote grande. Tu papel es pasarle el link y
quedarte disponible para las consultas que salgan.

**B · En la conversación.** El usuario pega el texto aquí y traduces tú, con los 4 pasos
de abajo. Conviene cuando el lote es corto, cuando hace falta discutir decisiones línea
por línea, o cuando el contexto de la escena es enredado.

Los dos terminan igual: un `trabajo.json` que la página puede importar y que el validador
de escritorio puede auditar.

---

## Paso 1 — Recopilar el lote

Pide en un solo bloque lo que falte. Si el usuario ya pegó el texto o dio una ruta,
**no preguntes nada más** y salta al Paso 2.

```
Texto fuente:   pegado aquí, o ruta a un CSV/TSV exportado de la hoja
Proyecto:       nombre del juego o del lote (para la carpeta de salida)
Columna:        cuál columna te asignaron (si aplica)
Contexto:       quién habla, tono del juego, glosario previo si existe
```

**Si el usuario no da contexto, no lo inventes** — tradúcelo igual y anota en el bloque C
las líneas cuyo sentido depende de contexto que no tienes.

Lee `docs/guidelines-cliente.md`, `docs/estilo-es-latino.md` y
`docs/adaptacion-creativa.md` antes de traducir.

---

## Paso 2 — Traducir

Sigue `workflows/traducir.md`. Construye el `trabajo.json`, traduce fila por fila, y
produce tres bloques:

**A · Columna traducida** — las filas en orden, 1:1 con el original. Este es el
entregable que se pega en la hoja.

**B · Consultas para anna** — nombres propios dudosos, errores detectados en el texto
original (**no los corrijas en la traducción**, repórtalos), y líneas ambiguas por falta
de contexto. Si este bloque está vacío, dilo explícitamente.

**C · Adaptaciones creativas** — chistes, rimas, modismos, muletillas de personaje o
nombres que cambiaste para que funcionen en español. Cada uno en tres partes: **qué
había**, **qué pusiste**, **qué se habría perdido sin el cambio**. La cliente pide
libertad creativa **y** que se le avise: sin este bloque, la libertad se vuelve un
cambio silencioso.

Si el lote tiene diálogo o humor y este bloque quedó vacío, revísalo antes de entregar —
cero adaptaciones suele significar que se tradujo pegado al inglés.

---

## Paso 3 — Compuerta de QA (obligatoria, antes de entregar)

Sigue `workflows/qa.md`. Corre el validador y **pega su salida real** en la respuesta:

```powershell
python scripts\qa_localizacion.py <ruta-al-json>
```

- **ERROR** → corrígelo y vuelve a correr. No entregues con errores abiertos.
- **AVISO** → decide caso por caso y explica la decisión. Un aviso descartado se
  menciona, no se oculta.

No declares el lote listo sin haber mostrado la salida del script. "Revisé y está bien"
no es la evidencia; la tabla del validador sí.

---

## Paso 4 — Entrega

El terminal no sirve para revisar 200 filas ni para pegar sin equivocarse. Pásale el lote
a la página: **Importar trabajo.json** en `page/columna-es.html`. Ahí quedan los pares
EN/ES lado a lado, los flags en la fila que los disparó, la edición en línea y los
botones de copiado.

Escribe también `salida-es.txt` como respaldo local:

```powershell
python scripts\qa_localizacion.py <ruta-al-json> --salida <carpeta>\salida-es.txt
```

Cierra con:

| Entregable | Estado |
|---|---|
| Filas traducidas | N de N |
| QA determinístico | Sin errores / N errores |
| Consultas para anna | N (o ninguna) |
| Adaptaciones declaradas | N (o ninguna) |
| Página de revisión | URL |
| Respaldo local | ruta de `salida-es.txt` |

Recuérdale al usuario lo único que la skill no puede hacer por él: **pegar solo en su
columna asignada**, sin desplazar filas ni dejar líneas en blanco al final. Si la página
muestra el aviso de saltos de línea internos, esas filas se copian a mano.
