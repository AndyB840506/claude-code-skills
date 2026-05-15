# 10+ Principios de Diseño de Skills

Estos hacen que una skill sea realmente buena:

## 1. No Inventes Datos

Si la skill necesita información del usuario, pregúntala. Nunca la inventes.

**Mal:** Genero una propuesta con nombre ficticio  
**Bien:** Pregunto "¿Nombre del cliente?"

## 2. Datos Reales Primero, Preguntas Después

Si puedes obtener datos automáticamente (web scraping, lectura de archivos), hazlo primero. Solo pregunta lo que no puedas encontrar.

**Mal:** Preguntar por todo  
**Bien:** Leer lo que existe, preguntar lo que falta

## 3. Auto-Instalación de Dependencias

Si necesita herramientas, instálalas automáticamente.

Aviso: "Preparando herramientas (30 segundos la primera vez)"

## 4. Libertad Creativa en Diseño

Si genera HTML/dashboards, no dictes CSS rígido. Describe el resultado visual deseado, deja que Claude diseñe.

Resultado: Más bonito y único.

## 5. Adaptación al Contexto

Si la skill sirve para múltiples tipos (ej: propuestas para diferentes industrias), adapta las preguntas.

## 6. Flujo Conversacional

Debe sentirse como conversación natural, no como formulario.

**Mal:**
```
1. Nombre del cliente
2. Servicios
3. Horas
[formulario largo]
```

**Bien:** Preguntas naturales, agrupadas en bloques

## 7. Fallbacks Amigables

Si algo falla (instalación, scraping), no bloquees. Ofrece alternativa y sigue adelante.

## 8. Mensaje de Bienvenida

Si la skill va en un kit, incluye mensaje de bienvenida que se active con cualquier input del usuario.

## 9. Sin Precios Sugeridos

No incluir "como servicio" ni precios al final del output.

## 10. Resultado Claro

Al terminar, mostrar qué se generó, qué datos se usaron, qué falta.

Ejemplo:
```
✓ Propuesta generada: propuesta-acme-2026-05-14.html
✓ Datos usados: nombre, servicios, horas
⚠️ Falta: presupuesto desglosado (agregar manualmente)
¿Quieres ajustar algo?
```

## 11. Modelos Fijos, API Key Configurable

Los proyectos que usan IA no deben exponer la elección del modelo al usuario final. Fijar siempre el mejor modelo (ej: Sonnet para chat, Opus para reportes).

Lo único configurable: la API key.

## 12. Tono Conversacional Progresivo

Si genera un agente conversacional, empezar cálido y empático. Solo volverse más directo si detectas patrones que lo justifiquen (respuestas evasivas, inconsistencias).

## 13. Nombre Humano para Agentes

Si creas un agente conversacional, darle nombre humano rotativo por sesión. Humaniza la interacción.

Ejemplo: "Yo soy María" vs "Yo soy tu asistente" → la segunda es fría.
