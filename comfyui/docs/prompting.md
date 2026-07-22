# Prompting Guide (per model family)

> Standalone copy exists at `imagen-a-prompt/docs/prompt-formats.md` (user-requested, no cross-deps) — when a model's rules change, update BOTH files.

Claude may draft/refine SFW prompts on request (backgrounds, environments, concepts, poses, lighting). Explicit prompts are user-side; the structures below transfer.

## Z-Image / Qwen-encoder models — natural language
Formula: **subject + action + setting + lighting + camera/style**, as full sentences.
- Good: `A boxer resting in a dim locker room, steam in the air, single overhead lamp, 35mm photo, shallow depth of field`
- Weak: `boxer, locker room, dramatic, 4k, masterpiece` (keyword-stacking wastes this encoder)
- Useful vocabulary: camera (35mm, wide-angle, drone shot, close-up), lighting (golden hour, overcast, neon, rim light), medium (photo, oil painting, 3D render, cel-shaded).

## SDXL fotorreal (bigASP) — natural language, NOT booru tags
Same formula as Z-Image (subject + action + setting + lighting + camera/style), 1-2 quality tags at the end if the checkpoint wants them. Negative acts (classic SDXL) — use it for anti-illustration too when output looks painted instead of photoreal (`illustration, anime, cartoon, drawing, painting, 3d render, cgi, plastic skin`). Settings are reasonable SDXL defaults, not a verified official recipe — check bigASP_v2's Civitai page: `cfg ~6 · steps 30 · dpmpp_2m_sde · karras · 1024×1024`. Template: `comfyui/templates/sdxl-bigasp-photoreal-api.json`.

## Illustrious / anime SDXL checkpoints — booru tags
Comma-separated tags, rough priority order:
`<count> → appearance → pose/action → setting → lighting/composition → quality`
- Example: `1girl, red hair, ponytail, boxing gloves, fighting stance, boxing ring, dramatic lighting, from below, masterpiece, best quality`
- Tags must be REAL Danbooru tags — invented phrases do little. Look up exact tags on the Danbooru tag wiki.
- Weight syntax: `(tag:1.3)` boosts, `(tag:0.7)` dampens. Beyond ~1.5 causes artifacts.
- Negative prompt staples: `lowres, bad anatomy, bad hands, extra fingers, watermark, signature`
- Check each checkpoint's Civitai page: many specify required quality-tag prefixes and a recommended negative.
- Template: `comfyui/templates/illustrious-sdxl-booru-api.json` (Illustrious-XL-v2.0 — stylized/anime, will NOT look photoreal regardless of prompt; for that use the bigASP template above).

## Z-Image Turbo: la trampa de la negación (aprendido 2026-07-11, BTQ EP.021)

Template: `comfyui/templates/zimage-txt2img-api.json`.

- **A CFG 1.0 el prompt negativo NO actúa** (matemáticamente apagado). La comunidad de
  Civitai los pone igual (ej. "blurry ugly bad") pero son decorativos. Subir CFG degrada
  el modelo turbo — no es la solución.
- **"DO NOT render X" en el positivo tiende a EVOCAR X**, no a prohibirlo. Y pedir un
  concepto que CONTIENE el elemento prohibido lo garantiza (ej.: pedir "broadcast
  test-card geometry" y prohibir círculos = salen círculos, la carta de ajuste ES
  círculos concéntricos).
