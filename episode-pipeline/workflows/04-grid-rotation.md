# Workflow 04 — Rotación del grid "Episodios recientes"

**Este workflow aplica a BTQ.** Para MPD ver la sección "MPD — acumulación de
Expedientes" al final: desde el rediseño "La Guarida" (2026-07-22) el sitio de MPD ya
no usa un grid de 4 cards que rota — usa un patrón distinto, decidido con Andrés el
2026-08-14.

**Regla de ROTACIÓN para BTQ** (confirmada con el usuario): el grid de 4 cards muestra
los 4 episodios ANTERIORES al que está en circulación — el nuevo NO se agrega al grid
porque su propio embed/link ya lo cubre. Al lanzar: rota — entra el anterior al nuevo,
sale el más antiguo.

**Orden visual de BTQ** (`btq-production/website/index.html`): descendente, el más
reciente de los 4 primero, arriba a abajo (verificado en vivo 2026-07-05 al lanzar
EP.020: grid pasó de `018,017,016,015` a `019,018,017,016` — 019 arriba, no abajo).

Antes de editar el markup, confirma el orden real leyendo las 4 cards actuales
(Paso 1) — no asumas a partir de un ejemplo genérico.

---

## Paso 0 — Confirmar que `spotify_url` ya es una URL real

**No escribas "pending" en el markup del sitio.** Antes de tocar el grid, revisa
`spotify_url` en el episode brief / `pipeline-state-ep[NNN].md`:

- **URL real presente** → continúa normalmente al Paso 1
- **Sigue como "pending"** → detente aquí mismo: "Necesito la URL pública de Spotify
  para EP.0XX antes de rotar el grid — el `href` de la card que entra depende de eso.
  ¿Ya está publicado? Pásame la URL cuando esté disponible y seguimos justo desde
  aquí." Esto puede pasar incluso dentro de la misma sesión si el checkpoint de
  Spotify (cierre de Stage B en `02-assets.md`) no se resolvió todavía — no asumas que
  ya se resolvió solo porque la sesión sigue corriendo.

**OJO — también revisa la URL del episodio que ENTRA al grid (el anterior al que se
lanza).** La card que se agrega NO es la del episodio que se lanza, es la del anterior
(que estaba en circulación, ver Paso 2). Su URL de Spotify puede estar `pending` /
sin registrar aunque la del episodio nuevo ya esté en vivo — pasó con EP.017 el
2026-06-22 (su URL nunca se anotó desde su propio lanzamiento). Si el `spotify_url`
del episodio que entra no está registrado en su launch file / roadmap, pídela al
usuario (verificada desde el browser, regla EP.016) **antes** de tocar el markup —
no pongas "pending" en un `href`. Al obtenerla, propágala también al launch file +
roadmap de ESE episodio, no solo úsala en la card.

**Y lo mismo para el episodio QUE SE LANZA:** al recibir su URL, escríbela en su propio
launch file (línea `Live:`/`Spotify URL`) además del roadmap — la de EP.020 quedó
"pendiente" en su launch file desde su propio lanzamiento y solo se registró al rotar
el grid de EP.021 (2026-07-13).

---

## Paso 1 — Leer el grid actual

Abre `btq-production/website/index.html` y localiza el contenedor del grid:

| Show | Contenedor | Card | Campos por card |
|---|---|---|---|
| BTQ | `<div class="stag">` (sección `#tracklist`) | `<a class="track" href="[spotify URL]">` | `.t-num` (3 dígitos), `.t-ref` (referencia cultural), `.t-title`, `.t-quote`, `.t-right` (bloque "Escuchar →") — clases verificadas en vivo 2026-07-13 (EP.021); los nombres anteriores `ep-list`/`ep-row` eran de un markup viejo |

Anota las 4 cards actuales en orden — son tu punto de partida para el diff.

---

## Paso 2 — Calcular el grid rotado

Dado que el episodio que se está lanzando es EP.0XX (el `ep_number` del episode brief):

1. **El nuevo NO entra al grid.**
2. El episodio que estaba "en circulación" antes de este lanzamiento (= el que tenía el
   slot del embed/Spotify-disponible-ahora) **entra** al grid, al final (posición más
   reciente).
3. El más antiguo de las 4 cards actuales **sale**.
4. Las otras 3 cards se mantienen, recorriéndose una posición hacia "más antiguo".

