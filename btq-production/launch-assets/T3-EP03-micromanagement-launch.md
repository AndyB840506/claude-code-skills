# BTQ T3 · EP.03 — El señor Burns y Balú (launch assets)

> Procedimiento: `.claude/skills/episode-launch/workflows/t3-conversacional.md` — leerlo antes
> de copiar este kit.

**Temporada 3, episodio 3** (en Spotify for Creators: season 3, episode 3). Andrés Bermúdez y
Alejandro Aguirre. Grabado el 2026-10-24 por Zoom (carpeta `E:\Podcast\BTQ\T3\2026-10-24
19.39.59 BTQ`). Publicación: **domingo 2026-10-25, 9:30 PM** (Colombia), confirmado por Andy.
Web: **teaser completo antes de salir** (como EP.02) y al salir, botón al link del episodio y
redeploy (Andy, 2026-10-24).

| Dato | Valor | Cómo se obtuvo |
|---|---|---|
| Máster | `E:\Podcast\BTQ\T3\EP 03.mp3` (128 kbps, 44,1 kHz); no hay `EP 03.wav` en la carpeta | listado de disco |
| Duración | **46:51** (decodificado entero con ffmpeg). La cabecera del mp3 dice 45:13 (`ffprobe` format=duration): no usar ese dato | `ffmpeg -f null` |
| Transcripción | `E:\Transcriptor\transcripciones\BTQ-T3-EP03.srt` (411 segmentos, 0:56 a 46:31) | WhisperX large-v2 + diarización, 2026-10-24 (≈3 min) |
| Reparto de voz | Andy 26,3 min (65 %) · Alejo 13,9 min (35 %) | suma de segmentos del SRT |
| Hablantes en el SRT | `SPEAKER_00` = Andy · `SPEAKER_01` = Alejo · `SPEAKER_02` = canción de cierre (45:55) | "Yo soy Andrés y conmigo como siempre está el señor Alejo" (01:00) |

Notas del audio:
- Abre directo con la conversación, retomando el EP.02 (jefe vs. líder) y anunciando el tema:
  micromanagement, y "la otra cara": cuándo sí hace falta (01:45–02:26).
- Cumple lo que el EP.02 dejó pendiente (micromanagement como "otro temita").
- La diarización tiene cruces menores (p. ej. 44:55 "hasta la próxima semana, Andy" lo dice
  Alejo y sale como `SPEAKER_00`): las citas se atribuyen leyendo el contexto, no la etiqueta.
- Whisper escribe "Behind the Cue/Cube": es el nombre del show, no se corrige en el SRT.
- Términos en inglés quedan en inglés ([[feedback_btq_english_terms_untranslated]]):
  micromanagement, micromanager, team leader/TL, KPIs, PIP, coaching, feedback, knowledge gap,
  A-B testing, SOPs, accountability, upper management, overconfident, top performer.
- Anuncian para la próxima semana invitadas: mujeres líderes en el BPO (41:28–43:01), y la IA
  como tema de otro episodio (33:23–33:40). **Andy (2026-10-24): las invitadas SÍ se prometen
  en texto**; la IA no.

---

## Fuera de todo texto escrito (aunque esté en el audio)

- Personas con nombre en tono negativo: Adriana, la supervisora de Andy en sus inicios
  (22:39–23:26); Manny (10:41).
- Empresas con nombre en tono negativo: el jefe de Alejo en Asurion que "no hacía nada" y se
  escudaba en él (08:42–09:21) y la vendedora que su supervisor no supo apreciar (24:20–24:43).
- El director de Andy en su trabajo anterior y el regaño por el cumpleaños de una TL en la sala
  de reuniones (09:31–09:48, 34:05–38:14): el empleador es identificable por el LinkedIn de
  Andy. **Andy autorizó usar la anécdota (2026-10-24)**, sin nombrar al empleador ni al
  director.
- El jefe "en el limbo" de Alejo (10:46–12:35): sin nombre de empresa; si se usa, sin datos
  que la identifiquen.
- "La nena vendía hasta una loca embarazada" (24:27) y "agarrándole hasta el hombre" (14:29):
  quedan en el audio.
- Personas nombradas en tono positivo: ninguna en este episodio.
- Blockbuster y Netflix (31:18–32:28): hecho público; se puede nombrar, **sin cifras** (el
  audio no da ninguna).

