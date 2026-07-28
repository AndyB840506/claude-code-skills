EPISODE: EP.024 (BTQ)
stage_a: **complete — guion APROBADO por Andy el 2026-07-28. Listo para grabar.**
stage_b: no iniciado (grabación, transcripción, assets).
stage_c: no iniciado.

## Guion — ESCRITO 2026-07-28

Archivo: `launch-assets/EP024-peter-guion.html` · Artifact:
https://claude.ai/code/artifact/b84b68c3-97d0-49e2-ae28-184e8e333740

**Título — RETITULADO 2026-07-28 con la fórmula invertida:**

```
EP.24 — Por qué su mejor empleado se vuelve un mal jefe: el Principio de Peter
```

78 caracteres (límite de YouTube: 100). Va idéntico en portada, Spotify y YouTube.
**Primer episodio con la fórmula nueva**: el problema al frente en las palabras del oyente, el
teórico detrás como autoridad. Ver `guion-style-btq.md` § Título para la evidencia que la motivó.

**Coherencia título ↔ guion (regla nueva, verificada):** la promesa se responde en el bloque DATO
del segmento 4 — «mientras más vendía la persona antes del ascenso, PEOR jefe resultó ser», con la
caída de 0,061 y el tercio de trabajador.

*Título anterior, descartado:* `EP.24 — Principio de Peter: por qué su mejor empleado se vuelve un
mal jefe` (71 car.). Mismo contenido, arrancando por un término que nadie busca.

**Esqueleto TRENZADO** (el D del menú de rotación) — primera vez que se usa. Dos hilos alternados
que no se resuelven hasta el segmento 5: A = la sátira de 1969, B = el paper de 2019. El invertido
se usó en EP.023 y el canónico sigue en pausa tras 4 usos seguidos.

**Tesis:** el ascenso no es un premio, es un cambio de oficio — y la empresa lo está usando como
sistema de pago.

| Lint | Resultado |
|---|---|
| `lint_guion_repeticion.py` vs 7 guiones | **PASS** — cero 6-gramas compartidos (primera pasada dio FAIL con 5; reescritas) |
| Duración | 5.525 palabras escritas → **42,2 min** con factor +13% (centro del estándar 40-45) |
| Muletillas | `imagínense` 0 · disclaimer de cajón 0 · puente-molde 0 |
| Moldes retirados en EP.023 | los 3 ausentes |
| Alcance | call center 0 · contact center 0 · BPO 0 |
| Tuteo | 0 |
| Remates | 3 (máximo 4) |
| Cierre canónico | las 7 piezas presentes + jingle de salida |
| Disclaimer de encuadre | 54 palabras (rango 35-55), con la mitad de «qué NO va a oír» |

**Primer episodio con disclaimer de encuadre.** Va en el segmento 0, entre el hook en frío y el
«Buenas y santas», después del jingle de entrada.

## Fuentes — todas verificadas 2026-07-28

- **Peter & Hull 1969.** La formulación exacta está corroborada por la cita del paper de QJE y
  por fuentes enciclopédicas. **El libro NO se abrió en su edición completa**: la única copia
  íntegra en línea es un escaneo sin autorización y se descartó. Jerarquiología, incompetencia
  creativa y la autoría de Hull vienen de fuentes secundarias legítimas. No hay cita textual
  larga del capítulo 1 en el guion, a propósito.
- **Benson, Li & Shue (QJE 2019).** PDF abierto y leído directamente (Open Access CC BY-NC).
  Cifras usadas: 131 empresas · 38.843 trabajadores · 1.553 ascendidos · 5.956 jefes · 2005-2011
  (Tabla I) · +0,074 pp por duplicar ventas sobre una tasa mensual de 0,0023 (Tabla II col. 2) ·
  −0,061 de valor agregado y «casi un tercio de un trabajador» sobre un equipo de 5 (Tabla III
  col. 2) · +30% de calidad gerencial en el contrafactual.
- ⚠️ **No mezclar con el working paper de 2018** (NBER w24343): otra muestra —214 empresas,
  ~53.000 trabajadores, «14% más probable»— y es la versión que repite la prensa. El «15%» que
  circula sale de ahí. El guion usa SOLO las cifras publicadas.
- **Barings/Leeson 1995** (Britannica; National Library Board de Singapur) y **McClellan/Antietam
  1862, 22.717 bajas** (American Battlefield Trust, Britannica, Encyclopedia Virginia).
- **Little 1961**, *Operations Research* 9(3):383-387 — solo para el teaser de EP.025.

## Recomendaciones tejidas (grep: ninguna usada antes)

| Medio | Cuál | Segmento |
|---|---|---|
| Libro (referente) | *The Peter Principle*, 1969 | 3 |
| Serie | *The Office* — Michael Scott | 5 |
| Charla/video | «Why Is My Boss Incompetent?», Yale Insights 2018, con video de Kelly Shue | 6 |

## Métrica de seguimiento — minutos por reproducción

Spotify **no** entrega retención dentro del episodio (confirmado con Andy 2026-07-28: el único
archivo de retención es el semana-a-semana, y es ilegible con 1-3 oyentes por semana). El proxy
que sí sale de los exports normales, y que se anota en el `pipeline-state` de CADA episodio:

```
minutos por reproducción = horas de consumo x 60 / reproducciones
```

| Episodio | Min/reproducción | Nota |
|---|---|---|
| EP.022 | ~23-28 | ventanas aproximadas, n=9 |
| EP.023 | ~20,5 | 3,41 h / 10 reproducciones, ~60% de 33,77 min |
| EP.024 | *(pendiente)* | |

Es un proxy débil con estos volúmenes — sirve por tendencia a lo largo de 4-5 episodios, no por
el valor de un episodio suelto. **Alternativa mejor si hay vistas suficientes: YouTube Studio sí
da la curva de retención minuto a minuto** del mismo audio. Revisar cuántas vistas tiene el ítem
de EP.023 antes de sacar conclusiones de ahí.

## Pendiente

- Artwork (portadas 3 formatos + quote cards): no iniciado. Las cards se componen DESPUÉS de
  grabar, contra la transcripción real.
- Grabación: dejar **3 s de silencio en cabeza y cola** (en EP.023 quedaron 0,59 s) + 30 s de
  room tone. El jingle varía respecto al de EP.023 manteniendo su formato.
- **Artículo en `/episodios/<slug>` + su `og:image`** — nuevo paso del kit desde 2026-07-28
  (ver `episode-launch/workflows/step2a-episode-article.md`). Se escribe antes del plan
  social, porque los 4 posts de LinkedIn se cortan de él; se **despliega el domingo**, junto
  con el episodio, para que el CTA de escucha tenga a dónde apuntar. Slug propuesto:
  `por-que-su-mejor-empleado-se-vuelve-un-mal-jefe` (derivado del título aprobado).
