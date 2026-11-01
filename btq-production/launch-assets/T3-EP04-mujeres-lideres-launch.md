# BTQ T3 · EP.04 — Mujeres líderes del BPO (launch assets)

> Procedimiento: `.claude/skills/episode-launch/workflows/t3-conversacional.md` — leerlo antes
> de copiar este kit.

**Temporada 3, episodio 4** (en Spotify for Creators: season 3, episode 4). Andrés Bermúdez y
Alejandro Aguirre, con Adriana Simbaqueba y Paula Cantor de invitadas. Grabado el 2026-10-31 por
Zoom (carpeta `E:\Podcast\BTQ\T3\2026-10-31 19.35.48 Behind The Queue`).

| Dato | Valor | Cómo se obtuvo |
|---|---|---|
| Máster | `E:\Podcast\BTQ\T3\EP 04.mp3` (128 kbps); no hay `EP 04.wav` en la carpeta | listado de disco |
| Duración | **74:45** (decodificado entero con ffmpeg; la cabecera coincide: 4485,5 s) | `ffmpeg -f null` y `ffprobe` |
| Volumen | mean -20,7 dB / max 0,0 dB | `volumedetect` |
| Transcripción | `E:\Transcriptor\transcripciones\BTQ-T3-EP04.srt` (800 segmentos, 0:57 a 74:25) | WhisperX large-v2 + diarización, 2026-10-31 |
| Reparto de voz | Adriana 23,6 min (36 %) · Andy 19,9 (31 %) · Paula 16,2 (25 %) · Alejo 5,5 (8 %) | suma de segmentos del SRT |
| Hablantes en el SRT | `SPEAKER_00` = Andy · `SPEAKER_01` = Alejo · `SPEAKER_02` = Adriana · `SPEAKER_03` = Paula · `SPEAKER_04` = canción de cierre (73:49) | presentaciones 00:59-05:20 y 23:34 |

Notas del audio:
- Paula y Alejo comparten micrófono (Andy, 2026-10-31), así que las pistas de Zoom no los separan;
  la diarización sí lo hizo. Cruces menores: "Esa es Paula" (38:55, sale como Adriana), 40:26
  (Adriana, sale como Paula), "Mándeme la incapacidad" (41:56, sale como la canción). Las citas se
  atribuyen leyendo el contexto, no la etiqueta.
- Whisper escribe "Behind the Cue/Cube": es el nombre del show, no se corrige en el SRT.
- Cumple la promesa del EP.03 (mujeres líderes del BPO).
- Andy promete al aire que las redes de Adriana y Paula van en la descripción (72:45): dicen
  LinkedIn, Adriana (70:39) y `paula.cantor` (71:13). Whisper escribe mal el de Adriana.
- Próximo episodio: IA en el BPO, "el otro sábado"; a las dos se les hace invitación abierta, sin
  respuesta al aire (63:02-63:42, 72:35).
- Términos en inglés quedan en inglés ([[feedback_btq_english_terms_untranslated]]): background,
  KPIs, coaching, feedback, team leader, jumper, root causes, account manager, Operations Manager,
  understaffed, dashboard, BPO.

---

## Fuera de todo texto escrito (aunque esté en el audio)

Empresas con acusación o tono negativo:
- Intouch: le cancelaron el contrato a Adriana cerca de un año después de la cirugía (15:49-16:36);
  cabeza "solo mujeres" y "roscas" (17:33-18:16). Las dos juntas, además, se leen como acusación.
- TP/Teleperformance: "ahí sí entendí por qué TP tiene la fama que tiene" y recorte de contratos en
  pandemia (13:39-14:24); "eso es como el bullying" (08:42); Paula no pasó el proceso (24:29).
- Colsila: trato "terrible", llamadas de noche (07:01-07:22). Atento y los fraudes del área español
  (05:57).
- KM2: cafetería "de cárcel" (25:03), edificio "un hueco" (24:38), "tenía a toda mi empresa contra
  mí" (28:48). Crecer "porque te comías al jefe" (53:37-54:31): sin empresa tampoco.

