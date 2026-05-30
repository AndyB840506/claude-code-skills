# Leracom MCP Server Builder - Instrucciones

**Para: Equipo de Desarrollo Leracom**
**Fecha: 12 de Mayo 2026**
**Objetivo: Crear MCP Server para integrar HireSignal con Claude Code**

---

## Quick Start (5 minutos)

### Paso 1: Ubicación de la Skill

```
Tu skill está en:
.claude/skills/leracom-mcp-builder/

Archivos principales:
- SKILL.md         ← Descripción de la skill
- PROMPT.md        ← El prompt que ejecutas
- config/          ← Archivos de configuración (JSON, MD)
```

### Paso 2: Ejecutar en VS Code

**Opción A: Command Palette**

```
1. Abre Command Palette (Ctrl+Shift+P)
2. Escribe: "Claude Code: Run Skill"
3. Selecciona: "leracom-mcp-builder"
4. Responde las 3-4 preguntas
5. Espera 2-3 minutos → Proyecto generado
```

**Opción B: Slash command**

```
/leracom-mcp-builder
```

**Opción C: Copiar Prompt**

```
1. Abre PROMPT.md en esta carpeta
2. Copia TODO el contenido
3. Pégalo en el chat con Claude
4. Espera 2-3 minutos → Proyecto generado
```

---

## Preguntas que te hará la Skill (4 preguntas exactas)

Cuando ejecutes, te hará estas 4 preguntas en este orden:

| # | Pregunta | Respuesta esperada | Ejemplo |
|---|----------|-------------------|---------|
| 1 | ¿Dónde crear el servidor MCP? | Nombre de carpeta | `leracom-mcp-server` |
| 2 | ¿Incluir tests? | Sí o No | `sí` (recomendado) |
| 3 | ¿Qué puerto para desarrollo? | Número de puerto | `3000` |
| 4 | ¿URL HireSignal API? | URL o vacío para demo | `https://hiresignal.example.com` o dejar vacío |

**Todas las respuestas se guardan en `.env` automáticamente para deployment posterior.**

---

## Lo que recibirás

Después de ejecutar la skill, tendrás una carpeta completa:

```
leracom-mcp-server/
├── src/
│   ├── index.ts                    ← Servidor MCP Node.js
│   ├── tools/
│   │   ├── scoreInterview.ts       ← Herramienta 1: Scoring
│   │   ├── listJobDescriptions.ts  ← Herramienta 2: Listar JDs
│   │   ├── getJobDetails.ts        ← Herramienta 3: Detalles JD
│   │   ├── submitScore.ts          ← Herramienta 4: Guardar score
│   │   ├── getInterviewHistory.ts  ← Herramienta 5: Historial
│   │   └── getAnalytics.ts         ← Herramienta 6: Analytics
│   ├── types/
│   │   ├── mcp.ts                  ← Interfaces MCP
│   │   └── hiresignal.ts           ← Interfaces HireSignal
│   └── utils/
│       └── api-client.ts           ← Cliente HTTP
├── config/
│   ├── scoring-schema.json         ← Esquema de scoring
│   ├── contradiction-rules.md      ← Reglas de contradicciones
│   ├── evidence-rubric.md          ← Rúbrica de evidencia
│   └── report-template.json        ← Template de reporte
├── package.json                    ← Dependencias NPM
├── tsconfig.json                   ← Configuración TypeScript
├── .env.example                    ← Variables de entorno
├── README.md                       ← Guía de inicio
├── IMPLEMENTACION.md               ← Detalles técnicos
├── DEPLOYMENT_CHECKLIST.md         ← Checklist pre-deployment
└── tests/
    └── tools.test.ts               ← Tests básicos
```

---

## Después de Generar: Próximos Pasos

### 1. Instalar Dependencias

```bash
cd leracom-mcp-server
npm install
```

### 2. Configurar Variables de Entorno

```bash
cp .env.example .env
# Edita .env con tu ANTHROPIC_API_KEY
```

### 3. Correr Localmente

```bash
npm run dev
# → Servidor MCP escuchando en http://localhost:3000
```

### 4. Conectar desde Claude Code

En la configuración de Claude Code:

