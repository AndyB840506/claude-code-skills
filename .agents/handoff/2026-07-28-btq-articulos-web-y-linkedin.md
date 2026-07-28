# Handoff: BTQ — guion EP.024, artículos de episodio en la web y su enganche a LinkedIn
**Date:** 2026-07-28 (martes — verificado contra `date`, no copiado)
**Machine:** desktop (E:\)
**Status:** Complete — todo lo desplegado está verificado en vivo; EP.024 espera grabación

---

## What We Accomplished This Session

**EP.024 — guion aprobado, pendiente grabación**
- Guion completo del Principio de Peter, esqueleto D (trenzado): 5.605 palabras = 42,8 min.
  Fuentes primarias abiertas antes de escribir (el PDF de Peter y el QJE 2019 de Benson,
  Li y Merkley). Artifact publicado.
- Retitulado con la **fórmula invertida**: `EP.24 — Por qué su mejor empleado se vuelve un
  mal jefe: el Principio de Peter` (78 caracteres). Primer episodio con la fórmula nueva.
- Se le quitaron 7 calcos del inglés (feedback de Andy) y **un agradecimiento a comentarios
  que no existían** — los analytics de EP.023 muestran 0 comentarios.

**Reglas de guion actualizadas** (`btq-production/guion-style-btq.md`)
- El guiño a comentarios del episodio anterior pasó a ser **condicional**.
- Se mató la calibración vieja (+35,5% / ÷150) y quedó el factor por esqueleto a 148 wpm,
  separando el registro histórico del texto normativo.
- Fórmula de título invertida, con la tabla de evidencia que la motivó.

**Analítica de EP.023 → decisiones**
- Tres estrategias de contenido dan primeras semanas estadísticamente iguales (15,9 / 15,9 / 14,0).
- La captación de oyentes nuevos cayó de 36 a 2 por mes; los recurrentes se mantienen ~31-39.
- Los episodios con nombre propio de cultura pop **convierten 4,6× peor** que los de teoría.
  Yo había recomendado lo contrario mirando solo impresiones; me retracté con los datos de consumo.
- Hora de lanzamiento **cerrada en 20:00**, con la razón escrita: los buckets diarios de
  Spotify no pueden responder esa pregunta, así que no se vuelve a abrir.

**Web — páginas de texto por episodio (lo nuevo de esta sesión)**
- `/episodios` (índice) y `/episodios/por-que-su-equipo-rinde-distinto-cuando-lo-miran`
  (EP.023 como artículo derivado, con JSON-LD `PodcastEpisode`).
- `ep.css` **replica `index.html`**, no un sistema propio. Corrección de Andy: la fuente del
  diseño es la web en vivo, no un documento.
- `sitemap.xml` (derivado del disco por `build-sitemap.py`) — `robots.txt` lo anunciaba desde
  siempre y el archivo nunca había existido.
- `og:image` **por episodio** (`/og/btq-ep023.png`): antes todos los artículos iban a compartir
  la imagen genérica y en el feed de LinkedIn se verían idénticos.
- `.vercelignore`: `/index-v2`, `/index-v3` y `/index-liner` estaban servidos con **200** —
  tres portadas viejas completas, indexables como duplicado de `/`. También salieron
  `build-sitemap.py` (código fuente público) y tres imágenes huérfanas (~4 MB).

**El artículo entra al kit de lanzamiento**
- `episode-launch/workflows/step2a-episode-article.md` (nuevo) — el artículo se escribe
  **antes** del plan social, porque los 4 posts de LinkedIn se cortan de él.
- `step2-generate-assets.md` §B.1 (nuevo) — qué link va en el primer comentario según el día:
  jueves/lunes/martes el artículo, domingo Spotify.

## Where We Paused

**Last action:** cierre de sesión — retrospectiva aplicada y auditoría del kit sin hallazgos.
**Next action:** grabar EP.024.
**Blockers:** todo lo que queda depende de Andy (grabación, jingle, Google Search Console).

## Files to Read First

- `btq-production/pipeline-state-ep024.md` — estado de EP.024 y su lista de pendientes
- `.claude/skills/episode-launch/workflows/step2a-episode-article.md` — el paso nuevo
- `.claude/skills/episode-launch/workflows/step2-generate-assets.md` §B.1 — reglas de LinkedIn
- `btq-production/guion-style-btq.md` — fórmula de título y calibración, ambas cambiadas hoy

## Notes / Gotchas

- **El deploy de BTQ es `vercel --prod` normal**, no el flujo prebuilt. `vercel.json` no
  tiene `ignoreCommand` (verificado hoy). MPD sí lo tiene — no confundirlos.
- **No agregar `overflow-x: hidden` a `html/body` de `ep.css`.** Se agregó creyendo que la
  página desbordaba en móvil; no desbordaba, fallaba la captura (Edge headless tiene un piso
  de ~492 px y `--window-size` no lo baja). Además rompe `position: sticky`. Para medir de
  verdad: cargar la página en un iframe del ancho objetivo y comparar `scrollWidth` con
  `innerWidth`. La advertencia quedó escrita dentro del CSS.
- **Las fuentes de marca hay que enlazarlas explícitamente** en cada página nueva
  (`api.fontshare.com`). Están instaladas en esta máquina, así que un render local se ve
  correcto aunque el `<link>` falte — no se detecta con capturas.
- **`brand-constants.md` NO está desactualizado.** Lo reporté como pendiente dos veces sin
  abrirlo; al abrirlo, el nombre «Sala de Máquinas» es el de la dirección de artwork v4 y el
  documento ya trae la anotación de qué sigue vigente. No volver a listarlo.
- **Los artículos arrancan en EP.023 y van hacia adelante.** EP.017–EP.022 quedan sin
  artículo por decisión de Andy — descartado a propósito, no pendiente olvidado.
- Assets de EP.023 en `E:\AI\outputs\BTQ-EP023\` (máquina de escritorio; no existen en el portátil).

## Questions to Answer

- **Jingle de EP.023: sin documentar.** `btq-production/jingle-brief.md:132` lo marca
  pendiente y **no hay ningún archivo de jingle ni stinger en `E:`** (verificado hoy con
  `find`). Falta que Andy diga cuál de las tres direcciones usó, su duración y dónde vive.
- **Google Search Console — aplazado por decisión de Andy hasta el reset.** El sitio ya está
  técnicamente limpio, pero enviar el sitemap y pedir indexación requiere entrar con su
  cuenta. Si las tres portadas viejas ya estaban indexadas, el 404 las saca sola pero puede
  tardar semanas; se acelera pidiendo la retirada en GSC.
- **Refrescar el preview de LinkedIn** antes del jueves: LinkedIn cachea por URL, así que si
  el enlace del artículo ya se compartió alguna vez, seguirá mostrando la tarjeta vieja hasta
  pasarlo por su Post Inspector.