- **Regla:** el control es 100% del prompt positivo. No nombrar el concepto problemático
  en ninguna forma; describir SOLO lo que sí se quiere en su lugar ("plain dark smoke and
  golden dust" en vez de "test-card background, no rings").
- Settings comunidad (Civitai, modelo 2168935): cfg=1, steps=8-9, sampler euler o
  res_multistep, scheduler simple.
- **Personajes conocidos: declarar proporciones canon explícitas** ("a tall adult man,
  his head is about one quarter of his total height, long legs") — sin eso el render
  tiende a chibi/cabezón (BTQ EP.021, Homero).
- **Personas genéricas (sin referente conocido): declarar rasgos étnicos explícitos en
  el positivo** (aprendido 2026-07-21, BTQ EP.023) — sin esa descripción, Z-Image Turbo
  cae por defecto en un hombre de rasgos asiáticos independientemente del contexto de la
  escena (agente de call center genérico, sin ninguna pista étnica en el prompt). No es
  un error del render, es el sesgo por defecto del modelo ante un prompt neutro. Regla:
  cualquier escena con una persona SIN referente conocido debe declarar explícitamente
  rasgos/etnia en el positivo (ej. "a Latino man in his 30s", "a Black woman in her 40s",
  "a white man with a beard") — no dejarlo implícito ni asumir que "persona genérica" el
  modelo lo va a variar solo.
- **Flat in = flat out:** pedir "flat colors / cel shading plano" produce imagen sin
  sombras aunque la escena tenga fuentes de luz. Para covers dramáticos describir la
  iluminación SIEMPRE (rim light, lado en sombra, sombra proyectada, oclusión) — para
  2D con drama, la referencia útil es "cinematic style of The Simpsons Movie (2007)".
- Para retoques localizados usar VAEEncode + **SetLatentNoiseMask** (img2img enmascarado);
  `VAEEncodeForInpaint` con denoise <1 deja parches grises en modelos no-inpaint. Si hay
  que ELIMINAR estructura (no solo retocarla), destruirla primero (blur pesado en PIL) y
  luego re-texturizar enmascarado a denoise ~0.4 — a denoise medio la estructura
  subyacente sobrevive y se repinta más nítida.
- **Conceptos de "luz partida" (mitad iluminada / mitad en sombra de la misma persona u
  objeto) necesitan ángulo frontal, no 3/4** (aprendido 2026-07-21, BTQ EP.023): un
  ángulo de tres cuartos solo muestra un lado de la cara/cuerpo a cámara, así que no hay
  línea de división visible aunque el prompt la pida explícitamente. Fix: pedir "facing
  the camera directly, frontal angle" + describir la línea de luz como "hard-edged...
  sharp and straight, not a soft gradient" en vez de "rim light" (que sugiere solo un
  borde, no una mitad completa).
- **Un adjetivo de color cerca de la luz/fondo tiñe todo el fondo**, aunque se pida
  "void black" en otra parte del prompt (ej. "faint red glow dissolving into shadow" →
  fondo completo rojo, no negro puro; aprendido 2026-07-13, BTQ EP.021 CARD1 en el
  portátil). Si hay una fuente de luz de color en la escena, declarar explícitamente que
  el resto del fondo se apaga a negro puro: "background fades to pure black, no colored
  wash" — no basta con pedir "void black" una sola vez al principio del prompt.
- **Escenas de un solo objeto en vacío pueden alucinar objetos extra** sin que se pidan
  (ej. una figurita apareció sola junto a una vela; aprendido 2026-07-13, BTQ EP.021
  CARD3). Para composiciones de un solo objeto, agregar "alone, nothing else in frame"
  suprime el objeto extra.
- **Post-proceso PIL (composicion, scrims, grading, aprobacion en miniatura): se movio a `artwork-composition.md`.** Este archivo cubre que pedirle al MODELO; el otro, que
  hacer despues con lo que devolvio.
- **Negar rasgos faciales en el positivo puede EMPEORAR el resultado, no solo no
  ayudar** (segunda instancia confirmada, aprendido 2026-07-17, MPD EP.005 Q3): pedir
  explícitamente "her face never visible", "no nose or lips visible" en el prompt
  positivo de una cantante de perfil produjo una cara MÁS iluminada y detallada que el
  intento anterior sin esa negación — la trampa de la negación (ver arriba) también
  aplica a rasgos anatómicos, no solo a objetos/conceptos. **Regla que sí funcionó:**
  en vez de negar el rasgo, describir la posición de la fuente de luz y el ángulo de la
  cabeza que produce el resultado deseado ("light source directly behind her, head
  turned away from camera, hair falling over where her face would be") — control
  geométrico/lumínico positivo, no una lista de prohibiciones.
- **Consistencia visual de un sujeto recurrente a través de varias generaciones
  separadas** (aprendido 2026-07-17, MPD EP.005): al generar portada + múltiples quote
  cards que retratan a la MISMA persona (real o de marca) en generaciones
  independientes, cada prompt nuevo debe reusar literalmente los descriptores físicos
  ya aprobados en la primera generación (corte de pelo, color, complexión) — no
  redescribir "a la memoria" cada vez. En EP.005, la segunda tarjeta con la misma
  cantante quedó con pelo largo ondulado tipo "cantante de jazz" en vez del corte bob
  ya establecido en la portada, porque el prompt nuevo no copió la descripción exacta
  del primero.
- **Para ELIMINAR un elemento hay que borrar TODAS sus palabras, incluidos los sinónimos
  atmosféricos — y verificarlo programáticamente antes de encolar** (aprendido 2026-07-22,
  portada MPD Temporada 2, costó 4 generaciones). Secuencia real: (1) el prompt pedía humo
  saliendo del puro y el modelo se lo puso al VASO; (2) al reescribirlo con "there is no smoke
  anywhere near the glass" el humo siguió saliendo del vaso — la trampa de la negación otra vez;
  (3) al quitar esa frase el humo del puro desapareció, pero seguían apareciendo plumas porque el
  prompt aún decía **"thick haze hangs in the air"**; (4) recién al eliminar también `haze` quedó
  limpio. **Regla:** grepear el prompt por el concepto Y sus sinónimos (`smoke|haze|mist|fog|vapour`)
  y ABORTAR el POST si alguno aparece — no basta con quitar la mención obvia. Corolario de
  atribución: cuando dos objetos cercanos compiten por un efecto (humo, luz, reflejo), amarrar el
  efecto al objeto en la MISMA oración ("from the glowing tip of that cigar...") y verificar con un
  crop ampliado de la zona antes de dar la imagen por buena — a tamaño completo el error no se ve.

## Chroma (T5-flan encoder) — prompts DENSOS o look genérico (aprendido 2026-07-11)

Template: `comfyui/templates/chroma-txt2img-api.json` — usa `ModelSamplingAuraFlow`
(NO `ModelSamplingSD3`, ese mismatch produjo ruido puro pese a "success" — ver
`docs/troubleshooting.md`).

- **Chroma castiga prompts cortos**: cada bloque no descrito se rellena con "promedio AI"
  (piel plástica, render genérico) — fue la causa raíz del "chafitas" del usuario, no la
  receta. A/B mismo-seed: receta oficial (flan+padding 1) vs sustituta = mejora marginal;
  prompt denso vs corto = la diferencia grande.
- Estructura por párrafo: sujeto detallado → encuadre/pose → ropa/materiales →
  cámara/lente → luz → textura de piel → entorno (2-3 detalles). Plantillas rellenables
  (real / animado / 3D) viven como MarkdownNote en el workflow "Chroma Personajes Pro".
- **A diferencia de Z-Image turbo, aquí el negativo SÍ actúa** (cfg 3.8 real). Úsalo de
  cortafuegos de estilo: `photograph, realistic skin` para forzar 2D; `anime, illustration`
  para forzar fotorreal.
- Settings oficiales (del workflow del creador, no de memoria): euler +
  BetaSamplingScheduler 26 steps (alpha/beta 0.45), shift 1.0, cfg 3.8, base 1152×1152.

## Iteration method (applies to both)
0. **Mantener una lista de requisitos YA satisfechos y verificarlos TODOS en cada iteración**, no
   solo el que se está arreglando (aprendido 2026-07-22, portada MPD T2, 19 generaciones). En
   Z-Image, reescribir una frase del prompt desplaza otros atributos aunque el seed no cambie —
   cada arreglo rompió algo ya logrado: se arregló el humo y el vaso perdió la calavera moldeada;
   se sacó la butaca de la chimenea y aparecieron dos calaveras decorativas en la repisa. **Antes de
   presentar una iteración, recorrer la lista completa** (sujeto, atributos del sujeto, composición,
   luz, paleta, elementos prohibidos) y reportar honestamente qué se ganó Y qué se perdió — nunca
   presentar como "arreglado" mirando solo el cambio nuevo.
0.b **Verificar relaciones entre objetos con un crop ampliado, no a tamaño completo.** Los errores
   de atribución (de qué objeto sale el humo/la luz/el reflejo) son invisibles en la imagen entera
   y saltan al ampliar. En la sesión citada el usuario detectó que el humo salía del VASO y no del
   puro; a tamaño completo había pasado desapercibido dos veces.
0.c **Los gates de palabras prohibidas van con límite de palabra (`\bword\b`), no subcadena** —
   `unmistakable` contiene `mist` y abortó un envío correcto (mismo día).
1. **Fix the seed** while developing a prompt — image changes only where the prompt changed. Learn cause/effect.
2. Change ONE thing per run.
3. Prompt done → switch seed to random for variations.
4. Recurring defect → name it in the negative prompt rather than piling positives.
5. Composition right / details wrong → raise steps or try another sampler before rewriting the prompt.

## In ComfyUI
- Seed control lives on the KSampler node (`control_after_generate`: fixed/increment/randomize).
- CFG: how strictly the model follows the prompt. Baselines: SDXL ~7; turbo/distilled models need LOW cfg (1–3) and few steps — check the template's defaults before "fixing" them.
