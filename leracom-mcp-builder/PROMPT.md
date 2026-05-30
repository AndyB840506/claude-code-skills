# Leracom MCP Server Builder - Prompt

Ejecuta este prompt para generar automáticamente el MCP Server completo para HireSignal.

---

## 🚀 START HERE

Eres un experto en MCP (Model Context Protocol) servers y debes crear un servidor MCP completamente funcional para que Leracom integre HireSignal con Claude Code.

**Tu tarea:** Generar una carpeta `leracom-mcp-server/` con todo lo necesario para que Leracom simplemente:
1. Corra `npm install`
2. Configure variables de entorno
3. Corra `npm run dev`
4. Tenga un MCP Server completamente funcional

---

## Especificaciones

### 🎯 Servidor MCP Node.js + TypeScript

**Estructura base:**
```
leracom-mcp-server/
├── src/index.ts          ← Servidor MCP principal
├── src/tools/            ← Cada herramienta en archivo separado
├── src/types/            ← TypeScript interfaces
├── src/utils/            ← Funciones compartidas
├── config/               ← Archivos de configuración (JSON/MD)
├── package.json
├── tsconfig.json
├── .env.example
└── README.md
```

### 🛠️ 6 Herramientas MCP a Implementar

**Cada herramienta es un archivo `.ts` independiente en `src/tools/`**

#### 1. **ScoreInterview** (src/tools/scoreInterview.ts)
```
Input:
  - transcript: string (texto de la entrevista)
  - jobTitle: string
  - seniority: "junior" | "mid" | "senior" | "leadership"
  - culture?: string

Output (JSON):
  {
    "verdict": "PASS" | "CONDITIONAL" | "REJECT",
    "overall_score": 7.5,
    "dimension_scores": { ... },
    "evidence": [ ... ],
    "confidence": 0.92,
    "contradictions": [ ... ],
    "recommendations": [ ... ]
  }

Implementación:
- Llama a Claude API con prompt que incluya scoring-schema.json
- Procesa la respuesta
- Devuelve JSON estructurado
```

#### 2. **ListJobDescriptions** (src/tools/listJobDescriptions.ts)
```
Input: (ninguno, o opcional: culture filter)

Output (JSON):
  {
    "jobs": [
      {
        "id": "jd_1",
        "title": "Senior Backend Engineer",
        "level": "senior",
        "culture": "startup",
        "weights": { ... },
        "threshold": 7.0
      }
    ],
    "total": 5
  }

Implementación:
- Lee de hiresignal_data.json (si existe)
- O devuelve ejemplos hardcoded para demo
```

#### 3. **GetJobDetails** (src/tools/getJobDetails.ts)
```
Input:
  - jobId: string

Output (JSON):
  {
    "id": "jd_1",
    "title": "...",
    "description": "...",
    "weights": { ... },
    "threshold": 7.0,
    "culture_factors": [ ... ],
    "english_threshold": 7
  }

Implementación:
- Busca en data
- Devuelve detalles completos del JD
```

#### 4. **SubmitScore** (src/tools/submitScore.ts)
```
Input:
  - jobId: string
  - candidateName: string
  - score: number
  - verdict: "PASS" | "CONDITIONAL" | "REJECT"
  - evidence: object

Output (JSON):
  {
    "success": true,
    "interviewId": "int_12345",
    "message": "Score submitted successfully"
  }

Implementación:
- Guarda en hiresignal_data.json
- Devuelve confirmación
```

#### 5. **GetInterviewHistory** (src/tools/getInterviewHistory.ts)
```
Input:
  - jobId?: string (opcional, filter)
  - limit?: number (default 10)

Output (JSON):
  {
    "interviews": [
      {
        "id": "int_1",
        "jobId": "jd_1",
        "candidate": "John Doe",
        "verdict": "PASS",
        "score": 7.8,
        "date": "2026-05-12"
      }
    ],
    "total": 45
  }

Implementación:
- Lee historial de hiresignal_data.json
- Filtra por jobId si se proporciona
```

#### 6. **GetAnalytics** (src/tools/getAnalytics.ts)
```
Input: (ninguno, o opcional: jobId filter)

Output (JSON):
  {
    "total_interviews": 45,
    "pass_rate": 0.33,
    "reject_rate": 0.67,
    "average_score": 6.2,
    "by_dimension": {
      "technical_depth": 6.5,
      "authenticity": 5.8,
      ...
    }
  }

Implementación:
- Calcula estadísticas de hiresignal_data.json
- Devuelve KPIs por dimensión
```

