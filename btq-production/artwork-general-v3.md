# BTQ — Artwork general del show (v3) — og-image / social preview

> ## ⛔ NO USAR ESTE PROMPT TAL CUAL (2026-07-23)
>
> El prompt de abajo pide **círculos concéntricos** de fondo ("like the grooves of a
> vinyl record"). Ese motivo quedó **VETADO en TODAS las imágenes BTQ** por decisión de
> Andy del **2026-07-10 (EP.021)** — ver `.claude/skills/episode-launch/docs/brand-constants.md`
> § "Reglas de la dirección" #3 y su bloque congelado, que incluye la línea
> `DO NOT render any concentric ring, circle, halo, or archery-target pattern anywhere in this image.`
> Este archivo es anterior a esa decisión y nunca se actualizó.
>
> **Qué falta para poder usarlo:** decidir con Andrés qué patrón geométrico reemplaza a
> los surcos de vinilo (la regla pide "el patrón del universo del referente"; para la
> imagen de marca general no hay referente de episodio, así que es una decisión creativa
> abierta). Hasta entonces, la og-image no se regenera desde acá.
>
> Recordatorio aparte: la og-image **actualmente en vivo** tiene el typo horneado
> "PREMIUM KEY EDITOIAL" y un garabato sobre el vinilo — sigue publicada.

Reemplaza `website/og-image.png` (1600×900, referenciado en `index.html` para
`og:image`/`twitter:image`). El actual tiene un bug real: texto roto de IA
("PREMIUM KEY EDITOIAL" — typo, debería decir EDITORIAL — y un garabato ilegible
superpuesto sobre el vinilo). Esta versión aplica el estilo v3 (ver
`.claude/skills/episode-launch/docs/brand-constants.md`) a la imagen de marca general del
show, no de un episodio puntual — así que no lleva número de EP, lleva la URL.

---

## Social preview / og-image — 1920×1080px (recortar a 1600×900 al subir)

```
Dark cinematic editorial image, rendered with real volume and material
texture (fabric, headset, desk) — NOT a flat silhouette cutout. Void
black background #0A0A0A.

Center-right composition: a contact-center supervisor, seen from
behind or at a three-quarter angle, standing at their desk wearing a
professional contact-center boom-mic headset (NEVER music/gaming
headphones) — looking out over a dim row of call-center workstations
fading into darkness, as if reflecting at the end of a shift. Rendered
with real shading on the headset, shirt fabric and desk surface — not
a flat black shape.

Dark, moody shading with warm golden #C9A84C rim light and ambient
glow outlining the figure, like a dark statue lit from behind.

Background: concentric circles of thin gold #C9A84C line art radiating
behind the figure like a halo — styled like the grooves of a vinyl
record, tying the contact-center scene to the "pop culture" identity
of the show. Subtle, like an engraved watermark, not competing with
the figure or the text.

No circuit boards. No cartoon style. Cinematic.

Typography:
- Top center: five small gold #C9A84C dots
- "BEHIND THE QUEUE" — ultra bold white condensed sans-serif, large
- "BTQ" — small gold below

Below the figure, left-aligned:
"Donde la cultura pop entra al contact center."
White text, bold

Footer black bar at bottom:
- Left: "behind-thequeue.com" white
- Right two rows:
  Row 1: Facebook icon, Instagram icon, TikTok icon
  Row 2: Spotify icon, Apple Podcast icon, Amazon Music icon

Do NOT place any text in the bottom-right corner.
Format: wide 16:9, 1920x1080px.
```

**Checklist antes de subir:** (1) headset de contact center (diadema con micrófono boom),
NUNCA audífonos de música/gaming; (2) render con volumen/textura real, no silueta plana; (3)
círculos concéntricos estilo surcos de vinilo, finos, sin competir con el texto; (4)
tipografía en las 3 capas (puntos, wordmark, BTQ) + tagline exacto, letra por letra — cero
texto adicional inventado (el bug actual tiene "PREMIUM KEY EDITOIAL" y un garabato que NO
deben repetirse); (5) footer con URL a la izquierda y las 2 filas de íconos a la derecha,
sin número de episodio (esta imagen es de marca general, no de un episodio).

**Al aprobar:** reemplazar `btq-production/website/og-image.png`, comprimir bajo 500 KB si
hace falta, y desplegar con `vercel --prod` desde `btq-production/website/` (recordar: BTQ
NO se despliega con git push, ver memoria `reference_deploy_mechanisms`).
