# Brand constants (BTQ)

| Element | Value |
|---------|-------|
| Background | Void Black `#0A0A0A` |
| Accent | Signal Gold `#C9A84C` |
| Off-white | `#F5F2EC` |
| Headline font | Playfair Display |
| Body | DM Sans |
| Accent | Bebas Neue |
| Headsets | Contact center boom mic — NEVER music headphones |
| Spotify category | Society & Culture |
| Primary language | Spanish |
| Core audience | Hombre 35–44, supervisor/gerente BPO — Colombia 70% + EE.UU. 20% (analytics 2026-06-12) |
| Nostalgia era | Referentes y estética 80s/90s — la adolescencia de la audiencia núcleo |
| Priority platform | LinkedIn (profesional 35–44; 15% escucha en desktop en el trabajo) |

---

## Dirección de artwork (CONGELADA v3 — 2026-07-04 — restaurada de EP.10 Kratos)

> **Historial:** la dirección original de EP.10 (Kratos/God of War) tenía más capas de
> diseño de las que sobrevivieron — postura narrativa (de espaldas, reflexionando, no de
> frente a cámara), una SEGUNDA figura a otra escala para crear relación, un símbolo
> watermark del universo del referente, y una tipografía en capas (5 puntos + wordmark +
> "BTQ"). Esa riqueza se perdió cuando se "congeló" v1 el 2026-06-12 (EP.017-019: figura
> única, de frente, parada, en humo dorado) — el usuario lo calificó de genérico. Se probó
> v2 (cómic pulp ilustrado, 2026-07-04) y tampoco convenció. **v3 restaura la fórmula de
> EP.10 como el estándar oficial** — no es una idea nueva, es recuperar lo que ya
> funcionaba antes de simplificarse de más.

**BTQ = imagen editorial cinemática, render con volumen (no silueta plana) + patrón
geométrico watermark del universo del referente.** Lo que define el estilo es la TEXTURA
del render — figuras con volumen y material real (músculo, armadura, tela), sombreadas en
tonos oscuros con luz dorada ambiental/de contorno, como una estatua oscura iluminada desde
atrás — no un recorte plano de silueta lisa (esa era la falla de v1). El número de figuras
NO es una regla fija: una sola figura protagonista está perfecto si la historia es de un
solo personaje; una segunda figura a otra escala se usa SOLO cuando la relación (maestro/
aprendiz, líder/sucesor) es parte central de la historia de ese episodio — no forzarla si
no aplica.

Bloques que se copian VERBATIM en todo prompt de portada (cambian el sujeto, si aplica una
segunda figura, el patrón geométrico y el título):

**[BLOQUE CONGELADO — ATMÓSFERA BTQ v3]**
```
Dark cinematic editorial image, rendered with real volume and material
texture (muscle, armor, fabric) — NOT a flat silhouette cutout. Void
black background #0A0A0A.

Center composition: dramatic figure of [FIGURA PRINCIPAL], seen from
behind or at an angle — [describir la postura/acción concreta del
personaje]. Dark, moody shading with warm golden #C9A84C rim light and
ambient glow outlining the figure, like a dark statue lit from behind.

[SI APLICA — solo cuando la relación es parte central de la historia:
to one side, smaller in scale, a second figure of [FIGURA SECUNDARIA]
— creating a size contrast that tells a relationship.]

Background: concentric circles of thin gold #C9A84C line art radiating
behind the figure like a halo, framed by a geometric border pattern
drawn from the referent's own culture/era (e.g. Greek key / meander for
Ancient Greece) — subtle, like an engraved watermark, not competing
with the figure.

No circuit boards. No cartoon style. Cinematic.
```

**[BLOQUE CONGELADO — TIPOGRAFÍA + FOOTER BTQ v3]**
```
Typography:
- Top center: five small gold #C9A84C dots
- "BEHIND THE QUEUE" — ultra bold white condensed sans-serif, large
- "BTQ" — small gold below

Below silhouettes:
"[Título del episodio: referente + gancho de liderazgo]"
White text, bold

Footer black bar at bottom:
- Left: "Behind the Queue" white
- CENTER: "EP.0XX" gold #C9A84C — prominent
- Right two rows:
  Row 1: Facebook icon, Instagram icon, TikTok icon
  Row 2: Spotify icon, Apple Podcast icon, Amazon Music icon

Do NOT place any text in the bottom-right corner.
Format: square 3000x3000px.
```

**Regla de rostros:** el rostro puede verse parcialmente si la postura lo expone (de
perfil, de espaldas mostrando poco), pero no es el foco — el énfasis está en el volumen del
cuerpo/armadura y el rim light, no en el detalle facial. Persona real → mantenerlo de
espaldas/en sombra por likeness; ficticio → hay más libertad, pero seguir sin buscar el
primer plano de cara.

**Reglas de la dirección:**
1. **Número de figuras según la historia, no una regla fija.** Una sola figura protagonista
   es válida por defecto; sumar una segunda a otra escala SOLO si la relación (maestro/
   aprendiz, líder/sucesor) es parte central de la historia de ese episodio específico —
   no inventar un segundo personaje que no viene al caso.
2. **Render con volumen y textura de material, nunca silueta plana.** Músculo, armadura,
   tela con sombreado real + luz dorada de contorno — como una estatua oscura iluminada
   desde atrás, no un recorte negro liso (esa era la falla de v1).
3. **Fondo: círculos concéntricos dorados + patrón geométrico del universo del referente**
   (greca griega para Kratos; para otro referente, el patrón equivalente de esa cultura/
   época — un mosaico romano, un patrón art-deco de los 80s, etc.) en línea fina, tipo
   marca de agua, sin competir con la figura ni el texto.
4. **Conteo explícito de figuras:** "EXACTLY [N]" para cada silueta — sigue siendo el error
   más frecuente de Flow.
5. **Tipografía:** texto exacto entre comillas + "render text EXACTLY as written, letter
   by letter, no changes". Verificar letra por letra con zoom antes de aprobar. Si Flow
   genera la escena pero OMITE el texto: NO regenerar — modo edición sobre la misma imagen
   ("same image, keep everything identical, add text...").
6. **Checklist antes de aprobar:** (a) render con volumen/textura real, no silueta plana,
   (b) número de figuras justificado por la historia (no forzado a 2), (c) círculos
   concéntricos + patrón geométrico del universo correcto de fondo, (d) texto letra por
   letra, (e) footer con las 2 filas de íconos completas.

Prompt de referencia validado: EP.10 (Kratos/Atreus, Omega griego de fondo) — ver bloque de
arriba, es el prompt real usado. El primer prompt v3 aplicado a un episodio nuevo se prueba
contra Gladiator EP.019 — ver `btq-production/launch-assets/EP019-gladiator-artwork-v3-test.md`.
