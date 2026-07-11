# Brand constants (BTQ)

| Element | Value |
|---------|-------|
| Background | Void Black `#0A0A0A` |
| Accent | Signal Gold `#C9A84C` |
| Off-white | `#F5F2EC` |
| Headline font | Playfair Display |
| Body | DM Sans |
| Accent | Bebas Neue |
| Headsets | Contact center boom mic — NEVER music headphones |
| Spotify category | Society & Culture |
| Primary language | Spanish |
| Core audience | Hombre 35–44, supervisor/gerente BPO — Colombia 70% + EE.UU. 20% (analytics 2026-06-12) |
| Nostalgia era | Referentes y estética 80s/90s — la adolescencia de la audiencia núcleo |
| Priority platform | LinkedIn (profesional 35–44; 15% escucha en desktop en el trabajo) |

---

## Dirección de artwork (CONGELADA v3 — 2026-07-04 — restaurada de EP.10 Kratos)

> **Historial:** la dirección original de EP.10 (Kratos/God of War) tenía más capas de
> diseño de las que sobrevivieron — postura narrativa (de espaldas, reflexionando, no de
> frente a cámara), una SEGUNDA figura a otra escala para crear relación, un símbolo
> watermark del universo del referente, y una tipografía en capas (5 puntos + wordmark +
> "BTQ"). Esa riqueza se perdió cuando se "congeló" v1 el 2026-06-12 (EP.017-019: figura
> única, de frente, parada, en humo dorado) — el usuario lo calificó de genérico. Se probó
> v2 (cómic pulp ilustrado, 2026-07-04) y tampoco convenció. **v3 restaura la fórmula de
> EP.10 como el estándar oficial** — no es una idea nueva, es recuperar lo que ya
> funcionaba antes de simplificarse de más.

**BTQ = imagen editorial cinemática, render con volumen (no silueta plana) + patrón
geométrico watermark del universo del referente.** Lo que define el estilo es la TEXTURA
del render — figuras con volumen y material real (músculo, armadura, tela), sombreadas en
tonos oscuros con luz dorada ambiental/de contorno, como una estatua oscura iluminada desde
atrás — no un recorte plano de silueta lisa (esa era la falla de v1). El número de figuras
NO es una regla fija: una sola figura protagonista está perfecto si la historia es de un
solo personaje; una segunda figura a otra escala se usa SOLO cuando la relación (maestro/
aprendiz, líder/sucesor) es parte central de la historia de ese episodio — no forzarla si
no aplica.

Bloques que se copian VERBATIM en todo prompt de portada (cambian el sujeto, si aplica una
segunda figura, el patrón geométrico y el título):

**[BLOQUE CONGELADO — ATMÓSFERA BTQ v3]**
```
Dark cinematic editorial image, rendered with real volume and material
texture (muscle, armor, fabric) — NOT a flat silhouette cutout. Void
black background #0A0A0A.

Center composition: dramatic figure of [FIGURA PRINCIPAL], seen from
behind or at an angle — [describir la postura/acción concreta del
personaje]. Dark, moody shading with warm golden #C9A84C rim light and
ambient glow outlining the figure, like a dark statue lit from behind.

[SI APLICA — solo cuando la relación es parte central de la historia:
to one side, smaller in scale, a second figure of [FIGURA SECUNDARIA]
— creating a size contrast that tells a relationship.]

Background: a geometric pattern drawn from the referent's own
culture/era (e.g. Greek key / meander for Ancient Greece), rendered in
thin gold #C9A84C line art — subtle, like an engraved watermark, not
competing with the figure.

DO NOT render any concentric ring, circle, halo, or archery-target
pattern anywhere in this image.

No circuit boards. No cartoon style. Cinematic.
```

**[BLOQUE CONGELADO — TIPOGRAFÍA + FOOTER BTQ v3]**
```
Typography:
- Top center: five small gold #C9A84C dots
- "BEHIND THE QUEUE" — ultra bold white condensed sans-serif, large
- "BTQ" — small gold below

Below silhouettes:
"[Título del episodio: referente + gancho de liderazgo]"
White text, bold

Footer black bar at bottom:
- Left: "Behind the Queue" white
- CENTER: "EP.0XX" gold #C9A84C — prominent
- Right two rows:
  Row 1: Facebook icon, Instagram icon, TikTok icon
  Row 2: Spotify icon, Apple Podcast icon, Amazon Music icon

Do NOT place any text in the bottom-right corner.
Format: square 3000x3000px.
```

