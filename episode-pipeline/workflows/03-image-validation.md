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

## Paso 1 — Pausa para generación (punto de pausa estructural)

No existe API de generación de imágenes — Flow/Nani Banana son herramientas manuales.
Presenta los 3 prompts (de Stage 2) y pide:

> **Prompts listos para EP.0XX — 1:1 · 9:16 · 16:9.**
> Genera cada uno en Flow/Nani Banana (selecciona el mejor de los candidatos) y
> dime las rutas de los archivos descargados cuando estén listos.

Espera la respuesta del usuario con las rutas. **No continúes sin ellas.**

---

## Paso 2 — Spawn del subagent de validación

Lanza un agente `general-purpose` (tiene acceso a `Read`, que puede ver imágenes) con
un prompt autocontenido que incluya:

- Las rutas de las 3 imágenes generadas
- Las reglas estándar a verificar (cópialas del archivo de referencia — no las
  resumas de memoria, las reglas exactas viven en `btq-project/workflows/artwork.md`):
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
     MGS RAY documentados en `btq-project/workflows/artwork.md`

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
