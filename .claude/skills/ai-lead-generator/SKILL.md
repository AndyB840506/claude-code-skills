---
name: ai-lead-generator
description: "Genera leads de negocio reales con IA buscando en Google y redes sociales. Busca empresas que necesitan lo que vendes, las puntúa 0-100, categoriza por probabilidad de conversión (PREMIUM/HOT/WARM/COLD), genera reporte HTML descargable como PDF y CSV para CRM. Triggers: 'buscar leads', 'generar leads', 'encontrar clientes', 'lead generation', 'prospección', 'find leads', 'find prospects', 'generate leads', 'cambiar modo de búsqueda', 'cambiar a Serper'."
---

# AI Lead Generator

Busca leads reales en Google y redes sociales, los puntúa del 0 al 100, los categoriza por probabilidad de conversión, y genera un reporte HTML descargable como PDF.

**Regla fundamental: nunca inventes leads. Cada lead debe provenir de una búsqueda real.**

---

## Paso 0 — Verificar configuración de búsqueda

### 0.1 Leer archivo de configuración

Busca `lead-generator.config.json` en la carpeta raíz. Si no existe, créalo:

```json
{
  "search_mode": "native",
  "serper_api_key": "",
  "hunter_api_key": "",
  "hunter_enrichment": false
}
```

| Modo | Valor | Descripción |
|------|-------|-------------|
| Nativo Claude | `"native"` | WebSearch integrado. Gratis. |
| Serper.dev | `"serper"` | Google API. Más rápido. |
| Híbrido | `"hybrid"` | Serper + Hunter.io para emails. |

### 0.2 Validar el modo activo

- Si `search_mode` es `"serper"` pero la key está vacía → cambia a `"native"`
- Si `search_mode` es `"hybrid"` pero falta Hunter key → usa solo Serper

---

## Paso 1 — Entender qué necesita el usuario

### 1.1 Tono de comunicación

Habla como si explicaras a alguien que nunca ha hecho esto. Sin tecnicismos. Con paciencia.

### 1.2 Si el usuario ya describió lo que busca

Extrae datos directamente y confirma en un solo mensaje.

### 1.3 Si el usuario NO sabe qué quiere

Entra en modo sondeo:

> ¡Hola! 👋 Voy a ayudarte a encontrar clientes potenciales.
>
> Necesito entender dos cosas:
>
> **1. ¿Qué vendes?** (en una frase)
> - Ejemplos: "Hago páginas web", "Vendo seguros", "Ofrezo servicio de limpieza para oficinas"
>
> **2. ¿A qué tipo de empresa le quieres vender?**
> - Ejemplos: "Restaurantes", "Clínicas", "Empresas de transporte"

---

## Paso 2 — Ejecutar búsquedas

Construye 10-14 queries:

**Tipo A — Encontrar empresas (6-8 queries):**
- `"[nicho]" "[país]" site:linkedin.com/company`
- `"[nicho]" "[país]" contacto OR email`
- `"[nicho]" "[país]" presupuesto OR cotizar`

**Tipo B — Encontrar contacto directo (4-6 queries):**
- `"[empresa]" "gerente general" site:linkedin.com/in`
- `"[empresa]" "CEO" OR "dueño" linkedin`

### Modo NATIVE — WebSearch
Usa WebSearch para cada query. Extrae nombre, URL, snippets.

---

## Paso 3 — Scoring y categorización

Score de **0 a 100**:

| Criterio | Puntos |
|----------|--------|
| Website activo | 10 |
| LinkedIn activo < 60 días | 10 |
| Email encontrado | 10 |
| Redes sociales < 30 días | 10 |
| Decision-maker identificado | 15 |
| LinkedIn del decision-maker | 15 |
| Celular/WhatsApp directo | 10 |
| Buy signal detectado | 10 |

**Categorías:**
- `PREMIUM` (76–100): Sabes quién decide + celular/LinkedIn + señal de interés
- `HOT` (51–75): Señales de necesidad + contacto localizable
- `WARM` (26–50): Presencia activa, sin señal directa
- `COLD` (0–25): Existe pero falta información de contacto

---

## Paso 4 — Generar el reporte HTML

Crea `leads/leads-[nicho]-[fecha].html`.

**Estructura:**
1. Encabezado — Título, región, fecha, conteo por categoría
2. Dashboard de filtros — Búsqueda, filtros, botón PDF
3. Tabla resumen ejecutivo
4. Tarjetas de leads (mayor a menor score)

Cada tarjeta tiene:
- **La empresa:** Nombre, badge categoría, score, website, LinkedIn, email, ubicación
- **Contacto directo:** Nombre decisor, cargo, celular/WhatsApp, LinkedIn personal
- **Señales de compra:** Si existen

---

## Paso 5 — Generar CSV para CRM

Crea `leads/leads-[nicho]-[fecha].csv`:

```
Empresa,Score,Categoría,Website,LinkedIn Empresa,Email,Ubicación,Decisor Nombre,Decisor Cargo,Decisor LinkedIn,Celular/WhatsApp,Buy Signals
```

---

## Paso 6 — Guardar y presentar

1. Crea carpeta `leads/` si no existe
2. Guarda archivos
3. Abre HTML en navegador
4. Muestra resumen

```
✅ ¡Listo! Modo: [NATIVE/SERPER/HYBRID]

📊 [n] leads encontrados
   🥇 PREMIUM: [n]
   🔥 HOT: [n]
   🌡️ WARM: [n]
   ❄️ COLD: [n]

📁 Guardado en:
   → leads/leads-[nicho]-[fecha].html
   → leads/leads-[nicho]-[fecha].csv
```

---

## Core Rules

- Nunca inventes leads — cada uno proviene de una búsqueda real
- Si no encuentras suficientes, lo dices claramente
- Buy signals específicos según lo que el usuario ofrece
- CSV listo para CRM incluido
