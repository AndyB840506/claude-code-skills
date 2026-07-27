# BTQ — Brief del jingle (stinger de marca)

**Decisión:** 2026-07-25. Reemplaza la música de intro/outro. Ver `guion-style-btq.md` § Jingle.

---

## Especificación dura

| | |
|---|---|
| Duración | **2 a 4 segundos.** Si pasa de 5, no es un stinger, es una intro. |
| Uso | **El mismo** al abrir y al cerrar. Es una firma sonora, no dos piezas. |
| Final | Termina **seco**, en silencio. Sin fade largo, sin cola de reverb. |
| Relación con la voz | **Nunca por debajo del habla.** Termina, y después entra Andy. |
| Formato | WAV 48 kHz para editar; el MP3 sale del render final del episodio. |
| Loudness | Que **no pique** por encima del habla. Al montarlo, dejarlo un par de dB por debajo del pico de la voz, no al tope. |

> ⚠️ **LA DIRECCIÓN SONORA SIGUE ABIERTA A PROPÓSITO (act. 2026-07-26).** Andy probó la
> línea industrial el 2026-07-25 y le **chocó**: «por el sonido industrial choca un poco,
> así que voy a experimentar con el sonido». EP.023 salió con un jingle propio y **la
> decisión ahora es variarlo por episodio** (ver § Varía por episodio, abajo) — así que la
> dirección sonora no se va a "cerrar" nunca en un archivo único. Lo que sigue abajo son
> hipótesis de partida, no un estándar aprobado. Lo fijado es la **forma**: duración, corte
> seco, mismo stinger en los dos extremos, y que Andy entre sobre el silencio.

## De qué mundo sale

El sistema visual v4 se llama **Sala de Máquinas**: grafito, acero, un solo naranja,
luz plana de taller. El sonido tiene que salir del mismo sitio — no de una sala de juntas.

**Sí:** un mecanismo. Un relé que cierra, un interruptor industrial, un tono de señal
corto. Grave, seco, con cuerpo metálico. Serio pero no fúnebre.

**No:** piano corporativo inspirador. Swell orquestal. Drop de EDM. Ukelele. Whoosh de
tráiler. Voz cantada. Campanitas de "notificación". Nada que suene a curso de LinkedIn.

## ⚠️ El generador no va a obedecer la duración. No pelee con el prompt.

**Comprobado 2026-07-25:** los generadores de música por texto ignoran las duraciones
cortas. Uno pide 3 segundos y devuelven 60. Tienen una longitud mínima de salida y el
prompt no la cambia — insistir es perder la tarde.

**El flujo correcto es al revés: que genere sus 60 segundos, y el stinger se recorta.**
Eso además juega a favor: de un track de 60 s salen varios candidatos y se elige el mejor.

```
python scripts/cortar_jingle.py <track.wav>
```

Sin más argumentos imprime el mapa de energía del track y **propone los tres mejores
puntos de arranque** — los golpes más secos, donde el sonido entra de la nada. Después:

```
python scripts/cortar_jingle.py <track.wav> --start 12.4 --dur 3.0
```

Recorta, aplica un fade de salida de 45 ms para que no suene un *click*, normaliza el pico
a −3 dBFS y exporta WAV 48 kHz. Y genera además **`BTQ-jingle-PRUEBA-empalme.wav`**:
stinger + 2,5 s de silencio + stinger. **Escuche ese**, porque es exactamente como se va a
oír en el episodio, al abrir y al cerrar.

Si sale con cola o se siente largo, se vuelve a cortar con otro `--start` o `--dur` más
corto. **No hay que regenerar nada.**

## Prompts para pegar en el generador

Tres direcciones distintas, no tres versiones de la misma. Genera las tres y compara —
el juicio final es de oído, no de descripción.

**A · El relé** *(la más literal respecto al episodio y a la marca)*
```
Industrial audio-logo loop. Begins immediately, cold, with no intro build:
a single mechanical relay click, dry and close-miked, followed by two low
synth-bass notes in a minor key. Metallic body, slight tape saturation.
Repeat that same short motif every few seconds with silence between
repeats. Dry, no reverb tail. No drum kit, no melody beyond those two
notes. Serious, industrial, understated.
```

**B · El tono de señal** *(más abstracta, más "marca" que "escena")*
```
Minimal sonic-branding loop. Opens cold on the first beat with three
descending analog synth tones over a low industrial hum, minor key, dry
and precise, slightly detuned. Let the motif repeat with clear gaps of
near-silence between each repetition. No percussion, no reverb wash, no
swell. Restrained and confident, not uplifting.
```

**C · La máquina que arranca** *(la más rítmica; sirve si A y B suenan muy quietas)*
```
Short industrial motif, repeated. Starts instantly on a dry percussive
metallic hit, with one low bass note underneath and a brief filtered pulse
of machinery. Minor key. Tight and mechanical, no reverb, no fanfare.
Repeat the same figure throughout with space between repeats.
```

> **Los prompts ya no piden 3 segundos** — pedirlo no sirve (ver arriba). Lo que piden es
> que el track **arranque con el golpe**, sin construcción previa, y que el motivo se
> repita: así cualquier tramo de 3 s es recortable y hay varios candidatos por generación.
> Lo único que sí conviene insistir en el prompt es `dry, no reverb tail`: la cola de
> reverb es lo único que el recorte no puede arreglar del todo.

## Cómo elegir la buena

1. **Escuche `BTQ-jingle-PRUEBA-empalme.wav`, no el stinger suelto.** El script lo genera
   solo: stinger + silencio + stinger. Tiene que funcionar en los dos sitios sin sentirse
   repetido ni fuera de lugar.
2. **Escúchelo a volumen bajo, en el celular.** Si a bajo volumen no se distingue de
   cualquier otro pódcast, no es una firma.
3. **Si duda de si es largo, es largo.** Vuelva a cortar con `--dur 2.5`.
4. **Lo único que el recorte no arregla es la cola de reverb.** Si el track viene mojado,
   no lo pelee: regenere pidiendo `dry, no reverb tail`.

## Al montarla

- Andy graba **3 s de silencio antes de la primera palabra y 3 después de la última** —
  ahí se pega el jingle sin recortar voz.
- El jingle de cierre entra **después** de que la firma termina, no encima.
## Varía por episodio — la firma es la FORMA, no el archivo

**Decisión de Andy, 2026-07-26 (reemplaza la regla anterior de "asset permanente que se
reusa sin regenerarlo").** Cada episodio lleva **su propio jingle**, generado y recortado
de nuevo, manteniendo **el mismo formato que el de EP.023**. Lo que se mantiene constante
entre episodios es la especificación dura de arriba —2-4 s, mismo stinger al abrir y al
cerrar, corte seco, nunca por debajo del habla—, no la grabación.

Consecuencia práctica: **el jingle vuelve a la lista de pendientes de cada episodio.** No
es un paso que se hace una vez y se hereda. El flujo por episodio es el de arriba: generar
60 s, `cortar_jingle.py` para el mapa de energía, elegir sobre
`BTQ-jingle-PRUEBA-empalme.wav`.

> **Pendiente de documentar:** qué terminó siendo el jingle de EP.023 (cuál de las tres
> direcciones, duración final, y el archivo fuente). Es la referencia de formato de aquí en
> adelante, así que sin eso escrito "el mismo formato que EP.023" no es verificable por
> nadie que retome esto en otra sesión.