---

## A · Spotify

**Título** (72 caracteres, elegido por Andy 2026-10-24; lleva la keyword "call center"; "Balú"
con tilde, decisión de Andy):
`EP.03 — El señor Burns y Balú: los dos jefes que hay en todo call center`

**Preview (primeros 100 caracteres):**
```
En todo call center hay dos jefes: el que está encima de cada llamada y el que no hace absolutamente
```

**Descripción — HTML copy-safe (ESTA es la que se pega en Spotify):**
```html
<p>En todo call center hay dos jefes: el que está encima de cada llamada y el que no hace absolutamente nada. En este tercer episodio de la temporada 3, Andrés Bermúdez y Alejandro Aguirre hablan de micromanagement: por qué un jefe termina encima de su gente, qué le hace al equipo y cuándo sí hace falta.</p>
<p>Lo cuentan con dos personajes. El señor Burns, que revisa todo, no deja que nadie se salga del proceso de siempre y tiene un Smithers en cada equipo. Y Balú, el jefe que deja que todo funcione por ósmosis: sin coaching, sin seguimiento, con la hoja de resultados pegada en el cubículo y nadie que explique qué significa.</p>
<p>Hay historias de los dos lados. Alejo llegó a un equipo, las metas se dispararon y aun así su jefe empezó a revisarle todo, hasta que tuvo que pedirle: déjame trabajar, necesito que confíes en lo que estoy haciendo. Andrés vivió lo contrario: un director que nunca le dio feedback y que le pidió castigar a sus supervisores porque los encontraron cantándole el Happy Birthday a una team leader en una sala vacía.</p>
<p>Debajo de las anécdotas hay una distinción útil: el micromanagement que busca el quiebre y el seguimiento que le da la mano a alguien. Un PIP, un A-B testing o un proceso nuevo piden estar encima, pero con metas objetivas y todas las herramientas para que la persona salga adelante. Y el feedback no es solo para corregir: también es para felicitar.</p>
<p>La próxima semana queremos hablar con mujeres líderes del BPO, de cómo ha sido su camino en esta industria. Si usted es una de ellas y quiere contar su historia, escríbanos.</p>
<p>¿Su jefe es más señor Burns o más Balú? Cuéntenos en los comentarios.</p>
<p>Escúchalo ahora en Spotify.</p>
<p>📩 <a href="mailto:andy@behind-thequeue.com">andy@behind-thequeue.com</a> | 🌐 <a href="https://behind-thequeue.com">behind-thequeue.com</a><br>
📸 Instagram: @behindthequeue84 | 🎵 TikTok: @behind.the.queue | 📘 <a href="https://facebook.com/behindthequeue">Facebook</a><br>
💼 <a href="https://linkedin.com/company/behind-the-queue">linkedin.com/company/behind-the-queue</a></p>
```

**Descripción — texto plano (fallback, una línea por párrafo):**
```
En todo call center hay dos jefes: el que está encima de cada llamada y el que no hace absolutamente nada. En este tercer episodio de la temporada 3, Andrés Bermúdez y Alejandro Aguirre hablan de micromanagement: por qué un jefe termina encima de su gente, qué le hace al equipo y cuándo sí hace falta.

Lo cuentan con dos personajes. El señor Burns, que revisa todo, no deja que nadie se salga del proceso de siempre y tiene un Smithers en cada equipo. Y Balú, el jefe que deja que todo funcione por ósmosis: sin coaching, sin seguimiento, con la hoja de resultados pegada en el cubículo y nadie que explique qué significa.

Hay historias de los dos lados. Alejo llegó a un equipo, las metas se dispararon y aun así su jefe empezó a revisarle todo, hasta que tuvo que pedirle: déjame trabajar, necesito que confíes en lo que estoy haciendo. Andrés vivió lo contrario: un director que nunca le dio feedback y que le pidió castigar a sus supervisores porque los encontraron cantándole el Happy Birthday a una team leader en una sala vacía.

Debajo de las anécdotas hay una distinción útil: el micromanagement que busca el quiebre y el seguimiento que le da la mano a alguien. Un PIP, un A-B testing o un proceso nuevo piden estar encima, pero con metas objetivas y todas las herramientas para que la persona salga adelante. Y el feedback no es solo para corregir: también es para felicitar.

La próxima semana queremos hablar con mujeres líderes del BPO, de cómo ha sido su camino en esta industria. Si usted es una de ellas y quiere contar su historia, escríbanos.

¿Su jefe es más señor Burns o más Balú? Cuéntenos en los comentarios.

Escúchalo ahora en Spotify.

📩 andy@behind-thequeue.com | 🌐 behind-thequeue.com
📸 Instagram: @behindthequeue84 | 🎵 TikTok: @behind.the.queue | 📘 Facebook: facebook.com/behindthequeue
💼 LinkedIn: linkedin.com/company/behind-the-queue
```

