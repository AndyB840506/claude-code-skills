# BTQ Web Overhaul Guide
## behind-thequeue.com — Wix Implementation

**Fecha:** Mayo 2026  
**Estado del sitio al inicio:** 5 de 7 páginas en 404  
**Prioridad máxima:** Arreglar navegación rota antes de cualquier diseño

---

## Cómo usar esta guía

1. Abre el editor de Wix en `manage.wix.com`
2. Sigue las páginas en el orden de este documento (Home → Episodios → About → Escuchar → Contacto)
3. Copia el texto de cada sección directamente desde aquí — está listo para pegar
4. Al terminar cada página: **Publish** antes de pasar a la siguiente
5. Al finalizar todo: verificar navegación desde incógnito en `behind-thequeue.com`

---

## PASO 0 — Arreglar navegación (hacer PRIMERO)

En Wix Editor → Pages & Menu:

| Página | Acción |
|---|---|
| Episodios | Crear nueva página, URL: `/episodios` |
| About | Crear nueva página, URL: `/about` |
| Escuchar | Crear nueva página, URL: `/escuchar` (eliminar o redirigir `/suscribirse`) |
| Contact | Crear nueva página, URL: `/contact` |
| Bio | Redirigir `/bio` → `/about` (en Wix: 301 redirect en Settings) |

**SEO global — hacer una sola vez:**
- Wix Dashboard → SEO → Personalized SEO Plan → establecer versión canónica como `behind-thequeue.com` (sin www)
- Subir favicon con el logo BTQ (si no está)
- Crear OG Image 1200×630px en colores BTQ (fondo negro, texto oro) y subir en SEO → Social Share Image

---

## PÁGINA 1 — Home

**SEO:**
- Title tag: `Behind the Queue — Podcast de liderazgo y CX en español`
- Meta description: `Conversaciones sobre liderazgo, servicio al cliente y experiencias humanas. Un podcast para profesionales de operaciones en LATAM. Escúchalo en Spotify.`
- H1: `Las experiencias que no se olvidan ocurren por decisión.`

---

### Sección 1 — Hero

**Visual:** Fondo Void Black `#0A0A0A`. Texto en Off-white `#F5F2EC`. Botón CTA en Signal Gold `#C9A84C`. Fuente: Playfair Display Bold.

**Contenido:**

```
[Encima del título — texto pequeño en Signal Gold, Bebas Neue]
BEHIND THE QUEUE · TEMPORADA 2

[Título principal — Playfair Display Bold, grande]
Las experiencias que no se olvidan
ocurren por decisión.

[Subtítulo — DM Sans, tamaño mediano, Off-white]
Un podcast en español sobre liderazgo, servicio al cliente
y las decisiones que definen equipos.

[Botón CTA — fondo Signal Gold, texto negro]
ESCUCHAR EN SPOTIFY

[Texto debajo del botón — pequeño, Off-white 60% opacidad]
También disponible en Apple Podcasts
```

---

### Sección 2 — Qué es BTQ

**Visual:** Fondo `#111111`. Texto Off-white. Ancho máximo de columna: 720px, centrado.

```
[Título de sección — Playfair Display, Signal Gold]
Sobre el podcast

[Cuerpo — DM Sans Regular]
Behind the Queue es un podcast en español para profesionales
de operaciones, liderazgo y servicio al cliente.

Cada episodio parte de una obra cultural — un videojuego, una
película, un anime, una canción — y extrae los principios que
definen cómo se construyen equipos, se toman decisiones y se
crea una experiencia que la gente no olvida.

No es un podcast de motivación. Es un podcast para quien
lleva años en la industria y quiere ver su trabajo desde
un ángulo diferente.

[Texto pequeño, Signal Gold]
Temporada 2 — EP.010 en adelante
```

---

### Sección 3 — Episodios destacados

**Visual:** Fondo Void Black. Grid de 2 columnas (desktop) / 1 columna (mobile). Cada card: borde izquierdo 3px Signal Gold, fondo `#111111`, padding interno.

**Cards (una por episodio, en este orden):**

