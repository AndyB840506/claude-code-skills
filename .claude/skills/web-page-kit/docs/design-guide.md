# Design Guide — Art Direction First, then Patterns

These rules are a **TOOLKIT, not a checklist.** Art direction (Rule 0) decides which patterns apply. Most pages should use only a few of the mechanical patterns below — **stacking all of them is exactly what produces generic, interchangeable "AI-looking" pages.**

---

## Rule 0 — Art direction is mandatory and comes FIRST (non-negotiable)

Before writing any HTML, commit to a distinctive design concept. A page that skips this and just stacks the defaults (centered hero + 3 feature cards + alternating backgrounds + count-up stats + parallax + rotating gradient ring) will look like every other AI site — that is a **FAIL**, not a deliverable.

### Process (every page, no exceptions)
1. **Get ONE real reference first.** Ask the user for one Awwwards / Dribbble / site they admire. One concrete reference beats three rounds of guessing. If they have none, pick a clear tone (Rule 8) and state it out loud before coding.
2. **Commit to a concept:** tone (Rule 8) + a layout *architecture* + one signature idea. Write it down first.
3. **Design the layout to serve the concept** — do not reach for the default skeleton. Hero shape, section order, and grids must follow the concept.
4. **Run the anti-generic checklist below before declaring it done.**

### Banned by default — use ONLY if the chosen concept genuinely calls for it
- ❌ Centered hero with a big gradient + two buttons
- ❌ A row of 3 identical feature cards
- ❌ Auto-rotating carousel / slider
- ❌ Rotating conic/hue gradient ring around a photo (Rule 9)
- ❌ Alternating white / light-grey / white section backgrounds
- ❌ Inter / Roboto / Arial / Helvetica / Space Grotesk as the display font
- ❌ Parallax hero + count-up stats applied by reflex on every page
- ❌ A row of oversized "big-number" stats (e.g. 7 / 3 / 9 / <24h) — a recognizable AI tell; prefer a quiet inline caption
- ❌ Em-dashes (—) sprinkled through the copy as the default connector — overuse is an AI tell; prefer periods, commas, or colons (keep — only for genuine number ranges)
- ❌ Emoji used as icons (use line SVGs)

### Anti-generic checklist — must pass before delivery
- [ ] Committed to a named concept + anchored to one real reference?
- [ ] Layout is asymmetric / editorial / unexpected — NOT centered-hero-then-uniform-card-grid?
- [ ] Display type is oversized and distinctive (clamp up to 5–11rem), not 2–3rem Inter?
- [ ] One signature moment a stock template wouldn't have?
- [ ] Avoided every banned item above (or can justify each one I kept)?
- [ ] Motion is intentional and concept-driven — not fade-up on everything?

If you can't tick these, it isn't done. Everything below (Rules 1–17) is how to execute the concept — not a sequence to apply wholesale.

---

## Rule 1: Self-Contained HTML

Every generated file must be a **single, self-contained HTML file**:

✅ **Allowed:**
- All CSS inside `<style>` tag in `<head>`
- All JS inside `<script>` tag before `</body>`
- Google Fonts via CDN (`<link rel="preconnect">` + stylesheet)
- Inline SVGs
- Base64-encoded small images (under 10KB)

❌ **Not allowed:**
- External `.css` files
- External `.js` files (no jQuery, no Bootstrap CDN)
- `<link rel="stylesheet" href="styles.css">` pointing to a local file
- Framework dependencies (React, Vue, Angular)

**Why:** A self-contained file works offline, deploys with one drag-and-drop, and never breaks due to missing dependencies.

> **Premium-tier exception:** when the brief is explicitly *ultra-premium / agency-grade*, external CDN libs (GSAP/ScrollTrigger/Lenis) are allowed — see **Rule 18**. Standard pages stay self-contained.

---

## Rule 2: Scroll Reveal Animations

Use the **Intersection Observer API** — no libraries, pure vanilla JS.

### Basic Fade-In + Slide-Up Pattern:

```css
/* CSS */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

```javascript
// JS
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

Apply `.reveal` class to: section headings, cards, feature items, images.

---

## Rule 3: Stagger Animation (Grids & Lists)

