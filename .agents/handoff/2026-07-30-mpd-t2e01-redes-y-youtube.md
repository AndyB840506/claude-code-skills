# Handoff: MPD T2·E1 — redes programadas y canal de YouTube

**Date:** 2026-07-30 (jueves)
**Machine:** desktop (E:\)
**Status:** Complete — **las tres publicaciones quedaron programadas en IG + FB.** El episodio
publica **mañana viernes 31**. YouTube queda parqueado por decisión de Andrés.

> Tercer handoff con fecha 2026-07-30. Los otros dos son de temas distintos:
> `2026-07-30-mpd-t2e01-artwork-el-27.md` (sesión de la mañana, artwork) y
> `2026-07-30-andyfreelancer-admin-password.md` (otro proyecto). Este continúa el primero:
> su Next Step #4 era «plan de lanzamiento de T2·E1 — es lo único del episodio que falta».
> Eso es lo que se hizo acá.

---

## Qué se hizo

### 1. Plan de lanzamiento social — creado y PROGRAMADO

`episodios/social-ep006.md` (commit `c2169b2`). **No existía**: verificado contra el disco, no
contra el handoff — el patrón `social-epNNN.md` tenía 002/004/005 y faltaba el 006, y
`ep006-metadata.md` lo decía por su lado («Falta solo el plan de lanzamiento»).

| Día | Fecha | Ángulo | Pieza |
|---|---|---|---|
| 1 · Lanzamiento | viernes 31 jul | La maldición no aguanta el examen | Portada 1:1 + story 9:16 + Q1 |
| 2 · Contenido | domingo 2 ago | Lo que el mito tapa: la fama a los 20 | Card Q2 (35:01) |
| 3 · Recordatorio | martes 4 ago | Cierre humano, última llamada | Card Q4 (41:21) |

Días de semana verificados contra el calendario real. **Andrés confirmó que los tres quedaron
programados** (commit `4e06ef3`).

### 2. Dos trampas que se evitaron, y por qué importan

- **El molde de EP.005 es de Temporada 1.** Traía thread de X/Twitter y hook de TikTok —
  pero X no está activo y TikTok lleva en pausa desde el 2026-07-19. La regla vigente
  (`social-t2-revelacion.md`) es **solo Instagram + Facebook**. También traía hashtags
  retirados con el pivote (`#DondeRiffsEncuentranWhisky`, `#RiffsYWhisky`, `#RocksMetalJazz`,
  `#ConversacionesDeRiffs`, `#BogotaMusical`).
- **El gancho del cold open estaba quemado.** Los 4 beats del arco de revelación ya habían
  salido —dato que **solo Andrés tenía**, no está en el repo— y el Beat 3 ya contó Brian Jones
  en la piscina + Morrison en París. Ese mismo párrafo abre la descripción de Spotify. El Día 1
  se reescribió para abrir con **el giro** (el episodio desmiente la maldición que el teaser
  prometió), que es lo único que ningún teaser reveló.

### 3. Artifact publicado

https://claude.ai/code/artifact/4cc9f260-8a65-47bc-ab02-2d218e7406db — el plan con el copy
listo para pegar, botón de copiar por bloque y conteo de caracteres. Paleta de La Guarida
sacada del specimen `rebrand/identidad-la-guarida.html`, tema único (nocturno) a propósito.
**Si se edita `social-ep006.md`, republicar sobre esa misma URL.**

### 4. Canal de YouTube — creado, enlazado y PARQUEADO

`https://www.youtube.com/channel/UC9NYMQREuQj2VtDS0YFXbrA` (commits `b459a9b`, `84b3e2d`).

- Agregado a `show-metadata-t2.md` y a **los dos** bloques de enlaces de `ep006-metadata.md`
  (el plano y el HTML).
- `episodios/youtube-ep006.md` nuevo: título, descripción densa en keywords, 20 tags y capítulos.
- **⏸️ Decisión de Andrés: T2·E1 NO se anuncia en YouTube. El anuncio arranca con el próximo
  episodio.** El archivo está marcado como parqueado. **No es un pendiente.**

### 5. El hallazgo que sobrevive al episodio: capítulos de YouTube

**La lista de capítulos de Spotify NO es portable a YouTube tal cual.** `ep006-metadata.md`
trae 18 marcadores; el último es `41:38 Outro` sobre un episodio de `41:47` — **9 segundos**.
YouTube exige mínimo 10 s por capítulo y **descarta la lista entera en silencio** si uno
incumple: el video queda sin capítulos y no avisa. La versión de YouTube usa **17**, cortando
en `39:01 Cierre`. Regla escrita en `podcast-creator/workflows/07-youtube.md`.

### 6. Retrospectiva aplicada (commit `5536afb`)

Tres reglas, y el `/prompt-reviewer` encontró un defecto en una de ellas antes de cerrarla —
ver § Notes.

---

## Dónde pausamos

**Última acción:** cierre de sesión, retrospectiva y auditoría aplicadas.
**Siguiente acción:** cuando el episodio publique mañana, cambiar el link del show por el deep
link del episodio.
**Bloqueantes:** ninguno. El episodio está programado y las redes también.

---

## Archivos a leer primero

- `episodios/social-ep006.md` — el plan, con su sección de Gotchas (lo que quedó abierto)
- `episodios/youtube-ep006.md` — metadata de YouTube **parqueada**, y la regla de los capítulos
- `episodios/ep006-metadata.md` — descripción, capítulos y estado del episodio

---

## Next Steps

