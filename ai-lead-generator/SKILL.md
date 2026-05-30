---
name: ai-lead-generator
description: "Generate and find business leads with AI / Genera leads de negocio con IA. Spanish triggers: buscar leads, generar leads, encontrar clientes potenciales, prospección de clientes, lead generation, buscar prospectos, encontrar empresas para vender, base de datos de clientes, buscar contactos de negocios, quiero encontrar clientes, dame leads de, busca empresas que necesiten, prospección comercial, pipeline de ventas, encontrar potenciales clientes. English triggers: find leads, generate leads, find prospects, find potential clients, generate leads list, lead generation, build lead list, create leads, find customers, prospect search, find businesses. Configuration: cambiar modo de búsqueda, change search mode, configurar API, configure API, cambiar a Serper, cambiar a nativo, configurar Hunter."
---

# AI Lead Generator

Busca leads reales en Google y redes sociales, los puntúa del 0 al 100, los categoriza por probabilidad de conversión, y genera un reporte HTML descargable como PDF — todo en el idioma del usuario.

**Regla fundamental: nunca inventes leads. Cada lead debe provenir de una búsqueda real. Si no encuentras información suficiente para un campo, déjalo vacío — jamás lo rellenes con datos inventados.**

---

## Antes de empezar — Detectar idioma

Antes de escribir cualquier respuesta, analiza el idioma en que el usuario escribió su primer mensaje y úsalo para TODO: preguntas, respuestas, el reporte HTML, el CSV, los mensajes de progreso y el resumen final.

- Si escribe en español → todo en español
- Si escribe en inglés → everything in English
- Si escribe en portugués → tudo em português
- Si escribe en otro idioma → responde en ese idioma

No preguntes el idioma. Simplemente detéctalo y úsalo. Si no estás seguro, usa el idioma de la mayoría de las palabras.

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
| Nativo Claude | `"native"` | WebSearch integrado. Gratis. Para empezar. |
| Serper.dev | `"serper"` | Google API. Más rápido. $50/mes → 50.000 búsquedas. |
| Híbrido | `"hybrid"` | Serper + Hunter.io para emails verificados. ~$99/mes. |

### 0.2 Validar el modo activo

- Si `search_mode` es `"serper"` o `"hybrid"` pero la key está vacía → cambia a `"native"` para esta sesión e informa al usuario.
- Si `search_mode` es `"hybrid"` pero falta la key de Hunter → usa solo Serper, omite el enriquecimiento de emails.

### 0.3 Cambiar de modo

Si el usuario pide cambiar el modo (frases como "change search mode", "cambiar a Serper", "configurar API"), muestra este menú:

```
¿Qué modo quieres activar?

  [1] native  — WebSearch de Claude (gratis, sin configuración)
  [2] serper  — Serper.dev API ($50/mes → 50.000 búsquedas)
  [3] hybrid  — Serper + Hunter.io (~$99/mes, emails verificados)
```

Guarda la selección en `lead-generator.config.json` y confirma con:
> ✅ Listo. Modo [X] activado y guardado. Mantén `lead-generator.config.json` fuera de repositorios públicos — contiene tus API keys.

---

## Paso 1 — Bienvenida y entender qué necesita el usuario

### 1.1 Tono y estilo de comunicación

Habla siempre como si le explicaras algo a alguien que nunca ha hecho esto antes. Sin tecnicismos. Con paciencia. Con entusiasmo. Usa frases cortas. Usa analogías simples.

Ejemplos de cómo hablar:
- ❌ "Vamos a hacer prospección B2B en verticales específicas"
- ✅ "Vamos a buscar empresas a las que puedas ofrecerle lo que vendes 🎯"

- ❌ "El sistema ejecutará queries semánticas para identificar decision-makers"
- ✅ "Voy a buscar quién es el jefe o dueño de cada empresa para que puedas contactarlo directamente"

### 1.2 Detectar si el usuario sabe qué quiere

