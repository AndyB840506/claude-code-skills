# Artwork EP.04 — "Paul is Dead"

## Estado: PRODUCCIÓN FINAL COMPLETA (2026-08-20)

Escena base generada a 1024×1024 (validación v4 aprobada por Andrés), upscaleada a
3000×3000 con RealESRGAN x4plus + `ImageScale` exacto, `night_grade` variante E
aplicado, compuesta con `comfyui/templates/mpd-portada-ep04-t2.py` (copiado de
`mpd-portada-ep03-t2.py`). Archivos finales:

- `E:\Podcast\MPD\Temporada 2\EP 04\artwork\MPD-T2E04-PORTADA-3000.jpg` (1:1, Spotify)
- `E:\Podcast\MPD\Temporada 2\EP 04\artwork\MPD-T2E04-16x9-FINAL.png`
- `E:\Podcast\MPD\Temporada 2\EP 04\artwork\MPD-T2E04-9x16-FINAL.png`

## Concepto final aprobado (v4, 2026-08-20)

El mismo estudio fijo "La Guarida" (chimenea encendida, butaca de cuero vacía,
mármol, paredes azul noche) con el marco ovalado sosteniendo una **página de
periódico envejecida, montada como pieza de museo** — nexo directo con el
artículo real de Fred LaBour en el *Michigan Daily* que dispara todo el guion.
Tres vinilos reales en la repisa (surcos y etiqueta visibles, sin arte impreso).

**Por qué este concepto (y no los descartados):** ver la iteración completa abajo.
El resumen: se necesitaba diferenciar de EP.03 (que usó un retrato en el mismo
marco) sin repetir el motivo "retrato/rostro" que ya falló dos veces en esa
temporada por razones de marca — así que el objeto central pasó a ser el
periódico, que además liga más directo con la tesis de este guion específico
(el artículo, no un rostro, es el origen real del mito).

## Iteración completa (4 rondas + 1 pedido rechazado, documentadas para no repetir errores)

1. **v1 — espejo antiguo empañado:** aprobado por Andrés en el primer intento
   (sin correcciones). Escalado a producción completa (3000×3000, 16:9, 9:16) y
   publicado brevemente. **Descartado después** por feedback de Andrés: se
   parecía demasiado a EP.03 a primera vista (mismo marco ovalado + vinilos +
   chimenea, aunque el contenido del marco fuera distinto).
2. **Pedido de Andrés — retrato de Paul McCartney en primer plano, mitad en
   sombra, sonriendo:** RECHAZADO. Regla del sistema (`mrputridsden/CLAUDE.md`,
   `comfyui/docs/prompting.md`): nunca rostros reconocibles en portadas — ni de
   personas reales ni genéricas. Razón reforzada en este caso: retratar a una
   persona real y viva en el material promocional de un episodio que trata
   justamente sobre cómo se fabrica evidencia falsa sobre ella es el riesgo que
   el episodio critica. Andrés pidió explícitamente hacer "override" de
   cualquier restricción escribiéndolo distinto en el prompt — se rechazó
   también esa vía: nombrar a la persona específica no reduce el riesgo, lo
   aumenta (más identificable, no menos). No se generó ninguna imagen para este
   pedido.
3. **v2 — foto genérica (no Paul), mitad iluminada/mitad dañada, con sonrisa
   parcial visible:** como alternativa intermedia, se ofreció una foto de época
   de un hombre genérico con solo la mitad inferior del rostro visible (comisura
   de sonrisa) y el resto disuelto en daño físico — misma técnica de
   degradación validada en EP.03. **Falló:** el modelo ignoró la instrucción de
   daño parcial y devolvió un rostro completo, nítido y totalmente reconocible
   (ojos, pelo, sonrisa completa). Mismo patrón de fallo ya documentado en
   EP.03 (2 intentos fallidos ahí también) — no se insistió por esta vía.
