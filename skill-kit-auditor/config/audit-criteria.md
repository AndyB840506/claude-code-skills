# Criterios de auditoría — Ejemplos PASS / FAIL

Referencia completa para los 18 patrones de fallo detectables por `skill-kit-auditor`.
Carga este archivo cuando necesites detalle adicional sobre un criterio.

---

## #1 — Frontmatter: name coincide con folder

**PASS:**
```
Folder: .claude/skills/ai-lead-generator/
Archivo: SKILL.md
Frontmatter: name: ai-lead-generator   ← coincide exactamente
```

**FAIL — archivo mal nombrado dentro de carpeta:**
```
Folder: .claude/skills/smart-recruiter/
Archivo: smart-recruiter.md  ← debería llamarse SKILL.md
```

**FAIL — archivo plano en la raíz de skills (sin carpeta):**
```
.claude/skills/btq-guion.md  ← INCORRECTO
Correcto: .claude/skills/btq-guion/SKILL.md
```

**Acción correctiva:** Asegurarse de que `name:` en el frontmatter sea idéntico al nombre de la carpeta (kebab-case, sin mayúsculas). Nunca colocar archivos `.md` de skills directamente en la raíz de `.claude/skills/` — siempre usar subcarpeta con `SKILL.md`.

---

## #2 — Triggers: mínimo 5 frases, sin solapamientos

**PASS:**
```yaml
description: >
  Audita skills. Triggers: auditar skills, revisar kit, mejorar skills,
  skill audit, review skill kit, fix circular flows, quality check skills,
  mejorar consistencia, skill quality review, auditar proyecto.
```

**FAIL:**
```yaml
description: "Crea skills."
```
Motivo: menos de 5 triggers, solo en español.

**FAIL por solapamiento:**
- Skill A tiene trigger "revisar prompt"
- Skill B también tiene trigger "revisar prompt"

**Acción correctiva:** Mínimo 8 triggers (4 español + 4 inglés), sin frases idénticas entre skills.

---

## #3 — Consistencia de idioma entre archivos del proyecto

**PASS:**
```
CLAUDE.md: español  →  INSTRUCCIONES.md: español  →  SKILL.md: bilingüe ✓
```

**FAIL:**
```
CLAUDE.md: inglés
INSTRUCCIONES.md: español
SKILL.md: mezcla sin patrón
```

**Acción correctiva:** CLAUDE.md e INSTRUCCIONES.md deben estar en el mismo idioma (preferiblemente el idioma principal del usuario). SKILL.md puede ser bilingüe.

---

## #4 — Welcome message bilingüe en skills bilingües

**PASS:**
```markdown
## Welcome — Candidate Mode (English)
> **Smart Recruiter — Interview Starting**

## Bienvenida — Modo Candidato (Español)
> **Smart Recruiter — Empezamos la entrevista**
```

**FAIL:**
```markdown
## Welcome message
> **Smart Recruiter — Job Setup**
```
(Solo en inglés en una skill que dice soportar español)

**Acción correctiva:** Si la skill declara soporte bilingüe, cada welcome message necesita su versión en ambos idiomas.

---

## #5 — Principios sin duplicación en 3+ lugares

**PASS:**
```
SKILL.md: contiene los principios completos (fuente de verdad)
CLAUDE.md: referencia a SKILL.md o resumen de 2-3 líneas máximo
INSTRUCCIONES.md: no repite los principios
```

**FAIL:**
```
CLAUDE.md líneas 24-35: "Los 10 principios de una buena skill"
SKILL.md líneas 64-96: "13 Principios de diseño de skills"
INSTRUCCIONES.md líneas 15-30: "Principios que sigue Claude"
```
(Tres versiones diferentes del mismo contenido, ninguna es claramente la fuente de verdad)

**Acción correctiva:** Designar SKILL.md como única fuente de verdad para los principios. CLAUDE.md solo puede tener un link o resumen ultra-corto.

---

## #6 — Un solo punto de entrada de documentación

**PASS:**
```
README.md: tabla de contenidos concisa con links a secciones
```

**FAIL:**
```
README.md: "EMPIEZA AQUÍ — guía general"
ESTRUCTURA.txt: "Guía de navegación"
PANEL_PRINCIPAL.md: "⭐ LO IMPORTANTE"
```
(Tres archivos compiten por ser el punto de entrada sin orden claro)

**Acción correctiva:** Un solo archivo de entrada (README.md o CLAUDE.md). Los demás lo referencian, no lo duplican.

---

## #7 — Principio #2: datos primero, preguntas después

**PASS:**
```markdown
## Paso 0 — Detección automática
Lee job-config.json si existe. Si no existe, ir al Paso 1.
```

