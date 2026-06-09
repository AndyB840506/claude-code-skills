# Workflow 04 — Rotación del grid "Episodios recientes"

**Misma regla para ambos shows** (confirmada con el usuario): el grid de 4 cards
muestra los 4 episodios ANTERIORES al que está en circulación — el nuevo NO se agrega
al grid porque su propio embed/link ya lo cubre. Al lanzar: rota — entra el anterior al
nuevo, sale el más antiguo. Orden oldest -> newest, izquierda a derecha / arriba a abajo.

La lógica de rotación es idéntica en ambos sitios. Lo único que cambia es el markup —
**cada show usa su propio sistema visual, nunca el del otro** (ver memoria
`feedback_mpd_vs_btq_typography`).

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

---

## Paso 1 — Leer el grid actual

Abre el `index.html` del show correspondiente y localiza el contenedor del grid:

| Show | Contenedor | Card | Campos por card |
|---|---|---|---|
| BTQ | `<div class="ep-list stagger">` en `btq-production/website/index.html` | `<a class="ep-row" href="[spotify URL]">` | `.ep-num` (3 dígitos), `.ep-body > .ep-ref-tag` (referencia cultural), `.ep-row-title`, `.ep-row-quote`, `.ep-arrow` |
| MPD | `<div class="episodes-grid">` en `mrputridsden-production/website/index.html` | `<div class="episode-card" data-ep="0XX">` | `.ep-number`, `.ep-title`, `.ep-meta` (duración · fecha · "Co-host"/invitado), `.ep-description`, `.ep-link` (con SVG + href de Spotify) |

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

**Ejemplo concreto** (mismo patrón documentado para BTQ en
[btq-project/SKILL.md:254-257](C:\Users\andre\.claude\skills\btq-project\SKILL.md#L254-L257)):
si el grid actual muestra `012, 013, 014, 015` y se lanza `EP.017` (lo que significa que
`EP.016` era el que estaba en circulación), el grid rotado queda `013, 014, 015, 016`
— `012` sale, `016` entra, `017` NO aparece (su embed ya lo cubre).

Si tienes dudas sobre cuál era "el episodio en circulación" antes de este lanzamiento
(por ejemplo, hay un salto de números o el grid está desactualizado), **pregunta al
usuario antes de tocar el markup** — no asumas (ver memoria `feedback_confirm_domain_logic`).

---

## Paso 3 — Editar el markup

**BTQ**: usa los campos del episode brief + lo generado en Stage 2 (`episode-launch`)
para la card que entra — `cultural_ref` → `.ep-ref-tag`, título → `.ep-row-title`, una
cita/frase representativa del episodio → `.ep-row-quote`, número de 3 dígitos →
`.ep-num`, URL de Spotify → `href` del `<a class="ep-row">`.

**MPD**: usa los campos del episode brief + lo generado en Stage 2
(`shownotes-ep[NNN].md` / `youtube-ep[NNN].md`) para la card que entra — número →
`.ep-number` y `data-ep`, título → `.ep-title`, duración/fecha/formato → `.ep-meta`,
descripción breve → `.ep-description`, URL de Spotify → `href` del `.ep-link` (conserva
el SVG existente, solo cambia el texto y el href).

En ambos casos: edita las 4 cards para que reflejen el grid rotado — no agregues una
quinta ni dejes la que sale.

---

## Al terminar

1. Confirma: "Grid de [show] rotado — [lista de 4 episodios resultante]." y continúa a
   `05-deploy-verify.md`.
2. Agrega a la bitácora:
   ```
   ## Stage 4 — Rotación de grid
   - Qué se hizo: grid de [show] rotado de [grid anterior] a [grid nuevo]
   - Episodio que entra: EP.0XX | Episodio que sale: EP.0YY
   - Archivo modificado: [ruta a index.html]
   - Resultado: OK
   ```
