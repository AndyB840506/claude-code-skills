# Claude Code Skills

> Colección de skills reutilizables y de código abierto para Claude Code. **Ready to fork, improve, and share.**

Cada skill es un módulo completo que le enseña a Claude a hacer algo específico. Están organizados en carpetas con estructura clara: router mínimo (`SKILL.md`), workflows paso a paso, y documentación.

---

## 🚀 Skills Disponibles

### **session-close**
Workflow completo para cerrar sesiones productivas.
- **Pasos:** Retrospective → Prompt Reviewer → Skill Management → Handoff
- **Ubicación:** `.claude/skills/session-close/`
- **Para quién:** Cualquiera que itere constantemente en skills
- **Triggers:** `session close`, `end session`, `closing session`, `cierre de sesión`

### **retrospective**
Analiza sesiones para extraer learnings y propone actualizaciones a skills.
- **Detecta:** Correcciones del usuario, trabajo iterativo, pasos improvisados
- **Genera:** Diffs específicos listos para aplicar
- **Ubicación:** `.claude/skills/retrospective/`
- **Triggers:** `retrospective`, `what did we learn`, `update skills`

### **skill-management**
Estructura clara para skills mantenibles. Router mínimo + workflows separados.
- **Enseña:** Patrón de carpetas, convenciones de nombres, progresión de complejidad
- **Ubicación:** `.claude/skills/skill-management/`
- **Para quién:** Quien crea skills complejas o quiere compartirlas

### **prompt-reviewer** (español) & **prompt-reviewer-en** (inglés)
Revisa prompts, skills e instrucciones para mejorar clarity, completitud, consistencia.
- **Modos:** Quick (5 min) o Thorough (análisis completo)
- **Output:** Propuestas concretas de mejora
- **Ubicación:** `.claude/skills/prompt-reviewer/` y `.claude/skills/prompt-reviewer-en/`

### **crear-skill** (español) & **skill-creator** (inglés)
Asistente para crear tus propias skills personalizadas.
- **Guía:** Desde idea hasta skill funcional
- **Valida:** Estructura, triggers, documentación
- **Ubicación:** `.claude/skills/crear-skill/` y `.claude/skills/skill-creator/`

### **Más skills**
- **handoff** — Respalda sesiones con git + documentación
- **ai-lead-generator** — Busca leads de negocio con scoring automático
- **smart-recruiter** — Entrevistas de selección automáticas
- **btq-project** — Master context para el podcast Behind the Queue

---

## 📦 Instalación

Cada skill funciona **directamente en tu proyecto Claude Code**:

```bash
# Clona este repositorio
git clone https://github.com/AndyB840506/claude-code-skills.git

# Copia el skill que quieras a tu proyecto
cp -r claude-code-skills/.claude/skills/session-close ~/.claude/skills/
# o a nivel de proyecto
cp -r claude-code-skills/.claude/skills/session-close /tu-proyecto/.claude/skills/
```

Claude Code detecta automáticamente cualquier skill en `.claude/skills/nombre/SKILL.md`.

Luego simplemente escribe el comando:
```
/session-close
/retrospective
/crear-skill
```

---

## 🛠️ Estructura

Todos los skills siguen este patrón:

```
.claude/skills/nombre-skill/
├── SKILL.md           # Router: triggers + descripción (< 50 líneas)
├── workflows/         # Procedimientos paso a paso (si aplica)
│   ├── workflow1.md
│   └── workflow2.md
├── templates/         # HTML, email, documentos (si aplica)
└── docs/              # Documentación avanzada (si aplica)
```

**Reglas:**
- SKILL.md siempre bajo 50 líneas
- Cada procedimiento en archivo separado
- Triggers múltiples y específicos
- Completamente auto-contenido (sin dependencias externas)

Ver [skill-management](.claude/skills/skill-management/SKILL.md) para un ejemplo completo.

---

## 🤝 Contribuye

¡Las contribuciones son bienvenidas! Ve a [CONTRIBUTING.md](CONTRIBUTING.md) para:
- Cómo hacer fork y crear branch
- Estructura esperada para nuevas skills
- Proceso de PR
- Convenciones de nombres y commits

**Tipos de contribuciones que aceptamos:**
- ✅ Nuevos triggers más específicos
- ✅ Mejoras a documentación y ejemplos
- ✅ Bugfixes en instrucciones
- ✅ Nuevas skills bien estructuradas
- ✅ Traducciones
- ✅ Secciones "Troubleshooting"

**No aceptamos:**
- ❌ Skills sin estructura de carpeta
- ❌ SKILL.md > 50 líneas sin workflows
- ❌ Cambios sin discusión previa

---

## 📚 Documentación

