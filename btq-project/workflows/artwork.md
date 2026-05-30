# Workflow: Artwork Prompts BTQ

Genera prompts listos para Flow / Nani Banana 2 en los 3 formatos del episodio.

---

## Step 0 — Verificar si existe un prompt de referencia

**ANTES de escribir cualquier prompt con personajes, mechs o criaturas:**
Buscar imagen de referencia oficial del personaje/mech en la web o pedirla al usuario. Nunca confiar en descripción de memoria.

Por qué: Old Snake MGS4 generó múltiples correcciones (Solid Eye lado incorrecto, LED color equivocado, barba completa en vez de bigote, sin bandana). Metal Gear RAY salió como dinosaurio. Ambos errores eran evitables con una imagen de referencia antes de escribir el prompt.

Flujo obligatorio para personajes/mechs:
1. WebSearch "[personaje] official artwork [juego/película] [año]" — o pedir imagen al usuario
2. Extraer specs visuales críticos en ALL CAPS del diseño oficial
3. Escribir el prompt con esos specs — nunca de memoria

**TAMBIÉN**, preguntar: "¿Tienes un prompt de episodio anterior como referencia para este tipo de obra (anime / videojuego / película / música)?"

Si Andy comparte uno → usarlo como plantilla base y adaptar al nuevo episodio.
Si no existe → usar la plantilla de esta sección y adaptar.

El prompt del EP.012 (Bohemian Rhapsody / Queen) es la referencia canónica para episodios musicales con personajes reales.

---

## Reglas core — no negociables

- **Siempre en color** — cinematic, photographic, warm. Nunca monocromo ni desaturado
- **4K cinematic** — hyperrealistic skin texture, film grain, 35mm Kodak aesthetic
- **Nunca PCB/circuits** a menos que el episodio sea explícitamente sobre AI o tech
- **Nunca texto en esquina inferior derecha** — watermark de Flow/Veo vive ahí
- **EP number SIEMPRE al centro del footer** — nunca esquina derecha
- **Headset cuando aparezca:** boom microphone arm desde el ear cup hacia la cara — contact center style, NUNCA music headphones
- **Nani Banana 2 siempre genera 4 candidatos** — pedir a Andy que elija uno antes de guardar

**Brand colors como luz real (EP.015+):**
El gold #C9A84C debe aparecer como fuente de luz real dentro de la escena — no solo en la tipografía overlay. Ejemplos validados:
- Rail gun cargando emite gold glow (REX)
- Luz gold reflejada en agua del dock (RAY)
- Corredor con fuente de luz gold al fondo (Snake silhouette)
- Split lighting gold/cold-blue en rostro (Old Snake)
- Pantalla gold activa vs. pantalla muerta gris (Codec)

Fórmula: una fuente de luz gold + rim light frío opuesto = BTQ palette viva en el ambiente. Aplica a todas las quote cards e imágenes del episodio.

---

## Tipografía master (todos los formatos)

```
Top center: five small gold #C9A84C dots
"BEHIND THE QUEUE" — ultra bold white condensed sans-serif, large
"BTQ" — small gold #C9A84C below
Below figures: [episode subtitle] — white text, bold
```

## Footer master (todos los formatos)

```
Footer black bar at bottom:
- Left: "Behind the Queue" white
- CENTER: "EP.0XX" gold #C9A84C — prominent, with character silhouettes
- Right two rows:
  Row 1: Facebook icon, Instagram icon, TikTok icon
  Row 2: Spotify icon, Apple Podcast icon, Amazon Music icon
Do NOT place any text in the bottom-right corner.
```

---

## División de responsabilidades: Laswell vs. Flow agent

| Quién | Qué genera |
|---|---|
| **Flow agent** | Descripción visual del personaje — a partir de imagen de referencia oficial |
| **Laswell** | Bloque de layout BTQ — tipografía + footer + formato |

Andy sube la imagen de referencia al agente de Flow → Flow describe el visual → Andy agrega el bloque de layout de Laswell → genera.

**Regla de corrección — prompt completo siempre:**
Cuando se corrija un prompt para Flow/Nani Banana 2, entregar SIEMPRE el prompt completo corregido — nunca solo el fragmento modificado. Flow no toma correcciones parciales correctamente. Incluso si el cambio es solo un panel de un triptych, reescribir el prompt completo con la corrección integrada.

---

## Plantilla de layout BTQ — lo que genera Laswell

```
[Visual del personaje — generado por Flow agent desde imagen de referencia]

Typography:
- Top center: five small gold #C9A84C dots
- "BEHIND THE QUEUE" — ultra bold white condensed sans-serif, large
- "BTQ" — small gold #C9A84C below
- Below figure: "[Subtítulo del episodio]" — white text, bold

Footer black bar at bottom:
- Left: "Behind the Queue" white
- CENTER: "EP.0XX" gold #C9A84C — prominent with character silhouettes
- Right two rows:
  Row 1: Facebook icon, Instagram icon, TikTok icon
  Row 2: Spotify icon, Apple Podcast icon, Amazon Music icon

No circuit boards. No Live-Action, No Rendering.
Do NOT place any text in the bottom-right corner.
Format: [tamaño según formato].
```

**Chibi / Neko — mismo principio:** Flow agent describe el visual desde referencia. Indicar en el prompt de Flow: `chibi Neko version` para que el agente ajuste las proporciones y agregue orejas/cola.

---

## Formatos por episodio

