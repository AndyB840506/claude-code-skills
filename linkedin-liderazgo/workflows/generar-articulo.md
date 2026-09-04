# Workflow — Generar Artículo

## EXECUTION

Has invocado `/linkedin-liderazgo`. Ejecuta el proceso en pasos:

### Paso 1 — Calibrar voz (solo si no existe `perfil-voz.md`)

Verifica si existe `C:\Users\andre\.claude\skills\linkedin-liderazgo\perfil-voz.md`.

- **Si existe:** léelo y úsalo directamente. NO vuelvas a preguntar esto.
- **Si no existe:** pregunta en un solo bloque conversacional (no formulario uno por
  uno):
  ```
  Antes del primer artículo, calibremos tu voz (esto se guarda y no se repite):
  1. ¿Cómo describirías tu tono al escribir? (cercano, directo, formal, inspirador, con humor...)
  2. ¿Sueles usar anécdotas propias o casos de otros? Dame un ejemplo breve si tienes uno en mente.
  3. ¿Hay palabras o frases que odias ver en posts de LinkedIn? ("sinergia", "disruptivo", etc.)
  4. ¿Tienes alguna postura fuerte en temas de liderazgo que sueles defender? (ej: contra el micromanagement, a favor de la transparencia radical)
  5. ¿Usas emojis? ¿Cuántos hashtags al final sueles poner (0-3 es lo típico)?
  ```
  Guarda las respuestas en `perfil-voz.md` dentro de la carpeta de la skill, en
  formato libre pero completo — este archivo es la fuente de verdad de la voz del
  usuario en cada artículo futuro.

### Paso 2 — Pedir el tema

Si el usuario ya dio el tema al invocar la skill, sáltate esta pregunta. Si no:

> "¿Sobre qué tema de liderazgo empresarial quieres escribir?"

**Si el usuario dice que no sabe / pide ideas:** ofrece 2-3 ángulos de
`docs/temas-btq.md` (episodios ya trabajados en BTQ, el podcast de liderazgo del
usuario) — reescritos como pregunta o ángulo de LinkedIn, no como título del episodio.
Antes de usar uno, confirma su estado real si el episodio no está marcado publicado.
Nunca copiar frases del guion del podcast: es fuente de tema y caso, no de texto.

### Paso 3 — Generar el borrador

Escribe un artículo de 600-1200 palabras aplicando `perfil-voz.md`:
- Hook concreto en la primera línea (escena, número, o cita — nunca una apertura
  genérica).
- Desarrollo con al menos un ejemplo o anécdota específica (real del usuario si la
  dio, o marcada explícitamente como ejemplo hipotético si no).
- Postura clara del autor — no un balance vacío entre dos lados.
- Cierre sin muletillas de resumen; una idea, pregunta o llamado a la reflexión.
- Longitud y ritmo de oración variados (no todas las oraciones del mismo largo).
- Formato listo para LinkedIn: párrafos cortos, saltos de línea entre ideas, sin
  markdown de encabezados (LinkedIn no los renderiza).

### Paso 4 — Checklist anti-patrones de IA

Corre el checklist completo de `docs/anti-patrones-ia.md` contra el borrador. Para
cada uno de los 10 patrones, cuenta o revisa literalmente el texto (no lo estimes de
memoria) y corrige lo que aparezca. Arma la tabla de reporte como se especifica en ese
documento.

### Paso 5 — Generar portada con ComfyUI

**Toda portada se genera siempre con ComfyUI** — decisión del usuario, 2026-09-04.
Sigue `docs/estilo-visual.md` completo (estilo abstracto/conceptual, modelo Z-Image
Turbo, 1200×630, procedimiento de servidor + verificación visual + copia a
`linkedin-articulos\` + embebido vía shell sin pasar el base64 por el contexto).

Si el usuario pide explícitamente saltarse la portada, continúa al Paso 6 sin imagen.

### Paso 6 — Publicar como artifact y ofrecer ajustes

**Todo artículo se entrega siempre como Artifact (página HTML publicada), nunca solo
como texto plano en el chat** — decisión del usuario, 2026-09-04, para poder abrirlo y
copiarlo con un botón en vez de seleccionar texto a mano.

1. Carga la skill `artifact-design` antes de escribir el HTML (obligatorio, cada vez).
2. Construye la página con: la portada del Paso 5 arriba del título (si se generó),
   artículo en columna de lectura cómoda, botón "Copiar texto" (Clipboard API con
   fallback a `textarea` + `execCommand('copy')` — nunca un link de descarga, están
   bloqueados en el visor), hashtags, y la tabla del checklist de
   `docs/anti-patrones-ia.md` visible debajo del artículo (no oculta detrás de un
   toggle — es parte de la entrega, no un detalle secundario).
3. Trata el tema del artículo como el sujeto de diseño: paleta y tipografía específicas
   a ese artículo, no una plantilla fija reusada sin pensar — sigue el proceso de
   `artifact-design` (paleta de 4-6 tokens nombrados, 2-3 familias tipográficas con rol
   claro, layout en una o dos frases) antes de escribir el HTML. La misma paleta debe
   guiar el prompt de la portada (Paso 5) para que imagen y página se vean como un
   mismo objeto.
4. Título del artifact: 2-4 palabras específicas a la tesis del artículo (nunca
   genérico tipo "Artículo de LinkedIn"). Favicon: 📋 (consistente entre artículos de
   esta skill, para reconocerlos juntos en la galería).
5. Publica con `Artifact` (`action: publish`, sin `url` — cada artículo es una página
   nueva, no una actualización de la anterior).

Después de publicar, pregunta: "¿Ajusto algo — tono, longitud, ángulo — o lo dejamos
así?"

Si el usuario pide un ajuste puntual, corrige solo esa parte, vuelve a correr el
checklist únicamente sobre el texto modificado, actualiza el HTML y publica de nuevo
sobre el mismo `file_path` de esta conversación (mismo URL).

### Paso 7 — Guardar el texto (opcional)

La portada (si se generó) ya quedó guardada en `C:\Users\andre\repos\linkedin-articulos\`
como parte del Paso 5 — esto es solo para el texto.

Pregunta: "¿Lo guardo en un archivo?" Si dice que sí:
- Verifica si existe `C:\Users\andre\repos\linkedin-articulos\`; si no, créala.
- Guarda como `YYYY-MM-DD-slug-del-tema.md` (fecha real del sistema, no inventada).
- Nunca guardes artículos generados dentro de `~/.claude/` — esa carpeta es solo para
  el archivo de instrucciones de la skill y `perfil-voz.md`, no para el contenido de
  producción.

---

**Artículo listo.** Reporta al final: tema usado, si se usó `perfil-voz.md` existente
o se calibró uno nuevo, y si se guardó en archivo (ruta) o no.
