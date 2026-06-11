# Workflow 00 — Roadmap (Stage A: pre-producción)

Primer paso del pipeline cuando NO existe todavía un `pipeline-state-ep[NNN].md` para
el episodio — es decir, cuando arrancamos antes de grabar. Cubre roadmap → guion →
artwork, y termina en la única pausa real de esta etapa: ir a grabar.

---

## Paso 1 — Confirmar cuál episodio sigue

Lee `roadmap-[show].md` (`btq-production/roadmap-btq.md` o
`mrputridsden-production/roadmap-mpd.md`) y busca la primera fila en estado
`en roadmap` o `guion listo` — ese es el candidato a "el episodio que sigue".

**Confirma siempre con el usuario antes de continuar** (no asumas — ver memoria
`feedback_confirm_domain_logic`):

> "Según el roadmap, el siguiente episodio es EP.0XX — [título] (estado: [estado]).
> ¿Arrancamos con ese, o es otro?"

Si el usuario corrige, usa el que indique — y si no aparece en la tabla, agrégalo.

---

## Paso 2 — Generar el guión de grabación

Invoca el workflow de guión correspondiente — **no reimplementes la lógica de
escritura de guiones aquí**:

| Show | Invoca |
|---|---|
| BTQ | `/btq-guion` (skill dedicada — 8 pasos, Tone Master, checklist de calidad) |
| MPD | `podcast-creator/workflows/01-episodio.md` (recuerda leer `glosario-cachaco.md` y `podcast-profile.json` primero, y preguntar "¿esta semana hay Silla Pútrida?") |

Espera a que el guión quede completo y aprobado por el usuario antes de seguir.

---

## Paso 3 — Generar prompts de artwork

Genera los prompts de portada (1:1, 9:16, 16:9) siguiendo el mismo patrón que ya usa
el pipeline más adelante para validar imágenes — reutiliza las reglas estándar de cada
show (sistema tipográfico propio, nunca mezclar — ver memoria
`feedback_mpd_vs_btq_typography`):

| Show | Referencia de reglas de prompt |
|---|---|
| BTQ | reglas vigentes documentadas en `btq-project` / artwork del pipeline (Stage de validación de imágenes) |
| MPD | `podcast-creator/workflows/03-artwork.md` + sistema tipográfico en memoria `mrputridsden_project` |

**No generes las imágenes todavía** — eso ocurre en la etapa de validación (Stage C),
junto con el resto del material visual. Aquí solo se preparan los prompts para
tenerlos listos cuando llegue ese momento.

---

## Paso 4 — Crear/actualizar el archivo de estado del episodio

Crea `pipeline-state-ep[NNN].md` (junto a `pipeline-audit-ep[NNN].md`, en la carpeta de
producción del show correspondiente) con esta forma:

```
EPISODE: EP.0XX ([show])
stage_a: complete — [fecha]
stage_b: pending
stage_c: pending
spotify_url: pending
notes: guion aprobado en [ruta], prompts de artwork preparados (ver bitácora Stage 0)
```

Actualiza también `roadmap-[show].md`: cambia el estado de la fila de este episodio a
`guion listo`.

---

## Al terminar

1. Confirma en una línea y entrega la pausa natural de esta etapa:
   > "Guion y prompts de artwork listos para EP.0XX ([show]) — **ve a grabar cuando
   > puedas**. Cuando tengas el audio grabado, retoma el pipeline (\"corre el pipeline
   > para EP.0XX\") y seguimos directo con la transcripción — el estado queda guardado
   > en `pipeline-state-ep[NNN].md`."
2. Agrega a la bitácora `pipeline-audit-ep[NNN].md` (créala si no existe):
   ```
   ## Stage A — Roadmap y pre-producción
   - Qué se hizo: episodio confirmado desde roadmap, guion generado y aprobado,
     prompts de artwork preparados, archivo de estado creado
   - Archivos generados: [ruta guion], [ruta notas de artwork/prompts]
   - Resultado: OK — pausa natural, esperando grabación
   ```
3. **No continúes a `00-intake.md` automáticamente** — esta etapa termina aquí porque
   el siguiente paso depende de que exista un audio grabado que todavía no existe.
