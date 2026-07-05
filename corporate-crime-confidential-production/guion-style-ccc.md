# Corporate Crime Confidential — Guion Style Notes

## Calibración de duración — dimensionar en PALABRAS, no en minutos adivinados

**Ritmo real de Andy en CCC ≈ 137 palabras/min** (medido contra el SRT de Case File No. 001:
~3.104 palabras habladas / 22,7 min de audio, ver `pipeline-state-ep001.md`). Ese número
ya incluye pausas naturales — es ritmo de entrega, no de lectura en seco. Muy cercano al
ritmo medido de BTQ (~143 wpm, ver `btq-production/guion-style-btq.md`), así que la misma
fórmula aplica: `palabras ≈ minutos objetivo × 137`.

**Tabla de dimensionamiento (palabras habladas → minutos a 137 wpm):**

| Objetivo real | Palabras habladas |
|---|---|
| ~23 min | ~3.150 |
| ~30 min | ~4.100 |
| ~45 min | ~6.300 |

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
