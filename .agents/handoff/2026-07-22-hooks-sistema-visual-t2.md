# Handoff: Hooks reactivos + sistema visual "La Guarida" (MPD T2)
**Date:** 2026-07-22 (segunda sesión del día)
**Status:** Complete — próxima sesión: redes sociales y overhaul de la web

---

## What We Accomplished This Session

**1. Hooks reactivos en `~/.claude/settings.json`** (scripts en `~/.claude/hooks/`)

Nacieron del pendiente que Andrés había diferido: convertir reglas críticas de memoria en algo que
el harness ejecute, porque las reglas escritas se ignoran en la práctica.

| Hook | Qué hace | Costo si no hay problema |
|---|---|---|
| `PreToolUse`/Bash | Bloquea cmdlets de PowerShell mandados por Bash (exit 127) | 0 |
| `PreToolUse`/Bash+PowerShell | Bloquea `-Encoding UTF8` (BOM); avisa en `-Encoding ASCII` | 0 |
| `Stop` | Avisa si hay trabajo sin commitear o sin pushear | 0 |

- **Verificados en vivo**, no solo en pipe-test: los dos `PreToolUse` bloquearon intentos reales
  durante la sesión — incluida una escritura mía con BOM que iba a corromper un `.py`.
- **`SessionStart` fue descartado a propósito.** Hacía `git pull` en cada arranque: ~824 ms fijos,
  peor caso 60 s de timeout, para prevenir un clon stale que mordió UNA vez en un mes. Andrés
  corrigió el enfoque: el proceso debe ser lean, los hooks son reactivos y de costo cero.
  Ver memoria `feedback_hooks_reactivos`.
- **Agujero encontrado y cerrado:** `claude-continuity` respaldaba `settings.json` pero NO
  `~/.claude/hooks/`. Restaurar en el portátil habría dejado los hooks apuntando a archivos
  inexistentes, fallando en silencio. `sync`/`install` ahora copian `config/hooks/` en las 4
  variantes (ps1 + sh), y las rutas usan `$env:USERPROFILE` en vez de `C:\Users\andre`.
- Se consolidó el hook de BOM duplicado: se eliminó `.claude/settings.json` del repo de skills
  (era un subconjunto del global).

**2. Resuelto el choque visual de MPD Temporada 2**

El handoff anterior lo dejó como cabo suelto: el specimen de identidad (ámbar/carretera, póster
ilustrado) no concordaba con la portada (foto de estudio victoriano).

- **Manda el artwork, y el argumento no es estético:** el specimen partía de "una cantina al borde
  de una carretera", iconografía derivada de **The Crossroads**, que es codename INTERNO. Construía
  identidad pública sobre un nombre que el público nunca verá, mientras *Den* —la guarida— no
  aparecía. Specimen viejo eliminado; el nuevo es `rebrand/identidad-la-guarida.html`.
- **Defecto medido en la portada vigente:** a 150 px (tamaño real en Spotify) el wordmark blanco
  sobre mármol pálido era un borrón y el "MPD" rojo desaparecía. Nadie lo había medido.
- **Lockup nuevo** en `comfyui/templates/mpd-lockup-t2.py`: Bookman Old Style Bold en vez de
  **Impact**, scrim en degradado arriba y abajo, título en una sola línea, sin "MPD" rojo ni los 5
  puntos, footer solo con iconos. `mpd-portada-compose.py` quedó **intacto** para el archivo de T1.
- **Paleta nocturna por contraste térmico.** Andrés objetó los cafés y pidió fríos. Diagnóstico: la
  escena era cálida en TODO (fuego, mármol, madera y sombras), lo que la aplanaba hacia "club de
  caballeros". Se generaron 5 gradings y se eligió el más frío (E). Parámetros congelados en
  `comfyui/templates/night_grade.py`.
- **Paleta muestreada del pixel real**, no propuesta a ojo: Medianoche #0B1A39, Tinta #151E3B,
  Humo #2C2F43, Piedra #55555B, **Brasa #D9BF7A (único acento cálido)**, Polvo #E7DDC9.