For cards and lists entering in sequence:

```css
.stagger-item {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.4s ease, transform 0.4s ease;
}

.stagger-item.visible { opacity: 1; transform: translateY(0); }
.stagger-item:nth-child(1).visible { transition-delay: 0s; }
.stagger-item:nth-child(2).visible { transition-delay: 0.1s; }
.stagger-item:nth-child(3).visible { transition-delay: 0.2s; }
.stagger-item:nth-child(4).visible { transition-delay: 0.3s; }
.stagger-item:nth-child(5).visible { transition-delay: 0.4s; }
.stagger-item:nth-child(6).visible { transition-delay: 0.5s; }
```

Apply to: service cards, portfolio grid, team members, feature list.

---

## Rule 4: Counter Animation

For metrics and stats — count from 0 to the real number when the section scrolls into view:

```javascript
function animateCounter(el) {
  const target = parseInt(el.getAttribute('data-target'));
  const duration = 1500;
  const step = target / (duration / 16);
  let current = 0;

  const timer = setInterval(() => {
    current += step;
    if (current >= target) {
      el.textContent = target.toLocaleString();
      clearInterval(timer);
    } else {
      el.textContent = Math.floor(current).toLocaleString();
    }
  }, 16);
}

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
      entry.target.classList.add('counted');
      animateCounter(entry.target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('[data-target]').forEach(el => counterObserver.observe(el));
```

HTML: `<span data-target="1250">0</span> clients served`

**Only use real numbers.** Never invent stats.

---

## Rule 5: Parallax Effect

At least one parallax element per page (usually the hero):

```css
.hero {
  background-attachment: fixed;
  background-size: cover;
  background-position: center;
}
```

For CSS-only parallax on solid backgrounds (more compatible):

```css
.parallax-section {
  transform: translateZ(0);
  background-position: center;
  background-size: cover;
}
```

Or using JS for element parallax:

```javascript
window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  document.querySelector('.parallax-element').style.transform = 
    `translateY(${scrollY * 0.3}px)`;
});
```

---

## Rule 6: Hover Effects

Every interactive element should respond to hover:

```css
/* Cards */
.card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.12);
}

/* Buttons */
.btn {
  transition: background 0.2s ease, transform 0.1s ease;
}
.btn:hover {
  filter: brightness(1.1);
  transform: translateY(-1px);
}

/* Links */
a { transition: color 0.2s ease; }
```

---

## Rule 7: Navigation Scroll Behavior

```css
nav {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 100;
  transition: background 0.3s ease, backdrop-filter 0.3s ease;
}

nav.scrolled {
  background: rgba(255,255,255,0.9);
  backdrop-filter: blur(10px);
  box-shadow: 0 1px 20px rgba(0,0,0,0.08);
}
```

```javascript
window.addEventListener('scroll', () => {
  document.querySelector('nav').classList.toggle('scrolled', window.scrollY > 50);
});
```

---

## Rule 8: Visual Design Direction (frontend-design)

**Do not use lookup tables.** Generic font-by-industry assignments produce predictable, forgettable pages. Instead, commit to a deliberate aesthetic direction for every site.

### Step 1 — Choose a Tone (pick one, commit fully)

Brutally minimal · Maximalist · Retro-futuristic · Organic/natural · Luxury/refined · Playful/toy-like · Editorial/magazine · Brutalist/raw · Art deco/geometric · Soft/pastel · Industrial/utilitarian · Dark & dramatic · Warm & handcrafted

### Step 2 — Choose Typography with Intent

- Pair a **distinctive display font** (headings) with a **refined body font** — 2 fonts max
- **Never use**: Inter, Roboto, Arial, Helvetica, Space Grotesk as the primary display font
- **Ask**: what would this brand print on a business card? That's the font energy to match
- Source from Google Fonts — look beyond the top-20 popular list

### Step 3 — Build a Color Story

- Dominant color + sharp accent — avoid timid, evenly-distributed palettes
- Commit to light OR dark — never a weak middle ground
- Use CSS variables for every color (`--primary`, `--accent`, `--bg`, `--text`)

### Step 4 — Design Something Memorable

