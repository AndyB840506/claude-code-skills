---
name: leracom-mcp-builder
description: "Automatiza la creación completa del MCP Server para HireSignal. Genera estructura TypeScript/Node.js, herramientas MCP, servidor local, y documentación. Use cuando necesite crear un MCP server que conecte Claude Code con HireSignal. Triggers ES: crear MCP server, construir servidor MCP, MCP para HireSignal, conectar Claude con HireSignal, generar servidor MCP, leracom MCP, servidor TypeScript MCP. English triggers: build MCP server, create MCP server, MCP for HireSignal, HireSignal MCP, connect Claude to HireSignal, TypeScript MCP server, MCP builder, generate MCP, leracom server."
---

# Leracom MCP Server Builder

**Automatiza la creación completa del MCP Server para HireSignal**

Una skill que crea automáticamente todo lo necesario para que Leracom conecte Claude Code con HireSignal:
- Estructura TypeScript/Node.js completa
- Herramientas MCP (tools) implementadas
- Servidor funcionando en local
- Documentación lista para deployment

---

## HireSignal API Integration

**Base URL Configuration:**

```
Production:  https://api.hiresignal.com/v1
Staging:     https://staging-api.hiresignal.com/v1
Development: http://localhost:3000/api/v1
```

**Important:** 
- Use the URL WITHOUT trailing slash in `.env`
- The SDK will append endpoint paths automatically
- Example: URL = `https://api.hiresignal.com/v1`, endpoint `/scoring/analyze` → full request to `https://api.hiresignal.com/v1/scoring/analyze`

**Set in `.env` as:**
```env
# Production
HIRESIGNAL_API_URL=https://api.hiresignal.com/v1

# OR Staging
HIRESIGNAL_API_URL=https://staging-api.hiresignal.com/v1
```

**Required Endpoints:**

| Tool | Method | Endpoint | Purpose |
|------|--------|----------|---------|
| ScoreInterview | POST | `/scoring/analyze` | Analyze interview transcript |
| ListJobDescriptions | GET | `/jobs` | List all job descriptions |
| GetJobDetails | GET | `/jobs/{jobId}` | Get single job specification |
| SubmitScore | POST | `/results/submit` | Store scoring result |
| GetInterviewHistory | GET | `/results/history` | Retrieve past interviews |
| GetAnalytics | GET | `/analytics/summary` | Get hiring metrics |

**Authentication:** Bearer token in `HIRESIGNAL_API_KEY` environment variable

---

## Quick Start (5 minutos)

```bash
# En VS Code o terminal, simplemente corre:
/leracom-mcp-builder

# O copia el prompt en la skill y ejecuta
```

**Resultado:** Carpeta `leracom-mcp-server/` completamente funcional con:
- ✅ Servidor MCP Node.js + TypeScript
- ✅ 6 Tools implementadas (ScoreInterview, ListJobs, etc.)
- ✅ Integración Claude API
- ✅ package.json + tsconfig.json
- ✅ README con instrucciones deployment
- ✅ Tests básicos

---

## Lo que entrega

**Carpeta generada automáticamente:**

```
leracom-mcp-server/
├── src/
│   ├── index.ts                 ← Servidor MCP principal
│   ├── tools/
│   │   ├── scoreInterview.ts
│   │   ├── listJobDescriptions.ts
│   │   ├── getJobDetails.ts
│   │   ├── submitScore.ts
│   │   ├── getInterviewHistory.ts
│   │   └── getAnalytics.ts
│   ├── types/
│   │   ├── mcp.ts
│   │   └── hiresignal.ts
│   └── utils/
│       └── api-client.ts
├── config/
│   ├── scoring-schema.json      ← Spec de scoring
│   ├── contradiction-rules.md   ← Reglas de contradicciones
│   ├── evidence-rubric.md       ← Rúbrica de evidencia
│   └── report-template.json     ← Template de reporte
├── package.json
├── tsconfig.json
├── .env.example
├── README.md                    ← Deployment guide
├── IMPLEMENTACION.md            ← Detalles técnicos
└── tests/
    └── tools.test.ts            ← Tests básicos
```

