# Handoff: BTQ Temporada 3 — relanzamiento con Alejandro

**Date:** 2026-09-26
**Machine:** escritorio (E:\)
**Status:** Dirección de T3 decidida y registrada; logo elegido y pendiente del visto bueno de
Alejandro. Ningún episodio de T3 grabado todavía.

---

## What We Accomplished This Session

- **BTQ pasa a la Temporada 3 con Alejandro como co-host.** Fuentes: la minuta de la reunión
  que pegó Andy y sus decisiones en esta sesión. Todo quedó en `btq-production/roadmap-btq.md`
  § Temporada 3:
  - **Sin guion.** Conversación libre con una hoja de ruta por episodio, como en MPD.
  - **Vuelta a los temas originales de EP.01–09**, todos de la industria BPO, verificados
    contra el RSS.
  - **Tono** conversacional, con anécdotas y referencias. ~45 min. Invitados a futuro.
  - **Numeración:** la T3 **reinicia en EP.01** (season 3, episode 1 en Spotify for Creators).
  - **EP.028 Ley de Little retirada:** se cae la promesa del teaser de EP.027.
  - **"Buenas y santas"** se reemplaza por algo más fresco (por definir).
- **Reglas de T2 marcadas donde viven, no borradas:**
  - En `roadmap-btq.md`: la rotación 3+1 y la estrategia editorial quedan superadas, el giro de
    alcance del 07-25 queda revertido, y EP.028–031 pasan a registro histórico.
  - `guion-style-btq.md` **no se aplica a T3**; las reglas de host único quedan marcadas [SOLO T2].
  - `brand-constants.md` queda EN REVISIÓN.
  - La fila 028 de `linkedin-liderazgo/docs/temas-btq.md` quedó marcada como nunca producida.
- **Metadata del RSS:** hay 4 errores de season/episode anotados en el roadmap.
  **EP.23 Hawthorne está marcado como S3E1** y choca con el EP.01 de T3.
- **Paquete para Alejandro:**
  - 6 transcripts limpios (EP.016, 018–022, elegidos por contenido de call center) en
    `E:\Podcast\BTQ\T3-paquete-alejandro\`.
  - Carpeta de Drive creada **vacía**, id `1tRz4IiUKhpUlpC_92NK3pD8WbS1SMabN`. Andy tiene que
    arrastrar los archivos.
- **Logo:** se generaron 3 conceptos con Z-Image (A: Q que habla, B: carnet, C: en vivo).
  - **Andy eligió el C, variante v1** ("THE" pequeño junto a QUEUE).
  - El generador escribió mal el texto, así que se recompuso con PIL en Arial Black:
    `E:\AI\outputs\BTQ-T3-logo-C-final-v1-the-apilado.png` (1024 px).
  - Andy ya se lo mandó a Alejandro.
- **Música de T3:** lista, según Andy (no la he visto).
- **Retrospectiva:**
  - Regla nueva en `comfyui/docs/prompting.md`: el texto de un logo se compone con PIL desde el
    primer intento.
  - 2 memorias de referencia nuevas: feeds RSS de BTQ y MPD, y que el conector de Drive no sube
    archivos locales.
  - Se corrigió `btq_production_state.md`, que llevaba 3 meses desactualizada (se había quedado
    en EP.016).
- **Commits:** `c8404f4`, `6166e5a`, `631fabb`, `fcd9722`, más los del cierre. Todos pusheados.

## Where We Paused

**Last action:** cierre de sesión.
**Next action:** esperar el visto bueno de Alejandro al logo, y su foto y bio para la página.
**Blockers:** foto y bio de Alejandro (bloquean la página); su visto bueno al logo (bloquea
pasarlo a 3000 px o a vector).

## Next Steps (quién actúa)

1. **Andy:** arrastrar los 6 `.txt` de `E:\Podcast\BTQ\T3-paquete-alejandro\` a la carpeta de
   Drive y compartirla con Alejandro.
2. **Andy, en Spotify for Creators:** corregir EP.23 (S3E1 → S2E23), EP.22 (ep 19 → 22) y EP.16
   (sin season → S2E16). **Hay que hacerlo antes de publicar el EP.01 de T3.**
3. **Andy + Alejandro:** confirmar el roadmap. El borrador de 8 temas **solo está en la
   conversación, no en el repo**:
   - 01 La industria BPO en general
   - 02 Mi primer día en un call center
   - 03 Ser bilingüe en el BPO
   - 04 La IA en el call center
   - 05 De agente a líder
   - 06 Mitos del call center
   - 07 Llamadas que no se olvidan
   - 08 Por qué la gente se va
4. **Andy:** elegir el saludo nuevo. Propuesta favorita: "Gracias por comunicarse con Behind the
   Queue, le habla Andrés… y Alejandro. ¿Con quién tengo el gusto?"
5. **Tras el visto bueno de Alejandro:** pasar el logo a 3000×3000 (RealESRGAN) o a vector.
   Considerar "AL AIRE" en vez de "EN VIVO" si molesta que diga en vivo algo grabado.
6. **Cuando lleguen la foto y la bio:** refresh de la página, que pasa de autor único a dos
   hosts (hero con los dos, "Quiénes somos", archivo por temporada). Fotos reales, no IA.
7. **Checkpoint del miércoles antes de la grabación del sábado:** hoja de ruta del EP.01. La
   fecha exacta no está en la minuta.

## Notes / Gotchas

- `start.ps1` de continuity salió con **exit 128** al arrancar, aunque el pull y la restauración
  de memoria terminaron bien. **No se investigó.**
- `start.ps1` avisa de **memoria repartida en 3 slugs**: sigue viva la de
  `C--Users-andre-repos-kit-skill-creator` (104 archivos).
- `linkedin-liderazgo/docs/temas-btq.md` línea 3 apunta a `repos\kit-skill-creator\...`, un
  workspace retirado el 2026-09-22. Es una ruta vieja que ya estaba ahí; no se tocó.
- EP.01–09 no tienen transcript (época TurboScribe). Si Alejandro los necesita, los audios
  están en el RSS; estimar el tiempo de WhisperX antes de lanzar.
- ComfyUI quedó corriendo en el escritorio (PID 28944).

## Files to Read First

- `btq-production/roadmap-btq.md` § Temporada 3 (arriba de la tabla)
- Memoria `project_btq_t3_alejandro.md`
