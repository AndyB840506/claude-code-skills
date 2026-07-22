# Workflow 03 — Artwork del Episodio

Genera prompts listos para copiar en Google Flow (con Nani Banana Pro o Imagen 3) en 3 formatos. Los prompts van en inglés — los modelos de imagen responden mejor en inglés.

**Regla fundamental: Siempre preguntar si existe un prompt exitoso de un episodio anterior antes de crear uno nuevo. Reusar estructura probada > crear desde cero.**

---

## Paso 0 — Cargar datos

**0.a — OBLIGATORIO ANTES DE PROPONER CUALQUIER DIRECCIÓN VISUAL: MIRAR el artwork vigente.**
No basta con leer los colores del perfil — hay que ABRIR la imagen actual del show (portada
publicada y/o el último `EP0XX-1x1-FINAL*`) con la herramienta Read y verla. Si no se encuentra el
archivo, PEDIRLE al usuario que la comparta antes de seguir. Prohibido proponer paleta, estilo o
composición nueva sin haber visto la actual.
*(Mordió el 2026-07-22, rebrand MPD Temporada 2: se diseñó una identidad completa —paleta ámbar,
wordmark, specimen en vivo— asumiendo un lenguaje fotográfico, cuando la portada real del show era
un póster ilustrado negro/crema/ROJO. Se propuso además reemplazar el crimson `#9B1C1C` que estaba
escrito en `podcast-profile.json` y ya había sido leído. El usuario tuvo que corregirlo mandando un
screenshot, después de varias generaciones perdidas.)*

1. Lee `podcast-profile.json`: nombre del podcast, colores de marca, estilo visual, tono.
2. Busca archivos `artwork-ep*.md` en el directorio. Si existen, lista los disponibles: "Tengo prompts guardados del EP.001 y EP.002 — ¿quieres usar alguno como base?"
3. Lee el script del episodio si existe para extraer el tema y referencia cultural.

---

## Paso 1 — Datos del episodio visual

Pregunta en un solo mensaje:

> **Para el artwork del episodio:**
> 1. ¿Cuál es el número de episodio?
> 2. ¿El episodio tiene una referencia visual clara? (película, serie, personaje, persona real, lugar icónico, concepto abstracto...) Si no, ¿qué emoción o imagen debería transmitir la portada?
> 3. ¿Qué vibe quieres para este episodio? (dramático, energético, melancólico, cálido, oscuro, esperanzador, minimal...)
> 4. ¿Hay algún episodio anterior cuyo artwork funcionó bien y quieres usar como estructura base?

Si el usuario tiene un episodio anterior como referencia → lee ese archivo y úsalo como estructura, cambiando solo el contenido específico de este episodio (colores, sujeto, texto, expresión).

---

## Paso 2 — Construir los prompts

Para cada formato, genera un prompt completo en inglés siguiendo esta arquitectura:

### Línea de apertura — estilo y calidad
```
Cinematic photographic image. Hyperrealistic, captured on 35mm Kodak Portra film. [Warm/Cool/Moody] color grading. [Año o era si es relevante para el tema].
```

### Sujeto principal — descripción detallada
- **Si hay persona real:** nombre completo + edad aproximada + rasgos físicos en detalle. Usar CAPS para colores críticos: "DARK BROWN hair", "BLUE eyes", "wearing a RED jacket"
- **Si hay personaje de ficción:** nombre + descripción física detallada como si fuera una persona real fotografiada
- **Si es abstracto/conceptual:** descripción visual del concepto, metáfora visual, ambiente

### Iluminación y fotografía
```
Key light from [dirección: left/right/above]. [Warm golden/Cool blue/Neutral] tone. Soft shadows. [Referencia cinematográfica si aplica]. NOT a 3D render. NOT an illustration. Photorealistic only.
```

### Tipografía en imagen
```
Text overlay: '[TÍTULO DEL EPISODIO]' in [bold/ultra-bold] [color] [sans-serif/serif] at [top/center/bottom]. '[EP.NNN]' small [color] at [posición]. '[NOMBRE PODCAST]' ultra-bold [color] at bottom center.
```

### Footer de marca
```
Bottom bar: solid [color principal de marca] background. Brand colors throughout: [hex primario], [hex secundario], [hex acento].
```

> **⚠️ Regla del footer:** El lado derecho del footer bar siempre muestra los logos de las **3 plataformas de streaming** (Spotify · Apple Podcasts · Amazon Music) en color plata/blanco. **NUNCA** poner redes sociales (Instagram, Facebook, TikTok) en el artwork del episodio — esas van en los flyers de social media, no en la portada.
>
> **⚠️ Regla de íconos de plataforma:** El problema no es usar nombres de marca — el problema es ser VAGO. Nombrar los logos directamente funciona correctamente en generación:
> - ✅ `"Spotify logo, Apple Podcasts logo, Amazon Music logo — small, in silver #A8A8A8"`
> - ❌ `"silver platform logos"` ← ESTE es el error: vago, el modelo elige cualquier logo arbitrario (ej: PlayStation)
>
> **Corrección en Flow (modo edición):** Si los íconos salen incorrectos, usar la función de edición de imagen de Flow escribiendo:
> `"replace the logos for Spotify logo, Amazon Music logo, and Apple Music logo"`
>
> **Fallback final:** Si la edición tampoco funciona → añadir logos reales en Canva.