- One detail that makes the page unforgettable: a texture, an unexpected layout, a micro-interaction, a typographic choice
- Asymmetry > symmetry · Overlap > separation · Diagonal flow > horizontal stacking
- Backgrounds with atmosphere (gradient mesh, noise, geometric pattern) > solid colors

**Every page must have a unique design identity. No two pages should look the same.**

---

## Rule 9: Animated Profile / Brand Ring

For sites with a key person's photo or brand mark as focal point:

```css
.profile-ring {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  padding: 4px;
  background: linear-gradient(135deg, var(--accent), var(--primary), var(--secondary));
  animation: ring-rotate 4s linear infinite;
}

@keyframes ring-rotate {
  from { filter: hue-rotate(0deg); }
  to { filter: hue-rotate(360deg); }
}

.profile-img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}
```

Use for: portfolio, personal brand, podcast, coach/consultant pages.

---

## Rule 10: Mobile-First Responsive

Every page must work on mobile. Core breakpoints:

```css
/* Base: mobile */
.container { padding: 0 16px; }
.grid { grid-template-columns: 1fr; }

/* Tablet */
@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

/* Desktop */
@media (min-width: 1024px) {
  .container { max-width: 1200px; margin: 0 auto; padding: 0 32px; }
  .grid { grid-template-columns: repeat(3, 1fr); }
}
```

Always test: navigation collapses to hamburger on mobile, text is readable, CTAs are tappable.

---

## Rule 11: Scroll-Driven Video (Apple-style) — `site_type: scroll`

Use when the user selects **Scroll Experience** or provides a video file.

The hero section stays sticky while the video advances frame by frame as the user scrolls.

### HTML Structure:
```html
<div class="scroll-video-container">  <!-- 500vh tall -->
  <div class="scroll-video-sticky">   <!-- position: sticky -->
    <video id="hero-video" muted playsinline preload="auto">
      <source src="hero.mp4" type="video/mp4">
    </video>
    <div class="scroll-progress-bar"></div>
    <div class="video-overlay">
      <h1 class="reveal">[Headline]</h1>
      <p class="reveal">[Sub-headline]</p>
      <a href="#next" class="btn reveal">Get Started</a>
    </div>
  </div>
</div>
```

### CSS:
```css
.scroll-video-container {
  height: 500vh; /* Controls scroll speed — more vh = slower */
  position: relative;
}

.scroll-video-sticky {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: hidden;
}

#hero-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.scroll-progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3px;
  background: var(--accent);
  width: 0%;
  transition: width 0.1s linear;
}
```

### JavaScript:
```javascript
const video = document.getElementById('hero-video');
const container = document.querySelector('.scroll-video-container');
const progressBar = document.querySelector('.scroll-progress-bar');

// Wait for video metadata
video.addEventListener('loadedmetadata', () => {
  function updateVideo() {
    const rect = container.getBoundingClientRect();
    const containerHeight = container.offsetHeight - window.innerHeight;
    const scrolled = -rect.top;
    const progress = Math.max(0, Math.min(1, scrolled / containerHeight));

    video.currentTime = progress * video.duration;
    progressBar.style.width = (progress * 100) + '%';

    requestAnimationFrame(updateVideo);
  }
  requestAnimationFrame(updateVideo);
});
```

### Mobile Fallback:
```javascript
// On mobile: autoplay instead of scroll-sync
if (window.innerWidth < 768) {
  video.autoplay = true;
  video.loop = true;
  video.play();
  // Disable scroll sync
}
```

**Height guide:** `300vh` = fast scroll, `500vh` = medium, `700vh` = slow/cinematic.

---

## Rule 12: prefers-reduced-motion

**Required in every generated page.** Some users have motion sensitivity. Always respect system preferences.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }

  .reveal {
    opacity: 1 !important;
    transform: none !important;
  }

  .parallax-element {
    transform: none !important;
  }
}
```

For scroll-video with reduced motion:
```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  // Show video poster/thumbnail, disable scroll sync
  video.pause();
  video.currentTime = 0;
}
```

---

## Rule 13: Performance Patterns

Apply these to every generated page to ensure smooth animations.

### Passive Scroll Listeners (prevents jank)
```javascript
// ✅ Correct — passive listener
window.addEventListener('scroll', handleScroll, { passive: true });

