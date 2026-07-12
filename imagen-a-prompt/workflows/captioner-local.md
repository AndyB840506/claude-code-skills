# Ruta local — captioner uncensored en tu GPU

Para imágenes con contenido explícito, la visión NO la hace Claude (límite del modelo,
no configurable por skill): la hace un VLM local sin restricciones que corre en tu
ComfyUI. El resultado (caption/tags) es tuyo tal cual lo emite el modelo local.

## Requisitos (ya instalados en ambas máquinas, 2026-07-08)

- ComfyUI corriendo (server local, API en `http://127.0.0.1:8188`)
- Custom nodes: `ComfyUI-JoyCaption` (AILab pack) y `ComfyUI-WD14-Tagger`
- Detección de máquina: `Get-PSDrive E` existe → desktop, AI root = `E:\AI`;
  si no → portátil, AI root = `D:\AI`

## Cuál usar

| Captioner | Salida | Mejor para |
|---|---|---|
| **JoyCaption** (`joycaption-beta-one`, 4-bit) | Descripción en oraciones | Z-Image, Chroma |
| **JoyCaption modo `Stable Diffusion Prompt`** | Texto ya con forma de prompt | prompt directo sin re-redactar (verificado 2026-07-12) |
| **WD14 Tagger** (`wd-eva02-large-tagger-v3`) | Booru tags | Illustrious/SDXL anime |

## Pasos (vía API, Claude ejecuta la mecánica)

0. Si la API no responde, levantar el server:
   `Start-Process "<AI root>\ComfyUI_windows_portable\run_nvidia_gpu.bat"` y esperar
   a que `/system_stats` responda (~30-60 s).
1. Copiar la imagen a `<AI root>\ComfyUI_windows_portable\ComfyUI\input\`.
2. Encolar el grafo (**la API rechaza grafos sin nodo de salida** — `JC_adv` solo no
   basta: cerrar con `PreviewAny` conectado al STRING; WD14 sí es nodo de salida):
   - JoyCaption: `LoadImage → JC_adv → PreviewAny (slot 1)` — el caption sale en
     **slot 1 (STRING)**;
     el slot 0 muestra la instrucción al VLM y ahí aparecen los ERRORES de carga como
     texto (caption vacío = leer slot 0). Quantization `Maximum Savings (4-bit)`,
     memory `Clear After Run`. **Nunca la opción fp8 en 12 GB** (descomprime a bf16
     ~18.6 GB → OOM).
   - WD14: `LoadImage → WD14Tagger|pysssss` (threshold 0.35, character 0.85). Tags en
     history: `outputs.<node_id>.tags`.
3. Recuperar el resultado del history de la API y entregarlo al usuario tal cual.
4. **Cache gotcha:** re-runs idénticos devuelven output cacheado (history con outputs
   vacíos) — mover cualquier input (ej. temperature 0.60→0.61) para forzar re-ejecución.

## Del caption al prompt final

- El caption/tags crudos se entregan al usuario sin edición.
- El usuario arma el prompt final con `docs/prompt-formats.md` como guía de estructura
  y settings; Claude asiste con la mecánica (formato, orden de bloques, settings del
  modelo) sobre las partes no explícitas.
- Alternativa 100% local sin manos: el workflow guardado `img2prompt` en ComfyUI
  encadena tagger → prompt → img2img directo (denoise 0.5 copia fiel / 0.7 suelta /
  1.0 ignora la referencia).