**FAIL:**
```markdown
## Paso 1 — Sondeo
Pregunta al usuario: ¿Qué vendes? ¿A quién? ¿En qué sector?
[Luego en Paso 2: busca datos en la web]
```
(Pide datos al usuario antes de intentar obtenerlos automáticamente)

**Acción correctiva:** Intentar leer/buscar datos automáticamente primero. Solo preguntar si no se pudieron obtener.

---

## #8 — Principio #6: máximo 2-3 bloques de preguntas

**PASS:**
```markdown
Bloque 1 (datos básicos): "¿Nombre del puesto y empresa?"
[procesa y continúa]
Bloque 2 (requisitos): "¿Requisitos obligatorios? ¿Deseables?"
```

**FAIL:**
```markdown
Paso 1: ¿Qué vendes?
Paso 1.1: ¿A qué empresa?
Paso 1.2: ¿Sector?
Paso 1.3: ¿Tamaño de empresa?
Paso 1.4: ¿País?
Paso 1.5: ¿Idioma del cliente?
```
(6 preguntas seguidas que se perciben como interrogatorio)

**Acción correctiva:** Agrupa preguntas relacionadas en un solo mensaje. Máximo 3 preguntas por bloque.

---

## #9 — Principio #4: sin diseño rígido prescriptivo

**PASS:**
```markdown
Genera un reporte HTML con los datos. Puedes elegir el estilo visual.
```

