# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Podcast Creator Kit — Mr. Putrid's Den

## Comportamiento al iniciar

Cuando el usuario abra esta carpeta y escriba cualquier cosa:

### Paso A — Detectar idioma

Analiza el primer mensaje:
- **"hola"** o español → responde en español, guarda `idioma: "es"`
- **"hello"** o inglés → responde en inglés, guarda `idioma: "en"`
- Si no es claro → responde bilingüe

### Paso B — Verificar perfil existente

Busca `podcast-profile.json` en el directorio actual.

---

## Si `podcast-profile.json` NO existe

> **Bienvenido al Kit de Producción de Podcast**
>
> ¿Ya tienes idea clara de qué va a tratar tu podcast, o todavía estás explorando ideas?

- Si ya lo tiene claro → lanza `00-setup.md`
- Si está explorando → muestra las 6 categorías de contenido (ver workflow 00-setup.md) → lanza `00-setup.md`

---

## Si `podcast-profile.json` SÍ existe

Lee el archivo y responde en el idioma guardado:

> **Bienvenido de vuelta a [nombre del podcast]**
>
> ¿Qué producimos hoy?
>
> 1. **Guion** — script completo del próximo episodio
> 2. **Plan de grabación** — checklist y guía para el día de grabación
> 3. **Artwork** — prompts para la portada del episodio
> 4. **Social Media** — plan de lanzamiento 3 días
> 5. **Show Notes** — descripción y metadatos para Spotify y Apple
> 6. **Exportar HTML** — paquete de producción + página pública
> 7. **Actualizar perfil** — cambiar datos del podcast

---

## Reglas globales

- **Leer `podcast-profile.json` siempre** antes de cualquier workflow. Si no existe → lanzar `00-setup.md`.
- **No inventar datos del podcast.** Si falta información, preguntar o usar `[PENDIENTE]`.
- **Idioma:** mantener el idioma detectado durante toda la sesión.
- **Al terminar cada workflow:** sugerir el siguiente paso lógico.
- **Documentos y guiones:** siempre en HTML optimizado para PDF (descargar vía IlovePDF).
- **Copias:** cada documento generado se copia a `G:\My Drive\kit-podcast-creator\` automáticamente.
- **Skill activa:** `podcast-creator` en `.claude/skills/podcast-creator/SKILL.md`

---

## Estructura de carpetas

```
kit-podcast-creator/
├── podcast-profile.json          ← Estado central del sistema
├── audio/                        ← Intro y outro del show
├── scripts/                      ← Guiones en HTML (EP.001, EP.002...)
├── documents/                    ← Propuestas y documentos importantes
├── fichas-invitados/             ← Una ficha por invitado de La Silla Pútrida
├── templates/                    ← Cuestionario y carta de invitación Silla Pútrida
├── glosario-cachaco.md           ← Términos cachacos de los 40's (consultar siempre)
├── eventos.json                  ← Base de datos de eventos para segmento de promo
└── .claude/skills/podcast-creator/
    ├── SKILL.md
    └── workflows/
        ├── 00-setup.md
        ├── 01-episodio.md
        ├── 02-grabacion.md
        ├── 03-artwork.md
        ├── 04-social-media.md
        ├── 05-show-notes.md
        └── 06-html-export.md
```

---

## Segmentos permanentes del podcast

### La Silla Pútrida
- Formato especial de episodio cuando hay invitado
- **Antes de generar cualquier guión**, preguntar: *"¿Esta semana hay Silla Pútrida?"*
- Si SÍ → el episodio gira 100% en torno al invitado
- Generar cuestionario de aprobación ANTES del guión y esperar confirmación del invitado
- El segmento de Promoción se mueve al FINAL del episodio
- Guardar ficha del invitado en `fichas-invitados/[nombre-invitado].md`
- Templates en `templates/silla-putrida-cuestionario.md` y `templates/silla-putrida-invitacion.md`

### Segmento de Promoción (todos los episodios)
- Presente en **todos** los episodios sin excepción (Juan lo conduce)
- Episodio normal → va en el bloque intermedio (antes del cierre)
- Episodio Silla Pútrida → va al final (después del bloque del invitado, antes del outro)
- Consultar `eventos.json` para usar eventos reales del segmento

---

## Lenguaje cachaco clásico bogotano de los 40's

Este es el lenguaje oficial del podcast. Aplica en **todos** los guiones, documentos y comunicaciones.

- Consultar `glosario-cachaco.md` antes de generar cualquier guión
- Palabras frecuentes: "ala", "chirriado", "pútrido", "cachifo", "sumerce", "caray", "carachas", "a la orden", "divino", "soberano"
- **NO usar:** "parcero" (muy moderno), "bacano" (moderno popular), "vosotros" (España), "vos" (paisa/argentino), "ché" (argentino)
- El tratamiento entre hosts y al oyente: "sumerce" (formal cachaco) o "usted" — nunca "tú" en los guiones

---

## Estructura de episodio según tipo

**Episodio normal (co-host Andrés + Juan):**
```
1. Intro music (30 seg)
2. Bienvenida — Andrés y Juan
3. Tema principal — Bloque A
4. [INTERCAMBIO]
5. Tema principal — Bloque B
6. Segmento de Promoción (Juan) — eventos, conciertos underground
7. Takeaway / Reflexión final
8. Outro music (30 seg)
```

**Episodio Silla Pútrida (con invitado):**
```
1. Intro especial Silla Pútrida (30 seg)
2. Bienvenida + presentación del invitado
3. Bloque de preguntas aprobadas — Bloque A
4. [INTERCAMBIO natural]
5. Bloque de preguntas aprobadas — Bloque B
6. Cierre con el invitado (dónde encontrarlo)
7. Segmento de Promoción (Juan) — AL FINAL
8. Outro music (30 seg)
```
