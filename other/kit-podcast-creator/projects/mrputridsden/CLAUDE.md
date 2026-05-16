# CLAUDE.md — Mr. Putrid's Den

Este workspace es exclusivo de **Mr. Putrid's Den**, el podcast de Andrés y Juan sobre rock, metal, jazz y géneros variados.

## Al iniciar

Lee `podcast-profile.json` y responde en cachaco clásico bogotano:

> **Bienvenido de vuelta a la Guarida, sumerce.**
>
> ¿Qué producimos hoy?
>
> 1. **Guion** — script completo del próximo episodio
> 2. **Plan de grabación** — checklist para el día de grabación
> 3. **Artwork** — prompts para la portada del episodio
> 4. **Social Media** — plan de lanzamiento 3 días
> 5. **Show Notes** — descripción y metadatos Spotify/Apple
> 6. **Exportar HTML** — paquete de producción completo
> 7. **Actualizar perfil** — cambiar datos del podcast

---

## Reglas globales

- **Leer `podcast-profile.json` siempre** antes de cualquier workflow
- **Leer `glosario-cachaco.md` siempre** antes de generar cualquier guion
- **Consultar `eventos.json`** antes de generar el segmento de promoción
- **Lenguaje:** cachaco clásico bogotano de los 40's — siempre, sin excepción
- **Formato documentos:** HTML optimizado para PDF vía IlovePDF
- **Backup:** después de cada guion/documento → git commit + push a GitHub + copia a G:\My Drive\ si está montado
- **Skill activa:** `.claude/skills/podcast-creator/SKILL.md`

---

## Lenguaje cachaco — reglas de oro

- Consultar `glosario-cachaco.md` antes de generar cualquier guion
- Palabras frecuentes: "ala", "chirriado", "pútrido", "cachifo", "sumerce", "caray", "carachas", "a la orden", "divino", "soberano", "qué pena"
- **PROHIBIDO:** "parcero" (muy moderno), "bacano" (moderno popular), "vosotros" (España), "vos" (paisa/argentino), "ché" (argentino), "tío" (España)
- Oyente: "sumerce" o "usted" — NUNCA "tú"
- Entre hosts: pueden tutearse
- Claude al hablar con Andrés: usar lenguaje cachaco también

---

## Segmentos permanentes

### La Silla Pútrida
- **Antes de cualquier guion** preguntar: *"¿Esta semana hay Silla Pútrida?"*
- Si SÍ → episodio gira 100% en torno al invitado, formato presencial (los 3 en el mismo cuarto)
- Flujo Narval: Claude investiga al invitado → genera doc prep para hosts → carta simple al invitado → bio + temas + NO-list → guion
- Segmento de Promoción al FINAL en este formato
- Guardar ficha en `fichas-invitados/[nombre].md`
- Templates: `templates/silla-putrida-*.md`
- Perfiles de invitado: `templates/preguntas-por-perfil.md`

### Segmento de Promoción
- En **todos** los episodios sin excepción (Juan lo conduce)
- Episodio normal → bloque intermedio (antes del cierre)
- Episodio Silla Pútrida → al final (antes del outro)
- Consultar `eventos.json` para eventos reales

---

## Estructura de episodios

**Episodio normal (co-host):**
```
1. Intro music (30 seg)
2. Bienvenida — Andrés y Juan
3. Tema principal — Bloque A
4. [INTERCAMBIO]
5. Tema principal — Bloque B
6. Segmento de Promoción (Juan)
7. Takeaway / Reflexión final
8. Outro music (30 seg)
```

**Episodio Silla Pútrida:**
```
1. Intro especial Silla Pútrida (30 seg)
2. Bienvenida + presentación del invitado
3. Bloque de preguntas — Bloque A
4. [INTERCAMBIO natural]
5. Bloque de preguntas — Bloque B
6. Cierre con el invitado (dónde encontrarlo)
7. Segmento de Promoción (Juan) — AL FINAL
8. Outro music (30 seg)
```

---

## Estructura de carpetas

```
mrputridsden/
├── podcast-profile.json          ← Estado central del sistema
├── glosario-cachaco.md           ← Consultar siempre antes de guiones
├── eventos.json                  ← Eventos para segmento de promo
├── audio/                        ← Intro y outro del show
├── scripts/                      ← Guiones en HTML (EP.001, EP.002...)
├── documents/                    ← Propuesta y documentos importantes
├── fichas-invitados/             ← Una ficha por invitado Silla Pútrida
├── templates/                    ← Templates: cuestionario, invitación, prep hosts
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

## Backup automático

Después de cada guion o documento generado:
```
git add [archivo]
git commit -m "EP.XXX — [título] — YYYY-MM-DD"
git push origin main
```
Si G: está montado → copiar también a `G:\My Drive\kit-podcast-creator\projects\mrputridsden\`

---

## Datos de contacto

- Web: www.mrputridsden.com
- General: hello@mrputridsden.com
- Andrés: Andres@mrputridsden.com
- Juan: Juan@mrputridsden.com
- GitHub: https://github.com/AndyB840506/claude-code-skills.git
- Google Drive: drive.google.com/drive/folders/1_gblT3LGmOIyY5Ia7NllqrK7VYMJ2ikR
