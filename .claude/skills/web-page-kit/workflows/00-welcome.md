# Workflow 00 — Welcome: Guided Onboarding

This is the entry point for every new session. Guides the user step by step from language selection through to deployment.

---

## Step 1 — Language / Idioma

Present this exact message (bilingual):

---

> **Welcome to Web Page Kit!** / **¡Bienvenido a Web Page Kit!**
>
> I'll help you build and publish a professional website, step by step.
> Te ayudo a crear y publicar un sitio web profesional, paso a paso.
>
> **Choose your language / Elige tu idioma:**
>
> 1. 🇺🇸 **English**
> 2. 🇨🇴 **Español**

---

Wait for selection. Store as `language: "en"` or `language: "es"` in config.

All subsequent output in this session uses the selected language.

---

## Step 2 — Website Type

**EN version:**

> **What kind of website do you want to build?**
>
> 1. 🎬 **Scroll Experience** — Cinematic, Apple-style. The page comes alive as you scroll. Premium visual impact.
> 2. 💼 **Business / Professional** — Services, about, contact. Clean and trustworthy.
> 3. 🎨 **Portfolio / Creative** — Showcase your work. For designers, photographers, developers, artists.
> 4. ✍️ **Blog / Editorial** — Articles, stories, guides. Content-first design.
> 5. 🛒 **E-commerce / Shop** — Products, pricing, buy flow.
> 6. 📅 **Events** — Conference, concert, workshop. Dates, speakers, register.
> 7. 🎙️ **Personal Brand / Creator** — Your story, your services, your community.
> 8. 📻 **Podcast** — Episode archive, host bio, subscribe links.

---

**ES version:**

> **¿Qué tipo de sitio web quieres crear?**
>
> 1. 🎬 **Scroll Experience** — Cinematográfico, estilo Apple. La página cobra vida mientras haces scroll. Impacto visual premium.
> 2. 💼 **Negocio / Profesional** — Servicios, quiénes somos, contacto. Limpio y confiable.
> 3. 🎨 **Portafolio / Creativo** — Muestra tu trabajo. Para diseñadores, fotógrafos, devs, artistas.
> 4. ✍️ **Blog / Editorial** — Artículos, historias, guías. Diseño centrado en contenido.
> 5. 🛒 **E-commerce / Tienda** — Productos, precios, flujo de compra.
> 6. 📅 **Eventos** — Conferencia, concierto, taller. Fechas, ponentes, registro.
> 7. 🎙️ **Marca Personal / Creator** — Tu historia, tus servicios, tu comunidad.
> 8. 📻 **Podcast** — Archivo de episodios, bio del host, links de suscripción.

---

Wait for selection. Map to `site_type`:

| Selection | site_type |
|---|---|
| 1 — Scroll Experience | `scroll` |
| 2 — Business | `business` |
| 3 — Portfolio | `portfolio` |
| 4 — Blog | `blog` |
| 5 — E-commerce | `ecommerce` |
| 6 — Events | `events` |
| 7 — Personal Brand | `personal` |
| 8 — Podcast | `podcast` |

---

## Step 3 — Start Method

**Before presenting options:** Check if the user has existing HTML files in `kit-instagram-web/` (e.g., `web-yoguinna.html`, `web-sants1988.html`). If they exist, offer them as a starting template — it's faster than building from scratch and the architecture is already proven.

**EN:**
> **How do you want to start?**
>
> 1. 🆕 **Create from scratch** — I'll ask you a few questions and we build it together.
> 2. 🔗 **Import an existing site** — Paste a URL. I'll analyze the design and adapt it to your brand.
> 3. ♻️ **Use existing template** — Adapt one of your previously generated HTML files (faster, proven design).

**ES:**
> **¿Cómo quieres comenzar?**
>
> 1. 🆕 **Crear desde cero** — Te hago unas preguntas y lo construimos juntos.
> 2. 🔗 **Importar un sitio existente** — Pega una URL. Analizo el diseño y lo adapto a tu marca.
> 3. ♻️ **Usar template existente** — Adapto uno de tus HTMLs ya generados (más rápido, diseño probado).

---

Map selection:
- Option 1 → continue to Step 4A (setup from scratch)
- Option 2 → continue to Step 4B (import flow)

---

## Step 4A — Setup from Scratch

**ACTION:** Pre-fill context in session memory:
- `site_type`: [from Step 2]
- `language`: [from Step 1]

Then launch `workflows/00-setup.md` with this context.

Before launching, show the progress map:

**EN:**
```
📋 Your production flow:

  ✅ Step 1 — Welcome (you're here)
  ⬜ Step 2 — Setup: Brand & identity
  ⬜ Step 3 — Homepage
  ⬜ Step 4 — Content pages (optional)
  ⬜ Step 5 — SEO optimization
  ⬜ Step 6 — Publish → Live in minutes

Let's start with Step 2. I'll ask you a few questions about your site.
```

**ES:**
```
📋 Tu flujo de producción:

  ✅ Step 1 — Bienvenida (estás aquí)
  ⬜ Step 2 — Configuración: Marca e identidad
  ⬜ Step 3 — Página de inicio
  ⬜ Step 4 — Páginas de contenido (opcional)
  ⬜ Step 5 — Optimización SEO
  ⬜ Step 6 — Publicar → En línea en minutos

Empecemos con el Step 2. Te haré unas preguntas sobre tu sitio.
```

---

## Step 4B — Import Existing Site

**ACTION:** Pre-fill context:
- `site_type`: [from Step 2]
- `language`: [from Step 1]

Show progress map (same as 4A but with "Import" in Step 2).

Then launch `workflows/00-import.md` with this context.

---

## After Setup Completes

When `00-setup.md` or `00-import.md` finishes, return here and show the updated flow:

**EN:**
```
✅ Setup complete!

📋 Production flow:
  ✅ Step 1 — Welcome
  ✅ Step 2 — Setup done
  ⬜ Step 3 — Homepage  ← next
  ⬜ Step 4 — Content pages
  ⬜ Step 5 — SEO
  ⬜ Step 6 — Publish

Ready to build your homepage? Just say "homepage" or "next step".
```

**ES:**
```
✅ ¡Configuración lista!

📋 Flujo de producción:
  ✅ Step 1 — Bienvenida
  ✅ Step 2 — Configuración lista
  ⬜ Step 3 — Página de inicio  ← siguiente
  ⬜ Step 4 — Páginas de contenido
  ⬜ Step 5 — SEO
  ⬜ Step 6 — Publicar

¿Listo para crear tu página de inicio? Solo di "homepage" o "siguiente paso".
```

Continue step by step, marking each as ✅ when complete, until Step 6 (Publish).

---

## Mid-Session: Returning Users

If `website-config.json` already exists when the skill is invoked, skip Steps 1-3 and show:

**EN:**
> "Welcome back! Your [site_type] site config is ready.
> Where do you want to continue?
> — Homepage / Content page / SEO / Publish"

**ES:**
> "¡Bienvenido de nuevo! Tu configuración para [site_type] está lista.
> ¿Dónde quieres continuar?
> — Página de inicio / Contenido / SEO / Publicar"

---

**Welcome complete.** The user knows exactly where they are and what comes next at every step.