Personas con nombre:
- Tono negativo: el señor Nilton (07:06); Rafael, director en TP (13:52).
- Tono positivo o neutro, sin permiso: Carlos Villamarín (dicho "Villamizar" en broma, 03:08-04:14),
  Julián Lasprilla, Alex Valcárcel, John Laguna, Rafa, David Cañón.
- Datos personales de las invitadas: la cirugía de Adriana y sus hijos (Andy dice "cuatro", ella
  "tres": 02:11, 57:12), su exmarido (12:32); edad de Paula.

Quedan en el audio: "las tetas por fuera" (53:45), "tienen la cabeza metida dentro del culo"
(48:22), "más sexo que Petro" (69:31), lo de "tocarla" (40:45), Petro.

Sin citar como hecho (el audio no lo sostiene con fuente): "la primera campaña bilingüe que llegó a
Colombia" (05:29), "reemplazados por robots" (19:40), jardín infantil en las empresas (60:14).

Autorizado por Andy (2026-10-31): la anécdota del perro de Paula, sin nombrar a KM2 ni al jefe, **con
aviso a Paula antes de publicar**. La broma de 69:31 se queda en el audio.

---

## A · Spotify

**Título** (elegido por Andy 2026-10-31; lleva la keyword "call center"; frase de 27:28):
`EP.04 — "Esta niña": lo que le toca a una mujer para liderar en un call center`

**Preview (primeros 100 caracteres):**
```
Cuando Paula Cantor era supervisora en un call center, los agentes no la llamaban por su nombre. Dec
```

**Descripción — HTML copy-safe (ESTA es la que se pega en Spotify):**
```html
<p>Cuando Paula Cantor era supervisora en un call center, los agentes no la llamaban por su nombre. Decían "esta niña". Una vez se lo dijeron hasta a Recursos Humanos: es que esta niña me está diciendo tal cosa.</p>
<p>En este cuarto episodio de la temporada 3, Andrés Bermúdez y Alejandro Aguirre cumplen lo que prometieron y reciben a dos líderes del BPO. Adriana Simbaqueba es abogada, nunca ejerció y arrancó en la industria en 2004. Paula Cantor es diseñadora industrial, entró a un call center buscando plata para salir de fiesta y llegó a Operations Manager.</p>
<p>Las dos cuentan lo que les tocó: agentes que recibían soporte de la supervisora y después iban a preguntarle lo mismo a un hombre, jefes que prefieren a sus amigos, y un estigma que sigue ahí. Si una mujer habla duro, es histérica. Si llora por algo, llora por todo. Si es muy dulce, es demasiado suave. Y si es mamá, hay quien asume que va a estar menos disponible, cuando eso, dice Adriana, no tiene nada que ver con el rendimiento ni con el cumplimiento de metas.</p>
<p>La historia que más pesa es la de Paula. El día que tuvo que dormir a su perro llamó a avisar que no podía ir, y su jefe le respondió que estaba poniendo en riesgo su trabajo. Fue. Se sentó en su puesto y lloró el día completo delante de su equipo. Después se lo contó muchas veces a la gente que lideró: nadie espera que usted sea una máquina.</p>
<p>También hay método. Adriana lo resume en una frase: somos personas trabajando con personas y para personas. Las generaciones nuevas, dice, ya no se deslumbran por un buen salario sino por sentirse parte de algo, y el trabajo de un líder no es imponer su estilo sino poner a girar todos esos mundos en torno a un mismo resultado. Uno cuida a las personas y los números vienen.</p>
<p>¿Alguna vez le han quitado autoridad en el trabajo por ser mujer, por ser joven o por ser mamá? Cuéntenos en los comentarios.</p>
<p>Escúchalo ahora en Spotify.</p>
<p>Encuéntrelos en LinkedIn: <a href="https://www.linkedin.com/in/adriana-simbaqueba/">Adriana Simbaqueba</a> | <a href="https://www.linkedin.com/in/paula-cantor/">Paula Cantor</a> | <a href="https://www.linkedin.com/in/alejandro-aguirre-hernandez/">Alejandro Aguirre</a> | <a href="https://www.linkedin.com/in/andres-bermudez-rodriguez">Andrés Bermúdez</a></p>
<p>📩 <a href="mailto:andy@behind-thequeue.com">andy@behind-thequeue.com</a> | 🌐 <a href="https://behind-thequeue.com">behind-thequeue.com</a><br>
📸 Instagram: @behindthequeue84 | 🎵 TikTok: @behind.the.queue | 📘 <a href="https://facebook.com/behindthequeue">Facebook</a><br>
💼 <a href="https://linkedin.com/company/behind-the-queue">linkedin.com/company/behind-the-queue</a></p>
```

