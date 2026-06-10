# Execution

## Paso 1 — Identificar el proyecto a deployar

Pregunta (si no es obvio del contexto de la conversacion) cual proyecto/directorio se va a deployar. Ejemplos en este repo:
- `mrputridsden-production/website` -> proyecto Vercel `v0-mr-putrids-den`
- `btq-production/website` -> proyecto Vercel `website`

## Paso 2 — Verificar `.vercel/repo.json`

Lee `c:\Users\andre\.claude\skills\.vercel\repo.json`. Para el proyecto que se va a deployar:

- Confirma que existe una entrada con el `name` correcto.
- Confirma que `directory` **NO** sea `"."` (eso apunta al root del monorepo y causo el incidente del 404 del 2026-06-09 — desplego 151 archivos del repo completo con settings de Next.js incompatibles).
- Confirma que `directory` apunte exactamente al folder que se quiere deployar (ej. `mrputridsden-production/website`).

Si `directory` es `"."` o no coincide con el folder esperado, **STOP** — reporta el problema, no crees el flag, y pregunta al usuario si corrige el mapeo (no lo edites sin confirmacion si ya esta apuntado a un directorio especifico distinto al esperado, podria ser intencional).

## Paso 3 — Verificar el directorio de deploy

Confirma que el directorio (`<directory>` del paso 2) existe y contiene:
- Un `vercel.json` (o que el usuario confirme que el proyecto remoto tiene los settings correctos sin override local).
- Archivos del sitio (`index.html` u otro entrypoint esperado).

Si `vercel.json` existe, repórtalo (no hace falta validar su contenido a fondo, solo que exista y sea JSON valido).

## Paso 4 — Verificar estado de produccion actual

Corre un `curl -sI` (o equivalente) contra la URL de produccion del proyecto para confirmar que esta respondiendo `200 OK` ANTES del deploy. Esto da una baseline para detectar si el proximo deploy rompe algo.

## Paso 5 — Resumen

Da un resumen corto de:
- Proyecto y directorio validados (repo.json, directorio, vercel.json).
- Baseline de produccion (status code).
- Que comando `vercel` se puede correr ahora (build/--prod).

No corras el deploy tu mismo en este paso — solo valida. El usuario o el flujo principal decide cuando correr `vercel build` / `vercel --prod`.

## Paso 6 — Post-push check (si el flujo incluye `git push origin main/master`)

**Riesgo conocido:** si el proyecto tiene la integracion de GitHub de Vercel activa (deploys automaticos en push), un `git push` a `main`/`master` puede disparar un build automatico con deteccion de framework que **sobrescribe un deploy prebuilt** y rompe produccion (404). Esto paso el 2026-06-09 con MPD (`directory: "."` en `.vercel/repo.json`) y el 2026-06-10 con `lucca-tech-web` (proyecto standalone, push de `b553039`).

Si el flujo de esta sesion incluye un `git push` a `main`/`master` de un proyecto deployado via prebuilt:

1. Espera ~30-60s despues del push (el auto-deploy de Vercel tarda en correr).
2. Corre `curl -sI` contra la URL de produccion del proyecto.
3. Si el status cambio de `200` a `404`/error, **repite el deploy prebuilt** (recrea `.vercel/output/static` + `config.json`, `vercel deploy --prebuilt --prod --yes`) y re-apunta el alias con `vercel alias set`.

**Fix de raiz (recomendado, requiere confirmacion del usuario):** para proyectos deployados via prebuilt, desactivar el auto-deploy de Vercel en la integracion de GitHub, o agregar `"ignoreCommand": "exit 0"` a `vercel.json` para que los builds disparados por push se salten. Sin esto, el problema se repetira en cada push a main/master.
