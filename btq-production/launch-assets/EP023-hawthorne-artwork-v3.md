# EP.023 — Efecto Hawthorne · Artwork v3

EP.023 no tiene referente pop (pilar SEO, igual que EP.020 y EP.022) — mismo desafío: qué
escena representa el tema en el lenguaje visual v3 (ver
`.claude/skills/episode-launch/docs/brand-constants.md`), sin usar el círculo concéntrico/
diana que quedó VETADO desde EP.021 salvo que sea el sujeto literal de la escena (no es el
caso aquí).

**Concepto (revisado 2026-07-21, tras validación local):** el primer intento usaba un
agente de call center partido a la mitad por la luz (ver historial de esta sesión) —
funcionó como metáfora pero Andy prefirió quitar la persona del todo y anclar el símbolo
directamente al contenido del capítulo. Concepto final: **un foco incandescente estilo
1920s de filamento visible** (el objeto real del experimento de iluminación de la fábrica
Hawthorne, 1924) colgando de un cable, iluminando **un headset moderno de call center con
boom-mic** apoyado sobre un escritorio de madera oscura. Une el origen histórico real del
capítulo con su sujeto actual en una sola imagen literal, sin gente — foco = el estudio
original; headset = el monitoreo de calidad de hoy. El patrón geométrico de fondo se
resuelve con una **forma de onda de audio** (waveform de una llamada) en línea fina
dorada detrás del foco — literal al mundo de un pódcast sobre monitoreo de llamadas, y
evita por completo cualquier círculo/anillo. Validado con test local en ComfyUI
(Z-Image Turbo, 1024×1024, `E:\AI\outputs\BTQ-EP023-bulb-v1_00001_.png`) — aprobado por
Andy ("si esta bn").

---

## PORTADA 1:1 — 3000×3000px

```
Dark cinematic editorial still-life photograph, rendered with real
volume and material texture (glass, filament, headset plastic and
foam, wood grain) — NOT a flat silhouette cutout. Void black
background #0A0A0A. No people, no hands, no faces anywhere in the
image.

Center composition: a vintage 1920s-style incandescent light bulb
with a visible glowing filament, hanging from a bare cord from the
top of the frame, casting warm golden #C9A84C light downward.
Directly below it, resting on a dark wooden desk, a modern
professional contact-center boom-mic headset (NEVER music/gaming
headphones), its coiled cable resting beside it on the desk. The
bulb's warm glow is the only light source in the scene, illuminating
the headset from above and casting a soft shadow beneath it, while
the rest of the scene fades into near-total black.

Dark, moody shading — warm golden glow concentrated on the bulb and
headset, near-total darkness everywhere else. Real shading and
reflections on the glass bulb and headset plastic — not a flat shape.

Background: a subtle audio waveform pattern — the visual shape of a
recorded phone call, thin gold #C9A84C line art, oscillating
horizontally behind the bulb like an engraved watermark. This is a
deliberate visual pun: a call center runs on recorded/monitored
audio. Subtle, not competing with the bulb/headset or the text.

DO NOT render any concentric ring, circle, halo, or archery-target
pattern anywhere in this image.

No circuit boards. No cartoon style. Cinematic.

Typography:
- Top center: five small gold #C9A84C dots
- "BEHIND THE QUEUE" — ultra bold white condensed sans-serif, large
- "BTQ" — small gold below

Below the bulb and headset:
"Efecto Hawthorne: la llamada que nadie audita"
White text, bold

Footer black bar at bottom:
- Left: "Behind the Queue" white
- CENTER: "EP.23" gold #C9A84C — prominent
- Right two rows:
  Row 1: Facebook icon, Instagram icon, TikTok icon
  Row 2: Spotify icon, Apple Podcast icon, Amazon Music icon

Do NOT place any text in the bottom-right corner.
Format: square 3000x3000px.
```

**Checklist:** (1) CERO personas/manos/caras en la imagen — es una escena de objetos; (2)
el foco debe leerse como un foco incandescente vintage de filamento visible, no una lámpara
moderna; (3) el headset debe leerse claramente como un headset de call center con boom-mic,
NUNCA audífonos de música/gaming; (4) el foco es la ÚNICA fuente de luz — el resto de la
escena cae a negro casi total; (5) render con volumen/textura real (vidrio, filamento,
plástico del headset, veta de la madera), NO silueta plana; (6) el patrón de fondo debe
leerse como una forma de onda de audio (línea horizontal oscilante), no como decoración
abstracta ni como anillo; (7) CERO círculos concéntricos, anillos o diana en ninguna parte
de la imagen — vigilar especialmente que el waveform no se cierre sobre sí mismo formando
un círculo; (8) tipografía en las 3 capas + título exacto letra por letra; (9) footer con
EP.23 y las 2 filas de íconos completas.

---

## 16:9 — YouTube thumbnail / web hero — 1920×1080px

```
Same rendering style and palette as the 1:1 version: dark cinematic
editorial still-life photograph, real volume and material texture,
void black #0A0A0A background, warm golden #C9A84C glow. No people,
no hands, no faces anywhere in the image.

COMPOSITION: wide frame, the vintage incandescent bulb and the
contact-center headset positioned right-of-center, same as the 1:1
concept — bulb hanging above, headset resting on the dark wooden desk
below it, warm glow as the only light source. Subtle gold
audio-waveform line art radiates behind the bulb. Left portion of the
frame stays mostly void black, reserved for text.

DO NOT render any concentric ring, circle, halo, or archery-target
pattern anywhere in this image.

Typography (left-aligned, vertically centered in the black portion):
- "EFECTO HAWTHORNE" — off-white #F5F2EC, huge, bold
- "la llamada que nadie audita" — gold #C9A84C, smaller, below

No footer bar on this format — thumbnails get cropped.
Format: wide 16:9, 1920x1080px.
```

**Checklist:** (1) foco + headset claramente visibles en la mitad derecha, legibles incluso
en miniatura; (2) mitad izquierda casi negro puro para el texto; (3) cero personas/manos/
caras; (4) texto legible al 10% de zoom; (5) sin footer a propósito en este formato; (6)
cero círculos/anillos/diana.

---

## 9:16 — historia/teaser — 1080×1920px

Se deriva de la misma composición vertical usada en episodios anteriores: foco + headset +
waveform dorado en el tercio superior-central, degradado a negro hacia abajo, título en el
tercio inferior, mismo bloque de tipografía y footer que el 1:1. No generado en este
documento — replicar el mismo patrón de adaptación 1:1→9:16 ya usado en episodios previos
(EP.020, EP.022) una vez se apruebe el 1:1. Mismo veto de círculos/anillos/diana aplica.

---

## Nota

Tercera vez que la dirección v3 se aplica a un episodio SIN referente pop (EP.020: diana de
tiro al blanco; EP.022: checklist con una casilla sin marcar; EP.023: foco incandescente
vintage + headset moderno + waveform de audio). Mismo criterio en los tres: un símbolo
literal del propio contenido del episodio en vez de un patrón decorativo desconectado — en
EP.023 además se optó explícitamente por quitar a la persona de la escena por completo tras
el primer intento (ver historial: concepto original de un agente partido por la luz,
descartado 2026-07-21 por preferencia de Andy, no por falla técnica).
