---
name: crear-skill
description: "Asiste al usuario para crear sus propias skills de Claude Code personalizadas en español o inglés, automatizar flujos de trabajo, crear comandos o convertir procesos manuales en automáticos. Triggers: 'crea una skill', 'quiero una skill', 'skill personalizada', 'automatizar esto como skill', 'crear comando Claude Code', 'convertir en skill', 'hacer esto automático'."
---

# Crear Skill — Crea tus propias skills

Le describes un proceso que quieres automatizar y Claude genera una skill completa lista para usar. Es la herramienta que crea herramientas.

Las skills de Claude Code son archivos `.md` que le enseñan a Claude a hacer tareas específicas. Cualquier proceso que hagas de forma repetitiva puede convertirse en una skill.

---

## Flujo de Creación

1. **Entender** — ¿Qué quieres automatizar?
2. **Diseñar** — Planifica input, proceso, output
3. **Escribir** — Genero la skill en `.md`
4. **Confirmar** — ¿Quieres que la guarde?
5. **Instalar** — La skill queda lista en `.claude/skills/`
6. **Testear** — Verificamos que funciona
7. **Presentar** — Resumen de lo generado

---

## Quick Links

- [Paso 1: Entender](workflows/understand.md) — Qué necesitas
- [Paso 2: Diseñar](workflows/design.md) — Estructura de la skill
- [Paso 3-5: Crear e Instalar](workflows/create-install.md) — Genero y guardo
- [Paso 6-7: Test y Presentación](workflows/test-present.md) — Verifico y presento
- [Principios de Diseño](docs/design-principles.md) — 10+ principios de buenas skills

---

## Ejemplo

```
/crear-skill

"Quiero una skill que lea un CSV de productos 
y genere fichas de producto en HTML"

↓ 

Creo la skill completa → Te pido confirmación → 
La instalo → Listo para usar
```

---

## Idioma

Puedes crear skills en:
- **Español** — para uso personal o equipo hispanohablante
- **English** — para compartir globalmente

---

## Dónde se Guardan

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

---

## Crítico: Secciones de EJECUCIÓN

Para que tu skill *realmente ejecute* (no solo mostrar documentación), el SKILL.md debe incluir una sección `## EXECUTION` con instrucciones explícitas.

**Sin EXECUTION:** La skill muestra documentación pero no dispara acciones  
**Con EXECUTION:** La skill realmente ejecuta el proceso cuando se invoca

### Plantilla

```markdown
## EXECUTION

Has invocado `/tu-skill`. Ahora ejecuta el proceso:

### Paso 1: [Primera acción]
[Qué hacer, qué buscar]

### Paso 2: [Segunda acción]
[Qué hacer, qué buscar]

[Continúa con todos los pasos...]

---

**¡Proceso completado!** [Resumen de lo realizado]
```

### Ejemplo (de una skill real: retrospective)

```markdown
## EXECUTION

Has invocado `/retrospective`. Ahora realiza el análisis:

### Paso 1: Extraer Señales
Escanea la conversación: correcciones, trabajo rehecho, pasos faltantes, qué funcionó

### Paso 2: Mapear a Skills
Identifica qué skills necesitan actualizarse

### Paso 3: Proponer Cambios
Muestra diffs específicos

### Paso 4: Pedir Confirmación
Espera aprobación del usuario

### Paso 5: Aplicar Cambios
Actualiza archivos si fue aprobado

---

**¡Retrospective completado!**
```

**Incluye secciones EXECUTION en toda skill que generes.** Esto es lo que hace que las skills realmente funcionen.