```
[Card EP.013]
EP.013 · Back to the Future
"Back to the Future: la mentoría que cambió el futuro"
─────────────────────────────────────
"Tu futuro todavía no está escrito. Hazlo uno bueno."
[Link: → Escuchar en Spotify]  ← link al episodio específico en Spotify

[Card EP.012]
EP.012 · Bohemian Rhapsody
"La experiencia que nadie pidió — y todos recordaron para siempre"
─────────────────────────────────────
"Las reglas son útiles. Romperlas con propósito es arte."
[Link: → Escuchar en Spotify]

[Card EP.011]
EP.011 · Frieren
"El costo de no valorar a tu equipo hasta que ya no está"
─────────────────────────────────────
"Lo que tienes hoy no va a estar para siempre."
[Link: → Escuchar en Spotify]

[Card EP.010]
EP.010 · God of War
"Kratos: el líder que dejó de gritar"
─────────────────────────────────────
[Link: → Escuchar en Spotify]
```

**Botón al final de la sección:**
```
[Botón — borde Signal Gold, fondo transparente, texto Signal Gold]
VER TODOS LOS EPISODIOS → /episodios
```

---

### Sección 4 — Quote de marca

**Visual:** Fondo Signal Gold `#C9A84C`. Texto Void Black `#0A0A0A`. Centrado. Fuente: Playfair Display Bold Italic.

```
"Las experiencias que no se olvidan
ocurren por decisión."

— Behind the Queue
```

---

### Sección 5 — Plataformas

**Visual:** Fondo `#111111`. Iconos de plataformas en fila, Off-white, con link.

```
[Título pequeño — DM Sans, Off-white]
Disponible en

[Iconos con links — en fila]
🎵 Spotify     🍎 Apple Podcasts
```

---

## PÁGINA 2 — /episodios

**SEO:**
- Title tag: `Episodios — Behind the Queue Podcast`
- Meta description: `Todos los episodios de Behind the Queue. Liderazgo, CX y decisiones humanas a través de videojuegos, películas y música. Temporada 2 disponible.`
- H1: `Episodios`

---

### Sección 1 — Header

**Visual:** Fondo Void Black. Texto Off-white. Línea decorativa Signal Gold debajo del título.

```
[Encima — pequeño, Signal Gold, Bebas Neue]
BEHIND THE QUEUE · TEMPORADA 2

[H1 — Playfair Display Bold]
Episodios

[Subtítulo — DM Sans]
Cada episodio parte de una obra cultural
y extrae lo que te sirve para el trabajo real.
```

---

### Sección 2 — Grid de episodios

**Visual:** 1 columna, stack vertical. Cada card: fondo `#111111`, borde izquierdo 4px Signal Gold, número EP en Signal Gold grande (Bebas Neue), título en Playfair Display.

**Cards completas:**

```
┌─────────────────────────────────────────────────┐
│ EP.013  ·  Back to the Future                   │
│                                                  │
│ Back to the Future: la mentoría que              │
│ cambió el futuro                                 │
│                                                  │
│ La historia de Marty y Doc Brown vista desde     │
│ el único ángulo que nadie había usado: el de     │
│ la mentoría. Qué diferencia a un jefe de un      │
│ mentor. Y cómo uno de ellos puede cambiar        │
│ el arco completo de una carrera.                 │
│                                                  │
│ "Tu futuro todavía no está escrito.              │
│  Hazlo uno bueno."                               │
│                                   [→ Spotify]   │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ EP.012  ·  Bohemian Rhapsody                    │
│                                                  │
│ La experiencia que nadie pidió —                 │
│ y todos recordaron para siempre                  │
│                                                  │
│ Bohemian Rhapsody no debería haber existido.     │
│ Era demasiado larga, demasiado rara, demasiado   │
│ difícil de clasificar. Y es la canción más       │
│ transmitida de todos los tiempos en Spotify.     │
│ Qué nos dice eso sobre cómo se crean las         │
│ experiencias que la gente no olvida.             │
│                                                  │
│ "Las reglas son útiles. Romperlas con            │
│  propósito es arte."                             │
│                                   [→ Spotify]   │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ EP.011  ·  Frieren                               │
│                                                  │
│ El costo de no valorar a tu equipo               │
│ hasta que ya no está                             │
│                                                  │
│ Frieren vive durante siglos pero apenas recuerda │
│ a las personas que pasaron por su vida. Cuando   │
│ finalmente entiende lo que perdió, es demasiado  │
│ tarde. Una conversación sobre presencia, equipo  │
│ y lo que cuesta darse cuenta tarde.              │
│                                                  │
│ "Lo que tienes hoy no va a estar para siempre.  │
│  Valóralo antes de que se convierta en recuerdo."│
│                                   [→ Spotify]   │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ EP.010  ·  God of War                           │
│                                                  │
│ Kratos: el líder que dejó de gritar             │
│                                                  │
│ Kratos pasó siglos siendo puro fuego y           │
│ destrucción. El cambio que experimentó en        │
│ God of War (2018) no fue de personalidad —       │
│ fue de decisión. Qué puede enseñarle un dios     │
│ de la guerra a alguien que lidera un equipo.     │
│                                   [→ Spotify]   │
└─────────────────────────────────────────────────┘
```

