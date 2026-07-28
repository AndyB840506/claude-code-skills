# Apertura fija de Mr. Putrid's Den — T2

> Decisiones del 2026-07-24 (estudio de mercado + feedback de círculo cercano). El logo sonoro y el
> disclaimer son **bumpers fijos reutilizables**: se producen UNA vez y se pegan en cada episodio.

**Orden de apertura:** `Logo sonoro (3–5s) → Disclaimer → Intro music → Bienvenida (Andrés)`.
El logo va primero porque el branding sonoro dice que la firma debe ser el primer sonido que se oye.

## Estado de producción (2026-07-28, confirmado por Andrés)

| Pieza | Estado |
|---|---|
| Disclaimer (ElevenLabs) | ✅ **hecho** |
| Música de intro | ✅ **hecha** |
| Logo sonoro (3–5 s) | ⬜ **pendiente** — único bloqueante de la apertura fija; brief en §2 |

> Los archivos de audio resultantes no están registrados acá — al retomar, pedirle a Andrés la ruta
> exacta antes de asumir dónde quedaron.

---

## 1. Disclaimer (texto fijo) — VERSIÓN CORTA, decidida 2026-07-28

**28 palabras, ~15 segundos.** Reemplaza la versión de 88 palabras (~50 s) tras el feedback del
piloto: la prueba de 0:40 que Andrés mandó **seguía siendo larga** ("pa mi sigue siendo largo").
Se conserva lo único irremplazable —el contrato dato-vs-leyenda y "la última palabra será suya"—
y se corta la enumeración de "historias, mitos, y todo lo que quedó sin explicación", que era
donde vivía el tiempo muerto.

```
Bienvenido a la Guarida.

Aquí se abren los expedientes que la música dejó sin cerrar.

El mito no se vende como verdad. La última palabra siempre será suya.
```

- **SIN `[whispers]`.** Se dice normal, en voz grave. El susurro se retiró por completo: el
  feedback fue "el susurro al inicio… mejor decirlo normalmente" y "es poco serio". *(La versión
  anterior ya había bajado de mucho susurro a un solo `[whispers]` inicial; esto lo lleva a cero.)*
- La gravedad la da la voz y el ritmo, no el susurro ni las pausas largas.
- Sin mayúsculas de énfasis: grave y bajo, no fuerte.
- Sirve igual en v3 o en Multilingual v2 — al ser tan corto ya no necesita `<break>` tags.

<details>
<summary>Versión larga anterior (88 palabras, ~50 s) — retirada 2026-07-28</summary>

Se conserva como registro de por dónde pasó la apertura, no como opción.

```
[whispers] Bienvenido a la Guarida.

Aquí, cuando cae la noche, se abren los expedientes que la música dejó sin cerrar... y de vez en cuando, otros que el tiempo prefirió olvidar. Historias, mitos... y todo lo que quedó sin explicación.

Le vamos a contar la leyenda completa. Pero recuerde una cosa... aquí el mito no se vende como verdad. Lo que es dato, será dato. Lo que es leyenda... se queda como leyenda.

La última palabra... siempre será suya.

Baje las luces. El expediente ya está sobre la mesa.
```

</details>

---

## 1.b Feedback del piloto (círculo cercano, 2026-07-25) — fuente de los cambios de arriba

Estaba solo en WhatsApp; se transcribe acá para que no se pierda.

**Valida (no tocar):** el tono y el approach — *"me gusta, pq es mi estilo, tipo, oscuro, un poco
macabro… está genial el approach"*. El alcance abierto — *"tendrías apertura para hablar de lo q
sea, invitar a quien sea"*. Y los bumpers fijos — *"creo q algo diferente en cada capítulo es como
raro"*.

**Pide cambiar — todo en la apertura, nada en el cuerpo narrado:**
- *"tal vez el intro y el outro son muy largos"*
- *"el susurro al inicio, creo q tal vez quería mejor, like, decirlo normalmente"* / *"es poco serio"*
- Sobre la prueba de 0:40: *"pa mi sigue siendo largo"*
- *"me parece chevere un opening que sea corto y pegajoso, q uno se lo pueda aprender… q tu lo
  escuches y de una ya lo relaciones con el podcast"* → **esto es exactamente el logo sonoro.**

**Dos advertencias al leer este feedback:**
1. Elogia el **intro** de Leyendas Legendarias (*"esa vaina no se le olvida a uno jamás"*), **no su
   tono**. El canon rechaza a propósito la comedia de LL y eso sigue en pie — no leer esto como
   "hagámoslo tipo LL".
2. Ella se declara fuera del target: *"a mí en particular ya no me llaman este tipo de contenidos
   pq en alguna época lo consumí demasiado"*. Su feedback de oficio (duración, memorabilidad,
   marca sonora) pesa mucho; su "no me engancha" pesa poco. No sobre-corregir hacia una oyente que
   avisó que no es la oyente.

Norte que ella misma mandó: **Relatos de la Noche** — la misma referencia que ya estaba en canon.
Ojo: esa tutea ("¿te atreves a escuchar?") y MPD usa **usted**. Eso no se copia.

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

## 3. Música de intro — RECORTAR (feedback 2026-07-25: "el intro y el outro son muy largos")

**Target nuevo: ~15-20 s**, no 40-45. Cuenta la suma, no cada pieza: con el disclaimer viejo la
apertura llegaba a **~85 s antes de la primera palabra de Andrés** (logo 3-5 s + disclaimer ~50 s +
música ~30 s). Con el disclaimer corto y la música recortada baja a **~35 s**, que es lo que la
apertura fija debería costar.

El outro también se recorta (ver §Outro abajo). La estructura de ~40 s que sigue es la del brief
original — usarla como paleta y como guía de progresión, pero **entregando en 15-20 s**.

### Brief original (cama corta, máx 45 s)

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
