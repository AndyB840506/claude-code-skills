# Prompting Guide (per model family)

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

## Iteration method (applies to both)
1. **Fix the seed** while developing a prompt — image changes only where the prompt changed. Learn cause/effect.
2. Change ONE thing per run.
3. Prompt done → switch seed to random for variations.
4. Recurring defect → name it in the negative prompt rather than piling positives.
5. Composition right / details wrong → raise steps or try another sampler before rewriting the prompt.

## In ComfyUI
- Seed control lives on the KSampler node (`control_after_generate`: fixed/increment/randomize).
- CFG: how strictly the model follows the prompt. Baselines: SDXL ~7; turbo/distilled models need LOW cfg (1–3) and few steps — check the template's defaults before "fixing" them.