---

### 📦 Archivos de Configuración (Incluir en `config/`)

**Copia estos 4 archivos en la carpeta `config/`:**

1. `scoring-schema.json` — [CONTENIDO DEL ARCHIVO ACTUAL]
2. `contradiction-rules.md` — [CONTENIDO DEL ARCHIVO ACTUAL]
3. `evidence-rubric.md` — [CONTENIDO DEL ARCHIVO ACTUAL]
4. `report-template.json` — [CONTENIDO DEL ARCHIVO ACTUAL]

Estos archivos definen cómo funciona el scoring.

---

### 📄 Archivos Base a Generar

#### `package.json`
```json
{
  "name": "leracom-mcp-server",
  "version": "1.0.0",
  "description": "MCP Server for HireSignal Interview Scoring",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "dev": "ts-node src/index.ts",
    "start": "node dist/index.js",
    "test": "jest"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.1.0",
    "axios": "^1.6.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "typescript": "^5.0.0",
    "ts-node": "^10.0.0",
    "jest": "^29.0.0"
  }
}
```

#### `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

#### `.env.example`
```
ANTHROPIC_API_KEY=sk_ant_...
HIRESIGNAL_API_URL=https://your-hiresignal-url
HIRESIGNAL_DATA_FILE=./data/hiresignal_data.json
NODE_ENV=development
```

---

### 📖 Documentación a Generar

#### `README.md`
- Qué es este servidor
- Quick start (3 pasos)
- Cómo correr localmente
- Cómo desplegar (Vercel, Railway, Heroku)
- Cómo configurar variables de entorno
- Cómo conectar desde Claude Code
- Troubleshooting

#### `IMPLEMENTACION.md`
- Detalles técnicos de cada herramienta
- Flujo de datos
- Cómo integra con HireSignal
- Ejemplos de requests/responses
- Cómo extender con más tools

#### `DEPLOYMENT_CHECKLIST.md`
- Lista de verificación pre-deployment
- Variables de entorno requeridas
- Testing checklist
- Monitoreo en producción

---

## 🎯 Resultado Final

Cuando termines, Leracom debe poder:

```bash
# 1. Instalar
npm install

# 2. Configurar (copiar .env.example a .env, llenar API key)
cp .env.example .env
# Editar .env con su ANTHROPIC_API_KEY

# 3. Correr localmente
npm run dev
# → Servidor MCP escuchando en puerto 3000

# 4. En Claude Code, configurar MCP server pointing a http://localhost:3000

# 5. Usar tools en cualquier skill:
# "Usa la herramienta ScoreInterview para analizar esta transcripción..."
# → Funciona automáticamente
```

---

## 📋 Checklist de Generación

- [ ] Carpeta `leracom-mcp-server/` creada
- [ ] `src/index.ts` implementado (servidor MCP)
- [ ] 6 tools en `src/tools/` (cada uno en su archivo .ts)
- [ ] `src/types/` con interfaces TypeScript
- [ ] `src/utils/` con funciones compartidas
- [ ] `config/` con los 4 archivos JSON/MD
- [ ] `package.json` + `tsconfig.json`
- [ ] `.env.example` generado
- [ ] `README.md` claro y completo
- [ ] `IMPLEMENTACION.md` con detalles técnicos
- [ ] `DEPLOYMENT_CHECKLIST.md`
- [ ] `tests/tools.test.ts` básico

---

## Notas Importantes

1. **TypeScript stricto** → Todas las interfaces bien tipadas
2. **Error handling** → Try-catch en cada tool
3. **Logging** → console.log de debug en dev mode
4. **Modular** → Cada tool en archivo separado
5. **Documentado** → Cada función tiene JSDoc
6. **Testeable** → Tests básicos para validar

---

## Inicio Automático

Cuando ejecutes este prompt:

1. Confirma que quieres crear el servidor
2. Te pregunta: ¿Nombre de la carpeta? (default: leracom-mcp-server)
3. Te pregunta: ¿Incluir tests? (default: sí)
4. Genera todo automáticamente
5. Al terminar, dice: "✅ MCP Server ready! npm install && npm run dev"

---

**COMIENZA AHORA** con la estructura y generación. Léeme la confirmación cuando termines.
