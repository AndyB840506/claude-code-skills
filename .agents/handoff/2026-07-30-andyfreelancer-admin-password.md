# Handoff: andyfreelancer — contraseña del admin dashboard

**Date:** 2026-07-30 (jueves)
**Machine:** desktop (E:\)
**Status:** In progress — se localizó el mecanismo de auth; el usuario fue a DigitalOcean a leer/cambiar el valor y NO volvió a confirmar. **Nada verificado contra el sitio live.**

> Sesión corta y en paralelo con la sesión de MPD T2E01 (handoff `2026-07-30-mpd-t2e01-artwork-el-27.md`, escrito 8:51 AM). Temas independientes; no hay estado cruzado.

---

## What We Accomplished This Session

- **Identificado el mecanismo de auth del dashboard `/admin` de andyfreelancer.com** leyendo el código (repo `the-freelancer`, rama `master`, sincronizado con `origin/master`, sin commits hoy):
  - La contraseña **es la env var `PATCH_SECRET`**. Es un secreto compartido en **texto plano — sin hash** — comparado con `crypto.timingSafeEqual` en `server.js:445` (login POST) y `server.js:411` (middleware `requirePatchSecret`).
  - Consecuencia clave: **es recuperable, no solo reseteable** — si DO lo muestra en claro, se lee; no hay que regenerar nada.
  - La MISMA env var gatea el `Authorization: Bearer` de `/admin/orders`, pero el dashboard reenvía el token que el usuario escribió, así que **cambiarla no rompe ningún otro cliente**: no hay clientes que lo guarden.
  - Hay rate limit de 10 intentos fallidos / 15 min por IP (`authLimiter`, `server.js:263`, con `skipSuccessfulRequests`).
- **Descartado el `.env` local como vía**: en `C:\Users\andre\repos\the-freelancer` solo existe `.env.example` (387 bytes) y **no** contiene `PATCH_SECRET`.
- **Aplicado a memoria** el hallazgo de topología: `reference_andyfreelancer_infra.md` ahora documenta las **dos superficies de admin** (ver Notes).

## Where We Paused

**Last action:** El usuario dijo "I will go to DO to get it". Se le indicó la ruta *DO → Apps → `the-freelancer` → Settings → componente `the-freelancer` → Environment Variables → `PATCH_SECRET`*, con la advertencia de que guardar dispara redeploy (~1-2 min de rebote del sitio).

**Next action:** Preguntarle al usuario **qué pasó en DO** antes de proponer nada: ¿pudo leer el valor, o tuvo que ponerle uno nuevo? (Ver Questions.)

**Blockers:** Todo depende de esa respuesta. El agente no tiene el valor y no puede leer el panel de DO.

## Files to Read First

- `C:\Users\andre\repos\the-freelancer\server.js` — líneas 399-459 (auth + login) y 255-269 (rate limiters). Es la fuente de verdad del mecanismo.
- `C:\Users\andre\repos\the-freelancer\estimador\config\admin.php` — el segundo admin, sin verificar (ver Notes).
- Memoria `reference_andyfreelancer_infra.md` — topología completa de hosting/DNS/email/admin.
- Memoria `reference_do_app_platform_api.md` — la vía por API, que **no se usó esta sesión** (ver Notes).

## Notes / Gotchas

- **NO VERIFICADO — el segundo admin.** `estimador/config/admin.php:2` tiene `$ADMIN_PASSWORD = 'admin1234'` hardcodeado y commiteado, con un comentario "Change before using on a live server". **No se comprobó** si ese PHP es alcanzable en el sitio live (la app es Express en DO; el PHP podría ser peso muerto que nada sirve) ni si el repo es público. **No tratarlo como hallazgo de seguridad hasta verificar esas dos cosas** — decirlo antes de medirlo sería exactamente el fallo de la faja.
- **Miss de esta sesión (no encodeado a propósito):** existía `reference_do_app_platform_api.md`, que documenta que **todo lo de DO se hace por API** con un token `dop_v1` de acceso total que Andy mantiene activo (creado 2026-07-07, **expira ~2026-08-06** — o sea, todavía válido hoy). No se consultó; se mandó al usuario a hacer clics en el panel. La regla que lo cubre ya existe (CLAUDE.md § regla de transición #3), así que **no se escribió una copia nueva** — se deja acá como recordatorio operativo.
- **Matiz honesto sobre esa vía:** la API probablemente **no** habría recuperado el valor viejo — DO devuelve las env vars de tipo SECRET como blobs cifrados `EV[1:...]`. **Esto NO está verificado**, es entendimiento del agente, no hecho probado. Lo que sí habría dado la API: respuesta definitiva sobre el tipo de la variable, y un set-and-verify determinista.
- El repo `the-freelancer` quedó **limpio y sincronizado** con `origin/master` (HEAD `556ab5c`). No se tocó ni un archivo ahí — la sesión fue de solo lectura sobre ese repo.

## Questions to Answer

1. **¿Qué pasó en DO?** ¿`PATCH_SECRET` se pudo leer en claro, o era tipo SECRET y hubo que escribir uno nuevo? (Esto decide si queda algo por hacer o no.)
2. Si se puso uno nuevo: **¿se quiere verificar el login contra el sitio live?** Se puede con un `curl -X POST https://andyfreelancer.com/admin -d "token=..."` — 200 con el HTML del dashboard = bien, 401 = mal. Ojo con el rate limit de 10 fallos/15 min.
3. **¿Se revisa el admin PHP del estimador?** Requiere comprobar (a) si `/estimador/...` se sirve en producción y (b) si el repo de GitHub es público. Si ambas son sí, esa contraseña hardcodeada hay que rotarla.
