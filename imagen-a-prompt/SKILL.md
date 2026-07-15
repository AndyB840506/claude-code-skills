---
name: imagen-a-prompt
description: Toma cualquier imagen, la analiza en detalle completo (sujeto, anatomía, pose, ropa, entorno, luz, cámara, estilo, paleta) y genera un prompt listo para ComfyUI en el formato del modelo destino (Z-Image, Chroma, Illustrious/SDXL booru, SDXL fotorreal/bigASP), etiquetado con la plantilla ComfyUI exacta a correr. Standalone y portable entre máquinas. Triggers ES - imagen a prompt, describe esta imagen, prompt desde imagen, analiza imagen para prompt, reverse prompt, sacar prompt de imagen, replicar imagen, prompt de referencia. Triggers EN - image to prompt, describe image for prompt, reverse engineer prompt, prompt from image, recreate this image, reference image prompt.
---

# Imagen a Prompt — análisis visual completo para ComfyUI

Convierte una imagen de referencia en un prompt detallado y formateado para el modelo
que vayas a usar en ComfyUI. Skill autocontenida: todo lo que necesita vive en esta
carpeta. Funciona en cualquier máquina con este repo clonado.

Dos rutas de análisis:

| Ruta | Quién ve la imagen | Cuándo |
|---|---|---|
| **Visión directa** | Claude (herramienta Read) | Imágenes SFW — la ruta por defecto |
| **Captioner local** | JoyCaption/WD14 en tu GPU vía ComfyUI API | Contenido explícito, O cualquier rechazo/evasiva de Claude (persona real identificable, sobre-cautela con un personaje ficticio, etc.) — ver `workflows/captioner-local.md` |

## Reference

- `workflows/analizar-imagen.md` — proceso completo (recopilar inputs → analizar →
  formatear → entregar)
- `docs/prompt-formats.md` — formato exacto por familia de modelo + settings + negativos
- `workflows/captioner-local.md` — ruta local uncensored (JoyCaption/WD14 vía API)

## EXECUTION

Has invocado `/imagen-a-prompt`. Sigue `workflows/analizar-imagen.md` de principio a fin.

## Hard rules

- Skill autocontenida: no leer ni depender de archivos de otras skills. Los formatos
  de prompt viven en `docs/prompt-formats.md` de ESTA carpeta.
- El detalle anatómico y de pose se describe completo y sin eufemismos en imágenes SFW;
  para contenido explícito la visión la hace el captioner local (JoyCaption es un VLM
  uncensored en la máquina del usuario), no Claude — es un límite del modelo, no de la
  skill, y la ruta local existe precisamente para eso.
- Decisión explícita del usuario (2026-07-15): si Claude rechaza o evade describir la
  imagen — incluyendo el caso de una persona real identificable, además de contenido
  explícito o sobre-cautela con un personaje ficticio/anime — no reintentar con otro
  phrasing ni insistir: cambiar directo a la ruta local (`workflows/captioner-local.md`)
  y decirlo en una línea. El captioner local corre en la GPU del propio usuario sobre
  sus propias imágenes de referencia.
- Nunca inventar detalles que no están en la imagen; si algo no se distingue (marca,
  texto, un objeto ambiguo), decirlo en vez de rellenarlo.
- Prompts de salida en inglés siempre.
