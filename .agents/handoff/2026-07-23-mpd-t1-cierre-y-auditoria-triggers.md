# Handoff: MPD Temporada 1 clausurada + auditoría de solapamiento de triggers
**Date:** 2026-07-23 (jueves)
**Machine:** desktop (E:\)
**Status:** Complete — todo aplicado, verificado y respaldado

> Tercero de la sesión del 2026-07-23. Los otros dos:
> `2026-07-23-hiresignal-outreach-pendiente-fulfillment.md` (estado de HireSignal) y
> `2026-07-23-procedencia-causa-raiz.md` (la regla de entrada y por qué existe).

---

## 1 · Mr. Putrid's Den — Temporada 1 CLAUSURADA

**Decisión de Andrés:** el proyecto inicial de MPD queda cerrado. EP.001–EP.005 (era co-host
con Juan, temática rock/metal/jazz) es **archivo público intacto** — no se reabre, no se edita
retroactivamente, no se borra. De aquí en adelante **solo el modelo solo de Temporada 2**.

**Contradicción resuelta:** dos memorias decían cosas distintas — `rebrand_cruce_de_caminos`
("100% misterios y leyendas") vs `archivos_secretos_pillar` ("rotan con episodios anclados en
banda"). **Gana 100% misterios.** Los episodios de análisis de banda salen del roadmap.

**Excepción declarada: La Silla Pútrida sigue ABIERTA.** Si aparece un invitado, se hace el
episodio aunque no sea de misterios. Está escrita en 3 sitios a propósito (encabezado del
`CLAUDE.md` de la skill, el propio segmento, y la memoria del pilar) porque una sesión que
leyera solo la memoria habría concluido que estaba muerta.

**Muertos, NO pendientes:** los slots que existían por los contactos de Juan — entrevista a
artista emergente y spotlight de eventos underground. Se venían reportando como pendientes.

### Archivos tocados
| Archivo | Cambio |
|---|---|
| `memory/project_mpd_juan_departure.md` | 92 → 32 líneas, reencuadrado como "T1 clausurada" |
| `memory/project_mpd_archivos_secretos_pillar.md` | Quitada la rotación con banda; agregada la excepción de la Silla |
| `memory/project_mpd_rebrand_cruce_de_caminos.md` | T1 marcada como clausurada |
| `mrputridsden/podcast-profile.json` | `roadmap_9_episodes` marcado OBSOLETO; EP.8 y EP.9 CANCELADOS |
| `mrputridsden/CLAUDE.md` | Descripción del show → misterios y leyendas; Silla como excepción |
| `mrputridsden/SKILL.md` | Triggers a T2 (fuera `podcast metal`/`podcast rock`) |

**Hallazgo:** "ya hicimos los cambios correspondientes" era cierto casi por completo —
`roadmap-mpd.md` y todas las descripciones del JSON (tagline, corta, larga, Spotify 600) ya
estaban en T2 desde el 07-22. Faltaban solo dos huecos: `roadmap_9_episodes` y el `CLAUDE.md`.

## 2 · Auditoría de solapamiento de triggers (las 28 skills)

Script re-ejecutable en **`skill-management/scripts/audit-triggers.py`** — 5 tests. Enlazado
desde el checklist de `skill-management/SKILL.md`.

**Resultado tras los arreglos:** A) exactas 0 · B) contención 1 · C) casi-duplicados 1 ·
D) 1 aviso heurístico · E) 3 skills sin zona `Triggers:`.

- **Arreglado (riesgo alto):** `episode-launch` reclamaba 5 frases genéricas (`lanzar episodio`,
  `metadata episodio`, `portada episodio`...) siendo skill **exclusiva de BTQ**. Todas llevan
  BTQ ahora y la descripción manda a `episode-pipeline` para MPD/CCC.
- **Arreglado:** `mrputridsden` con triggers de T1 (`podcast metal`, `podcast rock`).
- **Aceptado a propósito:** `landing page` (ui-ux-pro-max) ⊂ `create landing page`
  (web-page-kit). Ambas hacen landing pages de verdad; se resolvió con texto desambiguador
  cruzado, igual que `handoff`/`session-close`. El script lo seguirá marcando: es esperado.
- **Aviso sin choque real:** `mrputridsden` con `misterios del rock` etc. — ninguna otra skill
  reclama esas frases hoy. Muerde solo si aparece un segundo show de misterios.

## 3 · Métrica de reproceso (primera corrida)

El chequeo nuevo del `retrospective` dio **4 artefactos reescritos tras darlos por buenos**,
de 6 inputs asumidos sin abrir su fuente. 3 de los 9 commits del día son correcciones propias.
Referencia para la próxima sesión: **si baja de 4, §Procedencia está sirviendo.**

## Notes / Gotchas

- Dos instrumentos sub-reportan **sin dar error** (quedaron en `skills/CLAUDE.md` § Debugging):
  `Measure-Object -Line` no cuenta líneas en blanco; `glob('**/…')` de Python omite carpetas con
  punto — leyó 18 de 28 skills y produjo un "cero colisiones" falso.
- El test de **coincidencia exacta no basta** para triggers: no veía el caso peor. Por eso el
  script tiene contención y casi-duplicados.
- `podcast-profile.json` se editó con la herramienta Edit y se validó con `json.load` después.
  No usar `Set-Content` sobre él (BOM).

## Next Steps

1. **NEEDS USER INPUT (Andrés + Hugo):** plan de fulfillment de HireSignal — sigue siendo el
   bloqueo que manda. Detalle en el handoff de HireSignal.
2. Al cerrar la próxima sesión, comparar el número de reprocesos contra el 4 de hoy.
3. Opcional: `frontend-design`, `retrospective` y `ui-ux-pro-max` no tienen zona `Triggers:`
   explícita — compiten con toda su prosa. No es un choque hoy, pero es el terreno donde
   aparecería el próximo.
