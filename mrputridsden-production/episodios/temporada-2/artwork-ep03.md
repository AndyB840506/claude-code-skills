# Artwork EP.03 — "La Bestia que el rock volvió inmortal"

## Estado: PRODUCCIÓN FINAL COMPLETA (2026-08-15)

Escena base regenerada a 1536×1536 (mismo prompt/seed 3082026 del concepto aprobado, ver
abajo), upscaleada a 3000×3000 con RealESRGAN, `night_grade` variante E aplicado, compuesta
con `comfyui/templates/mpd-portada-ep03-t2.py` (título/tagline/footer) y
`mpd-quote-card-ep03-t2.py` (4 quotes verbatim del SRT real). Archivos finales:

- `E:\Podcast\MPD\Temporada 2\EP 03\artwork\MPD-T2E03-PORTADA-3000.jpg` (1:1, Spotify)
- `E:\Podcast\MPD\Temporada 2\EP 03\artwork\MPD-T2E03-16x9-FINAL.png`
- `E:\Podcast\MPD\Temporada 2\EP 03\artwork\MPD-T2E03-9x16-FINAL.png`
- `E:\Podcast\MPD\Temporada 2\EP 03\artwork\MPD-T2E03-Q1..Q4-1920x1080.png`

**Nota sobre la composición final vs. el concepto v3 de abajo:** al regenerar a 1536×1536
la composición salió simétrica (un vinilo a cada lado del marco, chimenea centrada) en vez
de la agrupación asimétrica de 3 vinilos de v3 — mismo concepto (estudio, marco ovalado,
retrato disuelto, vinilos reales, chimenea), composición distinta. Andrés vio ambas y
aprobó la nueva. Se intentó además replicar el mood de `MPD-T2E03-validation_00001_.png`
(v1, librero + candelabro) pero ese render tenía el patrón de diana vetado en el sleeve del
vinilo Y el rostro demasiado legible — 2 intentos de corregirlo sin perder el mood
fallaron (el rostro salía cada vez más nítido/reconocible), así que se descartó a favor de
la simétrica, que sí cumplía las reglas desde el primer intento.

**2 bugs reales encontrados y corregidos en el script de composición** (`mpd-portada-ep03-t2.py`,
copiado de `mpd-portada-ep02-t2.py`): (1) el wordmark quedaba superpuesto sobre el marco en
16:9 — el crop `y_center=0.55` heredado de EP02 no aplicaba a esta escena; corregido a
`y_center=0.30` tras probar 4 valores. (2) el título de EP.03 (38 caracteres, más largo que
el de EP02) se cortaba en 9:16 porque el piso del auto-fit de fuente (`0.030`) era muy alto
para que el texto llegara a caber; bajado a `0.018`. Ambos verificados visualmente
re-renderizando antes de dar por bueno — ver `pipeline-audit-ep03.md` Stage 3.

## Concepto aprobado (2026-08-14) — referencia histórica del prompt/seed usados

Aprobado por Andrés en la validación 1024×1024 + grading azul. El escalado a producción
(upscale 3000×3000 vía RealESRGAN, tipografía/lockup/footer con `mpd-portada-ep-t2.py`,
quote cards) queda para más cerca del lanzamiento del episodio — mismo patrón que EP.02
y EP.022 "Extra 2". No es bloqueante para cerrar Stage A.

## Concepto

El mismo estudio fijo "La Guarida" (chimenea encendida, butaca de cuero vacía, whisky
servido, puro apagado, mármol, paredes azul noche) con un elemento nuevo propio de este
expediente: un marco ovalado antiguo sobre la repisa con una fotografía sepia tan
deteriorada que el rostro se disolvió en una mancha ilegible — sin ojos, nariz ni boca,
solo la silueta del pelo y los hombros. Junto al marco, tres discos de vinilo reales
(surcos y etiqueta visibles, sin sleeve con arte impreso) — señalan "esto es rock" sin
imaginería ocultista.

