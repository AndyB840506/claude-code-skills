# Workflow: Quote Cards BTQ

Extrae los quotes más potentes del guión y genera prompts de imagen para cada uno.

---

## Step 1 — Extraer quotes del guión (orden de prioridad)

1. **Líneas [REMATE]** — siempre las más fuertes; standalone por diseño
2. **Línea de apertura del hook** — la que engancha antes de revelar el personaje
3. **Cierre de Mito o Realidad** — "La realidad es..."
4. **Mensaje directo del cierre** — el dirigido a agentes/supervisores
5. **Frase TM del personaje** — siempre incluir como última card

Evitar: datos estadísticos aislados, transiciones, líneas de setup. Cada quote debe funcionar solo sin contexto.

**Target: TODOS los REMATEs del guión** — no curar un subset. Extraer cada línea [REMATE] del guión completo y presentarlos todos al usuario. El usuario decide cuáles producir como cards — no Laswell.

Por qué: en EP.015 se generaron 6 cards curadas → usuario esperaba los 11 REMATEs del guión. El criterio editorial es del host, no del AI.

Flujo correcto:
1. Extraer TODOS los [REMATE] del guión en orden de aparición
2. Presentar tabla completa con segmento origen y potencial de engagement
3. Usuario confirma selección (o dice "todos")
4. Generar prompts para los confirmados

---

## Step 2 — Specs de la quote card

- Un quote por card — nunca combinar
- Texto grande, bold, alto contraste: off-white `#F5F2EC` sobre fondo oscuro
- Atribución abajo: **"— Andy · Behind the Queue · EP.0XX"** en gold `#C9A84C`
- Sin footer de íconos — usar "Behind the Queue · EP.0X" en gold bottom-center
- Fondo: derivado del artwork del episodio, oscurecido/blureado para legibilidad
- Formato: cuadrado 1:1, mínimo 1080×1080px

---

## Step 3 — Plantilla de prompt

> **División de responsabilidades:** Flow agent maneja el background visual (derivado del artwork del episodio). Laswell genera solo el quote + layout de texto.

```
[Background visual — generado por Flow agent desde artwork del episodio]

QUOTE (centered, large, bold, off-white #F5F2EC):
"[Texto del quote]"

Below quote: "— Andy · Behind the Queue · EP.0XX" — gold #C9A84C, smaller text.
Bottom center: "Behind the Queue · EP.0XX" — gold #C9A84C, small.

Format: square 1080×1080px.
```

---

## Step 4 — Entrega

Presentar quotes seleccionados en tabla antes de generar prompts:

| # | Quote | Segmento origen | Por qué funciona |
|---|---|---|---|
| 1 | "[quote]" | [REMATE] Seg. X | Standalone, punchy, shareable |
| 2 | "[quote]" | Hook | Curiosidad sin spoiler |
| 3 | "[quote]" | TM personaje | Cierre memorable |

Pedir confirmación de Andy antes de generar los prompts de imagen.

El quote del Día 2 del plan de redes (el más shareable) se elige de esta lista.