| Formato | Tamaño | Uso | Composición |
|---|---|---|---|
| 1:1 | 3000×3000px | Portada de plataforma, feed posts | PRIMARY — composición central |
| 9:16 | 1080×1920px | TikTok, Stories | Stack vertical de personajes |
| 16:9 | 1920×1080px | LinkedIn | Spread horizontal |

Generar los 3 formatos por episodio. Adaptar composición de personajes por formato.

---

## Guía de adaptación por tipo de episodio

**Anime — versión principal** (Frieren, Dragon Ball, Saint Seiya, Maomao):
- Nombrar el personaje directamente en el prompt — el modelo respeta el diseño canónico cuando tiene nombre + specs exactos
- Describir colores, ropa y rasgos EN MAYÚSCULAS basados en el diseño oficial — NO inventar ni "interpretar"
- Verificar siempre vs. referencia visual oficial antes de dar "chidori"
- **Apertura canónica (exacta, sin variaciones):** `Color cinematic anime image 4k.`
- **NUNCA usar estas palabras en prompts de anime:** `live-action` · `photographic` · `rendering` · `rendered` · `render` — todos son triggers de photorealism/live-action que hacen que el modelo genere en estilo humano real en vez de anime

**Anime — variante Chibi / Neko** (validado EP.014 Maomao, mayo 2026):
- **Apertura canónica:** `Color cinematic anime image chibi Neko version, No Live-Action, No Rendering.`
- Chibi: proporciones cabeza grande (60–70% del cuerpo), cuerpo pequeño y simplificado, ojos muy expresivos
- Neko: orejas de gato del COLOR DEL CABELLO del personaje + cola pequeña del mismo color
- Specs del personaje (colores, ropa, expresión) permanecen idénticos a la versión principal
- Prohibición aplica igual: sin `live-action`, sin `rendering`, sin `photographic`

**Videojuego** (God of War, Metal Gear, The Last of Us):
- Los personajes ficticios se pueden nombrar directamente
- Referenciar la estética de cutscenes cinematográficas del juego
- Rendering hiperrealista — estos personajes ya tienen diseños high-fidelity
- Incluir props/armas icónicos como anclas visuales

**Película / Música — personas reales** (actores, músicos):
- **NO nombrar a la persona real** — riesgo de flag por copyright/likeness
- Usar versión silueta/sombra: "a silhouette figure suggesting [descripción física genérica del personaje]"
- Para músicos: silueta en escenario con instrumento icónico, sin rostro visible
- Para actores: silueta o figura en sombras con vestuario icónico del personaje, sin rasgos faciales claros
- El personaje ficticio sí puede nombrarse (Marty McFly, Doc Brown) — la restricción es sobre el actor real, no el personaje

---

## Notas críticas de personajes — actualizar con cada episodio

| Episodio | Personaje | Specs críticos |
|---|---|---|
| EP.011 | Himmel (Frieren) | BLUE HAIR — NOT blonde. ALL CAPS en el prompt. |
| EP.011 | Eisen (Frieren) | SHORT AND STOCKY — shorter than Frieren. NOT tall. |
| EP.012 | Freddie Mercury | ⚠ PERSONA REAL — usar silueta/sombra sin nombrar. Thick dark mustache (later era), jet-black short hair, warm olive skin |
| EP.012 | Brian May | ⚠ PERSONA REAL — usar silueta/sombra sin nombrar. MASSIVE halo of long CURLY DARK BROWN hair |
| EP.012 | Roger Taylor | ⚠ PERSONA REAL — usar silueta/sombra sin nombrar. Long wavy BLONDE shoulder-length hair |
| EP.012 | John Deacon | ⚠ PERSONA REAL — usar silueta/sombra sin nombrar. Short DARK BROWN hair, clean-cut |
| EP.013 | Marty McFly / Doc Brown | ⚠ PERSONAS REALES (actores). Nombres de actores SÍ funcionaron en producción (Christopher Lloyd, Michael J. Fox). Approach: photorealistic 1985 film era, 35mm Kodak Portra aesthetic. Los personajes ficticios (Marty, Doc) se nombran directamente. |
| EP.014 | Maomao (Kusuriya no Hitorigoto) | DARK TEAL-GREEN hair in low twin pigtails with small colored beads (red + teal). BRIGHT BLUE eyes. Freckle cluster on nose bridge. Green hanfu servant robes. NOT silver. NOT grey-violet eyes. NOT pink robes. |
| EP.015 | Solid Snake — MG1 era (1987) | Early 20s. Short jet-black hair. Clean-shaven. Olive-drab military jacket, worn fabric. NOT sneaking suit yet. |
| EP.015 | Solid Snake — MGS1 era (1998) | Mid-30s. BLUE BANDANA on forehead. CHARCOAL-GRAY sneaking suit — NOT pure black — subtle teal undertone, panel seams, utility belt. 3-day stubble. Steel-blue eyes. SOCOM pistol. |
| EP.015 | Old Snake — MGS4 era (2008) | Appears 60s. WHITE hair swept dramatically back. GREY MUSTACHE — NOT full beard. Deep wrinkles, weathered aged skin. DARK GREY BANDANA covering forehead down to nose bridge — only one eye visible below. SOLID EYE on RIGHT side — lateral sensor device extending from right eye, RED/ORANGE LED (NOT green, NOT eyepatch). BLACK mesh tactical bodysuit with harness straps. CRITICAL: the bandana + mustache combo is what distinguishes Old Snake from Big Boss — do not omit either. |

Agregar a esta tabla cada vez que Andy corrija un detalle de personaje después de la generación.
