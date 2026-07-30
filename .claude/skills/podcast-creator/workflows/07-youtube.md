# Workflow 07 — Metadatos de YouTube

Genera título, descripción, tags, texto de miniatura y capítulos optimizados para YouTube.

**Antes de generar, revisa el formato real del episodio publicado más reciente del show**
(p.ej. BTQ EP.015 — `https://youtu.be/DsRGtiimlAg`). En la práctica el título no sigue un
límite estricto de 60 caracteres — BTQ usa títulos largos tipo
`[Hook]: [frase] | EP.0XX | [Nombre del show]` (~95 chars). Si el show tiene su propio
perfil/skill (p.ej. `episode-launch` para BTQ), ese formato real tiene prioridad sobre
la plantilla genérica de abajo.

**Regla fundamental sobre tags vs. hashtags — nunca confundirlos:**
- **Tags / keywords** (campo Tags de YouTube Studio, keywords de Spotify, listas de tags
  en redes) = lista separada por comas para búsqueda/SEO. Formato: `tag1, tag2, tag3, ...`
- **Hashtags dentro de la descripción** = un set separado, más pequeño, separado por
  espacios con prefijo `#`, para descubribilidad en feed. Formato: `#Tag1 #Tag2 #Tag3`
- Genera ambos — no sustituyas la lista de tags por hashtags ni viceversa.

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

Si el script tiene bloques `<h2>`, extrae los tiempos y títulos automáticamente.

Si no — **antes de decirle al usuario que no hay timestamps disponibles, revisa la
transcripción diarizada** en `E:\Transcriptor\transcripciones\[Show] Ep.[NNN].srt` —
localiza las transiciones de sección buscando frases clave por tema (nombres de
frameworks/autores, nombres de segmentos como "Aplicable Hoy", referencias culturales).
Timestamps reales del transcript superan rangos estimados. Solo si tampoco existe
transcripción, pide los momentos clave al usuario.

```
00:00 Intro
0X:XX [Título del bloque A]
0X:XX [Título del bloque B]
0X:XX [Segmento de promoción / cierre]
```

**Tres reglas duras de YouTube. Si UNA falla, la plataforma descarta la lista ENTERA en
silencio** — el video queda sin capítulos y no avisa:

1. El primer capítulo debe ser exactamente `00:00`.
2. Mínimo 3 capítulos.
3. **Cada capítulo debe durar al menos 10 segundos — incluido el último**, que se mide contra
   la duración total del episodio, no contra otro marcador.

La tercera es la que muerde, porque el marcador final suele ser un «Outro» pegado al final del
audio. **Mordió en MPD T2·E1 (2026-07-30):** la lista de Spotify traía 18 marcadores y el último
era `41:38 Outro` sobre un episodio de `41:47` — **9 segundos**. La versión de YouTube salió con
17, cortando en el marcador anterior; el de Outro se conservó en la lista de Spotify, que no
tiene esta regla. **La lista de capítulos de Spotify no es portable a YouTube tal cual.**

**Verificar, no estimar:** convertir cada marcador a segundos, restar contra el siguiente (y el
último contra la duración real del episodio) y confirmar que el mínimo es ≥10 s.

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
  Tags:               [N] terms · [N] chars / 500 [✓/✗]
  Capítulos:          [N] bloques · primero en 00:00 [✓/✗]
                      más corto: [N] s / mín 10 s [✓/✗]
  Archivo:            youtube-ep[NNN].md
══════════════════════════════════════════
```

3. Si el título excede 60 caracteres, propone una versión corregida antes de guardar.
