---
name: crear-skill
description: "Asiste al usuario para crear sus propias skills de Claude Code personalizadas en español o inglés, automatizar flujos de trabajo, crear comandos o convertir procesos manuales en automáticos. Triggers: 'crea una skill', 'quiero una skill', 'skill personalizada', 'automatizar esto como skill', 'crear comando Claude Code', 'convertir en skill', 'hacer esto automático', 'create a skill', 'I want a skill', 'custom skill', 'automate this as a skill'."
---

# Crear Skill — Crea tus propias skills

Le describes un proceso que quieres automatizar y Claude genera una skill completa lista para usar en español o inglés. Es la herramienta que crea herramientas.

Las skills de Claude Code son archivos `.md` que le enseñan a Claude a hacer tareas específicas. Cualquier proceso que hagas de forma repetitiva puede convertirse en una skill. Puedes crear skills en tu idioma preferido.

---

## Paso 1 — Entender qué necesita el usuario

Pregunta de forma conversacional:

- **¿En qué idioma quieres la skill?** — Español o English
- **¿Dónde quieres guardar esta skill?** — Business (privada, solo para tu empresa) u Other (pública, se puede compartir)
  - **Business:** Skills para proyectos internos, confidenciales o específicos de tu empresa. Se guardan en `.claude/skills/business/` y nunca se comparten públicamente.
  - **Other:** Skills de utilidad general que se pueden compartir con otros usuarios. Se guardan en `.claude/skills/other/` y se pueden publicar en repositorios públicos.
- **¿Qué quieres que haga Claude automáticamente?** — describe el resultado que esperas
- **¿Qué información necesita recibir?** — URL, texto, carpeta, datos, archivo...
- **¿Qué debe generar?** — HTML, informe, archivo, código, dashboard...
- **¿Lo vas a usar tú o se lo vas a dar a otras personas?** (esto también puede indicar si es business u other)

Si el usuario ya describió suficiente (ej: "una skill que lea un CSV de productos y genere fichas de producto en HTML"), diseña directamente.

Si no sabe qué skill crear, proponle ideas:

**Para negocios:**
- Generador de propuestas comerciales (datos del cliente → propuesta PDF/HTML profesional)
- Calculadora de presupuestos (servicio + horas → presupuesto detallado)
- Generador de contratos (datos → contrato personalizado)
- Creador de presentaciones de ventas (producto → slides HTML)
- Onboarding de clientes (datos → carpeta + emails + documentos)

**Para marketing:**
- Generador de copy para ads (producto + público → variantes de anuncios)
- Planificador de contenido (nicho → calendario de 30 días con ideas)
- Creador de emails de venta (producto → secuencia de emails)
- Generador de posts para redes (tema → posts para IG, LinkedIn, X)

**Para desarrollo:**
- Generador de APIs (modelo de datos → API completa)
- Documentador de código (repositorio → documentación)
- Generador de tests (código → suite de tests)
- Scaffolding de proyectos (tipo de proyecto → estructura completa)

**Para productividad:**
- Resumidor de documentos (PDF → resumen ejecutivo)
- Transcriptor de reuniones (notas → acta formal)
- Generador de SOPs (proceso → documento de procedimiento paso a paso)
- Analizador de datos (CSV → dashboard con insights)

---

## Paso 2 — Diseñar la skill

Antes de escribir, planifica la estructura:

1. **Input** — qué recibe la skill (qué pregunta al usuario)
2. **Proceso** — qué pasos sigue (en orden)
3. **Herramientas** — qué necesita usar (WebFetch, Bash, Read, Write, herramientas nativas de Claude Code)
4. **Output** — qué genera y en qué formato
5. **Experiencia de usuario** — cómo se siente usarla (mensajes amigables, flujo conversacional)

### Principios de diseño de skills

**1. No inventes datos** — si la skill necesita información del usuario, pregúntala. Nunca la inventes.

**2. Datos reales primero, preguntas después** — si la skill puede obtener datos automáticamente, hazlo primero. Solo pregunta lo que no puedes encontrar solo.

**3. Auto-instalación de dependencias** — si necesita herramientas, instálalas automáticamente.

**4. Libertad creativa en diseño** — si genera HTML/dashboards, no dictes CSS rígido. Describe el resultado y deja que Claude diseñe.

**5. Adaptación al contexto** — si la skill sirve para diferentes tipos, adapta las preguntas.

**6. Flujo conversacional** — debe sentirse como conversación natural, no formulario.

**7. Fallbacks amigables** — si algo falla, ofrece alternativa y sigue adelante.

**8. Mensaje de bienvenida** — si la skill va en un kit, incluye mensaje de bienvenida.

**9. Sin precios sugeridos** — no incluir "como servicio" ni precios al final.

**10. Resultado claro** — mostrar qué se generó, qué datos se usaron, qué falta.

---

## Paso 3 — Escribir la skill

Genera el archivo `.md` con estructura clara:

1. Frontmatter con `name` y `description`
2. Secciones numeradas con pasos claros
3. Ejemplos concretos
4. Reglas explícitas

---

## Paso 4 — Instalar la skill

Después de generarla, instálala en la carpeta correcta:

**Si es BUSINESS (privada):**
```bash
mkdir -p .claude/skills/business
cp [nombre-skill].md .claude/skills/business/
```

**Si es OTHER (pública):**
```bash
mkdir -p .claude/skills/other
cp [nombre-skill].md .claude/skills/other/
```

---

## Paso 5 — Crear kit (si la compartes)

Si la skill va a ser usada por otros, genera un kit completo con CLAUDE.md e INSTRUCCIONES.md.

---

## Paso 6 — Testear

1. Simula ser usuario nuevo
2. Verifica que las instrucciones son claras
3. Si genera archivos, verifica que funcionan
4. Ajusta si algo no fluye

---

## Paso 7 — Presentar al usuario

Muestra:
1. Nombre y ruta del archivo
2. Frases que la activan
3. Input y output
4. Instrucciones para usarla
5. Pregunta si quiere ajustar