// ❌ Wrong — blocks scroll
window.addEventListener('scroll', handleScroll);
```

### requestAnimationFrame for smooth sync
```javascript
// ✅ Use rAF for anything tied to scroll position
function update() {
  // ... update animation state
  requestAnimationFrame(update);
}
requestAnimationFrame(update);

// ❌ Don't do this — fires too often, causes jank
window.addEventListener('scroll', () => {
  video.currentTime = calculateProgress();
});
```

### will-change (use sparingly)
```css
/* Only on elements that will animate */
.animated-card {
  will-change: transform;
}

/* Remove after animation completes (JS) */
el.addEventListener('transitionend', () => {
  el.style.willChange = 'auto';
});
```

### Debounce Resize Events
```javascript
let resizeTimer;
window.addEventListener('resize', () => {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => {
    // recalculate layout
  }, 150);
}, { passive: true });
```

---

## Rule 14: Accessibility Baseline

Every generated page must meet these minimums.

### Color Contrast
- Body text on background: **4.5:1 minimum** (WCAG AA)
- Large text (18px+ or 14px bold): 3:1 minimum
- Test: use WebAIM Contrast Checker mentally — white (#FFF) on #666 = 4.48:1 ✅, on #999 = 2.85:1 ❌

### Font Sizes
- Body text: minimum **16px**
- Captions/labels: minimum **14px**
- Never use `font-size` below 12px for any visible text

### Focus States
```css
/* Never remove focus outlines — make them visible */
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: 3px;
}

/* Remove only for mouse users */
:focus:not(:focus-visible) {
  outline: none;
}
```

### Alt Text
Every `<img>` must have `alt`:
```html
<!-- Decorative image -->
<img src="bg-pattern.svg" alt="">

<!-- Content image -->
<img src="profile.jpg" alt="[Owner name] — [brief description]">

<!-- Placeholder (CSS div instead of img) is better than alt="" on content images -->
```

### Semantic HTML
- One `<h1>` per page (the main headline)
- Heading hierarchy: H1 → H2 → H3 (never skip levels)
- Use `<nav>`, `<main>`, `<section>`, `<footer>` — not just `<div>`
- Buttons must have text or `aria-label`
- Links must describe destination ("Learn more about our services" not just "click here")

---

## Rule 15: Multilingual Page Pattern (EN/ES/PT)

When a site needs to serve multiple languages without page reload:

### Data Attributes
Add `data-en`, `data-es`, `data-pt` to every text element and input placeholder:
```html
<h1 data-en="Your Title" data-es="Tu Título" data-pt="Seu Título">Your Title</h1>
<input data-en="Your name" data-es="Tu nombre" data-pt="Seu nome" placeholder="Your name">
```

### setLang() Function
```javascript
function setLang(lang) {
  document.documentElement.setAttribute('data-lang', lang);
  localStorage.setItem('pref-lang', lang);
  document.querySelectorAll('[data-en]').forEach(el => {
    const text = el.dataset[lang] || el.dataset.en;
    if (!text) return;
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      el.placeholder = text;
    } else { el.textContent = text; }
  });
}
```

### Auto-Detection on Load
```javascript
(function() {
  const saved = localStorage.getItem('pref-lang');
  if (saved && ['en','es','pt'].includes(saved)) { setLang(saved); return; }
  const nav = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
  if (nav.startsWith('pt')) setLang('pt');
  else if (nav.startsWith('es')) setLang('es');
  else setLang('en');
})();
```

### Footer Override (unobtrusive escape hatch)
Small links in footer — visible but not prominent — let users override the detected language:
```html
<div style="margin-top:8px;font-size:11px;opacity:0.5">
  <button id="lang-en" onclick="setLang('en')">EN</button> |
  <button id="lang-es" onclick="setLang('es')">ES</button> |
  <button id="lang-pt" onclick="setLang('pt')">PT</button>
