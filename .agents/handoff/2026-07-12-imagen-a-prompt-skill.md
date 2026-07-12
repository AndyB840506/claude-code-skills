# Handoff: Skill imagen-a-prompt — creada, probada end-to-end y afinada

**Date:** 2026-07-12
**Status:** Complete — skill funcionando, probada con caso real, learnings encodados

---

## What We Accomplished This Session

- **Skill nueva `imagen-a-prompt`** (root del repo, standalone y portable): toma cualquier
  imagen y genera prompts para ComfyUI en 3 formatos (Z-Image frases / Chroma párrafos
  densos / Illustrious booru tags). Commits `92c896c` + `ab7bc1a`.
- **Arquitectura de 2 rutas** (decisión clave de diseño): imágenes SFW = visión directa de
  Claude (checklist de 8 bloques); contenido explícito = captioners locales uncensored
  (JoyCaption/WD14) en la GPU vía ComfyUI API — Claude solo maneja la mecánica. Se le
  explicó al usuario que una skill no puede quitar restricciones del modelo; esta
  arquitectura es la que sí logra el objetivo.
- **Primer uso real exitoso**: imagen explícita de E:\Downloads → levantó el server caído →
  WD14 tags + JoyCaption Descriptive + JoyCaption modo "Stable Diffusion Prompt" → 3 prompts
  entregados y guardados en `E:\Downloads\60c5cbef6b7c1ed9ea5d6a3b1e3598d5.prompts.txt`.
- **Retrospective aplicada** (commit `7648753`): regla de ubicación root-vs-nested en
  `crear-skill/docs/conventions.md`; hechos de API (`prompt_no_outputs` exige nodo terminal
  `PreviewAny`, modo SD-Prompt de JC, consultar `/object_info/<class>` antes de armar
  grafos) en `comfyui/workflows/image-to-prompt.md`; puntero de doble copia en
  `comfyui/docs/prompting.md`.
- **Audit del kit**: `imagen-a-prompt` pasa el checklist; SKILL.md=74 líneas >50 aceptado
  a propósito (opción A del usuario: EXECUTION inline es el estándar del kit).

## Where We Paused

**Last action:** Session close (retrospective + audit aplicados, este handoff).
**Next action:** Nada pendiente de esta skill. Uso normal: `/imagen-a-prompt <ruta>`.
**Blockers:** Ninguno.

## Files to Read First

- `imagen-a-prompt/SKILL.md` — flujo completo de la skill (4 pasos, 2 rutas)
- `imagen-a-prompt/workflows/captioner-local.md` — ruta local con los gotchas de API ya encodados
- `imagen-a-prompt/docs/prompt-formats.md` — copia standalone de formatos (¡mantener en sync con `comfyui/docs/prompting.md`!)

## Notes / Gotchas

- **Doble copia deliberada de formatos de prompting** (pedido del usuario: skill standalone
  sin cruces): cambios de reglas por modelo se actualizan en AMBOS archivos — hay punteros
  recíprocos en cada uno.
- La API de ComfyUI rechaza grafos sin nodo de salida; `JC_adv` necesita `PreviewAny` en el
  STRING (slot 1). WD14 sí es nodo de salida.
- JoyCaption `prompt_style: Stable Diffusion Prompt` emite texto ya con forma de prompt —
  evita re-redacción.
- Los captioners alucinan texto en-imagen (firmas/rótulos) — verificar contra la imagen si
  el texto importa.

## Questions to Answer

- Ninguna abierta.
