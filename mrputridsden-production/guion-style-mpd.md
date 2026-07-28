# Guía de calibración de guion — Mr. Putrid's Den (MPD)

> Consultar SIEMPRE antes de escribir un guion nuevo de MPD (mismo patrón que
> `btq-production/guion-style-btq.md`). Creado 2026-07-17 tras el primer episodio solo grabado
> (EP.005, Aterciopelados) — antes de esto la duración se estimaba con la fórmula prestada de BTQ
> (mismo host, otro show); ya no hace falta.

---

> **PENDIENTE (decidido 2026-07-25, aplazado a la semana del 2026-08-03):** adoptar aquí la
> regla de **español neutro** que se fijó en `btq-production/guion-style-btq.md` § Español
> neutro. Andy confirmó que aplica igual a MPD (mismo público, toda Latinoamérica); se aplazó
> para cerrar BTQ primero y estrenar con EP.023. Al retomarla, leer la sección de BTQ y
> adaptarla — **no copiarla a ciegas**: MPD tiene otro registro y su propia voz.

## Calibración de duración — dimensionar en PALABRAS, no en minutos adivinados

Mismo método que BTQ/CCC: contar palabras **escritas** del guion y convertir a duración hablada
real usando el wpm y la expansión medidos de este show — no estimar minutos a ojo por segmento.

**Estándar editorial de duración (heredado de BTQ/CCC, mismo host):** 40–45 min de contenido
hablado, sin contar intro/outro musical. EP.005 fue el episodio que fijó el nuevo target de 43 min
tras la salida de Juan (ver memoria `project_mpd_juan_departure`).

**Dato real medido — EP.005 (2026-07-17, primer episodio solo, SRT real vía WhisperX):**
- Guion escrito: **4.616 palabras** (narración, sin contar bloques `dato`/`leyenda`/`recomendacion`/`nota-produccion`, que son referencia de producción, no texto leído).
- Habladas según el SRT (`E:\Transcriptor\transcripciones\MPD EP 05.srt`): **5.699 palabras**.
- Expansión real en vivo: **+23,5%** (1.235×) — menor que el +35,5% de BTQ. Andrés improvisa menos
  al alargar frases en este show que en BTQ, o el registro conversacional de MPD ya venía más
  cerca del texto escrito.
- Ritmo real de Andrés en MPD solo: **≈159 wpm** (5.699 palabras / 35,79 min de habla efectiva,
  medido desde el inicio de la Bienvenida hasta el final del Cierre, sin contar intro ni outro
  musical). Más rápido que su ritmo medido en BTQ (150 wpm) — registro/tema distinto.
- Duración real resultante: **~35,8 min**, por debajo del piso de 40 min del estándar editorial.
  El guion se quedó corto para el target de 43 min pese a que la fórmula prestada de BTQ estimaba
  ~42 min — la expansión menor (+23,5% vs +35,5% asumido) explica la diferencia.

