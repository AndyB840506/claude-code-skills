# CLAUDE.md — Podcast Creator Kit

Kit de producción de podcasts conversacionales. Genera perfiles, guiones, documentos y flujos de trabajo para cualquier podcast.

Los podcasts creados con este kit viven en `projects/[nombre-podcast]/` — cada uno es un workspace independiente con su propio CLAUDE.md.

## Al iniciar

### Paso A — Detectar idioma

Analiza el primer mensaje:
- **"hola"** o español → responde en español, guarda `idioma: "es"`
- **"hello"** o inglés → responde en inglés, guarda `idioma: "en"`
- Si no es claro → responde bilingüe

### Paso B — Verificar si hay un podcast activo

Busca `podcast-profile.json` en el directorio actual.

**Si NO existe** → modo creación:

> **Bienvenido al Kit de Producción de Podcast**
>
> ¿Ya tienes idea clara de qué va a tratar tu podcast, o todavía estás explorando?

- Si ya lo tiene claro → lanza `00-setup.md`
- Si está explorando → muestra estas categorías de ejemplo y lanza `00-setup.md`:
  1. **Educativo** — enseñás algo: habilidades, conceptos, tutoriales
  2. **Entrevistas** — conversaciones con invitados del campo
  3. **Narrativo** — historias, reportajes, true crime, documentales
  4. **Conversacional co-host** — dos o más personas charlan sobre un tema
  5. **Noticias / Actualidad** — análisis de lo que pasa en un sector
  6. **Nicho apasionado** — comunidad específica (música, deporte, gastronomía, etc.)

**Si SÍ existe** → modo producción:

> **Bienvenido de vuelta a [nombre del podcast]**
>
> ¿Qué producimos hoy?
>
> 1. **Guion** — script completo del próximo episodio
> 2. **Plan de grabación** — checklist para el día de grabación
> 3. **Artwork** — prompts para la portada del episodio
> 4. **Social Media** — plan de lanzamiento 3 días
> 5. **Show Notes** — descripción y metadatos Spotify/Apple
> 6. **Exportar HTML** — paquete de producción completo
> 7. **Actualizar perfil** — cambiar datos del podcast

---

## Reglas globales

- **Leer `podcast-profile.json` siempre** antes de cualquier workflow. Si no existe → lanzar `00-setup.md`.
- **No inventar datos del podcast.** Si falta información → preguntar o usar `[PENDIENTE]`.
- **Idioma:** mantener el idioma detectado durante toda la sesión.
- **Al terminar cada workflow:** sugerir el siguiente paso lógico.
- **Documentos y guiones:** HTML optimizado para PDF vía IlovePDF.
- **Backup:** git commit + push después de cada documento generado. Verificar G: antes de copiar allá.
- **Skill activa:** `.claude/skills/podcast-creator/SKILL.md`

---

## Estructura de carpetas del kit

```
kit-podcast-creator/
├── CLAUDE.md                         ← Este archivo (kit genérico)
├── .claude/skills/podcast-creator/   ← Skill y workflows del kit
│   ├── SKILL.md
│   └── workflows/
│       ├── 00-setup.md
│       ├── 01-episodio.md
│       └── ...
├── templates/                        ← Templates genéricos reutilizables
│   ├── episodio-invitado-cuestionario.md
│   ├── episodio-invitado-invitacion.md
│   ├── episodio-invitado-prep-hosts.md
│   └── preguntas-por-perfil.md
├── docs/                             ← Documentación del kit
└── projects/                         ← Podcasts creados con este kit
    └── [nombre-podcast]/             ← Workspace independiente por podcast
        ├── CLAUDE.md                 ← Config específica del podcast
        ├── podcast-profile.json
        └── ...
```

---

## Features disponibles en el kit

Cuando se crea un nuevo podcast (`00-setup.md`), el kit pregunta por:

### Segmento de episodio con invitado (opcional)
- Episodio especial donde el invitado es protagonista absoluto
- Incluye: carta de invitación → cuestionario simple → investigación del invitado (Modo Narval) → guion
- Grabación presencial recomendada: todos en el mismo cuarto
- El invitado solo confirma: bio libre + temas + lo que NO quiere tocar
- Tipos de invitados: artistas, promotores, luthiers, dueños de venues, productores, ingenieros de sonido

### Segmento de promoción (opcional)
- Bloque fijo en todos los episodios donde se mencionan eventos, lanzamientos, artistas
- Conducido por un host designado
- Se alimenta de `eventos.json` — una base de datos que el host llena antes de cada grabación
- Posición: bloque intermedio en episodio normal, al final en episodio con invitado

### Modo Narval (investigación de invitados)
- Claude investiga al invitado en la web antes de generar el guion
- Genera documento de prep para los hosts con: bio real, datos curiosos, preguntas únicas
- Los hosts llegan preparados como si fueran fans de verdad — eso genera la mejor energía

### Lenguaje y tono
- El kit pregunta por región y estilo de habla al crear el perfil
- Se guarda en `podcast-profile.json` → se aplica en todos los guiones y documentos
- Si el podcast tiene jerga propia → se puede crear un glosario en `glosario-[podcast].md`

### Fichas de invitados
- Una ficha por invitado en `fichas-invitados/[nombre].md`
- Guarda: preguntas aprobadas, temas cubiertos, NO-list, redes
- Evita repetir preguntas si el invitado regresa