**Si el usuario ya describió lo que busca** (ej: "quiero leads de restaurantes en Colombia que necesiten delivery") → extrae los datos directamente y pasa a confirmar en un solo mensaje.

**Si el usuario NO tiene claro qué quiere** (ej: "quiero leads", "I need leads", "quiero clientes", o cualquier mensaje vago) → entra en modo sondeo:

Muestra este mensaje (en el idioma del usuario):

---
*Ejemplo en español:*

> ¡Hola! 👋 Voy a ayudarte a encontrar clientes potenciales para tu negocio.
>
> Esto funciona así: yo busco en Google, LinkedIn e Instagram empresas que probablemente necesitan lo que tú vendes — y te doy una lista con su contacto y una nota de qué tan fácil es venderles.
>
> Para empezar necesito entender dos cosas súper simples:
>
> **1. ¿Qué vendes?** (en una frase, como si se lo dijeras a un amigo)
>
> Por ejemplo:
> - "Vendo seguros para carros"
> - "Hago páginas web para negocios"
> - "Ofrezco servicio de limpieza para oficinas"
> - "Vendo software de nómina para empresas"
> - "Doy clases de inglés para adultos"
>
> **2. ¿A qué tipo de empresa le quieres vender?**
>
> Por ejemplo:
> - "A restaurantes"
> - "A clínicas o consultorios médicos"
> - "A empresas de transporte"
> - "A cualquier empresa que tenga más de 10 empleados"
> - "No sé, ayúdame a decidir"
>
> ¿Qué me cuentas? 😊

---

Si el usuario responde "no sé" o "ayúdame a decidir" al tipo de empresa → pregúntale quién es su cliente ideal con estas preguntas simples:

> Cuéntame un poco más:
> - ¿Tu producto/servicio es para empresas grandes, medianas o pequeñas?
> - ¿Lo que vendes requiere que la empresa tenga vehículos, empleados, computadores, un local físico...?
> - ¿Has vendido antes? ¿A quién le fue más fácil venderle?

Con esas respuestas, sugiérele 3 nichos concretos y pregunta cuál prefiere.

### 1.3 Confirmar parámetros antes de buscar

Una vez que tienes el nicho y el producto/servicio, confirma todo en un solo mensaje antes de buscar:

> Perfecto, ya tengo todo lo que necesito 🎉
>
> Voy a buscar: **[tipo de empresa]** en **[país/región]**
> Para ofrecerles: **[lo que vende el usuario]**
> Cantidad: **[n] leads**
> Idioma de los leads: **[idioma]**
>
> ¿Todo correcto? ¿O quieres cambiar algo?

Si el usuario no especificó país, región o cantidad → asume Colombia, leads en español, 20 leads, y menciónalo en la confirmación para que pueda corregir.

---

## Paso 2 — Ejecutar búsquedas

Informa al usuario con entusiasmo (en su idioma):

> 🔍 ¡Arrancamos! Voy a revisar Google, LinkedIn e Instagram buscando empresas que puedan necesitar lo que vendes. Esto tarda unos 2-3 minutos...

### Número de queries según modo de búsqueda

| Modo | Queries | Explicación |
|------|---------|-------------|
| **NATIVE (WebSearch)** | 6-8 máximo | Max 10 WebSearch calls total. Usa solo los queries de mayor rendimiento |
| **SERPER** | 10-14 | Sin límite de API. Usa todos los queries para cobertura máxima |
| **HYBRID** | 8-10 | Combina Serper + Hunter. Completa búsquedas pero evita Hunter overload |

Para el sistema de tiers de queries (TIER 1/2/3), rate limits por modo y ejemplos de ejecución completos, ver **[docs/search-modes.md](docs/search-modes.md)**.

### Extracción de datos por lead

Por cada empresa encontrada, captura:

| Campo | Qué extraer | Prioridad |
|-------|-------------|-----------|
| `nombre_empresa` | Nombre oficial | Alta |
| `website` | URL principal | Alta |
| `linkedin_empresa` | URL perfil empresa `/company/` | Alta |
| `industria` | Sector o subsector | Alta |
| `ubicacion` | Ciudad, país | Alta |
| `tamaño_estimado` | Número de empleados | Media |
| `email_empresa` | Email general o de contacto | Alta |
| `telefono_fijo` | Teléfono de oficina | Media |
| `decision_maker_nombre` | Nombre completo del gerente/dueño/CEO | **Crítico** |
| `decision_maker_cargo` | CEO, Gerente General, Dueño, Director, Fundador | **Crítico** |
| `decision_maker_linkedin` | URL perfil personal `/in/[nombre]` | **Crítico** |
| `celular_directo` | Número celular/móvil (NO fijo) — preferir WhatsApp | **Crítico** |
| `whatsapp` | Número WhatsApp si está publicado | **Crítico** |
| `ultima_actividad` | Fecha último post o publicación | Media |
| `redes_sociales` | Twitter, Instagram, Facebook de la empresa | Baja |
| `buy_signals` | Frases o señales de necesidad detectadas | Alta |
| `fuente` | Dónde fue encontrado | Media |
| `notas` | Datos adicionales | Baja |

**Reglas para el contacto directo:**
- Si encuentras un celular Y un teléfono fijo → muestra SOLO el celular
- Si encuentras WhatsApp → marcarlo claramente como preferido
- Si encuentras el LinkedIn personal del decision-maker → es el campo más valioso para contacto directo por DM
- Cargos que cuentan como decision-maker: CEO, Gerente General, Gerente Comercial, Director General, Dueño, Propietario, Fundador, Co-Fundador, Presidente, Owner, Founder

**Si encuentras múltiples contactos (> 2), aplicar ranking:**

Rank contacts por este orden de prioridad (usa solo los top 2 en el reporte):

| Prioridad | Criterio | Ejemplo |
|-----------|----------|---------|
| 1️⃣ Máxima | CEO o Dueño + celular/WhatsApp + LinkedIn activo < 30 días | CEO Juan García, CEO - LinkedIn, +57 321 4567890 |
| 2️⃣ Alta | CEO o Gerente General + LinkedIn activo (sin celular) | CEO María López - LinkedIn solo |
| 3️⃣ Media | Gerente Comercial + celular/WhatsApp | Sales Director con teléfono |
| 4️⃣ Baja | Fundador sin contacto directo o contacto genérico | Founder name sin celular |

**Ejemplo:** Si encuentras 5 contactos:
- CEO con WhatsApp → **Opción 1 (Rank 1️⃣)**
- Gerente Comercial con celular → **Opción 2 (Rank 3️⃣)**
- Otros 3 contactos → descarta en el reporte, menciona en notas "5 contactos encontrados, mostrando los 2 de mayor relevancia"

Deduplica: misma empresa en múltiples resultados → un solo registro consolidado.

---

## Paso 3 — Scoring y categorización

Score de **0 a 100** (más bonus):

| Criterio | Puntos | Cómo evaluarlo |
|----------|--------|----------------|
| Website activo y funcional | 10 | URL accesible |
| LinkedIn empresa con actividad < 60 días | 10 | Perfil con posts recientes |
| Email o contacto general encontrado | 10 | Email público o formulario activo |
| Actividad en redes sociales < 30 días | 10 | Último post reciente |
| Tamaño > 10 empleados | 10 | Mencionado en LinkedIn, web o directorio |
| **Decision-maker identificado (nombre + cargo)** | **15** | Nombre real de quien decide |
| **LinkedIn personal del decision-maker encontrado** | **15** | URL `/in/` verificado |
| **Celular o WhatsApp directo encontrado** | **10** | Número móvil, no fijo |
| Buy signal detectado | 10 | Señal real de necesidad activa |
| *(Bonus) Email verificado por Hunter.io* | +10 | Solo modo HYBRID |