**Tags (10):**
```
call center, BPO, contact center, micromanagement, liderazgo, jefe vs líder, team leader, feedback, podcast en español, Colombia
```

**Fuente de cada afirmación** (SRT, hora aproximada): los dos jefes en cualquier empleo
(25:23–25:34) · tema micromanagement y cuándo sí hace falta (01:45–02:26) · por qué el jefe se
pone encima: se siente amenazado (03:36–03:59, 06:00–06:12) · el señor Burns y su Smithers en
cada equipo (25:57–26:31) · revisar todo (12:01–12:25) · "si está funcionando, no lo toque",
nadie se sale (18:22–18:40) · Balú, ósmosis, sin coaching ni seguimiento (21:56–22:09) · hoja
en el cubículo sin explicación (23:03–23:14) · Alejo: metas disparadas, "déjame trabajar,
necesito que confíes" (11:15–11:39) · director sin feedback (34:05–34:20, 40:58–41:04) ·
castigar a los supervisores por el Happy Birthday a una TL, sala no ocupada (35:28–36:47) ·
busca el quiebre vs. darte la mano (13:04–13:22, 20:55–21:03) · PIP (12:37–13:00) · A-B
testing (19:58–20:13) · metas objetivas y todas las herramientas (19:40–19:58, 20:26–20:55) ·
feedback para felicitar (39:49–40:46) · mujeres líderes del BPO la próxima semana, escríbanos
(41:28–43:24).

---

## B · Plan social — domingo a martes

Igual que el EP.02: intriga el **domingo en la tarde**, primer comentario con Spotify todos los
días, LinkedIn en primera persona (lo publica Andy) y `@Alejandro Aguirre` escrito a mano al
pegar. **Link del episodio: pendiente de Andy** (al programar en Spotify for Creators); va en
los primeros comentarios donde dice `<LINK EP.03>`.