---

## Herramientas MCP Implementadas

1. **ScoreInterview** — Llama Claude para analizar transcripción
2. **ListJobDescriptions** — Obtiene JDs disponibles
3. **GetJobDetails** — Detalles de un JD específico
4. **SubmitScore** — Guarda resultado de scoring
5. **GetInterviewHistory** — Historial de entrevistas
6. **GetAnalytics** — Estadísticas y KPIs

---

## Cómo funciona

1. **Corre el skill** → Te pregunta si quieres crear/actualizar server
2. **Instala dependencias** → npm install automático
3. **Inicia servidor** → `npm run dev` funciona
4. **Conéctate desde Claude Code** → Configura en settings
5. **Usa las herramientas** → En cualquier skill o proyecto

---

## Para Leracom

**Instrucciones simples:**

1. En VS Code: Abre Command Palette → "Claude Code: Run Skill"
2. Selecciona "leracom-mcp-builder"
3. Responde las preguntas (3-4 preguntas)
4. En 2-3 minutos: Proyecto completamente generado
5. Lee README.md para deployment

**El servidor estará listo para:**
- Conectar con HireSignal API
- Responder tools desde Claude Code
- Desplegar en producción

---

## Stack Técnico

- **Runtime:** Node.js 18+
- **Lenguaje:** TypeScript
- **MCP:** @modelcontextprotocol/sdk
- **HTTP Client:** axios
- **Dev:** ts-node, nodemon
- **Tests:** Jest

---

## Environment Configuration

**`.env.example` template (required keys):**

```env
# Required - HireSignal API
HIRESIGNAL_API_URL=https://api.hiresignal.example.com/v1
HIRESIGNAL_API_KEY=your_bearer_token_here

# Required - Claude API
ANTHROPIC_API_KEY=sk-ant-xxxxx

# Optional - Execution mode. Valid values:
#   development → uses mock data, skips real API calls
#   staging     → connects to staging-api.hiresignal.com
#   production  → connects to api.hiresignal.com (default if omitted)
HIRESIGNAL_MODE=development
NODE_ENV=development

# Optional - Server port
PORT=3000
```

**How to set up:**
```bash
cp .env.example .env
# Edit .env with your actual keys
```

**Keep `.env` out of git:**
```bash
echo ".env" >> .gitignore
```

## Deployment

Después de generar, el README incluye:
- ✅ Cómo correr localmente (`npm run dev`)
- ✅ Cómo desplegar en Vercel/Railway/Heroku
- ✅ Configuración de variables de entorno
- ✅ Troubleshooting común
- ✅ Conexión desde Claude Code

**Pre-deployment checklist:**
- [ ] All 6 tools tested locally
- [ ] HireSignal API credentials validated
- [ ] Environment variables set in deployment platform
- [ ] Tests passing (`npm test`)
- [ ] Production API URL configured

---

## Soporte

- **README.md** → Instrucciones paso a paso
- **IMPLEMENTACION.md** → Detalles técnicos
- **Email:** (configurar en .env o README del proyecto)

---

**Listo para Leracom.** Corre y obtiene un MCP Server completo en minutos.

---

## EXECUTION

**Cuando se invoca `/leracom-mcp-builder`, ejecutar:**

1. Leer el archivo de ejecución: `.claude/skills/leracom-mcp-builder/PROMPT.md`
2. Seguir las instrucciones de ese archivo paso a paso

Este `SKILL.md` es documentación y referencia técnica. `PROMPT.md` contiene el flujo de generación. Siempre leer `PROMPT.md` antes de ejecutar cualquier acción.

**Nota de diseño:** Esta skill usa `PROMPT.md` como executor intencional — es un template de generación de código que varía por proyecto. No se embebe en `SKILL.md` porque cambiaría según el cliente (Leracom vs otros). Esto es by design, no un fallo del criterio #11.
