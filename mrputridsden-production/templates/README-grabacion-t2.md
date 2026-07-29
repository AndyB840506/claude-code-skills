# Template de grabación — Mr. Putrid's Den, Temporada 2

> Creado 2026-07-28, a partir del proyecto real de **T2·01 «El Club de los 27»** ya publicado.
> Existe porque la cadena de FX original se armó siguiendo un video de YouTube y traía tres
> parámetros mal — no de oído, sino medibles. Este template los deja fijos.

## Archivos

| Archivo | Qué es |
|---|---|
| `MPD-T2-grabacion.RPP` | Proyecto de Reaper con los bumpers ya colocados y la cadena de FX |
| `masterizar-podcast.ps1` | Convierte el WAV renderizado en el MP3 final, medido y verificado |

---

## Flujo de una grabación

1. **Copiar** `MPD-T2-grabacion.RPP` a la carpeta del episodio nuevo y renombrarlo.
2. **Grabar** el cuerpo en la pista `My Vocal`.
3. **Colocar el cuerpo en `POSITION 35.5`** — ahí termina la música de intro. Ni antes ni después.
4. **Mover el outro** al final del cuerpo (es lo único que cambia de sitio en cada episodio).
5. **Renderizar a WAV 24-bit.** No a MP3 — así el MP3 se codifica una sola vez.
6. **Correr el masterizador:**
   ```powershell
   .\masterizar-podcast.ps1 "E:\Podcast\MPD\Temporada 2\EP 0X\MPD EP 0X.wav"
   ```
   Imprime una tabla con OK/FALLA contra los targets y avisa si hay que ajustar la ganancia.

---

## La apertura fija — no se re-negocia cada episodio

Son bumpers reutilizables. Ya vienen en el template en estas posiciones exactas:

| Pieza | Entra | Sale | Notas |
|---|---|---|---|
| Logo sonoro | 0:00,0 | 0:04,5 | `SOFFS 1.0`, fade-in **0,05 s** |
| Disclaimer | 0:04,0 | 0:17,5 | 28 palabras, sin susurro |
| Música de intro | 0:17,5 | 0:35,5 | `SOFFS 12.0` — arranca dentro del track |
| **Cuerpo del episodio** | **0:35,5** | — | ← lo único que cambia |
| Outro | fin del cuerpo | +17,3 s | `SOFFS 41.5`, fade-out 2 s |

**Apertura total: 35,5 s.** El brief pide ~35 (`audio/t2-disclaimer-e-intro.md`). El piloto llegó a
57 s y el feedback fue explícito: *"tal vez el intro y el outro son muy largos"*.

### Por qué esos `SOFFS` raros

- **Logo `SOFFS 1.0`:** el archivo fuente dura 13 s pero el gesto real vive entre 2,1 y 7,6 s; lo
  demás es cola. Además traía **doble fade-in** — el propio del archivo más 3,56 s puestos en Reaper,
  o sea que la firma tardaba ~3,5 s en aparecer en un logo que debe durar 3-5 s enteros.
- **Intro `SOFFS 12.0`:** los primeros 8 s de `The_Locked_Porch` son casi silencio. La meseta
  hipnótica está en 16-30 s del track.
- **Outro `SOFFS 41.5`:** el track tiene **7 s de silencio digital en el medio** (34-41 s). Arrancar
  en 40 metía 2 s de nada al empezar el outro.

---

## Los tres parámetros que estaban mal

| # | Qué | Estaba | Debe |
|---|---|---|---|
| 1 | Techo del limitador del máster | 0,0 dBFS | **−2,0 dBFS** |
| 2 | Nivel integrado del render | −18,3 LUFS | **−16 LUFS** |
| 3 | Fade-in del logo | 3,56 s | **0,05 s** |

**El 1 y el 2 ya no se arreglan en Reaper.** Se arreglan en `masterizar-podcast.ps1`, fuera de Reaper,
porque así es determinista y medible en vez de a oído. El render de Reaper puede seguir saliendo a
−18,3: el script se encarga.

Lo que sí importa que Reaper no haga: **no subir el limitador ni normalizar al renderizar.** Si el
WAV llega ya topado a 0 dBFS, el masterizador tiene que trabajar contra eso.

---

## Qué está verificado y qué no

**Verificado por medición** sobre el episodio publicado:

- La cadena produce **LRA 6,6 LU**, que es sano para voz hablada. La cadena **no está rota**.
- El máster resultante da −16,0 LUFS · LRA 6,5 · true peak −1,2 dBFS. Pasa Spotify y Apple.
- El limitador trabaja picos, no dinámica: el LRA solo cae 0,1 LU.

**NO verificado — nunca se inspeccionó ni se escuchó:**

- Los ajustes internos de `Podcast EQ`, `Podcast Comp` y `Podcast De-Esser`. Viven como estado
  serializado del plugin dentro del `.RPP` y no se pueden leer desde fuera.
- Si la curva de EQ o el de-esser le convienen a esta voz en particular.

O sea: la cadena está **medida en su resultado**, no auditada en su interior. Si algún día suena
mal y las métricas están bien, el problema está en esos tres plugins y hay que abrirlos a oído.

---

## Checklist antes de publicar

- [ ] Cuerpo en `POSITION 35.5`
- [ ] Outro pegado al final del cuerpo
- [ ] Renderizado a **WAV**, no a MP3
- [ ] `masterizar-podcast.ps1` dice **LISTO PARA PUBLICAR**
- [ ] Transcribir con `/transcriptor` y **cruzar el SRT contra los bloques `dato`/`leyenda`** del
      guion — en T2·01 se leyó al aire una nota de producción y hubo que cortar 7,9 s
      (ver `guion-style-mpd.md` § Bloques que no se leen)
