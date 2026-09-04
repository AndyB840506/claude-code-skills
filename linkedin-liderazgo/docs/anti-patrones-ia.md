# Anti-Patrones de IA — Checklist Verificable

Cada patrón sigue la forma condición → acción → verificación. Correr este checklist
contra CADA borrador antes de mostrarlo al usuario, y reportar el resultado en tabla.
No es opinión — cada fila se puede contar o comprobar releyendo el texto.

| # | Patrón (condición) | Acción si aparece | Verificación |
|---|---|---|---|
| 1 | La primera frase usa una apertura genérica ("En el mundo empresarial actual...", "En un mundo cada vez más...", "¿Alguna vez te has preguntado...", "Imagina un escenario donde...") | Reescribir el hook con una escena concreta, un número, o una cita textual — algo que solo pudo pasar una vez | Releer la primera línea; no debe calzar con ninguna de esas plantillas |
| 2 | Hay 3 o más guiones largos ("—") en todo el artículo | Reducir a máximo 1-2, reemplazando el resto por punto y seguido o coma | Contar ocurrencias literales de "—" en el texto final |
| 3 | Aparece la estructura "no es X, es Y" más de una vez | Dejar solo la instancia más fuerte; eliminar el resto | Contar ocurrencias del patrón "no es ... es ..." |
| 4 | El cierre usa "En conclusión", "En resumen", "Al final del día", "En definitiva" | Reescribir el cierre como una idea concreta, una pregunta a la audiencia, o una postura — sin la muletilla | Releer el último párrafo; no debe empezar con esas frases |
| 5 | Hay una lista de 2-3 adjetivos vacíos seguidos ("es dinámico, innovador y transformador") sin ejemplo que los sostenga | Sustituir por un hecho o ejemplo concreto que demuestre el adjetivo | Buscar cadenas de adjetivos sin sustantivo/ejemplo cerca |
| 6 | El artículo presenta "por un lado... por otro lado..." y termina sin tomar postura | Forzar una opinión clara del autor al final de ese bloque | Releer si el párrafo termina en una afirmación o en un empate |
| 7 | Aparece alguna palabra prohibida en `perfil-voz.md` (sección "Palabras que odio") | Reemplazar por lenguaje directo y específico | Grep de cada palabra prohibida contra el texto final |
| 8 | El artículo no menciona ningún dato concreto (cifra, nombre, fecha, lugar, empresa) | Agregar al menos un dato específico, real o explícitamente marcado como ejemplo hipotético | Releer el texto buscando al menos un número o nombre propio |
| 9 | Todas las oraciones tienen una longitud similar (ninguna menor a 8 palabras) | Cortar al menos una oración a menos de 6 palabras para variar el ritmo | Contar palabras de cada oración; debe haber al menos una corta |
| 10 | Hay 2 o más signos de interrogación en el primer párrafo — retóricas del autor O diálogo citado dentro de la escena | Reescribir a discurso indirecto o dejar máximo una, por defecto siempre, incluida la excepción de "es diálogo citado, no retórica del autor" — confirmado 2026-09-04: se dejó pasar como excepción razonada y el usuario pidió corregirlo igual | Contar signos de interrogación en el primer párrafo |

## Reporte esperado

Al terminar el checklist, mostrar una tabla así antes del artículo final:

| # | Patrón | ¿Apareció? | ¿Corregido? |
|---|---|---|---|
| 1 | Apertura genérica | No | — |
| 2 | Exceso de guiones largos | Sí (4) | Sí, reducido a 1 |
| ... | ... | ... | ... |

Si algún patrón aparece y NO se corrige, decirlo explícitamente y explicar por qué se
dejó así (ej.: el usuario pidió mantener esa frase).
