# Workflow 07 — Metadatos de YouTube

Genera título, descripción, tags, texto de miniatura y capítulos optimizados para YouTube.

**Regla fundamental: El título no puede superar 60 caracteres. Verificar el conteo explícitamente antes de entregar.**

---

## Paso 0 — Cargar datos

1. Lee `podcast-profile.json`: nombre del podcast, host(s), link de YouTube, categoría, hashtags_base, colores y tipografía de marca.
2. Busca el script del episodio (`episodio-[NNN]-*.md`). Si existe, extrae:
   - Tema central y 3-5 puntos principales
   - Nombre del invitado si aplica
   - Bloques `<h2>` (para generar capítulos automáticamente)
3. Si existe `shownotes-ep[NNN].md`, reutiliza esa descripción como base — para YouTube debe quedar más densa en keywords (es buscador, no solo feed).

---

## Paso 1 — Datos adicionales

Pregunta solo lo que no encontraste en los archivos existentes:

> 1. ¿Cuál es el número y título del episodio?
> 2. ¿Tienes timestamps de capítulos? (si el script tiene bloques `<h2>`, los extraigo automáticamente — si no, dime los momentos clave)
> 3. ¿Texto para la miniatura? (3-5 palabras — si no tienes uno, propongo una opción)

---

## Paso 2 — Generar metadatos

### A. Título (máx 60 chars)

`[Gancho o nombre central] — [Nombre Podcast] EP.[NNN]`
**→ Conteo: [N] caracteres** ✓ (verde si ≤60) / ✗ (rojo si >60, proponer versión corta)

---

### B. Descripción

**Primeras 3 líneas (visibles antes de "ver más" — las que más pesan para SEO):**
`[Hook del episodio en 1 línea] · EP.[NNN] · Escúchalo en Spotify: [link]`

**Descripción completa:**
Misma estructura que la descripción de Spotify (`shownotes-ep[NNN].md`, sección C), pero adaptada:
- Más densa en keywords — YouTube es un buscador, no solo un feed
- Incluye el link de YouTube junto a las demás plataformas
- Cierra con el bloque de contacto del perfil

---

### C. Tags / Keywords (15-20)

Mezcla español + inglés — la audiencia de YouTube es bilingüe por naturaleza de la plataforma. Combina:
- Nombre del podcast y variantes (2-3)
- Tema específico del episodio (4-6)
- Categoría general del podcast (3-4)
- Nombres propios mencionados — invitados, artistas, eventos, lugares (3-5)

`[tag1], [tag2], [tag3], ...`

---

### D. Texto de miniatura

3-5 palabras máximo, alto contraste, coherente con la tipografía y colores de marca definidos en `podcast-profile.json`.

`[TEXTO PROPUESTO]`

---

### E. Capítulos / Timestamps

Si el script tiene bloques `<h2>`, extrae los tiempos y títulos automáticamente. Si no, usa los momentos que indique el usuario.

```
00:00 Intro
0X:XX [Título del bloque A]
0X:XX [Título del bloque B]
0X:XX [Segmento de promoción / cierre]
```

---

## Paso 3 — Guardar y presentar

1. Guarda como `youtube-ep[NNN].md` en el directorio actual.
2. Muestra verificación de longitudes:

```
══════════════════════════════════════════
  YouTube metadata generada ✓
══════════════════════════════════════════
  Episodio:           EP.[NNN]
  Título:             [N] chars [✓/✗]
  Tags:               [N] terms
  Capítulos:          [Sí/No — N bloques]
  Archivo:            youtube-ep[NNN].md
══════════════════════════════════════════
```

3. Si el título excede 60 caracteres, propone una versión corregida antes de guardar.