</div>
```

**Why this approach over IP geolocation:**
- `navigator.language` = free, instant, ~90% accurate, no external API, no latency
- `localStorage` persists user override across visits
- Footer override handles edge case: browser set to wrong language
- Single HTML file stays fully self-contained (no server-side rendering needed)

---

## Rule 16: Design Reference Database

Use this table in **Rule 8 Step 2 & 3** to make concrete, non-generic choices. Pick a tone → grab the font pair and palette that fit → commit.

### Font Pairings by Tone

| Tone | Display Font | Body Font | Google Fonts Import |
|---|---|---|---|
| Editorial / Magazine | Fraunces | Outfit | `Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Outfit:wght@300;400;600` |
| Editorial / Magazine | Playfair Display | DM Sans | `Playfair+Display:ital,wght@0,700;1,400&family=DM+Sans:wght@400;500` |
| Luxury / Refined | Cormorant Garamond | Jost | `Cormorant+Garamond:ital,wght@0,600;1,400&family=Jost:wght@300;400;500` |
| Luxury / Refined | Bodoni Moda | Mulish | `Bodoni+Moda:ital,opsz,wght@0,6..96,700;1,6..96,400&family=Mulish:wght@300;400` |
| Brutalist / Raw | Bebas Neue | Space Mono | `Bebas+Neue&family=Space+Mono:wght@400;700` |
| Brutalist / Raw | Barlow Condensed | IBM Plex Mono | `Barlow+Condensed:wght@700;900&family=IBM+Plex+Mono:wght@400` |
| Minimalist | DM Serif Display | DM Sans | `DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500` |
| Minimalist | Libre Baskerville | Source Sans 3 | `Libre+Baskerville:ital,wght@0,700;1,400&family=Source+Sans+3:wght@300;400` |
| Retro-futuristic | Syne | DM Mono | `Syne:wght@700;800&family=DM+Mono:wght@400;500` |
| Retro-futuristic | Chakra Petch | Space Mono | `Chakra+Petch:wght@600;700&family=Space+Mono:wght@400` |
| Organic / Natural | Lora | Nunito | `Lora:ital,wght@0,600;1,400&family=Nunito:wght@300;400;600` |
| Organic / Natural | Crimson Pro | Source Sans 3 | `Crimson+Pro:ital,wght@0,600;1,400&family=Source+Sans+3:wght@400;600` |
| Playful / Toy-like | Baloo 2 | Quicksand | `Baloo+2:wght@500;700;800&family=Quicksand:wght@400;500;600` |
| Playful / Toy-like | Fredoka | Nunito | `Fredoka:wght@500;600;700&family=Nunito:wght@400;600` |
| Art Deco / Geometric | Cinzel | Raleway | `Cinzel:wght@700;900&family=Raleway:wght@300;400;500` |
| Art Deco / Geometric | Poiret One | Josefin Sans | `Poiret+One&family=Josefin+Sans:wght@300;400;600` |
| Dark & Dramatic | Abril Fatface | Lato | `Abril+Fatface&family=Lato:wght@300;400;700` |
| Dark & Dramatic | Yeseva One | Josefin Sans | `Yeseva+One&family=Josefin+Sans:wght@300;400;600` |
| Industrial / Utilitarian | Oswald | IBM Plex Sans | `Oswald:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500` |
| Warm & Handcrafted | Playfair Display | Lato | `Playfair+Display:ital,wght@0,700;1,400&family=Lato:wght@300;400` |

---

### Color Palettes by Industry + Tone

Each entry: `--bg` · `--text` · `--accent` · `--surface`

| Industry | Tone | Palette |
|---|---|---|
| Freelancer / Consultor | Dark editorial | `#0C0C0A` · `#EDE8DE` · `#C8A96E` · `#141410` |
| Freelancer / Consultor | Light minimal | `#F9F7F3` · `#1A1A16` · `#2D5BE3` · `#FFFFFF` |
| Tech / SaaS | Dark cyber | `#0A0E1A` · `#E8EEFF` · `#4D9EFF` · `#111827` |
| Tech / SaaS | Light clean | `#F5F7FF` · `#0F172A` · `#6366F1` · `#FFFFFF` |
| Health / Wellness | Organic light | `#F5F0E8` · `#2D2A25` · `#6B8C6B` · `#FEFCF8` |
| Health / Wellness | Calm dark | `#121A14` · `#E8F0E8` · `#7EC8A0` · `#1A2B1C` |
| Restaurante / Food | Warm dark | `#110B07` · `#F5EDD8` · `#D4622A` · `#1C1208` |
| Restaurante / Food | Rich editorial | `#1A0A10` · `#F2E8E8` · `#C94040` · `#250F18` |
| Creativo / Diseño | Acid contrast | `#0A0A0A` · `#F0FF44` · `#FF3C38` · `#161616` |
| Creativo / Diseño | Clean white | `#FAFAFA` · `#111111` · `#FF3C38` · `#F0F0F0` |
| Moda / Luxury | Black gold | `#0A0A08` · `#F5F0E3` · `#C9A84C` · `#141412` |
| Moda / Luxury | Ivory refined | `#FAF8F3` · `#1A1816` · `#8B7355` · `#FFFFFF` |
| Bienes Raíces | Navy brass | `#0D1B2A` · `#EEE8DF` · `#B8975A` · `#162233` |
| Bienes Raíces | Light stone | `#F7F5F0` · `#1C1C1A` · `#4A6741` · `#FFFFFF` |
| Eventos | Electric dark | `#08060F` · `#EDE8FF` · `#8B5CF6` · `#110F1C` |
| Eventos | Warm fiesta | `#0F0800` · `#FFF5E6` · `#F59E0B` · `#1A1000` |
| Podcast / Media | Mono editorial | `#111111` · `#F2F2F0` · `#E84545` · `#1C1C1C` |
| Personal Brand | Warm neutral | `#F5F2ED` · `#2A2520` · `#C0714F` · `#FFFFFF` |