**Con fecha — mañana viernes 31, cuando publique:**

1. **Cambiar el link del show por el deep link del episodio.** Andrés dijo: *«cuando te pase la
   info del capítulo se actualiza, no hay pedo»* — o sea, él pasa la URL y se actualiza.
   Va a **dos** sitios en `ep006-metadata.md`: el bloque de descripción plano y el HTML.
   ⚠️ Los posts de **Facebook ya programados** también llevan el link del show; esos se editan
   **en el programador, no en el repo** — cambiar el `.md` no los toca.
2. **Re-pegar la descripción en Spotify si se quiere que el link de YouTube salga.** Al agregar
   el canal, el archivo y lo publicado dejaron de coincidir. Se puede hacer en la misma pasada
   que el punto 1.

**Sin fecha, decisiones de Andrés que quedaron abiertas:**

3. **Las 4 quote cards son 16:9.** En el feed de Instagram una pieza apaisada rinde peor que
   1:1 o 4:5. **No se recortaron** — re-renderizar desde `mpd-quote-card-t2.py` cambia un asset
   ya aprobado, así que es decisión suya.
4. **Nota de contenido / línea de apoyo.** El copy del Día 2 y del Día 3 va directo a sobredosis
   y suicidio. `show-metadata-t2.md` deja abierta la decisión editorial. **No se agregó.**
5. **Falta el clip de audio de 30-60 s.** Candidatos: el tramo del BMJ (15:27-18:00) o el cierre
   de «lo que el mito tapa» (35:01).
6. **El 16:9 usado como miniatura de YouTube anuncia Spotify, Apple y Amazon — no YouTube.**
   Y a 320×180 la bajada en itálica no se lee. Las dos se arreglan re-renderizando desde
   `mpd-portada-ep-t2.py`. Relevante solo cuando arranque el anuncio en YouTube (punto 7).

**Para el próximo episodio:**

7. **Arranca el anuncio en YouTube.** `youtube-ep006.md` queda como plantilla: lo reutilizable
   es la estructura y **la regla de los capítulos**, que aplica a todos los episodios.

**Verificaciones sueltas del canal (mi instrumento fue débil, mirarlas a ojo):**

8. **El nombre del canal parece decir «Mr Putrid's Den» sin punto**; el canónico —y el wordmark
   del propio artwork— es **«Mr. Putrid's Den»**. Lo único que llegó fue el `<title>` a través de
   un conversor a markdown, así que puede ser artefacto del instrumento.
9. **No se confirmó si hay handle.** La URL es `/channel/UC9NYM…`. Si no está fijado,
   `@mrputridsden` alinearía con Instagram.

**Marcadores pendientes:** se escaneó `mrputridsden-production/` por `USER-COMMENT`,
`NEEDS USER INPUT`, `FIXME`, `[TODO]` y `[VERIFICAR`. Los dos hits (`ep006-metadata.md:139` y
`guion-style-mpd.md:279`) son **narrativos** —describen un hueco de verificación pasado— y no
piden acción. **Sin marcadores vivos.**

---

## Notes / Gotchas

- **Reprocesos por procedencia hoy: 1.** Verbal, no de commit. Se afirmó «para el perfil de
  YouTube no hay nada en el kit» después de grepear **el repo**; un minuto después `E:\` tenía
  el kit de redes completo — banner 2560×1440, avatar, cover de Facebook, header de X. La regla
  de que el output va a `E:\` existía, pero escrita como regla de **escritura**; muerde como
  regla de **búsqueda**.
- **El `/prompt-reviewer` encontró un defecto en la regla que yo acababa de escribir para
  arreglar eso.** La primera versión decía «el repo guarda instrucciones; el disco guarda el
  producto» — **falso**: hay 12 assets renderizados dentro del repo (`den-bg.jpg`,
  `og-image.jpg`, `t2-cover.jpg`, `bar-bg.png`…), en `*/website/`, porque se despliegan desde
  ahí. Tal como estaba, la regla habría causado el error inverso. Corregida al corte real:
  **`E:\` = artwork de episodio, audio, banners de redes; repo `*/website/` = assets del sitio.**
  Moraleja operativa: la regla nueva escrita para tapar un fallo puede traer su propio fallo —
  por eso existe el paso de review.
- **El estado de publicación de una campaña no vive en el repo.** Qué beats salieron solo lo
  sabía Andrés. El calendario daba una aritmética plausible (22/25/28/31) que **no es evidencia**.
  Preguntarle fue lo que evitó repetir el gancho por tercera vez. Regla escrita en
  `podcast-creator/workflows/04-social-media.md`, como pregunta 5 del Paso 1.
- **El lint de copy mide dentro de los bloques, no sobre el archivo.** El documento nombra los
  hashtags retirados en su sección «no usar», así que un grep crudo se encuentra a sí mismo.
  De paso cazó un typo (`sobreidosis`).

---

## Questions to Answer

- ¿El nombre del canal lleva el punto de «Mr.»? (punto 8)
- ¿Se fija el handle `@mrputridsden`? (punto 9)
- ¿Se re-renderizan las quote cards a formato de feed? (punto 3)
- ¿El Día 3 cierra con línea de apoyo? (punto 4)
- Vienen de antes, sin decidir: «Martes de misterio», episodio de leyendas venezolanas,
  ofrecimiento de ayuda con la edición, y el español neutro en MPD (aplazado a la semana del
  **2026-08-03**, marcador vivo en `guion-style-mpd.md` línea ~10).
