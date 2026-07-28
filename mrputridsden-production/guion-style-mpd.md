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

> ## ⚠️ ESTA TABLA QUEDÓ CORTA — corregida el 2026-07-28 con la grabación de EP.006
>
> La grabación del piloto de T2 (Club de los 27) **desmintió la calibración de EP.005.** Medido con
> `ffprobe` sobre `E:\Podcast\MPD\Temporada 2\EP 01\MPD EP 01.mp3`: **5.230 palabras escritas
> produjeron 45:55 de audio**, todo habla (verificado con espectrograma — no hay música pegada).
>
> - Ritmo real compuesto: **113,9 palabras escritas por minuto** (0,008781 min por palabra).
> - La tabla de abajo asumía **128,9** palabras escritas por minuto. Se equivocaba por **13%**.
> - Consecuencia concreta: un guion de 5.543 palabras —el "target de 43 min" de la tabla vieja—
>   produce en realidad **~48,7 min**, fuera del rango editorial.
>
> **Usar esta tabla mientras haya n=2:**
>
> | Objetivo real | Palabras ESCRITAS |
> |---|---|
> | 40 min (piso) | ~4.555 |
> | 43 min (target de Andrés) | ~4.896 |
> | 45 min (techo) | ~5.124 |
>
> **Lo que NO se puede afirmar todavía:** si el desfase viene de que Andrés habla más lento en T2
> (registro más grave y pausado del formato misterio) o de que improvisa más. Para separar wpm de
> expansión hace falta el SRT, que aún no existe porque el piloto se va a regrabar. Hasta entonces
> el número compuesto es lo único medido, y es suficiente para dimensionar.

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
`dato`/`leyenda`/`recomendacion`/`nota-produccion`, que son referencia de producción y no se leen
al aire) y **multiplicar por 0,008781 para obtener minutos** — o dividir entre 113,9. Ese factor es
el ritmo compuesto medido sobre la grabación de EP.006. No usar el par 159 wpm / ×1,235: sobreestima
cuántas palabras caben.

⚠️ **Contar con script, no a ojo, y con los patrones en escapes unicode.** Las tildes se manglan al
pasar por la línea de comandos y devuelven **ceros falsos** en los greps de muletillas (mordió el
2026-07-28: el lint reportó 0 muletillas con patrones rotos). Escribir el script a disco y correrlo
desde ahí.

**Muestra: n=2** (EP.005 y el piloto de EP.006), y los dos discrepan fuerte entre sí — 128,9 vs
113,9 palabras escritas por minuto. Con dos puntos tan separados, tratar el número como provisional
y **medir la duración real de cada episodio grabado con `ffprobe`** antes de dar por buena cualquier
estimación. Al tener SRT, separar wpm de expansión. Los SRT viven en `E:\Transcriptor\transcripciones\`.

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
