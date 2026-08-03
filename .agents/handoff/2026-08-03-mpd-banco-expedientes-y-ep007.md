# Handoff: MPD — banco de expedientes T2 y borrador de EP.007

**Date:** 2026-08-03 (lunes — verificado con `Get-Date`)
**Machine:** desktop (E:\ existe, verificado)
**Status:** In progress — el guion de EP.007 está escrito pero **corto y no grabable**; falta una segunda ronda de fuentes.

---

## What We Accomplished This Session

**Selección de temas — regla nueva de Andrés (la decisión más importante del día)**

- Andrés corrigió un sesgo del análisis: yo estaba tratando la **alta rotación de un tema como
  defecto**. Al revés — es **demanda probada**, y con audiencia en construcción ir al nicho
  primero hace la captación mucho más difícil.
- El diferenciador **no es la originalidad del tema: es el detalle subexpuesto**.
- Los temas de nicho **no se descartan**: se aplazan a **uno cada 3 o 4 episodios**. Con la cuenta
  actual, el primer slot de nicho cae en **T2·E4 o T2·E5**.
- Escrito en `roadmap-mpd.md` § Regla de audiencia, como "segunda capa".

**Banco de expedientes (archivo nuevo)**

- `mrputridsden-production/banco-expedientes.md` — 17 candidatos en dos carriles, **cada uno
  marcado VERIFICADO o SIN VERIFICAR** según si se abrió la fuente o sale de memoria del modelo.
- Incluye competencia mapeada, y **11 temas descartados por premisa fabricada** — venían de una
  grilla de sugerencias generada por IA que Andrés estaba revisando; siguen una plantilla y
  describen fenómenos que no existen (no hay fuente primaria que abrir).
- Hallazgo de mercado: los episodios top de **Leyendas Legendarias** (el podcast más escuchado de
  México en Spotify) son Crowley, pactos con el diablo y MK Ultra. El género premia el territorio
  ocultista. **Decisión de Andrés si eso mueve el límite del show** — el límite escrito es sobre
  simbología en branding/artwork, no sobre tratar el tema con ángulo escéptico.

**T2·E1 cerrado con datos verificados**

- **Publicado el 2026-08-01** (la memoria decía 07-31 — estaba mal), **41 min**,
  https://open.spotify.com/episode/3KW68cHhHpkMCLbgZkiov7
- Título publicado: "El Club de los 27: la maldición que los números desmienten".
- Todo leído de Spotify, no de memoria. `roadmap-mpd.md` y la memoria ya actualizados.
- **Checkpoint de plays: ~2026-08-14.**

**EP.007 — investigación y borrador**

- Alcance aprobado: **expediente completo en tres actos**, que es lo que T2·E1 prometió al aire.
- Tres ángulos verificados en esta sesión, uno por acto. La tesis: **las tres leyendas satánicas
  del rock tienen autor humano identificable, y ninguno es el diablo.**
  - Acto I: la leyenda de la encrucijada era de **Tommy Johnson**, contada por su hermano
    **LeDell** al folclorista **David Evans** (1971). Saltó a Robert Johnson porque los dos
    vivieron en **Hazlehurst, Mississippi**. Además: el mito lo construyó la reedición de
    **Columbia de 1961** (*King of the Delta Blues Singers*), no el Delta de los 30.
  - Acto II: Page compró **Boleskine House** a comienzos de los 70 y la vendió en 1992; abrió la
    librería ocultista **The Equinox** en 1974. El pacto se lo debemos en buena parte a
    **Kenneth Anger**, colaborador despechado que lo llamó *"dabbler"* en prensa.
  - Acto III: **Michael Mills** lanza lo de "Stairway" al revés en **1981**; audiencia de la
    Asamblea de California en **1982**; y el juicio a **Judas Priest en Nevada, 1990**,
    desestimado.
- Guion: `scripts/EP007-el-rock-y-el-diablo.html` + su `.artifact.html`.
- Artifact publicado (privado): https://claude.ai/code/artifact/b0212e3a-a943-4707-9577-e69ac5c0395f

**Retrospectiva aplicada (3 cambios)**

1. `mrputridsden/CLAUDE.md` — **anunciar el próximo expediente al aire es un compromiso
   vinculante**, no un gancho. Decidir antes de grabar; si se anuncia, escribirlo en el guion; y
   **abrir el cierre del episodio anterior al arrancar cualquier expediente**.
