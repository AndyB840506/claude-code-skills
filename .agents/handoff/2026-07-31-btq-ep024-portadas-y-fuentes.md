# Handoff: BTQ EP.024 — portadas v4 y re-verificación de fuentes

**Date:** 2026-07-31 (viernes)
**Machine:** desktop (E:\)
**Status:** In progress — EP.024 tiene portadas y guion corregido; **falta grabar**.
MPD T2·E1 sale hoy a las **21:00**.

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
- ¿Persigo en fuente primaria los **£827 millones** exactos y el «más del doble del capital del
  banco»? Britannica dice «roughly £830 million». Están en el guion sin verificar.
- ¿EP.024 mantiene salida en domingo (**2026-08-02**)? Es inferencia mía desde la nota «se
  despliega el domingo»; **no verificado** contra una fecha publicada.
