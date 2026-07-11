# Workflow 03 — Validación de imágenes generadas

**Esta es la pieza genuinamente nueva del pipeline.** Ni `episode-launch` ni
`podcast-creator` validan las *imágenes resultantes* — solo generan los prompts. Aquí
es donde se cierra ese loop: generar → validar contra las reglas estándar → corregir
si falla → repetir hasta que pase.

---

## Paso 0 — Preguntar si ya existen assets de una sesión previa

**Antes de presentar los prompts**, pregunta: "¿Ya tienes imágenes generadas de una
sesión anterior para este episodio — todas, o solo algunas? Si tienes el set completo,
pásame las 3 rutas y validamos esas directamente. Si tienes solo algunas, dime cuáles
te faltan y seguimos solo con esas."

Si el usuario pasa rutas: verifica con `Read` que cada archivo existe y es una imagen
válida antes de pasar al subagente de validación. Si una ruta falla, pídela de nuevo —
no asumas que el set está completo ni sigas adelante con una ruta rota.

Por qué: en EP.016 el usuario tuvo que decir DOS veces "ya lo tengo, no lo regeneres"
(cover-art y luego quote cards en Stage 3b) — y terminó completando el set combinando
1 imagen de una sesión anterior + 2 nuevas. Preguntar primero y permitir un set mixto
evita ciclos de regeneración innecesarios. Si confirma que ya tiene el set completo,
salta directo al Paso 2 (validación) con esas rutas.

---

## Paso 1 — Generación (ruta local primero — TODOS los shows, desde 2026-07-11)

