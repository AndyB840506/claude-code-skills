# Handoff: localizar-es-latino + endurecimiento de la faja
**Date:** 2026-09-15 (martes)
**Machine:** laptop (D:\ — sin unidad E:, verificado con `Get-PSDrive`)
**Status:** Complete — skill entregada y funcionando; quedan confirmaciones con la cliente

---

## What We Accomplished This Session

**1. Skill nueva `localizar-es-latino`** (raíz del repo, portable a cualquier workspace).
Traducción EN → ES **neutro** para localización de videojuegos adultos (18+) de la
cliente **anna_b.th**. SKILL.md es un router de 48 líneas; todo lo demás vive en
`workflows/` y `docs/`.

**2. Herramienta publicada como Artifact:**
https://claude.ai/artifact/2f5c644NufwrLFoun8U2VD — **build v8**, capacidad `sample`.
Pegás la columna inglesa, traduce, valida y copia la columna lista para la hoja. El
código fuente es `localizar-es-latino/page/columna-es.html`: **republicar ese archivo
actualiza la misma URL**.
Lo más valioso que hace: **enmascara los tokens de juego con centinelas `⟦n⟧` antes de
mandarlos al modelo** y los restaura después, así `[CORCHETES]`, `{llaves}`, `<i>`,
`(GG)`, `%s`, `$VAR` y `\n` literal no pueden alterarse. Si el modelo pierde uno, la fila
sale marcada en rojo.

**3. Corrección de estándar de idioma a mitad de sesión.** Se había escrito "base
mexicana" y Andrés corrigió a **español NEUTRO**: *léxico neutro siempre, carácter
regional nunca*. Se reescribieron el doc de estilo, el prompt de la página y los dos
validadores. Los mexicanismos pasaron de estar **recomendados** a estar **marcados**.

**4. `~/.claude/CLAUDE.md` § Verification — puntos 7 y 8 nuevos.** Salieron de que Andrés
preguntara por qué hicieron falta 8 versiones y si había un loophole. Los dos que se
encontraron y cerraron:
- La faja se disparaba al **declarar**, así que **no afirmar nada la desactivaba**:
  "probá vos y contame" funcionaba como exención, y encima se siente más honesto.
- **Evidencia adyacente**: mostrar una verificación real de *otra cosa* (`node --check`
  limpio) junto a un arreglo sin probar, que le da al mensaje textura de verificado.
- Punto 8 = *trust, but always verify*: un cambio enviado no es un cambio aplicado.

**5. memory-audit manual** (a pedido, no por umbral): 2 fixes aplicados — ruta rota en
`episode-pipeline/SKILL.md` y `project_geo_outreach_pipeline.md` recortada de 113 a 60
líneas. **No se movió `.audit-baseline.json`** a propósito: la corrida fue manual, y
moverla retrasaría la próxima auditoría real.

**6. Retrospectiva → 4 skills actualizadas:** `verify` (regla 11: entregar sin verificar
cuenta como declarar hecho), `retrospective` (segundo conteo obligatorio: reproceso por
iteración ciega), `crear-skill` (restricciones del sandbox antes de diseñar un artifact
interactivo), `session-close` (no re-disparar memory-audit si ya corrió).

## Where We Paused

**Last action:** cierre de sesión — commit y push de todo lo anterior.
**Next action:** esperar el **lote de prueba que anna va a enviar** y correrlo por la
página v8. Ese es el primer uso con texto real del juego.
**Blockers:** **bloqueado del lado de la clienta.** No hay nada técnico pendiente: la
herramienta funciona, pero la validación de la calidad de traducción depende de que
llegue ese lote. Hasta entonces, todo lo verificado son líneas de ejemplo.

## Files to Read First

- `localizar-es-latino/SKILL.md` — router; de ahí salen todos los demás
- `localizar-es-latino/docs/estilo-es-latino.md` — el estándar de español neutro, que fue
  lo más corregido de la sesión
- `localizar-es-latino/page/columna-es.html` — la herramienta; republicar actualiza la URL
- `~/.claude/CLAUDE.md` § Verification puntos 7-8 — las reglas nuevas

## Notes / Gotchas

- **`confirm()` y `alert()` están BLOQUEADOS en el sandbox de artifacts.** Devuelven
  `false` en silencio, sin error: toda acción detrás de una confirmación nativa nunca se
  ejecuta. Fue la causa raíz de las 8 versiones — Limpiar, Retraducir y Reemplazar
  estaban los tres muertos a la vez. Guardado en
  `reference_artifacts_sin_dialogos_nativos.md`. Usar confirmación en dos toques.
- **Los checks del contrato existen dos veces** (Python en `qa_localizacion.py`, JS en la
  página) **a propósito**, como medición cruzada. Si se toca uno hay que tocar el otro;
  si no coinciden, hay un bug en alguno, no elegir el que guste.
- **El cuadro de contexto de la página entra al prompt.** Si se pega ahí texto ya
  traducido, arrastra el estilo. La página ahora avisa.
- La página tiene un **sello de build visible** arriba a la izquierda: sirve para
  descartar copias cacheadas antes de diagnosticar nada.

## Questions to Answer

1. **Para anna — el `¿` sin cerrar.** Su propio ejemplo lo escribe así (`¿cuánto más...`
   sin `?` final, porque el inglés no cierra), pero no es ortografía RAE estándar.
   Confirmarlo **una vez** y fijarlo para todo el proyecto.
2. **Para anna — vocabulario sexual neutro.** Honestamente **no existe término vulgar
   neutro** para el acto sexual ni para la vagina: toda opción fuerte está marcada
   (`coger` MX/AR, `follar` ES, `concha` Cono Sur, `panocha` MX). La skill resuelve
   reformulando, pero si ella tiene un mercado objetivo definido, eso lo cierra para todo
   el juego. Decisión de ella, no mía.
3. **Las tablas de vocabulario son criterio profesional mío, no validadas por la
   cliente.** Ajustarlas con su primer feedback real, sobre todo la fila de términos
   sexuales.
4. **Falta probar la página con un lote real — y el lote lo manda anna.** Al cerrar la
   sesión quedó pendiente de su lado: ella envía un lote de prueba para comprobar la
   traducción. Lo único verificado hasta ahora son líneas de ejemplo, así que el
   registro neutro, las tablas de vocabulario y el enmascarado de tokens siguen sin
   confirmarse contra texto de producción. **Al retomar, preguntar primero si ese lote
   ya llegó** antes de planear cualquier otra cosa sobre esta skill.