---

### CSS Pattern Keywords by Tone

Quick reference for spatial decisions — radius, spacing, border style, shadows:

| Tone | Border Radius | Spacing Feel | Border Style | Shadow |
|---|---|---|---|---|
| Editorial | 0px – 4px | Generous vertical, tight horizontal | None or 1px hairline | Minimal |
| Luxury | 0px – 2px | Wide margins, sparse content | Thin gold/brass lines | Soft glow or none |
| Brutalist | 0px – 2px | Dense, compressed | Thick 2-4px solid black | Hard offset shadows |
| Minimalist | 8px – 12px | Maximum whitespace | Subtle 1px `rgba` | Light diffuse |
| Retro-futuristic | 0px or full (pill) | Geometric grid | Neon thin lines | Colored glow |
| Organic | 16px – 32px | Breathing room, soft rhythm | Dotted or none | Warm diffuse |
| Playful | 16px – 32px (mixed) | Bouncy, variable | Bold colored | Playful offset |
| Art Deco | 0px | Structured columns | Double lines, ornamental | None |
| Dark & Dramatic | 0px – 6px | High contrast, large type | None or colored accent | Deep dramatic |
| Industrial | 0px | Compact, utilitarian | Monochrome solid | None |

---

**How to use this table in practice:**

1. Commit to a tone (Rule 8 Step 1)
2. Pick a font pair from the tone row → paste the Google Fonts import string
3. Pick a palette from the industry + tone row → assign to CSS variables
4. Use the CSS pattern keywords to guide radius, spacing, and border decisions
5. Add one memorable detail (Rule 8 Step 4) that goes beyond the table

---

## Rule 17: Reskin ≠ Overhaul (improving an existing page)

When a user calls an existing page "basic", "generic", or "not premium", changing
only colors and fonts on the same layout is a reskin — it will be rejected. A real
premium upgrade changes the ARCHITECTURE:

- Layout: asymmetric, full-bleed, editorial — not centered hero + uniform card grid
- Type scale: oversized display headlines (clamp up to 6–11rem), not 2–3rem
- Interaction: editorial interactive list (hover-expand rows) instead of identical
  cards; marquee; custom cursor; scroll-driven reveals
- A dramatic moment: a dark↔light section break, one signature accent color
- Replace emoji icons with line SVGs

Fastest way to lock direction: ask the user for ONE concrete reference (Awwwards /
Dribbble). One real reference beats three rounds of guessing.

### Feature-parity audit before replacing a live page (don't drop OR bury function)
A redesign is not just a new look — it replaces a working page. Two failures hit in the
BTQ liner-notes swap (validated 2026-06-24), and the user reported both as "missing":

