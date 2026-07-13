# Workflow 05 — Deploy + verificación (gate final)

Última etapa: preflight → **gate de aprobación final** (el único gate explícitamente
pedido por el usuario para el pipeline) → deploy → verificación HTTP 200 → verificación
Spotify (informativa). No declares nada como "publicado" sin completar los pasos del
gate y el deploy — ver memoria `feedback_verify_before_done`.

---

## Paso 1 — Preflight

Invoca `/deploy-preflight` con target **Vercel** (es el único usado por ambos shows).
Esto corre los chequeos del skill (project link/repo.json, directorio y vercel.json,
secrets, baseline de producción + host real). (Nota 2026-07-13: la referencia anterior
a un flag + hook `deploy-preflight-gate.ps1` era stale — ese hook no existe en las
máquinas actuales; el bloqueo real contra deploys sin validar es el gate de aprobación
del Paso 2.)

Si el preflight reporta algo en estado FAIL (manual): detente aquí y reporta el
bloqueo al usuario — no continúes al gate de aprobación con un preflight a medias.

---

## Paso 2 — GATE FINAL DE APROBACIÓN (el único pedido por el usuario)

Presenta un resumen completo de **todo lo que está por publicarse** — este es el punto
donde el pipeline se detiene y espera "sí, publica":

> **Resumen pre-deploy — EP.0XX ([show]):**
>
> **Assets generados (Stage 2):**
> - [lista de archivos: launch-assets / shownotes / youtube / artwork, con rutas]
>
> **Imágenes validadas (Stage 3):**
> - [3 imágenes, formato, resultado de validación — PASS tras N rondas]
>
> **Grid rotado (Stage 4):**
> - [show]: de `[grid anterior]` a `[grid nuevo]` — entra EP.0YY, sale EP.0ZZ
>
> **Preflight (Stage 5, paso 1):** [PASS / FIXED — N auto-corregidos]
>
> ¿Apruebas publicar todo esto a producción? (sí / ajustar algo primero)

**No corras `vercel --prod` sin un "sí" explícito.** Si el usuario pide ajustar algo,
vuelve al stage correspondiente — no fuerces el deploy con cambios pendientes.

---

## Paso 3 — Deploy

Tras la aprobación, ejecuta el deploy del show correspondiente:

| Show | Comando | Carpeta |
|---|---|---|
| BTQ | `$env:NODE_OPTIONS="--use-system-ca"; vercel --prod` | `btq-production/website/` |
| MPD | `$env:NODE_OPTIONS="--use-system-ca"; vercel --prod` | `mrputridsden-production/website/` |

(El `NODE_OPTIONS` bypassa el bloqueo SSL de Avast — ver memoria `feedback_antivirus_smtp_ssl`.)

Captura la URL de producción que reporta Vercel al terminar.

---

## Paso 4 — Verificación HTTP 200 (pieza nueva — nunca existió antes)

**No declares el deploy exitoso solo porque Vercel reportó éxito** — confirma que la
URL en vivo realmente responde. Corre contra la home del sitio correspondiente:

```powershell
$url = "https://behind-thequeue.com"   # o https://mrputridsden.com / la URL que reportó Vercel
try {
    $response = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 30
    Write-Output ("HTTP " + $response.StatusCode + " — " + $url)
} catch {
    Write-Output ("FALLO — " + $url + " — " + $_.Exception.Message)
}
```

- **200** → verificación OK, continúa al siguiente paso
- **Cualquier otro código o error** → NO declares el deploy como exitoso. Reporta el
  código/error exacto al usuario y pregunta cómo proceder (rollback, esperar
  propagación de DNS/cache, investigar logs de Vercel)

---

## Paso 5 — Verificación Spotify (informativa, no bloqueante)

Confirma que el episodio nuevo ya aparece en la página pública del show — una señal
extra de que el lanzamiento está realmente visible, más allá de que el sitio cargue.

**Esto es un chequeo SOFT, no un gate de pass/fail como el HTTP 200**: Spotify puede
tardar en procesar y mostrar un episodio recién publicado — un "no aparece todavía" es
normalmente lag de propagación, no un problema del deploy.

Usa `WebFetch` contra la página pública del show correspondiente (NUNCA contra "Spotify
for Podcasters" — ese es el dashboard privado del creador y requiere login; no se debe
intentar acceder con credenciales, ver memoria `feedback_service_account_security`):

| Show | URL pública del show en Spotify |
|---|---|
| BTQ | `https://open.spotify.com/show/5figtqa6zJxW1pE1sWJeEP` |
| MPD | `https://open.spotify.com/show/0M12ujB9eJqr0dWZUwEf6B` |

Busca el episodio nuevo (por título y/o número `EP.0XX` del brief) en el listado de la
página:

- **Aparece** → repórtalo como PASS: "Episodio confirmado en vivo en la página pública
  de Spotify."
- **No aparece** → repórtalo como informativo, NO como falla: "El episodio aún no
  aparece en la página pública de Spotify — esto suele ser normal por tiempo de
  propagación, no indica un problema con el deploy. Puedes verificar de nuevo más tarde
  si quieres confirmarlo."

---

## Al terminar

0. Actualiza `pipeline-state-ep[NNN].md` → `stage_c: complete`. Esto cierra el ciclo
   completo del episodio en el sistema de checkpoints. (Si en el futuro existe un
   `roadmap-[show].md` para ese show, actualiza también su fila a `publicado` — verificado
   2026-07-05 que ese archivo NO existe todavía para ningún show; `pipeline-state-ep[NNN].md`
   es hoy la única fuente de verdad.)
1. Si todo pasó, confirma:
   > **EP.0XX publicado y verificado — [show].**
   > URL: [url] → HTTP 200 confirmado.
   > Spotify: [episodio confirmado en la página del show / aún no visible — posible lag de propagación]
   > Pipeline completo: transcripción → assets → imágenes validadas → grid rotado → deploy verificado.

2. Agrega la entrada final a la bitácora:
   ```
   ## Stage 5 — Deploy + verificación
   - Qué se hizo: preflight ([resultado]) → gate de aprobación (aprobado por el usuario)
     → vercel --prod → verificación HTTP → verificación Spotify (informativa)
   - URL verificada: [url] → [código HTTP]
   - Verificación Spotify: [PASS — episodio encontrado en la página del show]
                            o [INFO — aún no visible, posible lag de propagación]
   - Resultado: OK — episodio publicado y verificado en vivo
   ```

3. Cierra: "Pipeline de EP.0XX completo — bitácora en `pipeline-audit-ep[NNN].md`."