**Por qué este concepto:** liga directo con la tesis del guion — su retrato ya está en
la sala sin que nadie lo haya colgado ahí a propósito (mismo hilo del Acto I: nadie dio
la cara por poner a Crowley en la portada de Sgt. Pepper's).

## Iteración (3 rondas, documentadas para no repetir los mismos errores)

1. **v1 — rechazada:** el sleeve de vinilo salió con un patrón de diana/círculos
   concéntricos (motivo vetado, colado disfrazado de arte de portada — mismo patrón que
   mordió en BTQ EP.022). El rostro del retrato quedó demasiado nítido y detallado.
2. **v2 — parcial:** el patrón de diana se corrigió (sleeve descrito como cartón liso sin
   gráfica, en vez de negar "no circles"), pero los vinilos dejaron de leerse como
   vinilos (quedaron como tarjetas/papeles en blanco) y apareció un segundo marco de
   sobra en la esquina superior.
3. **v3 — aprobada:** vinilos descritos explícitamente como discos reales (surcos, hoyo
   central, etiqueta) en vez de "sleeves lisos" — recuperó la lectura de "rock" sin
   reintroducir el patrón vetado (los surcos de un disco real son textura física
   esperable, no el motivo gráfico decorativo prohibido). Rostro descrito vía deterioro
   físico de la foto ("dissolved into a blank yellowed smear, no eyes/nose/mouth
   visible") en vez de negar iluminación — logró la ilegibilidad sin el efecto rebote de
   la trampa de negación.

## Prompt aprobado (Z-Image Turbo, positivo)

```
A Victorian-era study at night, book-lined walls, a single antique oval picture frame
alone on the wall above a lit fireplace, nothing else hangs on the wall. The fireplace
glows warm amber in one corner. An empty worn leather armchair faces away from the
camera toward the fire. A glass of whisky sits poured on a side table beside an
extinguished cigar. The oval frame holds an old photograph so faded, water-stained and
discolored by age that the sitter's face has dissolved into a blank yellowed smear, no
eyes, no nose, no mouth visible, just a vague dark silhouette shape of a head and
shoulders against blotchy sepia paper. On the mantelpiece beside the frame, three round
black vinyl records lean upright in a small wooden rack, their black circular edges and
center holes visible side-on, the paper sleeves behind them plain solid dark cardboard
with no printed artwork. Cold blue-grey shadows and midtones fill the room; warmth comes
only from the fireplace's glow catching the edge of the frame and the vinyl. Thin wisps
of smoke drift from the embers. Cinematic 35mm photograph, shallow depth of field, moody
atmospheric lighting, high detail, film grain. DO NOT render any concentric ring
pattern, target pattern, or halo pattern printed on any flat surface in this image.
```

Negativo (decorativo a cfg=1, ver `comfyui/docs/prompting.md`):
`deformed, disfigured, mutated, extra limbs, missing limbs, extra fingers, missing fingers, fused fingers, bad anatomy, bad proportions, warped body, blurry, lowres, watermark, signature`

Settings: Z-Image Turbo, seed 3082026, steps 9, cfg 1.0, sampler res_multistep, scheduler
simple, 1024×1024.

## Archivos (validación, no producción final)

- Escena base aprobada: `E:\AI\outputs\MPD-T2E03-validation-v3_00001_.png`
- Con grading azul variante E: `E:\AI\outputs\MPD-T2E03-validation-v3-graded.png`

## Al retomar para producción final

1. Re-generar a mayor resolución base (1536² como EP.02) o upscalear la v3 con
   RealESRGAN 4x → 3000×3000.
2. `night_grade` variante E (ya validado en este concepto).
3. Componer con un `mpd-portada-ep03-t2.py` nuevo (copiar de
   `mpd-portada-ep02-t2.py`, mismo patrón sin `draw_numeral`).
4. Título en una sola línea: "La Bestia que el rock volvió inmortal" — medir que quepa
   en `title_frac` antes de fijar tamaño de fuente (regla de EP.024 sobre títulos largos).
5. Quote cards: 4, verbatim contra el SRT real, después de grabar y transcribir.