- **Artwork oficial:** `E:\Podcast\MPD\Temporada 2\artwork\MPD-T2-PORTADA-CONTEXTO-3000.jpg` y
  `MPD-T2-ESCENA-OFICIAL-3000.jpg` (escena sin texto, para episodios). Las versiones cálidas están
  en `alternativas\` — no se borró nada.

**Artifacts publicados:**
- Specimen: https://claude.ai/code/artifact/38786035-1d73-4558-b20b-d45244cf6b57
- Comparativa de las 5 temperaturas: https://claude.ai/code/artifact/eb4f0fd0-2f02-4885-9bd0-518a9a007997

## Where We Paused

**Last action:** `/session-close` — retrospectiva aplicada (8 aprendizajes), audit de skills limpio.
**Next action:** lo que Andrés pidió explícitamente para la próxima sesión:
1. **Teasers de revelación para redes sociales.** El gancho narrativo ya existe: el contraste
   T1 cálido → T2 azul nocturno es en sí mismo el anuncio del cambio.
2. **Overhaul de la página web** con el sistema de Temporada 2. Ya no está bloqueado: specimen y
   artwork hablan el mismo idioma.
**Blockers:** Ninguno.

## Files to Read First

- `mrputridsden-production/rebrand/identidad-la-guarida.html` — el sistema visual vigente.
- `comfyui/templates/night_grade.py` y `mpd-lockup-t2.py` — grading y lockup de T2.
- Memoria `project_mpd_rebrand_cruce_de_caminos` — reescrita con el sistema cerrado.
- Memoria `feedback_hooks_reactivos` — el principio lean antes de proponer automatización.

## Notes / Gotchas

- **Deuda técnica: el scrim está duplicado.** `comfyui/templates/scrim-overlay.py` ya existía
  (creado el 2026-07-21 por ESTE mismo problema) y hoy se reimplementó como `_scrim` dentro de
  `mpd-lockup-t2.py`, por buscar templates por nombre en vez de listar el directorio. Andrés
  decidió dejarlo anotado, no refactorizar al cierre. Si se toca ese archivo, unificar primero.
- **Deuda: `comfyui/docs/prompting.md` llegó a 220 líneas** y mezcla prompting con post-proceso
  (composición PIL, scrim, grading). Dividir en `artwork-composition.md` cuando se vuelva a tocar.
- **La web de MPD despliega SOLO por el flujo prebuilt** — verificar que `.vercel/project.json`
  tenga `projectName: mr-putrids-den-web`. Ver `deploy-preflight` Paso 1b.
- **T1 quedó en otro lenguaje visual** (cálido, Impact). Es coherente con que sea otra temporada.
  Si se quiere uniformar el catálogo, `night_grade.py` re-gradea EP.001–005 en lote — pero es
  decisión de Andrés, no se toca sin OK.
- Los hooks bloquean por regex; un comando de Bash que mencione un cmdlet como texto literal fuera
  de un heredoc dará falso positivo. El deny explica cómo seguir y cuesta un turno.

## Questions to Answer

- **El guion de T2·E1 tiene 5 marcadores `[VERIFICAR: ...]` sin resolver**, y hay que chequearlos
  ANTES de grabar (`mrputridsden-production/scripts/EP006-club-de-los-27.html`):
  1. Sobredosis de Roma (marzo 94) + anécdota de velas/lirios del Unplugged.
  2. Cita de Wendy Cobain sobre "ese club estúpido" — reportada, no transcripción confirmada.
  3. Cifras del estudio BMJ 2011: 1.046 músicos, 71 muertes / 7% durante el seguimiento.
  4. Edades: Lennon 40, Elvis 42, Bowie 69, Prince 57, Avicii 28, Mac Miller 26.
  5. Cita de Neil Young ("it's better to burn out than to fade away") en la nota de Cobain.
- ¿Se re-gradean las portadas de EP.001–005 con `night_grade.py` para uniformar el catálogo?