**Categorías:**

| Categoría | Score | Lo que significa en palabras simples |
|-----------|-------|--------------------------------------|
| `COLD` | 0–25 | La empresa existe pero no sabes a quién llamar ni si te necesita |
| `WARM` | 26–50 | Puedes contactarlos, pero no sabes si están interesados |
| `HOT` | 51–75 | Hay señales de que pueden necesitar lo que vendes, y sabes cómo contactarlos |
| `PREMIUM` | 76–100 | Sabes quién decide, tienes su celular o LinkedIn, y hay señal de interés |

---

## Paso 4 — Generar el reporte HTML

Crea `leads/leads-[nicho]-[fecha].html` en el idioma del usuario. Diseño moderno, profesional y **100% PDF-safe**.

### Reglas PDF-safe (OBLIGATORIAS):

```css
* {
  -webkit-print-color-adjust: exact !important;
  print-color-adjust: exact !important;
  color-adjust: exact !important;
}
@media print {
  .lead-card { 
    page-break-inside: avoid; 
    break-inside: avoid;
    box-shadow: none !important;
    border: 1px solid #333 !important;  /* Darker border for print visibility */
    background-color: #FFF !important; /* Ensure solid background */
  }
  .no-print { display: none !important; }
  @page { margin: 20mm; }
}
```

- **NO gradientes** en fondos importantes → colores sólidos.
- **NO `opacity` ni `rgba` con transparencia** en elementos clave.
- Contraste AAA en todos los textos sobre color.

### Paleta:

Elige colores que comuniquen visualmente la temperatura del lead:
- **COLD** — tono neutro/gris (señal: sin información aún)
- **WARM** — tono azul o suave (señal: hay potencial)
- **HOT** — tono naranja/rojo moderado (señal de necesidad activa)
- **PREMIUM** — tono destacado/dorado (señal: máxima prioridad)

Diseño libre — elige una paleta que contraste bien y respete contraste AAA.
No uses gradientes ni transparencias (requerimiento PDF, no estético).

### Estructura del HTML:

**1. Encabezado** — Título, región, fecha, modo, badges de conteo por categoría.

**2. Dashboard de filtros (`class="no-print"`):**
- Buscador por nombre
- Filtros: Todos / PREMIUM / HOT / WARM / COLD
- Botón "Descargar PDF" → `window.print()`

**3. Tabla resumen ejecutivo (visible en PDF):**
Rank | Empresa | Score | Categoría | Decisor | Contacto directo | Ubicación

**4. Tarjetas de leads (mayor a menor score).**

Cada tarjeta tiene DOS secciones claramente separadas:

**Sección A — La empresa:**
- Nombre + badge categoría + score + barra de progreso
- 🌐 Website · 💼 LinkedIn empresa · 📧 Email · 📍 Ubicación · 👥 Tamaño · 🏢 Industria · 📅 Última actividad

**Sección B — A quién contactar (destacada visualmente con fondo diferente):**
- 👤 Nombre del decisor + cargo
- 📱 Celular / WhatsApp (si se encontró) — en verde si es WhatsApp
- 🔗 LinkedIn personal (botón azul con texto "Ver perfil · Enviar DM")
- Si no se encontró el decisor → mostrar mensaje amigable: "No encontramos el contacto directo — te recomendamos buscar en LinkedIn: [link búsqueda]"

**Sección C — Señales de compra** (si existen):
- Lista de buy signals en color ámbar llamativo

**5. Metodología** (al final, visible en PDF) — fecha, fuentes, scoring, disclaimer.

### JavaScript para filtros y PDF:

```javascript
function filterLeads(category) {
  document.querySelectorAll('.lead-card').forEach(card => {
    card.style.display = (category === 'ALL' || card.dataset.category === category) ? '' : 'none';
  });
  document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelector('[data-filter="' + category + '"]').classList.add('active');
}
function searchLeads(query) {
  document.querySelectorAll('.lead-card').forEach(card => {
    const name = card.querySelector('.company-name').textContent.toLowerCase();
    card.style.display = name.includes(query.toLowerCase()) ? '' : 'none';
  });
}
function downloadPDF() { window.print(); }
```

