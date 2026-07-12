---
name: imagen-a-prompt
description: Toma cualquier imagen, la analiza en detalle completo (sujeto, anatomía, pose, ropa, entorno, luz, cámara, estilo, paleta) y genera un prompt listo para ComfyUI en el formato del modelo destino (Z-Image, Chroma, Illustrious/SDXL). Standalone y portable entre máquinas. Triggers ES - imagen a prompt, describe esta imagen, prompt desde imagen, analiza imagen para prompt, reverse prompt, sacar prompt de imagen, replicar imagen, prompt de referencia. Triggers EN - image to prompt, describe image for prompt, reverse engineer prompt, prompt from image, recreate this image, reference image prompt.
---

# Imagen a Prompt — análisis visual completo para ComfyUI

Convierte una imagen de referencia en un prompt detallado y formateado para el modelo
que vayas a usar en ComfyUI. Skill autocontenida: todo lo que necesita vive en esta
carpeta. Funciona en cualquier máquina con este repo clonado.

Dos rutas de análisis:

| Ruta | Quién ve la imagen | Cuándo |
|---|---|---|
| **Visión directa** | Claude (herramienta Read) | Imágenes SFW — la ruta por defecto |
| **Captioner local** | JoyCaption/WD14 en tu GPU vía ComfyUI API | Contenido explícito — ver `workflows/captioner-local.md` |

## Reference

- `docs/prompt-formats.md` — formato exacto por familia de modelo + settings + negativos
- `workflows/captioner-local.md` — ruta local uncensored (JoyCaption/WD14 vía API)

## EXECUTION

Has invocado `/imagen-a-prompt`. Ejecuta el proceso:

### Paso 1 — Recopilar inputs

Pide en un solo bloque (si ya vinieron en la invocación, salta al Paso 2):

```
Imagen: [ruta del archivo, o arrástrala al chat]
Modelo destino: [menú]
Objetivo: [replicar fiel / variaciones / solo el estilo] — default: replicar fiel
```

Para el modelo destino usa AskUserQuestion con opciones:
**Z-Image** (frases naturales) / **Chroma** (párrafos densos) / **Illustrious-SDXL**
(booru tags) / **Los 3 formatos**.

### Paso 2 — Analizar la imagen

Lee la imagen con la herramienta Read y extrae TODOS estos bloques (el detalle es el
producto — no resumas):

1. **Sujeto(s):** cuántos, qué son, edad aparente, rasgos físicos completos (rostro,
   cabello, complexión, piel, expresión), cada parte del cuerpo visible y su posición.
2. **Pose y acción:** postura exacta, orientación, qué hacen las manos, dirección de
   la mirada, tensión corporal.
3. **Ropa y materiales:** cada prenda/accesorio, tela, estado, cómo cae sobre el cuerpo.
4. **Entorno:** ubicación, 3-5 objetos concretos del fondo, profundidad, época.
5. **Luz:** fuente(s), dirección, dureza, color, sombras proyectadas, hora del día.
6. **Cámara y encuadre:** ángulo, distancia (close-up/medio/completo), lente aparente,
   profundidad de campo, composición.
7. **Estilo y medio:** foto/ilustración/3D/anime, referencias de estilo reconocibles,
   acabado (grano, cel-shading, pintura).
8. **Paleta y textura:** 3-5 colores dominantes, contraste, texturas notables.

Si la imagen es contenido explícito, no la analices con visión directa: cambia a
`workflows/captioner-local.md` (el captioner local corre en la GPU del usuario sin
restricciones) y explica el cambio de ruta en una línea.

### Paso 3 — Formatear el prompt

Con el análisis del Paso 2, genera el prompt según `docs/prompt-formats.md` para el/los
modelo(s) elegidos. Reglas fijas:

- El prompt SIEMPRE en inglés (los modelos de imagen rinden mejor en inglés); la
  conversación sigue en el idioma del usuario.
- Incluye el negativo solo donde actúa (Chroma, SDXL clásico); en Z-Image turbo el
  negativo es decorativo — todo el control va en el positivo.
- Ajusta al objetivo: "replicar fiel" = todo el detalle; "variaciones" = sujeto+estilo
  fijos, entorno/pose abiertos; "solo estilo" = medio, luz, paleta y acabado sin el
  sujeto concreto.
- Cierra cada prompt con la línea de settings sugeridos del modelo (están en
  `docs/prompt-formats.md`).

### Paso 4 — Entregar

Presenta cada prompt en un bloque de código listo para copiar, etiquetado con el modelo.
Pregunta si quiere guardarlo a un archivo `.txt` junto a la imagen original.

---

**Proceso completado.** Resume: imagen analizada, formato(s) generado(s), dónde quedó
guardado (si aplica).

## Hard rules

- Skill autocontenida: no leer ni depender de archivos de otras skills. Los formatos
  de prompt viven en `docs/prompt-formats.md` de ESTA carpeta.
- El detalle anatómico y de pose se describe completo y sin eufemismos en imágenes SFW;
  para contenido explícito la visión la hace el captioner local (JoyCaption es un VLM
  uncensored en la máquina del usuario), no Claude — es un límite del modelo, no de la
  skill, y la ruta local existe precisamente para eso.
- Nunca inventar detalles que no están en la imagen; si algo no se distingue (marca,
  texto, un objeto ambiguo), decirlo en vez de rellenarlo.
- Prompts de salida en inglés siempre.
