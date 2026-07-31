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
> **1. Ritmo de articulación: ~168 wpm.** Medido sobre los 13 SRT reales de
> `E:\Transcriptor\transcripciones\` con `wpm.py`, contando palabras contra tiempo con voz (no contra
> duración total):
>
> | Show | n | wpm hablando | rango |
> |---|---|---|---|
> | BTQ | 8 | **167,3** | 162,8 – 178,9 |
> | MPD | 5 | **168,2** | 158,4 – 180,2 |
> | **Global** | **13** | **167,6** | 158,4 – 180,2 |
>
> Andrés articula parecido en los dos shows. Pero el rango es ±6%, así que **no es una constante
> dura**: sirve para dimensionar, no para predecir un episodio concreto al minuto.
>
> ⚠️ **Corrección del 2026-07-28 (segunda de ese día).** La cifra anterior — «~175 wpm, constante,
> no se re-negocia» — era un **artefacto del medidor**. `wpm.py` contaba la etiqueta de diarización
> `[SPEAKER_00]:` como palabra hablada, porque pasa el filtro de «contiene letras». Infla entre
> **3,6% y 8,6%** según cuántos segmentos tenga el archivo. Corregido en `wpm.py` ese mismo día; los
> números de arriba ya son los limpios. Cualquier cifra de wpm anterior al 2026-07-28 está inflada.
>
> **2. Densidad de pausa: ES EL DIAL, y es decisión de dirección.** Medido con `silencedetect` a
> igual umbral sobre los mp3:
>
> | Episodio | % del tiempo con voz | % pausa |
> |---|---|---|
> | MPD EP.04 P1 (T1, co-host) | 86,4% | 13,6% |
> | MPD EP.04 P2 (T1, co-host) | 91,3% | 8,7% |
> | Piloto T2 (solo, descartado — se regrabó) | 67,5% | 32,5% |
> | **T2·01 publicable (solo, regrabado 2026-07-28)** | **73,3%** | **26,7%** |
>
> Un tercio del piloto es silencio: 14,9 min de pausa en 45:55. Eso **no es un defecto** — es el
> registro pausado que pide el formato de misterio (la referencia del género, *Relatos de la Noche*,
> vive de eso). Pero hay que dimensionar el guion sabiéndolo.
>
> **3. Expansión sobre el escrito: depende de qué tan pegado al guion se lea.** El piloto se leyó
> casi textual. La cifra que se escribió aquí el 2026-07-28 —«31,0 min × 175 wpm ≈ 5.425 habladas
> sobre 5.230 escritas, expansión ≈1,04»— **quedó mal por arrastre de la constante inflada**: con los
> 167,6 correctos son ≈5.196 habladas, **expansión ≈0,99**. Y era una cifra *derivada*, no medida: el
> piloto se descartó y nunca tuvo SRT. Usar el punto medido de T2·01 (1,087), no este.
> EP.005 (T1) traía ≈1,23. No es una constante del show; es cuánto improvisa según el modo.
>
> ### La fórmula
>
> ```
> minutos = (palabras_escritas × expansión) / 167,6 / (1 − pausa_SRT)
> ```
>
> 🚨 **LOS DOS INSTRUMENTOS NO SE MEZCLAN — y la versión anterior de esta fórmula los mezclaba.**
> El wpm sale del SRT; la pausa se puede medir con `silencedetect` **o** con el SRT, y dan números
> distintos sobre el mismo audio. Meter la pausa de `silencedetect` en una fórmula cuyo wpm vino del
> SRT infla el resultado ~8%: sobre T2·01 predecía **45,2 min** para un episodio que dura **41,8**.
>
> | Instrumento | Pausa en T2·01 | Con qué wpm se usa |
> |---|---|---|
> | SRT (`1 − voz/total` del propio SRT) | **22,2%** | ✅ con los 167,6 de la tabla |
> | `silencedetect` −40 dB | **26,7%** | ❌ nunca con esos 167,6 |
>
> Conversión medida sobre T2·01: **pausa_silencedetect ≈ pausa_SRT + 4,5 puntos**. Sirve para la
> prueba de pausa de más abajo, que se hace antes de grabar y por tanto no tiene SRT: se mide con
> `silencedetect` y se le restan ~4,5 puntos antes de meterla a la fórmula.
>
> **Palabras escritas para un episodio de 43 min**, según cómo se vaya a leer (expansión 1,09, modo
> leído; pausa en términos de SRT):
>
> | Densidad de pausa (SRT) | Palabras ESCRITAS |
> |---|---|
> | 22% (pausado, como T2·01) | **~5.150** |
> | 17% (intermedio) | ~5.500 |
> | 12% (ágil, como T1) | ~5.800 |
>
> Precisión esperada: **±3%**. La fórmula con la constante global da 42,6 min para T2·01 contra los
> 41,8 reales, porque ese episodio articuló 172,1 (2,7% sobre la media). Es una herramienta de
> dimensionado, no un cronómetro.
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

**Estado de la muestra (actualizado 2026-07-28 con el SRT de la regrabación — T2 ya está en n=2):**
la articulación (167,6 wpm) tiene n=13 pero rango ±6%, así que se usa para dimensionar, no para
predecir. La **expansión** tiene n=3 y los puntos siguen lejos (1,23 en EP.005 · 1,04 en el piloto ·
**1,087 en T2·01**) — depende del modo de lectura, así que no promediarlos. La **densidad de pausa**
de T2 ya tiene n=2 (32,5% piloto → 26,7% regrabación) y sigue siendo la variable que más manda: por
eso la prueba de pausa de arriba, en vez de confiar en una tabla.

### Punto de calibración — T2·01 «El Club de los 27» (regrabado 2026-07-28)

| | |
|---|---|
| Escritas (`host-text` + el bloque `dato` que se leyó) | **5.108** |
| Habladas (SRT limpio, sin etiquetas de speaker) | **5.552** |
| Expansión | **1,087** |
| Articulación | **172,1 wpm** |
| Pausa (SRT / `silencedetect` −40 dB) | **22,2% / 26,7%** |
| Duración final | **41:47** |

⚠️ **Ojo al contar lo escrito: se leyó un bloque `dato` al aire** (el de Alan Wilson, 76 palabras).
No fue descuido de lectura — ver § Bloques que no se leen, abajo. Si se cuentan solo los `host-text`
(5.036) la expansión sale 1,102 en vez de 1,087; la diferencia es menor, pero el conteo honesto
incluye lo que de verdad se leyó.

---

## Loudness — targets de máster (medidos sobre el piloto de EP.006, 2026-07-28)

El piloto salió **−25,8 LUFS integrado, LRA 15,1, true peak −2,1 dBFS**. Está ~10 LU por debajo del
estándar de podcast, y con un rango dinámico del doble de lo normal para voz hablada. Peor: la
mitad del episodio se hunde — por tramos dio −20,4 → −24,5 → −27,8 → **−29,2** → −19,6 LUFS, casi
10 LU de deriva entre el centro y los extremos.

| Métrica | Piloto | T2·01 entregado | Target |
|---|---|---|---|
| Integrado | −25,8 LUFS | **−16,0 LUFS** ✅ | **−16 LUFS** (Spotify normaliza a −14) |
| LRA | 15,1 LU | **6,5 LU** ✅ | **~6 LU** |
| True peak | −2,1 dBFS | **−1,2 dBFS** ✅ | ≤ −1 dBFS |

**Verificar antes de publicar cualquier episodio:**

```
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 "archivo.mp3"
ffmpeg -hide_banner -i "archivo.mp3" -af ebur128=peak=true -f null -
```

### Cómo se llegó al target en T2·01 (2026-07-28)

El render crudo de Reaper salía a **−18,3 LUFS con true peak +0,1 dBFS** — o sea, por debajo del
estándar **y** clipeando a la vez. La causa: el limitador del máster topaba a 0,0 dBFS de pico de
muestra, y el encode a MP3 genera overs inter-muestra por encima de eso.

Se corrigió **fuera de Reaper**, sobre el WAV, para que sea determinista y medible:

```
ffmpeg -i "EP.wav" -af "volume=3.2dB,alimiter=limit=0.7943:attack=2:release=80:level=0" \
  -c:a libmp3lame -b:a 128k -ar 44100 -ac 2 "EP MASTER.mp3"
