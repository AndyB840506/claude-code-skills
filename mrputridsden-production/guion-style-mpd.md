# Guía de calibración de guion — Mr. Putrid's Den (MPD)

> Consultar SIEMPRE antes de escribir un guion nuevo de MPD (mismo patrón que
> `btq-production/guion-style-btq.md`). Creado 2026-07-17 tras el primer episodio solo grabado
> (EP.005, Aterciopelados) — antes de esto la duración se estimaba con la fórmula prestada de BTQ
> (mismo host, otro show); ya no hace falta.

---

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

**Tabla de dimensionamiento (recalibrada con datos reales de EP.005 — wpm 159,2 / expansión 1,235):**

| Objetivo real | Palabras habladas | Palabras ESCRITAS |
|---|---|---|
| 40 min (piso del estándar) | ~6.368 | ~5.156 |
| 42.5 min (centro del estándar) | ~6.766 | ~5.479 |
| 43 min (target fijado por Andrés) | ~6.846 | ~5.543 |
| 45 min (techo del estándar) | ~7.164 | ~5.801 |

**Cómo medir:** contar palabras de los bloques `host-text` únicamente (no `dato`/`leyenda`/
`recomendacion`/`nota-produccion`, que son referencia de producción, no se leen al aire),
multiplicar por 1.235 (expansión verificada) y dividir por 159 (wpm verificado). Marcar los
tiempos de la arquitectura en consecuencia.

**Muestra: n=1.** Esta es la primera calibración real de MPD solo — recalibrar (wpm y expansión)
contra el SRT de los próximos 2-3 episodios grabados, igual que BTQ ajustó de 143→150 wpm tras
más datos. Los SRT viven en `E:\Transcriptor\transcripciones\`.

---

## Nota de transcripción — artefacto de intro

El primer segmento del SRT de EP.005 (00:00:00–00:00:24) transcribió el intro musical (voz
femenina gutural) como una cadena larga de "Aaaa..." — es un artefacto esperado de WhisperX al
oír música/vocalización no hablada, no un error de la grabación. Excluir ese segmento (y el
segmento final con la letra del outro cantado) al contar palabras habladas para calibración.
