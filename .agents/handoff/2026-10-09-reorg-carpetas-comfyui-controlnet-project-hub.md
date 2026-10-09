# Handoff: Reorg de carpetas, ControlNet para ComfyUI, fixloop y Project Hub
**Date:** 2026-10-09 (viernes)
**Machine:** desktop (E:\)
**Status:** Complete en el escritorio — el portátil se reorganiza solo en su segundo arranque

---

## What We Accomplished This Session
- **ArtCraft / storytold evaluados.** ArtCraft: app en la nube, licencia "fair source" (no MIT), sin modelos locales. El resto de la org (PhotoCraft, etc.) son clones de apps de Adobe/Microsoft de 9 días, Apache-2.0. Andy pidió probar PhotoCraft.
- **ComfyUI:** instalado Z-Image Fun ControlNet Union 2.1 (2602-8steps, 6.71 GB, sha256 verificado) en `E:\AI\models\model_patches\` + `comfyui_controlnet_aux` (sin `onnxruntime-gpu`). Prueba A/B: figura confinada al tercio superior 9:16 — texto 0/2, CN 1.0 2/2. Plantilla `comfyui/templates/zimage-controlnet-api.json`; docs en `artwork-composition.md` y `stack-reference.md`; backup en `repos/comfyui-setup`.
- **PhotoCraft** (portable v0.5.0 en `E:\Sandbox\photocraft\`): PSD de la portada MPD T2E04 16:9 con 4 capas de texto vivas, verificado con psd-tools.
- **fixloop** (`E:\Sandbox\fixloop\fixloop.py`, SOLO en el escritorio, sin git): pintar máscara en PhotoCraft → Z-Image repinta solo esa zona. Humo del vaso de MPD-T2-poe-v14 eliminado tras 9 corridas. Receta: `--destroy-caf --strength 0 --denoise 0.7`.
- **Memoria:** 11 archivos locales eran más viejos que los del repo → reemplazados; 2 de BTQ fusionados a mano; índice partido en 4 hubs (`hub_*.md`) → 76 líneas / 11.9 KB; slugs huérfanos movidos a backup (local + `claude-continuity/archive/`).
- **Reorg:** `repos\_kits` (14 kit-*), `repos\_archive` (9 + claude-bootstrap desde E:), `E:\Personal`, `E:\Work`, BTQ `EP 26`, MPD `Temporada 1\` (EP 04/05). 16 archivos con rutas reescritas (6 plantillas vivas de comfyui incluidas). `cv` y `freelance-jobs` con git local.
- **Project Hub:** https://claude.ai/artifact/53P61HDQafMEKpW3fuciqU — generado por `claude-continuity/project-hub/build_projects.py` (hace fetch y compara con GitHub).
- **start.ps1** (`claude-continuity`): paso 3b aplica el layout en cada arranque (`reorganize-repos.ps1 -Quiet`), se relanza si el pull lo cambió, y compara memoria con fines de línea normalizados (101 falsos "conservados" → 1 real).

## Where We Paused
**Last action:** session-close (retrospectiva aplicada: 4 aprendizajes; auditoría de kit limpia).
**Next action:** en el **portátil**, correr `start.ps1` dos veces (el primero solo baja el script nuevo; el segundo reorganiza). Si el clasificador de permisos lo bloquea, Andy lo corre a mano.
**Blockers:**
- Repos privados de `cv` y `freelance-jobs`: Andy los crea en github.com/new y pega las URLs.
- `E:\msdownld.tmp`: protegido por Windows, oculto — se deja.

## Files to Read First
- memoria `reference_project_hub.md` — layout acordado, cómo refrescar el hub, pendientes
- memoria `project_fixloop_prototype.md` — lecciones de las 9 corridas
- `comfyui/docs/artwork-composition.md` — ControlNet para composición y para quitar objetos
- `C:\Users\andre\.claude\project-map.md` — mapa nuevo (no se sincroniza entre PCs; el hub sí)

## Notes / Gotchas
- **HireSignal en el escritorio: 80 commits detrás de GitHub + 3 archivos sin commitear.** No hacer pull a ciegas; revisarlo con Andy antes de trabajar ahí. the-freelancer 18 detrás, lucca-tech-web 1 detrás (trabajo del portátil del 10-06).
- El clasificador de permisos bloqueó a Claude mover repos y borrar carpetas de primer nivel en E:. No rodearlo: se le pasa el comando a Andy, **cada uno en su propio bloque de código** (dos comandos en inline code llegaron rotos).
- En modo inpaint, el ControlNet de Z-Image RE-CREA lo que se quiere borrar → strength 0 para quitar objetos.
- `MPD EP 05.mp3` no está en `E:\Podcast\MPD\Temporada 1\EP 05\` (ya faltaba antes del movimiento).
- `E:\Personal\6041ab9d-....pdf` se movió sin abrirlo — Andy debe confirmar que es personal.

## Questions to Answer
- ¿Promover fixloop del sandbox al skill `comfyui`? (Andy decide tras probarlo con una máscara pintada por él)
- ¿Instalar el ControlNet lite (2.02 GB) en el portátil?
- BTQ T3 EP.02 se graba el sábado 2026-10-10 (según memoria; no es de esta sesión).
