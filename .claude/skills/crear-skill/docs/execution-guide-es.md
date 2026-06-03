# Secciones EXECUTION — Cómo Hacer que las Skills Realmente Funcionen

Para que tu skill *realmente ejecute* (no solo mostrar documentación), el SKILL.md debe incluir una sección `## EXECUTION` con instrucciones explícitas.

**Sin EXECUTION:** La skill muestra documentación pero no dispara acciones  
**Con EXECUTION:** La skill realmente ejecuta el proceso cuando se invoca

---

## Patrón Estándar de 4 Pasos

Toda skill de producción debe seguir este patrón. No lo desvíes sin razón explícita.

```markdown
## EXECUTION

Has invocado `/tu-skill`. Ejecuta el proceso en 4 pasos:

### Paso 1 — Recopilar inputs

Pide exactamente lo que necesitas, en un solo bloque. Nombra cada campo.
Una vez confirmados, NO hagas más preguntas — procede al Paso 2.

```
Campo A: [descripción]
Campo B: [descripción]
Campo C: [descripción]
```

Si el usuario ya proporcionó la información en la invocación, salta directamente al Paso 2.

---

### Paso 2 — Generar (en paralelo cuando sea posible)

Genera todos los outputs en una sola respuesta. Etiqueta cada bloque claramente.
Tareas independientes van en paralelo — no serialices lo que puede ir en paralelo.

**A · [Bloque de output 1]**
[contenido]

**B · [Bloque de output 2]**
[contenido]

**C · [Bloque de output 3]**
[contenido]

---

### Paso 3 — Aprobación

Antes de cualquier acción irreversible (commit, deploy, llamada a API, envío de email):

> "¿Apruebas o ajustas algo antes de [commit/deploy/enviar]?"

Espera aprobación explícita. Si el usuario dice "ajustar [bloque]" — revisa solo ese bloque.
Si dice "sí" o "aprobado" — procede al Paso 4.

---

### Paso 4 — Ejecutar + Resumen

Ejecuta la acción aprobada. Termina con una tabla de estado:

| Entregable | Estado |
|------------|--------|
| [Asset A] | Listo |
| [Asset B] | Listo |
| [Commit/Deploy] | Listo / Falló (razón) |
```

---

## Plantilla mínima (skills simples sin commit/deploy)

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