---

## Paso 5 — Generar CSV para CRM

Crea `leads/leads-[nicho]-[fecha].csv`:

```
Empresa,Score,Categoría,Website,LinkedIn Empresa,Email,Email Verificado,Ubicación,Industria,Tamaño,Decisor Nombre,Decisor Cargo,Decisor LinkedIn,Celular/WhatsApp,Buy Signals,Fuente,Última Actividad,Notas
```

- Escapar comas dentro de campos con comillas dobles
- Todos los leads incluidos, incluso COLD
- Ordenar de mayor a menor score
- "Email Verificado" = `Sí` solo si vino de Hunter.io

---

## Paso 6 — Guardar, abrir y presentar resultados

1. Crea la carpeta `leads/` si no existe:
```bash
mkdir -p leads
```

2. Guarda ambos archivos en `leads/`.

3. Abre el HTML automáticamente en el navegador:
```bash
start leads/leads-[nicho]-[fecha].html
```
*(En Mac usar `open`, en Linux usar `xdg-open`)*

4. Muestra el resumen en el idioma del usuario:

```
✅ ¡Listo! Tu reporte está listo · Modo: [NATIVE/SERPER/HYBRID]

📊 [n] leads encontrados
   🥇 PREMIUM: [n]  ← tienen decisor + celular/LinkedIn + señal de compra
   🔥 HOT:     [n]  ← señales de interés + contacto localizable
   🌡️ WARM:    [n]  ← presencia activa, sin señal directa aún
   ❄️ COLD:    [n]  ← existen pero falta información de contacto

📞 Decisores encontrados con contacto directo: [n] de [total]
   → [n] con celular/WhatsApp
   → [n] con LinkedIn personal para DM

📁 Guardado en:
   → leads/leads-[nicho]-[fecha].html  (se abrió en tu navegador)
   → leads/leads-[nicho]-[fecha].csv   (para importar a tu CRM)

💡 Los 3 más fáciles de contactar HOY:
   1. [Empresa] — [Decisor], [Cargo] — [Celular o LinkedIn]
   2. [Empresa] — [Decisor], [Cargo] — [Celular o LinkedIn]
   3. [Empresa] — [Decisor], [Cargo] — [Celular o LinkedIn]

⚙️  Para cambiar el modo de búsqueda escribe: "cambiar modo"
```

5. Cierra con una pregunta simple y amigable:
> "¿Quieres que busque más leads, filtre por ciudad, o te ayude a preparar un mensaje para contactar a alguno de ellos? 😊"

---

## Fallbacks y manejo de errores

- **Si Serper falla** (401, 429, timeout) → avisa, cambia a `native` solo para esta sesión, continúa sin interrumpir.
- **Si Hunter no encuentra emails** → omite silenciosamente, sin restar puntos.
- **Si no se encuentra el decisor de ninguna empresa** → en el resumen final avisa: "No encontré contactos directos en esta búsqueda. Para conseguirlos, te recomiendo buscar manualmente en LinkedIn los perfiles de gerentes de estas empresas."
- **Si una búsqueda no da resultados** → reformula con sinónimos y reintenta una vez antes de descartarla.
- **Si hay menos leads que los pedidos** → genera el reporte con los que encontraste y explica con palabras simples por qué puede haber menos.
- **Si el usuario escribe algo confuso** → no adivines. Pregunta de forma amigable: "¡No te preocupes! Solo cuéntame: ¿qué vendes y a qué tipo de empresa le quieres vender? Con eso ya puedo empezar 😊"
- **Si la API key tiene formato inválido** → avisa antes de intentar la llamada y ofrece corregirla paso a paso.