**Imagen de cada post** (generador: `comfyui/templates/btq-social-t3.py <out> EP.03`; todo en
`E:\Podcast\BTQ\T3\redes\EP03\` salvo las portadas):

| Post | Archivo |
|---|---|
| Domingo tarde · IG/FB | `BTQ-T3-EP03-teaser-1x1.png` |
| Domingo tarde · stories 1-3 | `BTQ-T3-EP03-story-1-9x16.png`, `-story-2-`, `-story-3-` (la 3 deja libre abajo para el sticker de enlace) |
| Domingo 9:30 PM · LinkedIn y Facebook | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP03-portada-16x9.png` |
| Domingo 9:30 PM · Instagram | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP03-portada-1x1.png` |
| Domingo 9:30 PM · TikTok | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP03-portada-9x16.png` |
| Lunes · LinkedIn | `BTQ-T3-EP03-cita-andres-4x5.png` (SRT 08:07; cortada antes de "ni su trabajo") |
| Martes · LinkedIn | `BTQ-T3-EP03-cita-alejo-4x5.png` (SRT 13:04) |
| Martes · reel IG/FB y TikTok | `BTQ-T3-EP03-reel-andres-burns-9x16.mp4` (1080×1920, H.264 + AAC, 68,4 s) |

Citas: las 5 de las piezas y los posts se comprobaron textuales contra el SRT con script (con
mutación de control). La del reel ("Un señor Burns tiene un Smithers", 26:13) el SRT la escribe
"Sr. Burns"; la re-transcripción del clip, "señor Burns".

### Domingo 25 oct, tarde · intriga · Instagram/Facebook (+ 3 stories)

```
En todo call center hay dos jefes: el señor Burns, que está encima de cada llamada, y Balú, que no hace absolutamente nada.

Esta noche a las 9:30 PM sale el EP.03 de la temporada 3 de Behind the Queue: micromanagement, y cuándo sí hace falta.

#BehindTheQueue #PodcastEnEspañol #NuevoEpisodio #BPO #CallCenter #ContactCenter #Liderazgo #Colombia #LATAM #Bogota
```

Stories (fondo crema, texto azul marino; la tercera con sticker de enlace a Spotify):
```
1 · ¿Su jefe es el señor Burns o es Balú?
2 · Hay que dar feedback. Así sea para felicitar.
3 · Hoy · 9:30 PM · EP.03 en Spotify.
```

### Domingo 25 oct, 9:30 PM · lanzamiento

**LinkedIn** (prioritaria):
```
¿Su jefe es más señor Burns o más Balú?

En el EP.03 de la temporada 3 de Behind the Queue, Alejandro Aguirre y yo hablamos de micromanagement. Llegamos a que en todo call center hay dos jefes: el que revisa todo y no deja que nadie se salga del proceso de siempre, y el que deja que todo funcione por ósmosis, sin coaching y sin seguimiento.

Alejo lo vivió con un jefe que le revisaba todo justo cuando las metas se habían disparado: "Déjame trabajar, necesito que confíes en lo que estoy haciendo."

Pero también hablamos de cuándo sí hace falta estar encima. Un PIP o un proceso nuevo lo piden. La diferencia está en para qué: buscar el quiebre o darle la mano a alguien.

#BPO #ContactCenter #CallCenter #Liderazgo #Micromanagement #PodcastEnEspañol #Colombia #LATAM
```

**Primer comentario:**
```
Episodio completo acá 👉 <LINK EP.03>
```

**Instagram/Facebook** (portada 1:1 o 16:9):
```
EP.03, al aire.

El señor Burns y Balú: los dos jefes que hay en todo call center. Andy y Alejo hablan de micromanagement desde los dos lados: el jefe que revisa todo, el que nunca da feedback, y cuándo sí toca estar encima.

¿Cuál le tocó a usted? Cuéntenos abajo.

Link en la bio.

#BehindTheQueue #PodcastEnEspañol #NuevoEpisodio #BPO #CallCenter #ContactCenter #Liderazgo #Micromanagement #TeamLeader #TrabajoEnColombia #Colombia #LATAM #Bogota
```

**TikTok** (portada 9:16):
```
En todo call center hay dos jefes: el señor Burns y Balú.
EP.03 de Behind the Queue, ya en Spotify.
#BPO #CallCenter #Liderazgo #Colombia
```

### Lunes 26 oct, 7 a 8 AM · LinkedIn

```
"Un líder de verdad no debería sentirse en ningún momento amenazado."

Lo dije en el EP.03 de Behind the Queue, y lo digo porque me tocó un director que hacía lo contrario de estar encima: nunca me dio feedback. Yo sabía que estaba haciendo las cosas bien solo porque no me llamaban.

Hasta que unos supervisores le cantaron el Happy Birthday a una team leader en una sala que nadie estaba usando. Le llegó el comentario, y me pidió castigarlos de una manera severa.

No lo hice. Les di la retroalimentación, les expliqué por qué no estaba bien, y la vida siguió. No estaban afectando el trabajo ni los números.

Toca ser jefe cuando hay que serlo. Pero no por cosas minúsculas.

¿A usted le han pedido castigar algo que no lo merecía?

#Liderazgo #BPO #ContactCenter #GestionDeEquipos #Micromanagement #Colombia
```

**Primer comentario:**
```
El episodio completo, para el camino al trabajo 👉 <LINK EP.03>
```

### Martes 27 oct · refuerzo

**LinkedIn:**
```
Alejo tiene una regla para cuando le toca estar encima de alguien, en un PIP o con un proceso nuevo: metas objetivas, y todas las herramientas para que la persona salga adelante.

Como él lo dijo en el EP.03 de Behind the Queue: "Este micromanagement no es para hacerte caer. Este micromanagement es para darte la mano y sacarte de donde estás."

Y la otra mitad: el feedback no es solo para corregir. "Cojan a su gente que lo está haciendo bien. Felicítenlos."

¿Cuándo fue la última vez que su jefe lo felicitó en una sesión de feedback?

#Liderazgo #BPO #ContactCenter #TeamLeader #Feedback #Colombia #LATAM
```

**Primer comentario:**
```
El EP.03 completo 👉 <LINK EP.03>
```

**Instagram/Facebook** (reel de 68 s):
```
"Un señor Burns tiene un Smithers."

Fragmento del EP.03 de la temporada 3: el jefe que no hace nada, el que revisa todo, y el que le hace el juego en cada equipo. ¿Usted tiene uno de cada uno?

Episodio completo en Spotify, link en la bio.

#BehindTheQueue #PodcastEnEspañol #BPO #CallCenter #ContactCenter #Liderazgo #Micromanagement #GestionDeEquipos #TrabajoEnColombia #Colombia #LATAM
```

**TikTok** (mismo reel):
```
¿Su jefe es el señor Burns o es Balú?
EP.03, temporada 3, en Spotify.
#BPO #CallCenter #Liderazgo #Colombia
```

**Fuente de cada afirmación del plan social** (SRT): las de la descripción, más: "un líder de
verdad no debería sentirse en ningún momento amenazado" (08:07–08:18) · director que nunca dio
feedback, sabía que estaba bien porque no lo llamaban (34:05–34:20, 40:58–41:15) · castigo
severo pedido por el jefe (36:55–37:01) · retroalimentación, explicar por qué no está bien,
"life goes on" (36:47–37:26) · no afectaba trabajo ni números, cosas minúsculas (37:28–37:36) ·
toca ser jefe (37:36–37:44) · feedback para felicitar, "Cojan a su gente… Felicítenlos"
(39:49–40:06) · Smithers que le hace el juego al jefe en cada equipo (26:04–26:24).

---

## D · Portada (compuesta, no generada)

Compositor: `comfyui/templates/btq-portada-t3.py`. Al componerla salió un defecto: la línea con
Ñ/Ú bajaba y se pegaba a la siguiente (el título se alineaba por el tope de cada línea, y los
acentos lo suben). Arreglado con tope común de mayúscula; ahora los topes quedan a 122 px en
1:1. Regresión EP.02: el bloque del título sube 2 px (1:1) y 1 px (16:9) por la sobreoscilación
de O/G, con el mismo espaciado entre líneas; las portadas publicadas del EP.02 no se tocan.

```
python comfyui/templates/btq-portada-t3.py "EP.03" "EL SEÑOR BURNS Y BALÚ:|LOS DOS JEFES QUE HAY|*EN TODO CALL CENTER*" "E:/Podcast/BTQ/T3/portada/BTQ-T3-EP03-portada"
```

| Formato | Archivo |
|---|---|
| 1:1 · 3000×3000 (Spotify) | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP03-portada-1x1.png` |
| 9:16 · 1080×1920 | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP03-portada-9x16.png` |
| 16:9 · 1920×1080 (YouTube) | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP03-portada-16x9.png` |

---

## E · Clip de audio para reel

**El señor Burns, Balú y Smithers** (Andy abre con los dos jefes, Alejo propone a Burns).

| | |
|---|---|
| In / out en el máster | 25:23.0 → 26:31.4 (seek antes de `-i`) |
| Duración | 68,40 s |
| Archivos | `E:\Podcast\BTQ\T3\clip\BTQ-T3-EP03-CLIP-01.wav` (24-bit, sacado del mp3: no hay WAV del máster) y `.mp3` (192 kbps) |
| Volumen | mean -23,2 dB / max -1,9 dB; no es silencio |
| Bordes | Re-transcrito el clip solo: abre en "Cualquier empleo…" (0,19 s) y cierra en "…en cada equipo" (67,98 s); el fundido de salida empieza en 68,1 s |

---

## Publicación

- [ ] Subir y programar en Spotify for Creators (domingo 25, 9:30 PM) y pasar el link del
      episodio para los primeros comentarios.
- [ ] Web: teaser antes de salir (tarjeta EP.03 con fecha, quote card y botón "Domingo 9:30 PM"
      al show; EP.02 pasa a la fila "Temporada 3"). Preview lo revisa Andy; luego producción.
- [ ] **Al salir el episodio:** botón a "Escuchar" con el link del episodio, quitar la fecha de
      la etiqueta, redeploy y verificar con `curl -L` + diff.