**Nota de implementación en Wix:** Para los links de cada episodio en Spotify, Andy debe pegar el link específico de cada episodio (no el del show general). Estos links están disponibles en Spotify for Podcasters.

---

## PÁGINA 3 — /about

**SEO:**
- Title tag: `Andrés Bermúdez — Behind the Queue`
- Meta description: `Andrés Ricardo Bermúdez Rodríguez. Ingeniero Industrial, 15 años en BPO/CX, Bogotá. Creador de Behind the Queue, el podcast en español sobre liderazgo y experiencia.`
- H1: `Andrés Bermúdez Rodríguez`

---

### Sección 1 — Header + foto

**Visual:** Fondo Void Black. Foto de Andy a la izquierda (o arriba en mobile), texto a la derecha. Borde de foto: circular o cuadrado con esquinas redondeadas, borde Signal Gold.

```
[H1 — Playfair Display Bold]
Andrés Bermúdez Rodríguez

[Texto pequeño — Bebas Neue, Signal Gold]
HOST · BEHIND THE QUEUE

[Cuerpo — DM Sans]
Ingeniero Industrial con más de 15 años de experiencia
en operaciones BPO y servicio al cliente en Colombia y LATAM.
```

---

### Sección 2 — Bio completa

```
[Cuerpo — DM Sans, Off-white]

Comencé Behind the Queue porque hay conversaciones que
no ocurren en los pasillos de las empresas de operaciones —
conversaciones sobre por qué la gente se queda, por qué se va,
qué diferencia a un equipo que recuerdas de uno que olvidaste
al día siguiente.

Llevo más de 15 años en la industria BPO y de servicio al cliente.
He visto equipos que funcionan como máquinas y equipos donde
nadie quiere llegar al trabajo. La diferencia casi nunca está
en el proceso. Está en las decisiones.

Behind the Queue es el espacio donde conecto esas decisiones
con algo que ya conocen: una película que vieron de niños,
un videojuego que jugaron hasta las 3am, una canción que
suena exactamente como lo que sienten en una junta.

No hablo para motivar. Hablo para que la próxima vez que
estén en esa junta, vean algo que antes no veían.

[Texto pequeño — DM Sans, Signal Gold]
Bogotá, Colombia · Disponible en Spotify, Apple Podcasts
```

---

### Sección 3 — Links de plataformas

```
[Título — DM Sans pequeño, Off-white]
Encuéntrame en

[Links en fila o grid]
📻 Spotify    🍎 Apple Podcasts
📸 @behindthequeue84    🎵 @behind.the.queue    💼 LinkedIn
✉️ andy@behind-thequeue.com
```

---

## PÁGINA 4 — /escuchar

**SEO:**
- Title tag: `Escuchar — Behind the Queue Podcast`
- Meta description: `Behind the Queue disponible en Spotify y Apple Podcasts. Podcast en español sobre liderazgo, CX y decisiones humanas. Suscríbete gratis.`
- H1: `Escucha Behind the Queue`

---

### Sección 1 — Header

**Visual:** Fondo Void Black. Centrado.

```
[H1 — Playfair Display Bold]
Escucha Behind the Queue

[Subtítulo — DM Sans]
Disponible donde escuchas tus podcasts.
Gratis. Sin registro.
```

---

### Sección 2 — Embed Spotify

**Implementación en Wix:** Agregar un bloque HTML embed con el iframe de Spotify.

```html
<!-- Copiar esto en Wix → Add Element → Embed HTML → HTML iFrame -->
<iframe
  style="border-radius:12px"
  src="https://open.spotify.com/embed/show/5figtqa6zJxW1pE1sWJeEP?utm_source=generator&theme=0"
  width="100%"
  height="352"
  frameBorder="0"
  allowfullscreen=""
  allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
  loading="lazy">
</iframe>
```

---

### Sección 3 — Plataformas

