# Handoff: andyfreelancer.com — SEO fix + DNS/email + housekeeping de sesiones paralelas

**Date:** 2026-06-19
**Status:** Complete (lo mío) — quedan 3 acciones manuales de Andrés (ver Where We Paused)

---

## What We Accomplished This Session

- **SEO "not indexed" resuelto.** Era un soft-404: el catch-all de Express en
  `repos/the-freelancer/server.js` servía 200-homepage para cualquier path. Fix: 301 de
  `/services` y `/services/*` → `/`, y catch-all `*` → 404 real. Commit `80dcb47` en
  `the-freelancer` (rama `master`), desplegado en DO App Platform y verificado en vivo
  (301 / 404 / 200). Gemini había sugerido un redirect pero asumiendo Next.js/Vercel — el
  stack real es Express.
- **Email reparado (DNS).** El dominio no tenía MX. Topología: registrador Porkbun (panel
  DNS dormido, no tocar), DNS autoritativo en DigitalOcean (Networking → Domains), web en
  DO App Platform detrás de Cloudflare. Se agregaron en la zona **apex** `andyfreelancer.com`
  (NO en `www`, ni en App Platform → Domains): MX `fwd1.porkbun.com` (10), MX
  `fwd2.porkbun.com` (20), TXT `v=spf1 include:_spf.porkbun.com ~all`. Confirmado vía
  Cloudflare DoH.
- **Housekeeping de procesos** (commits en repo skills, ambos checkouts sincronizados en `9adae19`):
  - Fix workflow handoff: `git add` con alcance + `git pull --rebase` antes de push +
    sección "Parallel sessions" (`164d5c3`).
  - session-close co-author → Opus 4.8 (`9adae19`).
  - Rutina nueva `docs/parallel-sessions-worktree.md` (worktree por sesión).
  - graphify reencuadrado en `docs/roadmap-future-proofing.md` (NO descartado; quiere algo
    visual y ligero).
- **Memorias guardadas:** `reference-andyfreelancer-infra`, `feedback-menus-welcome`,
  `feedback-parallel-sessions`, `project-graphify-interest`, `feedback-validate-before-theorizing`.

## Where We Paused

**Last action:** montar rutina worktree + escribir este handoff.
**Next action (ACCIONES MANUALES DE ANDRÉS — que no se le pasen):**
1. **Probar el correo:** mandar un email a `hello@andyfreelancer.com` y confirmar que llega
   (esperar ~30 min de propagación desde el 2026-06-19).
2. **Porkbun → Email Forwarding:** confirmar a qué buzón reenvía `hello@`.
3. **Search Console:** Inspección de URLs → `https://andyfreelancer.com/` → Solicitar indexación.
4. *(Opcional)* borrar los MX/TXT redundantes en la zona DNS `www` (no sirven, no estorban).

**Blockers:** ninguno técnico. Las 4 de arriba son manuales, solo Andrés puede hacerlas.

## Files to Read First

- `~/.claude/projects/.../memory/reference_andyfreelancer_infra.md` — toda la topología
  (hosting, DNS, email, y el gotcha de usar DoH en vez de nslookup local)
- `docs/parallel-sessions-worktree.md` — rutina para correr sesiones paralelas sin cruzar cables
- `repos/the-freelancer/server.js` — el fix de SEO (commit 80dcb47)

## Notes / Gotchas

- **nslookup local MIENTE** en esta máquina (caché/PoP viejo) — para verificar DNS usar DoH:
  `curl -s -H "accept: application/dns-json" "https://cloudflare-dns.com/dns-query?name=andyfreelancer.com&type=MX"`.
- **Porkbun: nunca "Yes, update my domain"** — cambiaría los nameservers y tumbaría el sitio.
- **Dos sesiones compartieron working tree** este día → el commit del EP.018 absorbió una
  edición de roadmap de la otra sesión (no se perdió nada). Por eso la rutina worktree.
- **Dos checkouts del repo skills:** `.claude/skills` y `repos/kit-skill-creator` — ambos
  en `9adae19`; hacer `git pull` en el que se use al retomar.

## Questions to Answer (al retomar)

- ¿Llegó el correo de prueba a `hello@andyfreelancer.com`?
- ¿Se solicitó la indexación de `/` en Search Console?
- ¿Retomamos el guion del EP.018 Mundial (lo dejó la otra sesión en
  `btq-production/launch-assets/EP018-mundial-guion.html`)?
