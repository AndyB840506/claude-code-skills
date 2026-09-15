# Guidelines del cliente (anna_b.th) — reglas y su interpretación operativa

Fuente: brief de localización entregado por anna_b.th. Contacto para dudas: **anna.b_th**.

Cada regla aparece abajo como la escribió el cliente, seguida de lo que significa en
la práctica para esta skill. Donde la guideline es ambigua, se dice que es ambigua —
no se resuelve en silencio.

---

## 1. Solo escribir en la columna asignada

> "Only write in the column that was assigned to you."
> "Do not swap columns under any circumstances. Otherwise the other languages will break when we build it."

**Operativo:** la skill nunca produce una hoja completa ni toca otras columnas.
Produce **una sola columna**, en orden, con exactamente la misma cantidad de filas
que el original. El paso de pegado lo hace la persona.

**Por qué importa más de lo que parece:** una fila de más o de menos no rompe el
español — corre todas las filas siguientes de **todos** los idiomas. Es el error
más caro del lote y el más fácil de cometer.

---

## 2. Nombres propios

> "Pay attention to the names. If you have problems with translating names or you doubt about it, it's better to contact me (anna.b_th)."

**Operativo:** ante un nombre propio dudoso, **no elegir en silencio**. Va al bloque
de Consultas con: el nombre, por qué hay duda, y 1–2 opciones propuestas.

Casos típicos que generan duda y deben consultarse:
- Nombres que son también un juego de palabras o un chiste.
- Nombres con connotación distinta o impronunciable en español.
- Nombres que ya aparecieron traducidos en otro lote (riesgo de inconsistencia).
- Apodos con carga de registro (cariñoso, despectivo) que no sobrevive literal.

Si el nombre es neutro y no hay duda real, se deja **tal cual, sin traducir**.

---

## 3. Paridad de puntuación final

> "Pay attention to dots in the end of each sentence: if the ENG version has it, so do other languages. If the ENG ver does not have it, so don't other languages."

**Operativo:** el último carácter de puntuación del español **espeja el del inglés**.
Si el inglés termina en `.`, el español también. Si el inglés no lleva punto final,
el español tampoco. Igual con `!`, `?`, `...`, `…` y con la ausencia de todo.

**Verificado por el script** (check `puntuación final`).

### El caso de `¿` y `¡` — leer con cuidado

El español abre signos que el inglés no tiene. Los propios ejemplos del cliente
muestran cómo se resuelve:

```
<i>God fucking damn it, how much more...</i>
<i>Maldita sea, ¿cuánto más...</i>
```

El inglés no lleva `?` final → el español **tampoco lo cierra**, pero sí abre `¿`
porque la frase es interrogativa. Queda un `¿` sin cerrar. Es lo que el cliente
escribió en su propio ejemplo, así que es la convención de este proyecto.

```
(GG), hey!
(GG), ¡eh!
```

Aquí el inglés sí termina en `!` → el español cierra `!` y además abre `¡`.

**Regla:** abrir `¿`/`¡` cuando la frase lo pide en español; cerrar **solo si el
inglés cierra**. El script marca los signos sin cerrar como **AVISO**, no como
error, justamente porque en este proyecto son esperables.

**Ambigüedad reconocida:** dejar `¿` sin cerrar no es ortografía estándar de la RAE.
La convención del cliente manda, pero si el lote es grande vale una línea a anna
confirmándolo una sola vez.

---

## 4. Sintaxis, tags y placeholders

> "Pay attention to syntax!"

Los ejemplos del cliente muestran dos cosas que se preservan intactas:

| Elemento | Ejemplo | Regla |
|---|---|---|
| Tags de formato | `<i>...</i>` | Mismos tags, misma cantidad, mismo orden, envolviendo el texto equivalente |
| Placeholders | `(GG)` | Se copian **literales**, nunca se traducen ni se reordenan sin necesidad |

También aplica a `{variable}`, `[TOKEN]`, `%s`, `%d`, `$VAR` si aparecen.

**Verificado por el script** (checks `tags` y `placeholders`).

**No copiar la tipografía francesa.** En el ejemplo del cliente el francés escribe
`hé !` con espacio antes del `!` — eso es norma francesa. En español **no se pone
espacio antes de `!` o `?`**. El script marca ese espacio como error.

---

## 5. Sin párrafos nuevos, sin espacios sobrantes

> "Do not leave empty paragraphs or spaces after the text. The program reads them as separate text and then does not output the rest."
> "Do not create separate paragraphs unless specified in the text! Otherwise, all subsequent text will be lost when transferred to the engine."

**Operativo, y es la regla más destructiva de la lista:**
- Cero espacios al inicio o al final de cada celda.
- Cero filas vacías al final del bloque.
- Un salto de línea interno solo si el inglés lo tiene, y **la misma cantidad**.
- Nunca partir una frase larga en dos párrafos "para que se lea mejor".

**Verificado por el script** (checks `espacios`, `vacíos`, `saltos de línea`).

---

## 6. Errores en el texto original — reportar, no corregir

> "About mistakes in original text: it is better not to correct them, but write to me, because they will not be transferred automatically from the table. They will have to be corrected separately in the code."

**Operativo:** si el inglés tiene un typo, un tag mal cerrado o una incoherencia,
**la traducción se hace sobre la intención correcta** (no se replica el typo en
español), pero el hallazgo va al bloque de Consultas con número de fila y texto
exacto. Corregir la celda inglesa está fuera del alcance: esa fila vive en el código.

---

## 7. Libertad creativa — con aviso

> "Do not be afraid to change the jokes/phrases/poems/names to your liking, if this way it sounds better in your language, just make sure to notify me."
> "The more creative, the better!"

**Operativo:** la adaptación no es una concesión que la cliente tolera — es lo que
pide. La literalidad torpe es el error por defecto: un chiste que no da risa traducido
literal es un chiste roto, aunque cada palabra esté "bien".

Lo que se conserva siempre es **la función y la intensidad** de la línea; las palabras
concretas son negociables. Método completo, categorías que casi siempre hay que
adaptar (chistes, modismos, rimas, muletillas, acentos) y lo que **no** se puede tocar
por creativo que sea: **`adaptacion-creativa.md`**.

Pero **toda adaptación se declara** en el bloque C. La diferencia entre libertad
creativa y cambio silencioso es exactamente ese bloque.

**Excepción — los nombres se proponen, no se aplican.** La regla 2 pide consultarlos
y esta autoriza cambiarlos; no se contradicen. Un nombre reaparece en todo el juego y
en todos los idiomas, así que la decisión unilateral en un lote es un problema en el
siguiente. Va al bloque de Consultas con opciones, y mientras tanto se deja el
original.

---

## 8. Deadlines y accesos

> "DEADLINES are set for us to release the game in time... If you understand you can't make it in time, please contact me!"
> "If you need access to files, don't send a request! It comes to the mail not to me, accordingly, it is better to just write."

**Operativo:** fuera del alcance de la skill, pero si el usuario menciona que va
corto de tiempo o que no puede abrir un archivo, recordarle que la vía es
**escribirle directo a anna.b_th**, no el botón de "solicitar acceso" de Drive.
