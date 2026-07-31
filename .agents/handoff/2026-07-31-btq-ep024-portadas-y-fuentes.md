# Handoff: BTQ EP.024 — portadas v4 y re-verificación de fuentes

**Date:** 2026-07-31 (viernes)
**Machine:** desktop (E:\)
**Status:** In progress — EP.024 **listo para grabar**, sin ninguna cifra sin verificar.
MPD T2·E1 sale hoy a las **21:00**.

> **Este handoff se extendió en una segunda pasada de la misma sesión** (ver § Segunda mitad).
> Se prefirió extenderlo antes que escribir un segundo archivo del mismo día sobre el mismo
> episodio, que habría obligado a reconciliar dos documentos. Lo de la primera mitad queda como
> está; lo que cambió de estado está marcado abajo.

---

## What We Accomplished This Session

### 1. Portadas de BTQ EP.024 — las 3, con la compuerta en PASS

`E:\Podcast\BTQ\EP 24\BTQ Artwork EP 24\` — 1:1 (3000²), 16:9 (1920×1080), 9:16 (1080×1920),
más el JPG q92 y los reescalados de 300 y 96 px.
`verify_assets.py EP024 --root "..." --stage-a` → **PASS**, exit 0. Negro de marca `#0E1113`,
cero negro puro. Stage 2 leído a ojo en las tres.

### 2. El generador y la fórmula de título estaban en conflicto — arreglado

`portada-ep-compose.py` nació el 2026-07-25 esperando un ancla de **nombre propio de 2 palabras**
y la dibujaba **una palabra por línea**. La fórmula invertida del 2026-07-28 —y EP.024 es el
primer episodio que la usa— hace que el ancla sea una frase de 10 palabras.

| | ancla 1:1 | ancla 16:9 | legible a 96 px |
|---|---|---|---|
| EP.023 (fórmula corta) | 420 px | 216 px | sí |
| EP.024 **antes** del fix | 232 px | **84 px** | no |
| EP.024 **después** | 348 px | 168 px | sí |

Dos cambios: el ancla se **envuelve por ancho**, y el paso de línea se calcula sobre **la tinta
real** (con el avance fijo `asize * 0.86` la tilde de `QUÉ` chocaba con la pata de la `R`).

### 3. Fuentes re-verificadas ANTES de grabar — 2 errores encontrados

Instrucción de Andrés: *«siempre revisa las fuentes porque después de que grabe te das cuenta que
no era como estaba en el guion»*. Se re-abrieron las fuentes primarias pese a que el checkpoint
decía «verificadas 2026-07-28».

- **Luisiana no es «un tercio del territorio»** → 828.000 mi² sobre ~3,8 M = **~23%**.
  Corregido a «casi una cuarta parte».
- **«El 30% es la única cifra que aparece igual en el borrador y en el publicado»: falso.**
  También coinciden los cinco subordinados por jefe, «casi un tercio de un trabajador» y el
  periodo 2005-2011. Corregido a «una de las pocas cifras que sobrevivió igual».

Otras tres por precisión: «the slows» es **atribuida** a Lincoln, no cita documentada; Leeson
cumplió 3a7m desde la condena o 4a4m desde el arresto, no «cuatro y medio»; el QJE se publicó en
**nov 2019**, así que «siete años» pasó a «casi siete años».

**Confirmado textualmente en el paper publicado:** 131 empresas · 38.843 trabajadores · 1.553
ascendidos · 5.956 jefes · 2005-2011 · caída de 0,061 (Tabla III col. 2) · +30% en el
contrafactual · «casi un tercio de un trabajador» sobre equipos de cinco.

### 4. Artifact del guion republicado

https://claude.ai/code/artifact/b84b68c3-97d0-49e2-ae28-184e8e333740 — **Andy graba leyendo el
Artifact, no el `.html`.** El publicado llevaba desde el 07-28 a las 11:59 desincronizado de un
`.html` editado a las 15:47: le faltaba la muletilla ya retirada *además* de las 5 correcciones
de hoy. Regenerado desde el `.html` y republicado sobre la misma URL.

### 5. Retrospectiva y auditoría de kit aplicadas

5 aprendizajes escritos (re-verificar fuentes antes de grabar · working paper ≠ publicado ·
resincronizar el Artifact al editar un guion · probar un generador contra el caso viejo · dónde
viven las portadas de episodio en disco). `banned-patterns.json` pasó a v2 con
`applies_to_direction`: 7 patrones quedaron acotados a `escena-renderizada` porque exigían cosas
retiradas de BTQ el 2026-07-25 — **no se borraron**, MPD y CCC sí renderizan escena.

---

---

## Segunda mitad — cifras, relleno y cierre de fuentes

### 6. Las cifras van en numeral (regla nueva de Andrés)

