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

## 15. Aprobación Antes de Acciones Irreversibles

Toda skill que haga commit, deploy, llamada a API externa, o envío de email debe
presentar los resultados y esperar aprobación explícita **antes** de ejecutar.

**Patrón:**
> "Assets listos. ¿Apruebas o ajustas algún bloque antes de hacer commit?"

**Regla:** Si el usuario dice "ajustar [X]", revisa solo ese bloque — no regeneres todo.
Si dice "sí", procede.

**Anti-patrón:** Hacer commit automáticamente después de generar sin gate de aprobación.

---

## 16. Generación en Paralelo

Si la skill genera múltiples outputs independientes (ej: SEO + redes sociales + artwork),
generarlos todos en una sola respuesta con etiquetas claras — no en turnos separados.

**Bien:**
```
**A · Spotify SEO**
...

**B · Social plan**
...

**C · Prompts de artwork**
...
```

**Mal:** "Primero el SEO. ¿Listo? Ahora el social. ¿Listo? Ahora el artwork."

**Por qué:** Reduce turnos de conversación, mantiene contexto completo visible para aprobación.

---

## 14. Validación Geográfica para Documentos Específicos de Ubicación

Antes de redactar cualquier documento que dependa de una provincia/estado/país (formularios de gobierno, solicitudes de becas, registros legales, documentos de cumplimiento):

1. Extraer señales de ubicación de TODO lo disponible: código de área del teléfono (+1 587 = Alberta, +1 416 = Ontario, etc.), código postal, ciudad/provincia mencionada explícitamente
2. Confirmar con el usuario: "¿Confirmas que operan en [provincia inferida]?" antes de empezar
3. Solo entonces comenzar el borrador

**Anti-patrón:** Generar el documento y luego corregir la provincia — requiere reescritura completa de estadísticas, ciudades, leyes, costos de registro, y referencias gubernamentales.  
**Mejor:** Validar primero, generar una sola vez correctamente.

## 17. Reglas Verificables — Condición → Acción → Verificación

Cada regla de juicio que agregues a una skill (no los pasos de `## EXECUTION`, sino las
reglas de "cuándo hacer qué" que vive junto a ellos) debe tener forma explícita:

**"Cuando [condición disparadora], hacer [acción concreta], verificar con [método
comprobable]."**

**Mal:** "Revisa que el texto sea claro antes de entregar."
**Bien:** "Cuando el output incluya una cita textual, verificar contra el audio/fuente
original antes de aprobar — no aceptar de memoria."

Una regla sin condición de disparo explícita o sin método de verificación es prosa, no
regla: un modelo que infiere menos del contexto (ej. Opus vs. Fable) la va a pasar por
alto o aplicarla de forma inconsistente. Antes de dar una skill por terminada, revisa
cada regla de juicio y confirma que tenga las tres partes.
