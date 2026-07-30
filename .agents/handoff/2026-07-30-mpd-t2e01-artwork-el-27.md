# Handoff: MPD T2·E1 — el artwork se rehízo entero (concepto «el 27»)

**Date:** 2026-07-30 (jueves)
**Machine:** desktop (E:\)
**Status:** Complete — los 7 archivos de artwork están listos. **El episodio publica mañana
viernes 2026-07-31** (verificado: el 31 cae viernes).

> Continúa `2026-07-28-mpd-t2e01-master-y-portada.md`. Lo que ese handoff daba por cerrado
> —la portada 1:1— se descartó hoy. El máster, el SRT, la metadata de texto y los capítulos
> siguen válidos y no se tocaron.

---

## Qué se hizo

### 1. Andrés ya subió y programó el episodio

Confirmado por él al abrir la sesión: **subido a Spotify y programado para el viernes 31.**
Eso ya no es un pendiente. Lo que sí queda: pegar la URL en la descripción y —si la portada
1:1 vieja ya viajó con la subida— re-subir la nueva.

### 2. La portada de cinco sillas se descartó, por dos defectos

Ambos los señaló Andrés; los dos se confirmaron midiendo, no discutiendo.

**a) Estaba fuera de la paleta de su propia marca.** Se compuso el 07-28 sin `night_grade`,
así que quedó en un casi-negro neutro mientras el resto del sistema vive en azul nocturno:

| Asset | sesgo azul B−R |
|---|---|
| Medianoche declarado `#0B1A39` | +46 |
| Fondo de la web `den-bg.jpg` | +36,7 |
| Portada de temporada T2 | +36,7 |
| **Portada del episodio (vieja)** | **+0,9** |

**b) Cinco sillas de cinco estilos distintos leen como un arrume de muebles, no como un club.**
Lo que hace deliberada una repetición es que los objetos sean *idénticos*; la variedad la hace
ver accidental. Y la silla vacía es iconografía de true-crime genérico, no de un show anclado
en rock.

### 3. Concepto nuevo: el «27» tipográfico

Escenario vacío con un haz de luz + el numeral compuesto con PIL en Bookman (relleno tenue +
contorno brasa). **El modelo nunca genera el número** — regla del kit: no genera texto que se
vaya a leer.

De tres tratamientos renderizados y mirados (sólido / contorno / ghost) ganó el **ghost**: el
contorno solo se desvanece en miniatura y el sólido tapa el haz.

**Los 7 archivos, en `E:\Podcast\MPD\Temporada 2\EP 01\artwork\` (máquina: desktop):**

| Pieza | Archivo | Peso |
|---|---|---|
| Portada 1:1 · 3000² | `MPD-T2E01-PORTADA-3000.jpg` | 695 KB |
| Portada 16:9 · 1920×1080 | `MPD-T2E01-16x9-FINAL.png` | 985 KB |
| Portada 9:16 · 1080×1920 | `MPD-T2E01-9x16-FINAL.png` | 1.152 KB |
| Q1 17:23 | `MPD-T2E01-Q1-1920x1080.png` | 591 KB |
| Q2 35:01 | `MPD-T2E01-Q2-1920x1080.png` | 843 KB |
| Q3 36:01 | `MPD-T2E01-Q3-1920x1080.png` | 473 KB |
| Q4 41:21 | `MPD-T2E01-Q4-1920x1080.png` | 954 KB |

La 1:1 anterior quedó respaldada como `MPD-T2E01-PORTADA-3000-PRE-GRADING-2026-07-28.jpg`.

**Verificado, no supuesto:** cero píxeles `#000000` en los siete; B−R de +38,8 a +48,3; bloque
de título mirado a 300 px y 150 px (la 1:1) y a 480×270 / 270×480 (las otras dos).

### 4. Dos compositores nuevos (commit `d28db30`)

- `comfyui/templates/mpd-portada-ep-t2.py` — los **tres** formatos del episodio desde un solo
  sitio. `mpd-lockup-t2.py` sigue siendo el de las piezas de TEMPORADA y no se tocó.
- `comfyui/templates/mpd-quote-card-t2.py` — cards 1920×1080 en La Guarida, con ajuste
  automático a N líneas (la Q3 tiene 128 caracteres y no cabe en las dos fijas del de T1).

Los de T1 (`mpd-portada-compose.py`, `mpd-quote-card-compose.py`) son Impact + crimson +
dorado: **no se usan en T2** y no se mutaron, se versionó al lado.

### 5. Retrospectiva y auditoría del kit aplicadas

Seis reglas nuevas escritas (ver § Notes) y dos referencias obsoletas corregidas: `roadmap-mpd.md`
seguía llamando «reusables» a los compositores de T1 (se conservó la frase porque *narra* lo del
07-17, con nota de retiro debajo) y `stack-reference.md` ganó la forma fuerte de la regla de
texto acentuado.

---

## Dónde pausamos

**Última acción:** cierre de sesión — retrospectiva y auditoría aplicadas.
**Siguiente acción:** plan de lanzamiento de T2·E1 (el episodio ya está programado).
**Bloqueantes:** ninguno para publicar.

---

## Archivos a leer primero

- `mrputridsden-production/episodios/ep006-metadata.md` — todo lo publicable, con el bloque de
  artwork reescrito hoy y las rutas de las 4 cards
