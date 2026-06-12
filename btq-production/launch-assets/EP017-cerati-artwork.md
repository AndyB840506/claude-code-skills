# EP.017 — Soda Stereo · Artwork (dirección congelada 2026-06-12)

Primera aplicación de la dirección visual congelada de BTQ (póster gráfico editorial,
siluetas a contraluz sobre dorado — bloques verbatim en
`.claude/skills/episode-launch/docs/brand-constants.md`).

**Calendario:** grabación sáb 13-jun · live dom 14-jun 8PM.
Teaser intriga → viernes/sábado · Lanzamiento → domingo 8PM.

---

## PORTADA 1:1 — GENERADA Y APROBADA 2026-06-12 ✓

```
Square podcast cover, 1:1, 3000x3000px. Graphic editorial poster design
with strong backlit silhouettes — NOT photorealistic 3D.

SCENE: The silhouettes of EXACTLY THREE male musicians — a rock trio —
performing on a dark stadium stage, backlit so they read as pure black
shapes with thin golden rim light (#C9A84C) on their edges:
  - CENTER, slightly forward: the frontman, lean, singing into a
    microphone on a stand while playing an electric guitar, head tilted up
  - LEFT, slightly behind: the bassist, legs apart, bass slung low
  - RIGHT, slightly behind: the drummer at his kit, arms raised mid-hit
Count check: three people total, no more, no less.
NO visible face detail on any of them — solid silhouettes and rim
light only.

Behind the trio, a wall of warm golden stage light (#C9A84C) with haze
and smoke, forming a glowing halo that makes the three black silhouettes
pop. In the far background, very dim, thousands of tiny out-of-focus
crowd lights (lighters).

ERA: late 1980s Latin American new wave / rock aesthetic. The musicians'
hair and clothing are 1988-correct: voluminous hair, slim jackets,
skinny trousers. Analog film grain, slight halation on the lights,
muted retro color grading, screen-print poster texture. No modern
elements: no LED screens, no smartphones, no laser lights, no in-ear
monitors. It must feel like a poster printed in 1988.

BACKGROUND: void black #0A0A0A dominates the top and bottom of the image.

TYPOGRAPHY (render text EXACTLY as written, letter by letter, no changes):
  TOP THIRD, centered, above the band:
    Line 1: "SODA STEREO" — huge ultra-bold condensed sans-serif,
            uppercase, signal gold #C9A84C
    Line 2: "EL LIDERAZGO QUE SIGUE SONANDO" — white, uppercase,
            same font, one third the size of Line 1, letter-spaced

FOOTER: full-width strip at the very bottom, on the void black background.
  Left: "Behind the Queue" in small white sans-serif
  Center: "EP.017" in bold signal gold #C9A84C
  Right: small silver platform icons — Spotify (circle with three curved
  lines) and YouTube (rounded rectangle with play triangle)
```

**Checklist:** (1) exactamente 3 siluetas; (2) texto letra por letra; (3) cero caras +
estética 1988. — Pasó las tres el 2026-06-12.

---

## TEASER 9:16 — Intriga (publicar viernes/sábado — NO revela la banda)

Concepto: el micrófono solo bajo el spotlight — siembra la pregunta del episodio
sin nombrar a Soda Stereo. La revelación llega el domingo con la portada.

```
Vertical image, 9:16, 1080x1920px. Graphic editorial poster design —
NOT photorealistic 3D.

SCENE: a single vintage microphone on a straight stand, completely alone
at the center of a dark stadium stage, positioned in the upper half of
the vertical frame. One golden spotlight (#C9A84C) falls on the empty
microphone from above, forming a visible cone of light through haze.
Nobody is on stage. In the dark background, thousands of tiny
out-of-focus crowd lights (lighters), very dim — the crowd is still
there, waiting. 1980s concert aesthetic: analog film grain, slight
halation on the lights, muted retro color grading, screen-print poster
texture. No modern elements: no LED screens, no smartphones.

BACKGROUND: void black #0A0A0A dominates the top and bottom of the image.

TYPOGRAPHY (render text EXACTLY as written, letter by letter, no changes):
  BOTTOM THIRD, centered:
    Line 1: "LO QUE CONSTRUISTE..." — white, uppercase, bold condensed
            sans-serif
    Line 2: "¿SIGUE SONANDO SIN TI?" — signal gold #C9A84C, uppercase,
            same font, twice the size of Line 1
    Line 3: "DOMINGO 8 PM · NUEVO EPISODIO" — silver, small, uppercase,
            letter-spaced

FOOTER: full-width strip at the very bottom, on the void black background.
  Left: "Behind the Queue" in small white sans-serif
  Center: "EP.017" in bold signal gold #C9A84C
  Right: small silver platform icons — Spotify (circle with three curved
  lines) and YouTube (rounded rectangle with play triangle)
```

**Checklist:** (1) el escenario está VACÍO — si aparece una figura humana, regenerar;
(2) texto letra por letra — ojo al signo "¿" de apertura, Flow a veces lo omite o lo
voltea (si lo daña dos veces, fallback: quitar "¿" y dejar solo "SIGUE SONANDO SIN TI?");
(3) las tres líneas no llevan tildes a propósito — no agregar ninguna.

---

## TEASER 9:16 — Lanzamiento (domingo 8PM)

NO se genera desde cero: se reusa la portada aprobada. En Flow, sobre la imagen
aprobada de la portada:

1. Pedir el reframe a vertical: `"same image, extend to 9:16 vertical format,
   keeping the band and all text identical"`
2. Cambiar solo la línea blanca: `"replace the line EL LIDERAZGO QUE SIGUE SONANDO
   with YA DISPONIBLE, same font, same position, same color"`

Resultado: misma imagen que la audiencia ya vio en el feed de intriga, ahora con
"YA DISPONIBLE" — refuerzo de reconocimiento, no asset nuevo.

**Checklist:** (1) siguen siendo 3 siluetas tras el reframe; (2) "YA DISPONIBLE"
letra por letra; (3) el footer sobrevivió la extensión vertical (si Flow lo deforma,
recortar y regenerar solo el strip).