**Regla de rostros:** el rostro puede verse parcialmente si la postura lo expone (de
perfil, de espaldas mostrando poco), pero no es el foco — el énfasis está en el volumen del
cuerpo/armadura y el rim light, no en el detalle facial. Persona real → mantenerlo de
espaldas/en sombra por likeness; ficticio → hay más libertad, pero seguir sin buscar el
primer plano de cara.

**Reglas de la dirección:**
1. **Número de figuras según la historia, no una regla fija.** Una sola figura protagonista
   es válida por defecto; sumar una segunda a otra escala SOLO si la relación (maestro/
   aprendiz, líder/sucesor) es parte central de la historia de ese episodio específico —
   no inventar un segundo personaje que no viene al caso.
2. **Render con volumen y textura de material, nunca silueta plana.** Músculo, armadura,
   tela con sombreado real + luz dorada de contorno — como una estatua oscura iluminada
   desde atrás, no un recorte negro liso (esa era la falla de v1).
3. **Fondo: SOLO el patrón geométrico del universo del referente** (greca griega para
   Kratos; para otro referente, el patrón equivalente de esa cultura/época — un mosaico
   romano, scan-lines de TV analógica, un patrón art-deco de los 80s, etc.) en línea fina,
   tipo marca de agua, sin competir con la figura ni el texto. **Los círculos concéntricos/
   anillos/diana están VETADOS en todas las imágenes — portadas Y quote cards (decisión de
   Andy 2026-07-10, EP.021; antes el motivo estaba "reservado para la portada" y por eso
   reaparecía).** Única excepción: cuando la diana ES el sujeto central de la escena (ej.
   Q2 de EP.020). Incluir el ban explícito en el prompt desde el primer intento.
4. **Conteo explícito de figuras:** "EXACTLY [N]" para cada silueta — sigue siendo el error
   más frecuente de Flow.
5. **Tipografía:** texto exacto entre comillas + "render text EXACTLY as written, letter
   by letter, no changes". Verificar letra por letra con zoom antes de aprobar. Si Flow
   genera la escena pero OMITE el texto: NO regenerar — modo edición sobre la misma imagen
   ("same image, keep everything identical, add text...").
6. **Checklist antes de aprobar:** (a) render con volumen/textura real, no silueta plana,
   (b) número de figuras justificado por la historia (no forzado a 2), (c) patrón
   geométrico del universo correcto de fondo y CERO círculos/anillos/diana (Flow los
   reinserta solo — verificar), (d) texto letra por letra, (e) footer con las 2 filas de
   íconos completas.

Prompt de referencia validado: EP.10 (Kratos/Atreus, Omega griego de fondo) — ver bloque de
arriba, es el prompt real usado. El primer prompt v3 aplicado a un episodio nuevo se prueba
contra Gladiator EP.019 — ver `btq-production/launch-assets/EP019-gladiator-artwork-v3-test.md`.

---

## Quote Cards — mismo tratamiento cinematográfico que la portada (desde 2026-07-05, EP.020)

> **Actualización 2026-07-11 (EP.021, aprobada por Andy):** las quote cards BTQ ahora se
> producen LOCALMENTE — escena vía ComfyUI (skill `comfyui`) + texto compuesto
> determinista con PIL (cita off-white + atribución gold sobre la mitad negra). El texto
> ya NO se genera con el modelo, así que los patrones de fallo de Flow de abajo solo
> aplican si se usa Flow como fallback. **Formato: 16:9 (1920x1080)** — el split 50/50 se
> mantiene (mitad negra texto / mitad escena), solo cambió la proporción; 1:1 únicamente
> si se necesita para feed de Instagram. Citas verbatim validadas contra el SRT real.
> Procedimiento compartido para los 3 shows en `episode-pipeline/workflows/03b-marketing.md`.

