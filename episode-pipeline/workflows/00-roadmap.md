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

⚠️ **No edites el roadmap (número/orden de episodios) por una frase ambigua del usuario.**
Confirma la numeración exacta ANTES de tocar la tabla (lección 2026-06-26: un swap EP.019↔020
hecho sobre un comentario ambiguo tocó revertirse). Si el usuario dice algo que contradice el
orden actual, repíteselo en numeración explícita y espera el "sí" antes de editar.

**BTQ:** antes de confirmar el candidato, revisa la sección "Estrategia editorial"
de `roadmap-btq.md` (referentes 80s/90s primero, un pilar SEO al mes, fórmula de
título con keyword, cadencia ≥7 días) y verifica que el episodio propuesto cumpla.
Si el roadmap lleva 3–4 pop-culture seguidos sin pilar SEO, propónselo al usuario.

---

## Paso 2 — Generar el guión de grabación

Invoca el workflow de guión correspondiente — **no reimplementes la lógica de
escritura de guiones aquí**:

| Show | Invoca |
|---|---|
| BTQ | `/btq-guion` si está instalada. **Si NO existe** (caso 2026-06-26): escribir el guion directamente siguiendo `btq-production/guion-style-btq.md` — esa guía ya tiene las 9 reglas de chispa, la estructura canónica del episodio, la voz narrativa y el lint. NO reimplementar reglas aquí. |
| MPD | `podcast-creator/workflows/01-episodio.md` (recuerda leer `glosario-cachaco.md` y `podcast-profile.json` primero, y preguntar "¿esta semana hay Silla Pútrida?") |

**Requisitos adicionales para guiones BTQ** (analytics 2026-06-12 — pásalos a
`/btq-guion` como parte del encargo, complementan su checklist propio):
1. **Re-enganche al ~60% del guion:** los completion rates rondan 50–67% — el dato o
   giro más fuerte del episodio NO va en el primer tercio; reservar uno explícitamente
   para la segunda mitad.
2. **Cierre con pregunta comentable** que interpele al oyente sobre SU situación (no un
   resumen, no una pregunta sobre el referente) — efecto EP.016: 7 comentarios.
3. **Checklist anti-repetición** (mismo estándar que MPD, ver
   `.claude/skills/mrputridsden/CLAUDE.md` §Reglas anti-repetición): presupuesto de
   muletillas, sin réplicas de pura validación, sin meta-transiciones, listas → una
   escena, lint final antes de entregar.

Espera a que el guión quede completo y aprobado por el usuario antes de seguir.

---

## Paso 3 — Generar prompts de artwork

Genera los prompts de portada (1:1, 9:16, 16:9) siguiendo el mismo patrón que ya usa
el pipeline más adelante para validar imágenes — reutiliza las reglas estándar de cada
show (sistema tipográfico propio, nunca mezclar — ver memoria
`feedback_mpd_vs_btq_typography`):

| Show | Referencia de reglas de prompt |
|---|---|
| BTQ | reglas vigentes en `.claude/skills/episode-launch/docs/brand-constants.md` (dirección de artwork CONGELADA: póster gráfico, siluetas a contraluz sobre dorado #C9A84C, footer fijo). El skill `btq-project` no existe (2026-06-26); brand-constants.md es la fuente real. Ejemplo aplicado: `btq-production/launch-assets/EP019-gladiator-artwork.md` |
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
