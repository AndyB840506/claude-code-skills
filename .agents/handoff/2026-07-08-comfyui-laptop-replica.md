# Handoff: ComfyUI replicado en el portátil (D:\AI)

**Date:** 2026-07-08
**Status:** Complete — stack instalado, verificado con generación real, docs y skill actualizados

---

## What We Accomplished This Session

- **Clon global `~/.claude/skills` sincronizado en el portátil:** estaba 1 mes stale
  (desde 2026-06-12) — el pull trajo comfyui y ~10 skills/updates más. Regla nueva en
  `CLAUDE.md` § inicio: el paso 1 ahora también hace pull del clon global.
- **Stack ComfyUI completo replicado en `D:\AI`** siguiendo `comfyui-setup/RESTORE.md`
  con sustitución `E:\AI` → `D:\AI`: portable v0.27.0 (misma versión del desktop),
  configs adaptados sin BOM, los 5 modelos (~26 GB, réplica completa por decisión de
  Andy pese a 6 GB VRAM), 3 custom nodes (Manager, WD14, JoyCaption) con deps, 6
  workflows y manual offline.
- **Verificado por observación:** server arriba en :8188, los 5 modelos visibles por
  API, custom nodes importados sin error, y generación SDXL real completada
  (`D:\AI\outputs\smoke_test_d_install_00001_.png`, 1024², success).
- **Docs actualizados y pusheados:** skill `comfyui` ahora es machine-aware (AI root =
  E:\AI desktop / D:\AI portátil; commits `84d118a` + audit fixes), `RESTORE.md` del
  repo backup marcado como validado + URLs directos del set Z-Image que faltaban
  (branch `master` de ese repo, no `main`), memoria two-pcs actualizada, memoria nueva
  `feedback-full-replica-env` (Andy prefiere réplica completa sobre instalación mínima).

## Where We Paused

**Last action:** Session close (retrospective aplicada → audit limpio → este handoff).
**Next action:** Nada técnico pendiente de esta sesión. Los pendientes de comfyui
siguen siendo de Andy: elegir checkpoint anime/Illustrious en Civitai (ahora para las
DOS máquinas) y disparar Stage 2 (LoRA) cuando tenga diseños de personaje.
**Blockers:** Ninguno.

## Files to Read First

- `comfyui/SKILL.md` + `comfyui/docs/stack-reference.md` — ahora cubren ambas máquinas.
- `C:\Users\andre\repos\comfyui-setup\RESTORE.md` — receta validada, con URLs de Z-Image.

## Notes / Gotchas

- En el portátil (6 GB VRAM / 16 GB RAM): SDXL verificado OK; **Z-Image sin probar** —
  esperar lentitud fuerte u OOM. Si Andy reporta OOM con Z-Image aquí, es esto.
- El server de esta sesión quedó corriendo como background task; para uso normal el
  launcher es `D:\AI\run_comfyui.bat`.
- El .7z del portable se borró tras extraer (re-descargable; URL en RESTORE.md).

## Questions to Answer

- Ninguna abierta.