**Cambio de dirección:** hasta EP.019 las quote cards usaban un estilo propio —
"Graphic editorial poster design — NOT photorealistic 3D" (más plano, tipo póster/
halftone). Desde EP.020 quedan retiradas: las quote cards usan el MISMO render
cinematográfico/con volumen real que la portada (bloque congelado de ATMÓSFERA BTQ v3
de arriba), no un estilo aparte. Razón: el usuario calificó el estilo póster plano de
"boring/sketchy" al compararlo lado a lado con la portada — quiere una sola identidad
visual consistente entre portada y quote cards, no dos.

**Cómo aplicar a partir de EP.021:**
- Composición: se mantiene el split 50/50 (mitad negro con texto, mitad escena) — eso
  no cambió, solo el render de la escena.
- Escena: cualquier objeto/entorno que ilustre la cita, renderizado con volumen y
  textura de material real (vidrio, metal, tela, madera — lo que aplique), sombreado
  oscuro + luz dorada de contorno ambiental, "like a dark statue lit from behind" —
  igual que la figura de la portada, no una silueta plana ni textura de póster/
  halftone/screen-print.
- Encabezar cada prompt con: "Dark cinematic editorial image, rendered with real
  volume and material texture — NOT a flat graphic poster, NOT a silhouette cutout."
  y cerrar con "No circuit boards. No cartoon style. No flat poster texture. Cinematic."
  (mismo patrón que el bloque congelado de portada).
- Checklist de aprobación: agregar el ítem "render con volumen/textura real — NO plano
  ni tipo póster" a la lista existente de cada card (texto letra por letra, mitad negro
  reservada, etc.).
- **NO agregar el anillo/círculo concéntrico dorado (diana) de fondo en las quote
  cards** — desde 2026-07-10 (EP.021) el motivo está vetado en TODAS las imágenes,
  incluida la portada (ver §Reglas de la dirección #3); ya no existe el caso "reservado
  para la portada". Única excepción: escenas donde la diana ES el sujeto central (ej.
  Q2 de EP.020). Cada escena ya lleva su propio objeto como metáfora, no hace falta
  reforzarlo con el anillo dorado detrás.
- **Sí darle a cada card un elemento de fondo propio, desenfocado (profundidad de
  campo), relevante al tema específico de esa cita** — sin el anillo, un objeto solo
  flotando en negro puro puede sentirse repetitivo entre las 4 cards del mismo
  episodio. El fondo debe ser distinto por card (no reciclar el mismo elemento en dos
  cards), muy fuera de foco para no competir con el objeto principal ni el texto, y
  coherente con el mundo del episodio (ej. EP.020: bullpen de contact center, pared de
  medidores, display de turnos, fila de escritorios — cuatro variantes del mismo
  universo, cuatro objetos distintos).

Ver `btq-production/launch-assets/EP020-metricas-launch.md` §E como primera aplicación
de esta dirección (las 4 quote cards reescritas 2026-07-05, anillo de fondo retirado en
la misma sesión).

**Patrones de fallo conocidos de Flow (aplicar preventivamente, no esperar a que falle):**
- **Reinserta el anillo genérico solo:** aunque el prompt pida otro fondo (bullpen,
  medidores, display de turnos, fila de escritorios), Flow tiende a devolver el anillo
  dorado de la portada igual — pasó en Q1, Q3 y Q4 de EP.020 en su primer intento. Por
  eso, TODO prompt de imagen BTQ — portada Y quote cards (salvo la escena donde el
  anillo/diana ES el sujeto) — debe incluir DESDE EL PRIMER intento la línea explícita:
  "DO NOT render any concentric ring, circle, halo, or archery-target pattern anywhere
  in this image." No esperar a la primera falla para agregarla.
- **Autocorrige palabras deliberadamente sin tilde:** si el texto de una card pide una
  palabra sin acento por regla de marca (ej. "NUMERO", "TERMOMETRO") pero es la
  ortografía estándar del español con tilde, Flow puede seguir renderizándola acentuada
  pese a instrucciones explícitas — en EP.020 sobrevivió al prompt original + 2 rondas
  de edición dirigida sobre la misma palabra. **Regla de corte:** si after 2 intentos de
  edición dirigida ("keep everything identical, only fix word X") la palabra sigue mal,
  DEJAR de reintentar en Flow — la escena ya validada se aprueba, y esa palabra puntual
  se corrige por fuera (overlay/recorte en un editor simple como Canva) en vez de seguir
  quemando generaciones en el mismo punto.