**BTQ es descendente** (verificado en vivo 2026-07-05, lanzamiento EP.020): el grid
mostraba `018, 017, 016, 015` y se lanzó `EP.020` (lo que significa que `EP.019` era
el que estaba en circulación) → el grid rotado quedó `019, 018, 017, 016` — `015`
sale, `019` entra AL PRINCIPIO (posición más reciente, no al final).

Si tienes dudas sobre cuál era "el episodio en circulación" antes de este lanzamiento
(por ejemplo, hay un salto de números o el grid está desactualizado), **pregunta al
usuario antes de tocar el markup** — no asumas (ver memoria `feedback_confirm_domain_logic`).

---

## Paso 3 — Editar el markup

Usa los campos del episode brief + lo generado en Stage 2 (`episode-launch`) para la
card que entra — `cultural_ref` → `.t-ref`, título → `.t-title`, una cita/frase
representativa del episodio → `.t-quote`, número de 3 dígitos → `.t-num`, URL de
Spotify → `href` del `<a class="track">`.

Edita las 4 cards para que reflejen el grid rotado — no agregues una quinta ni dejes
la que sale.

**No olvides el badge "Última pista" / hero del episodio más reciente** (`<a
class="latest">` cerca del top de `index.html`, fuera del contenedor del grid de 4
cards) — es un elemento SEPARADO que también debe apuntar al episodio que se está
lanzando ahora (EP.0XX), no al que entra al grid. Confirmado como hueco real: tras el
lanzamiento de EP.018 (2026-06-22) el grid de 4 cards se rotó correctamente pero este
badge quedó apuntando a EP.017 hasta que se detectó y corrigió el 2026-06-29.

---

## Al terminar

1. Confirma: "Grid de BTQ rotado — [lista de 4 episodios resultante]." y continúa a
   `05-deploy-verify.md`.
2. Agrega a la bitácora:
   ```
   ## Stage 4 — Rotación de grid
   - Qué se hizo: grid de BTQ rotado de [grid anterior] a [grid nuevo]
   - Episodio que entra: EP.0XX | Episodio que sale: EP.0YY
   - Archivo modificado: [ruta a index.html]
   - Resultado: OK
   ```

---

## MPD — acumulación de Expedientes (no rotación)

**Decidido con Andrés el 2026-08-14.** El sitio de MPD (`mrputridsden-production/website/index.html`)
no tiene grid de 4 cards desde el rediseño "La Guarida" (2026-07-22). Cada expediente
del pilar "Archivos Secretos del Rock" (ver memoria `project_mpd_archivos_secretos_pillar`)
tiene su propia sección completa, y esas secciones **se acumulan indefinidamente** — no
hay rotación, no hay archivado automático de expedientes de T2.

**Markup real** (verificado 2026-08-09 en el fix del sitio, confirmado en vivo 2026-08-14):
cada expediente es una `<section class="band" id="expedienteNN">` con un `.case`
(`.case-art` = portada 340px + figcaption, `.case-body` = `<h3>` título, párrafos,
`.roll` con los nombres/hechos clave, `.btn-outline` con el link de Spotify). Ver
Expediente 01 (`id="expediente"`) y Expediente 02 (`id="expediente02"`) como plantilla.

**Al lanzar un expediente nuevo (EP.0X):**
1. Duplica la sección `.case` del expediente anterior, cambia el `id` a `expediente0X`.
2. Rellena portada, título, párrafos y `.roll` desde el episode brief / show notes.
3. Cambia el `href` del `.btn-outline` a la URL real de Spotify (nunca "pending" — mismo
   Paso 0 que BTQ).
4. Mueve el hero (`.file` en `#hero`) para que apunte al expediente nuevo — el anterior
   se queda con su sección `.case` completa en el body, ya no en el hero.
5. Actualiza el embed de "Sintoniza" (`#escucha`) al episodio más reciente.
6. Actualiza el índice de nav (`<nav class="bar-nav">`) si el ancla `#expediente0X` no
   está enlazada.

**"El Archivo" (`id="archivo"`) es solo para Temporada 1** — la lista compacta de 5 filas
de EP.001-005. Los expedientes de T2 NUNCA bajan a esa lista ni a ninguna otra; se
quedan como sección `.case` completa para siempre. Si en el futuro la página se vuelve
demasiado larga, es una decisión nueva de Andrés, no automática — no archivar por
iniciativa propia.
