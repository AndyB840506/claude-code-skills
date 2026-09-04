# YouTube Metadata — MPD EP.04 (T2·E4)

**Nota:** canal de YouTube de MPD está `pendiente` en `podcast-profile.json` (por crear) — esta metadata queda lista para cuando exista.

## A. Título (máx 60)

`Fingieron la muerte de Paul McCartney | EP.04`
→ **45 caracteres ✓** (verificado con `.Length`)

## B. Descripción

**Primeras 3 líneas:**
En 1969 un estudiante inventó como broma la muerte de Paul McCartney. Medio mundo armó las pruebas usted mismo. EP.04 de Mr. Putrid's Den — Escúchalo en Spotify: https://open.spotify.com/show/0M12ujB9eJqr0dWZUwEf6B

**Descripción completa** (misma base que `ep04-metadata.md` §C, adaptada a YouTube — más densa en keywords, incluye link de YouTube):

```
En 1969, un estudiante aburrido de escribir reseñas de discos inventó una broma en una sola noche. Cincuenta y seis años después, todavía hay gente que no está segura de que fuera mentira.

En este episodio de Mr. Putrid's Den abrimos el Expediente 04: cómo Fred LaBour, estudiante de periodismo de la Universidad de Michigan, escribió por venganza contra el género de la crítica musical un artículo que decía que Paul McCartney llevaba muerto desde 1966 — y cómo, sin que él moviera un dedo más, miles de desconocidos se pusieron a armar las pruebas ellos mismos, disco por disco, portada por portada.

En este episodio:
✦ Quién era Fred LaBour y por qué escribió el artículo más ridículo que se le ocurrió — sin esperar que nadie se lo creyera
✦ El rumor que ya había fallado dos veces antes de 1969, y qué cambió esta vez
✦ Las "pistas" que el propio público encontró solo, sin que nadie coordinara nada — de Abbey Road a "cranberry sauce"
✦ Lo que pasó cuando encontraron a Paul de verdad — y cómo la misma maquinaria de fabricar dobles siguió funcionando después: Avril Lavigne, los reptilianos, Justin Bieber

La última palabra siempre es suya.

Escúchanos también en Spotify, Apple Podcasts, Amazon Music y más — link en bio.
🌐 www.mrputridsden.com
📱 Instagram: @mrputridsden
✉️ hello@mrputridsden.com

#MrPutridsDen #ArchivosSecretosDelRock #MisteriosYLeyendas #LeyendasDelRock #PaulIsDead #PodcastDeMisterio
```

## C. Tags / Keywords (15-20)

`Mr. Putrid's Den, MrPutridsDen, La Guarida, Paul is Dead, Fred LaBour, Michigan Daily, Beatles conspiracy theory, Abbey Road hidden clues, Paul McCartney double, Avril Lavigne conspiracy theory, Melissa Vandella, reptilian theory Justin Bieber, leyendas del rock, misterios del rock, podcast de misterio en español, mitos del rock, podcast rock Bogotá`

→ 18 tags

## D. Texto de miniatura

`PAUL ESTÁ MUERTO`

(alto contraste, serif Bookman Old Style Bold sobre paleta "La Guarida" — azul nocturno #0B1A39 + brasa #D9BF7A; sin pentagramas/tarot/símbolos ocultistas ni rostros reconocibles, ver `podcast-profile.json` § logo_descripcion y [[feedback_mpd_no_occult_symbols]] / [[feedback_no_real_person_likeness_override]])

## E. Capítulos / Timestamps

Verificados contra el SRT real (`E:\Transcriptor\transcripciones\MPD EP 04.srt`), no contra los rangos estimados del guion — el guion estimaba Acto I desde 07:30 y el cierre desde 39:00 sobre una duración total de ~43 min; el episodio real corrió mucho más corto (31:53). **Nota:** timestamps del archivo crudo (mp3 exportado de Reaper) — si Andrés agrega bumpers/intro/outro musicales en una masterización posterior que corran el inicio del archivo, todos los capítulos se desplazan por ese offset; re-verificar contra el archivo final antes de publicar en YouTube.

```
00:00 Cold open — Detroit, 12 de octubre de 1969
02:16 Bienvenida al Expediente 04
04:35 Contexto — el rumor con antecedentes
05:32 Acto I — El estudiante que inventó al doble
21:06 Acto II — Las pruebas que el público fabricó solo
25:33 Acto III — Los dobles que vinieron después
31:25 Cierre
```

**Verificación de las 3 reglas duras (contra el audio real, 31:53):**
- Primer capítulo en 00:00 ✓
- 7 capítulos (mínimo 3) ✓
- Duración de cada capítulo (contra el siguiente, el último contra 31:53):
  - 00:00→02:16 = 136s · 02:16→04:35 = 139s · 04:35→05:32 = 57s · 05:32→21:06 = 934s · 21:06→25:33 = 267s · 25:33→31:25 = 352s · **31:25→31:53 = 28s**
  - Todos ≥10s ✓ (margen amplio en los 7; medido, no estimado — ver script de verificación en la bitácora)

---

```
══════════════════════════════════════════
  YouTube metadata generada ✓
══════════════════════════════════════════
  Episodio:           EP.04 (T2·E4)
  Título:             45 chars ✓
  Tags:               18 terms
  Capítulos:          7 bloques · primero en 00:00 ✓
                      más corto: 28 s / mín 10 s ✓
  Archivo:            episodios/temporada-2/youtube-ep04.md
══════════════════════════════════════════
```