**Descripción — texto plano (fallback, una línea por párrafo):**
```
Cuando Paula Cantor era supervisora en un call center, los agentes no la llamaban por su nombre. Decían "esta niña". Una vez se lo dijeron hasta a Recursos Humanos: es que esta niña me está diciendo tal cosa.

En este cuarto episodio de la temporada 3, Andrés Bermúdez y Alejandro Aguirre cumplen lo que prometieron y reciben a dos líderes del BPO. Adriana Simbaqueba es abogada, nunca ejerció y arrancó en la industria en 2004. Paula Cantor es diseñadora industrial, entró a un call center buscando plata para salir de fiesta y llegó a Operations Manager.

Las dos cuentan lo que les tocó: agentes que recibían soporte de la supervisora y después iban a preguntarle lo mismo a un hombre, jefes que prefieren a sus amigos, y un estigma que sigue ahí. Si una mujer habla duro, es histérica. Si llora por algo, llora por todo. Si es muy dulce, es demasiado suave. Y si es mamá, hay quien asume que va a estar menos disponible, cuando eso, dice Adriana, no tiene nada que ver con el rendimiento ni con el cumplimiento de metas.

La historia que más pesa es la de Paula. El día que tuvo que dormir a su perro llamó a avisar que no podía ir, y su jefe le respondió que estaba poniendo en riesgo su trabajo. Fue. Se sentó en su puesto y lloró el día completo delante de su equipo. Después se lo contó muchas veces a la gente que lideró: nadie espera que usted sea una máquina.

También hay método. Adriana lo resume en una frase: somos personas trabajando con personas y para personas. Las generaciones nuevas, dice, ya no se deslumbran por un buen salario sino por sentirse parte de algo, y el trabajo de un líder no es imponer su estilo sino poner a girar todos esos mundos en torno a un mismo resultado. Uno cuida a las personas y los números vienen.

¿Alguna vez le han quitado autoridad en el trabajo por ser mujer, por ser joven o por ser mamá? Cuéntenos en los comentarios.

Escúchalo ahora en Spotify.

LinkedIn:
Adriana Simbaqueba: linkedin.com/in/adriana-simbaqueba
Paula Cantor: linkedin.com/in/paula-cantor
Alejandro Aguirre: linkedin.com/in/alejandro-aguirre-hernandez
Andrés Bermúdez: linkedin.com/in/andres-bermudez-rodriguez

📩 andy@behind-thequeue.com | 🌐 behind-thequeue.com
📸 Instagram: @behindthequeue84 | 🎵 TikTok: @behind.the.queue | 📘 Facebook: facebook.com/behindthequeue
💼 LinkedIn: linkedin.com/company/behind-the-queue
```

**Tags (10):**
```
call center, BPO, contact center, mujeres líderes, liderazgo, liderazgo femenino, team leader, machismo laboral, podcast en español, Colombia
```

**Fuente de cada afirmación** (SRT, hora aproximada): "esta niña", Recursos Humanos (27:20-27:36)
· Adriana abogada, arrancó en 2004, nunca ejerció (02:11, 05:26, 40:40) · Paula diseñadora
industrial, plata para irse de fiesta, Operations Manager (02:53, 25:29, 29:36) · soporte y
preguntarle al hombre (26:49) · jefes que prefieren a sus amigos hombres (16:59) · el estigma
(54:37-54:51) · mamá, disponibilidad, rendimiento y metas (58:55-59:09) · el perro, "poniendo en
riesgo tu trabajo", llorar en el puesto, contárselo al equipo (43:15-44:59) · personas con personas
(19:20) · salario vs. sentirse parte (38:59-39:14) · imponer estilos, mundos y un mismo resultado
(20:24-20:41) · cuidar a las personas y los números vienen (67:00).

---

## B · Plan social — domingo a miércoles

