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

## Dirección de artwork (CONGELADA 2026-06-12 — validada con EP.017 Soda Stereo)

**BTQ = póster gráfico/editorial.** Pieza de diseño con siluetas a contraluz — NUNCA
fotograma cinematográfico fotorrealista. Si una imagen podría pasar por portada de MPD
(film still crimson/dorado), falló. El referente cultural rota cada episodio y se muestra
FIEL A SU ÉPOCA (principio de nostalgia); el marco negro+dorado nunca cambia — eso es lo
que la audiencia reconoce en la grilla.

Bloques que se copian VERBATIM en todo prompt de portada (solo cambia el sujeto central):

**[BLOQUE CONGELADO — ATMÓSFERA BTQ]**
```
Graphic editorial poster design with strong backlit silhouettes —
NOT photorealistic 3D. The subjects read as pure black shapes with thin
golden rim light (#C9A84C) on their edges, against a wall of warm golden
stage light (#C9A84C) with haze and smoke forming a glowing halo.
NO visible face detail on anyone — solid silhouettes and rim light only.
Era-correct hair, clothing and props for the cultural referent's decade.
Analog film grain, slight halation on the lights, muted retro color
grading, screen-print poster texture. No modern elements.
BACKGROUND: void black #0A0A0A dominates the top and bottom of the image.
```

**[BLOQUE CONGELADO — FOOTER BTQ]**
```
FOOTER: full-width strip at the very bottom, on the void black background.
  Left: "Behind the Queue" in small white sans-serif
  Center: "EP.0XX" in bold signal gold #C9A84C
  Right: small silver platform icons — Spotify (circle with three curved
  lines) and YouTube (rounded rectangle with play triangle)
```

**Reglas de la dirección:**
1. **Conteo explícito de figuras:** si el referente es una banda/grupo, escribir
   "EXACTLY [N] people, no more, no less" y describir la pose de cada uno — es el error
   más frecuente de Flow. Verificar el conteo antes de aprobar.
2. **Cero rostros** — siluetas sólidas con rim light (likeness de personas reales + Flow
   daña caras).
3. **Tipografía:** texto exacto entre comillas + "render text EXACTLY as written, letter
   by letter, no changes". Máximo ~5 palabras por línea. Evitar tildes/eñes en el texto
   dentro de la imagen cuando haya alternativa (la frase completa con tildes va en el
   caption del post); verificar letra por letra con zoom antes de aprobar.
   Si Flow genera la escena pero OMITE el texto (pasó con el thumbnail EP.017): NO
   regenerar — se pierde la escena aprobada. Modo edición sobre la misma imagen:
   "On this same image, keep everything identical and add text..." + las líneas exactas.
4. **Checklist antes de aprobar:** (a) conteo de figuras correcto, (b) texto letra por
   letra, (c) cero caras + estética fiel a la época del referente (sin LEDs, smartphones,
   in-ears si la era no los tenía).
5. **El referente en escena, no implícito (feedback EP.017):** las portadas llevan al
   sujeto/banda presente y en acción — el concepto abstracto ("micrófono solo",
   "escenario vacío") se percibe simplón como portada. Lo abstracto se reserva para
   teasers de INTRIGA, donde no revelar es el objetivo. (Regla hermana de la #5 del
   workflow 03-artwork de MPD, confirmada allá desde EP.003.)

Prompt de referencia validado: portada EP.017 (trío en silueta contra pared de luz dorada).
