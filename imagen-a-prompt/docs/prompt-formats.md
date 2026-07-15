# Formatos de prompt por familia de modelo

Copia autocontenida para esta skill (origen: guía de prompting del stack local,
2026-07-11). Si se aprende algo nuevo sobre un modelo, actualizar AQUÍ.

## Z-Image / Qwen-encoder — frases naturales

Fórmula: **sujeto + acción + entorno + luz + cámara/estilo**, en oraciones completas.

- Bien: `A boxer resting in a dim locker room, steam in the air, single overhead lamp, 35mm photo, shallow depth of field`
- Mal: `boxer, locker room, dramatic, 4k, masterpiece` (apilar keywords desperdicia este encoder)

Reglas críticas (Z-Image **turbo**):
- **A CFG 1.0 el negativo NO actúa** — es decorativo. Todo el control va en el positivo.
- **"DO NOT render X" EVOCA X.** Nunca nombrar el concepto prohibido; describir solo lo
  que sí se quiere en su lugar.
- **Flat in = flat out:** describir la iluminación SIEMPRE (rim light, lado en sombra,
  sombra proyectada) o sale plano.
- Personajes de proporciones conocidas: declarar proporciones explícitas ("a tall adult
  man, his head is about one quarter of his total height") o tiende a chibi.
- **Un adjetivo de color cerca de la luz/fondo tiñe todo el fondo**, aunque se pida
  "void black" aparte (ej. "faint red glow" → fondo completo rojo). Si hay una fuente de
  luz de color, declarar explícito que el resto se apaga a negro puro: "background fades
  to pure black, no colored wash".
- **Escenas de un solo objeto en vacío pueden alucinar objetos extra** sin pedirlos.
  Agregar "alone, nothing else in frame" lo suprime.
- **Logos/íconos SÍ los reconoce, pero solo aislados** — mezclados con escena + texto
  largo en un mismo prompt, los íconos pueden salir bien pero el texto SIEMPRE sale con
  errores de ortografía. Aislar los íconos en su propia generación (fondo negro puro,
  "no text, no words, no letters", sin escena) y componer todo el texto legible aparte
  (PIL u otra herramienta determinista) — nunca dejar que el modelo genere texto que se
  vaya a leer en el resultado final.

Settings sugeridos: `cfg 1.0 · steps 8-9 · euler o res_multistep · scheduler simple`

## Chroma (T5-flan encoder) — párrafos DENSOS

Chroma castiga prompts cortos: cada bloque no descrito se rellena con "promedio AI"
(piel plástica, render genérico). Estructura por párrafo, en este orden:

1. Sujeto detallado (rasgos, edad, complexión)
2. Encuadre y pose
3. Ropa y materiales
4. Cámara y lente
5. Luz (fuentes, dirección, color)
6. Textura de piel / superficie
7. Entorno con 2-3 detalles concretos

- **Aquí el negativo SÍ actúa** (cfg real). Usarlo como cortafuegos de estilo:
  `photograph, realistic skin` para forzar 2D; `anime, illustration` para forzar fotorreal.

Settings sugeridos: `euler + Beta scheduler · 26 steps · cfg 3.8 · base 1152×1152`

## Illustrious / SDXL anime — booru tags

Tags separados por coma, en orden de prioridad:
`<count> → apariencia → pose/acción → entorno → luz/composición → calidad`

- Ejemplo: `1girl, red hair, ponytail, boxing gloves, fighting stance, boxing ring, dramatic lighting, from below, masterpiece, best quality`
- Los tags deben ser tags REALES de Danbooru — frases inventadas hacen poco.
- Pesos: `(tag:1.3)` sube, `(tag:0.7)` baja. Más de ~1.5 produce artefactos.
- Negativo estándar: `lowres, bad anatomy, bad hands, extra fingers, watermark, signature`
- Revisar la página de Civitai del checkpoint: muchos exigen prefijos de calidad y un
  negativo recomendado propios.

Settings sugeridos: `cfg ~7 · steps 25-30 · sampler según el checkpoint (ver Civitai)`

## Método de iteración (aplica a todos)

1. Semilla FIJA mientras se desarrolla el prompt — la imagen solo cambia donde cambió
   el prompt.
2. Cambiar UNA cosa por corrida.
3. Prompt listo → semilla aleatoria para variaciones.
4. Defecto recurrente → nombrarlo en el negativo (si el modelo lo respeta) en vez de
   apilar positivos.
5. Composición bien / detalles mal → subir steps o cambiar sampler antes de reescribir
   el prompt.