> ## ⚠️ EL MODELO DE UNA SOLA CIFRA NO SIRVE — reemplazado el 2026-07-28
>
> **La duración de un episodio de MPD no la manda el largo del guion. La manda cuánto se pausa.**
> Eso se midió, no se supuso, y corrige un error de análisis del mismo día: al ver que el piloto de
> T2 duró 45:55 contra ~40,5 estimados se concluyó "el guion está 13% largo" y se recortó. Falso —
> el guion estaba bien; lo que cambió fue la entrega.
>
> ### Las tres variables, separadas
>
> **1. Ritmo de articulación: ~175 wpm. Es una CONSTANTE.** Medido sobre los 12 SRT reales de
> `E:\Transcriptor\transcripciones\`, contando palabras contra tiempo con voz (no contra duración
> total):
>
> | Show | n | wpm hablando | rango |
> |---|---|---|---|
> | BTQ | 8 | **176,9** | 171,2 – 191,0 |
> | MPD | 4 | **174,7** | 168,5 – 180,2 |
>
> Andrés articula igual en los dos shows y en todos los episodios. Esta cifra no se re-negocia.
>
> **2. Densidad de pausa: ES EL DIAL, y es decisión de dirección.** Medido con `silencedetect` a
> igual umbral sobre los mp3:
>
> | Episodio | % del tiempo con voz | % pausa |
> |---|---|---|
> | MPD EP.04 P1 (T1, co-host) | 86,4% | 13,6% |
> | MPD EP.04 P2 (T1, co-host) | 91,3% | 8,7% |
> | **Piloto T2 (solo, registro de misterio)** | **67,5%** | **32,5%** |
>
> Un tercio del piloto es silencio: 14,9 min de pausa en 45:55. Eso **no es un defecto** — es el
> registro pausado que pide el formato de misterio (la referencia del género, *Relatos de la Noche*,
> vive de eso). Pero hay que dimensionar el guion sabiéndolo.
>
> **3. Expansión sobre el escrito: depende de qué tan pegado al guion se lea.** El piloto se leyó
> casi textual — 31,0 min de voz × 175 wpm ≈ 5.425 habladas sobre 5.230 escritas, **expansión ≈1,04**.
> EP.005 (T1) traía ≈1,23. No es una constante del show; es cuánto improvisa según el modo.
>
> ### La fórmula
>
> ```
> minutos = (palabras_escritas × expansión) / 175 / (1 − pausa)
> ```
>
> **Palabras escritas para un episodio de 43 min**, según cómo se vaya a leer (expansión 1,04, modo
> leído):
>
> | Densidad de pausa | Palabras ESCRITAS |
> |---|---|
> | 32% (pausado, como el piloto) | **~5.000** |
> | 20% (intermedio) | ~5.800 |
> | 13% (ágil, como T1) | ~6.300 |
>
> **Decidir el registro ANTES de dimensionar el guion.** Un mismo guion de 5.000 palabras dura 44
> min pausado y 35 min ágil — nueve minutos de diferencia sin tocar una sola palabra.

<details>
<summary><strong>Tabla anterior (EP.005 — wpm 159,2 / expansión 1,235). Superada, se conserva como registro.</strong></summary>

| Objetivo real | Palabras habladas | Palabras ESCRITAS |
|---|---|---|
| 40 min (piso del estándar) | ~6.368 | ~5.156 |
| 42.5 min (centro del estándar) | ~6.766 | ~5.479 |
| 43 min (target fijado por Andrés) | ~6.846 | ~5.543 |
| 45 min (techo del estándar) | ~7.164 | ~5.801 |

</details>

**Cómo medir (actualizado 2026-07-28):** contar palabras de los bloques `host-text` únicamente (no
`dato`/`leyenda`/`recomendacion`/`nota-produccion`, que son referencia de producción y no se leen al
aire) y aplicar la fórmula de arriba con la densidad de pausa que se vaya a usar. No usar el par
159 wpm / ×1,235 de EP.005: mezcla articulación con pausa y da un número que solo vale para ese
episodio.

### Prueba de pausa — hacer esto ANTES de dimensionar un guion nuevo

Grabar **un bloque de prueba** (2-3 minutos bastan) leyendo como se va a leer el episodio, y medirlo:

```
ffprobe -v error -show_entries format=duration -of csv=p=0 "prueba.mp3"
ffmpeg -hide_banner -i "prueba.mp3" -af "silencedetect=noise=-40dB:d=0.35" -f null - 2>&1 \
  | grep -o "silence_duration: [0-9.]*" | awk '{s+=$2} END {print "silencio total:", s, "seg"}'
```

`% pausa = silencio / duración`. Con ese número y la fórmula sale el largo del guion. Es la única
forma de no estar adivinando: dos entregas del mismo texto se separan hasta nueve minutos.

⚠️ **El umbral importa.** A −35 dB el piloto da 63,8% con voz y a −40 dB da 67,5%. Usar **siempre
−40 dB** para que las cifras sean comparables entre episodios, y no comparar nunca una medición de
`silencedetect` contra una derivada de SRT — son instrumentos distintos.

⚠️ **Contar con script, no a ojo, y con los patrones en escapes unicode.** Las tildes se manglan al
pasar por la línea de comandos y devuelven **ceros falsos** en los greps de muletillas (mordió el
2026-07-28: el lint reportó 0 muletillas con patrones rotos). Escribir el script a disco y correrlo
desde ahí.

**Estado de la muestra:** la articulación (~175 wpm) tiene n=12 y es sólida. La **expansión** tiene
n=2 y los dos puntos están lejos (1,23 en EP.005 vs 1,04 en el piloto de T2) — depende del modo de
lectura, así que no promediarlos. La **densidad de pausa** de T2 tiene n=1 y es justo la variable
que más manda: por eso la prueba de pausa de arriba, en vez de confiar en una tabla.

Cuando exista el SRT de la regrabación, recalcular expansión y pausa y subir T2 a n=2. Los SRT viven
en `E:\Transcriptor\transcripciones\`.

---

## Loudness — targets de máster (medidos sobre el piloto de EP.006, 2026-07-28)

El piloto salió **−25,8 LUFS integrado, LRA 15,1, true peak −2,1 dBFS**. Está ~10 LU por debajo del
estándar de podcast, y con un rango dinámico del doble de lo normal para voz hablada. Peor: la
mitad del episodio se hunde — por tramos dio −20,4 → −24,5 → −27,8 → **−29,2** → −19,6 LUFS, casi
10 LU de deriva entre el centro y los extremos.

| Métrica | Piloto | Target |
|---|---|---|
| Integrado | −25,8 LUFS | **−16 LUFS** (Spotify normaliza a −14) |
| LRA | 15,1 LU | **~6 LU** |
| True peak | −2,1 dBFS | ≤ −1 dBFS ✓ |

**Verificar antes de publicar cualquier episodio:**

```
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 "archivo.mp3"
ffmpeg -hide_banner -i "archivo.mp3" -af ebur128=peak=true -f null -
```

---

## Nota de transcripción — artefacto de intro

El primer segmento del SRT de EP.005 (00:00:00–00:00:24) transcribió el intro musical (voz
femenina gutural) como una cadena larga de "Aaaa..." — es un artefacto esperado de WhisperX al
oír música/vocalización no hablada, no un error de la grabación. Excluir ese segmento (y el
segmento final con la letra del outro cantado) al contar palabras habladas para calibración.
