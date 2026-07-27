# Step 4a — SafeCreative: RETIRADO (2026-07-26)

> ⚠️ **BTQ ya no registra episodios en SafeCreative.** Decisión de Andy, 2026-07-26.
> No generar la metadata de registro ni ofrecerla como paso opcional. Referencia histórica:
> el registro de EP.015 (work ID 2605315837136) fue el formato que se usaba.
>
> Esto NO aplica a otros shows: `podcast-creator/workflows/00-setup.md` sigue sugiriendo
> SafeCreative a quien arranca un podcast desde cero, y esa recomendación general se queda.

---

# Step 4b — Update website episode grid (post-publish, once Spotify URL is live-verified)

> ⚠️ **Estructura reescrita 2026-07-25 con el rebrand v4.** Ya **no** existe
> `<div class="ep-list">` ni el comentario `GRID RULE` que esta sección describía: el reskin
> tipográfico los reemplazó y la descripción vieja mandaba a editar un nodo inexistente.
> Verificado contra `btq-production/website/index.html` real.

El sitio `behind-thequeue.com` (proyecto Vercel `website`) muestra los episodios en **dos
bloques separados**, y publicar uno nuevo toca los dos:

| Bloque | Selector | Contenido |
|---|---|---|
| Último episodio (destacado) | `.mast-foot > a.latest` | `lt-n` (número, 3 dígitos), `lt-k` = `Último episodio · [Teórico]`, `lt-t` = título. **Sin cita.** |
| Tracklist | `.stag > a.track` ×4 | `t-num`, `t-ref` (teórico/referente), `t-title`, `t-quote`. Orden **newest→oldest**. |

1. Editar `btq-production/website/index.html`:
   - `a.latest` pasa a ser el episodio nuevo (número, teórico, título, `href`).
   - El que estaba en `a.latest` **baja al primer lugar del tracklist** — y ahí sí necesita
     `t-quote`, que el bloque destacado no tenía. **Sacarla textual del SRT del episodio**,
     no inventarla ni parafrasear el guion; el patrón de las 4 existentes es la frase de
     firma del cierre.
   - Se cae el `a.track` de número más bajo, para que el tracklist siga en 4.
   - El `href` va a la URL de Spotify **verificada en vivo** (ver la advertencia de re-push en
     step1-collect-inputs.md — nunca reutilizar una URL solo "confirmada" antes de re-subir).
2. Redeploy from `btq-production/website/`: run `vercel --prod`.
3. **Git commit alone does NOT update the live site** — Vercel deploy is manual via CLI,
   not auto-deploy from git push. Confirmed in EP.016: the HTML had the correct grid in the
   commit, but the live site kept showing the stale grid until `vercel --prod` ran.
4. Verify live (run via Bash tool — uses `$(date +%s)` and `grep`, not available in
   native PowerShell 5.1):
   ```
   curl -s "https://behind-thequeue.com/?v=$(date +%s)" | grep -o "episode/[a-zA-Z0-9]*"
   ```
   PowerShell alternative:
   ```
   (Invoke-WebRequest -Uri "https://behind-thequeue.com/?v=$(Get-Random)").Content -split '"' | Select-String "episode/"
   ```
   Confirm the new episode's URL appears and matches the live-verified Spotify URL.
