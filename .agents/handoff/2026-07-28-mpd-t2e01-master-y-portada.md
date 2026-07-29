# Handoff: MPD T2·E1 «El Club de los 27» — máster publicable, portada y la constante de wpm corregida

**Date:** 2026-07-28 (martes)
**Machine:** desktop (E:\)
**Status:** Complete — el episodio está listo para subir a Spotify y programar para el **viernes 2026-07-31**.

> **Cuarto handoff del 2026-07-28.** Los otros tres: dos de BTQ
> (`2026-07-28-btq-articulos-web-y-linkedin.md`) y el de la auditoría de reglas + reestructura del
> guion (`2026-07-28-mpd-auditoria-y-ep006.md`). **Este continúa ese último**: allí el episodio
> quedaba sin publicar porque Andrés iba a regrabar. Ya regrabó.

---

## Qué se hizo

### 1. El episodio quedó publicable

Andrés regrabó el 2026-07-28 a las 18:26. Sobre esa toma:

| | Antes | Entregado |
|---|---|---|
| Duración | 42:18,8 | **41:47,3** |
| Integrado | −18,3 LUFS | **−16,0 LUFS** ✅ |
| LRA | 6,6 | **6,5** ✅ |
| True peak | **+0,1 dBFS** (clipping) | **−1,2 dBFS** ✅ |
| Apertura | 57 s | **35,5 s** ✅ |