Mismo esquema del EP.03: intriga el **domingo en la tarde**, primer comentario con Spotify todos
los días, LinkedIn en primera persona (lo publica Andy) y las @-menciones de Alejandro Aguirre,
Adriana Simbaqueba y Paula Cantor escritas a mano al pegar. El lunes 2 de noviembre debe ser festivo
en Colombia (Todos los Santos trasladado; no comprobado contra calendario oficial), así que ese post
puede rendir mejor más tarde.

Link del episodio: lo pasó Andy el 2026-10-31 (sin el parámetro `?si=`).

**Imagen de cada post** (generador: `comfyui/templates/btq-social-t3.py <out> EP.04`; todo en
`E:\Podcast\BTQ\T3\redes\EP04\` salvo las portadas):

| Post | Archivo |
|---|---|
| Domingo tarde · IG/FB | `BTQ-T3-EP04-teaser-1x1.png` |
| Domingo tarde · stories 1-3 | `BTQ-T3-EP04-story-1-9x16.png`, `-story-2-`, `-story-3-` (la 3 deja libre abajo para el sticker de enlace) |
| Domingo 9:30 PM · LinkedIn y Facebook | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP04-portada-16x9.png` |
| Domingo 9:30 PM · Instagram | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP04-portada-1x1.png` |
| Domingo 9:30 PM · TikTok | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP04-portada-9x16.png` |
| Lunes · LinkedIn | `BTQ-T3-EP04-cita-paula-4x5.png` (SRT 64:37; elegida por Andy, 2026-10-31) |
| Martes · LinkedIn | `BTQ-T3-EP04-cita-adriana-4x5.png` (SRT 67:07) |
| Miércoles · LinkedIn | `BTQ-T3-EP04-cita-paula-irme-4x5.png` (SRT 30:52; pedida por Andy, 2026-10-31) |
| Martes · reel IG/FB y TikTok | `BTQ-T3-EP04-reel-paula-nina-9x16.mp4` (1080×1920, H.264 + AAC, 64,8 s; lámina con cita del clip, SRT 27:24) |

### Domingo 1 nov, tarde · intriga · Instagram/Facebook (+ 3 stories)

```
"Esta niña." Así le decían los agentes a su supervisora.

Esta noche a las 9:30 PM sale el EP.04 de la temporada 3 de Behind the Queue, con dos invitadas: Adriana Simbaqueba y Paula Cantor, dos líderes del BPO que cuentan lo que les tocó para llegar.

#BehindTheQueue #PodcastEnEspañol #NuevoEpisodio #BPO #CallCenter #ContactCenter #Liderazgo #MujeresLideres #Colombia #LATAM #Bogota
```

Stories (fondo crema, texto azul marino; la tercera con sticker de enlace a Spotify):
```
1 · ¿Le han dicho "esta niña" en el trabajo?
2 · Somos personas trabajando con personas y para personas.
3 · Hoy · 9:30 PM · EP.04 en Spotify.
```

### Domingo 1 nov, 9:30 PM · lanzamiento

**LinkedIn** (prioritaria):
```
Si una mujer habla duro, es histérica. Si llora por algo, llora por todo. Si es muy dulce, es demasiado suave.

Eso lo dijo Paula Cantor en el EP.04 de la temporada 3 de Behind the Queue, donde Alejandro Aguirre y yo invitamos a dos líderes del BPO: Paula y Adriana Simbaqueba, a quien conozco desde que trabajamos juntos hace más de diez años.

A Paula los agentes le decían "esta niña". Adriana arrancó en esta industria en 2004. Las dos llegaron al mismo lugar: la gente pesa más que los números, y no es un discurso bonito. Como dijo Adriana: si la gente se siente bien donde está, va a hacer su trabajo bien y los números van a aparecer.

Gracias a las dos por venir.

#BPO #ContactCenter #CallCenter #Liderazgo #MujeresLideres #PodcastEnEspañol #Colombia #LATAM
```

**Primer comentario:**
```
Episodio completo acá 👉 https://open.spotify.com/episode/4toaNIfokVoTlUInTLSdbt
```

**Instagram/Facebook** (portada 1:1 o 16:9):
```
EP.04, al aire.

"Esta niña": lo que le toca a una mujer para liderar en un call center. Andy y Alejo reciben a Adriana Simbaqueba y Paula Cantor, dos líderes del BPO, para hablar de resistencia, estigmas, ser mamá y líder, y por qué la gente pesa más que el negocio.

¿Le han quitado autoridad por ser mujer, por ser joven o por ser mamá? Cuéntenos abajo.

Link en la bio.

#BehindTheQueue #PodcastEnEspañol #NuevoEpisodio #BPO #CallCenter #ContactCenter #Liderazgo #MujeresLideres #TrabajoEnColombia #Colombia #LATAM #Bogota
```

**TikTok** (portada 9:16):
```
"Esta niña": lo que le toca a una mujer para liderar en un call center.
EP.04 de Behind the Queue, ya en Spotify.
#BPO #CallCenter #Liderazgo #Colombia
```

### Lunes 2 nov · LinkedIn

```
"Me siento feliz de que puedan ver el ejemplo de mujeres como nosotras y decir, ok, sí se puede."

Así cerró Paula Cantor el EP.04 de Behind the Queue, y no lo dice desde afuera. Llegó a supervisora muy joven y los agentes se referían a ella así: "esta niña". Pasó por el odio, por el "yo te digo y punto", y por las reuniones donde le pedían dejar de hablarle así a la gente. Hasta que entendió que tenía que explicar el porqué y ganarse la confianza.

Y luego contó algo que no se me va a olvidar. El día que tuvo que dormir a su perro, su jefe le dijo que estaba poniendo en riesgo su trabajo. Fue, se sentó en su puesto y lloró el día completo frente a todo su equipo.

Esa imagen le quedó grabada, y se la contó a la gente que lideró muchas veces: nadie espera que usted sea una máquina.

¿Qué le ha enseñado a usted el peor jefe que ha tenido?

#Liderazgo #BPO #ContactCenter #GestionDeEquipos #MujeresLideres #Colombia
```

**Primer comentario:**
```
El episodio completo, para el camino 👉 https://open.spotify.com/episode/4toaNIfokVoTlUInTLSdbt
```

### Martes 3 nov · refuerzo

**LinkedIn:**
```
Adriana Simbaqueba arrancó en esta industria en 2004 y trae una pregunta que muchos jefes no hacen.

Cuando un agente dice que no puede ir porque su mamá tuvo un accidente, ¿qué responde usted? Ella les pedía a sus supervisores algo simple: preguntar qué necesita, escribirle para saber cómo sigue, y acercarse apenas vuelva.

Su conclusión en el EP.04 de Behind the Queue: "Si la gente se siente bien donde está, va a hacer su trabajo bien y los números van a aparecer."

Y lo que dice que más la enorgullece de su carrera no es un KPI: es la gente que ha ascendido trabajando con ella.

¿Cuál es la persona que usted vio crecer y de la que más orgulloso está?

#Liderazgo #BPO #ContactCenter #TeamLeader #MujeresLideres #Colombia #LATAM
```

**Primer comentario:**
```
El EP.04 completo 👉 https://open.spotify.com/episode/4toaNIfokVoTlUInTLSdbt
```

**Instagram/Facebook** (reel de 65 s):
```
"Es que esta niña me está diciendo tal cosa."

Fragmento del EP.04 de la temporada 3: Paula Cantor cuenta lo que es ser supervisora muy joven y que un agente la lleve hasta Recursos Humanos con esa frase.

Episodio completo en Spotify, link en la bio.

#BehindTheQueue #PodcastEnEspañol #BPO #CallCenter #ContactCenter #Liderazgo #MujeresLideres #TrabajoEnColombia #Colombia #LATAM
```

**TikTok** (mismo reel):
```
¿A usted también le han dicho "esta niña" en el trabajo?
EP.04, temporada 3, en Spotify.
#BPO #CallCenter #Liderazgo #Colombia
```

### Miércoles 4 nov · LinkedIn

```
"Fui esa gente que llegó y quería irse a los 10 minutos."

Por eso, cuando le tocó liderar, Paula Cantor quiso hacer algo distinto. Que quien se sienta con usted no le diga "deje de quedarse en After Call", sino que le pregunte cómo está, cómo le fue ayer, cómo siguió su mamá.

Lo contó en el EP.04 de Behind the Queue: en sus campañas también había que cumplirles a los jefes, pero más que eso quería que a la gente le gustara estar ahí.

¿Qué lo hizo a usted querer irse de un trabajo a los 10 minutos?

#Liderazgo #BPO #ContactCenter #Attrition #MujeresLideres #Colombia
```

**Primer comentario:**
```
El EP.04 completo 👉 https://open.spotify.com/episode/4toaNIfokVoTlUInTLSdbt
```

**Fuente de cada afirmación del plan social** (SRT): las de la descripción, más: querer irse a los 10
minutos, hacer algo distinto, las preguntas, cumplirles a los jefes (30:33-31:13) · conozco a Adriana
desde hace más de diez años (01:40) · supervisora súper joven (26:15-26:33) · el odio, "yo te digo y
punto", explicar por qué y confiar (26:56-27:24) · dejar de hablarle así a la gente (27:59) · la
imagen grabada, contarlo a todos (44:50-44:59) · qué necesitas, escribirle, acercarse al volver
(41:40-42:20; ella dice "atropellaron a mi mamá") · el orgullo más allá del KPI, la gente que ascendió
(66:04-67:30).

---

## D · Portada (compuesta, no generada)

Compositor: `comfyui/templates/btq-portada-t3.py`, con modo nuevo de 4 personas (`INVITADAS`). La foto
de Adriana solo mide 400×400 px: en la 1:1 de 3000 px se amplía unas 2 veces y se nota algo blanda.
Si llega una foto más grande, se cambia la ruta y se recompone. Regresión: EP.03 da 0 px de diferencia
en los 3 formatos; en redes, EP.01 y EP.03 quedan idénticos en 7 de 7 piezas.

```
python comfyui/templates/btq-portada-t3.py "EP.04" '"ESTA NIÑA":|LO QUE LE TOCA A UNA MUJER|*PARA LIDERAR EN UN CALL CENTER*' "E:/Podcast/BTQ/T3/portada/BTQ-T3-EP04-portada"
```

| Formato | Archivo |
|---|---|
| 1:1 · 3000×3000 (Spotify) | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP04-portada-1x1.png` |
| 9:16 · 1080×1920 | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP04-portada-9x16.png` |
| 16:9 · 1920×1080 (YouTube) | `E:\Podcast\BTQ\T3\portada\BTQ-T3-EP04-portada-16x9.png` |

---

## E · Clip de audio para reel

**"Esta niña"** (Paula). Abre con "O yo le daba soporte…" y lleva adentro la cita de la lámina (la re-transcripción
la oye entera, en 0:35). En 0:45 Whisper oye "No, dale, dale" sin que el SRT del episodio
lo registre: revisarlo al oído.

| | |
|---|---|
| In / out en el máster | 26:49,65 → 27:54,45 (seek antes de `-i`) |
| Duración | 64,80 s |
| Archivos | `E:\Podcast\BTQ\T3\clip\BTQ-T3-EP04-CLIP-01.wav` (24-bit, sacado del mp3: no hay WAV del máster) y `.mp3` (192 kbps) |
| Volumen | mean -23,2 dB / max -5,9 dB; no es silencio |
| Bordes | Re-transcrito el clip solo: abre en "O yo le daba soporte…" (0,15 s) y cierra en "…con todos tiene problemas" (64,27 s); el fundido de salida empieza en 64,65 s |

---

## Publicación

- [ ] Avisar a Paula de la anécdota del perro y a las dos de lo que dice el kit, antes de publicar.
- [x] Subido en Spotify for Creators (Andy, 2026-10-31):
      https://open.spotify.com/episode/4toaNIfokVoTlUInTLSdbt
      **Hora: pendiente de confirmar** (patrón de los EP.02 y EP.03: domingo 9:30 PM, que es lo que
      dicen teaser y stories).
- [x] Link puesto en los cuatro primeros comentarios.
- [x] Web: tarjeta del EP.04 en local (`ep04-cita-paula.jpg`), EP.03 baja a la fila "Temporada 3".
- [ ] **Al salir el episodio:** comprobar oEmbed, `vercel --prod` y `curl -L` + diff contra el local.
