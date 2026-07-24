# Apertura fija de Mr. Putrid's Den — T2

> Decisiones del 2026-07-24 (estudio de mercado + feedback de círculo cercano). El logo sonoro y el
> disclaimer son **bumpers fijos reutilizables**: se producen UNA vez y se pegan en cada episodio.

**Orden de apertura:** `Logo sonoro (3–5s) → Disclaimer → Intro music → Bienvenida (Andrés)`.
El logo va primero porque el branding sonoro dice que la firma debe ser el primer sonido que se oye.

---

## 1. Disclaimer (texto fijo)

Alcance híbrido (ya no solo "el rock") y **menos whisper** que la primera prueba — la gravedad la da
la voz, no el susurro (feedback: "tanto whisper suena poco serio").

### Versión Eleven v3 (recomendada — audio tags)

```
[whispers] Bienvenido a la Guarida.

Aquí, cuando cae la noche, se abren los expedientes que la música dejó sin cerrar... y de vez en cuando, otros que el tiempo prefirió olvidar. Historias, mitos... y todo lo que quedó sin explicación.

Le vamos a contar la leyenda completa. Pero recuerde una cosa... aquí el mito no se vende como verdad. Lo que es dato, será dato. Lo que es leyenda... se queda como leyenda.

La última palabra... siempre será suya.

Baje las luces. El expediente ya está sobre la mesa.
```

- Un solo `[whispers]` al inicio (menos susurro). Las pausas van con "..." (v3 no usa `<break>`).
- Sin mayúsculas de énfasis: queremos grave y bajo, no fuerte.

### Versión Multilingual v2 (fallback — break tags)

```
Bienvenido a la Guarida. <break time="0.6s"/> Aquí, cuando cae la noche, se abren los expedientes que la música dejó sin cerrar... y de vez en cuando, otros que el tiempo prefirió olvidar. <break time="0.6s"/> Historias, mitos, y todo lo que quedó sin explicación. <break time="0.7s"/> Le vamos a contar la leyenda completa. <break time="0.4s"/> Pero recuerde una cosa: <break time="0.5s"/> aquí el mito no se vende como verdad. Lo que es dato, será dato. Lo que es leyenda... se queda como leyenda. <break time="0.7s"/> La última palabra siempre será suya. <break time="0.5s"/> Baje las luces. <break time="0.4s"/> El expediente ya está sobre la mesa.
```

### Ajustes ElevenLabs (puntos de partida, afinar de oído)

- **Modelo:** v3 (recomendado) o Multilingual v2 (mejor normalización en español).
- **Voz:** grave, madura, con aire. Voice Library (male · deep · mature · narration) o Voice Design con:
  > *A deep, resonant middle-aged male voice speaking slowly and intimately, low and close to the mic. Mysterious and calm with a faint eerie edge — a late-night radio host telling a story by firelight. Warm but haunting, subtle gravel. Not theatrical, not whispery.*
- **v3:** Stability = Natural · Speed ~0.85. **v2:** Stability ~50 · Similarity ~80 · Style ~15.
- Si un `[whispers]` se cuela hablado, bórralo de esa toma.

---

## 2. Logo sonoro (firma de marca, 3–5 s)

Motivo corto, memorable y **fijo** — lo primero que suena. Debe ser reconocible al instante y contener
la frase de 3–5 s que se repita en toda variante. Eerie pero pegajoso; no un jingle largo.

**Brief:** un gesto sonoro breve que "abra la puerta de la Guarida" — p. ej. una nota grave de piano
desafinado + un roce de cuerda frotada + crepitar de vinilo que se apaga. Frío, con un solo destello
cálido de guitarra. Sin coros, sin campanas, sin clichés de horror.

---

## 3. Música de intro (cama corta, máx 45 s)

Lúgubre e incómodo pero magnético — la incomodidad viene de la TENSIÓN sin resolver, no de clichés.
Espacioso, no denso (arregla el "muy lleno" de la iteración `La_Grieta_del_Mito`).

**Prompt (para MusicFX / Lyria / Suno / Udio — en inglés):**

```
Instrumental, no vocals. A short, eerie intro for a mystery/legends podcast — gloomy and
unsettling, yet magnetic, pulling the listener in. Sparse and spacious, with lots of silence and
room tone. Slow, around 66 BPM, over a low heartbeat-like sub-bass pulse. Detuned prepared piano
playing single hesitant notes; a low bowed double-bass drone with a faint dissonant, unresolved
edge; shimmering bowed-glass overtones; reversed reverb swells; faint vinyl crackle and distant
creaks. Cold and haunting, with a single warm guitar note emerging late, like an ember. It builds
slow dread that does NOT fully resolve — it leans forward, inviting you in. Cinematic, restrained,
hypnotic. NO choirs, NO church organ, NO orchestral horror stabs, NO tolling bells, NO screams,
NO heavy metal.
```

**Estructura (~40 s):** 0–8s casi silencio + nota desafinada + pulso; 8–25s drone disonante + swells;
25–40s motivo hipnótico + brasa de guitarra, **tensión sin cerrar** que entrega al show.

**Outro:** misma paleta, más cálida, resuelve en un acorde sostenido con fade de vinilo, ~20 s.
