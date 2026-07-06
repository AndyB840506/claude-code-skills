# Workflow 03b — Material de marketing (Macro-Stage C)

Genera el material de lanzamiento que el usuario sube manualmente a redes: plan
social y quote cards estáticas. Reutiliza el artwork recién validado en Stage 3 como
base visual — por eso corre justo después y no antes.

**No reimplementa nada que ya exista** — invoca los workflows de cada show igual que
el resto del pipeline.

---

## Paso 1 — Plan social de 4 días

| Show | Cómo se genera |
|---|---|
| BTQ | Ya viene incluido en el output de `episode-launch` (Stage 2) — el plan social de 4 días (Jueves intriga / Sábado calentamiento / Domingo 8PM lanzamiento / Martes refuerzo) ya está generado. Fuente vigente de esta regla: `.claude/skills/episode-launch/workflows/step2-generate-assets.md` §B (`btq-project/SKILL.md` no existe en disco, confirmado 2026-06-26). **No regeneres nada aquí** — solo confírmalo y preséntalo de nuevo si el usuario lo necesita a mano. |
| MPD | Invoca `podcast-creator/workflows/04-social-media.md` — genera `social-ep[NNN].md` con copy por plataforma (cuando redes estén activas, ver `mrputridsden/CLAUDE.md`) |

---

## Paso 2 — Quote cards estáticas

**Imágenes estáticas, no animadas** — la animación fue lo que se descartó por costo de
tokens/iteraciones; iterar imágenes estáticas no tiene ese límite (confirmado por el
usuario).

| Show | Cómo se genera |
|---|---|
| BTQ | No hay un workflow compartido — cada episodio genera su sección "Quote Cards" inline dentro de `btq-production/launch-assets/EP0XX-*-launch.md` (ver EP019 como referencia reciente): extrae TODOS los `[REMATE]` del guion (no un subset curado — el usuario decide cuáles producir), genera prompts cuadrados 1:1 con specs de marca ya definidas (texto off-white sobre fondo derivado del artwork, atribución en gold) |
| MPD | Sigue el mismo patrón que BTQ — extrae las frases más fuertes del guion (priorizando las que cumplen la regla "autoexplicables sin contexto del episodio", ver memoria `mrputridsden_project` regla #4) y genera prompts cuadrados 1:1 con el sistema tipográfico propio de MPD (silver/crimson — ver memoria `feedback_mpd_vs_btq_typography`, nunca mezclar con BTQ). Sigue la misma estructura que BTQ (un quote por card, atribución, formato 1080×1080 mínimo) pero con el sistema visual de MPD |
| CCC | Ver `corporate-crime-confidential-production/quotecards-ep001.md` como referencia — extrae las líneas marcadas `[ÉNFASIS]` del guion (equivalente al `[REMATE]` de BTQ) y verifica cada una contra la transcripción real antes de generar (el guion puede tener líneas no grabadas). **Regla propia de CCC:** distinguir cita real documentada (atribuir por nombre a la persona real) de narración dramatizada en primera persona (atribuir al show, nunca a la persona real como si fuera cita literal) — ver `corporate-crime-confidential-production/guion-style-ccc.md` |

**Antes de generar los prompts**, pregunta si el usuario ya tiene quote cards de una
sesión previa para este episodio — todas, algunas, o ninguna (mismo patrón que Stage 3,
Paso 0 — el usuario puede ya haberlas creado junto con el artwork). Distingue dos
respuestas posibles y registra cada una por separado en la bitácora:
- **Ya las tiene** (todas o un set parcial que decide completar): pide las rutas,
  verifica con `Read` que cada archivo existe antes de continuar
- **Decide saltarse el paso por completo** (no quiere quote cards esta vez): no fuerces
  la generación — registra el skip explícito y continúa

Si no las tiene, presenta los prompts resultantes para que el usuario los genere en
Flow — **misma pausa estructural que Stage 3** (no existe API de generación de imágenes):

> "Prompts de quote cards listos para EP.0XX — [N] cards. Genera cada una en Flow y
> dime las rutas cuando estén listas."

⚠️ **Desactualizado para BTQ desde EP.020 (2026-07-05) — verificar antes de asumir que
esto sigue aplicando:** `.claude/skills/episode-launch/docs/brand-constants.md` §"Quote
Cards" documenta que, desde EP.020, las quote cards BTQ comparten el MISMO render
cinematográfico y el MISMO nivel de checklist que la portada (no un tratamiento aparte
más simple) — incluye patrones de fallo conocidos de Flow (reinserta el anillo dorado
genérico aunque el prompt pida otro fondo; autocorrige palabras sin tilde). Para BTQ,
corre el mismo subagent/chequeo de Stage 3 sobre las quote cards usando ese checklist —
no te saltes la validación asumiendo que el formato es "más simple". Para MPD, si su
sistema de quote cards no tiene un checklist equivalente documentado, sigue bastando con
la revisión visual rápida del usuario.

---

## Al terminar

1. Confirma: "Material de marketing listo para EP.0XX — plan social + [N] quote cards
   generadas." y continúa a `04-grid-rotation.md`.
2. Agrega a la bitácora:
   ```
   ## Stage 3b — Material de marketing
   - Qué se hizo: plan social confirmado/generado, quote cards generadas (BTQ: sección
     inline de `launch-assets/EP0XX-*-launch.md` | MPD: equivalente)
   - Archivos generados: [rutas — social-ep[NNN].md, prompts/imágenes de quote cards]
   - Resultado: OK
   ```
