# Handoff: MPD EP.007 — reescritura completa, misterio sobre resolución

**Date:** 2026-08-05 (miércoles)
**Machine:** desktop (E:\ existe, verificado; grabación en `E:\Podcast\MPD\Temporada 2\EP 02`)
**Status:** In progress — guion reescrito y grabado UNA vez (toma corta, 24:40); falta segunda
grabación sobre el guion ya extendido a 5.725 palabras, y una ronda de verificación de fuentes.

---

## What We Accomplished This Session

**Corrección de fondo, en 3 pasadas de feedback de Andrés**

1. **Mythbusters → cuento de los hermanos Grimm.** El enfoque de "destapar la leyenda" (heredado
   del canon del 2026-07-24) se retiró. Medido: T2·E1 salía 1:5 leyenda:corrección, el primer
   borrador de EP.007 1:2. Ambos eran el show resolviendo el misterio, solo que con más o menos
   elegancia.
2. **No resolver, ni siquiera "con matices".** El episodio no debe decir quién tiene la razón, ni
   dar un veredicto final. Se deja al oyente investigar por su cuenta.
3. **No hedging al aire.** Frases como "esto no está confirmado" o "en fuentes débiles" **dentro
   del `host-text`** también rompen inmersión, aunque sean honestas. Esa cautela va SOLO en
   `.verificar`/`nota-produccion` (no se lee) o en una única línea de cierre ("cada quien decide
   qué cree").

Las dos correcciones quedaron guardadas en memoria:
`feedback_mpd_mystery_over_resolution.md` y `feedback_mpd_no_hedging_onair.md`.

**EP.007 reescrito de raíz** — `mrputridsden-production/scripts/EP007-el-rock-y-el-diablo.html`
- Los tres actos (encrucijada, Boleskine, backmasking) se cuentan completos, con escena, sin
  destape ni veredicto.
- Entró el tercio de "símbolos" que faltaba y que el título ya prometía: los 4 símbolos de
  *Led Zeppelin IV*.
- Quitado el Takeaway explícito ("quién escribió cada historia") — era la resolución que se
  estaba evitando.
- Artifact publicado: https://claude.ai/code/artifact/43ede7d6-8099-4da5-bd27-71a709c7a507

**Grabación real + recalibración con datos propios (no prestados)**
- Andrés grabó el borrador corto (3.322 palabras) en `E:\Podcast\MPD\Temporada 2\EP 02\` (wav +
  mp3 + rpp). Medido con ffprobe/silencedetect: **24:40, pausa 24,9%**.
- Transcrito con WhisperX (SRT en `E:\Transcriptor\transcripciones\MPD EP 02.srt`). wpm real:
  **176,9**. Expansión real: **1,005** (casi verbatim — mucho más ajustado que el 1,087 de T2·01).
- Con esos números reales (no los de T2·E1), el objetivo correcto para 43 min es **~5.790
  palabras**, no las ~5.280 que había calculado con la calibración prestada.
- Guion expandido en pasadas chicas (100-300 palabras + remedición) hasta **5.725 palabras**
  (dentro del ±3% del objetivo). Balance por acto: Cold open 508 · Acto I 1.709 · Acto II 1.773 ·
  Acto III 1.400 · Cierre 335.
- Punto de calibración T2·02 agregado a `guion-style-mpd.md` (expansión ya en n=4).

**Conector del Expediente 03 decidido** — Andrés vio que Crowley ya queda instalado como
personaje en el Acto II y decidió que el próximo expediente es **Crowley y su huella musical más
allá de Zeppelin** (leads sin verificar: "Mr. Crowley" de Ozzy, mención en "Quicksand" de Bowie,
su rostro en *Sgt. Pepper's*). Reemplaza a "Paul is Dead" como candidato principal (queda como
secundario). **NO se anuncia al aire en el cierre de EP.007** — mismo criterio de "anunciar es un
compromiso" que ya estaba en el canon.

**Retrospectiva aplicada**
- `mrputridsden/CLAUDE.md` — el canon de formato del 2026-07-24 ("desenmascarar el mito sin apagar
  el escalofrío") se marcó SUPERADO y reemplazado, con el bloque viejo conservado en `<details>`
  como registro histórico. Se agregó un checklist de auto-chequeo de 2 preguntas antes de entregar
  cualquier guion/revisión.
- `guion-style-mpd.md` — regla nueva: una pasada de reescritura que agregue más de 5 `.verificar`
  necesita su propia sesión de verificación antes de grabar, no exprimirla el mismo día.
- Auditoría del kit corrida (`audit-triggers.py`): 0 colisiones, 0 `SKILL.md` sobre 50 líneas —
  sin hallazgos, esta sesión no tocó skills.

---

## Where We Paused

**Last action:** retrospectiva aplicada y commiteada (parte del commit `78553d2` + este handoff).

**Next action:** decidir cómo cerrar la deuda de verificación antes de la próxima grabación —
ver Questions to Answer.

**Blockers:**
- Ninguno técnico. El guion está listo para una segunda grabación completa (~43 min) siempre que
  se resuelva primero la verificación de fuentes de abajo.

---

## Files to Read First

- `mrputridsden-production/scripts/EP007-el-rock-y-el-diablo.html` — el guion final, con **~16
  bloques `.verificar`** (6 originales de la sesión del 03-ago + ~10 nuevos de hoy)
- `mrputridsden-production/guion-style-mpd.md` § Punto de calibración T2·02 y § regla nueva de
  deuda de verificación
- `.claude/skills/mrputridsden/CLAUDE.md` § Formato narrativo — canon nuevo + checklist
  de auto-chequeo
- `mrputridsden-production/banco-expedientes.md` — Crowley ahora es el candidato 2 (principal)

---

## Notes / Gotchas

- **La expansión (escrito→hablado) NO es una constante del show — varía por toma, no solo por
  episodio.** T2·01 dio 1,087; esta misma grabación de EP.007 dio 1,005, casi verbatim. Antes de
  dimensionar un guion, usar el SRT de LA MISMA grabación si existe, nunca el de otro episodio.
- **La grabación que existe en `E:\Podcast\MPD\Temporada 2\EP 02\` es del guion CORTO (3.322
  palabras), no del guion final (5.725).** Hay que regrabar completo — lo grabado hoy sirvió para
  calibrar, no es la toma final.
- **~10 marcadores `.verificar` nuevos quedaron sin abrir** (raíz africana del mito del cruce,
  incendio de Boleskine 1900, lecturas de los símbolos de *Led Zeppelin IV*, cita de Rob Halford
  sobre el juicio, alcance del PMRC/audiencia del Senado de 1985, fama de Tommy Johnson en vida,
  escultura turística de Clarksdale, si el juicio de Nevada fue con jurado o no, año de muerte de
  Kenneth Anger). Ninguno se verificó en esta sesión — quedaron marcados, no investigados.
- **No hay `USER-COMMENT`/`NEEDS USER INPUT`/`[TODO]`/`FIXME` pendientes** en los archivos de
  producción tocados hoy — los pendientes reales están todos en formato `.verificar`, ya listados
  arriba.

---

## Questions to Answer

1. **¿Se dedica la próxima sesión a verificar los ~10 marcadores nuevos antes de grabar, o se
   graba con lo que hay y se corrige en edición si algo falla?** La regla nueva de esta sesión
   dice que más de 5 `.verificar` sin cerrar pide una sesión dedicada — pero es decisión de
   Andrés, no automática.
2. **¿Se empieza ya la investigación del Expediente 03 (Crowley y su huella musical), o se espera
   a cerrar EP.007 primero?**
3. **Pendiente de antes, sigue abierto:** los plays de EP.002–EP.005 (solo Andrés los tiene en
   Spotify for Podcasters) — el banco de temas sigue ordenado por criterio, no por audiencia real.
