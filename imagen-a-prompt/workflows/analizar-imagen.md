# Analizar imagen y generar prompt

## Paso 1 — Recopilar inputs

Pide en un solo bloque (si ya vinieron en la invocación, salta al Paso 2):

```
Imagen: [ruta del archivo, o arrástrala al chat]
Modelo destino: [menú]
Objetivo: [replicar fiel / variaciones / solo el estilo] — default: replicar fiel
```

Para el modelo destino usa AskUserQuestion con opciones:
**Z-Image** (frases naturales) / **Chroma** (párrafos densos) / **Illustrious-SDXL**
(booru tags) / **Los 3 formatos**.

## Paso 2 — Analizar la imagen

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

## Paso 3 — Formatear el prompt

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

## Paso 4 — Entregar

Presenta cada prompt en un bloque de código listo para copiar, etiquetado con el modelo.
Pregunta si quiere guardarlo a un archivo `.txt` junto a la imagen original.

---

**Proceso completado.** Resume: imagen analizada, formato(s) generado(s), dónde quedó
guardado (si aplica).
