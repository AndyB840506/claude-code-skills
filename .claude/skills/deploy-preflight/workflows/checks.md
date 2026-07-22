# Execution

## Paso 1 — Identificar el proyecto a deployar

Pregunta (si no es obvio del contexto de la conversacion) cual proyecto/directorio se va a deployar. Ejemplos en este repo:
- `mrputridsden-production/website` -> proyecto Vercel `mr-putrids-den-web` (dominio `mrputridsden.com`; renombrado 2026-07-19 tras el incidente del Paso 1b — el proyecto viejo `v0-mr-putrids-den` quedo huerfano/stale, no lo uses)
- `btq-production/website` -> proyecto Vercel `website`

## Paso 1b — Verificar que el link real coincide con el mapeo esperado

**Mordio 2026-07-19:** `mrputridsden-production/website/.vercel/project.json` estaba
linkeado al proyecto `website` — que es el proyecto REAL de BTQ, no de MPD. Causa mas
probable: colision de nombre — la carpeta de MPD tambien se llama `website`, y en algun
momento un `vercel link` (interactivo o con `--yes`) matcheo por nombre de carpeta y
linkeo al proyecto existente equivocado en vez de crear uno nuevo. Correr `vercel --prod`
desde ahi auto-alias el dominio real de BTQ (`behind-thequeue.com`) al build de MPD,
tumbando produccion de otro show hasta que se detecto y se restauro.

**Antes de correr `vercel --prod` (o `--prebuilt --prod`) desde cualquier directorio:**

```bash
cat <directory>/.vercel/project.json
```

**El nombre esperado del Paso 1 tambien caduca — verificalo contra el dominio, no contra
un doc** (mordio 2026-07-22, MPD): el proyecto se habia renombrado el 2026-07-19 y tanto
`.vercel/project.json` como la memoria `reference_mpd_website_live` seguian nombrando al
proyecto viejo (`v0-mr-putrids-den`), que habia quedado huerfano. Desplegar ahi **reporta
exito y deja produccion intacta** — no hay error visible. La unica fuente autoritativa es
quien sirve el dominio ahora mismo:

```bash
vercel inspect https://www.<dominio>/ --scope <team>
```

El campo `name` de la respuesta es el proyecto real. Si no coincide con `project.json`,
reescribi `project.json` con el `projectId` correcto (`vercel project inspect <nombre>
--scope <team>` lo devuelve; el `orgId` es el mismo para todos los proyectos del team) —
**nunca con `vercel link`** desde un subdirectorio, ver el pitfall del Paso 2.

Confirma que `projectName` coincide EXACTAMENTE con el esperado del Paso 1. Si no
coincide (o si el nombre de la carpeta coincide con el nombre de OTRO proyecto Vercel
conocido en este workspace — ej. una carpeta llamada `website` cuando existe un
proyecto `website` de otro show/cliente), **STOP** — no deployes. Reporta el mismatch y
pregunta al usuario como proceder (relinkear al proyecto correcto, o crear uno nuevo
dedicado con `vercel link --project <nombre-unico-no-generico> --yes`, evitando nombres
genericos como `website` que puedan volver a colisionar).

**No confundir con falsa alarma (verificado 2026-07-20, deploy EP.022 BTQ):** el output
de `vercel --prod` imprime "Deploying `<team-slug>/<project-name>`" — el team-slug es el
nombre de la cuenta/equipo de Vercel del usuario (ej. `mrputridsden`, aunque el deploy
sea de BTQ), NO el proyecto al que apunta. Ver ese slug no es evidencia de la colisión de
arriba. Lo que sí confirma un deploy correcto es: `project.json` ya validado ANTES de
correr el comando (paso de arriba) + la línea final `▲ Aliased <dominio-correcto>` del
output. Si ambos coinciden con lo esperado, el team-slug del output es irrelevante.

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

## Paso 3b — Verificar que no se filtren secrets

Antes de deployar (y antes de cualquier `git push` que dispare el flujo), corre un grep basico sobre los archivos del directorio a deployar buscando patrones de credenciales:

```bash
grep -RniE "sk-[a-zA-Z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----|password\s*=\s*['\"]" <directory>
```

Si hay match, **STOP** — no deployes ni hagas push hasta confirmar con el usuario si es una key real (rotarla/moverla a env var) o un falso positivo (ej. un access key publico como el de Web3Forms en el form de contacto de BTQ, que es seguro exponer por diseño). No asumas que un match es benigno sin preguntar.

## Paso 4 — Verificar estado de produccion actual + host real

Corre un `curl -sI` (o equivalente) contra la URL de produccion del proyecto para confirmar que esta respondiendo `200 OK` ANTES del deploy. Esto da una baseline para detectar si el proximo deploy rompe algo.

**Identificar el host real en los mismos headers** — no confiar en runbooks/docs del repo, pueden estar stale (mordio 2026-07-09: kumatalent.com ya habia migrado de Vercel a DO y el runbook seguia diciendo Vercel prebuilt):

- `x-vercel-id` / `server: Vercel` -> Vercel (aplica todo este skill).
- `x-do-app-origin` -> DigitalOcean App Platform. Si la app tiene deploy-on-push, el metodo es `git push` — NO corras el flujo vercel; verifica el deploy con un poll del marker nuevo en produccion. **Tiempo de publicacion depende del tipo de app:** static sites publican en ~20-60s; apps con build (Node/Express, etc.) tardan 1-3 min — usa un deadline de poll de al menos 6 min para no reportar timeout falso (verificado 2026-07-17, the-freelancer Node app).
- Otro host -> STOP y confirmar con el usuario el metodo de deploy.

Si el host real no coincide con el metodo asumido, re-rutea el deploy Y actualiza el doc stale del repo en la misma sesion.

**Si verificas con la tool WebFetch en vez de `curl`:** WebFetch cachea por URL ~15
minutos. Re-verificar un dominio justo despues de arreglarlo (ej. confirmar que un
alias se restauro) puede devolver la respuesta cacheada de ANTES del fix y parecer que
el problema sigue ahi (mordio 2026-07-19 verificando la restauracion de BTQ). Agrega un
query param cache-busting (`?cb=<algo unico>`) a la URL en cada refetch para forzar una
lectura real, o usa `curl` que no tiene este problema.

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

## Paso 8 — Email DNS (solo si el deploy envia correo)

Si la app deployada envia email (transaccional u outreach), verifica el DNS del dominio remitente ANTES del primer envio real:

```
nslookup -type=TXT <dominio> 8.8.8.8          # debe mostrar el SPF (v=spf1 ...)
nslookup -type=TXT _dmarc.<dominio> 8.8.8.8   # debe resolver (v=DMARC1; ...)
```

- Sin DMARC, Outlook filtra a Junk y mail-tester descuenta ~2 puntos (mordio 2026-07-17: outreach de hiresignal salio 7.7/10; agregar `_dmarc` TXT `v=DMARC1; p=none; rua=mailto:<buzon>` lo subio a 9.9 — DMARC pasa por alineacion SPF aun sin DKIM).
- Para cold outreach: score de mail-tester.com >= 9 antes del primer envio real a un prospecto.
- SMTP GoDaddy desde un host cloud (DO/AWS): si da "authentication failed" con creds validas, es bloqueo de IP cloud en 465/587 — usar puerto 3535/tls (ver memoria godaddy-smtp-do-port-3535).