Cada skill incluye:
- **SKILL.md** — Descripción + triggers + cómo usar (máx 50 líneas)
- **workflows/** — Procedimientos paso a paso
- **docs/** — Referencias avanzadas y troubleshooting

El repositorio completo incluye:
- **CONTRIBUTING.md** — Guía para contribuyentes
- **README.md** (este archivo) — Overview general

---

## 💡 Casos de Uso

**Para usuarios:**
- Automatiza flujos repetitivos
- Mejora la calidad de outputs con `prompt-reviewer`
- Cierra sesiones productivas con estructura

**Para developers:**
- Aprende a estructurar skills complejos
- Contribuye mejoras a skills públicos
- Crea skills privados en tu empresa usando este patrón

---

## 📄 Licencia

Este repositorio está bajo licencia **MIT**. Libre para usar, fork y adaptar.

---

## 🙌 Créditos

Diseñado por el equipo de [AndyB](https://github.com/AndyB840506) como parte del ecosistema de Claude Code.

**¿Preguntas?** Abre una Issue en GitHub o contacta directamente.

**¿Mejoras?** Fork, mejora, y abre un PR. La comunidad lo agradecerá. 🚀
- **docs/recursos.md** — Referencias de herramientas
- **Workflows** en `.claude/skills/*/workflows/` — Pasos específicos

---

## 🚀 Instalación

### Opción 1 — Clonar el repositorio
```bash
git clone https://github.com/AndyB840506/podcast-creator-kit.git
cd podcast-creator-kit/kit-podcast-creator
claude
```

### Opción 2 — Desde Claude Code
1. Abre Claude Code
2. Archivo → Abrir carpeta
3. Selecciona `kit-podcast-creator/`
4. ¡Listo!

---

## 🎯 Estructura del repositorio

```
podcast-creator-kit/
├── kit-podcast-creator/          ← Skill principal
│   ├── CLAUDE.md                 ← Entrada (edición inicial)
│   ├── INSTRUCCIONES.md          ← Guía de uso
│   ├── README.md                 ← Descripción detallada
│   ├── docs/
│   │   └── recursos.md           ← Referencia de herramientas
│   └── .claude/skills/podcast-creator/
│       ├── SKILL.md              ← Configuración de skill
│       └── workflows/            ← 6 workflows de producción
│           ├── 00-setup.md
│           ├── 01-episodio.md
│           ├── 02-grabacion.md
│           ├── 03-artwork.md
│           ├── 04-social-media.md
│           ├── 05-show-notes.md
│           └── 06-html-export.md
```

---

## 💡 Casos de uso

### Empezar un podcast desde cero
1. Abre el kit
2. Di "hola"
3. Sigue el setup (identidad, formato, tono)
4. Genera script, grabación, artwork, social media

### Producir episodios semanales
1. Usa el kit para generar scripts
2. Graba con la guía de checklists
3. Edita y exporta con el paquete HTML
4. Publica con el plan de social media

### Entrevistar a invitados
1. El kit genera cuestionario escalado
2. Briefing para enviar al invitado
3. Script con notas de escucha activa
4. Kit de cross-promotion para el invitado

---

## 🛠️ Herramientas recomendadas

El kit incluye referencias y guías para:
- **Grabación:** Audacity, GarageBand, Descript
- **Entrevistas remotas:** Riverside.fm, Zencastr
- **Edición:** Adobe Audition, Hindenburg Journalist
- **Transcripción:** TurboScribe, Otter.ai, Whisper
- **Imágenes IA:** Google Flow, Midjourney, DALL-E 3
- **Hosting:** Spotify for Creators, Buzzsprout, Transistor
- **Música:** YouTube Audio Library, Incompetech, Epidemic Sound

Ver `docs/recursos.md` para detalles completos.

---

## 📖 Flujo de producción típico

```
Lunes:     Escribir/revisar script
Miércoles: Grabar episodio
Jueves:    Editar audio
Viernes:   Crear artwork + social media + show notes
Siguiente miércoles: Publicar en todas las plataformas
```

---

## 🌍 Idiomas

El kit responde automáticamente en:
- **Español** — Si empiezas con "hola" o escribes en español
- **Inglés** — Si empiezas con "hello" o escribes en inglés

Mantiene el idioma durante toda la sesión.

---

## ✨ Características destacadas

✅ **Realismo desde el inicio** — Te prepara para que el primer episodio tome 8-15 horas
✅ **Formato flexible** — Cada episodio puede ser solo/entrevista/co-host
✅ **Herramientas integradas** — Recomendaciones concretas (no genéricas)
✅ **Documentos de apoyo** — Cuestionarios, briefings, kits de cross-promotion
✅ **Cadencia sostenible** — Diseñado para 1 episodio/semana
✅ **Multiidioma** — Español e inglés
✅ **Exportación HTML** — Paquete de producción + página pública

---

## 📝 Requisitos

- **Claude Code** (cualquier versión reciente)
- Nada más. El kit no necesita instalaciones adicionales.

---

## 🤝 Contribuciones

¿Mejoras o sugerencias? Abre un issue o pull request.

---

## 📄 Licencia

MIT License — Usa, modifica y comparte libremente.

---

## 🎙️ Próximas adiciones

- [ ] Video tutorials
- [ ] Ejemplos de podcasts generados con el kit
- [ ] Automatización de distribución multi-plataforma
- [ ] Integración con Spotify API para analytics

---

**¿Listo para crear tu podcast?** 

```bash
cd kit-podcast-creator
claude
```

Escribe "hola" y comienza. 🚀
