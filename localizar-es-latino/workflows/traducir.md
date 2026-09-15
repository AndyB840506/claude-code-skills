# Workflow — traducir un lote

## 1. Normalizar la entrada

El texto puede llegar de tres formas. En los tres casos el destino es el mismo: un
archivo de trabajo JSON.

| Llega como | Qué hacer |
|---|---|
| Texto pegado, una línea por string | Numerar las líneas en orden, tal cual |
| CSV/TSV exportado de la hoja | Leer con `Read`; identificar la columna inglesa por encabezado o por contenido |
| Ruta a un archivo | Igual que el anterior |

**No reordenar, no deduplicar, no saltar filas vacías.** Si el original trae una
celda vacía, en el JSON va como string vacío y en la salida va como línea vacía.
El orden y el conteo son el contrato.

Carpeta de trabajo: `C:\Users\andre\repos\localizacion\<proyecto>\` (crearla si no
existe). Si el usuario dio un archivo de entrada, usar la carpeta de ese archivo.

Archivo de trabajo `trabajo.json`. `consulta` y `adaptacion` son opcionales y se
llenan mientras traduces — de ahí salen los bloques B y C del entregable y las
secciones de la página de revisión:

```json
{
  "proyecto": "nombre-del-lote",
  "filas": [
    { "id": 1, "en": "<i>God fucking damn it, how much more...</i>", "es": "" },
    { "id": 2, "en": "(GG), hey!", "es": "" },
    {
      "id": 3,
      "en": "Frostbite.",
      "es": "Un escalofrío.",
      "adaptacion": { "tipo": "juego de palabras", "por_que": "..." }
    },
    {
      "id": 4,
      "en": "Mr. Pickles is waiting.",
      "es": "Mr. Pickles está esperando.",
      "consulta": "Nombre propio: ¿se traduce o se deja? ..."
    }
  ]
}
```

Lote de ejemplo completo y realista: `docs/ejemplo-lote.json`.

Escribirlo con la herramienta `Write` (no con `Set-Content`, que en PS 5.1 mete BOM
y rompe el parseo del JSON).

---

## 2. Traducir fila por fila

Leer antes: `docs/guidelines-cliente.md`, `docs/estilo-es-latino.md` y
`docs/adaptacion-creativa.md`.

Para cada fila, en este orden:

1. **Aislar tags y placeholders.** Identificar `<i>`, `</i>`, `(GG)`, `{var}`, `%s`.
   Esos fragmentos no se traducen: se reubican alrededor del texto equivalente.
2. **Preguntarse qué hace la línea** además de decir lo que dice: ¿chiste, rima,
   modismo, muletilla, caracterización, información de juego? Si la traducción literal
   conserva esa función, traducir directo. Si no, **cambiar el vehículo y conservar la
   función**, y anotarlo para el bloque C (`docs/adaptacion-creativa.md`).
   **Después de adaptar, aplicar la prueba del lector monolingüe:** tapando el inglés,
   ¿se entiende sola, cumple su función de verdad y suena a algo que alguien diría? Si
   falla, todavía no está lista.
3. **Traducir el contenido**, apuntando a registro y naturalidad, no a literalidad.
   Las groserías van con su equivalente de la misma intensidad — sin suavizar, sin
   omitir, sin asteriscos (`docs/estilo-es-latino.md` § Groserías). Y sin agregarlas
   donde el inglés no las tiene.
4. **Ajustar puntuación final** para que espeje exactamente la del inglés.
5. **Abrir `¿` / `¡`** si la frase en español lo pide (cerrar solo si el inglés cierra).
6. **Revisar el largo** si parece string de UI.
7. **Limpiar bordes:** sin espacio inicial ni final.

Si una fila no se puede traducir con confianza (falta contexto, nombre dudoso, error
en el original), **traducirla igual con la mejor opción** y anotarla para el bloque
correspondiente. Nunca dejar la celda vacía: una celda vacía rompe el build.

---

## 3. Acumular los dos bloques de reporte

Se escriben **dentro de `trabajo.json`**, en la fila que los origina — no en una lista
aparte. Así quedan anclados al número de fila y la página de revisión los agrupa sola.

**Consultas para anna** (campo `consulta`) — con número de fila:
```
Fila 14 · nombre propio "Mr. Pickles" — ¿se traduce o se deja? El chiste depende de
que "pickles" se entienda; propongo dejarlo o "Don Pepino".
Fila 31 · error en el original: "youre" sin apóstrofo. Traducido como "eres".
Fila 47 · sin contexto: "Fire!" puede ser "¡Fuego!" (disparar) o "¡Incendio!".
```

**Adaptaciones creativas** (campo `adaptacion`, con `tipo` y `por_que`) — el EN y el
ES ya están en la fila, así que `por_que` carga la tercera parte: qué se habría
perdido sin el cambio.
```
Fila 22 · rima
EN: "no pain, no gain"
ES: "sin dolor no hay honor"
Por qué: la gracia de la línea es la rima interna; la literal ("sin dolor no hay
ganancia") la pierde y queda como un consejo genérico.
```

Si alguno queda vacío, **decirlo explícitamente** ("Sin consultas para anna en este
lote"). Un bloque ausente se lee como olvido, no como ausencia de hallazgos.

---

## 4. Guardar y pasar a QA

Escribir las traducciones en `trabajo.json` y continuar con `workflows/qa.md`.
No presentar el lote al usuario antes de que el validador corra limpio.
