# Artwork EP.005 — Aterciopelados

## REGENERADO 2026-07-17 vía pipeline local (ComfyUI + PIL) — versión vigente

Los prompts de Google Flow más abajo quedan como **referencia histórica de dirección visual**
(el primer intento, generado 2026-06-17, antes del cambio de formato solo). El set vigente para
publicar se regeneró el mismo día del cambio de formato usando el stack local (Z-Image Turbo +
composición determinista con PIL), siguiendo el patrón fijado desde BTQ EP.021
(memoria `feedback_local_artwork_pipeline`). Primera vez que MPD usa este pipeline.

**Assets finales:** `E:\Podcast\MPD\EP 05\artwork-local\`
- `EP005-1x1-FINAL-print.png` (3000×3000, para impresión/Spotify) + `EP005-1x1-FINAL-FOR-UPLOAD.jpg` (JPEG q85, 477 KB, bajo el límite de 500 KB)
- `EP005-16x9-FINAL.png` (1920×1080 — YouTube/web/LinkedIn)
- `EP005-9x16-FINAL.png` (1080×1920 — Stories/Reels/TikTok)
- `Q1-final.png` — La paradoja (guitarrista bajo un bombillo, silueta pura)
- `Q2-final.png` — El takeaway (azotea sobre Bogotá al atardecer)
- `Q3-final.png` — **Concepto nuevo:** dúo Cerati/Andrea cantando juntos en un mic vintage (evoca el Unplugged 1996), reemplaza el concepto original "la voz" de un solo cantante. Cita: "Una canción secreta, escrita para Cerati — nadie lo supo hasta que él murió."
- `Q4-final.png` — El riesgo (Caribe Atómico): disco de vinilo disolviéndose en partículas

**Herramientas creadas (reusables para futuros episodios de MPD):**
- `comfyui/templates/mpd-portada-compose.py` — función `compose()`: tipografía de marca MPD (dots + wordmark + MPD + EP/título/tagline + footer con flor + iconos) sobre una escena ya generada. Alineación se infiere del aspect ratio.
- `comfyui/templates/mpd-quote-card-compose.py` — función `compose_quote_card()`: mismo footer, gradiente oscuro inferior + cita de 2 líneas + atribución.
- Ambos son **importables** (no solo CLI) para evitar el problema de tildes perdidas al pasar argumentos con acentos por shell — invocar con strings Python literales desde un script, no vía `sys.argv`.

**Notas del proceso:**
- Escenas generadas SIN texto horneado (regla de `docs/prompting.md`, aprendida BTQ EP.022) — el modelo nunca genera texto legible, todo el texto se compone con PIL después.
- Icon strip del footer (Spotify/Apple Podcasts/Amazon Music) reutilizado recortando la fila inferior de `E:\Podcast\BTQ\EP 22\BTQ Artwork EP 22\BTQ-icon-strip-source.png` — mismos iconos reales, no hubo que regenerarlos.
- Un artefacto de render (blip blanco) en la escena 16:9 original se corrigió con clone-stamp en PIL antes de componer (`EP005-16x9-FINAL.png` ya tiene el fix).
- Q1 y Q3 (versión original "la voz") mostraban detalle facial parcial en el primer intento — resueltos con instrucciones de backlight más explícitas (Q1) y con un cambio de concepto completo (Q3, ver arriba). Lección: sobre-especificar "no mostrar X" en el positivo puede evocar X en vez de prevenirlo (confirmado en el segundo intento de Q3, que empeoró) — mejor describir la fuente de luz/ángulo que produce el resultado deseado que enumerar negaciones.
- Portada 1:1 nativa a 1536×1536, luego upscale con `RealESRGAN_x4plus.pth` + `ImageScale` a 3000×3000 exacto — texto compuesto DESPUÉS del upscale, nunca antes (evita blur de PIL por un upscaler pensado para fotos).

---

## Prompts originales (Google Flow) — referencia histórica, no vigente

Prompts para Google Flow (Imagen 3 / Nani Banana Pro). En inglés a propósito (los modelos responden mejor).

**Dirección visual:** MPD congelada (2026-06-12). Fotograma cinematográfico 35mm, NO diseño gráfico.
**Regla de oro #1:** CERO rostros reconocibles — siluetas y rim light solamente. No renderizar la cara de Andrea Echeverri ni de Héctor Buitrago. Mujer-silueta con guitarra, hombre-silueta con bajo.
**Regla de oro #2:** Texto SIEMPRE en tercio inferior sobre gradiente oscuro. Nunca centrado en la imagen.
**Regla de oro #3:** Render del texto EXACTO, letra por letra. Verificar tildes/eñes con zoom; si Flow daña una tilde dos veces, fallback en mayúsculas.
**Icono central del footer (EP.005):** una pequeña flor crimson estilizada (florecita) — guiño a "Florecita rockera" y a lo "aterciopelado".

---

## PORTADA — 1:1 (3000×3000px)

```
Square cinematic image, 1:1, 3000×3000px.
This must look like a film still from a late-1980s / early-1990s movie shot on 35mm —
NOT a graphic design, NOT illustration.