**Visual:** Cards en fila. Fondo `#111111`, borde Signal Gold, ícono + nombre + botón.

```
[Card Spotify]
SPOTIFY
La plataforma principal
[Botón Signal Gold → link al show en Spotify]

[Card Apple Podcasts]
APPLE PODCASTS
[Botón borde Signal Gold → link al show en Apple Podcasts]
→ Placeholder: [LINK APPLE PODCASTS — agregar cuando esté disponible]
```

---

### Sección 4 — Redes sociales

```
[Título — DM Sans pequeño, Off-white]
También en

[Links]
📸 Instagram: @behindthequeue84
🎵 TikTok: @behind.the.queue
💼 LinkedIn: Andrés Bermúdez Rodríguez
```

---

## PÁGINA 5 — /contact

**SEO:**
- Title tag: `Contacto — Behind the Queue`
- Meta description: `¿Tienes una pregunta, propuesta o quieres hablar sobre el podcast? Escríbele a Andrés directamente.`
- H1: `Contacto`

---

### Sección 1 — Header + copy

**Visual:** Fondo Void Black. Centrado. Ancho máximo 640px.

```
[H1 — Playfair Display Bold]
Contacto

[Cuerpo — DM Sans]
Para propuestas de colaboración, preguntas sobre el podcast
o cualquier otro tema relacionado con Behind the Queue.

Respondo personalmente a todos los mensajes.

[Email visible — DM Sans, Signal Gold, clickeable]
andy@behind-thequeue.com
```

---

### Sección 2 — Formulario de contacto

**Implementación en Wix:** Usar el Wix Forms nativo (Add Element → Contact & Forms → Contact Form).

Campos del formulario:
- Nombre (texto, requerido)
- Email (email, requerido)
- Asunto (texto, opcional)
- Mensaje (área de texto, requerido)
- Botón de envío: texto `ENVIAR MENSAJE`, fondo Signal Gold, texto negro

**Confirmación de envío:** "Gracias. Respondo en menos de 48 horas."

---

## NAVEGACIÓN GLOBAL (Header + Footer)

### Header

```
[Logo BTQ — izquierda]          [Links — derecha]
                                Episodios  |  About  |  Escuchar  |  Blog  |  Contacto
```

**Visual:** Fondo Void Black con 95% opacidad (para que sea sticky sin bloquear). Logo en Off-white o Signal Gold.

### Footer

**Visual:** Fondo `#0A0A0A`. Tres columnas.

```
Columna 1:                  Columna 2:              Columna 3:
BEHIND THE QUEUE            Páginas                 Escuchar en
Podcast en español          · Episodios             · Spotify
sobre liderazgo y CX.       · About                 · Apple Podcasts
                            · Blog
andy@behind-thequeue.com    · Contacto
                                                    @behindthequeue84
                                                    @behind.the.queue

─────────────────────────────────────────────────────────────────
© 2026 Andrés Ricardo Bermúdez Rodríguez · behind-thequeue.com
```

---

## Checklist de verificación final

Después de publicar todo en Wix, verificar desde una ventana de incógnito:

- [ ] `behind-thequeue.com` — Home carga, diseño correcto
- [ ] `behind-thequeue.com/episodios` — 4 cards de episodios visibles
- [ ] `behind-thequeue.com/about` — Bio de Andy visible
- [ ] `behind-thequeue.com/escuchar` — Spotify embed carga
- [ ] `behind-thequeue.com/contact` — Formulario funciona, email visible
- [ ] `behind-thequeue.com/blog` — Posts existentes accesibles
- [ ] Todos los links del menú de navegación resuelven sin 404
- [ ] En mobile: Hero no corta texto, cards apilan correctamente
- [ ] Wix Dashboard → SEO → verificar que title/description estén en las 5 páginas nuevas
- [ ] Buscar "Behind the Queue podcast" en Google — confirmar que aparece el sitio

---

## Pendientes que requieren datos de Andy

```
□ Links individuales de cada episodio en Spotify (EP.010–EP.013)
  → Disponibles en Spotify for Podcasters → Episodios → Share
□ Link de Apple Podcasts del show
  → Disponible si el show ya está distribuido en Apple
□ Foto de Andy para la página About
  → Dimensiones recomendadas: 800×800px mínimo, cuadrada o vertical
□ Logo BTQ en formato SVG o PNG fondo transparente
  → Para favicon y header
```
