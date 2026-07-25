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

## De qué mundo sale

El sistema visual v4 se llama **Sala de Máquinas**: grafito, acero, un solo naranja,
luz plana de taller. El sonido tiene que salir del mismo sitio — no de una sala de juntas.

**Sí:** un mecanismo. Un relé que cierra, un interruptor industrial, un tono de señal
corto. Grave, seco, con cuerpo metálico. Serio pero no fúnebre.

**No:** piano corporativo inspirador. Swell orquestal. Drop de EDM. Ukelele. Whoosh de
tráiler. Voz cantada. Campanitas de "notificación". Nada que suene a curso de LinkedIn.

## Prompts para pegar en el generador

Tres direcciones distintas, no tres versiones de la misma. Genera las tres y compara —
el juicio final es de oído, no de descripción.

**A · El relé** *(la más literal respecto al episodio y a la marca)*
```
Short audio logo, 3 seconds. Starts with a single mechanical relay click,
dry and close-miked. Then two low synth-bass notes, minor, industrial and
warm. Metallic body, slight tape saturation. Ends abruptly in silence,
no reverb tail. No melody beyond the two notes. No drums. Serious,
industrial, understated.
```

**B · El tono de señal** *(más abstracta, más "marca" que "escena")*
```
Podcast sonic logo, 3 seconds. A low sustained industrial hum that resolves
into three descending synth tones, minor key, dry and precise. Analog,
slightly detuned. No percussion, no reverb wash. Ends clean and sudden.
Restrained and confident, not uplifting.
```

**C · La máquina que arranca** *(la más rítmica; sirve si A y B suenan muy quietas)*
```
3-second audio stinger. A short pulse of low industrial machinery starting
up, filtered, with a dry percussive metallic hit on the downbeat and one
bass note underneath. Minor. Tight, no reverb, hard stop. Mechanical and
serious, no fanfare.
```

> Ajuste si sale largo: bajar el número de segundos en el prompt y pedir explícitamente
> `hard stop, no fade`. Los generadores tienden a estirar y a poner cola de reverb.

## Cómo elegir la buena

1. **Escúchala a volumen bajo, en el celular.** Si a bajo volumen no se distingue de
   cualquier otro pódcast, no es una firma.
2. **Pégala al principio y al final del mismo archivo y escúchalos seguidos.** Tiene que
   funcionar en los dos sitios sin sentirse repetida ni fuera de lugar.
3. **Cuenta los segundos.** Si dudas si es larga, es larga.
4. **Prueba el empalme con la voz:** jingle → silencio → «Buenas y santas». Si tienes que
   recortar la cola del jingle para que no pise la voz, pide otra versión con `hard stop`.

## Al montarla

- Andy graba **3 s de silencio antes de la primera palabra y 3 después de la última** —
  ahí se pega el jingle sin recortar voz.
- El jingle de cierre entra **después** de que la firma termina, no encima.
- Guardar el archivo elegido como asset permanente de marca; se reusa en todos los
  episodios sin regenerarlo.
