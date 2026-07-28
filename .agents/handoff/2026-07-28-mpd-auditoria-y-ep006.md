# Handoff: MPD — auditoría de reglas + reestructura de EP.006 (T2·E1)

**Date:** 2026-07-28 (martes)
**Machine:** desktop (E:\)
**Status:** Complete — todo commiteado y pusheado. EP.006 **no se publica**: Andrés va a regrabar.

> Tercer handoff del 2026-07-28. Los otros dos son de BTQ (`2026-07-28-btq-articulos-web-y-linkedin.md`)
> y no de MPD. Este es el de MPD.

---

## Qué se hizo

Arrancó como "revisemos MPD full" → auditoría de reglas, y derivó en la revisión completa del
guion del estreno de Temporada 2. Ocho commits, de `5683f7e` a `d80d368`.

### 1. Auditoría de reglas del kit MPD (`5683f7e`)

**27 mandatos muertos de la era T1 retirados** de 12 archivos. Los que más podían morder:

- El **Segmento de Promoción** (retirado 2026-07-17) seguía vivo en 5 sitios, incluida la tabla de
  arquitectura que se le presenta a Andrés para aprobar antes de escribir un guion.
- **`MEMORY.md` seguía ordenando** la regla de 2 partes ("build the P1/P2 cut from the start")
  aunque el archivo apuntado sí decía RETIRED. Eso se carga en cada sesión.
- El default del workflow era `formato_episodio = "co-host"`.
- El saludo de la skill decía **"sumerce"**, prohibido 34 líneas más abajo en el mismo archivo.
- Los **templates de La Silla Pútrida** iban firmados "Andrés & Juan", prometían "los tres en el
  mismo cuarto" y describían el show viejo — y son documentos que se le mandan a un invitado real.
  Reescritos completos.
- `C:\Users\andre\repos\kit-skill-creator` **no existe** (verificado); estaba citado como raíz.

Intacto porque estaba bien: `podcast-profile.json` y las secciones de canon T2.

### 2. EP.004 verificado y numeración de T1 sellada (`3901023`, `3abecde`)

Ambas partes publicadas — verificado contra Spotify, no de palabra. P1 salió el **2026-06-14** (no
el 19 que decía el plan), 1h45; P2 el 06-20, 1h16.

**Decisión de Andrés: T1 queda sellada en T1·01–T1·05, no se renumera.** El hueco del archivo web
(la Parte 2 no tiene fila; el sitio dice tener la temporada completa con 5 filas cuando T1 publicó
6 items) se **aceptó como cosmético, NO es un pendiente** y no se re-litiga.

### 3. Revisión del guion de EP.006 (`37473f8`, `22fe9de`, `4663832`, `d80d368`)

El feedback del piloto (círculo cercano, vía WhatsApp) está ahora transcrito en
`audio/t2-disclaimer-e-intro.md` §1.b — antes vivía solo en el chat.

**Reestructura — el hallazgo de fondo.** El problema no era el tema sino que **el destape entraba
en el minuto 29:30**: media hora de retelling que el oyente ya se sabe antes de lo único que no
sabe. Ahora son 4 bloques y el desmentido (estudio BMJ) entra en **12:30**. El Bloque A cierra
reconociendo de frente "usted ya se sabe esto", lo que convierte la familiaridad en complicidad.

**Datos:** los 5 marcadores `[VERIFICAR]` estaban abiertos con el piloto ya grabado. Verificados
contra fuentes; **dos no aguantaron**:
- La sobredosis de Roma dejó a Cobain en coma **~20 horas, no "varios días"**.
- La frase de la mamá de Cobain es real (dicha a AP) pero **su significado está en disputa** —
  Segalstad sostiene que hablaba de dos tíos y un tío abuelo suicidas, no del club. El guion la
  daba como acta de fundación. Reescrito para contar las tres lecturas; ese pasaje nuevo es lo
  que subió el conteo sin rellenar.

**Apertura:** entraron el logo sonoro y el disclaimer que faltaban; el disclaimer bajó de 88 a 28
palabras (~50s → ~15s) y **sin susurro**. El guion pedía la música de **Temporada 1** en los dos
extremos; ahora pide la de T2 con advertencia de no usar la vieja.

**Paleta:** el guion seguía en el sistema visual de T1 (crimson, ámbar retirado, oro). Pasado a
"La Guarida" con los tokens leídos del specimen. Dos colores sobrevivían como **estilos inline**
en el body, invisibles al reemplazar el CSS.

### 4. La corrección de Andrés sobre la duración (`48f0df5`)

**Este es el punto más importante para la próxima sesión.** Se leyó el piloto de 45:55 como "el
guion está 13% largo", se cortaron ~500 palabras y se escribió en la guía un ritmo de "113,9
palabras/min" como constante. **Falso.** Andrés corrigió: lo leyó lento a propósito. Medido:

| | |
|---|---|
| Articulación de Andrés | **~175 wpm** — constante, n=12 SRT, igual en BTQ y MPD |
| Pausa en el piloto | **32,5%** (14,9 min de silencio en 45:55) |
| Pausa en T1 | 9-14% |
| Expansión del piloto | ~1,04 — leyó casi textual |

