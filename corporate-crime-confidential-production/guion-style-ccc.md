# Corporate Crime Confidential — Guion Style Notes

## Calibración de duración — dimensionar en PALABRAS, no en minutos adivinados

**Estándar editorial de duración (BTQ y CCC, fijado 2026-07-06):** el episodio debe caer **entre 40
y 45 minutos de contenido hablado**, sin contar intro ni outro musical. No es un mínimo sugerido —
es el rango objetivo. Case File No. 001 quedó en ~23 min, muy por debajo del estándar (ver la
lección de abajo); no repetir ese patrón en episodios futuros.

**Ritmo real de Andy en CCC ≈ 137 palabras/min** (medido contra el SRT de Case File No. 001:
~3.104 palabras habladas / 22,7 min de audio, ver `pipeline-state-ep001.md`). Ese número
ya incluye pausas naturales — es ritmo de entrega, no de lectura en seco. Cercano al
ritmo medido de BTQ (**~150 wpm**, recalibrado 2026-07-06 — ver `btq-production/guion-style-btq.md`),
así que la misma fórmula aplica: `palabras ≈ minutos objetivo × 137`. Ojo: a diferencia de BTQ, esta
cifra de CCC viene de comparar palabras HABLADAS reales contra minutos de audio real — no aplica un
factor de expansión aparte porque no se comparó todavía contra el guion escrito de ese episodio;
recalibrar cuando haya más de un SRT de CCC disponible.

**Tabla de dimensionamiento (palabras habladas → minutos a 137 wpm):**

| Objetivo real | Palabras habladas |
|---|---|
| 40 min (piso del estándar) | ~5.480 |
| 42.5 min (centro del estándar) | ~5.825 |
| 45 min (techo del estándar) | ~6.165 |

**Lección de Case File No. 001 (2026-07-04):** el script de este episodio declaró en su
propio footer "~6.700 palabras" para un objetivo de 45 min — nunca se verificó
programáticamente. El conteo real, excluyendo `[marcadores de producción]`, headers y la
sección de fuentes, era de solo ~2.955-3.116 palabras — la mitad del target. Andy grabó
el guion palabra por palabra tal cual estaba escrito; el guion en sí estaba
sub-escrito, no la grabación mal hecha. Antes de dar un script de CCC por completo,
**contar las palabras reales del texto hablado y compararlas contra la tabla de arriba**
— no confiar en un conteo autoreportado en el propio archivo. Este chequeo ya está
encodeado como paso obligatorio en `podcast-creator/workflows/01-episodio.md` (Paso 4).

---

## Pase de fact-check [VERIFICAR] — orden y reglas (fijado 2026-07-07, EP002)

Los guiones CCC nacen con flags `[VERIFICAR: ...]` inline para todo dato no confirmado
contra fuente primaria. El pase que los resuelve tiene reglas:

1. **Correrlo ANTES de renderizar el HTML de producción y el Artifact.** En EP002 el
   render se hizo primero y las correcciones tocaron espejarse a mano en 3 archivos
   (~10 ediciones duplicadas). El .md es la fuente; el HTML es derivado — se construye
   cuando el texto ya está cerrado.
2. **Resolver = editar el texto, no anotar al margen.** El flag se elimina y el dato
   queda confirmado, corregido o suavizado en el guion mismo. No se graba con flags
   abiertos.
3. **Cifras de prensa sin fuente primaria se suavizan al piso verificado.** Precedente
   EP002: el "$16.3B" del Choice Act citado en prensa no se confirmó contra fuente
   primaria; la apropiación documentada era $15B → el guion dice "more than fifteen
   billion". Mejor un número defendible que uno citable.
4. **Loguear el pase en la sección Sources** del guion: fecha, cuántos flags se
   resolvieron, cuáles se corrigieron y por qué — con las fuentes nuevas agregadas a
   la lista. El pipeline-state del episodio refleja "fact-check completo".

---

## Atribución en quote cards — formato docu-drama, no narración directa

CCC no es un show de narración directa como BTQ/MPD (donde el host simplemente cuenta la
historia). El guion usa un **formato docu-drama**: personajes reales o compuestos hablan
en primera persona, reconstruyendo su lógica interna a partir de conducta documentada
(records judiciales, cargos de la SEC/OCC, testimonio) — no son transcripciones literales
de lo que esa persona dijo alguna vez.

Esto importa para quote cards y cualquier cita pública del show:

- **Cita real y verificable** (ej. algo que Stumpf de verdad dijo en una entrevista o
  audiencia del Congreso, marcado en el guion como cita directa con fuente citable):
  atribuir por nombre a la persona real — "— John Stumpf, Wells Fargo CEO".
- **Narración dramatizada en primera persona** (el monólogo interno reconstruido del
  personaje compuesto o de un ejecutivo nombrado, voceando su conducta documentada pero
  sin que esas palabras exactas estén registradas en ninguna parte): **NUNCA** atribuir a
  la persona real como si fuera una cita literal — eso presenta ficción como hecho.
  Atribuir en su lugar al show: "— Corporate Crime Confidential, Case File No. [NNN]".

Ver `quotecards-ep001.md` para el precedente aplicado (6 cards, 1 cita real atribuida por
nombre, 5 narración dramatizada atribuida al show). Aplicar la misma distinción en
cualquier episodio futuro de CCC antes de generar quote cards o compartir citas en redes.