**Máster:** `E:\Podcast\MPD\Temporada 2\EP 01\MPD EP 01 MASTER.mp3` (máquina: desktop, `E:\`)
**SRT:** `E:\Transcriptor\transcripciones\MPD EP 01 MASTER.srt` (íd.)

La apertura se recortó editando el `.rpp` directamente: logo 13 s → 4,5 (traía **doble fade-in**,
el del archivo más 3,56 s de Reaper), música de intro 32,5 s → 18 con `SOFFS 12` para saltarse el
arranque casi vacío, y el outro movido a `SOFFS 41.5` porque `The_Locked_Porch` tiene **7 s de
silencio digital en el medio**. El outro NO se acortó: el brief pide ~20 s y los 18,8 ya cumplían
— el handoff anterior decía ~15 s y estaba mal.

El máster se hace **fuera de Reaper**, con `templates/masterizar-podcast.ps1`.

### 2. Se cortaron 7,9 s del episodio ya grabado

Se había leído al aire: *«Todas las cifras de este bloque quedaron confirmadas contra la cobertura
del estudio. No quedan estimados sin respaldo.»* Contabilidad de verificación, no narración.

**La causa no fue descuido de lectura.** La frase estaba correctamente clasificada dentro de un
bloque `class="dato"` — el guion la había etiquetado bien. El problema es que esos bloques se
renderizan **intercalados en el flujo de lectura**. Prueba de que es estructural: en el mismo
episodio se leyó al aire **otro** bloque `dato` completo (el de Alan Wilson, 76 palabras) sin que
nadie lo notara, porque ese sí sonaba a contenido. Regla nueva en `guion-style-mpd.md`.

### 3. La «constante» de 175 wpm era un artefacto del medidor

`wpm.py` contaba la etiqueta de diarización `[SPEAKER_00]:` como palabra hablada, porque pasa el
filtro de «contiene letras». Infla **3,6-8,6%** según cuántos segmentos tenga el archivo.

| | Antes | Real |
|---|---|---|
| BTQ (n=8) | 176,9 | **167,3** |
| MPD (n=5) | 174,7 | **168,2** |
| Global | ~175 «constante, no se re-negocia» | **167,6, rango ±6%** |

**Barrido cross-show hecho y limpio:** se reprodujo el método exacto de BTQ (palabras / habla
efectiva) con y sin etiquetas. Sin etiquetas da 146,0 · 152,0 · 140,3 · 147,3 contra los
147,4 · 153,4 · 142,5 · 148,6 publicados — diferencia constante de ~1,5. Con etiquetas se dispara
+4 a +9. **Los 148 wpm de BTQ se midieron bien; el bug era exclusivo de `wpm.py` de MPD.**

Segundo error encontrado en la misma guía: **la fórmula mezclaba instrumentos** — wpm derivado del
SRT dividido por una pausa de `silencedetect`. Predecía 45,2 min para un episodio de 41,8. Separada,
con la conversión documentada (~4,5 puntos entre las dos escalas).

### 4. Las 8 fechas del racimo: verificadas, todas correctas

Jones 3-jul-69 · Wilson 3-sep-70 · Hendrix 18-sep-70 · Joplin 4-oct-70 · Morrison 3-jul-71 ·
Winehouse 23-jul-11 · Johnson 16-ago-38. El estudio del BMJ cuadra **verbatim** en las seis cifras
citadas (Barnett, QUT, 1.046 músicos, 71 muertes, 7%, sin pico a los 27, 2-3× mortalidad en 20s-30s,
racimo 20-40 en los 70).

Cobain se dice como **«abril del 94» sin día**, lo que esquiva la discrepancia real (murió el 5, lo
encontraron el 8). Quedó bien.

### 5. Template de grabación

Andrés tenía ya un `MPD Template.rpp` guardado ese día a las 18:20 — **con los tres defectos**
(fade-in de 3,56 s, intro de 32,5 s, outro en `SOFFS 40`). Se reemplazó por el corregido, con los
bumpers movidos a carpeta estable y el anterior respaldado.

### 6. Metadata y portada

`episodios/ep006-metadata.md` — título, descripción plana y HTML, tags, **18 capítulos con
timestamps verificados contra el SRT final**, 4 textos de quote card verbatim del audio.

Portada 1:1 en `E:\Podcast\MPD\Temporada 2\EP 01\artwork\MPD-T2E01-PORTADA-3000.jpg` (desktop).

---

## Dónde pausamos

**Última acción:** cierre de sesión — retrospectiva aplicada y auditoría del kit corregida.
**Siguiente acción:** Andrés sube el episodio a Spotify y lo programa para el viernes 2026-07-31.
**Bloqueantes:** ninguno para publicar.

---

## Archivos a leer primero

- `mrputridsden-production/episodios/ep006-metadata.md` — todo lo que se pega en Spotify
- `mrputridsden-production/templates/README-grabacion-t2.md` — cómo grabar el próximo
- `mrputridsden-production/guion-style-mpd.md` — la constante corregida y las dos reglas nuevas

---

## Next Steps

**De Andrés:**
1. **Subir a Spotify y programar para el viernes 2026-07-31.** Al publicar, pegar la URL del
   episodio en la descripción de `ep006-metadata.md` (hoy dice PENDIENTE).
2. Subir la portada nueva de T2 al perfil del show en Spotify/Apple/Amazon (viene de antes).

**Pendiente de producción (no bloquea publicar):**
3. **Portada 16:9 y 9:16 + las 4 quote cards.** Los textos ya están listos y verbatim del audio.
   El concepto visual ya está resuelto (cinco sillas vacías), así que la segunda tanda debería
   ser rápida. **Máquina: desktop** — ComfyUI y los assets viven en `E:\`.
4. **Limpiar `BTQ Template.rpp`**: carga una grabación vieja de EP.023
   (`02-My Vocal-260725_1824.mp3` y su glued). Se detectó al comparar plantillas, no se tocó por
   ser otro show.

**Decisiones abiertas, vienen de antes:**
5. «Martes de misterio» — cadencia propuesta, sin decidir.
6. Episodio de leyendas venezolanas — contacto tibio, sin fecha.
7. Ofrecimiento de ayuda con la edición — en firme, sin usar.
8. **Español neutro en MPD** — decidido 2026-07-25, aplazado a la semana del **2026-08-03**. Al
   retomarlo, leer la sección de BTQ y **adaptarla, no copiarla**.

---

## Notes / Gotchas

- **Dos imprecisiones quedaron publicadas, por decisión de Andrés** (las considera menores y que
  pasan desapercibidas): en **12:48** dice «en menos de un año» donde el guion decía «dos años»
  (del 69 al 71 son dos), y en **15:56** dice «21.700 años-músico» donde el estudio y el guion
  dicen 21.750. Ambas confirmadas con doble transcripción, no son fallos de Whisper.
- **A `cfg=1.0` el prompt negativo no actúa.** Z-Image Turbo corre así, y por eso las tres primeras
  portadas salieron con vinilos de diana, relojes y calaveras pese al veto completo en el negativo.
  El veto se resuelve **construyendo la escena para que no haya motivo** de que aparezca lo vetado.
  La regla ya estaba escrita en `comfyui/docs/prompting.md` — el fallo fue no consultarla.
- **Los timestamps del SRT se corren cerca de la música**: el alineador fechó la primera frase del
  cuerpo en 28,5 s cuando arranca en 35,5. Dentro del cuerpo son fiables.
- **Ningún buscador de texto ve el `\r`**: `awk`, `grep` y `Select-String` devuelven cero sobre un
  archivo CRLF. Para verificar finales de línea, contar bytes con python u `od`.
- **Reprocesos por procedencia hoy: 3.** Los tres del mismo tipo — el dato correcto estaba
  disponible y no lo consulté: la salida de `wpm.py` sin mirar qué contaba, el `cfg=1.0` impreso en
  pantalla dos pasos antes de escribir el veto, y la regla de PS 5.1 sobre `2>&1` que está en la
  documentación de la herramienta.

---

## Questions to Answer

- ¿Se corrigen alguna vez el «un año» de 12:48 y el «21.700» de 15:56, o quedan así de forma
  definitiva? Hoy la decisión fue dejarlas.
- ¿La portada 16:9 y 9:16 y las quote cards se hacen antes del viernes o después de publicar?
