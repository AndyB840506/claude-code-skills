# Paso 1 — Entender Qué Necesita el Usuario

Pregunta de forma conversacional (no como formulario).

## Preguntas Clave

- **¿En qué idioma?** — Español, English, o ¿bilingüe (ambos)?
- **¿Qué quieres automatizar?** — Describe el proceso o resultado
- **¿Es de propósito general o específico?** — ¿Funciona para cualquier caso de uso, o es específico para un dominio, tipo de contenido, o herramienta?
- **¿Qué información necesita?** — URL, texto, carpeta, datos, archivo...
- **¿Qué debe generar?** — HTML, informe, código, archivo, dashboard...
- **¿Quién la usa?** — Solo tú, tu equipo, o públicamente
- **¿Cómo se publica o despliega el resultado?** — ¿El output final va a la web, a un archivo local, a una plataforma? (especialmente relevante si genera HTML o código)

## Si No Sabe Qué Crear

Propón ideas según su industria:

**Para negocios:**
- Generador de propuestas (datos → PDF/HTML profesional)
- Calculadora de presupuestos (horas/servicios → presupuesto)
- Generador de contratos (datos → contrato personalizado)
- Creador de presentaciones de ventas

**Para marketing:**
- Generador de copy para ads (producto → variantes)
- Planificador de contenido (nicho → calendario 30 días)
- Generador de emails de venta
- Generador de posts para redes (tema → IG/LinkedIn/X)

**Para desarrollo:**
- Generador de APIs (modelo → API completa)
- Documentador de código (repo → docs)
- Generador de tests (código → test suite)
- Scaffolding de proyectos

**Para productividad:**
- Resumidor de documentos (PDF → resumen)
- Transcriptor de reuniones (notas → acta)
- Generador de SOPs (proceso → procedimiento)
- Analizador de datos (CSV → dashboard)

## Si el Usuario Menciona un Kit o Skill Existente

Si dice "similar a X", "como el kit de Y", "parecido a lo que usamos para Z":
1. **Antes de diseñar**, leer ese kit: explorar sus workflows, config, y outputs
2. Reusar su arquitectura (router + workflows + docs) en lugar de inventar
3. Identificar qué tiene de diferente el nuevo kit vs. el referenciado

Esto evita rediseñar lo que ya existe y garantiza consistencia entre kits.

## Si Ya Describió Suficiente

Procede directamente al Paso 2 (Diseñar) sin más preguntas.
