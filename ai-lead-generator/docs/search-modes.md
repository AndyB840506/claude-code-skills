# Modos de Búsqueda — Referencia Completa

Detalle de tiers de queries, rate limits y ejemplos de ejecución por modo.
Carga este archivo cuando necesites los detalles de ejecución de búsquedas.

---

## Queries ordenados por prioridad (ejecutar en este orden)

**TIER 1 — Máximo rendimiento (ejecutar siempre, 3-4 queries):**
1. `"[nicho]" "[país]" site:linkedin.com/company` — Empresas directas en LinkedIn
2. `"[nicho]" "[país]" directorio OR listado filetype:pdf` — Listados empresariales
3. `"[nicho]" "[país]" "presupuesto" OR "cotizar" OR "solicitar"` — Buy signals

**TIER 2 — Alto rendimiento (ejecutar si budget permite, 2-3 queries):**
4. `"[nicho]" "[país]" contacto OR email OR "escríbenos"` — Información de contacto
5. `"[nicho]" "[país]" CEO OR "gerente general" linkedin` — Decision-makers

**TIER 3 — Complementarias (si modo = SERPER/HYBRID, 2-3 queries):**
6. `"[nicho]" "[país]" instagram OR facebook` — Redes sociales activas
7. `"[nombre empresa encontrado]" "gerente" OR "director" celular` — Contacto específico
8. `"[nicho]" "[país]" "[problema que resuelve tu producto]"` — Pain-point signals

**Si NATIVE mode y presupuesto de 10 WebSearches limitado:**
- Ejecuta TIER 1 (siempre): 3-4 queries = ~6 WebSearches
- Ejecuta TIER 2 (con 4 WebSearches restantes): 2-3 queries
- Descarta TIER 3 o reformula con máxima precisión

**Si query no da resultados después de reformulación (1 retry):** Salta a siguiente sin penalizar.

---

## Modo NATIVE — WebSearch de Claude

**Rate limits & fallback strategy:**
- Maximum 10 WebSearch calls per lead generation session
- If query returns no results: reformulate with synonyms (1 retry only)
- If timeout occurs: skip that query and continue with next one
- If 10 limit reached before completing all queries: generate report with partial results and note in summary

Usa WebSearch para cada query. Extrae nombre, URL, snippets, señales.

**CRITICAL:** Ejecuta queries en el orden de prioridad (TIER 1 → TIER 2 → TIER 3).

Ejemplo de ejecución NATIVE:
```
Budget: 10 WebSearches
1. Execute TIER 1 query 1 (LinkedIn companies)     ← 2-3 WebSearches
2. Execute TIER 1 query 2 (PDF directories)        ← 2-3 WebSearches
3. Execute TIER 1 query 3 (Buy signals)            ← 1-2 WebSearches
[Total: 5-8 WebSearches used]
4. Execute TIER 2 query 1 (Contact info)           ← 2-3 WebSearches
[Total: 7-11, approaching limit]
5. Skip remaining TIER 2/3 or reformulate into 1 high-precision query
→ Generate report with TIER 1 + partial TIER 2 results
```

---

## Modo SERPER — Serper.dev API

```bash
curl -s -X POST "https://google.serper.dev/search" \
  -H "X-API-KEY: [serper_api_key]" \
  -H "Content-Type: application/json" \
  -d '{"q": "[query]", "num": 10, "hl": "[idioma]", "gl": "[país_code]"}'
```

---

## Modo HYBRID — Serper + Hunter.io

Primero todas las búsquedas con Serper, luego para cada dominio encontrado:

```bash
curl -s "https://api.hunter.io/v2/domain-search?domain=[dominio]&limit=5&api_key=[hunter_api_key]"
```

De Hunter extrae: email, nombre, apellido, cargo del contacto. Si hay emails, suma +10 al score.