CENTER SCENE: silhouette of a woman with short hair standing defiant, holding an
electric guitar slung low, mid-performance. Slightly behind her, the silhouette of a
second figure holding a bass guitar. A tiny, gritty underground bar stage, a few
people in the shadowed foreground.
NO visible face detail anywhere — silhouettes and rim light only.
Lit from one side by deep crimson light #9B1C1C and from the other by warm golden
light, the two colors meeting on the edges of the silhouettes.
Heavy smoke, dust floating in the light beams, deep shadows, 35mm film grain,
high contrast, cinematic.
The bottom quarter of the image fades to near-black #0d0d0d.

TYPOGRAPHY:
  TOP CENTER:
    Five small silver dots in a horizontal row: · · · · ·
    Below dots: "MR. PUTRID'S DEN" — ultra-bold white condensed sans-serif, large
    Below that: "MPD" — small, crimson (#9B1C1C)

  BOTTOM THIRD, centered, over the dark gradient:
    Line 1 (silver #A8A8A8, small uppercase tracked): "EP.005"
    Line 2 (white bold condensed, large): "Aterciopelados"
    Line 3 (white italic, smaller): "De un bar de Bogotá al continente."
    Render text EXACTLY as written, letter by letter, no changes.

FOOTER BAR: solid #1a1a1a strip at very bottom, full width.
  Left: "Mr. Putrid's Den" in white small
  Center: "EP.005" in crimson (#9B1C1C) + small stylized crimson flower icon
  Right (silver #A8A8A8):
    1. Spotify: circle with three curved horizontal lines
    2. Apple Podcasts: rounded square with microphone and signal arc
    3. Amazon Music: wordmark "amazon music" with small orange curved arrow below
```

---

## PORTADA — 9:16 (1080×1920px) · Stories / Reels / TikTok

```
Vertical cinematic image, 9:16, 1080×1920px.
This must look like a film still from a late-1980s / early-1990s movie shot on 35mm —
NOT a graphic design, NOT illustration.

UPPER-CENTER SCENE: silhouette of a woman with short hair standing defiant, holding
an electric guitar slung low, mid-performance, positioned in the top two-thirds of the
tall frame. Behind her, the silhouette of a second figure with a bass guitar.
A gritty underground bar stage, smoke rising into the light.
NO visible face detail anywhere — silhouettes and rim light only.
Lit from one side by deep crimson light #9B1C1C and from the other by warm golden
light, meeting on the edges of the silhouettes.
Heavy smoke, dust in the beams, deep shadows, 35mm film grain, high contrast.
The bottom third of the image fades to near-black #0d0d0d.

TYPOGRAPHY:
  TOP CENTER:
    Five small silver dots in a row: · · · · ·
    Below dots: "MR. PUTRID'S DEN" — ultra-bold white condensed sans-serif
    Below that: "MPD" — small, crimson (#9B1C1C)

  LOWER THIRD, centered, over the dark gradient:
    Line 1 (silver #A8A8A8, small uppercase tracked): "EP.005"
    Line 2 (white bold condensed, large): "Aterciopelados"
    Line 3 (white italic, smaller): "De un bar de Bogotá al continente."
    Render text EXACTLY as written, letter by letter, no changes.

FOOTER BAR: solid #1a1a1a strip at very bottom, full width.
  Left: "Mr. Putrid's Den" in white small
  Center: "EP.005" in crimson (#9B1C1C) + small stylized crimson flower icon
  Right (silver #A8A8A8):
    1. Spotify: circle with three curved horizontal lines
    2. Apple Podcasts: rounded square with microphone and signal arc
    3. Amazon Music: wordmark "amazon music" with small orange curved arrow below
```

---

## PORTADA — 16:9 (1920×1080px) · YouTube / Web / LinkedIn

```
Cinematic widescreen image, 16:9, 1920×1080px.
This must look like a film still from a late-1980s / early-1990s movie shot on 35mm —
NOT a graphic design, NOT illustration.

LEFT-OF-CENTER SCENE: silhouette of a woman with short hair holding an electric guitar
slung low, mid-performance, placed on the left third of the wide frame. Behind her, the
silhouette of a second figure with a bass guitar. A gritty underground bar stage,
smoke drifting across the frame. Open negative space on the right for text.
NO visible face detail anywhere — silhouettes and rim light only.
Lit from one side by deep crimson light #9B1C1C and from the other by warm golden
light, meeting on the edges of the silhouettes.
Heavy smoke, dust in the beams, deep shadows, 35mm film grain, high contrast.
The bottom quarter fades to near-black #0d0d0d.

TYPOGRAPHY:
  TOP LEFT:
    Five small silver dots in a row: · · · · ·
    Below dots: "MR. PUTRID'S DEN" — ultra-bold white condensed sans-serif
    Below that: "MPD" — small, crimson (#9B1C1C)

  BOTTOM THIRD, right-aligned over the dark gradient:
    Line 1 (silver #A8A8A8, small uppercase tracked): "EP.005"
    Line 2 (white bold condensed, large): "Aterciopelados"
    Line 3 (white italic, smaller): "De un bar de Bogotá al continente."
    Render text EXACTLY as written, letter by letter, no changes.

FOOTER BAR: solid #1a1a1a strip at very bottom, full width.
  Left: "Mr. Putrid's Den" in white small
  Center: "EP.005" in crimson (#9B1C1C) + small stylized crimson flower icon
  Right (silver #A8A8A8):
    1. Spotify: circle with three curved horizontal lines
    2. Apple Podcasts: rounded square with microphone and signal arc
    3. Amazon Music: wordmark "amazon music" with small orange curved arrow below
```

---

## QUOTE CARDS — 16:9 (1920×1080px)

### Q1 — La paradoja
*Autoexplicativo: se entiende sin haber oído el episodio.*

```
Cinematic widescreen image, 16:9, 1920×1080px.
Dark atmospheric background: a small, gritty underground bar stage at night, a lone
guitar-player silhouette under a single bare bulb, a handful of people in the shadowed
crowd. Smoke, deep shadows, crimson and warm amber light. Full bleed, 35mm grain,
high contrast. NO visible face detail — silhouette only.

Dark gradient overlay at bottom third, from transparent at top to #0d0d0d at bottom.

TYPOGRAPHY — bottom third, centered, small-medium size:
  Line 1 (silver #A8A8A8, small uppercase tracked): "MR. PUTRID'S DEN · EP.005"
  Line 2 (white bold condensed): "La banda que medio continente cantó en la radio"
  Line 3 (same style): "había nacido para no sonar nunca en la radio."
  Render text EXACTLY as written, letter by letter, no changes.

FOOTER BAR: solid #1a1a1a strip at very bottom, full width.
  Left: "Mr. Putrid's Den" in white small
  Center: "EP.005" in crimson (#9B1C1C) + small stylized crimson flower icon
  Right (silver #A8A8A8):
    1. Spotify: circle with three curved horizontal lines
    2. Apple Podcasts: rounded square with microphone and signal arc
    3. Amazon Music: wordmark "amazon music" with small orange curved arrow below
```

### Q2 — El takeaway
*La frase central del episodio. Autoexplicativa.*

```
Cinematic widescreen image, 16:9, 1920×1080px.
Dark atmospheric background: a rooftop over the Bogotá skyline at dusk, mountains
faint in the haze, a single figure silhouette with an electric guitar looking out over
the city. Crimson and golden light on the horizon. Full bleed, moody, 35mm grain.
NO visible face detail — silhouette only.

Dark gradient overlay at bottom third, from transparent at top to #0d0d0d at bottom.

TYPOGRAPHY — bottom third, centered, small-medium size:
  Line 1 (silver #A8A8A8, small uppercase tracked): "MR. PUTRID'S DEN · EP.005"
  Line 2 (white bold condensed): "A veces la única forma de sonar universal"
  Line 3 (same style): "es sonar a lo que uno es."
  Render text EXACTLY as written, letter by letter, no changes.

FOOTER BAR: solid #1a1a1a strip at very bottom, full width.
  Left: "Mr. Putrid's Den" in white small
  Center: "EP.005" in crimson (#9B1C1C) + small stylized crimson flower icon
  Right (silver #A8A8A8):
    1. Spotify: circle with three curved horizontal lines
    2. Apple Podcasts: rounded square with microphone and signal arc
    3. Amazon Music: wordmark "amazon music" with small orange curved arrow below
```

### Q3 — La voz
*La voz de Andrea, sin nombrarla, autoexplicativo.*

```
Cinematic widescreen image, 16:9, 1920×1080px.
Dark atmospheric background: a woman silhouette singing into a vintage microphone,
head tilted, mouth open mid-note, backlit by a single crimson and golden spotlight,
smoke around her. Full bleed, dramatic, 35mm grain, high contrast.
NO visible face detail — silhouette and rim light only.

Dark gradient overlay at bottom third, from transparent at top to #0d0d0d at bottom.

TYPOGRAPHY — bottom third, centered, small-medium size:
  Line 1 (silver #A8A8A8, small uppercase tracked): "MR. PUTRID'S DEN · EP.005"
  Line 2 (white bold condensed): "En una época que quería voces dulces,"
  Line 3 (same style): "llegó una voz con filo que no pedía permiso."
  Render text EXACTLY as written, letter by letter, no changes.

FOOTER BAR: solid #1a1a1a strip at very bottom, full width.
  Left: "Mr. Putrid's Den" in white small
  Center: "EP.005" in crimson (#9B1C1C) + small stylized crimson flower icon
  Right (silver #A8A8A8):
    1. Spotify: circle with three curved horizontal lines
    2. Apple Podcasts: rounded square with microphone and signal arc
    3. Amazon Music: wordmark "amazon music" with small orange curved arrow below
```

### Q4 — El riesgo (Caribe Atómico)
*El gesto artístico. Autoexplicativo.*

```
Cinematic widescreen image, 16:9, 1920×1080px.
Dark atmospheric background: a vinyl record mid-air, dissolving at one edge into glowing
electronic particles and light, a hand silhouette having just let it go. Crimson and
golden light, smoke, deep shadows. Full bleed, surreal but photographic, 35mm grain.
NO visible face detail.

Dark gradient overlay at bottom third, from transparent at top to #0d0d0d at bottom.

TYPOGRAPHY — bottom third, centered, small-medium size:
  Line 1 (silver #A8A8A8, small uppercase tracked): "MR. PUTRID'S DEN · EP.005"
  Line 2 (white bold condensed): "Tenían la fórmula del éxito en la mano."
  Line 3 (same style): "Y la botaron a la basura."
  Render text EXACTLY as written, letter by letter, no changes.

FOOTER BAR: solid #1a1a1a strip at very bottom, full width.
  Left: "Mr. Putrid's Den" in white small
  Center: "EP.005" in crimson (#9B1C1C) + small stylized crimson flower icon
  Right (silver #A8A8A8):
    1. Spotify: circle with three curved horizontal lines
    2. Apple Podcasts: rounded square with microphone and signal arc
    3. Amazon Music: wordmark "amazon music" with small orange curved arrow below
```

---

## Recordatorio técnico

- **Antes de aprobar cualquier generación:** (a) texto letra por letra, sin palabras inventadas; (b) cero detalle facial; (c) parece foto de película, no póster.
- **Si sale perfecta salvo el texto:** modo edición de Flow sobre la misma imagen ("same image, fix only the text") — no regenerar desde cero.
- **Si los logos salen mal:** edición de Flow → "replace the logos for Spotify logo, Amazon Music logo, and Apple Music logo". Fallback: logos reales en Canva.
- **Portada 1:1 para subir:** PNG → JPEG en squoosh.app → comprimir bajo 500 KB (sirve para Spotify, Apple y Amazon).
```