1. **Don't silently drop functional affordances.** Before swapping `index-redesign.html`
   → `index.html`, diff the OLD page for things the new one must keep: contact form / email,
   **social links**, RSS/podcast platform links, nav anchors, i18n toggle, form POST endpoints,
   analytics/widgets, schema.org. Grep the old file (`git show HEAD~1:path`) for `mailto:`,
   `instagram|tiktok|linkedin|spotify|youtube`, `#contacto`, form `action=` — anything present
   before must be present after, or it's a regression.
2. **Present ≠ findable — surface contact + social, don't just leave them in the footer.**
   The redesign technically *had* email + social in the bottom colophon, but a minimal premium
   top bar with no "Contacto" link meant the user "couldn't find them anywhere." Fixes that
   worked: a **nav link** to the contact area, and a dedicated **contact section** that bundles
   email + a working form + social icons together (not scattered). If the nav can't reach it in
   one click, assume the user won't find it.

**Static-site contact forms:** a static host (Vercel/Netlify) has no backend to receive a POST.
Use a form service (Web3Forms — no account, key in the markup, AJAX + graceful no-JS fallback) or
a serverless function. A `mailto:` link alone is not "a form." See [[reference_btq_contact_form]].

---

## Rule 18 — Premium / agency tier (when "ultra-premium" is the brief)

When the user explicitly wants an **agency-grade, ultra-premium, "break the mold"** page
(not a standard business/portfolio site), the flat single-file recipe is not enough —
fade-up-on-scroll + Google Fonts is exactly what reads as "AI-generated." Promote to this
tier. **This is opt-in** — only for pages where distinctiveness is the whole point. Standard
pages stay on Rule 1's self-contained recipe.

> ### ⚠️ This is a TECHNIQUE tier, not a LOOK. Do not copy-paste it.
> The BTQ liner-notes page (black + gold, Boska serif, fbm gold shader, vinyl/record metaphor)
> is **one expression** of this tier — it is **not the template**. Cloning that exact palette,
> font, shader, and metaphor onto the next page produces a *new* generic clone, which is the
> very failure Rule 0 exists to prevent. **Always re-run Rule 0 first:** the page's *type*,
> brand, and one real reference decide the concept (tone, palette, type, the signature metaphor
> and what the background field actually *is*). Rule 18 only supplies the **class of capabilities**
> — a reactive global field, momentum scroll, scrubbed motion, tactile feedback — to *express*
> that concept. The capabilities endure; the look is rebuilt every time.
>
> **Adapt by page type, e.g.:** a fintech/SaaS page → the "reactive field" might be a precise
> data-grid/particle mesh in its brand color, type a clean grotesk, motion crisp and snappy.
> A restaurant → warm film-grain photography parallax, a serif with appetite, slow dissolves.
> An events page → kinetic typography + a strobe/pulse field. Same *engine*, different *vehicle*.
> If two pages from this tier could swap palettes and fonts and look interchangeable, the concept
> step was skipped.

### What separates premium from "nice template"
The gap is almost never *more sections* — it's **continuous, reactive motion + a signature
moment + non-default type.** The page should feel alive *after* the hero, not just during it.

### The stack that works (validated on the BTQ liner-notes page)
1. **A global reactive background, not a hero-only one.** A `position:fixed` WebGL canvas
   (`z-index:0`, `pointer-events:none`) behind the WHOLE page — a raw fragment shader
   (fbm noise, brand colors) reacting to `uTime` + an eased pointer. Body is `background:transparent`,
   the dark base color sits on `<html>` so it degrades cleanly. Putting atmosphere only behind
   the hero is the #1 reason "everything after the scroll feels dead."
2. **Momentum scroll.** Lenis with `smoothWheel:true` **and `syncTouch:true`** — touch must feel
   inertial, not the dry native scroll. Drive `ScrollTrigger.update` from Lenis; run via
   `gsap.ticker` with `lagSmoothing(0)`.
3. **Scrubbed, concept-driven motion — not uniform fade-up.** GSAP ScrollTrigger: one pinned
   kinetic hero moment (type splitting/scaling on scrub) + gentle scrubbed parallax on the
   lower half (drifting numerals, scaling pull-quote, drawing section rules) so nothing sits static.