*«Cuando hablemos de cifras coloques en número y no en letras porque es más confuso.»* **19
cifras-dato convertidas.** La razón fuerte resultó no ser la legibilidad: **en letras se escapan
de los lints**. Mi extractor de afirmaciones filtraba por dígitos y no tocó **ninguno** de los 16
bloques con la cifra escrita en palabras — y ahí adentro había un error real: «cincuenta y seis
años» sobre un libro de 1969, cuando el episodio sale en 2026. Son **57**.

Se dejan en letras las expresiones idiomáticas y los nombres de conceptos («medio siglo», «las
cinco etapas del duelo», «el uno por ciento de mejora diaria»). La prueba: ¿es un **dato**
verificable o una **forma de hablar**?

### 7. Pasada de relleno y argumentos débiles (Andrés eligió la opción 2: cortar Y sustituir)

Andrés detectó el incentivo estructural: **si el estándar de duración se mide en palabras
escritas, todo lo que alarga el texto sin alargar el audio empuja hacia la meta gratis.**

**Cortadas 355 palabras** de relleno: el mecanismo del Principio enunciado 5 veces seguidas, la
recepción del libro 4 veces, la invisibilidad del daño 3 veces (quedó solo el REMATE, que era el
bueno), y las muletillas de tribuna — incluida «ahora, seamos rigurosos, porque este pódcast
promete evidencia», que **anunciaba rigor a tres líneas de dos cifras sin verificar**.

**Añadidas 270 palabras** verbatim del paper: la robustez del **equipo distinto** (mata la
objeción «¿y si el equipo ya venía flojo?»), el **32% exacto** con el percentil 50→67, y el
**hallazgo del ranking** (descontadas las ventas, ser el nº 1 del equipo sigue prediciendo el
ascenso). Y se corrigió un sobre-alcance: el guion explicaba *por qué* la colaboración predice un
buen jefe cuando el paper dice «**we cannot pinpoint the exact channel**».

**El hallazgo metodológico:** los 7 argumentos débiles caían **todos** en los segmentos apoyados
en fuentes secundarias; **cero** en los dos construidos sobre el paper verificado. La densidad de
retórica es un detector de huecos de verificación.

### 8. Ejemplos inventados atribuidos a Peter

Los 4 ejemplos de «incompetencia creativa» iban como *«la solución que Peter propone»*: **2 no
existen en ninguna fuente** y **1 era anacrónico** (tipo de letra de los correos, en un libro de
1969). Reemplazados por los documentados: parquear en el puesto del jefe, dejar los cajones
abiertos, saltarse el café oficial, vestirse con un gusto apenas cuestionable.

### 9. Barings cerrado — y un «más» que sobraba

Andrés propuso publicar un rango («entre 827 y 830 millones») para no comprometerse. **Un intento
dirigido más cerró el dato en fuente institucional:** *Bank Underground*, el blog del personal del
**Banco de Inglaterra** — «Leeson hid the losses, which, in the end, reached £827 million —
**twice** the firm's capital». Sin hedge.

Y destapó un error que el hedge habría enterrado: el guion decía «**más** del doble del capital» y
la fuente dice *twice*. Corregido.

**EP.024 ya no tiene ninguna cifra sin verificar.** Único hueco declarado: el libro de Peter, que
Andrés confirmó que **no consiguió** — está explícito en el bloque de Fuentes, con la lista de qué
elementos vienen de fuentes secundarias.

---

## Where We Paused

**Última acción:** cierre de sesión — retrospectiva, auditoría de kit y handoff.
**Siguiente acción:** después de las 21:00, el deep link de MPD T2·E1 (punto 1 de Next Steps).
**Bloqueantes:** EP.024 depende de que Andrés grabe; el deep link depende de que MPD publique.

---

## Files to Read First

- `btq-production/pipeline-state-ep024.md` — estado del episodio + el registro completo de la
  re-verificación de fuentes y la trampa del PDF de NBER
- `btq-production/launch-assets/EP024-peter-guion.html` — el guion corregido
- `.claude/skills/episode-launch/docs/brand-constants.md` — la nota de reconciliación del
  generador con la fórmula invertida, y dónde va cada tipo de asset en disco

---

## Next Steps

**Hoy, después de las 21:00 (MPD T2·E1):**

1. **Deep link del episodio** en `mrputridsden-production/episodios/ep006-metadata.md` — va a
   **dos** sitios (el bloque plano y el HTML). ⚠️ Los posts de **Facebook ya programados** llevan
   el link del show y se editan **en el programador, no en el repo**.
2. **Re-pegar la descripción en Spotify** para que salga el link de YouTube (el archivo y lo
   publicado dejaron de coincidir al agregar el canal). Misma pasada que el punto 1.

**BTQ EP.024 — bloqueado en la grabación:**

