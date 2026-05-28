# Design Guide — Animations, HTML Rules & Visual Patterns

Apply these patterns to every generated page. They come from the instagram-web kit and are proven to produce professional, engaging results.

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

## Rule 8: Visual Design by Site Type

Match the design mood to the business:

| Site Type | Theme | Fonts | Vibe |
|---|---|---|---|
| Tech / SaaS | Dark (#0D0D0D + cyan/blue accent) | Space Grotesk, Inter | Futuristic, precise |
| Creative / Portfolio | Dark or high-contrast | Bebas Neue, Inter | Bold, visual |
| Health / Wellness | Light (#FAFAFA + green/earth) | Lato, Playfair Display | Calm, natural |
| Business / Corporate | Light (#FFFFFF + navy/grey) | Inter, Roboto | Professional, clean |
| Food / Hospitality | Warm (cream + earthy tones) | Playfair Display, Lato | Inviting, warm |
| Events | High energy (dark + vibrant accent) | Bebas Neue, Open Sans | Energetic, urgent |
| Blog / Editorial | Clean neutral | Georgia, Inter | Readable, calm |
| E-commerce | Light, conversion-optimized | Inter, Helvetica | Clean, CTA-focused |

Choose Google Fonts that match the vibe — 2 fonts max (one serif/display, one sans-serif for body).

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
