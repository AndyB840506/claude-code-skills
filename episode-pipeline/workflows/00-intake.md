# Workflow 00 — Intake (entrada a Macro-Stage B)

Construye el "episode brief": el objeto que todos los stages siguientes leen para
evitar repetir preguntas que sus workflows normalmente harían. Este es el punto de
entrada de **Macro-Stage B** (post-grabación → Spotify) — asume que el audio ya existe.

---

## Paso 0 — Revisar el archivo de estado del episodio (checkpoint de retomada)

Antes de preguntar nada, busca `pipeline-state-ep[NNN].md` para el episodio en
cuestión (junto a `pipeline-audit-ep[NNN].md`, en la carpeta de producción del show).
Este archivo es lo que permite retomar el pipeline en una sesión distinta a donde lo
dejaste — léelo y enrútate según lo que diga, **no reconstruyas el brief desde cero si
ya hay progreso guardado**:

| Estado del archivo | Acción |
|---|---|
| No existe ningún `pipeline-state-ep[NNN].md` | **No asumas — pregunta primero**: "No tengo un archivo de estado para EP.0XX — ¿ya grabaste y tienes el guion listo, o arrancamos desde cero por el roadmap?". Si responde que ya grabó/escribió (caso de episodios que venían en curso antes de este checkpoint, ej. BTQ EP.16): crea `pipeline-state-ep[NNN].md` retroactivamente con `stage_a: complete` y sigue aquí mismo. Si responde que no: **redirige a `00-roadmap.md` (Stage A)** |
| `stage_a: complete`, `stage_b: pending` | Continúa normalmente con este workflow (Paso 1) — es el caso esperado: pre-producción lista, audio recién grabado |
| `stage_b: complete`, `spotify_url: pending` | **Detente aquí** — no reproceses nada. El episodio ya pasó por transcripción/assets; lo único pendiente es publicar en Spotify. Pregunta: "EP.0XX ya tiene transcripción y metadata listos — solo falta publicarlo en Spotify y darme la URL en vivo. ¿Ya lo subiste?" Si trae la URL, actualiza el archivo de estado y pasa directo a Stage C (`03-image-validation.md`) |
| `stage_b: complete`, `spotify_url` resuelto | Salta directo a Stage C — Macro-Stage B ya está cerrada, no repreguntes nada de este workflow |

Esto es exactamente lo que evita el problema de BTQ EP.16: si el estado dice
`stage_b: complete, spotify_url: pending`, el pipeline se detiene ahí en vez de seguir
hacia Stage 4/5 sin nada que verificar.

---

## Paso 1 — Recolectar datos en un solo bloque

Pregunta todo de una vez:

> **Para arrancar el pipeline completo del episodio:**
> 1. ¿Qué show — Behind the Queue (BTQ) o Mr. Putrid's Den (MPD)?
> 2. Datos del episodio:
>    - Número y título
>    - Tema central / referencia cultural
>    - ¿Invitado? (nombre si aplica, "no" si es co-host normal)
>    - Fuentes/links/herramientas mencionadas que deban aparecer en las notas
>    - Frase de cierre (Closing TM) — solo si es BTQ, `episode-launch` la requiere
>    - URL de Spotify (o "pending" si aún no se sube)

No sigas preguntando más allá de esto — cualquier dato adicional que un workflow
posterior necesite y no esté aquí, ese workflow lo pedirá puntualmente en su momento
(no lo anticipes). El audio NO se pregunta — se descubre automáticamente (ver abajo).

---

## Auto-descubrir el archivo de audio crudo

Cada show graba siempre en la misma carpeta con un patrón de nombre predecible — no
hace falta pedirle la ruta al usuario:

| Show | Carpeta | Patrón de nombre |
|---|---|---|
| BTQ | `E:\Podcast\` | `Behind The Queue Ep.NN.mp3` (ej. `Behind The Queue Ep.16.mp3`) |
| MPD | `E:\Podcast\Mr.Putrid\` | `Mr Putrid N.mp3` (ej. `Mr Putrid 3.mp3`) |

Una vez tengas `show` y `ep_number`:

1. Lista los `*.mp3` de la carpeta correspondiente (Glob o `Get-ChildItem`).
2. Busca el archivo cuyo nombre contenga el número del episodio (los dígitos de
   `ep_number` — ej. `EP.017` → `17`). Acepta tanto formato con ceros (`Ep.16`) como
   sin ceros (`Mr Putrid 3`).
3. **Confirma siempre con una línea**, incluso si el match es único y limpio:
   > "Encontré `[archivo]` para EP.0XX — ¿es ese el audio? (sí / no, te paso la ruta)"
4. Si el usuario dice que no, o si hay cero o más de un archivo que matchea el número,
   **no adivines** — pide la ruta directamente.

El resultado de este paso llena el campo `audio_path` del brief.

---

## Construir el "episode brief"

Arma un bloque interno con esta forma — todos los stages siguientes lo leen:

```
EPISODE BRIEF
  show:            BTQ | MPD
  ep_number:       EP.0XX
  title:           [título completo]
  cultural_ref:    [referencia cultural / tema central]
  guest:           [nombre o "none"]
  sources:         [lista de links/herramientas/personas mencionadas]
  closing_tm:      [frase de cierre — BTQ únicamente]
  spotify_url:     [URL o "pending"]
  audio_path:      [ruta auto-descubierta y confirmada — ver paso anterior]
  language:        es
  speakers:        multi (ambos shows son co-host)
```

Actualiza `pipeline-state-ep[NNN].md` a `stage_b: in_progress`. Confirma el bloque al
usuario en una línea: "Brief armado para EP.0XX (show) — arranco con la
transcripción." y pasa directo a `01-transcription.md`.

---

## Notas

- Si el usuario ya proporcionó parte de estos datos al invocar el pipeline (ej. "corre
  el pipeline para BTQ EP.017, Pink Floyd, audio en E:\..."), no vuelvas a preguntar lo
  que ya tienes — solo completa los campos faltantes.
- Crea el archivo de bitácora `pipeline-audit-ep[NNN].md` ahora, con la primera entrada:
  ```
  ## Stage 0 — Intake
  - Qué se hizo: episode brief construido (show, audio, datos de episodio)
  - Resultado: OK
  ```
