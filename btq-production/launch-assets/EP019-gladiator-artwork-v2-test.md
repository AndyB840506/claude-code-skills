# EP.019 — Gladiator · Artwork v2 TEST (cómic pulp ilustrado)

Prueba de la nueva dirección de artwork BTQ (ver `.claude/skills/episode-launch/docs/brand-constants.md`,
CONGELADA v2 — 2026-07-04). Mismo episodio que v1 (silueta a contraluz) para comparar
manzanas con manzanas. Técnica: cómic pulp años 40-50, ilustrado a mano, halftone — tomada
de `corporate-crime-confidential-production` pero con la paleta propia de BTQ (negro+dorado,
sin tinta/pergamino/carmesí).

**Referente ficticio (Gladiator/Máximo, personaje de película, no persona real)** → rostro
expresivo permitido por la regla de rostros v2.

---

## PORTADA 1:1 — 3000×3000px

```
1940s-50s adventure pulp comic book cover illustration, hand-inked line
art with bold black outlines and cross-hatching, halftone dot shading
like vintage comic/newsprint printing — NOT a photorealistic render,
NOT a smooth digital illustration, NOT a backlit silhouette.

SCENE: EXACTLY ONE Roman gladiator, mid-action — lunging forward with a
short sword (gladius) raised overhead in a dramatic diagonal strike.
Segmented armor, crested helmet, cloak whipping behind him from the
motion, sand kicking up dynamically at his feet. His face is visible
beneath the helmet's brow, dirt-streaked, jaw set in fierce
determination — a fictional pulp-hero face, not a real person's
likeness. Rendered in bold black ink linework with gold #C9A84C
halftone shading on armor edges, muscle highlights and the sword's
blade. Behind him, the tiered stands of the Colosseum arena, packed
with tiny ink-crosshatched crowd silhouettes in flat gold and black.
Count check: one gladiator total.

Two-color pulp palette: void black #0A0A0A for ink linework and shadow,
signal gold #C9A84C as the dominant highlight/light color, off-white
#F5F2EC for small highlight details only. Aged newsprint grain texture,
slightly worn print edges, faint vintage misregistration halo on fine
linework. Era-correct armor and props for ancient Rome (~180 AD). No
modern elements, no gradients, no photorealistic shading — flat color
blocking with ink cross-hatching for shadow.

TYPOGRAPHY (render text EXACTLY as written, letter by letter, no changes):
  TOP THIRD, centered, bold vintage pulp comic lettering:
    Line 1: "GLADIATOR" — huge, signal gold #C9A84C with black ink
            outline
    Line 2: "LA HUELLA QUE DEJA UN LIDER" — off-white #F5F2EC,
            one third the size of Line 1, letter-spaced

FOOTER: full-width strip at the very bottom, on the void black background.
  Left: "Behind the Queue" in small white sans-serif
  Center: "EP.019" in bold signal gold #C9A84C
  Right: small silver platform icons — Spotify (circle with three curved
  lines) and YouTube (rounded rectangle with play triangle)
```

**Checklist:** (1) EXACTAMENTE 1 gladiador, en acción (no de pie quieto); (2) es ilustración
de tinta+halftone — si Flow devuelve algo fotorrealista o una silueta lisa, regenerar; (3)
texto letra por letra ("LIDER" sin tilde a propósito); (4) rostro visible y expresivo está
BIEN aquí (personaje ficticio) — si en vez de esto fuera un episodio de un músico/persona
real, ahí sí habría que ocultar el rostro.

---

## 16:9 — YouTube thumbnail — 1920×1080px

```
Same illustration technique and palette as the 1:1 version: 1940s-50s
adventure pulp comic book cover illustration, hand-inked line art with
bold black outlines and cross-hatching, halftone dot shading — NOT
photorealistic, NOT a smooth digital illustration, NOT a silhouette.

COMPOSITION: split for a wide frame —
  RIGHT HALF (exactly right 50% of frame): EXACTLY ONE Roman gladiator
  mid-lunge, gladius raised in a diagonal strike, cloak whipping with
  the motion, face visible and fierce beneath the helmet brow. Ink
  linework with gold #C9A84C halftone shading. Behind him, the
  Colosseum crowd in flat ink-crosshatched silhouette.
  LEFT HALF (exactly left 50% of frame): mostly void black #0A0A0A,
  reserved for the text.

Two-color pulp palette: void black #0A0A0A, signal gold #C9A84C,
off-white #F5F2EC for small highlights only. Aged newsprint grain,
worn print edges. Era-correct ancient Rome (~180 AD). No modern
elements.

TYPOGRAPHY (render text EXACTLY as written, letter by letter, no changes):
  LEFT HALF, vertically centered, left-aligned, bold vintage pulp
  comic lettering:
    Line 1: "LA HUELLA" — off-white #F5F2EC with black ink outline,
            huge
    Line 2: "DEL LIDER" — signal gold #C9A84C, same size or bigger
  No other text anywhere in the image. No footer bar on this format —
  YouTube crops thumbnails and the footer would be cut.
```

**Checklist:** (1) EXACTAMENTE 1 gladiador en la mitad derecha, en acción; (2) "LA HUELLA /
DEL LIDER" letra por letra, legible en miniatura (verlo al 10%); (3) mitad izquierda negro
casi puro; (4) sin footer en este formato a propósito.

---

## 9:16 — sigue la misma lógica (no generado en este test)

Cuando se apruebe 1:1 y 16:9, el 9:16 se deriva con la misma composición vertical que usaba
v1 (gladiador en el tercio superior-central, texto en el tercio inferior sobre degradado a
negro) pero con la técnica de tinta+halftone en vez de silueta a contraluz — mismo patrón
de adaptación que ya se usó para pasar de v1 1:1 a v1 9:16.

---

## Comparación pendiente

Genera estos dos (1:1 y 16:9) en Flow y compáralos contra:
- La portada real ya publicada de EP.019 (silueta a contraluz, v1)
- El comp de CSS "Concepto A" del artifact de hace un momento

Si te convence, este mismo patrón se aplica hacia adelante a EP.020 (aunque ahí no hay
referente pop — habría que pensar qué escena ilustrar para un episodio sin película/banda,
posiblemente la escena del agente "gameando" el número, estilo pulp de oficina) y a los
episodios futuros.
