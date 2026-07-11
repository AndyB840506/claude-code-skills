# Handoff: Stack de modelos para diseño de personajes (ComfyUI)

**Date:** 2026-07-11
**Status:** Complete — stack operativo de 6 modelos con workflows verificados; solo quedan tareas del usuario (licencias)

---

## What We Accomplished This Session

- **Fix HiDream:** el workflow bajado (plantilla Next Diffusion) apuntaba a `hidream_i1_dev_fp8.safetensors`; el archivo real del usuario es `hidream_i1_dev_uncensored_fp8_v0.2.safetensors`. Un solo widget corregido → verificado con generación real (~5 min/img).
- **Instalados y verificados de punta a punta** (generación real vía API, imágenes en `E:\AI\outputs\`):
  - `Chroma1-HD-fp8mixed` (9.19 GB, Comfy-Org repackaged) + encoder `t5xxl_flan_fp8_scaled` (5.16 GB, silveroxides)
  - Trío SDXL: `bigASP_v2` (fotorreal, repo del autor fancyfeast), `NoobAI-XL-v1.1`, `Illustrious-XL-v2.0` — todo HuggingFace directo, sin cuenta (usuario no quiere pagar/loguearse en Civitai)
  - `RealESRGAN_x4plus.pth` (upscaler fotorreal; solo existía el de anime)
- **5 workflows "Pro" nuevos** (patrón two-stage: base → hi-res muteable con Ctrl+M): HiDream Realista, Chroma Personajes, BigASP Fotorreal, NoobAI Personajes, Illustrious Personajes. Todos generados como JSON por script, validados y corridos.
- **Queja "Chroma medio chafitas" → A/B mismo-seed por API** (receta mía vs oficial flan vs flan+50steps): diferencias marginales entre recetas; la causa raíz era **densidad del prompt** (Chroma rellena los huecos con "promedio AI"). Workflow actualizado a receta oficial (flan + min_padding 1) de todas formas.
- **3 plantillas de prompt denso** (real / animado / 3D) como MarkdownNote en el canvas de Chroma Personajes Pro, con ejemplos rellenos.
- **Tiempos medidos (3080 Ti, two-stage):** SDXL 25-50 s · Chroma ~7-8 min · HiDream ~8-10 min. División de trabajo: SDXL para iterar a diario, Chroma/HiDream para hero shots.
- **Backup repo `comfyui-setup` al día** (commits `023925d`→`94ab2fa`): 5 workflows, MODELS.md refrescado con URLs de restauración (y arreglado tras corrupción por `Set-Content -Encoding ASCII`).
- **Retrospectiva aplicada:** stack-reference/prompting/troubleshooting/add-model del skill comfyui actualizados + regla de encoding en CLAUDE.md + triggers nuevos en comfyui/SKILL.md.

## Where We Paused

**Last action:** cierre de sesión (retrospectiva y audit aplicados, este handoff).
**Next action:** nada técnico pendiente — el stack está operativo. Si el usuario quiere seguir: LoRA training Stage 2 (ahora viable con los SDXL) o probar las plantillas de Chroma en producción.
**Blockers:** ninguno del lado técnico.

## Files to Read First

- `comfyui/docs/stack-reference.md` — inventario y tiempos actualizados de hoy
- `comfyui/docs/prompting.md` — sección Chroma nueva (prompts densos, negativo activo)
- `C:\Users\andre\repos\comfyui-setup\MODELS.md` — los 9 modelos con URLs exactas
- Workflows en `E:\AI\ComfyUI_windows_portable\ComfyUI\user\default\workflows\*Pro.json`

## Notes / Gotchas

- **Pendiente del usuario (no de Claude):** revisar licencias antes de uso comercial del juego — NoobAI (fair-ai-public-license-1.0-sd), Illustrious v2.0 (términos Onoma), bigASP v2. Listadas en MODELS.md § Pendiente.
- Los 2 LoRAs preexistentes (`skin`, `adapter_model`) son de base desconocida — NO cablearlos a ningún workflow sin confirmar su modelo base.
- Prompts por familia: SDXL estilizado = tags booru; bigASP = `score_8_up` + caption natural (entrenado con JoyCaption — se puede captionear una referencia con el stack local y usar ese texto); Chroma = párrafo denso obligatorio.
- Reddit y YouTube están bloqueados para fetch; la ruta que funcionó: buscar el nombre del workflow en OpenArt/Civitai y los modelos vía API de HuggingFace (`api/models?search=`, `?blobs=true`).
- Cola de ComfyUI: si el usuario limpia la cola del navegador, borra también los prompts encolados por API (pasó hoy — re-encolar, no hay pérdida).

## Questions to Answer

- ¿El usuario quiere arrancar Stage 2 (LoRA training de personajes propios sobre SDXL) como próxima sesión de este track?