```

- `limit=0.7943` = **−2,0 dBFS** de techo, que tras el encode aterriza en −1,2 a −1,7 dBTP.
- `attack=2:release=80` importa: con `attack=5:release=50` el mismo archivo perdió 0,8 LU y quedó
  en −16,8. Ataque más rápido controla mejor el pico **y** pierde menos nivel medio.
- `level=0` desactiva la auto-nivelación del limitador, que si no pisa la ganancia de `volume`.
- **Renderizar de Reaper a WAV, no a MP3** — así el MP3 se codifica una sola vez.

El LRA solo bajó de 6,6 a 6,5: el limitador trabaja los picos, no aplasta la dinámica. Si una
corrida futura baja el LRA más de ~0,5 LU, la ganancia es demasiada.

---

## Bloques que no se leen — el guion tiene que hacerlos imposibles de leer por error

**Mordió el 2026-07-28 y llegó hasta el máster.** En T2·01 se grabó al aire esta frase:

> «Todas las cifras de este bloque quedaron confirmadas contra la cobertura del estudio. No quedan
> estimados sin respaldo.»

Eso es contabilidad de verificación, no narración. Hubo que cortar 7,9 s del episodio ya grabado.

**La causa NO fue descuido de lectura.** La frase estaba correctamente clasificada dentro de un
bloque `class="dato"` — o sea, el guion la había etiquetado bien como referencia de producción. El
problema es que **los bloques `dato` y `leyenda` se renderizan intercalados en el flujo de lectura**,
entre dos bloques de narración, y leyendo de corrido no se distinguen. La prueba de que es
estructural y no humano: en el mismo episodio se leyó al aire **otro** bloque `dato` completo (el de
Alan Wilson, 76 palabras) sin que nadie lo notara, porque ese sí sonaba a contenido.

**Reglas, hasta que el render del guion se arregle:**

1. **Nada de contabilidad de verificación dentro de `dato` o `leyenda`.** Los marcadores
   `verificado <fecha>`, «confirmado contra X», «no quedan estimados sin respaldo» van en
   `nota-produccion`, que sí está visualmente separado y **ninguno de los 11 se leyó al aire**.
2. **`dato` y `leyenda` son para material que el host DECIDE si usa.** Si un dato tiene que sonar en
   el episodio, va escrito como narración en `host-text`, no como referencia.
3. **Antes de grabar, correr el lint de bloques:** verificar que ningún `dato`/`leyenda` contenga
   lenguaje de producción. El script que lo detecta está en la retrospectiva del 2026-07-28.
4. **Después de grabar, cruzar el SRT contra los bloques no-narrativos** para ver cuáles se leyeron.
   Es una comprobación de 10 segundos y es la única que agarra esto antes de publicar.

---

## Verificar las fuentes ANTES de escribir, no después

**Decisión de Andrés, 2026-07-28.** Ningún dato entra a un guion de MPD sin fuente verificada de
primera mano. No se escribe primero y se verifica después: para cuando el guion está grabado, un
dato malo cuesta una regrabación, no una edición de texto.

Qué salió bien y qué no en T2·01, como referencia de cuánto vale esto:

- **Las 8 fechas del racimo salieron correctas** (Jones 3-jul-69 · Wilson 3-sep-70 · Hendrix
  18-sep-70 · Joplin 4-oct-70 · Morrison 3-jul-71 · Winehouse 23-jul-11 · Johnson 16-ago-38), y el
  estudio del BMJ cuadró verbatim en las seis cifras que se citan. Pero **se verificaron después de
  grabar**, no antes — si una hubiera fallado, tocaba regrabar.
- **La de Cobain se resolvió sola por prudencia:** al aire se dice «abril del 94» sin día, lo que
  esquiva la trampa real (murió el 5, lo encontraron el 8). **Cuando una fecha tiene disputa
  documentada, decir el mes y no el día es una salida legítima**, no una debilidad.
- **La única floja quedó publicada:** «3 de marzo del 94 en Roma». Las fuentes se reparten entre el
  3 y el 4 y lo más común es que lo encontraron la madrugada del 4. Nadie la había marcado porque
  no estaba en la lista de `[VERIFICAR]` — **se verificó lo que el guion se acordó de marcar, no
  todo lo que afirmaba.**

**Por eso la regla no es «verificar los marcadores», es esta:**

1. **Toda fecha, cifra, cita y atribución** que el guion afirme necesita fuente antes de escribirse.
   No solo las que alguien marcó — la lista de marcadores es justamente lo que ya se sospechaba.
2. **Nombrar la fuente en el bloque `nota-produccion`**, con fecha de consulta. Si no se puede
   nombrar una fuente real, el dato no entra: se reformula o se corta.
3. **Cuando las fuentes se contradicen, decirlo en el guion** en vez de elegir en silencio. En T2·01
   esto ya se hizo bien con la frase de la mamá de Cobain — se cuentan las tres lecturas en vez de
   darla como acta de fundación. Ese es el patrón a repetir.
4. **Bajar la precisión es una herramienta válida.** Mes en vez de día, «unas 50 pastillas» en vez
   de un número exacto. Es preferible a afirmar de más.
5. **Re-abrir las fuentes JUSTO ANTES de grabar**, aunque ya se verificaran al escribir. El sello
   «verificado» de una sesión anterior es hipótesis, no hecho. Mordió en BTQ el 2026-07-31: un
   guion aprobado tres días antes y marcado como verificado tenía dos errores. Ver
   [[feedback_verify_sources_before_recording]].

### Las cifras van en NÚMERO, no en letras (regla de Andrés, 2026-07-31)

`827 millones`, no «ochocientos veintisiete millones». Andrés lee en voz alta y el numeral se
parsea más rápido — pero la razón fuerte es otra: **en letras, las cifras se escapan de los
lints**, porque cualquier extractor filtra por dígitos y no las ve. Ese día, en BTQ EP.024, la
primera pasada de verificación revisó 46 bloques y **no tocó ninguno de los 16 que traían la
cifra escrita en palabras** — dentro había un «cincuenta y seis años» que eran 57.

**Excepción:** expresiones idiomáticas y nombres de conceptos, donde el numeral suena raro leído
(«medio siglo después», «las cinco etapas del duelo»). La prueba: ¿es un **dato** verificable o
una **forma de hablar**? Dato → numeral.

---

## Nota de transcripción — artefacto de intro

El primer segmento del SRT de EP.005 (00:00:00–00:00:24) transcribió el intro musical (voz
femenina gutural) como una cadena larga de "Aaaa..." — es un artefacto esperado de WhisperX al
oír música/vocalización no hablada, no un error de la grabación. Excluir ese segmento (y el
segmento final con la letra del outro cantado) al contar palabras habladas para calibración.

**Los timestamps se corren cerca de la música.** En T2·01 el SRT fechó la primera frase del cuerpo
en **28,5 s** cuando el cuerpo arranca en **35,5 s** — el alineador arrastró el segmento ~8 s hacia
dentro de la música de intro. El final del episodio en cambio cuadró al segundo. **Los timestamps
dentro del cuerpo son confiables; los que caen junto a música, no.** Si un timestamp del arranque
decide algo, verificarlo contra el envolvente del audio (`ebur128` con `framelog`), no contra el SRT.

**Las etiquetas `[SPEAKER_00]:` no son palabras.** Ver la corrección de la constante de articulación
más arriba. `wpm.py` ya las excluye desde el 2026-07-28; cualquier script nuevo que cuente palabras
sobre un SRT diarizado tiene que hacer lo mismo.

**Para verificar una palabra concreta, re-transcribir el fragmento aislado.** Extraer 20-30 s con
`ffmpeg -ss` y correr WhisperX solo sobre eso quita el sesgo de contexto y funciona como segundo
instrumento. Así se confirmó en T2·01 que «en menos de un año» (donde el guion decía «dos años») y
«21.700» (donde decía «21.750») eran errores de lectura reales y no fallos de transcripción.
