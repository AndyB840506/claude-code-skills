# Idioma

Puedes crear skills en:
- **Español** — para uso personal o equipo hispanohablante
- **English** — para compartir globalmente

# Dónde se Guardan

Todas las skills van en:
```
.claude/skills/nombre-skill/SKILL.md
```

Si es muy grande, se organiza con carpetas:
```
.claude/skills/nombre-skill/
├── SKILL.md (router)
├── workflows/ (procedimientos)
└── docs/ (referencias)
```

**Regla de entrega mínima:** `SKILL.md` es obligatorio el mismo día que se crea la
carpeta — no se puede "completar después". Una carpeta con solo archivos de `config/`
o `workflows/` sin `SKILL.md` es una skill invisible: Claude no puede invocarla.

# Distinción con skill-creator

- **`/crear-skill`** — Esta skill. Para uso dentro de este workspace. Instrucciones en español.
- **`/skill-creator`** — Versión en inglés, para crear skills genéricas o compartibles globalmente.

# Secciones de EJECUCIÓN

Toda skill necesita una sección `## EXECUTION` con instrucciones explícitas para que
realmente funcione. Ver [Guía de EXECUTION](execution-guide-es.md) para plantillas y
ejemplos detallados.

**Incluye secciones EXECUTION en toda skill que generes.** Esto es lo que hace que las
skills realmente funcionen.

# Ejemplo

```
/crear-skill

"Quiero una skill que lea un CSV de productos
y genere fichas de producto en HTML"

↓

Creo la skill completa → Te pido confirmación →
La instalo → Listo para usar
```