**Ruta primaria (aprobada por Andy en BTQ EP.021, aplica a BTQ, MPD y CCC): generación
LOCAL vía la skill `comfyui`** (Z-Image Turbo por API — ya NO es cierto que "no existe
API de generación de imágenes"). Ventajas confirmadas: sin filtro de copyright para
personajes con nombre propio (advertir el riesgo IP de publicar, decisión editorial del
usuario), iteración barata con seed fijo, y sin los patrones de fallo de Flow.

Reglas de la ruta local (detalle en `comfyui/docs/prompting.md` §"la trampa de la
negación" — leer ANTES de escribir prompts):
1. El control es 100% del prompt positivo (a CFG 1 el negativo no actúa; "DO NOT render
   X" evoca X; no pedir conceptos que contienen el elemento prohibido).
2. Identidad de personajes desde píxeles de referencia (img2img / render cartoon fiel
   del propio modelo), nunca descrita de memoria — feedback de Andy EP.021 ("queda
   super picasso").
3. El texto de marca puede ir en el render (Z-Image lo hace bien) pero se verifica
   letra por letra; typos puntuales se parchan determinista con PIL sobre zonas planas.
   Alternativa igual de válida: escena sin texto + tipografía 100% PIL (tildes seguras).
4. Upscale a resolución final (ej. 3000x3000 Spotify) con RealESRGAN local.
5. La atmósfera/drama nace EN el render (una sola escena completa) — no componer figura
   sobre lienzo vacío (rechazado EP.021: "figura flotando en negro").

**Fallback:** si el usuario prefiere Flow/Nani Banana para algún formato (o el servidor
local no está disponible), presenta los prompts y pausa como antes:

> **Prompts listos para EP.0XX — 1:1 · 9:16 · 16:9.**
> Genera cada uno y dime las rutas cuando estén listas.

En esa ruta siguen vigentes los patrones de fallo de Flow documentados en
`episode-launch/docs/brand-constants.md`.

---

## Paso 2 — Validar las imágenes contra las reglas estándar

El agente principal puede ver imágenes con `Read` — **valida directamente tú mismo**
leyendo las 3 imágenes y aplicando las reglas de abajo. Es lo más eficiente y respeta la
guía de no spawnear subagentes sin necesidad (validado EP.018: 3/3 PASS leyendo directo).

Spawnea un `general-purpose` con el prompt autocontenido de abajo **solo si** quieres un
chequeo independiente (sin el sesgo del contexto que generó los prompts) o si tu contexto
ya está muy cargado. En cualquiera de los dos modos, verifica:

- Las rutas de las 3 imágenes generadas
- Las reglas estándar a verificar (cópialas del archivo de referencia — no las
  resumas de memoria):
  > ⚠️ **`btq-project/workflows/artwork.md` NO existe en disco** (confirmado 2026-06-26,
  > ver `episode-pipeline/workflows/00-roadmap.md` Paso 3) — la fuente real y vigente de
  > las reglas de artwork BTQ es `.claude/skills/episode-launch/docs/brand-constants.md`
  > § "Dirección de artwork". Usa el checklist de ahí (render con volumen/textura real,
  > número de figuras justificado, patrón geométrico correcto de fondo, texto letra por
  > letra, footer completo) en vez de buscar el archivo de abajo.
  1. **Regla de margen** ("Regla de margen — la tipografía vive en zonas muertas"):
     tipografía debe estar en tercio superior/inferior, sujeto/visual focal en tercio
     central — nunca texto centrado sobre rostros o props icónicos
  2. **Composiciones split-scene**: si la imagen usa una composición dividida, debe
     tener separación dura por porcentaje (ej. 50/50 o tercios) sin fusión en el
     centro — "no blending or merging at the center seam"
  3. **Verificación contra referencia oficial** (solo si hay personaje/mech): si el
     workflow de artwork (Step 0) usó una imagen de referencia oficial, el agente debe
     cargarla y comparar specs críticos (colores, accesorios, proporciones) contra la
     imagen generada — el mismo tipo de chequeo que detectó los errores de Old Snake /
     MGS RAY en un episodio anterior (ejemplo histórico, no un archivo vivo a consultar)

El agente debe devolver, **por cada imagen**, un veredicto estructurado:
```
Imagen [formato]:
  - Regla de margen:        PASS / FAIL — [detalle si falla]
  - Split-scene separation: PASS / FAIL / N-A — [detalle si falla]
  - Vs. referencia oficial: PASS / FAIL / N-A — [detalle si falla]
  - Veredicto general:      PASS / FAIL
```

---

## Paso 3 — Si falla: corregir y repetir

Si cualquier imagen recibe FAIL:
1. Toma el detalle específico del fallo (ej. "texto centrado sobre el rostro del
   personaje" o "LED del Solid Eye en el lado incorrecto")
2. Reescribe el prompt completo (nunca solo el fragmento — `episode-launch` y
   `podcast-creator` ya documentan que los modelos de imagen no toman correcciones
   parciales bien) incorporando la corrección
3. Vuelve al **Paso 1** — pausa de nuevo para que el usuario regenere con el prompt
   corregido

Repite hasta que las 3 imágenes obtengan PASS general.

---

## Paso 4 — Registrar en la bitácora (auditable)

Agrega **cada chequeo realizado** — no solo el resultado final — a
`pipeline-audit-ep[NNN].md`:

```
## Stage 3 — Validación de imágenes
- Qué se hizo: subagent de validación lanzado contra 3 imágenes generadas (rondas: [N])

### Ronda 1
- Imagen 1:1   → Regla de margen: PASS · Split-scene: N-A · Referencia: PASS → PASS
- Imagen 9:16  → Regla de margen: FAIL (texto sobre rostro) · ... → FAIL
- Imagen 16:9  → ... → PASS
- Acción: prompt 9:16 corregido y reenviado para regeneración

### Ronda 2
- Imagen 9:16  → Regla de margen: PASS · ... → PASS

- Resultado: OK — 3/3 imágenes con veredicto PASS tras 2 rondas
```

Esto es lo que permite al usuario auditar exactamente qué se revisó en cada paso.

---

## Al terminar

Confirma: "Las 3 imágenes de portada pasaron validación." y continúa a
`03b-marketing.md` (material de marketing — social, quote cards) **antes** de rotar el
grid, ya que ese material reutiliza el artwork recién validado como base visual.