3. **Grabar.** No hay nada en `E:\Podcast\BTQ\EP 24\` salvo el artwork. Dejar **3 s de silencio**
   en cabeza y cola (en EP.023 quedaron 0,59 s) + 30 s de room tone.
4. **Al transcribir, medir el factor real del esqueleto D (trenzado)** y anotarlo en la tabla de
   esqueletos de `guion-style-btq.md`. No tiene precedente medido: el ×1,134 usado sale de
   EP.023, que es esqueleto B. Si D expande como los de segmentos separados, el episodio se va a
   47-53 min, fuera del estándar.
5. **Quote cards** — se componen contra la transcripción real, nunca contra el guion.
6. **Artículo `/episodios/por-que-su-mejor-empleado-se-vuelve-un-mal-jefe` + su `og:image`.**
   Va antes del plan social (los posts de LinkedIn se cortan de él) y se despliega con el episodio.

**Decisiones abiertas de Andrés:**

7. **El checklist de `brand-constants.md` pide «exactamente UN elemento en `#FF3D00`», pero
   `portada-ep-compose.py` siempre dibuja DOS** (`EP.NN` en la cabecera + la última palabra del
   ancla) — en todos los episodios, no solo EP.024. O se corrige el checklist o se corrige el
   script; no lo decidí yo.
8. **El favicon del Artifact de EP.024 quedó en 🪜.** El original no es recuperable del HTML
   servido (es metadata del artifact). Si era otro, decirlo y se devuelve.
9. **«dos canadienses»**, primera línea de EP.024: se dejó **sin cambiar**. Raymond Hull nació en
   Inglaterra en 1919 pero era dramaturgo canadiense, así que la frase se sostiene. Anotado por
   si alguien la cuestiona.

**Vienen de antes, sin decidir:** las 4 quote cards de MPD son 16:9 (rinden mal en feed de IG);
nota de contenido / línea de apoyo para los días 2 y 3 de MPD; clip de audio de 30-60 s de MPD;
el 16:9 de MPD anuncia Spotify/Apple/Amazon pero no YouTube; el punto y el handle del canal de
YouTube de MPD; «Martes de misterio»; episodio de leyendas venezolanas; y el español neutro en
MPD (aplazado a la semana del **2026-08-03**, marcador vivo en `guion-style-mpd.md` ~línea 10).

---

## Notes / Gotchas

- **Reprocesos por procedencia hoy: 1.** Corregí el guion, lo commiteé y lo di por hecho sin abrir
  el **Artifact publicado**, que es lo que Andrés realmente lee. Estaba más viejo todavía. Lo cacé
  yo, no él, pero el patrón es el de siempre: declarar completo sin abrir el artefacto que el
  usuario consume.
- **El PDF que baja primero de NBER es el borrador de 2018** (214 empresas, 53.035 trabajadores).
  Usarlo habría puesto **las ocho cifras** del segmento 4 mal. El publicado está en la copia de la
  autora (`danielle.li/assets/docs/`), guardado en `E:\AI\outputs\BTQ-EP024\qje2019-publicado.pdf`.
- **Mi primer arreglo del compositor reventaba `HAWTHORNE`** — perdió el chequeo de ancho y el
  ancla se salía del cuadro. Solo apareció al probarlo con un título de la **fórmula vieja**.
  Regla nueva en `CLAUDE.md` § Debugging.
- **Un script de comparación dio un falso negativo** del «30%» porque el PDF trae un espacio
  Unicode y el patrón literal `30 percent` no matcheaba. Se destapó al chocar contra un escaneo
  anterior. Instrumento, no dato.
- **El parche del compositor NO es idéntico píxel a píxel** para títulos cortos: los tamaños de
  fuente vuelven iguales (420/216/152 px) pero el interlineado queda más ceñido — 220.013 px
  distintos, medido con `ImageChops`. Ningún asset publicado cambia.
- **Marcadores pendientes:** los `[VERIFICAR]` que quedan son de **EP.018 y EP.019**, episodios ya
  publicados, más menciones narrativas en documentos de reglas. **EP.024 no tiene ninguno.**
- **Machine-bound:** todo lo de `E:\` (portadas, audio, PDFs) es **solo del desktop**. En el
  portátil los assets se **regeneran**, no se copian — los composers son deterministas.

---

## Questions to Answer

- ¿Se corrige el checklist o el script por lo del doble `#FF3D00`? (punto 7)
- ¿El favicon del Artifact era otro? (punto 8)
- ¿EP.024 mantiene salida en domingo (**2026-08-02**)? Es inferencia mía desde la nota «se
  despliega el domingo»; **no verificado** contra una fecha publicada.

> **RESUELTO en la segunda mitad:** los £827 millones y la comparación con el capital quedaron
> confirmados en *Bank Underground* (Banco de Inglaterra). Ya no son pregunta abierta.

**Nuevo, para cuando se transcriba EP.024:** al medir el factor de expansión del esqueleto D,
**no compararlo contra el 1,134 de EP.023 sin más.** EP.024 cambió dos variables a la vez —
esqueleto nuevo *y* cifras en numeral, que reducen las palabras escritas sin tocar las habladas.
Atribuirle todo el cambio al esqueleto sería el error de «cifra compuesta» ya documentado.