- `comfyui/templates/mpd-portada-ep-t2.py` — si hay que retocar cualquiera de los tres formatos
- `comfyui/docs/artwork-composition.md` — tres reglas nuevas de hoy, incluida la de derivados

---

## Next Steps

**De Andrés — los tres cerrados el mismo 07-30, después de escribir este handoff:**
1. ~~Pegar la URL de Spotify~~ — hecha en los dos sitios. ⚠️ **Es la URL del SHOW**
   (`open.spotify.com/show/0M12ujB9eJqr0dWZUwEf6B`), no la del episodio. Queda alineada con
   los links de Apple y Amazon del mismo bloque, que también son de show, pero EP.005 usó el
   deep link del episodio, que solo existe una vez publicado. **Si se quiere ese formato,
   cambiarla el viernes 31.**
2. ~~Re-subir la portada 1:1~~ — **ya subida** la del «27», y el episodio sigue programado
   para el viernes 31. Confirmado por Andrés.
3. ~~Apagar ComfyUI~~ — cerrado (PID 26336); verificado que el puerto 8188 dejó de responder.

**De producción:**
4. **Plan de lanzamiento de T2·E1.** Es lo único del episodio que falta. Las 4 cards ya están
   renderizadas y sus textos son verbatim del SRT del máster, así que la quote del Día 2 no
   necesita re-confirmarse contra el audio.
5. **Limpiar `BTQ Template.rpp`**: carga una grabación vieja de EP.023. Viene del handoff del
   07-28, no se tocó por ser otro show.

**Decisiones abiertas:**
6. **El haz de luz quedó frío.** `night_grade` reserva el cálido para lo que pasa de 152 de
   luminancia y el núcleo del haz queda debajo, así que el único elemento cálido de la pieza es
   la tipografía brasa. Es consistente con «un solo acento cálido», pero si se quiere el haz
   ambarino hay que bajar el `PIVOT` — **parámetro congelado del sistema**, no se toca sin
   decisión explícita.
7. **Español neutro en MPD** — decidido 2026-07-25, aplazado a la semana del **2026-08-03**.
   Marcador vivo en `guion-style-mpd.md` línea ~10. Al retomarlo, leer la sección de BTQ y
   **adaptarla, no copiarla**.
8. «Martes de misterio», episodio de leyendas venezolanas, ofrecimiento de ayuda con la edición
   — los tres siguen sin decidir, vienen de antes.

**Marcador muerto, NO revivir:** `pipeline-state-ep004.md` línea 14 pide regenerar Q4+T2 de
EP.004 en Flow. Es de la era co-host, **clausurada** (ver memoria `project_mpd_juan_departure`).
No es un pendiente, es archivo.

---

## Notes / Gotchas

- **La herramienta de lectura de imágenes cachea por ruta.** Tras regenerar un PNG y releer la
  misma ruta, devolvió la versión ANTERIOR — estuve a un paso de reportar que el fix no había
  entrado. Para verificar un cambio: medir el archivo con PIL, o escribir la prueba con nombre
  nuevo. Regla escrita en el `CLAUDE.md` del proyecto.
- **Un derivado hereda los defectos del original, incluidos los que nadie buscó.** El 16:9 y el
  9:16 salieron de una 1:1 «aprobada» que estaba fuera de paleta, y el defecto se multiplicó por
  tres antes de que Andrés lo viera. Aprobación humana a tamaño completo ≠ verificación contra el
  sistema. Regla en `artwork-composition.md`.
- **La paleta también se mide en el sentido contrario.** Ya existía la regla de muestrear la
  paleta *del* artwork; faltaba la de medir el artwork *contra* la paleta. Instrumento: parche sin
  tipografía + sesgo de canal contra el hex declarado **y** contra un asset vivo.
- **De las tres semillas del escenario se eligió 4127 sobre 9219.** La 9219 es más cinematográfica
  pero su charco de luz **cierra en óvalo** dentro del cuadro; el de 4127 se sale por los dos
  bordes y no llega a leerse como forma circular, que es lo que el veto de aros/dianas prohíbe.
  La 9219 queda en `E:\AI\outputs\MPD-T2E01-escenario-s9219_00001_.png` por si se prefiere.
- **Reprocesos por procedencia hoy: 1.** El azul. La metadata del episodio decía literalmente
  «ver `rebrand/identidad-la-guarida.html`» y leí esa línea como restricción sin abrir el archivo
  ni medir el asset contra él. El dato estaba en tres sitios y lo destapó Andrés.

---

## Questions to Answer

- ~~¿La portada 1:1 vieja alcanzó a subirse?~~ **Resuelto el 07-30:** Andrés subió la nueva y
  el episodio sigue programado.
- ¿Se cambia la URL del show por el deep link del episodio cuando publique el viernes 31?
- ¿Se deja el haz frío o se decide bajar el `PIVOT` de `night_grade` para T2 entera? (Si se baja,
  afecta a todas las piezas del sistema, no solo a este episodio.)
- ¿Las dos imprecisiones del audio (12:48 «menos de un año», 15:56 «21.700») quedan definitivas?
  Vienen del handoff del 07-28; ese día la decisión fue dejarlas.
