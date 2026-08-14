# Handoff: MPD — decisión de rotación de expedientes + EP.03 (Crowley) Stage A completo

**Date:** 2026-08-14
**Machine:** desktop (E:\ existe, verificado; ComfyUI corrió y se cerró en esta sesión)
**Status:** Complete — Stage A de EP.03 cerrado, listo para grabar

---

## What We Accomplished This Session

**1. Decisión pendiente de MPD resuelta:** cómo escala el sitio (mrputridsden.com) al
llegar cada expediente nuevo de T2. Andrés decidió **acumular indefinidamente** — cada
expediente suma su propia sección `.case` completa, sin rotación ni archivado
automático. `episode-pipeline/workflows/04-grid-rotation.md` quedó separado: BTQ
mantiene la rotación de grid original, MPD tiene su propia sección "MPD — acumulación de
Expedientes" con el procedimiento paso a paso para el próximo lanzamiento.

**2. MPD EP.03 (T2·E3) — Stage A completo, de cero a "guion listo":**
- Tema: **Crowley y su huella en la música** — candidato ya decidido en
  `banco-expedientes.md`, confirmado con Andrés.
- Verificados con fuente antes de escribir: "Mr. Crowley" (Ozzy, 1980), "Quicksand"
  (Bowie, 1971), rostro de Crowley en Sgt. Pepper's (1967) — los 3 leads sin verificar
  del banco. Investigación adicional: Abadía de Thelema / muerte de Raoul Loveday (1923,
  origen real del apodo "el más malvado del mundo"), origen del apodo "La Bestia" (se lo
  puso su madre, no él), Batalla de Blythe Road (expulsión de la Golden Dawn, 1900, con
  W.B. Yeats), y el mito FALSO de que Black Sabbath viene de un texto de Crowley
  (desmentido con fuente — viene de una película de Boris Karloff, 1963).
- **Experimento de estilo de UN solo episodio** (decidido con Andrés): Tales from the
  Crypt — ritmo de suspenso tipo horror-anthology, Andrés más cómplice en
  bienvenida/cierre, dos guiños de cuarta pared, y el cierre rompe a propósito la regla
  de "nunca resolver" con un giro irónico (la madre le regaló el apodo sin querer → el
  rock le regaló la inmortalidad sin querer). Documentado en memoria
  `project_mpd_ep03_crypt_experiment` — si no funciona al escuchar la grabación,
  EP.02/EP.006 siguen siendo el molde para EP.04.
- Guion completo: `mrputridsden-production/scripts/EP03-la-bestia-que-el-rock-volvio-inmortal.html`
  — 4.482 palabras narradas (dentro de ±15% del target ~5.150). Publicado como Artifact:
  https://claude.ai/code/artifact/38b0c9d4-fe4e-4889-b149-080bd2948934
- **Conector al próximo expediente SÍ se anuncia:** "Paul is Dead" confirmado como
  Expediente 04 (`banco-expedientes.md` #3 actualizado — ya tiene ángulo verificado,
  Fred LaBour/Michigan Daily 1969).
- Artwork: concepto aprobado tras 3 iteraciones en ComfyUI local (Z-Image Turbo).
  Escena: estudio fijo "La Guarida" + marco ovalado con foto ilegible + vinilos reales.
  v1 tuvo un patrón de diana vetado colado en un sleeve de vinilo; v2 lo corrigió pero
  perdió la identidad de "vinilo"; v3 recuperó ambos. Grading azul variante E aplicado y
  aprobado. Detalle completo: `mrputridsden-production/episodios/temporada-2/artwork-ep03.md`.
  Producción final (upscale 3000×3000, tipografía, quote cards) diferida a más cerca del
  lanzamiento — no bloqueante.
- `pipeline-state-ep03.md` / `pipeline-audit-ep03.md` creados. Roadmap actualizado a
  "guion listo".

**3. Retrospectiva aplicada (4 fixes a skills, ver commit `877b3ae`):**
1. `episode-pipeline/workflows/00-roadmap.md` — checkpoint obligatorio: "¿el cierre
   anuncia el próximo expediente?" es decisión de Andrés, no default del asistente
   (mordió en esta sesión: el primer borrador del cierre de EP.03 decidió "no anunciar"
   sin preguntar).
2. Mismo archivo — MPD T2 debe aplicar `night_grade` al render de validación ANTES de
   presentarlo para aprobación de concepto, no solo en producción final.
3. `comfyui/docs/prompting.md` — técnica nueva: describir el deterioro FÍSICO de una
   foto (manchas de agua, decoloración) para volver un rostro ilegible, cuando el
   control de ángulo/luz no aplica.
4. `comfyui/docs/artwork-composition.md` — al purgar un motivo vetado de un objeto, no
   generalizarlo hasta borrarle su identidad (describir sus rasgos reales que no
   incluyen el motivo, no "superficie lisa sin nada").

**Auditoría de skills:** limpia — 28 skills, 0 colisiones de triggers, 0 archivos de
skill nuevos ni `SKILL.md` tocados esta sesión.

---

## Where We Paused

**Last action:** retrospectiva aplicada y pusheada (commit `877b3ae`), ComfyUI cerrado.
**Next action:** Andrés graba EP.03. Cuando tenga el audio, retomar el pipeline
("corre el pipeline para EP.03") → arranca directo en transcripción
(`pipeline-state-ep03.md` dice `stage_a: complete, stage_b: pending`).
**Blockers:** ninguno — todo lo que dependía de decisión de Andrés quedó resuelto en
esta sesión (rotación del sitio, estilo del episodio, conector, artwork).

---

## Files to Read First

- `mrputridsden-production/pipeline-state-ep03.md` — checkpoint, arranca ahí el
  próximo `episode-pipeline`
- `mrputridsden-production/pipeline-audit-ep03.md` — bitácora completa de Stage A
- `mrputridsden-production/scripts/EP03-la-bestia-que-el-rock-volvio-inmortal.html` —
  el guion para grabar (o el Artifact para leerlo cómodo)
- `mrputridsden-production/episodios/temporada-2/artwork-ep03.md` — prompt aprobado +
  ruta de las imágenes de validación en `E:\AI\outputs\`

---

## Notes / Gotchas

- **ComfyUI quedó CERRADO al final de la sesión** (proceso detenido y verificado con
  `curl` que ya no responde en `127.0.0.1:8188`). Si la próxima sesión necesita generar
  algo (producción final del artwork de EP.03), hay que levantarlo de nuevo — ver
  `comfyui/docs/stack-reference.md` § Launch.
- **El experimento de estilo Crypt es de UN episodio.** No asumir que EP.04
  ("Paul is Dead") lo hereda automáticamente — es decisión nueva de Andrés después de
  escuchar cómo salió EP.03 grabado.
- **3 bloques `.verificar` quedaron marcados en el guion** para re-abrir fuente antes de
  grabar: la Batalla de Blythe Road (fecha/vestuario exacto), cifras exactas de Sgt.
  Pepper's (más de 70 figuras — confirmar número), y el bloque de Bowie en Los Ángeles
  1975-76 (especialmente "ver cuerpos caer" — necesita fuente primaria nombrada, hoy
  viene de un resumen de búsqueda sin abrir el artículo directo).

---

## Questions to Answer

Ninguna abierta — todas las decisiones de esta sesión (rotación, estilo, conector,
artwork) quedaron resueltas con Andrés antes de cerrar.