4. **Tactile feedback.** Click/tap spawns a feedback gesture — a DOM ripple at the point AND a
   pulse fed into the shader at that coordinate (decaying uniform). Use `pointerdown`/`pointermove`
   (covers mouse + finger), not `mousedown`/`mousemove`.
5. **Non-default type.** Source from **Fontshare** (Boska, Satoshi, Clash Display, General Sans…)
   or another non-Google foundry — sidesteps the Inter/Roboto/Fraunces "AI tell." Oversized display
   (clamp up to ~11–15rem).
6. **Custom cursor** behind `@media (pointer:fine)` only — never on touch.

### Rule 1 exception (premium tier only)
External CDN libraries **are allowed** here (GSAP, ScrollTrigger, Lenis via jsdelivr) — the
self-contained constraint is relaxed because the motion quality is the deliverable. Everything
else (CSS, shaders, fonts link) still lives in the one file.

### Non-negotiable guardrails (still apply)
- Everything degrades: wrap GSAP/Lenis in `if (window.gsap && window.ScrollTrigger && !reduce)`;
  the WebGL IIFE must `canvas.remove()` on context/compile/link failure → CSS background shows.
  No JS = clean static editorial layout, never a broken page.
- Full `prefers-reduced-motion` branch: kill scrub/pin, ripple `display:none`, shader draws one frame.
- Passive listeners; cap `devicePixelRatio` (~1.5) in the shader; `will-change` only on animated nodes.

**Tell, not template:** the goal is that *we* are the differentiator. If the page could be
swapped with another AI page by changing the logo, it failed Rule 0 — this tier is how you make
that impossible.

### Full-bleed reactive background — gotchas (validated on the Andyfreelancer redesign)
The "reactive field" of point 1 doesn't have to be a shader. On Andyfreelancer it became an
**interactive SVG world map** (every country glows brand-red + shows its name on hover/tap) — same
*engine* (global reactive field), different *vehicle*. Whatever the field is, these traps recur:

- **Fixed, not absolute — and pan it on scroll.** A field anchored with `position:absolute` (or only
  behind the hero) **gets lost after a full scroll** — the exact "fondo de BTQ se pierde" bug. Use
  `position:fixed; z-index:0` so it's always behind the viewport, then add a *gentle* GSAP
  scroll-driven pan (`yPercent:-5`, `scrub:0.6`) so it feels alive without drifting off. Big pan +
  high scrub (`-8`/`1.1`) reads **stiff** ("más tieso"); keep the travel small and the scrub loose.
- **`preserveAspectRatio="…meet"`, not `slice`, for maps/wide art.** `slice` (cover) **crops the top
  and bottom** on wide/ultrawide screens — the southern hemisphere disappears. `meet` (fit-whole)
  keeps the full geometry visible; pair with `height:calc(100vh - <navH>)`.
- **Unify the theme across every section.** An opaque cream/orange block dropped mid-page makes the
  color transition "pega demasiado fuerte" and the samples "chocan porque no es el mismo oscuro."
  Sections over a global field should be **transparent or same-family translucent** (`rgba(bg,0.5)` +
  `backdrop-filter:blur`), including nav and footer — let the one field carry the whole page.
- **Real geometry for an interactive map.** Use Natural Earth via **world-atlas**
  (`countries-110m.json`, public domain) + **d3-geo** (`geoNaturalEarth1`, `geoPath`, `fitSize`) +
  **topojson-client** (`topojson.feature`) — not a hand-traced blob. Degrade to the plain dark
  background if the fetch/CDN fails.
- **pointer-events pass-through.** So hover reaches a fixed field behind the content:
  `header,section,footer{pointer-events:none}` then re-enable the interactive children
  (`a,button,input,select,textarea,summary,label,nav` + the map paths). Empty content areas then let
  the cursor light up the field behind them.
- **Live font specimen beats a Canva mockup** when the user is unfamiliar with a typeface — build a
  tiny standalone HTML specimen with the real Fontshare faces rather than rendering a Canva image
  (Canva bakes in un-editable garbled microtext). See [[feedback_named_concept_drives_render]].
