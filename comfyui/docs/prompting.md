# Prompting Guide (per model family)

> Standalone copy exists at `imagen-a-prompt/docs/prompt-formats.md` (user-requested, no cross-deps) — when a model's rules change, update BOTH files.

Claude may draft/refine SFW prompts on request (backgrounds, environments, concepts, poses, lighting). Explicit prompts are user-side; the structures below transfer.

## Z-Image / Qwen-encoder models — natural language
Formula: **subject + action + setting + lighting + camera/style**, as full sentences.
- Good: `A boxer resting in a dim locker room, steam in the air, single overhead lamp, 35mm photo, shallow depth of field`
- Weak: `boxer, locker room, dramatic, 4k, masterpiece` (keyword-stacking wastes this encoder)
- Useful vocabulary: camera (35mm, wide-angle, drone shot, close-up), lighting (golden hour, overcast, neon, rim light), medium (photo, oil painting, 3D render, cel-shaded).

## Illustrious / anime SDXL checkpoints — booru tags
Comma-separated tags, rough priority order:
`<count> → appearance → pose/action → setting → lighting/composition → quality`
- Example: `1girl, red hair, ponytail, boxing gloves, fighting stance, boxing ring, dramatic lighting, from below, masterpiece, best quality`
- Tags must be REAL Danbooru tags — invented phrases do little. Look up exact tags on the Danbooru tag wiki.
- Weight syntax: `(tag:1.3)` boosts, `(tag:0.7)` dampens. Beyond ~1.5 causes artifacts.
- Negative prompt staples: `lowres, bad anatomy, bad hands, extra fingers, watermark, signature`
- Check each checkpoint's Civitai page: many specify required quality-tag prefixes and a recommended negative.

## Z-Image Turbo: la trampa de la negación (aprendido 2026-07-11, BTQ EP.021)

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
- **Flat in = flat out:** pedir "flat colors / cel shading plano" produce imagen sin
  sombras aunque la escena tenga fuentes de luz. Para covers dramáticos describir la
  iluminación SIEMPRE (rim light, lado en sombra, sombra proyectada, oclusión) — para
  2D con drama, la referencia útil es "cinematic style of The Simpsons Movie (2007)".
- Para retoques localizados usar VAEEncode + **SetLatentNoiseMask** (img2img enmascarado);
  `VAEEncodeForInpaint` con denoise <1 deja parches grises en modelos no-inpaint. Si hay
  que ELIMINAR estructura (no solo retocarla), destruirla primero (blur pesado en PIL) y
  luego re-texturizar enmascarado a denoise ~0.4 — a denoise medio la estructura
  subyacente sobrevive y se repinta más nítida.
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

## Chroma (T5-flan encoder) — prompts DENSOS o look genérico (aprendido 2026-07-11)

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
1. **Fix the seed** while developing a prompt — image changes only where the prompt changed. Learn cause/effect.
2. Change ONE thing per run.
3. Prompt done → switch seed to random for variations.
4. Recurring defect → name it in the negative prompt rather than piling positives.
5. Composition right / details wrong → raise steps or try another sampler before rewriting the prompt.

## In ComfyUI
- Seed control lives on the KSampler node (`control_after_generate`: fixed/increment/randomize).
- CFG: how strictly the model follows the prompt. Baselines: SDXL ~7; turbo/distilled models need LOW cfg (1–3) and few steps — check the template's defaults before "fixing" them.
