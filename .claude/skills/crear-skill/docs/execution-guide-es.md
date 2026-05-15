# Secciones EXECUTION — Cómo Hacer que las Skills Realmente Funcionen

Para que tu skill *realmente ejecute* (no solo mostrar documentación), el SKILL.md debe incluir una sección `## EXECUTION` con instrucciones explícitas.

**Sin EXECUTION:** La skill muestra documentación pero no dispara acciones  
**Con EXECUTION:** La skill realmente ejecuta el proceso cuando se invoca

---

## Plantilla

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

---

## Ejemplo (de una skill real: retrospective)

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

---

## Principios Clave

- **Instrucciones explícitas** — Cada paso le dice al AI exactamente qué hacer
- **Resultados claros** — El paso describe tanto la acción como el resultado esperado
- **Sin suposiciones** — No asumas que el AI entiende contexto de docs
- **Flujo completo** — Cubre todos los pasos de principio a fin
- **Resumen al final** — Confirma completación con un mensaje final

**Incluye secciones EXECUTION en toda skill que generes.** Esto es lo que hace que las skills realmente funcionen.

---

## Directivas de EJECUCIÓN (Avanzado)

Para workflows multi-paso complejos, usa directivas explícitas:

### Pasos con confirmación del usuario
No uses **ACTION:**, el usuario espera confirmación:
```markdown
### Paso 1: Retrospective
/retrospective
- Espera confirmación del usuario
- Si SÍ: aplica cambios; Si NO: continúa al Paso 2
```

### Pasos que ejecutan inmediatamente
Usa **ACTION:** para claridad:
```markdown
### Paso 6: Compact Context
**ACTION:** Ejecuta el comando compact
/compact
**MUST EXECUTE:** Esto no es opcional.
- Reporta: "Context comprimido."
- Continúa al Paso 7 inmediatamente
```

**Regla:** Usa ACTION directives para pasos que ejecutan inmediatamente o deben suceder sin importar la interacción del usuario.
