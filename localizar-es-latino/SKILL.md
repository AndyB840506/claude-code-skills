---
name: localizar-es-latino
description: "Traduce texto de juegos de inglés a español latino neutro siguiendo las guidelines de localización del cliente (anna_b.th): paridad de puntuación final, preservación de tags y placeholders (<i>, (GG), {var}), una fila por celda sin párrafos nuevos, reporte de errores del original en vez de corregirlos, y adaptación creativa declarada. Incluye un validador determinístico que corre antes de entregar. Triggers ES: traducir al español, localizar juego, traducción de strings, columna de español, localización EN-ES, traducir diálogos, revisar traducción, guidelines de anna. Triggers EN: translate to spanish, game localization, localize strings, latam spanish translation, translation QA, check my translation."
---

# Localizar EN → ES neutro (localización de juegos)

El texto viaja en columnas de una hoja compartida entre idiomas: **una fila corrida, un
párrafo extra o un tag perdido rompen el build de TODOS los idiomas**, no solo del
español. Por eso la skill separa dos cosas que suelen mezclarse — **la traducción**,
creativa y libre, y **el contrato**, mecánico y verificable.

Lo mecánico no se revisa a ojo: se corre `scripts/qa_localizacion.py` y se muestra su
salida antes de entregar. Un lote "se ve bien" no es evidencia de que las 200 filas cuadren.

## Las tres reglas que más se violan

1. **Español neutro — léxico neutro siempre, carácter regional nunca.** Ningún jugador
   debe poder ubicar de qué país es la traducción. La jerga local queda fuera venga del
   país que venga, y el mexicanismo es el que más se cuela porque el neutro se construye
   sobre base mexicana: `chingada madre` está tan mal como `gilipollas` o `boludo`.
   → `docs/estilo-es-latino.md`
2. **Fidelidad de registro.** Son juegos 18+ con lenguaje obsceno y sexo explícito: se
   traduce completo, con la misma intensidad, sin suavizar ni pasar a lenguaje clínico.
   Corre en las dos direcciones — una línea limpia se traduce limpia.
   → `docs/estilo-es-latino.md` §§ Groserías y Contenido adulto
3. **Libertad creativa, que no contradice la anterior.** Se conserva la *función* y la
   *intensidad*; las palabras son negociables. Un chiste literal que ya no da risa es una
   traducción fallida. Decide la **prueba del lector monolingüe**: el jugador nunca ve el
   inglés, así que la línea tiene que funcionar sola. → `docs/adaptacion-creativa.md`

## Reference

- `workflows/ejecucion.md` — los dos caminos de trabajo y los 4 pasos **(empieza aquí)**
- `workflows/traducir.md` — procedimiento de traducción por lote
- `workflows/qa.md` — la compuerta de validación y cómo leer su salida
- `docs/guidelines-cliente.md` — las reglas de anna_b.th, literales + interpretación operativa
- `docs/estilo-es-latino.md` — español neutro, groserías, contenido adulto, longitud
- `docs/adaptacion-creativa.md` — cuándo y cómo improvisar, qué no se toca, cómo declararlo
- `docs/ejemplo-lote.json` — lote de ejemplo con el esquema completo
- `scripts/qa_localizacion.py` — validador (segunda medición, independiente de la página)
- `page/columna-es.html` — la herramienta: pegar, traducir, revisar, copiar

## EXECUTION

Has invocado `/localizar-es-latino`. Sigue `workflows/ejecucion.md`: elige el camino
(la página para lotes grandes, la conversación para lotes cortos o contexto enredado) y
ejecuta sus 4 pasos — recopilar, traducir, compuerta de QA, entregar.