**FAIL:**
```markdown
Reglas CSS obligatorias:
- Fondo: #F9FAFB
- Leads COLD: #E5E7EB
- Leads WARM: #DBEAFE
- Leads HOT: #FEF3C7
- Font-family: Arial, sans-serif
- Print: @media print { margin: 0.5in }
```
(Viola el principio #4 al dictar estilos exactos en lugar de dar libertad creativa)

**Acción correctiva:** Dar guías de contenido, no de CSS. Si hay un brand kit, referenciar su ID, no copiar sus colores.

---

## #10 — Numeración de pasos coherente

**PASS:**
```
Paso 1, Paso 2, Paso 3, Paso 4...
```
o
```
Paso 0 (setup), Paso 1, Paso 2...  ← aceptable si Paso 0 es claramente setup
```

**FAIL:**
```
Paso -1 (detección de idioma)
Paso 0 (configuración)
Paso 1 (sondeo)
Paso 1.5 (validación intermedia)
Paso 2...
```
(Numeración negativa y decimales crean ambigüedad sobre el orden real)

**Acción correctiva:** Usar enteros positivos empezando desde 0 o 1. Si hay un paso de setup, llamarlo "Paso 0 — Inicialización" o simplemente "Antes de empezar".

---

## #11 — Skill con contenido ejecutable propio

**PASS:**
```markdown
## Paso 1 — Análisis del transcript
Lee el transcript y extrae: nombre del candidato, puesto, fecha.
Aplica la rubric de evidencia: [criterios concretos aquí o en config/].
Output: objeto JSON con los campos X, Y, Z.
```

**FAIL:**
```markdown
## Uso
Para implementar, ejecutar workflows/design-scoring-engine.md
Para testear, ver workflows/test-and-deploy.md
```
(La skill es solo un índice de otros archivos; no puede ejecutarse sin cargar workflows)

**Acción correctiva:** SKILL.md debe ser ejecutable con la información que contiene. Los workflows son para detalle adicional, no para sustituir el flujo principal.

---

## #12 — Conteos matemáticamente correctos

**PASS:**
```markdown
Entrevista: ~12 exchanges
- Bloque 1 (dealbreakers): 2-3 exchanges
- Bloque 2 (background): 3-4 exchanges
- Bloque 3 (competencias): 3-4 exchanges
- Bloque 4 (cierre): 1-2 exchanges
Total declarado vs real: 9-13 ≈ ~12 ✓
```

**FAIL:**
```markdown
Entrevista: ~10-14 exchanges
- Exchange 1-2: dealbreakers
- 2-3 exchanges: background
- 3-5 exchanges: must-haves
- 2-3 exchanges: behavioral
- 1-2 exchanges: nice-to-haves
```
Suma real: 2 + 3 + 5 + 3 + 2 = 15 máximo, 9 mínimo. Declarado: 10-14. No coincide.

**Acción correctiva:** Sumar los rangos y verificar que el total declarado esté dentro del rango real.

---

## #13 — Comandos compatibles con Windows

**PASS:**
```bash
# Verificado para bash/zsh:
curl -s "https://api.example.com" -H "Authorization: Bearer $TOKEN"
```
o
```powershell
# Para PowerShell/Windows:
Invoke-WebRequest -Uri "https://api.example.com" -Headers @{Authorization="Bearer $env:TOKEN"}
```

**FAIL:**
```bash
curl -s 'https://api.example.com' \
  -H 'Authorization: Bearer '$TOKEN \
  -d '{"q": "'"$QUERY"'"}'
```
(Escape con comillas simples/dobles anidadas no funciona en PowerShell/cmd.exe)

**Acción correctiva:** Si la skill incluye comandos de terminal, proveer versión para bash Y para PowerShell, o usar solo sintaxis compatible con ambos.

---

## #14 — Variables de entorno con valores documentados

**PASS:**
```markdown
Variables requeridas en `.env`:
- `HIRESIGNAL_API_KEY`: tu API key de HireSignal (formato: `hs_xxxxx`)
- `HIRESIGNAL_MODE`: entorno de ejecución. Valores válidos: `development`, `production`
- `PORT`: puerto del servidor. Por defecto: `3000`
```

**FAIL:**
```env
HIRESIGNAL_API_KEY=your_api_key_here
HIRESIGNAL_MODE=development
PORT=3000
```
(No documenta qué valores son válidos para HIRESIGNAL_MODE ni el formato de la API key)

**Acción correctiva:** Para cada variable, documentar: descripción, valores válidos posibles, valor por defecto si aplica.

---

## #15 — Archivos de entrega sincronizados

**PASS:**
```
leracom-mcp-builder/ modificado: 2026-05-20
ENTREGA_LERACOM/leracom-mcp-builder.zip modificado: 2026-05-20 ✓
```

**FAIL:**
```
leracom-mcp-builder/ modificado: 2026-05-15 (más reciente)
ENTREGA_LERACOM/leracom-mcp-builder.zip modificado: 2026-05-12 (desactualizado)
```

**Acción correctiva:** Regenerar el ZIP o agregar una nota en README indicando que los ZIPs son snapshots y pueden estar desactualizados. Alternativamente, automatizar la generación de ZIPs como parte del flujo de entrega.

---

## #16 — Sin contenido de tecnología específica en skills genéricas

**PASS:**
```markdown
### Anti-patterns en proyectos backend
- No hardcodear credenciales en el código
- No omitir manejo de errores en llamadas a APIs externas
```

**FAIL:**
```markdown
### Anti-patterns a evitar en proyectos PHP/backend
- No usar `mysql_query()` — usar PDO
- No mezclar HTML con lógica PHP
```
(PHP-específico en una skill genérica de creación de skills)

**Acción correctiva:** Mover el contenido específico de tecnología a la skill o proyecto que lo necesita. En skills genéricas, usar ejemplos agnósticos al lenguaje.

---

## #17 — Sin contenido duplicado entre skills distintas

**PASS:**
```
btq-guion/SKILL.md: "Las reglas de Tone Master están en btq-project/SKILL.md sección 4."
btq-project/SKILL.md: contiene las reglas completas  ← única fuente de verdad
```

**FAIL:**
```
btq-guion/SKILL.md líneas 40-60:   tabla completa del roadmap Season 2 (12 filas)
btq-project/SKILL.md líneas 191-205: misma tabla del roadmap Season 2 (12 filas)
```
(Dos fuentes de verdad para la misma tabla. Cuando el roadmap cambie, solo se actualiza una.)

**Acción correctiva:** Designar una skill como fuente de verdad. La otra referencia
con "ver [nombre-skill]/SKILL.md sección X." No duplicar tablas, listas de más de
3 ítems, ni bloques de reglas entre skills distintas.

---

## #18 — Skills de ciclo de vida referencian hooks

**PASS:**
```markdown
## Auto-trigger via SessionEnd Hook
Puedes configurar esta skill para que se dispare automáticamente al cerrar la sesión.
Agrega a `settings.json`: { "hooks": { "SessionEnd": [...] } }
```

**FAIL:**
```markdown
# Session Close
Ejecuta /session-close al final de cada sesión.
[Sin mención de hooks, sin auto-trigger, sin referencia a SessionEnd]
```
(Una skill diseñada para ejecutarse al final de sesión que no menciona que puede
auto-dispararse via hook — el usuario tiene que recordar invocarla manualmente siempre)

**Aplica a skills que:**
- Se invocan típicamente al final/inicio de sesión (`session-close`, `handoff`, `retrospective`)
- Guardan estado o contexto antes de que el sistema lo descarte
- Están diseñadas para ejecutarse en intervalos regulares (reportes, monitoreo, backups)

**NOTA:** Si la skill es intencionalmente manual (el usuario debe decidir cuándo invocarla),
puede documentar "Esta skill es manual por diseño — no se recomienda auto-trigger" y también pasa.

**Acción correctiva:** Agregar sección "Auto-trigger via Hook" con ejemplo de configuración
en `settings.json`. Mencionar qué hook aplica (`SessionEnd`, `PreCompact`, etc.) y advertir
si hay conflicto con otras skills del kit.
