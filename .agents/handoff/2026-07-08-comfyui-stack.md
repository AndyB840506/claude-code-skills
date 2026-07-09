# Handoff: ComfyUI — stack local de generación de imágenes en E:\AI

**Date:** 2026-07-08
**Status:** Complete — Stage 1 instalado, verificado y documentado; Stage 2 (LoRA) planeado, no construido
**Nota:** este handoff se reconstruyó post-hoc desde los artefactos commiteados (`36baebb`) porque la sesión original no corrió su cierre — verificar contra `comfyui/SKILL.md` si algo no cuadra.

---

## What We Accomplished This Session

- **Stack completo instalado en `E:\AI` (desktop):** ComfyUI v0.27.0 portable con su propio
  Python, launcher `run_comfyui.bat`, modelos compartidos en `E:\AI\models` vía
  `extra_model_paths.yaml`, outputs en `E:\AI\outputs`. Respeta la regla de output drive
  (nada en C:\).
- **Modelos instalados y verificados:** SDXL base 1.0 (verificación SFW), set Z-Image Turbo
  bf16 (+ Qwen 3 4B text encoder + VAE; en 12 GB VRAM offloadea parcial a RAM — primera
  gen lenta, resto OK), y RealESRGAN x4plus anime para el workflow "Pulir". Falta
  checkpoint anime/Illustrious — Andy lo elige en Civitai y verifica licencia él mismo.
- **Workflows del usuario guardados:** `Desde Cero` (txt2img), `Pipeline Limpio`
  (referencia → JoyCaption + términos + img2img), `Pulir` (upscale → 2ª pasada denoise
  0.4), + 3 legacy.
- **Backup repo creado:** `C:\Users\andre\repos\comfyui-setup` (workflows, configs,
  RESTORE.md, MODELS.md; re-snapshot con `backup.ps1` + commit; GitHub privado).
- **Manual offline:** `E:\AI\manual.html` + Artifact publicado
  (https://claude.ai/code/artifact/79d37f6d-8fae-430f-a5fc-95cd287c61ba).
- **Skill `comfyui` creada y pusheada** (`36baebb`): SKILL.md router + 4 workflows
  (run-and-generate, add-model, image-to-prompt, lora-training-stage2) + 3 docs
  (stack-reference, troubleshooting, prompting).
- **Lección de debugging encodeada en la skill:** horas perdidas tuneando "censura"
  cuando el captioner devolvía strings vacíos por un load error silencioso — regla nueva:
  primero verificar que cada etapa emite contenido real (PreviewAny / metadata PNG del
  grafo ejecutado), después tunear parámetros. También: editar el workflow .json
  directamente > guiar cableado manual en canvas (3× first-try vs wires perdidos).

## Where We Paused

**Last action:** Skill commiteada y pusheada; la sesión cerró sin retrospective/handoff.
**Next action:** Nada pendiente técnico en Stage 1. Cuando Andy tenga diseños de
personaje que fijar: "arranca Stage 2" → plan aprobado en
`comfyui/workflows/lora-training-stage2.md` (OneTrainer + dataset-prep script en repos\ +
test SFW en 12 GB VRAM).
**Blockers:** Ninguno. Esperando a Andy:
1. Elegir checkpoint anime/Illustrious en Civitai (él verifica licencia — su regla).
2. Decidir cuándo arrancar Stage 2 (LoRA training).

## Files to Read First

- `comfyui/SKILL.md` — router + hard rules (content boundaries del proyecto adult-game,
  regla de verificación por observación, orden de debugging).
- `comfyui/docs/stack-reference.md` — paths, hardware, modelos, API, launch headless.
- `comfyui/workflows/lora-training-stage2.md` — el plan aprobado de Stage 2.

## Notes / Gotchas

- `extra_model_paths.yaml` se lee solo al arrancar el server: mapeo de carpeta nueva →
  restart; archivo nuevo en carpeta ya mapeada → solo `R` en el browser tab.
- Stack es del **desktop** (E:\ + 3080 Ti). El portátil no lo tiene (ver memoria
  two-pcs); rental fallback para training si 12 GB no alcanza: RunPod/Vast.ai, chequeando
  ToS para NSFW antes de recomendar.
- Boundary de contenido: Claude hace tooling/scripts/debugging — no curación, captioning
  ni evaluación de contenido explícito; personajes inequívocamente adultos, sin
  likenesses reales.
- Gotchas de instalación (bsdtar para .7z, URL del repo movida, VRAM real vía
  nvidia-smi) ya están en `comfyui/docs/stack-reference.md` § Gotchas.

## Questions to Answer

- Ninguna abierta. Stage 2 espera trigger explícito de Andy.