```json
{
  "mcp": {
    "servers": {
      "hiresignal": {
        "command": "http://localhost:3000"
      }
    }
  }
}
```

### 5. Usar las Herramientas

En cualquier skill o proyecto, ahora puedes usar:

```
"Usa ScoreInterview para analizar esta transcripción..."
→ Funciona automáticamente con el MCP Server
```

---

## Documentación Incluida

Después de generar, lee en este orden:

1. **README.md** (5 min) → Qué hace el servidor, cómo correr
2. **IMPLEMENTACION.md** (10 min) → Detalles técnicos de cada tool
3. **DEPLOYMENT_CHECKLIST.md** (5 min) → Antes de ir a producción

---

## Las 6 Herramientas MCP

| Herramienta | Input | Output | Uso |
|------------|-------|--------|-----|
| **ScoreInterview** | Transcript, Job Title, Seniority | Verdict, Score, Evidence | Analizar entrevista |
| **ListJobDescriptions** | (ninguno) | Lista de JDs | Ver trabajos disponibles |
| **GetJobDetails** | jobId | Detalles completos del JD | Ver specs de un trabajo |
| **SubmitScore** | jobId, candidateName, score, verdict | Success, interviewId | Guardar resultado |
| **GetInterviewHistory** | jobId?, limit? | Lista de interviews pasadas | Historial de scoring |
| **GetAnalytics** | jobId? | KPIs, estadísticas | Métricas de hiring |

---

## Deployment a Producción

Después de probar localmente:

### Opción 1: Vercel (Recomendado)

```bash
npm install -g vercel
vercel
# → Sigue los pasos, auto-deploys
```

### Opción 2: Railway

```bash
# Crea proyecto en railway.app
# Conecta tu repo GitHub
# Auto-deploys en cada push
```

### Opción 3: Heroku

```bash
heroku create leracom-mcp-server
git push heroku main
```

---

## Si Algo No Funciona

### "npm install falla"

```bash
# Asegúrate de tener Node 18+
node --version

# Si es muy viejo:
nvm install 18
nvm use 18
npm install
```

### "El servidor no inicia"

```bash
# Revisa que el puerto 3000 esté libre:
lsof -i :3000          # Mac/Linux
netstat -ano | findstr :3000  # Windows

# O usa otro puerto en .env:
PORT=3001
```

### "Error de API Key"

```bash
# Verifica que .env tiene tu API key:
cat .env | grep ANTHROPIC_API_KEY
```

### "Las herramientas no responden"

```bash
# Revisa los logs del servidor:
npm run dev
# Busca errores en la consola
```

---

## Soporte

1. Lee **README.md** en la carpeta generada
2. Revisa **IMPLEMENTACION.md** para detalles técnicos
3. Consulta **DEPLOYMENT_CHECKLIST.md** antes de deployar
4. Contacto: (configurar en .env o README del proyecto)

---

## Archivos de Configuración

La skill incluye 4 archivos de configuración (en `config/`):

- **scoring-schema.json** → Define las 7 dimensiones, pesos, umbrales
- **contradiction-rules.md** → Cómo detectar contradicciones (CRITICAL/WARNING/NOTE)
- **evidence-rubric.md** → Cómo extraer evidencia de transcripciones
- **report-template.json** → Estructura del reporte HTML

Estos archivos definen **exactamente cómo HireSignal puntúa candidatos**. El MCP Server los usa para validar requests.

---

## Qué hace el MCP Server

```
Usuario en Claude Code
    ↓
Usa tool "ScoreInterview"
    ↓
MCP Server recibe request
    ↓
Llama Claude API (con scoring-schema.json)
    ↓
Claude analiza transcript
    ↓
Devuelve verdict + evidence
    ↓
Usuario ve resultado en Claude Code
```

**No hay UI, todo es automático desde Claude Code.**

---

## Resumen de Ejecución

```
1. Ejecuta la skill          (2 min)
2. npm install              (1 min)
3. Configura .env           (1 min)
4. npm run dev              (1 min)
5. Conecta desde Claude Code (2 min)
6. ¡Usa las herramientas!   (∞ min de productividad)
```

---

**Comienza con PROMPT.md o ejecuta `/leracom-mcp-builder` en Claude Code.**
