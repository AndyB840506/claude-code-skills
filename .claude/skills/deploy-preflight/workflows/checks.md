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

**Maquina nueva / sin link (post cambio de PC):** si `repo.json` (y/o el `.vercel/` del proyecto) NO existe, no es un STOP — es setup. El `.vercel/` esta gitignored, asi que se pierde con cada cambio de PC. Ruta de recuperacion (verificada 2026-06-22, deploy EP.018 BTQ en portatil):
1. Si falta el CLI: `npm install -g vercel`. Si falta auth: el usuario corre `vercel login` (interactivo, su cuenta).
2. Saca el `projectId`: `vercel project inspect <proyecto> --scope <team>` (ej. `vercel project inspect website --scope mrputridsden`).
3. Saca el `orgId` (team id `team_...`): token en `C:\Users\andre\AppData\Roaming\xdg.data\com.vercel.cli\auth.json` -> `Invoke-RestMethod -Uri https://api.vercel.com/v2/teams -Headers @{Authorization="Bearer $token"}`. (El `vercel teams ls` muestra el slug, no el `team_...`.)
4. Escribe `<dir>/.vercel/project.json` a mano: `{"projectId":...,"orgId":...,"projectName":...}`. **No uses `vercel link`** (corrompe el repo.json del monorepo, ver pitfall abajo). Verifica que NO se creo un `.vercel` en la raiz y que sigue gitignored.

**Pitfall conocido:** nunca corras `vercel link --project X --yes` desde un subdirectorio de este monorepo — puede agregar una entrada corrupta a `.vercel/repo.json` (root) con `"directory": "."` para ese proyecto, causando que deploys posteriores suban el repo completo en vez del subdirectorio (esto le paso a BTQ el 2026-06-10). Si un proyecto necesita su propio link, crea `.vercel/project.json` directamente dentro de ese subdirectorio con el formato `{"projectId":..., "orgId":..., "projectName":...}` (ver `btq-production/website/.vercel/project.json` o `lucca-tech-web/.vercel/project.json` como ejemplo).

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

## Paso 6 — Estado actual: Git auto-deploy desconectado (MPD, BTQ, Lucca)

**Contexto:** un `git push` a `main`/`master` con la integracion de GitHub de Vercel activa puede disparar un build automatico con deteccion de framework que **sobrescribe un deploy prebuilt** y rompe produccion (404). Esto paso el 2026-06-09 con MPD (`directory: "."` en `.vercel/repo.json`) y el 2026-06-10 con `lucca-tech-web` (proyecto standalone, push de `b553039`) y con BTQ (ver pitfall de `vercel link` arriba).

**Fix de raiz ya aplicado (2026-06-10):** los 3 proyectos (`v0-mr-putrids-den`/MPD, `website`/BTQ, `lucca-tech-web`) tienen el auto-deploy de GitHub **desconectado** (`vercel git disconnect`). `git push` a este repo ya NO dispara builds para ninguno de los tres.

**Los deploys a produccion son manuales. OJO con `vercel --prod` (build remoto):** si el `vercel.json` del proyecto tiene `"ignoreCommand": "exit 0"` (es el caso de MPD/`v0-mr-putrids-den`), el build remoto se SALTA y el deployment queda VACIO -> al re-apuntar el alias, produccion devuelve **404** (incidente 2026-06-14, deploy EP.004). Para esos proyectos usa el **flujo prebuilt del Paso 7**. Si el proyecto NO tiene `ignoreCommand`, `vercel --prod --yes` desde el directorio del proyecto funciona.

Si en el futuro se agrega un proyecto nuevo deployado via prebuilt, aplica el mismo patron antes de confiar en deploys automaticos: `vercel git disconnect` y/o `"ignoreCommand": "exit 0"` en su `vercel.json`.

Si por algun motivo el auto-deploy se reconecta y un push rompe produccion (status `200`->`404`):

1. Corre `curl -sI` contra la URL de produccion del proyecto para confirmar el 404.
2. **Repite el deploy prebuilt** (Paso 7) y re-apunta el alias con `vercel alias set`.

## Paso 7 — Deploy prebuilt (metodo estandar para proyectos con `ignoreCommand`)

Verificado 2026-06-14 (deploy EP.004 P1 de MPD). Aplica a `v0-mr-putrids-den` y a
cualquier proyecto cuyo `vercel.json` tenga `"ignoreCommand": "exit 0"`. Desde el
directorio del proyecto (`<dir>`, ej. `mrputridsden-production/website`):

1. **Asegurar el output prebuilt** en `<dir>/.vercel/output/`:
   - `config.json` = `{"version":3}`
   - `static/index.html` = copia del `index.html` ACTUAL del proyecto. Copialo a mano
     (PowerShell `Copy-Item ...\index.html ...\.vercel\output\static\index.html -Force`).
     **No confies en `vercel build`** aqui: si el proyecto no esta "pulled" deja el
     `index.html` viejo en el output sin avisar.
2. **Crear `<dir>/.vercel/project.json` a mano** (NO `vercel link` desde subdir — corrompe
   el `repo.json` root). Usa los IDs de `.vercel/repo.json` (root):
   `{"projectId":...,"orgId":...,"projectName":...}`. (`.vercel/` esta gitignored -> no se commitea.)
3. `vercel deploy --prebuilt --prod` desde `<dir>` -> devuelve la URL del deployment.
4. `vercel alias set <deployment-url> www.<dominio>` — **`--prod` NO reapunta solo el
   dominio custom**; este paso es obligatorio.
5. **Verificar:** `curl -sI https://www.<dominio>/` debe dar `200`, y
   `curl -s https://www.<dominio>/ | grep "<marcador nuevo>"` debe encontrar el cambio.