El modelo nuevo está en `guion-style-mpd.md`: `minutos = (escritas × expansión) / 175 / (1 − pausa)`.
El mismo guion dura 44 min pausado y 35 ágil. **La densidad de pausa es decisión de dirección y hay
que fijarla ANTES de dimensionar.**

### 5. Loudness del piloto (targets, no fix — se regraba)

−25,8 LUFS integrado (target −16), LRA 15,1 (target ~6), true peak −2,1 dBFS ✓. Y se hunde en el
medio: −20,4 → −24,5 → −27,8 → **−29,2** → −19,6 por tramos. Comandos de verificación en la guía.

---

## Artefacto

**https://claude.ai/code/artifact/5ccd68c4-f116-429d-90ff-7c384e7c8647** — misma URL de siempre,
actualizada con todo lo anterior y la paleta de La Guarida. Estaba en la versión del 22 de julio.

Scripts de medición nuevos, guardados en `mrputridsden-production/`: `wpm.py` (ritmo desde SRT) y
`voiced.sh` (fracción con voz desde mp3).

---

## Next Steps

**Bloqueante, y es de Andrés (no lo puedo generar yo):**
1. **Logo sonoro (3–5 s)** — único pendiente de la apertura fija. Brief en
   `audio/t2-disclaimer-e-intro.md` §2. Es literalmente lo que pidió el feedback: "un opening
   corto y pegajoso, q uno se lo pueda aprender". Disclaimer y música de intro **ya están hechos**
   (confirmado por Andrés hoy) — pero **falta la ruta de esos archivos**, pedírsela antes de asumir.
2. **Recortar las músicas** a ~18 s (intro) y ~15 s (outro).

**Antes de regrabar:**
3. **Prueba de pausa** — grabar 2-3 min leyendo como se va a leer, medir con el procedimiento de
   `guion-style-mpd.md` § Prueba de pausa, y **recién ahí** decidir si el guion queda en 5.087
   palabras o hay que devolverle las ~500 que se cortaron (están intactas en el commit `37473f8`).
   Andrés eligió "déjame probarlo primero" — no dimensionar sin ese dato.
4. **Fechas del racimo — ÚNICO `VERIFICAR` abierto del guion.** Jones 3-jul-69, Wilson 3-sep-70,
   Hendrix 18-sep-70, Joplin 4-oct-70, Morrison 3-jul-71, Cobain 8-abr-94, Winehouse 23-jul-11,
   Johnson 16-ago-38. **No se verificaron una por una** — solo que son internamente consistentes.
   Todo el cold open se apoya en el 3 de julio. **Actúa: Claude, si Andrés lo pide.**

**Post-grabación:**
5. SRT (WhisperX) → recalibrar expansión y pausa, subir T2 a n=2 en `guion-style-mpd.md`.
6. Metadata/show-notes (`episodios/ep006-metadata.md`, no existe), quote cards, plan de lanzamiento.
7. Máster a −16 LUFS / LRA ~6.

**Decisiones abiertas registradas hoy en `roadmap-mpd.md` (salieron del chat, no estaban en disco):**
8. **"Martes de misterio"** — idea de cadencia de Andrés, respaldada en el feedback. Sin decidir.
9. **Episodio de leyendas venezolanas** — ella y una amiga; Andrés ofreció invitarlas. Contacto
   tibio, sin fecha.
10. **Ofrecimiento de ayuda con la edición** — dicho en firme, sin usar. Si la edición es el cuello
    de botella de la cadencia, esto ya está sobre la mesa.

**De antes, sigue vigente:**
11. **Español neutro en MPD** — decidido 2026-07-25, aplazado a la semana del **2026-08-03**. Al
    retomarlo, leer la sección de BTQ y **adaptarla, no copiarla**.
12. Subir la portada nueva de T2 a Spotify/Apple/Amazon (manual de Andrés, viene de antes).

---

## Notes / Gotchas

- **El artefacto publicado puede estar más viejo que el archivo local.** Estaba en la versión del
  22-jul. Leerlo (WebFetch) antes de sobrescribir — fue eso lo que destapó que el guion todavía
  cargaba el codename retirado "The Crossroads".
- **Los lints con tildes pasados por la línea de comandos dan ceros falsos.** Escribir el script a
  disco con escapes unicode. Quedó como regla en `skills/CLAUDE.md`.
- **`silencedetect` con umbral absoluto sub-reporta en los tramos fuertes** — dio "1 pausa" en el
  último minuto porque estaba 10 LU más alto. Lo desmintió el espectrograma.
- **Reprocesos por procedencia hoy: 2.** (1) Se dedujo la duración del guion teniendo el mp3 en
  disco; (2) la auditoría de reglas barrió los documentos pero no los entregables producidos bajo
  ellas, y por eso el codename y la paleta retirados sobrevivieron. Las dos lecciones quedaron
  escritas en `~/.claude/CLAUDE.md` §Procedencia y en `skills/CLAUDE.md`.