### Restricción final
```
No extra text outside specified overlays. Highly detailed, award-winning photography style.
```

---

## Dirección visual del show (CONGELADA 2026-06-12 — validada con EP.004 Kraken)

> **⚠️ Esta sección es específica de MPD (Mr. Putrid's Den) — no la apliques a otros
> shows.** El estilo fotorrealista "film still" y la prohibición de ilustración de
> abajo son decisiones de dirección de arte de MPD, no una regla general de la skill.
> Para cualquier otro show, usa la dirección visual definida en su propio
> `podcast-profile.json` (`logo_descripcion`, `colores`, `estilo visual` del Paso 3 de
> `00-setup.md`) en su lugar — incluso si eso significa ilustración, cómic, u otro
> estilo que esta sección de abajo prohíbe para MPD específicamente.

**MPD = fotograma cinematográfico.** Cada portada debe parecer un still de película de
los 80s en 35mm — NUNCA diseño gráfico ni póster ilustrado. Si una imagen podría pasar
por portada de BTQ (póster gráfico negro+dorado), falló.

Bloques que se copian VERBATIM en todo prompt de portada (solo cambia la escena central):

**[BLOQUE CONGELADO — ATMÓSFERA MPD]**
```
This must look like a film still from a 1980s movie shot on 35mm —
NOT a graphic design, NOT illustration.
Lit from one side by deep crimson light #9B1C1C and from the other by
warm golden light, the two colors meeting on the edges of the silhouette.
NO visible face detail anywhere — silhouette and rim light only.
Heavy smoke, dust floating in the light beams, deep shadows,
35mm film grain, high contrast, cinematic.
The bottom quarter of the image fades to near-black #0d0d0d.
```

**[BLOQUE CONGELADO — FOOTER MPD]**
```
FOOTER BAR: solid #1a1a1a strip at the very bottom, full width.
  Left: "Mr. Putrid's Den" in small white text
  Center: "EP.0XX" in crimson #9B1C1C with a small kraken tentacle icon
  Right (silver #A8A8A8): Spotify icon (circle with three curved lines),
  Apple Podcasts icon (rounded square with microphone), and the
  "amazon music" wordmark with small orange curved arrow below
```

**Reglas de la dirección:**
1. **NUNCA rostros reconocibles en portadas** — siluetas y rim light solamente. Resuelve
   dos problemas: Flow renderiza caras mal, y evita usar la imagen de artistas reales
   (Elkin, etc.) en material promocional. ⚠️ Esta regla SUPERSEDE la instrucción del
   Paso 2 de describir rasgos físicos de personas reales — esa aplica solo si el usuario
   pide explícitamente un retrato.
2. **Tipografía:** texto exacto entre comillas + "render text EXACTLY as written, letter
   by letter, no changes". Máximo ~5 palabras por línea, pocas líneas. Las tildes y eñes
   son el punto débil de Flow — verificar con zoom letra por letra; si daña una tilde dos
   veces seguidas, fallback: quitarla en mayúsculas.
3. **Checklist antes de aprobar cualquier generación:** (a) texto letra por letra sin
   palabras inventadas, (b) cero detalle facial, (c) parece foto de película, no póster.
4. Si la generación sale perfecta salvo el texto: usar el modo edición de Flow sobre esa
   misma imagen ("same image, fix only the text") en vez de regenerar desde cero.

Prompt de referencia validado: portada EP.004 (escena Teatro de Manrique 1984) — ver
`mrputridsden-production/episodios/artwork-ep004.md`.

---

## Reglas para prompts de Flow (confirmadas EP.003)

Aplicar siempre antes de generar cualquier prompt de artwork:

1. **Tipografía en tercio inferior — nunca al centro.** Usar gradiente oscuro (transparent → #0d0d0d) en el tercio inferior del frame y confinar todo el texto ahí. Texto centrado en la imagen = atravesado con el visual.

2. **Split scenes: división explícita con porcentajes.** Nunca escribir "merge at center" o "blending." Usar: `"Strict left-right vertical split: LEFT HALF (exactly left 50% of frame): [descripción]. RIGHT HALF (exactly right 50% of frame): [descripción]."` Sin esto, Flow superpone las dos escenas.

3. **Escenas con vida — siempre especificar actividad.** "Caribbean street" sin más = calle vacía. Siempre definir quién está en la escena y qué hace: "with dancers", "with crowd", "guitarist silhouette performing", etc.

4. **Quote cards autoexplicativos.** Los quotes deben entenderse sin haber escuchado el episodio. Eliminar referencias que requieren contexto interno (ej: "Iron Man" sin explicar que es el riff de Black Sabbath de Birmingham).

5. **El sujeto en escena, no implícito.** Si el momento tiene un protagonista (ej. Sister Rosetta en su boda), ponerlo explícitamente en el prompt. "Single spotlight on an empty stage" = imagen genérica sin fuerza narrativa.

---

## Paso 3 — Generar los 3 formatos

| Formato | Dimensiones | Uso principal |
|---|---|---|
| **1:1** | 3000×3000px | Spotify, redes cuadradas, portada del episodio |
| **9:16** | 1080×1920px | Instagram Stories, TikTok, Reels |
| **16:9** | 1920×1080px | YouTube thumbnail, portada web, LinkedIn |

Genera el prompt completo para cada formato. El contenido es el mismo — lo que cambia es:
- La composición del sujeto (centrado para 1:1, posicionado arriba para 9:16, en un lado para 16:9)
- El espacio tipográfico (diferente en cada formato)
- La instrucción de dimensiones al inicio

---

## Paso 4 — Plataformas de IA y opciones

Antes de usar, presenta al usuario las opciones disponibles para generar imágenes:

| Plataforma | Costo | Nivel | Mejor para |
|---|---|---|---|
| **Google Flow / Imagen 3** | Gratis (con cuenta Google) | Excelente | Retratos fotorrealistas, portadas limpias |
| **Kling AI** | Freemium / desde ~$10/mes | Muy bueno | Composiciones cinematográficas |
| **Midjourney** | ~$10/mes básico | El más artístico | Estilos consistentes y únicos |
| **Adobe Firefly** | Incluido en Creative Cloud / ~$5/mes | Muy bueno | Integración con Photoshop, seguridad comercial |
| **DALL-E 3** | Incluido en ChatGPT Plus $20/mes | Excelente | Sigue instrucciones detalladas de texto |
| **Stable Diffusion** | Gratis (instalación local) | Máximo control | Control total, curva de aprendizaje alta |

> **⚠️ Advertencia de costos:** Los planes gratuitos tienen límite de créditos/tokens. Una sesión con varias iteraciones puede consumir rápido los créditos. Para uso constante (1 episodio/semana), evalúa si la suscripción mensual se justifica.

**Recomendación:** Empieza con **Google Flow** (gratis) que produce excelentes resultados. Los prompts generados son optimizados para este modelo.

---

## Paso 5 — Instrucciones de uso

Después de los 3 prompts, añade:

```
──────────────────────────────────────────────────────
  ESPECIFICACIONES TÉCNICAS — PLATAFORMAS
──────────────────────────────────────────────────────
  Formato 1:1 (portada principal del episodio):
  ├─ Dimensiones: 3000 × 3000 px (cuadrado exacto)
  ├─ Formato: JPEG o PNG
  ├─ Color: RGB (NO CMYK)
  ├─ Resolución: 72 DPI mínimo

  Límites por plataforma:
  ├─ Spotify:        máx 500 KB
  ├─ Amazon Music:   máx 500 KB
  └─ Apple Podcasts: máx 4 MB (acepta JPEG o PNG)

  ⚠️ IMPORTANTE:
  Los modelos de IA generan PNG de alta resolución (100+ MB).
  ANTES de subir a cualquier plataforma:
  1. Convierte a JPEG
  2. Comprime con squoosh.app (es gratis)
  3. Verifica que quede bajo 500 KB → sirve para las 3
──────────────────────────────────────────────────────
  CÓMO USAR ESTOS PROMPTS EN GOOGLE FLOW
──────────────────────────────────────────────────────
  1. Abre: labs.google/fx/tools/image-fx
  2. Selecciona "Imagen 3" o "Nani Banana Pro" (si disponible)
  3. Pega el prompt del formato que necesitas
  4. Genera — el modelo produce 2-4 variantes
  5. Selecciona la mejor por formato
  6. Descarga cada variante
  
  Para la portada principal (formato 1:1):
  7. Convierte PNG a JPEG en squoosh.app
  8. Comprime hasta que esté bajo 500 KB
  9. Sube el mismo archivo a Spotify · Apple Podcasts · Amazon Music
  
  Si el resultado no cumple:
  → Ajusta la descripción del sujeto (más detalles físicos)
  → Añade al final: "highly detailed, sharp focus, professional photography"
  → Cambia la referencia de iluminación
  → Si hay texto mal renderizado: especifica la fuente más (ej. "Helvetica Bold")
──────────────────────────────────────────────────────
```

---

## Paso 7 — Guardar prompts

1. Guarda los 3 prompts como `artwork-ep[NNN].md` en el directorio actual.
2. Muestra resumen:

```
══════════════════════════════════════════
  Prompts de artwork generados ✓
══════════════════════════════════════════
  Episodio:  EP.[NNN]
  Formatos:  1:1 · 9:16 · 16:9
  Archivo:   artwork-ep[NNN].md
══════════════════════════════════════════
  → Guarda este archivo: el próximo episodio
    te preguntará si quieres reusar la estructura.
══════════════════════════════════════════
```

3. Pregunta: "¿Continuamos con el plan de social media?"

