# Contributing to Claude Code Skills

¡Gracias por interesarte en mejorar estas skills! Este repositorio contiene skills reutilizables para Claude Code que se pueden mejorar, extender y compartir con la comunidad.

## Cómo Contribuir

### 1. Fork el Repositorio
Haz click en "Fork" en GitHub. Esto crea tu propia copia del proyecto.

```bash
git clone https://github.com/TU-USUARIO/claude-code-skills.git
cd claude-code-skills
```

### 2. Crea una Branch
Para cada cambio, crea una rama descriptiva:

```bash
git checkout -b mejora/nombre-de-la-mejora
# o
git checkout -b fix/nombre-del-bug
# o
git checkout -b feature/nueva-funcionalidad
```

**Convención de nombres:**
- `mejora/` — mejoras a skills existentes
- `fix/` — correcciones de bugs
- `feature/` — nuevas skills o features
- `docs/` — mejoras a documentación

### 3. Haz tus Cambios

**Para mejorar un skill existente:**
```
.claude/skills/nombre-skill/
├── SKILL.md          # Actualizar descripción, triggers, instrucciones
├── workflows/        # Agregar/mejorar workflows
├── docs/             # Agregar documentación avanzada
└── scripts/          # Scripts helper si es necesario
```

**Reglas:**
- SKILL.md debe estar bajo 50 líneas (router claro)
- Cada workflow en archivo separado
- Triggers deben ser específicos y cubrir variaciones
- Documentar cambios en commit messages en español o inglés

### 4. Testea tus Cambios

Antes de hacer commit:

```bash
# Verifica que la estructura es correcta
ls -R .claude/skills/tu-skill/

# Abre el archivo SKILL.md y confirma que:
# - Nombre en frontmatter match folder name
# - Triggers sean claros y múltiples
# - Descripción sea concisa
# - Estructura sea consistente
```

### 5. Commit y Push

```bash
git add .
git commit -m "mejora: descripción clara de qué cambiaste"
git push origin mejora/nombre-de-la-mejora
```

**Mensaje de commit:**
- Empieza con verbo: `feat:`, `fix:`, `docs:`, `mejora:`
- Claro y conciso (1 línea máximo, 50 caracteres idealmente)
- Español o inglés consistente con el resto del proyecto

### 6. Crea un Pull Request

1. Ve a tu fork en GitHub
2. Click en "Compare & pull request"
3. Describe:
   - **Qué cambiaste** — descripción breve
   - **Por qué** — cuál es el problema que solucionas
   - **Cómo lo testeaste** — si aplica
4. Submit PR

**Ejemplo de descripción de PR:**

```
## Descripción
Mejora el skill `retrospective` para detectar también cambios fallidos.

## Problema
El skill actual solo detecta "redone work" pero no cuando algo falla completamente sin ser reintentado.

## Cambios
- Agregué patrón "Failed attempts" en Step 1
- Documenté en sección "What NOT to Encode"
- Actualicé ejemplo en Quick Start

## Testing
Probé manualmente detectando un skill fallido en la sesión anterior.
```

## Qué Tipo de Contribuciones Aceptamos

✅ **Mejoras bienvenidas:**
- Agregar triggers más específicos
- Mejorar ejemplos o documentación
- Arreglar bugs en instrucciones
- Optimizar workflows
- Traducir a otros idiomas
- Agregar secciones "Troubleshooting"
- Nuevas skills bien estructuradas

❌ **No aceptamos:**
- Cambios destructivos sin discusión previa
- Skills sin estructura de carpeta
- SKILL.md mayor a 50 líneas sin workflows
- Cambios a frontmatter `name:` sin justificación

## Estructura Esperada

Cualquier skill debe seguir este patrón:

```
.claude/skills/nombre-skill/
├── SKILL.md                    # Frontmatter + router (máx 50 líneas)
├── workflows/                  # Procedimientos paso a paso
│   ├── workflow1.md
│   └── workflow2.md
├── templates/                  # HTML, email, etc (si aplica)
└── docs/                       # Documentación avanzada (si aplica)
```

**SKILL.md debe tener:**
- Frontmatter: `name:` (kebab-case) y `description:` (con triggers)
- Descripción 1-liner
- Quick Start mostrando cómo usarlo
- Secciones numeradas claras
- Referencias a workflows si existen

Ver [skill-management/SKILL.md](.claude/skills/skill-management/SKILL.md) para ejemplo completo.

## Código de Conducta

- Sé respetuoso con otros contribuyentes
- Proporciona feedback constructivo
- Acepta feedback sobre tus PRs
- Si no estás seguro, pregunta antes de invertir mucho tiempo

## Preguntas?

Abre una Issue en GitHub describiendo:
1. Qué quieres hacer
2. Por qué lo quieres hacer
3. Cómo planeas hacerlo (si tienes idea)

---

**¡Gracias por contribuir! La comunidad de Claude Code te lo agradece.** 🚀
