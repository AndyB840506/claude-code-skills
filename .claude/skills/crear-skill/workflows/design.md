# Paso 2 — Diseñar la Skill

Planifica la estructura antes de escribir.

## 5 Elementos del Diseño

1. **Input** — Qué pregunta al usuario (datos, contexto, preferencias)
2. **Proceso** — Pasos que sigue (en orden)
3. **Herramientas** — Qué usa (WebFetch, Bash, Read, Write, nativas)
4. **Output** — Qué genera y formato (archivo, HTML, texto)
5. **UX** — Cómo se siente (mensajes, flujo conversacional)

## Ejemplo

| Elemento | Valor |
|---|---|
| Input | CSV de productos (usuario sube archivo) |
| Proceso | Leer CSV → Parsear datos → Generar HTML |
| Herramientas | Read (para leer CSV), Write (para guardar HTML) |
| Output | Archivo HTML con fichas de producto |
| UX | Mensajes amigables, progreso visual |

## Si el output es un artifact interactivo

Cargar `artifact-capabilities` y revisar las restricciones del runtime **antes** de
diseñar, no después de que fallen. Las que más muerden:

- **El sandbox bloquea `confirm()` y `alert()`** — devuelven `false` sin mostrar nada y
  sin error, así que toda acción puesta detrás de una confirmación nativa **nunca se
  ejecuta**. Los botones se ven bien y no hacen nada. Confirmación dentro de la página,
  en dos toques (mordió el 2026-09-15: tres botones destructivos muertos a la vez).
- **Las descargas que inicia la página están bloqueadas** salvo con la capacidad
  `downloads`; el portapapeles sí funciona.
- **Solo cargan recursos de unos pocos hosts** — todo lo demás falla en silencio.
- **Una capacidad puede resolver `null`** (vista sin permiso): diseñar la página para
  que siga siendo útil sin ella, y decirlo en pantalla.

Y una consecuencia de diseño, no solo técnica: **el usuario prueba lo que yo no puedo
ejecutar**. Antes de construir, decidir qué va a mostrar la página cuando algo falle —
un panel de diagnóstico visible vale más que cinco rondas de hipótesis.

## Siguiente

Procede a Paso 3 (Crear e Instalar).
