# Artwork BTQ — Workflow

Genera prompts listos para copiar en Gemini / Nani Banana 2 en 3 formatos estáticos. Los prompts van en inglés — los modelos de imagen responden mejor en inglés.

**Regla fundamental: preguntar siempre si existe un prompt exitoso de un episodio anterior antes de crear uno nuevo. Reusar estructura probada > crear desde cero.**

---

## Paso 0 — Cargar datos

1. Lee `../docs/brand-identity.md`: colores de marca, tipografías, estilo visual.
2. Busca archivos `artwork-ep*.md` en el directorio del proyecto. Si existen, lista los disponibles: "Tengo prompts guardados del EP.010, EP.011... — ¿quieres usar alguno como base?"
3. Lee el guion del episodio si existe para extraer el tema y referencia cultural.

---

## Paso 1 — Datos del episodio visual

Pregunta en un solo mensaje:

> **Para el artwork del episodio:**
> 1. ¿Cuál es el número de episodio?
> 2. ¿El episodio tiene una referencia visual clara? (videojuego, película, anime, personaje, lugar...) Si no, ¿qué emoción o imagen debería transmitir la portada?
> 3. ¿Qué vibe quieres para este episodio? (dramático, energético, melancólico, cálido, oscuro, minimal, elegante...)
> 4. ¿Hay algún episodio anterior cuyo artwork funcionó bien y quieres usar como estructura base?

Si el usuario tiene un episodio anterior como referencia → lee ese archivo y úsalo como estructura, cambiando solo el contenido específico de este episodio.

---

## Paso 2 — Construir los prompts

Para cada formato, genera un prompt completo en inglés siguiendo esta arquitectura:

### Línea de apertura — estilo y calidad
```
Cinematic photographic image. Hyperrealistic, [medium: 35mm film / digital / oil painting style]. [Tone: warm golden / cold noir / dramatic chiaroscuro]. [Era if relevant].
```

### Sujeto principal
- **Si hay referencia cultural (videojuego, película, anime):** descripción visual del concepto/escena icónica, atmósfera, sin personas reales
- **Si es abstracto/conceptual:** descripción visual de la metáfora, objetos, espacio

### Iluminación y fotografía
```
Key light from [left/right/above/below]. [Warm/Cool/Dramatic] tone. [Soft/Hard] shadows. NOT a 3D render. NOT an illustration. Photorealistic only.
```

### Tipografía en imagen
```
Text overlay: 'BEHIND THE QUEUE' in ultra-bold off-white #F5F2EC condensed sans-serif at [top/bottom]. 'EP.[NNN]' in Signal Gold #C9A84C at [position]. '[EPISODE TITLE]' in bold off-white below main subject.
```

### Footer de marca
```
Bottom bar: solid Void Black #0A0A0A. Left: 'Behind the Queue' in small off-white #F5F2EC. Center: 'EP.[NNN]' in Signal Gold #C9A84C. Right: Spotify logo, Apple Podcasts logo — small, in off-white #F5F2EC.
```

> **⚠️ Regla de íconos de plataforma:** Nombrar los logos directamente por marca — esto es lo que funciona:
> - ✅ `"Spotify logo, Apple Podcasts logo — small, in off-white #F5F2EC"`
> - ❌ `"silver platform logos"` ← vago, el modelo puede generar cualquier logo arbitrario
>
> **Corrección en Gemini (modo edición):** Si los íconos salen incorrectos, usar la función de edición de imagen escribiendo: `"replace the logos for Spotify logo and Apple Podcasts logo"`
>
> **Fallback final:** Si la edición tampoco funciona → añadir logos reales en Canva.

> **⚠️ Regla del footer:** Solo plataformas de streaming en el footer (Spotify · Apple Podcasts). Nunca redes sociales (Instagram, TikTok, LinkedIn) — esas van en los flyers de social media, no en la portada del episodio.

### Restricción final
```
No extra text outside specified overlays. Highly detailed, award-winning photography style. Brand colors throughout: #0A0A0A (Void Black), #C9A84C (Signal Gold), #F5F2EC (Off-white).
```

---

## Paso 3 — Generar los 3 formatos

| Formato | Dimensiones | Uso principal |
|---|---|---|
| **1:1** | 3000×3000px | Spotify, redes cuadradas, portada del episodio |
| **9:16** | 1080×1920px | Instagram Stories, TikTok, Reels — también para Día 2 de social media |
| **16:9** | 1920×1080px | YouTube thumbnail, LinkedIn, portada web |

Lo que cambia entre formatos:
- La composición del sujeto (centrado para 1:1, posicionado arriba para 9:16, en un lado para 16:9)
- El espacio tipográfico (diferente en cada formato)
- La instrucción de dimensiones al inicio

---

## Paso 4 — Especificaciones técnicas e instrucciones

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
  └─ Apple Podcasts: máx 4 MB (acepta JPEG o PNG)

  ⚠️ IMPORTANTE:
  Los modelos de IA generan PNG de alta resolución (50-100 MB).
  ANTES de subir a cualquier plataforma:
  1. Convierte a JPEG
  2. Comprime con squoosh.app (es gratis)
  3. Verifica que quede bajo 500 KB → sirve para las 2
──────────────────────────────────────────────────────
  CÓMO USAR EN GEMINI / NANI BANANA 2
──────────────────────────────────────────────────────
  1. Abre Gemini con Nani Banana 2 (si disponible)
  2. Pega el prompt del formato que necesitas
  3. Genera — el modelo produce 2-4 variantes
  4. Selecciona la mejor por formato
  5. Descarga
  
  Para la portada principal (formato 1:1):
  6. Convierte PNG a JPEG en squoosh.app
  7. Comprime hasta que esté bajo 500 KB
  8. Sube el mismo archivo a Spotify · Apple Podcasts
  
  Si el resultado no cumple:
  → Ajusta la descripción del sujeto (más detalles visuales)
  → Añade al final: "highly detailed, sharp focus, award-winning photography"
  → Cambia la referencia de iluminación
  → Si hay texto mal renderizado: especifica la fuente más (ej. "Helvetica Neue Bold Condensed")
  → Si los logos del footer salen mal: ver Regla de íconos arriba
──────────────────────────────────────────────────────
  ANIMACIONES (OPCIONAL — no parte del flujo estándar)
──────────────────────────────────────────────────────
  Kling AI y Google Flow/Veo 2 están disponibles para
  animar el artwork estático, pero NO se incluyen en
  este workflow por defecto.
  
  Razón: alto costo de tokens + riesgo de iteración.
  Si quieres animaciones, solicítalas por separado.
──────────────────────────────────────────────────────
```

---

## Paso 5 — Guardar prompts

1. Guarda los 3 prompts como `artwork-ep[NNN].md` en el directorio del proyecto.
2. Muestra resumen:

```
══════════════════════════════════════════
  Prompts de artwork generados ✓
══════════════════════════════════════════
  Episodio:  EP.[NNN]
  Formatos:  1:1 · 9:16 · 16:9
  Archivo:   artwork-ep[NNN].md
══════════════════════════════════════════
  → El próximo episodio preguntará si quieres
    reusar esta estructura como base.
  → La imagen 9:16 sirve también para el
    Día 2 de Stories en social media.
══════════════════════════════════════════
```

3. Pregunta: "¿Continuamos con el plan de social media?"
