# Paso 2a · Artículo del episodio

Escribe la página de texto del episodio en `behind-thequeue.com/episodios/<slug>`.

**Va ANTES del plan social**, no después: los cuatro posts de LinkedIn se cortan del
artículo (ver `step2-generate-assets.md` §B.1). Si se escriben primero los posts, cada
uno vuelve a destilar el guion por su cuenta y aparecen afirmaciones que el artículo no
sostiene.

## Por qué existe

El audio no se indexa. Sin texto no hay Google, y no hay nada que un modelo de lenguaje
pueda citar cuando alguien le pregunta por el tema del episodio. Además, la audiencia
núcleo es supervisor/gerente BPO que abre LinkedIn el lunes por la mañana **en el
trabajo**: puede leer, no puede darle play.

## Qué es y qué no es

Es un **artículo derivado**, no la transcripción. Destila el guion a: tesis, las cifras
con su fuente, los casos, la aplicación práctica y el bloque de fuentes. Después de
leerlo tiene que seguir habiendo razón para escuchar el episodio — el guion tiene
desarrollo, digresiones y voz que el artículo no reproduce.

Toda cifra que aparezca debe poder rastrearse hasta la fuente listada. Si un dato del
guion no se puede atribuir, **no entra al artículo**.

## Procedimiento

1. **Leer el guion completo** (`btq-production/launch-assets/EPNNN-*-guion.html`). No es
   mecánico: es redacción.

2. **Slug.** Del título del episodio, sin número de EP, en minúsculas y sin tildes:
   `por-que-su-equipo-rinde-distinto-cuando-lo-miran`. Es la URL permanente — no se
   cambia después de publicar.

3. **Copiar la imagen del preview:**
   ```powershell
   Copy-Item "E:\AI\outputs\BTQ-EPNNN\BTQ-EPNNN-COVER-16x9.png" `
             "btq-production\website\og\btq-epNNN.png" -Force
   ```
   Es la portada, **no** una quote card (razón en §B.1).

   **Si la portada es una escena renderizada (excepción puntual, no tipografía pura),
   guardarla como JPEG, no PNG.** El PNG de una portada 100% tipográfica pesa ~50 KB; el
   mismo tamaño con una escena/textura fotográfica de fondo pesa ~900-1000 KB, muy por
   encima del límite de 500 KB de `brand-constants.md`. Convertir con
   `im.save(path, "JPEG", quality=90, optimize=True)` — a esa calidad da ~150-200 KB para
   una escena típica. Verificar el tamaño final con `os.path.getsize()` antes de dar por
   copiado el asset (bit 2026-08-07, BTQ EP.025: se copió el PNG a 972 KB sin medirlo).

4. **Escribir el HTML** copiando la estructura del artículo de EP.023 —
   `website/episodios/por-que-su-equipo-rinde-distinto-cuando-lo-miran.html` es la
   plantilla viva. No inventar clases: `ep.css` replica el sistema de `index.html`.

   Esqueleto:
   ```
   head:  title · description · canonical · fuentes Fontshare · /ep.css
          og:type article · og:title/description/url
          og:image = /og/btq-epNNN.png (1920x1080) + og:image:alt
          JSON-LD PodcastEpisode (episodeNumber, datePublished, partOfSeries)
   body:  .grain · header del sitio
          section.ep-head  → .ep-kick, h1 (con <em> en la palabra clave), .ep-lede
          div.ep-grid      → varias section.blk con .sec-tag numerado ("01 — El origen")
                             última: section.blk.fuentes
                           → aside.rail (sticky: CTA de escucha + datos del episodio)
          footer .colo
   ```

5. **Enlazar desde el índice:** agregar la entrada en `website/episodios/index.html`
   dentro de `.lista`. Los `.t-title` / `.t-sub` son `<span>` y necesitan
   `display:block` — ya está en `ep.css`, no re-declarar.

6. **Regenerar el sitemap:** `python website/build-sitemap.py` (lo deriva del disco).

7. **Verificar antes de desplegar:**
   - `python -c "import json,re; ..."` — el JSON-LD parsea
   - el XML del sitemap está bien formado y contiene la URL nueva
   - captura a 1280px y a 390px **reales** (medir dentro de un iframe: Edge headless
     tiene un piso de ~492px y `--window-size` no lo baja)
   - cada `<img>` con regla de `width` lleva `height:auto` en la MISMA regla

8. **Desplegar** con el flujo de `deploy-preflight` (Vercel `--prod`, sin `ignoreCommand`).

## Cuándo se publica

**El domingo, junto con el episodio.** Antes no: el CTA de escucha del riel no tendría
a dónde apuntar. El post de intriga del jueves sí puede enlazarlo — para entonces el
artículo ya está escrito y en revisión, se despliega el domingo.

## Alcance: de EP.023 en adelante

**Decisión de Andy, 2026-07-28: no se escribe el atraso.** El artículo arranca en EP.023
(ya publicado) y de ahí en adelante cada episodio nace con el suyo dentro del kit.

EP.017–EP.022 tienen guion guardado pero **no** llevan artículo; EP.001–EP.016 ni
siquiera tienen guion en texto. No proponer el retro-llenado como pendiente — está
descartado a propósito, no olvidado. Si algún día se retoma, será una decisión nueva.