4. **v3 — periódico enmarcado, primer intento:** concepto nuevo sin ningún
   rostro. Buena diferenciación de EP.03, 3 vinilos visibles. **Problema
   menor:** el titular salió como pseudo-texto (letras que casi forman
   palabras: "AULICH DEERIICS") en vez de borrón limpio — la misma "trampa de
   la negación" documentada en `prompting.md`, aplicada a texto en vez de a un
   objeto.
5. **v4 — periódico enmarcado, segundo intento (ELEGIDO):** se reforzó la
   instrucción de desenfoque ("completely out of focus", "no legible
   letterforms", "washed out"). El pseudo-texto se redujo pero no desapareció
   del todo. A tamaño real de Spotify (150×150 px, verificado) es **completamente
   invisible** — se ve como un rectángulo pálido sin texto legible. A tamaño
   completo (3000px o el 16:9) el titular sigue siendo parcialmente
   pseudo-legible, pero no se consideró bloqueante dado que ningún formato de
   distribución se ve a esa resolución en el uso normal.

## Prompt final (Z-Image Turbo, positivo, v4)

```
A Victorian-era study at night, book-lined walls, a single antique oval picture
frame alone on the wall above a lit fireplace, nothing else hangs on the wall.
The fireplace glows warm amber in one corner. An empty worn leather armchair
faces away from the camera toward the fire. A glass of whisky sits poured on a
side table beside an extinguished cigar. The oval frame holds an old yellowed
newspaper front page mounted like a museum piece behind glass, badly faded with
age so the ink has bled and smeared into the paper, completely out of focus and
low contrast, no legible letterforms anywhere, no recognizable letters, no words
that can be read, just a soft hazy grey texture of vertical columns where the
ink has dissolved into an indistinct blur, the whole page washed out and pale,
suggesting the rhythm of text without ever resolving into readable characters.
On the mantelpiece beside the frame, three round black vinyl records lean
upright in a small wooden rack, their black circular edges and center holes
visible side-on, the paper sleeves behind them plain solid dark cardboard with
no printed artwork. Cold blue-grey shadows and midtones fill the room; warmth
comes only from the fireplace's glow catching the edge of the frame and the
vinyl. Thin wisps of smoke drift from the embers. Cinematic 35mm photograph,
shallow depth of field, moody atmospheric lighting, high detail, film grain. DO
NOT render any concentric ring pattern, target pattern, or halo pattern printed
on any flat surface in this image.
```

Negativo (decorativo a cfg=1): `deformed, disfigured, mutated, extra limbs, missing limbs, extra fingers, missing fingers, fused fingers, bad anatomy, bad proportions, warped body, blurry, lowres, watermark, signature`

Settings: Z-Image Turbo, seed 4202029, steps 9, cfg 1.0, sampler res_multistep,
scheduler simple, 1024×1024.

## Archivos

- Validación v4 (elegida) 1024 raw: `E:\AI\outputs\MPD-T2E04-validation-v4_00001_.png`
- Validación v4 con grading: `E:\AI\outputs\MPD-T2E04-validation-v4-graded.png`
- Base 3000×3000 pre-grading: `E:\AI\outputs\MPD-T2E04-portada-v4-3000_00001_.png`
- Base 3000×3000 con `night_grade` (usada en producción): `E:\AI\outputs\MPD-T2E04-escenario-v4-3000-graded.png`
- Descartados (referencia de la iteración, no usar): `MPD-T2E04-validation-v1*`, `MPD-T2E04-validation-v2*`, `MPD-T2E04-validation-v3*`, `MPD-T2E04-escenario_00001_.png` (regeneración 1536 fallida), `MPD-T2E04-escenario-3000-graded.png` (base del v1 descartado)

## Pendiente para el lanzamiento (Stage C, post-grabación)

Quote cards: no generadas todavía — requieren el SRT real post-grabación (mismo
patrón que EP.02/EP.03, 4 quotes verbatim).