2. `guion-style-mpd.md` — **el primer borrador llega corto**; dimensionar el MATERIAL antes de
   escribir, no solo el texto.
3. `scripts/mk-artifact.py` — herramienta nueva, sale del scratchpad. Verificada contra el caso
   que ya funcionaba: reproduce byte por byte el artifact publicado.

---

## Where We Paused

**Last action:** retrospectiva aplicada y pusheada (`e35cee3`); auditoría del kit corrida sin
hallazgos (0 colisiones de triggers, 0 SKILL.md sobre 50 líneas medido con `wc -l`).

**Next action:** **segunda ronda de fuentes para EP.007.** El guion está 33% corto y no se arregla
rellenando.

**Blockers:**
- **Faltan los plays de EP.002–EP.005** (solo Andrés los tiene, en Spotify for Podcasters). Sin
  eso, el banco está ordenado por criterio mío y por saturación del mercado, no por la audiencia
  real del show. La columna del roadmap lleva vacía desde EP.003.
- **Sin decidir:** si el cierre de EP.007 anuncia el tema del Expediente 03.

---

## Files to Read First

- `mrputridsden-production/banco-expedientes.md` — el banco de temas, con fuentes marcadas
- `mrputridsden-production/roadmap-mpd.md` § Regla de audiencia — la regla nueva de Andrés
- `mrputridsden-production/scripts/EP007-el-rock-y-el-diablo.html` — el borrador y sus 4 recuadros
  rojos (`.verificar`)
- `mrputridsden-production/guion-style-mpd.md` § El primer borrador llega corto

---

## Notes / Gotchas

- **El guion está 33% corto: 3.471 palabras narradas contra ~5.200.** Da 28,9 min leído pausado
  contra un piso de 40. **NO rellenar** — la § Pasada de relleno lo prohíbe explícitamente. Los
  cuatro sitios donde cabe material verificado están anotados dentro del propio guion; el más
  rentable es **quién era Tommy Johnson**, que hoy es solo un nombre y de él depende que el Acto I
  duela.
- **El material de Kenneth Anger es el más flojo del episodio.** El pleito por *Lucifer Rising* y
  el insulto público están reportados; **la maldición privada solo aparece en blogs y Steemit**. El
  guion dice explícitamente que al aire eso no se afirma. No subirle el peso sin fuente mejor.
- **Robert Johnson NO es el tema de EP.007, es la puerta.** Su biografía se gastó en el bloque C de
  T2·E1 (las dos fotos, tocar de cara a la pared, el fundador retroactivo) y no se repite. Tanto el
  roadmap como la memoria lo llamaban "el episodio de Robert Johnson" — el guion de T2·E1 decía
  otra cosa. Se agarró abriendo el guion.
- **El lint del guion ya está corrido** y sus resultados están pegados en el archivo: 0 muletillas,
  0 prohibidas, 0 deificación, 0 tuteos, 0 incidencias en el lint de bloques. Lo único que falla es
  el largo.
- **Registro confirmado: bogotano**, igual que T2·E1. El pendiente de español neutro de
  `guion-style-mpd.md:10` queda **re-aplazado** por decisión de Andrés — cambiar de registro en el
  episodio 2 de una temporada no se hace sin motivo.
- Los `.verificar` del guion son marcadores pendientes reales aunque no usen la sintaxis `[TODO]`:
  fecha de Boleskine (1970 vs 1971 → decir "a comienzos de los 70"), y **nombres y desenlace de los
  dos jóvenes de Nevada**, que son personas reales con familia viva.

---

## Questions to Answer

1. **¿Los plays de EP.002–EP.005?** Es lo que convierte el banco de criterio en medición.
2. **¿EP.007 anuncia el Expediente 03 en su cierre, o no?** Si sí, el candidato más limpio es
   **"Paul is Dead"** — misma mecánica (pistas inventadas por un autor identificable, Fred LaBour,
   *Michigan Daily*, 14-oct-1969) y es de carril principal.
3. **¿El límite de ocultismo se mueve?** La data dice que el género premia ese territorio. El
   límite escrito es sobre simbología en branding y artwork, no sobre el tema. Decisión de Andrés.
4. **Falta un expediente latinoamericano en el banco.** La regla de audiencia dice que lo local
   conecta doble (Kraken lo confirmó) y no hay ni uno. La memoria lo tenía anotado como pendiente
   desde julio. Vale una sesión de búsqueda propia.
