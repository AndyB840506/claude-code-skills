# Handoff: MPD Temporada 2 — identidad completa en los cuatro frentes
**Date:** 2026-07-22 (tercera sesión del día)
**Status:** Complete — la identidad de T2 quedó consistente en web, portada, redes y metadata. Pendiente: grabar T2·E1.

---

## What We Accomplished This Session

**1. Overhaul de la web (mrputridsden.com) — live**

No fue un reskin: la web era la Temporada 1 entera (neón blanco parpadeante, carmesí, vinilo
girando, fundas de disco, "la carta de la casa", tagline de riffs y whisky).

- Hero: la escena oficial de T2 como telón fijo con scrim, wordmark en serif sobre la zona
  oscura. Fuera el neón (una condensada de cartel moderno, prohibida en el specimen), el vinilo
  y el VU meter.
- Secciones nuevas: `#guarida` (qué es el show ahora), `#expediente` (Expediente 01 con la
  portada), `#archivo` (T1 completa, 5 filas, links de Spotify intactos), `#residente`,
  `#escucha`, `#contacto`.
- **Easter eggs recontextualizados:** los objetos de la sala nombran a los muertos del Club de
  los 27 (incluidos Alan Wilson y Robert Johnson). Se posicionan calculando la geometría real
  del `cover` en JS — los anteriores usaban porcentajes de viewport y se despegaban al cambiar
  el aspect ratio.
- Lenguaje tomado del guion, no inventado: "Archivos Secretos del Rock" y "Expediente 01" son
  las palabras que Andrés dice al aire.

**2. Kit de redes (6 piezas) + arco de revelación (4 beats)**

- `comfyui/templates/mpd-social-kit.py`: avatar 1500, portada FB 1640x624, post IG 1080, story
  1080x1920, banner YouTube 2560x1440, cabecera X 1500x500. Salida en
  `E:\Podcast\MPD\Temporada 2\redes\`.
- `social-t2-revelacion.md`: copy para IG y Facebook en 4 beats. TikTok sigue en pausa y X no
  está activo — no se generó copy para ninguna.
- **Teaser de la sábana** (idea de Andrés): la portada bajo una tela guardapolvo. La tela se
  generó AISLADA sobre negro en ComfyUI, no como escena completa con un cuadro debajo — así el
  que decide cuánto artwork se revela es el compositor, no el modelo. Scripts
  `mpd-teaser-sabana-gen.py` y `mpd-teaser-sabana.py`.

**3. Brasa #D9BF7A queda como acento canónico**

Había dos ámbares en circulación: la portada en Spotify usaba `#CE8B3A` y el specimen más la
web usaban brasa. Andrés decidió brasa y recomponer la portada. `mpd-lockup-t2.py` actualizado
y portada regenerada (1.749 px brasa, 0 del ámbar viejo).

**4. Metadata del show para Spotify**

`show-metadata-t2.md` + `podcast-profile.json` actualizado. El perfil seguía siendo T1 entero:
paleta crimson `#9B1C1C` y `logo_descripcion` pidiendo "vinilos, pósters de concierto" —
cualquier artwork generado desde ahí habría salido en la identidad vieja.

**5. Retrospectiva aplicada (5 cambios)**

`deploy-preflight` (verificar el proyecto contra el dominio live), `04-social-media.md` (rama de
arco de revelación sin fecha), `05-show-notes.md` (tope de 600 chars a nivel show),
`web-page-kit/design-guide.md` (regla `height:auto`), y se pagó la deuda de `prompting.md`:
dividido en `artwork-composition.md` (234 → 157 líneas).

## Where We Paused

**Last action:** `/session-close` — retrospectiva aplicada, audit de skills sin hallazgos reales.
**Next action:** **grabar T2·E1**. Antes de grabar hay que resolver los marcadores `[VERIFICAR]`
del guion (ver Questions).
**Blockers:** ninguno técnico. Todo lo que falta depende de que Andrés grabe y suba assets.

## Files to Read First

- `mrputridsden-production/show-metadata-t2.md` — lo que hay que pegar en las plataformas.
- `mrputridsden-production/social-t2-revelacion.md` — el copy de los 4 beats.
- `comfyui/docs/artwork-composition.md` — **doc nuevo**, post-proceso PIL separado de prompting.
- Memoria `reference_mpd_website_live` — reescrita con la trampa del project-link.

## Notes / Gotchas

- **La trampa que casi rompe el deploy:** el proyecto de Vercel se renombró el 2026-07-19 y
  tanto `.vercel/project.json` como la memoria seguían nombrando a `v0-mr-putrids-den`, que
  quedó huérfano. Desplegar ahí **reporta éxito y deja producción intacta**, sin error visible.
  El proyecto real es `mr-putrids-den-web`. Verificar SIEMPRE con
  `vercel inspect https://www.mrputridsden.com --scope mrputridsden` → campo `name`.
- **Verificar contra el dominio, no contra el mensaje del deploy.** Una lectura post-deploy
  devolvió caché de edge y parecía que no había subido. Usar cache-buster y confirmar
  `X-Vercel-Cache: MISS`.
- **El shader WebGL de la web nunca corrió** — hacía `getContext` sobre un `<div>`. Eran ~55
  líneas de GLSL muertas desde siempre; no se portaron.
- **`og:image` apuntaba a un `.png` que nunca se subió** — las previews en redes llevaban rotas
  quién sabe cuánto. Ahora existe `og-image.jpg` y responde 200.
- El `CLAUDE.md` de la skill `mrputridsden` documentaba el grid con `.episode-card` /
  `.episodes-grid`, clases que el overhaul eliminó. Reescrito. También mandaba a correr
  `vercel --prod`, que publica vacío y da 404.
- **No prometer fecha ni duración de un episodio sin grabar.** La estimación de EP.005 falló
  por 6 minutos. El estado se expresa "Expediente: Abierto".
- ComfyUI quedó detenido al cerrar (se relanza en ~30 s).
- La constante `MEDIANOCHE` de `mpd-lockup-t2.py` mentía: valía `(20,17,16)`, un casi-negro
  cálido, no el `#0B1A39` de la paleta. Renombrada a `FOOTER_DARK` conservando el valor.

## Questions to Answer

- **El guion de T2·E1 tiene 7 marcadores `[VERIFICAR]` sin resolver** y hay que chequearlos
  ANTES de grabar (`mrputridsden-production/scripts/EP006-club-de-los-27.html`): sobredosis de
  Roma, cita de Wendy Cobain, cifras del estudio BMJ 2011, edades de Lennon/Elvis/Bowie/Prince/
  Avicii/Mac Miller, y la cita de Neil Young en la nota de Cobain.
- **Pendiente manual de Andrés, bloquea el Beat 1 de redes:** subir la portada nueva
  (`MPD-T2-PORTADA-CONTEXTO-3000.jpg`) y las descripciones a Spotify/Apple/Amazon. Si el
  teaser del contraste sale con la portada vieja todavía en el perfil, el arco se rompe.
- **Categoría de Spotify sin confirmar:** propuse Music › Music History + Society & Culture ›
  Documentary, pero no salieron de documentación oficial. Confirmar los rótulos en el panel.
- **Decisión editorial abierta:** el show pasa a tratar muertes, sobredosis y suicidios de forma
  recurrente. Para el marcado "explícito" de la plataforma sigue siendo No, pero queda por
  decidir si los episodios abren con una nota de contenido.
- ¿Se re-gradean las portadas de EP.001–005 con `night_grade.py` para uniformar el catálogo?
  (Sigue abierta desde el handoff anterior — es decisión de Andrés, no se toca sin OK.)
